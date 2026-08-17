#!/usr/bin/env python3
"""THE FRAMEWORK PHASE'S UNTRUSTED CANDIDATES — the carry the residue sitting ordered, DERIVED.

THE RULINGS THIS EXISTS FOR.  User, 2026-08-17, `cowork_rulings_2026_08_17_residue_sitting.md`:

  * **Ruling 1** — *"All 29 ride the soft-discard, and each is carried into the framework phase's
    candidate enumeration as an UNTRUSTED CANDIDATE, never as a decision."*
  * **Ruling 3** — *"The sole-carrier guard applies as it applied before: the one `deferred`
    member, D-069, is carried into the framework phase's candidate enumeration as an untrusted
    candidate exactly as Ruling 1 carries the 29"* — *"(making the carried candidate population 30,
    derived — not typed — at execution)."*

★ WHAT AN UNTRUSTED CANDIDATE IS, AND WHY THE CARRY EXISTS AT ALL.  The sole-carrier guard was
proposed and accepted at the soft-discard sitting to answer the user's own question — whether the
discard risks losing *"a genuinely good idea that should have been used as input when designing
and/or building the inferrers"*.  The three structural nets the answer named (the disposition
discipline over every specification statement, the audit's something-missing verdict, the
fact-gate) miss exactly ONE class: an idea whose SOLE CARRIER is the register entry, typically a
deferred proposal that was never implemented.  This file is that class, published so the framework
phase's candidate enumeration meets it.

  A member here is **NOT a decision**, is **NOT authority for anything**, and carries **no
  provenance** — that is precisely what the retirement found.  It is a statement the record holds
  whose deciding act nobody could name, offered to a later design as raw material to be judged on
  its merits.  The retirement itself is *"a provenance verdict, not a judgment on soundness or
  usefulness; the statement stands at its home and is met by the derivation."*

WHAT IS DERIVED AND WHAT IS AUTHORED.

  DERIVED   the whole population: the entries the recovery pass returned NOTHING-FOUND for that the
            sole-carrier guard also marks SOLE-CARRIER (Ruling 1's 29), plus the sole-carrier
            member among the ratified-document check's SUBJECT-NOT-FOUND-THERE entries (Ruling 3's
            carry).  Never typed.
  DERIVED   every member's title, restatement, recorded home and status, read from the decisions
            register's own data file — LIVE or RETIRED, so this file re-derives identically before
            and after the retirement that made them candidates.
  AUTHORED  nothing about membership.  The sitting each member came from is attached from the
            derivation that placed it, not chosen.

THE STOPS, so the carry cannot silently stop being the carry:
  * a missing input artifact STOPS it;
  * a population other than the one the ruling states STOPS it — the ruling fixes the number and
    says in terms that it is derived rather than typed, so a derivation that produces another
    number has drifted from the ruling and is not adjusted to fit;
  * a member the decisions register's data file holds in NEITHER its live entries nor its retired
    block STOPS it — a candidate whose entry cannot be read is not published with blank fields;
  * a member carried by both rulings at once STOPS it.

Run:
  python tools/audit/gen_framework_untrusted_candidates.py
  python tools/audit/gen_framework_untrusted_candidates.py --check
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "decisions"))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import apply_soft_discard as first                                 # noqa: E402  the shared shape (#6)
import apply_residue_discard as residue                            # noqa: E402  the same populations (#6)

OUT = HERE / "framework_untrusted_candidates.json"

# The population the ruling fixes, and which it says in terms is DERIVED rather than typed. The
# number is here as a STOP on the derivation, never as its source.
RULED_POPULATION = 30

RULING = "cowork_rulings_2026_08_17_residue_sitting.md"
BY_RULING_1 = "Ruling 1 of " + RULING + " — one of the 29 withheld sole-carriers"
BY_RULING_3 = ("Ruling 3 of " + RULING + " — the sole-carrier member among the nine "
               "SUBJECT-NOT-FOUND-THERE entries, carried exactly as Ruling 1 carries the 29")


class Stop(Exception):
    """A demand of the carry is unmet. Never a warning, never a candidate published blank."""


def load(path: Path, what: str) -> dict:
    if not path.exists():
        raise Stop(f"{what} is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build() -> dict:
    recovery = load(residue.RECOVERY, "the committed recovery artifact")
    guard = load(residue.GUARD, "the committed sole-carrier artifact")
    checked = load(residue.CHECK, "the committed ratified-document check")
    backbone = load(residue.BACKBONE, "the decisions register's data file")

    nothing_found = {r["id"] for r in recovery["entries"] if r["result"] == first.NOTHING_FOUND}
    sole_carriers = {r["id"] for r in guard["entries"] if r["verdict"] == first.SOLE_CARRIER}
    not_found_there = {r["id"] for r in checked["entries"]
                       if r["result"] == residue.NOT_FOUND_THERE}

    by_ruling_1 = sorted(nothing_found & sole_carriers)
    by_ruling_3 = sorted(not_found_there & sole_carriers)
    overlap = sorted(set(by_ruling_1) & set(by_ruling_3))
    if overlap:
        raise Stop(f"{overlap} would be carried by both rulings at once — the two populations are "
                   f"meant to be disjoint and this derivation does not choose between them")

    # The entry is read wherever the register holds it: live, or in the retired block. That is what
    # makes this file re-derive identically before and after the retirement.
    entries = {e["id"]: (e, "live in the decisions register") for e in backbone["decisions"]}
    block = backbone.get(first.RETIRED_BLOCK) or {"entries": []}
    for record in block["entries"]:
        entries[record["the_entry"]["id"]] = (record["the_entry"],
                                              "retired from the decisions register")
    by_guard = {r["id"]: r for r in guard["entries"]}

    members = []
    for ident, carried_by in ([(i, BY_RULING_1) for i in by_ruling_1]
                              + [(i, BY_RULING_3) for i in by_ruling_3]):
        if ident not in entries:
            raise Stop(f"{ident} is a carried candidate but the decisions register's data file "
                       f"holds it in neither its live entries nor its retired block — a candidate "
                       f"whose entry cannot be read is not published with blank fields")
        entry, where = entries[ident]
        row = by_guard[ident]
        members.append({
            "id": ident,
            "the_title_the_register_gives_it": entry["title"],
            "the_restatement_the_register_gives_it": entry.get("plain"),
            "the_home_the_register_records": entry["home"],
            "the_status_the_register_records": entry["status"],
            "where_the_register_holds_it_now": where,
            "carried_by": carried_by,
            "why_the_guard_marked_it_a_sole_carrier": row["why_this_verdict"],
            "the_signals_that_fired": row["the_signals_that_fired"],
        })

    if len(members) != RULED_POPULATION:
        raise Stop(f"the derivation carries {len(members)} candidate(s) where the ruling states "
                   f"{RULED_POPULATION} — the derivation and the ruling have drifted apart, which "
                   f"is a STOP rather than an adjustment")

    return {
        "what_this_is":
            "THE FRAMEWORK PHASE'S UNTRUSTED CANDIDATES — the register entries the sole-carrier "
            "guard identified and the residue sitting ordered carried into the framework phase's "
            "candidate enumeration when it retired them. A member here is NOT a decision, NOT "
            "authority for anything, and carries NO provenance: that is what the retirement found. "
            "It is raw material for a later design to judge on its merits. Every field is read "
            "from a committed artifact; none is transcribed (D-431).",
        "generator": "tools/audit/gen_framework_untrusted_candidates.py",
        "dispatch": "cc_instruction_preparation_eighth.md, Task 2",
        "the_rulings_that_ordered_the_carry": {
            "source": RULING,
            "Ruling_1": "All 29 ride the soft-discard, and each is carried into the framework "
                        "phase's candidate enumeration as an UNTRUSTED CANDIDATE, never as a "
                        "decision.",
            "Ruling_3": "The sole-carrier guard applies as it applied before: the one `deferred` "
                        "member, D-069, is carried into the framework phase's candidate "
                        "enumeration as an untrusted candidate exactly as Ruling 1 carries the 29 "
                        "(making the carried candidate population 30, derived — not typed — at "
                        "execution).",
        },
        "★_why_this_class_exists_at_all":
            "The sole-carrier guard was proposed and accepted at the soft-discard sitting to "
            "answer the user's own question — whether the discard risks losing a genuinely good "
            "idea that should have been used as input when designing or building the inferrers. "
            "The three structural nets named in the answer (the disposition discipline over every "
            "specification statement, the audit's something-missing verdict, the fact-gate) miss "
            "exactly ONE class: an idea whose SOLE CARRIER is the register entry, typically a "
            "deferred proposal that was never implemented. This file is that class.",
        "★_how_the_population_is_derived_rather_than_listed": {
            "Ruling_1's_29": "the entries the deciding-act recovery pass returned NOTHING-FOUND "
                             "for that the sole-carrier guard also marks SOLE-CARRIER",
            "Ruling_3's_carry": "the sole-carrier member among the ratified-document check's "
                                "SUBJECT-NOT-FOUND-THERE entries",
            "the_entry_fields": "read from the decisions register's own data file, LIVE or "
                                "RETIRED — which is what makes this file re-derive identically "
                                "before and after the retirement that made them candidates",
            "the_STOP": f"a derived population other than {RULED_POPULATION} halts this tool "
                        f"rather than being adjusted, and a hand edit to the artifact fails "
                        f"`--check` on the next run",
        },
        "★_what_a_member_of_this_list_is_NOT":
            "It is not a decision, not authority, and not a finding that the statement is good. "
            "The retirement that produced it is a PROVENANCE verdict — 'not a judgment on "
            "soundness or usefulness; the statement stands at its home and is met by the "
            "derivation' — so a framework-phase reader judges each on its merits and cites the "
            "home document, never this file, if any of it is adopted.",
        "the_population": {
            "carried_by_Ruling_1": len(by_ruling_1),
            "carried_by_Ruling_3": len(by_ruling_3),
            "the_total": len(members),
            "the_total_the_ruling_states": RULED_POPULATION,
            "it_reconciles": len(members) == RULED_POPULATION,
        },
        "the_candidates": members,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the carry and report whether the artifact matches")
    args = ap.parse_args(argv)

    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: the framework phase's untrusted-candidate carry does not re-derive")
            return 1
        print("the framework phase's untrusted-candidate carry re-derives")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    data = json.loads(text)
    pop = data["the_population"]
    print("wrote", OUT.relative_to(ROOT).as_posix())
    print(f"  {pop['the_total']} untrusted candidate(s): {pop['carried_by_Ruling_1']} by Ruling 1, "
          f"{pop['carried_by_Ruling_3']} by Ruling 3")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
