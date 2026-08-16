#!/usr/bin/env python3
"""EVERY VALUE THE RULED SOFT-DISCARD MOVED IN THE TWO DERIVED CENSUSES, ENUMERATED AND CLASSED.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §6 kind 3 of
`cowork_rulings_2026_08_16_preparation_return.md`: the two derived censuses
(`gen_artifact_inventory_surface.py`, `gen_retirement_caller_check.py`) *"regenerate under the
bound WIDENED BY ONE NAMED CATEGORY — citation-carried standing (the document's naming in the
governing record sat inside a retired entry's own text) beside the ruled class standing and home
standing; every moved value enumerated and classed; movement outside all three a STOP."*

WHAT MOVES, AND WHY IT MOVES AT ALL.  Both censuses split their population by a CITATION SCAN over
the governing record — `CLAUDE.md`, `ARCHITECTURE.md`, `BUILD_AND_TEST.md`, `DECISIONS.md`,
`OPEN_ITEMS.md`, `STATUS.md`, `DEFECT_TYPES.md`, and the two registers' detail directories.  The
decisions register's INDEX and group files are RENDERED from its data, so retiring an entry removes
that entry's text from the governing record — and any document whose only naming was inside that
text crosses from the cited side to the uncited one.  Nothing else about the censuses moves.

★ WHAT CROSSING TO THE UNCITED SIDE DOES AND DOES NOT DO.  It makes a document a retirement
CANDIDATE and nothing more.  Every ruled condition on a candidacy stands untouched — mined first,
members seen by the user first for the stray root files, and the caller-check at the objects — so a
crossing changes a derived census and never a fate.  The ruling says so in terms.

THE THREE CATEGORIES, and how each is decided from the record rather than judged:
  * CLASS STANDING — the moved value's subject is a discard-population entry.  A census over FILES
    carries no entry-keyed value, so this category is expected to be empty here; it is computed
    rather than assumed absent, and a member would be reported.
  * HOME STANDING — the file is the home document of at least one RETIRED entry and of no LIVE
    entry.  The register's own home field decides it.
  * CITATION-CARRIED STANDING — the file's name appears in the rendered text of at least one
    RETIRED entry and nowhere else in the governing record as it now stands.  This is the category
    the ruling WIDENED the bound by, and it exists because the fourth batch measured a movement the
    two ruled categories could not explain.

THE STOPS:
  * a moved value none of the three categories reaches is a STOP-and-report — the ruling's own
    instruction, and the reason this tool exists rather than a paragraph in a report;
  * a value that moved in the direction NOBODY expected — a file entering the cited side — is a
    STOP, because the discard only ever removes text from the governing record;
  * a census whose citation scan cannot be read at either side is a STOP.

Run:
  python tools/audit/gen_census_movement_classification.py
  python tools/audit/gen_census_movement_classification.py --check
"""
from __future__ import annotations

import argparse
import json
import posixpath
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_artifact_inventory_surface as census                    # noqa: E402  (path set above)

OUT = HERE / "census_movement_classification.json"
BACKBONE = "tools/audit/decisions/backbone_decisions.json"

# The commit the censuses last re-derived at BEFORE this act — the state the movement is measured
# against.  It is the parent of the discard commit, and it is named here rather than resolved from
# a branch tip: a branch read is not trusted for what is current (D-253), and the comparison must
# be against one fixed state whatever else moves.
BEFORE_COMMIT = "b73d1c7b4e9dd8ced52dd92522977f272dcb718e"
BEFORE_COMMIT_IS = ("the commit before the ruled soft-discard was applied — Task 0 of "
                    "`cc_instruction_preparation_fifth.md`, at which both censuses re-derived "
                    "clean")

CLASS_STANDING = "class-standing"
HOME_STANDING = "home-standing"
CITATION_CARRIED = "citation-carried-standing"


class Stop(Exception):
    """A moved value outside the ruled bound. Never a warning, never a movement glossed."""


def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def governing_text_at(commit: str) -> str:
    """The governing record AS IT STOOD at a commit, from the git objects.

    The document and directory list is IMPORTED from the census that owns the scan (#6), so the
    two cannot disagree about what the governing record is.
    """
    chunks = []
    for name in census.GOVERNING_DOCUMENTS:
        chunks.append(git("show", f"{commit}:{name}"))
    listing = git("ls-tree", "-r", "--name-only", commit).split("\n")
    for directory in census.GOVERNING_DIRECTORIES:
        for path in sorted(p.strip().strip('"') for p in listing if p.strip()):
            if path.startswith(f"{directory}/") and path.endswith(".md"):
                chunks.append(git("show", f"{commit}:{path}"))
    return "\n".join(chunks)


def entry_text(entry: dict) -> str:
    """One register entry's own recorded text — the fields the register renders from."""
    return " ".join(str(entry.get(f, "")) for f in
                    ("title", "verbatim", "plain", "rationale", "home", "status_source",
                     "superseded_by"))


