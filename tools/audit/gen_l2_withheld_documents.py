#!/usr/bin/env python3
"""DERIVE THE HOME DOCUMENTS OF L2's IN ENTRIES — PRINTED FOR THE USER, AUTHORED INTO NOTHING.

WHY THIS EXISTS.  Ruling 6 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` orders the
pack-build dispatch to DERIVE the set of home documents of the ruled L2 verdict table's IN
entries, to PRINT it, and to STOP for the user's confirmation before any of it is authored into
`WITHHELD["l2"]["withheld_documents"]`.  This tool is the derivation half and nothing else.

WHAT IT IS NOT.  It authors nothing.  A document's presence in this artifact is not a judgment
that it should be withheld — that judgment is the user's, and Ruling 6 reserves it (D-661, #24).
It writes nothing into `WITHHELD`, `EXTRAS`, `VERDICTS` or `CRITERION`, renders no pack and
writes no pack directory.

WHERE IT READS FROM, AND FROM NOWHERE ELSE.

  the verdict table : `gen_derivation_boot_pack.VERDICTS["l2"]`, with that module's own
                      `VERDICT_IN` token.  The identity list is NOT re-authored here — one path
                      per concern (#6), and a copied list is a transcription (D-431).  Importing
                      that module executes its module level, which defines its tables; its
                      `main()` sits under an `if __name__ == "__main__":` guard and does not run
                      on import.  Nothing here calls `build()`, `build_subject()` or `main()`.
  the homes         : `tools/audit/decisions/backbone_decisions.json`, assembled EXACTLY as
                      `pack.build()` assembles it — the decisions array keyed by id, then each
                      retired entry's `the_entry` added under its own id where it carries a
                      truthy id AND that id is not already present.  Both guards, in that order,
                      so the two derivations cannot disagree.

HOW A DOCUMENT IS TAKEN FROM A HOME, stated mechanically so that no judgment enters: the home is
the entry's `"home"` string; the document is the substring BEFORE the first `:`, with surrounding
whitespace stripped; and it must then match `^[^\\s:]+\\.md$`.  Nothing is guessed and no home is
repaired.

THE FOUR STOPS, each ending the run:
  1. an IN identity the backbone does not carry;
  2. a home absent, empty, or whose leading token does not match the pattern;
  3. either direction of the reconciliation failing;
  4. the IN count is not 111 — Ruling 6 names "the 111 IN entries", and §4 of
     `cowork_rulings_2026_09_05_l2_withheld_family_sitting.md` records the ruled family as 111 IN,
     133 OUT, 0 UNPLACED.  A different count means the verdict table has moved since the user
     ruled it, and this derivation must not run over a family he did not rule.

Run:
    python tools/audit/gen_l2_withheld_documents.py           # write the artifact, print the list
    python tools/audit/gen_l2_withheld_documents.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "l2_withheld_documents.json")
BACKBONE = os.path.join(HERE, "decisions", "backbone_decisions.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_derivation_boot_pack as pack          # noqa: E402  (path set above)

SUBJECT = "l2"
RULED_IN_COUNT = 111

# The document half of a home string: everything before the first `:`, and it must be a bare
# relative path ending `.md` with no whitespace and no second colon in it.
DOCUMENT = re.compile(r"^[^\s:]+\.md$")

RULING_6 = (
    "The pack-build dispatch derives, from the register's data file "
    "(`tools/audit/decisions/backbone_decisions.json`) and the ruled verdict table, the set of "
    "home documents of the 111 IN entries; prints it; and **STOPs for the user's confirmation "
    "before the set is authored into `WITHHELD[\"l2\"][\"withheld_documents\"]`**, each with its "
    "finding, date and reason. The pilot's one withheld document is not restated for L2 — it "
    "enters, if at all, as a member of the derived set."
)


class Stop(Exception):
    """An identity has no entry, a home cannot be read, a count moved, or a side fails to close."""


def entry_number(identity: str) -> tuple[int, int, str]:
    """Sort key: by entry number where the identity carries one, and never by accident."""
    m = re.search(r"(\d+)", identity)
    return (0, int(m.group(1)), identity) if m else (1, 0, identity)


def read_backbone() -> dict:
    """Assembled EXACTLY as `pack.build()` assembles it — both guards, in that order."""
    with open(BACKBONE, encoding="utf-8") as fh:
        data = json.load(fh)
    backbone = {d["id"]: d for d in data.get("decisions", [])}
    for r in data.get("retired_entries", {}).get("entries", []):
        e = r.get("the_entry", {})
        if e.get("id") and e["id"] not in backbone:
            backbone[e["id"]] = e
    return backbone


def document_of(identity: str, entry: dict) -> str:
    home = entry.get("home")
    if not isinstance(home, str) or not home.strip():
        raise Stop(f"{identity}: its home is absent or empty (home={home!r})")
    doc = home.split(":", 1)[0].strip()
    if not DOCUMENT.match(doc):
        raise Stop(f"{identity}: the leading token of its home is not a document path "
                   f"(home={home!r}, leading token={doc!r})")
    return doc


def derive() -> dict:
    table = pack.VERDICTS[SUBJECT]
    in_entries = sorted((i for i, v in table.items() if v[0] == pack.VERDICT_IN),
                        key=entry_number)

    # STOP 4 — the ruled family, before anything is derived over it.
    if len(in_entries) != RULED_IN_COUNT:
        raise Stop(f"the verdict table grades {len(in_entries)} entries IN; the user ruled "
                   f"{RULED_IN_COUNT}. The table has moved since he ruled it, and this "
                   f"derivation must not run over a family he did not rule.")

    backbone = read_backbone()

    # STOP 1 — an IN identity the backbone does not carry.
    absent = [i for i in in_entries if i not in backbone]
    if absent:
        raise Stop(f"IN identity/identities the register's data file does not carry: {absent}")

    # STOP 2 rides inside `document_of`.
    by_document: dict[str, list[str]] = {}
    for identity in in_entries:
        by_document.setdefault(document_of(identity, backbone[identity]), []).append(identity)

    documents = [
        {"document": doc,
         "in_entries_homed_here": sorted(ids, key=entry_number),
         "how_many": len(ids)}
        for doc, ids in sorted(by_document.items())
    ]
    per_document_sum = sum(d["how_many"] for d in documents)

    # STOP 3 — both directions, before the artifact exists.
    accounted: dict[str, int] = {}
    for d in documents:
        for identity in d["in_entries_homed_here"]:
            accounted[identity] = accounted.get(identity, 0) + 1
    not_once = sorted((i for i in in_entries if accounted.get(i, 0) != 1), key=entry_number)
    if not_once:
        raise Stop(f"IN identity/identities not accounted to exactly one document: {not_once}")
    unnamed = [d["document"] for d in documents if d["how_many"] < 1]
    if unnamed:
        raise Stop(f"listed document(s) named by no IN identity: {unnamed}")
    if per_document_sum != len(in_entries):
        raise Stop(f"the per-document identity counts sum to {per_document_sum}, and there are "
                   f"{len(in_entries)} IN entries")

    return {
        "what_this_is":
            "The set of home documents of the entries the ruled L2 verdict table grades IN, "
            "derived under Ruling 6 of "
            "`records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md`, printed "
            "for the user's confirmation and authored into nothing.",
        "generator": "tools/audit/gen_l2_withheld_documents.py",
        "the_ruling_it_executes": {
            "ruling": "Ruling 6 of "
                      "`records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md`",
            "verbatim": RULING_6,
        },
        "where_it_reads_from": {
            "the_verdict_table": "gen_derivation_boot_pack.VERDICTS[\"l2\"], with that module's "
                                 "own VERDICT_IN token. The identity list is not re-authored "
                                 "here (#6, D-431).",
            "the_homes": "tools/audit/decisions/backbone_decisions.json, assembled exactly as "
                         "gen_derivation_boot_pack.build() assembles it — the decisions array "
                         "keyed by id, then each retired entry's `the_entry` added under its own "
                         "id where it carries a truthy id and that id is not already present.",
            "how_a_document_is_taken_from_a_home":
                "the substring before the first `:` in the entry's `home` string, whitespace "
                "stripped, which must then match `^[^\\s:]+\\.md$`. A home that is absent, empty "
                "or whose leading token does not match STOPS the run, naming the entry and its "
                "home string. Nothing is guessed and no home is repaired.",
        },
        "in_entries": in_entries,
        "documents": documents,
        "counted": {
            "in_entries": len(in_entries),
            "documents": len(documents),
            "sum_of_the_per_document_identity_counts": per_document_sum,
        },
        "★_the_reconciliation_taken_in_both_directions": {
            "every_IN_identity_accounted_to_exactly_one_document": True,
            "every_listed_document_named_by_at_least_one_IN_identity": True,
            "the_sum_of_the_per_document_counts_equals_the_IN_count": True,
            "a_failure_of_either_direction_is_a_STOP_not_a_field":
                "Each of the three is proved before this artifact is built; a failure raises and "
                "ends the run, so a `true` here is a record of a check that passed and never a "
                "claim made in place of one.",
        },
        "★_the_bound": {
            "what_this_derivation_reaches":
                "The entries of the ruled L2 verdict table and nothing wider. An entry the table "
                "does not grade is not reached, whatever its subject.",
            "what_a_document's_presence_here_is_not":
                "It is NOT a judgment that the document should be withheld. That judgment is the "
                "user's, and Ruling 6 reserves it: the set is printed and STOPs for his "
                "confirmation before anything is authored (D-661, #24).",
            "what_this_run_authored": "Nothing. No `WITHHELD`, no `EXTRAS`, no `VERDICTS`, no "
                                      "`CRITERION`, no pack directory.",
        },
    }


def main(argv: list[str]) -> int:
    artifact = derive()
    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"

    if "--check" in argv:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE: the L2 withheld-document derivation does not re-derive")
            return 1
        print("the L2 withheld-document derivation re-derives")
        return 0

    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    for d in artifact["documents"]:
        print(f"  {d['document']}  ({d['how_many']})")
    print(f"{artifact['counted']['in_entries']} IN entr(ies) homed in "
          f"{artifact['counted']['documents']} document(s)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
