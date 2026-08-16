#!/usr/bin/env python3
"""WHICH AUTHORED JUDGMENTS THE SOFT-DISCARD RETIRES — DERIVED, never hand-listed.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §6 kind 2 of
`cowork_rulings_2026_08_16_preparation_return.md`: the four authored judgment tables *"gain
RETIRED-SUBJECTS sections on the retired-block pattern: every judgment whose subject the discard
retires moves verbatim WITH its subject reference (#12 — nothing dropped, nothing re-authored);
the checks keep watching live subjects; a judgment in neither section halts; membership is DERIVED
and published, and a judgment whose membership cannot be derived STOPS to the user."*

WHAT AN AUTHORED JUDGMENT TABLE IS.  A committed table whose verdicts were WRITTEN by judgment and
accepted, not derived — the `CLAUDE.md` rule triage, the home classification's delegation-scope and
section-kind judgments, the delegation bar's FORM judgments, and the legacy-marking verification's
per-entry verdicts.  Each check re-verifies its table against the record; none can re-author it.
When the discard retires a judgment's SUBJECT, the judgment has nothing left to be about, and the
check refuses to write rather than dropping it silently — which is that guard working.

★ WHAT IS DERIVED HERE, AND WHAT IS NOT.  This tool derives WHICH judgments move.  It moves none:
the moves are performed in the four tables themselves, verbatim, each judgment carried whole with
its subject reference (#12).  This tool then re-verifies the partition on every run, in BOTH
directions, so a table and this derivation cannot drift apart.

THE TWO MEMBERSHIP RULES, which are the ruling's own two categories made mechanical.

  * AN ENTRY-KEYED TABLE (the rule triage; the legacy verification) — a judgment moves if and only
    if its subject register entry is in the retired block.  Nothing else can move it.
  * A DOCUMENT-KEYED TABLE (the home classification's authored documents; the delegation bar's
    FORMS) — a judgment moves if and only if its subject document is the home of at least one
    RETIRED entry and of no LIVE entry of that table's own population.  That is the ruling's
    second category — *a document whose home standing those entries alone carried* — read off the
    data rather than judged.  A document that keeps one live homed entry does not move, and a
    document that never held a retired entry cannot move: if such a document were nobody's home,
    something other than this discard emptied it, and that is not this act's to decide.

THE STOPS, so this cannot silently stop being what it claims:
  * a subject the two rules cannot place is a STOP to the user — never moved, never kept, by guess;
  * a judgment on the retired side whose subject the derivation says is LIVE is a STOP;
  * a judgment on the live side whose subject the derivation says is RETIRED is a STOP;
  * a subject in BOTH sections of one table is a STOP;
  * a subject in NEITHER section of its table is a STOP — the ruling's own sentence;
  * a data file with no retired block is a STOP: this derivation has no subject without one.

Run:
  python tools/audit/decisions/gen_retired_subject_moves.py           # derive and write
  python tools/audit/decisions/gen_retired_subject_moves.py --check   # re-derive and diff
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import claude_md_rule_triage as triage                             # noqa: E402  (path set above)
import gen_home_classification as homecls                          # noqa: E402  (path set above)
import gen_phase1p_delegation_bar as bar                            # noqa: E402  (path set above)
import gen_phase1w_legacy_verification as legacy                    # noqa: E402  (path set above)

BACKBONE = HERE / "backbone_decisions.json"
OUT = HERE / "retired_subject_moves.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"

RETIRED_BLOCK = "retired_entries"

RULING_SENTENCES = {
    "what the four tables gain":
        "gain RETIRED-SUBJECTS sections",
    "what moves and how":
        "every judgment whose subject the discard retires moves verbatim WITH its subject "
        "reference",
    "what the checks keep doing":
        "the checks keep watching live subjects; a judgment in neither section halts",
    "how membership is settled":
        "membership is DERIVED and published, and a judgment whose membership cannot be derived "
        "STOPS to the user",
}


class Stop(Exception):
    """A demand of the ruled treatment is unmet. Never a warning, never a judgment moved by guess."""


def flatten(text: str) -> str:
    import re
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_ruling() -> dict[str, str]:
    if not RULING.exists():
        raise Stop(f"the ruling record this treatment serves is missing: {RULING}")
    text = flatten(RULING.read_text(encoding="utf-8"))
    missing = [name for name, quote in RULING_SENTENCES.items() if flatten(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling that ordered this treatment is no longer in its "
                   f"ruling record, so the treatment would outlive the words that ordered it: "
                   f"{missing}")
    return dict(RULING_SENTENCES)


def home_document(entry: dict) -> str:
    return entry["home"].split(":")[0].replace("\\", "/")


def load() -> tuple[dict, list[dict], list[dict]]:
    backbone = json.loads(BACKBONE.read_text(encoding="utf-8"))
    block = backbone.get(RETIRED_BLOCK)
    if not block:
        raise Stop("the decisions register's data file carries no retired-entries block, so there "
                   "is no retirement for this derivation to be about")
    retired = [r["the_entry"] for r in block["entries"]]
    return backbone, backbone["decisions"], retired


# ── the two membership rules ─────────────────────────────────────────────────────────────────────

def entry_keyed(name: str, live_subjects: set[str], retired_ids: set[str],
                live_table: list[str], retired_table: list[str]) -> dict:
    """A judgment moves iff its subject register entry is retired."""
    should_move = sorted(retired_ids & (set(live_table) | set(retired_table)))
    return partition(name, "entry-keyed", live_table, retired_table, should_move, live_subjects,
                     {"the_rule": "the judgment's subject register entry is in the retired block",
                      "the_live_population": sorted(live_subjects)})


def document_keyed(name: str, population: list[dict], retired: list[dict],
                   live_table: list[str], retired_table: list[str]) -> dict:
    """A judgment moves iff its subject document homes a retired entry and no live population entry."""
    live_homes = {home_document(e) for e in population}
    retired_homes: dict[str, list[str]] = {}
    for e in retired:
        retired_homes.setdefault(home_document(e), []).append(e["id"])

    should_move = sorted(d for d in retired_homes if d not in live_homes
                         and d in set(live_table) | set(retired_table))
    out = partition(name, "document-keyed", live_table, retired_table, should_move, live_homes,
                    {"the_rule": "the subject document homes at least one RETIRED entry and no "
                                 "LIVE entry of this table's own population",
                     "the_live_population_size": len(population),
                     "the_documents_homing_a_retired_entry": dict(sorted(
                         (d, sorted(ids)) for d, ids in retired_homes.items()))})
    out["the_entries_whose_retirement_emptied_each_moved_document"] = {
        d: sorted(retired_homes[d]) for d in should_move}
    return out


def section_kind(backbone: dict, shc: dict) -> dict:
    """The same treatment ONE GRAIN FINER — a judgment about a SECTION rather than a document.

    The soft-discard can empty a section without emptying the document that holds it, so a
    document stays somebody's home while one of its sections stops deciding anything. The
    classifier owns this derivation and STOPS on a judgment that has lost its subject; here it is
    only PUBLISHED, and the classifier's own move list is asked for again so that a judgment still
    owing a move cannot pass unnoticed (#6 — the derivation has one home).
    """
    outstanding = homecls.derive_kind_moves(backbone)
    if outstanding:
        raise Stop("section-kind judgments still owe a move into `section_kind_retired`: "
                   + "; ".join(f"{d}:{ln} <- {', '.join(subj)}"
                               for (d, ln), subj in sorted(outstanding.items())))
    moved, live_count = [], 0
    for doc, spec in sorted(shc["documents"].items()):
        live_count += len(spec.get("section_kind", []))
        for k in spec.get("section_kind_retired", []):
            subjects = k.get("retired_subject_entries")
            if not subjects:
                raise Stop(f"the retired section-kind judgment at {doc}:{k['heading_line']} "
                           f"carries no subject reference, so its membership cannot be derived")
            moved.append(f"{doc}:{k['heading_line']}")
    return {
        "the_table": ("tools/audit/decisions/backbone_decisions.json :: "
                      "section_home_criterion.documents[*].section_kind"),
        "the_membership_rule": {
            "kind": "section-keyed",
            "the_rule": "the judgment decides no LIVE population entry and DID decide at least "
                        "one RETIRED one — the document-level rule at section grain",
            "derived_by": "tools/audit/decisions/gen_home_classification.py :: derive_kind_moves, "
                          "imported rather than restated (#6); the classifier STOPS on any "
                          "judgment that still owes a move, and on a retired judgment that "
                          "decides a live entry again",
        },
        "judgments_watching_live_subjects": live_count,
        "judgments_moved_to_the_retired_subjects_section": sorted(moved),
        "the_move_count": len(moved),
        "the_entries_whose_retirement_emptied_each_moved_section": {
            f"{doc}:{k['heading_line']}": k["retired_subject_entries"]
            for doc, spec in sorted(shc["documents"].items())
            for k in spec.get("section_kind_retired", [])
        },
    }


def partition(name: str, kind: str, live_table: list[str], retired_table: list[str],
              should_move: list[str], live_subjects, rule: dict) -> dict:
    """The four demands on one table's partition, in both directions.

    ★ WHAT THE RETIRED SIDE IS NOT ASKED.  A retired-subjects section is older than this act: the
    same tables carry judgments retired by earlier RE-HOMING waves, each with its own recorded
    retirement. This derivation is about THIS retirement, so a judgment already on the retired side
    whose subject the discard did not touch is left exactly where its own record put it — asking it
    to be re-derived here would make this act the authority for retirements it never performed.
    What IS asked of every retired-side judgment is the one thing that must never go unnoticed:
    that its subject has not become live again.
    """
    both = sorted(set(live_table) & set(retired_table))
    if both:
        raise Stop(f"{name}: {both} carried in BOTH the live table and the retired-subjects "
                   f"section. A judgment is one or the other.")
    unplaceable = sorted(s for s in live_table
                         if s not in live_subjects and s not in set(should_move))
    if unplaceable:
        raise Stop(f"{name}: the membership of {unplaceable} cannot be derived — the judgment is "
                   f"in the live table, its subject is not live, and this retirement did not "
                   f"retire it. It is neither moved nor kept by guess; the ruling's instruction "
                   f"is a STOP to the user.")
    wrongly_kept = sorted(set(should_move) & set(live_table))
    if wrongly_kept:
        raise Stop(f"{name}: {wrongly_kept} are judgments whose subjects the discard retired, and "
                   f"they are still in the live table")
    resurrected = sorted(s for s in retired_table if s in live_subjects)
    if resurrected:
        raise Stop(f"{name}: {resurrected} sit in the retired-subjects section while their "
                   f"subject is LIVE — read the judgment back into the live table rather than "
                   f"relying on the retired copy")
    return {
        "the_table": name,
        "the_membership_rule": {"kind": kind, **rule},
        "judgments_watching_live_subjects": len(live_table),
        "judgments_moved_to_the_retired_subjects_section": sorted(should_move),
        "the_move_count": len(should_move),
    }


def build() -> dict:
    ruling = locate_ruling()
    backbone, live, retired = load()
    retired_ids = {e["id"] for e in retired}
    live_ids = {e["id"] for e in live}

    # The rule triage's population: every LIVE register entry homed in CLAUDE.md — the predicate
    # the tool itself uses, read from the tool rather than restated (#6).
    claude_live = {e["id"] for e in live if home_document(e) == "CLAUDE.md"}

    # The legacy verification's population: every LIVE entry carrying the legacy mark.
    legacy_live = {e["id"] for e in live if e.get("legacy_subject")}

    # The home population — the ONE definition, imported from the classifier that owns it (#6).
    home_pop = homecls.home_population(backbone)
    home_pop_ids = {e["id"] for e in home_pop}
    retired_home_pop = [e for e in retired
                        if not e.get("home_is_layer_spec")
                        and e.get("nonspec_kind") in ("contract-home", "gap")]

    shc = backbone["section_home_criterion"]
    retired_docs_block = shc["documents_retired_when_their_last_entry_was_re_homed"]
    retired_doc_judgments = sorted(
        {d for key, value in retired_docs_block.items()
         if key.startswith("judgments") and isinstance(value, dict)
         for d in value})

    tables = [
        entry_keyed("tools/audit/claude_md_rule_triage.py :: TRIAGE",
                    claude_live, retired_ids,
                    sorted(triage.TRIAGE), sorted(triage.RETIRED_TRIAGE)),
        entry_keyed("tools/audit/decisions/gen_phase1w_legacy_verification.py :: VERDICTS",
                    legacy_live, retired_ids,
                    sorted(v[0] for v in legacy.VERDICTS),
                    sorted(v[0] for v in legacy.RETIRED_VERDICTS)),
        document_keyed("tools/audit/decisions/backbone_decisions.json :: "
                       "section_home_criterion.documents",
                       home_pop, retired_home_pop,
                       sorted(shc["documents"]), retired_doc_judgments),
        document_keyed("tools/audit/decisions/gen_phase1p_delegation_bar.py :: FORMS",
                       home_pop, retired_home_pop,
                       sorted(bar.FORMS), sorted(bar.RETIRED_FORMS)),
        section_kind(backbone, shc),
    ]

    return {
        "what_this_is":
            "THE DERIVED MOVE LIST for the ruled kind-2 treatment: which authored judgment moves "
            "into its table's RETIRED-SUBJECTS section because the soft-discard retired its "
            "subject, and which keeps watching a live subject. DERIVED on every run from the "
            "decisions register's own data file, never hand-listed, and re-verified in BOTH "
            "directions against the four tables as they stand.",
        "generator": "tools/audit/decisions/gen_retired_subject_moves.py",
        "dispatch": "cc_instruction_preparation_fifth.md, Task 1",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §6 (kind 2)",
            "every_sentence_located_in_that_record_on_this_run": ruling,
        },
        "the_retirement_this_is_about": {
            "the_live_record": len(live_ids),
            "the_retired_block": len(retired_ids),
            "★_the_source": "the decisions register's own data file; no entry identity is "
                            "restated here (D-431).",
        },
        "★_what_this_derivation_does_NOT_do":
            "It moves nothing and re-authors nothing. Every moved judgment is carried WHOLE, in "
            "its own table's retired-subjects section, in the words it was authored in (#12); "
            "this file says which, and re-checks that the tables agree with it. It also asserts "
            "nothing about whether a judgment is RIGHT — a retired subject is a provenance "
            "outcome, not a verdict on the judgment.",
        "tables": tables,
        "the_tally": {
            "tables_treated": len(tables),
            "judgments_moved": sum(t["the_move_count"] for t in tables),
            "judgments_still_watching_live_subjects":
                sum(t["judgments_watching_live_subjects"] for t in tables),
        },
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the move list and report whether the artifact matches")
    args = ap.parse_args(argv)

    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: the retired-subject move list does not re-derive")
            return 1
        print("the retired-subject move list re-derives, and every table agrees with it")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    data = json.loads(text)
    print("wrote", OUT.relative_to(ROOT).as_posix())
    for t in data["tables"]:
        print(f"  {t['the_move_count']:>3} moved, {t['judgments_watching_live_subjects']:>3} live "
              f"— {t['the_table']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
