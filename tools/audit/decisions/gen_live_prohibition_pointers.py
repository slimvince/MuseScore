#!/usr/bin/env python3
"""THE REVERSE POINTER FOR THE LIVE-PROHIBITION CLASS — from the register entry to the live
specification section that restates it as binding.

WHAT THIS ANSWERS.  The phase-1w verification (`OPEN_ITEMS.md` OI-302) found a class the LEGACY
mark cannot express: a decision whose SUBJECT is the dormant pipeline -- so the mark is right --
and which a LIVE `ARCHITECTURE.md` section at the same time restates as a standing do-not-retry
prohibition.  A reader who meets only the mark is told the subject is dormant and is NOT told the
rule still constrains what they may attempt.

The prohibition itself is published ONCE, in the specification (#6), and this tool does not copy
it.  What was missing is the reverse direction, and that is all this adds: a pointer from the
entry to the section, so the reader is one hop from the rule.

WHAT IT DOES NOT DO, both on the phase-1x dispatch's instruction and for a stated reason:
  * it adds NO new register field -- the pointer is appended to the entry's existing PROVENANCE
    part, which the register's own "How to read an entry" already defines as "where the status
    comes from, AND ANY LATER RULING THAT BEARS ON IT".  A live specification restating the
    decision as binding is exactly that;
  * it does NOT re-word the LEGACY marker, which the user weakened one wave earlier. A third
    revision of that wording in two waves is how a marker stops meaning anything.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  derived : WHICH entries are in the class, and which section each is restated in -- read from
            `phase1w_legacy_verification.json`, the artifact that measured it.  No identifier is
            listed in this file (D-431), so the class cannot silently disagree with the
            verification that found it.
  authored: the wording of the pointer sentence, and the three sections' quoted opening phrases.

WHY THE POINTER QUOTES THE LINE RATHER THAN ONLY NUMBERING IT.  A line number written into prose
is not a register anchor: `reaim_home_anchors.py` maintains the `home` anchors and nothing
maintains this one, so a number alone goes stale silently -- the failure `CLAUDE.md` rule (i)'s
own defense hit and had to be corrected for.  The pointer therefore carries the section's own
words, which stay findable after any insertion above them, and dates the line number as an
observation rather than asserting it as current.

Run:
    python tools/audit/decisions/gen_live_prohibition_pointers.py          # apply, then regenerate
    python tools/audit/decisions/gen_live_prohibition_pointers.py --check  # verify, write nothing
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
VERIFICATION = os.path.join(HERE, "phase1w_legacy_verification.json")
ARCHITECTURE = os.path.join(ROOT, "ARCHITECTURE.md")

sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

CLASS = "live-prohibition-in-spec"

# The do-not-retry lines, by the words they open with. The line numbers are DERIVED below by
# locating these phrases, never typed -- so a moved line re-aims itself and a reworded one STOPS.
# The third field is the DATE THE LINE NUMBER WAS OBSERVED, which the pointer states as an
# observation rather than as a current fact (see the docstring). It is per section because the
# sections were not all added on the same day, and a single hard-coded date would make the pointer
# for a later-added section say something untrue.
#
# ADDED 2026-08-09: the declared mode's weight, with the OI-354 verdict set (user, Ruling 23 of
# `cowork_rulings_2026_08_09_fourth_stop.md`). D-572 entered the derived class in that act and this
# tool STOPPED, correctly, because its authored table held no line listing that entry -- authoring
# the row for a member the derived cut DID reach is what the tool requires. NOTE THE CONSTRUCTION
# DIFFERENCE, which is why the opening phrase is the one below rather than the heading words: this
# prohibition is written over two lines, and the identifiers sit on the SECOND. The opening phrase
# must therefore be taken from the line that carries the identifier, because that is the line this
# tool reads them off.
SECTIONS = [
    ("the chord layer", "**Tried and closed on the chord layer — do not retry;", "2026-08-03"),
    ("the key layer", "**Tried and closed on this layer — do not retry;", "2026-08-03"),
    ("the search", "*Tried and closed on the search — do not retry;", "2026-08-03"),
    ("the declared mode's weight",
     "— do not retry; the register carries it with its evidence: D-572", "2026-08-09"),
]

MARKER = "**A LIVE specification section restates this as binding:**"


class Stop(Exception):
    """A premise this tool rests on is not true at the tree. Never a warning."""


def locate_sections() -> list[dict]:
    """Find each do-not-retry line, and read the entry identifiers it actually lists."""
    lines = open(ARCHITECTURE, encoding="utf-8", errors="replace").read().splitlines()
    found = []
    for label, opening, observed in SECTIONS:
        hits = [(i, ln) for i, ln in enumerate(lines, 1) if opening in ln]
        if len(hits) != 1:
            raise Stop(f"the do-not-retry line for {label} is not uniquely locatable in "
                       f"ARCHITECTURE.md ({len(hits)} match(es)) — it was moved or reworded, and "
                       f"the pointer must not be written against a phrase that no longer exists")
        line_no, text = hits[0]
        ids = sorted({tok.strip(".,;:*_`)") for tok in text.replace("(", " ").split()
                      if tok.strip(".,;:*_`)").startswith("D-")})
        found.append({"label": label, "line": line_no, "ids": ids, "text": text,
                      "observed": observed})
    return found


def pointer_for(sections: list[str], lines: list[int], phrases: list[str],
                observed: list[str]) -> str:
    where = "; ".join(f"{s} (at line {n} on {o}), under *\"{p}\"*"
                      for s, n, p, o in zip(sections, lines, phrases, observed))
    return (f" {MARKER} `ARCHITECTURE.md` — {where}. The LEGACY mark above says this decision's "
            f"SUBJECT is dormant; what is named there says the prohibition still constrains what "
            f"a future design may attempt, and the two are not the same claim. Pointer only — "
            f"the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.")


def apply(backbone: dict, members: dict, located: list[dict]) -> list[str]:
    by_id = {d["id"]: d for d in backbone["decisions"]}
    touched = []
    for did in sorted(members):
        d = by_id.get(did)
        if d is None:
            raise Stop(f"the verification names {did}, which the register does not carry")
        hits = [s for s in located if did in s["ids"]]
        if not hits:
            raise Stop(f"{did} is in the {CLASS} class but no located do-not-retry line lists it")
        src = d["status_source"]
        # Idempotent: a second run must not append a second copy.
        if MARKER in src:
            src = src.split(f" {MARKER}")[0]
        d["status_source"] = src + pointer_for(
            [h["label"] for h in hits],
            [h["line"] for h in hits],
            [h["text"].strip("*> ").split(";")[0] for h in hits],
            [h["observed"] for h in hits],
        )
        touched.append(did)
    return touched


def members_from_verification() -> set[str]:
    def walk(o):
        if isinstance(o, dict):
            if o.get("transfer") == CLASS and o.get("id"):
                yield o["id"]
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)
    return set(walk(json.load(open(VERIFICATION, encoding="utf-8"))))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = ap.parse_args(argv)

    raw = open(BACKBONE, encoding="utf-8").read()
    backbone = json.loads(raw)

    # The same establishment step gen_home_classification.py uses: this tool rewrites the whole
    # file, so its serialization must be a fixed point of the committed formatting, or the first
    # run buries the real change in a whole-file reformat.
    if json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n" != raw:
        print("REFUSED: re-serializing the untouched backbone is not byte-identical to the "
              "committed file, so writing would reformat it.")
        return 2

    located = locate_sections()
    members = members_from_verification()
    touched = apply(backbone, members, located)

    text = json.dumps(backbone, indent=2, ensure_ascii=False) + "\n"

    for s in located:
        print(f"  {s['label']}: ARCHITECTURE.md:{s['line']} lists {len(s['ids'])} entry(ies)")
    print(f"class members (derived from the verification): {len(members)}")

    if args.check:
        if text != raw:
            print(f"STALE vs the files: {len(touched)} entry(ies) do not carry the pointer as "
                  "derived")
            return 1
        print("every live-prohibition entry carries its pointer, as derived")
        return 0

    open(BACKBONE, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote backbone_decisions.json: pointer on {len(touched)} entry(ies)")
    print("now regenerate: python tools/audit/decisions/gen_decisions_register.py")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