def build() -> dict:
    before_names = census.cited_names(governing_text_at(BEFORE_COMMIT))
    after_text, sources = census.governing_text()
    after_names = census.cited_names(after_text)

    left = sorted(before_names - after_names)
    entered = sorted(after_names - before_names)
    if entered:
        raise Stop(f"names ENTERED the governing record's citation scan: {entered}. The ruled "
                   f"discard only ever removes an entry's text from the rendered register, so a "
                   f"name arriving is a movement this act cannot explain.")

    data = json.loads((ROOT / BACKBONE).read_text(encoding="utf-8"))
    live = data["decisions"]
    retired = [r["the_entry"] for r in data.get("retired_entries", {}).get("entries", [])]
    if not retired:
        raise Stop("the decisions register's data file carries no retired-entries block, so there "
                   "is no movement for this classification to be about")

    live_homes = {e["home"].split(":")[0].replace("\\", "/") for e in live}
    retired_homes: dict[str, list[str]] = {}
    for e in retired:
        retired_homes.setdefault(e["home"].split(":")[0].replace("\\", "/"), []).append(e["id"])
    retired_ids = {e["id"] for e in retired}

    rows, unclassed = [], []
    for name in left:
        homing = sorted({ids for doc, entries in retired_homes.items()
                         if posixpath.basename(doc) == name and doc not in live_homes
                         for ids in entries})
        naming = sorted({e["id"] for e in retired if name in entry_text(e)})

        if name in retired_ids:
            category, evidence = CLASS_STANDING, {"the_moved_value_is_itself_a_retired_entry": name}
        elif homing:
            category = HOME_STANDING
            evidence = {"the_retired_entries_it_homed": homing,
                        "and_it_homes_no_live_entry": True}
        elif naming:
            category = CITATION_CARRIED
            evidence = {"the_retired_entries_whose_own_text_named_it": naming,
                        "and_the_governing_record_now_names_it_nowhere_else": True}
        else:
            category, evidence = None, {}
            unclassed.append(name)
        rows.append({"the_moved_value": name,
                     "the_movement": "left the CITED side of the citation split; it is now on the "
                                     "UNCITED side, which is the retirement-CANDIDATE side",
                     "the_category": category, "the_evidence": evidence})

    if unclassed:
        raise Stop(f"moved values that none of the three ruled categories reaches: {unclassed}. "
                   f"The ruling's instruction on any other movement is a STOP-and-report; this "
                   f"tool does not widen the bound on its own authority.")

    by_category: dict[str, int] = {}
    for row in rows:
        by_category[row["the_category"]] = by_category.get(row["the_category"], 0) + 1

    return {
        "what_this_is":
            "EVERY VALUE THE RULED SOFT-DISCARD MOVED IN THE TWO DERIVED CENSUSES, enumerated and "
            "classed against the three categories the user's ruling of 2026-08-16 §6 (kind 3) "
            "bounds the act with. A movement outside all three halts this tool.",
        "generator": "tools/audit/gen_census_movement_classification.py",
        "dispatch": "cc_instruction_preparation_fifth.md, Task 1",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §6 (kind 3)",
            "the_bound_quoted": (
                "regenerate under the bound WIDENED BY ONE NAMED CATEGORY — citation-carried "
                "standing (the document's naming in the governing record sat inside a retired "
                "entry's own text) beside the ruled class standing and home standing; every moved "
                "value enumerated and classed; movement outside all three a STOP; a census "
                "crossing confers candidacy only — every ruled condition on candidacies stands "
                "untouched"),
        },
        "the_two_states_compared": {
            "before": BEFORE_COMMIT,
            "what_that_commit_is": BEFORE_COMMIT_IS,
            "after": "the working tree, at which the censuses are regenerated by this act",
            "★_how_the_comparison_is_made":
                "the CITATION SCAN itself is re-run over the governing record at both states — the "
                "earlier one read from the git objects — rather than the rendered surfaces being "
                "diffed. The scan and the governing-record definition are IMPORTED from the census "
                "that owns them (#6), so this classification and that census cannot disagree about "
                "what counts as a naming.",
        },
        "the_governing_record_scanned": {
            "documents": list(census.GOVERNING_DOCUMENTS),
            "directories": [f"{d}/**/*.md" for d in census.GOVERNING_DIRECTORIES],
            "sources_reported_by_the_census_at_the_current_state": sources,
        },
        "★_what_a_crossing_confers":
            "CANDIDACY ONLY. The uncited side is the retirement-candidate side of a derived "
            "census; every ruled condition on a candidacy — mined first, members seen by the user "
            "first for the stray root files, the caller-check at the objects — stands untouched, "
            "and nothing is archived, moved or deleted by any value below.",
        "★_what_this_classification_does_NOT_assert":
            "That a moved document is worth retiring, or that it is not depended on. The citation "
            "scan sees the governing record only; a reference from anywhere else is invisible to "
            "it, which is the standing bound the census publishes of itself.",
        "the_tally": {
            "values_that_moved": len(rows),
            "values_that_entered": len(entered),
            "by_category": dict(sorted(by_category.items())),
        },
        "the_moved_values": rows,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the classification and report whether the artifact matches")
    args = ap.parse_args(argv)

    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: the census movement classification does not re-derive")
            return 1
        print("the census movement classification re-derives, and every moved value is inside the "
              "ruled bound")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    data = json.loads(text)
    print("wrote", OUT.relative_to(ROOT).as_posix())
    print(f"  moved: {data['the_tally']['values_that_moved']}")
    for category, count in data["the_tally"]["by_category"].items():
        print(f"    {category}: {count}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
