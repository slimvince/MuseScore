#!/usr/bin/env python3
"""THE RESIDUE SITTING'S DISCARDS, CARRIES AND KEEPS — planned, applied, and afterwards re-checked.

THE RULINGS THIS EXISTS FOR.  User, 2026-08-17, `cowork_rulings_2026_08_17_residue_sitting.md`:

  * **Ruling 1** — *"All 29 ride the soft-discard, and each is carried into the framework phase's
    candidate enumeration as an UNTRUSTED CANDIDATE, never as a decision."*  The 29 are the
    sole-carrier members the guard withheld from the first discard.
  * **Ruling 2** — *"A ratification of a document reaches the decisions that document carries."*
    All 47 SUBJECT-IN-RATIFIED-DOCUMENT entries join the keep side, each with its deciding act
    recorded as the document-ratification act the check located.
  * **Ruling 3** — the nine SUBJECT-NOT-FOUND-THERE entries *"join the soft-discard under the same
    provisions as the 194"*, and the guard applies as before: their one `deferred` member is
    carried into the candidate enumeration exactly as Ruling 1 carries the 29.
  * **Ruling 4** — *"The six stay on the keep side on the recovery pass's original quoted acts."*

★ WHAT A SOFT-DISCARD IS, AND WHAT IT IS NOT — the first discard's own words, and the user's.
Retired from the live record, **not destroyed** (#12), and individually revivable the moment a
deciding act is named.  Every retired record carries the ruled clause verbatim: *"a provenance
verdict, not a judgment on soundness or usefulness; the statement stands at its home and is met by
the derivation."*  The statement each retired entry records still stands at its home document; what
is retired is the decisions register's claim to be the AUTHORITY for it.

★ WHY THIS IS A SEPARATE TOOL FROM `apply_soft_discard.py`, AND NOT A WIDENING OF IT.  That tool's
own STOP says it: *"the data file already carries a retired-entries block. This act adds one;
retiring a second population is a separate act with its own ruling."*  This IS that separate act,
with that separate ruling.  Everything the two share — the ruled clause, the retired-record shape,
the (B1) import, the stamp shape — is IMPORTED from it rather than restated (#6).

★ THE ONE THING THE RECORDS MUST NOT BLUR.  The retired block now holds TWO retirements.  Each
record already carries its own `retired_on`, `retired_by` and `the_retiring_authority`, so which act
retired which entry is readable per record; the block's own header gains an `acts` list saying the
same thing at the block level, and the first act's header statement is preserved verbatim (#12).

THE THREE INVOCATIONS.
    --plan    (the default)  derive the populations and PUBLISH what would change, writing no
                             register file at all.
    --apply                  perform the retirement and the fifty-three provenance stamps.
    --check                  re-verify the applied state, including the sitting's own arithmetic.

THE STOPS, so this cannot silently stop being what it claims:
  * a missing input artifact, or one carrying no population, STOPS it;
  * a discard population member the data file does not carry live STOPS it (D-671);
  * a member of the 29 that is also one of the 9, or a keep that is also a discard, STOPS it;
  * the nine carrying any number of sole-carrier members other than the one Ruling 3 names STOPS it;
  * the sitting's own arithmetic not reconciling — keep 474, retired 203, total 677 — STOPS it, and
    the ruling says so in terms: *"A derivation that does not reconcile to these sums is a
    STOP-and-report, not an adjustment."*
  * a keep with no act to record STOPS it — the ruling gives each keep its act, so an entry with
    none is not stamped with a blank;
  * a sentence of the ruling that ordered this act no longer in its ruling record STOPS it.

Run:
  python tools/audit/decisions/apply_residue_discard.py            # plan only, writes no register file
  python tools/audit/decisions/apply_residue_discard.py --apply    # perform it
  python tools/audit/decisions/apply_residue_discard.py --check    # re-verify the applied state
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import apply_soft_discard as first                                 # noqa: E402  the shared shape (#6)
from gen_live_prohibition_pointers import MARKER as LIVE_PROHIBITION_MARKER   # noqa: E402  (#6)

BACKBONE = HERE / "backbone_decisions.json"
RECOVERY = ROOT / "tools" / "audit" / "deciding_act_recovery.json"
GUARD = ROOT / "tools" / "audit" / "sole_carrier_subclass.json"
CHECK = ROOT / "tools" / "audit" / "ratified_document_check.json"
FILTER = ROOT / "tools" / "audit" / "decisions_filter_classification.json"
RULING = ROOT / "cowork_rulings_2026_08_17_residue_sitting.md"
PLAN = ROOT / "tools" / "audit" / "residue_discard_application.json"

RETIRED_BLOCK = first.RETIRED_BLOCK
RULED_CLAUSE = first.RULED_CLAUSE                                  # imported, never retyped (#6)

IN_RATIFIED = "SUBJECT-IN-RATIFIED-DOCUMENT"
NOT_FOUND_THERE = "SUBJECT-NOT-FOUND-THERE"
NO_RATIFICATION = "NO-DOCUMENT-RATIFICATION-ACT"

RETIRED_ON = "2026-08-17"
RETIRING_ACT = ("CC, `cc_instruction_preparation_eighth.md` Task 2, on the user's rulings of "
                "2026-08-17 (the residue sitting: Ruling 1 the 29, Ruling 3 the 9)")
AUTHORITY = "cowork_rulings_2026_08_17_residue_sitting.md §§1 and 3"
KEEP_AUTHORITY_47 = "cowork_rulings_2026_08_17_residue_sitting.md §2 (Ruling 2)"
KEEP_AUTHORITY_6 = "cowork_rulings_2026_08_17_residue_sitting.md §4 (Ruling 4)"

# The sums the sitting itself states, and which it makes a STOP rather than an adjustment.
RULED_KEEP_SIDE = 474
RULED_RETIRED = 203
RULED_TOTAL = 677

RULING_SENTENCES = {
    "what happens to the 29":
        "All 29 ride the soft-discard, and each is carried into the framework phase's candidate "
        "enumeration as an UNTRUSTED CANDIDATE, never as a decision.",
    "what a discard record must carry": RULED_CLAUSE,
    "what happens to the 47":
        "A ratification of a document reaches the decisions that document carries.",
    "what happens to the 9":
        "join the soft-discard under the same provisions as the 194",
    "the guard that survives for the nine":
        "the one `deferred` member, D-069, is carried into the framework phase's candidate "
        "enumeration as an untrusted candidate exactly as Ruling 1 carries the 29",
    "what happens to the 6":
        "The six stay on the keep side on the recovery pass's original quoted acts.",
    "the arithmetic is a STOP":
        "A derivation that does not reconcile to these sums is a STOP-and-report, not an "
        "adjustment.",
}


class Stop(Exception):
    """A demand of the act is unmet. Never a warning, never an entry quietly moved."""


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flatten(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_ruling() -> dict[str, str]:
    if not RULING.exists():
        raise Stop(f"the ruling record this act serves is missing: {RULING}")
    text = flatten(RULING.read_text(encoding="utf-8"))
    missing = [name for name, quote in RULING_SENTENCES.items() if flatten(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling that ordered this act is no longer in its ruling "
                   f"record, so the act would outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


def load(path: Path, what: str) -> dict:
    if not path.exists():
        raise Stop(f"{what} is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def populations() -> dict:
    """Every population this act touches, DERIVED from the committed artifacts and never listed."""
    recovery = load(RECOVERY, "the committed recovery artifact")
    guard = load(GUARD, "the committed sole-carrier artifact")
    checked = load(CHECK, "the committed ratified-document check")
    backbone = load(BACKBONE, "the decisions register's data file")

    nothing_found = {row["id"] for row in recovery["entries"]
                     if row["result"] == first.NOTHING_FOUND}
    sole_carriers = {row["id"] for row in guard["entries"] if row["verdict"] == first.SOLE_CARRIER}
    withheld = sorted(nothing_found & sole_carriers)
    if not withheld:
        raise Stop("the sole-carrier artifact withholds nothing from the first discard, so Ruling "
                   "1 has no population — the import is not what this act assumes it is")

    by_result: dict[str, list[str]] = {}
    for row in checked["entries"]:
        by_result.setdefault(row["result"], []).append(row["id"])
    not_found = sorted(by_result.get(NOT_FOUND_THERE, []))
    in_ratified = sorted(by_result.get(IN_RATIFIED, []))
    no_ratification = sorted(by_result.get(NO_RATIFICATION, []))
    if not not_found or not in_ratified or not no_ratification:
        raise Stop("the ratified-document check does not carry all three of its results, so this "
                   "act's populations cannot be derived from it")

    overlap = sorted(set(withheld) & set(not_found))
    if overlap:
        raise Stop(f"{overlap} are in BOTH Ruling 1's population and Ruling 3's — the two "
                   f"populations are meant to be disjoint and this act does not choose between "
                   f"them")

    discard = sorted(set(withheld) | set(not_found))
    keeps = sorted(set(in_ratified) | set(no_ratification))
    collision = sorted(set(discard) & set(keeps))
    if collision:
        raise Stop(f"{collision} would be retired AND stamped as kept in the same act")

    # Ruling 3's own guard, DERIVED rather than typed: the sole-carrier member among the nine is
    # carried into the framework phase's candidate enumeration beside the 29.
    carried_from_the_nine = sorted(set(not_found) & sole_carriers)
    if len(carried_from_the_nine) != 1:
        raise Stop(f"the nine carry {len(carried_from_the_nine)} sole-carrier member(s) "
                   f"{carried_from_the_nine} where Ruling 3 names exactly one — the derivation and "
                   f"the ruling have drifted apart, which is a STOP rather than an adjustment")

    live_ids = {e["id"] for e in backbone["decisions"]}
    absent = sorted(i for i in discard + keeps if i not in live_ids)
    if absent:
        raise Stop(f"this act names {absent}, which the decisions register's data file does not "
                   f"carry live — the two records disagree about the population and this act does "
                   f"not choose between them (D-671)")

    return {
        "recovery": recovery, "guard": guard, "checked": checked, "backbone": backbone,
        "the_29_withheld_sole_carriers": withheld,
        "the_9_subject_not_found_there": not_found,
        "the_47_subject_in_ratified_document": in_ratified,
        "the_6_no_document_ratification_act": no_ratification,
        "the_discard_population": discard,
        "the_keep_population": keeps,
        "the_untrusted_candidates_carried_from_the_nine": carried_from_the_nine,
    }


def stamp_47(row: dict) -> str:
    """The provenance stamp for one Ruling-2 keep: the document-ratification act the check located."""
    matches = row.get("the_subject_matches_found_in_ratified_documents") or []
    if not matches:
        raise Stop(f"{row['id']} is a Ruling-2 keep but the check artifact records no subject "
                   f"match, so there is nothing to record as its deciding act")
    match = matches[0]
    return (" ★ THE DECIDING ACT RECORDED AND KEPT (user's ruling of 2026-08-17, "
            f"{KEEP_AUTHORITY_47} — a ratification of a document reaches the decisions that "
            f"document carries): the recovered act ratifies `{match['the_ratified_document']}`, "
            f"and that document carries this entry's own subject recogniser "
            f"{match['what_matched_the_subject']} at line {match['at_line']}, reading — "
            f"\"{match['the_passage_quoted']}\" The match is quoted from "
            "`tools/audit/ratified_document_check.json`; no other field of this entry is touched.")


def stamp_6(row: dict) -> str:
    """The provenance stamp for one Ruling-4 keep: the recovery pass's ORIGINAL quoted act.

    The shape is the first discard's own (B1) stamp, imported rather than restated (#6) — the same
    evidence from the same artifact — with this ruling's authority and its own reason attached.
    """
    if not row["acts"]:
        raise Stop(f"{row['id']} is a Ruling-4 keep but the recovery artifact records no act for "
                   f"it, so there is nothing to record as its deciding act")
    act = row["acts"][0]
    return (" ★ THE DECIDING ACT KEPT ON THE RECOVERY PASS'S ORIGINAL EVIDENCE (user's ruling of "
            f"2026-08-17, {KEEP_AUTHORITY_6}): the tested document-ratification shape is not "
            "present for this entry, so the recovery pass's evidence stands exactly as it stood. "
            f"A passage at `{act['document']}` line {act['line']}, carrying "
            f"{', '.join(act['the_user_act_markers_the_passage_carries'])} and matching "
            f"{act['what_matched_the_subject']}, reads — \"{act['the_act_quoted']}\" The act is "
            "quoted from `tools/audit/deciding_act_recovery.json`; no other field of this entry is "
            "touched.")


def stamped(status_source: str, stamp: str) -> str:
    """Append the stamp to a provenance field WITHOUT displacing the live-prohibition pointer.

    ★ WHY THIS IS NOT A PLAIN APPEND, and why the marker is imported rather than retyped (#6).
    `gen_live_prohibition_pointers.py` appends a pointer to the same field and keeps itself
    idempotent by TRUNCATING the field at its own marker and re-appending — which assumes its
    pointer is the last thing there. A stamp appended after it would be silently deleted by that
    tool's next run, and its `--check` reports the disagreement immediately, which is how this was
    found rather than reasoned about. So a stamp goes BEFORE that marker where the field carries
    one, leaving the other tool's invariant exactly as it was.
    """
    at = status_source.find(f" {LIVE_PROHIBITION_MARKER}")
    if at == -1:
        return status_source + stamp
    return status_source[:at] + stamp + status_source[at:]


def retired_record(entry: dict, why: str, finding: str, reason: str) -> dict:
    return {
        "the_entry": entry,
        "retired_on": RETIRED_ON,
        "retired_by": RETIRING_ACT,
        "the_retiring_authority": AUTHORITY,
        "the_finding": finding,
        "the_reason": reason,
        "which_ruling_of_the_sitting_retired_it": why,
        "the_ruled_clause_verbatim": RULED_CLAUSE,
        "★_what_this_retirement_is_not":
            "It is NOT a finding that the decision is wrong, unsound or unwanted, and it is NOT a "
            "deletion. The statement this entry records STANDS AT ITS HOME and is met by the "
            "derivation, exactly as the ruled clause above says.",
        "how_it_is_revived":
            "By naming a deciding act for it. The entry is moved back into `decisions` unchanged; "
            "nothing has to be re-authored, because nothing was destroyed (#12).",
    }


def records_for(pop: dict) -> dict[str, dict]:
    """One retired record per member of this act's discard population, with its own finding."""
    by_recovery = {row["id"]: row for row in pop["recovery"]["entries"]}
    by_guard = {row["id"]: row for row in pop["guard"]["entries"]}
    by_check = {row["id"]: row for row in pop["checked"]["entries"]}
    by_entry = {e["id"]: e for e in pop["backbone"]["decisions"]}

    out: dict[str, dict] = {}
    for i in pop["the_29_withheld_sole_carriers"]:
        signals = by_guard[i]["the_signals_that_fired"]
        out[i] = retired_record(
            by_entry[i],
            "Ruling 1 — the 29 withheld sole-carriers ride the soft-discard",
            f"{by_recovery[i]['result']} at the deciding-act recovery pass; "
            f"{first.SOLE_CARRIER} at the sole-carrier guard, on the signal(s) {signals}",
            "No deciding act could be named for this entry from its own recorded fields, and none "
            "could be recovered from the documents the entry itself cites. The sole-carrier guard "
            "WITHHELD it from the first discard and returned it to the user; the user ruled that "
            "it rides the discard, and that it is carried into the framework phase's candidate "
            "enumeration as an UNTRUSTED CANDIDATE — never as a decision. The carry is published "
            "at `tools/audit/framework_untrusted_candidates.json`.")
    for i in pop["the_9_subject_not_found_there"]:
        row = by_check[i]
        docs = sorted({m["the_ratified_document"]
                       for a in row["acts"] for m in a.get("the_documents_searched", [])
                       if m.get("located")})
        out[i] = retired_record(
            by_entry[i],
            "Ruling 3 — the 9 SUBJECT-NOT-FOUND-THERE join the soft-discard",
            f"{NOT_FOUND_THERE} at the ratified-document check; the recovered act ratifies a "
            f"document, that document was located and searched, and no recogniser of this entry "
            f"matches in it. Documents searched: {docs}",
            "The ratified-document check removed the only recovered evidence, so this entry "
            "stands as NOTHING-FOUND in substance and joins the soft-discard under the same "
            "provisions as the 194 — byte-preserving, revivable, its statement standing at its "
            "home.")
    return out


def the_arithmetic(pop: dict, applied: bool) -> dict:
    """The sitting's own sums, reconciled in both directions. A disagreement is a STOP."""
    backbone = pop["backbone"]
    block = backbone.get(RETIRED_BLOCK)
    already_retired = len(block["entries"]) if block else 0
    live_now = len(backbone["decisions"])
    discard = len(pop["the_discard_population"])

    live_after = live_now if applied else live_now - discard
    retired_after = already_retired if applied else already_retired + discard

    filt = load(FILTER, "the committed decisions-register filter classification")
    confirmed = filt["the_distribution"]["DECIDING-ACT-NAMED"]
    b1 = first.b1_keeps({row["id"] for row in pop["recovery"]["entries"]
                         if row["result"] == "ACT-FOUND"})
    keep_side = (confirmed + len(b1) + len(pop["the_47_subject_in_ratified_document"])
                 + len(pop["the_6_no_document_ratification_act"]))

    before = block["the_population_before_this_retirement"] if block else live_now
    out = {
        "★_the_ruling_makes_this_a_STOP_rather_than_an_adjustment":
            RULING_SENTENCES["the arithmetic is a STOP"],
        "the_keep_side": {
            "the_ratified_confirmed_side_at_the_filter": confirmed,
            "the_ten_B1_keeps": len(b1),
            "the_47_SUBJECT_IN_RATIFIED_DOCUMENT": len(pop["the_47_subject_in_ratified_document"]),
            "the_6_NO_DOCUMENT_RATIFICATION_ACT": len(pop["the_6_no_document_ratification_act"]),
            "the_sum": keep_side,
            "the_sum_the_sitting_states": RULED_KEEP_SIDE,
            "it_reconciles": keep_side == RULED_KEEP_SIDE,
        },
        "the_retired_side": {
            "retired_by_the_first_discard": already_retired if applied else already_retired,
            "the_29_withheld_sole_carriers": len(pop["the_29_withheld_sole_carriers"]),
            "the_9_SUBJECT_NOT_FOUND_THERE": len(pop["the_9_subject_not_found_there"]),
            "the_sum": retired_after,
            "the_sum_the_sitting_states": RULED_RETIRED,
            "it_reconciles": retired_after == RULED_RETIRED,
        },
        "the_whole_population": {
            "keep_plus_retired": keep_side + retired_after,
            "the_sum_the_sitting_states": RULED_TOTAL,
            "the_population_the_data_file_records_before_any_retirement": before,
            "it_reconciles": keep_side + retired_after == RULED_TOTAL == before,
        },
        "the_live_record": {
            "before_this_act": live_now if not applied else live_now + discard,
            "after_this_act": live_after,
            "the_movement_the_sitting_states": "512 → 474",
            "it_reconciles": live_after == RULED_KEEP_SIDE,
        },
    }
    if applied:
        out["the_retired_side"]["retired_by_the_first_discard"] = already_retired - discard
    failed = [k for k, v in out.items() if isinstance(v, dict) and v.get("it_reconciles") is False]
    if failed:
        raise Stop(f"the sitting's arithmetic does not reconcile at {failed}: "
                   f"{json.dumps({k: out[k] for k in failed}, ensure_ascii=False)} — the ruling "
                   f"makes this a STOP-and-report, not an adjustment")
    return out


def build_plan(applied: bool = False) -> dict:
    ruling = locate_ruling()
    pop = populations() if not applied else None
    if pop is None:
        raise Stop("build_plan is the pre-act derivation; after the act the populations are no "
                   "longer live and the plan cannot be re-derived, which is that guard working")
    records = records_for(pop)
    by_check = {row["id"]: row for row in pop["checked"]["entries"]}
    by_recovery = {row["id"]: row for row in pop["recovery"]["entries"]}
    by_entry = {e["id"]: e for e in pop["backbone"]["decisions"]}

    return {
        "what_this_is":
            "THE RESIDUE SITTING'S DISCARDS, CARRIES AND KEEPS, DERIVED AND PLANNED. The four "
            "populations, the sitting's own arithmetic reconciled in both directions, the shape of "
            "every retired record, and the fifty-three provenance stamps. Running this file "
            "without `--apply` writes NO register file of any kind. Every figure here is computed; "
            "none is transcribed (D-431).",
        "generator": "tools/audit/decisions/apply_residue_discard.py",
        "dispatch": "cc_instruction_preparation_eighth.md, Task 2",
        "the_rulings_that_ordered_it": {
            "source": "cowork_rulings_2026_08_17_residue_sitting.md",
            "every_sentence_located_in_that_record_on_this_run": ruling,
            "★_the_clause_every_retired_record_carries_verbatim": RULED_CLAUSE,
        },
        "the_inputs_pinned_by_hash": {
            "the_recovery_artifact": {"file": "tools/audit/deciding_act_recovery.json",
                                      "sha256": sha256_of(RECOVERY)},
            "the_sole_carrier_artifact": {"file": "tools/audit/sole_carrier_subclass.json",
                                          "sha256": sha256_of(GUARD)},
            "the_ratified_document_check": {"file": "tools/audit/ratified_document_check.json",
                                            "sha256": sha256_of(CHECK)},
            "the_filter_classification": {"file": "tools/audit/decisions_filter_classification.json",
                                          "sha256": sha256_of(FILTER)},
            "the_decisions_register_data_file": {
                "file": "tools/audit/decisions/backbone_decisions.json",
                "sha256": sha256_of(BACKBONE)},
        },
        "★_how_every_population_is_derived_rather_than_listed": {
            "the_29": "the entries the recovery pass returned NOTHING-FOUND for that the "
                      "sole-carrier guard also marks SOLE-CARRIER — the guard's own withheld set, "
                      "computed the same way `apply_soft_discard.py` computes it",
            "the_9_the_47_and_the_6": "the three results of the ratified-document check, taken "
                                      "from that artifact's own per-entry `result` field",
            "the_one_candidate_carried_from_the_nine": "the sole-carrier member among the nine; "
                                                       "any number other than one halts this act",
        },
        "the_populations": {
            "the_29_withheld_sole_carriers": pop["the_29_withheld_sole_carriers"],
            "the_9_subject_not_found_there": pop["the_9_subject_not_found_there"],
            "the_47_subject_in_ratified_document": pop["the_47_subject_in_ratified_document"],
            "the_6_no_document_ratification_act": pop["the_6_no_document_ratification_act"],
            "the_untrusted_candidates_carried_from_the_nine":
                pop["the_untrusted_candidates_carried_from_the_nine"],
        },
        "the_arithmetic": the_arithmetic(pop, applied=False),
        "the_entries_this_act_would_retire": pop["the_discard_population"],
        "the_retired_record_each_would_receive": records,
        "the_fifty_three_keeps_whose_provenance_is_stamped": {
            "★_where_each_act_comes_from":
                "a Ruling-2 keep's act is the document-ratification the check located, with the "
                "subject match quoted and located in the ratified document; a Ruling-4 keep's act "
                "is the recovery pass's ORIGINAL quoted act, unchanged, because the tested shape "
                "is not present for it and the ruling leaves that evidence exactly as it stood.",
            "the_47": {i: stamp_47(by_check[i])
                       for i in pop["the_47_subject_in_ratified_document"]},
            "the_6": {i: stamp_6(by_recovery[i])
                      for i in pop["the_6_no_document_ratification_act"]},
        },
        "★_what_this_act_does_NOT_do": {
            "it_destroys_nothing":
                "Every retired entry is moved WHOLE and unchanged into the retired block of the "
                "same data file. Nothing is deleted and every discard is individually revivable "
                "(#12).",
            "it_judges_no_decision":
                "The ruled clause every record carries says it: a provenance verdict, not a "
                "judgment on soundness or usefulness. The statement stands at its home.",
            "it_touches_no_other_field":
                "The fifty-three provenance stamps append to `status_source` and to nothing else; "
                "no other field of any entry, retired or surviving, is altered.",
            "it_loses_no_carried_candidate":
                "The 29 and the one member carried from the nine are published as UNTRUSTED "
                "CANDIDATES at `tools/audit/framework_untrusted_candidates.json`, which derives "
                "its population from this act's own inputs and fails on a hand edit.",
        },
        "★_the_state_of_this_act": {
            "state": "NOT APPLIED",
            "what_that_means": "This artifact is the derivation and the plan. Running `--apply` "
                               "performs it and rewrites this block, and `--check` reads the "
                               "rewritten block back.",
        },
        "_by_entry_titles": {i: by_entry[i]["title"] for i in pop["the_discard_population"]},
    }


# ── the act ──────────────────────────────────────────────────────────────────────────────────────

APPLIED_STATE_KEY = "★_the_state_of_this_act"
PERFORMED_STATE_KEY = "★_the_act_was_PLANNED_AND_THEN_PERFORMED"


def apply_it() -> dict:
    plan = build_plan()
    discard = set(plan["the_entries_this_act_would_retire"])
    records = plan["the_retired_record_each_would_receive"]
    stamps = dict(plan["the_fifty_three_keeps_whose_provenance_is_stamped"]["the_47"])
    stamps.update(plan["the_fifty_three_keeps_whose_provenance_is_stamped"]["the_6"])

    backbone = load(BACKBONE, "the decisions register's data file")
    block = backbone.get(RETIRED_BLOCK)
    if not block:
        raise Stop("the data file carries no retired-entries block. This act APPENDS a second "
                   "retirement to the first discard's block; without that block this is not the "
                   "act it claims to be.")
    already = {r["the_entry"]["id"] for r in block["entries"]}
    collision = sorted(discard & already)
    if collision:
        raise Stop(f"{collision} are already retired — this act has run")

    before = len(backbone["decisions"])
    surviving, retired = [], []
    for entry in backbone["decisions"]:
        if entry["id"] in discard:
            retired.append(records[entry["id"]])
            continue
        if entry["id"] in stamps:
            entry["status_source"] = stamped(entry["status_source"], stamps[entry["id"]])
        surviving.append(entry)

    if len(surviving) + len(retired) != before:
        raise Stop(f"the move does not account for the live population: {len(surviving)} live + "
                   f"{len(retired)} retired against {before} before")

    backbone["decisions"] = surviving
    block["entries"] = block["entries"] + retired
    block["acts"] = block.get("acts") or []
    block["acts"].append({
        "the_act": RETIRING_ACT,
        "the_retiring_authority": AUTHORITY,
        "retired_on": RETIRED_ON,
        "entries_retired_by_this_act": len(retired),
        "the_ruled_clause_every_record_carries_verbatim": RULED_CLAUSE,
        "★_what_this_act_is": "The residue sitting's two discards — Ruling 1's 29 withheld "
                              "sole-carriers and Ruling 3's 9 SUBJECT-NOT-FOUND-THERE entries. "
                              "Which act retired which entry is readable per record from its own "
                              "`retired_by` field; this list says the same thing at block level so "
                              "a reader meets it without walking the records.",
    })
    block["★_this_block_now_holds_more_than_one_retirement"] = (
        "The block's own header fields below name the FIRST retirement, and they are preserved "
        "verbatim (#12) rather than rewritten: `the_population_before_this_retirement` is the "
        "whole non-trivial population of the register, which no later retirement moves, so the "
        "arithmetic live + retired = that number survives every act. Every OTHER header field — "
        "`retired_on`, `retired_by`, `the_retiring_authority` — is the first act's and is read "
        "as such; the `acts` list above is where later acts record themselves, and every record "
        "carries its own three fields.")

    BACKBONE.write_text(json.dumps(backbone, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="")
    restamp_plan(len(retired), len(surviving), before, len(stamps))
    return {"retired": len(retired), "live": len(surviving), "before": before,
            "stamped": len(stamps)}


def restamp_plan(retired: int, live: int, before: int, stamped: int) -> None:
    """Re-stamp the committed plan's state block, because the act it describes has happened.

    Same shape and same reason as the first discard's: the plan cannot be REGENERATED after the act,
    because its populations are no longer live and `populations()` STOPs by construction. What would
    otherwise survive is a committed artifact whose own state block says NOT APPLIED about an act
    that was applied, and a check that no longer looks at it (#10).
    """
    if not PLAN.exists():
        raise Stop(f"the committed plan is missing, so the act cannot record that it happened: "
                   f"{PLAN}")
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    if APPLIED_STATE_KEY not in plan:
        raise Stop(f"the committed plan carries no `{APPLIED_STATE_KEY}` block, so this act cannot "
                   f"find the statement about its own state that it must correct")
    former = plan.pop(APPLIED_STATE_KEY)
    plan[PERFORMED_STATE_KEY] = {
        "state": "APPLIED",
        "applied_on": RETIRED_ON,
        "applied_by": RETIRING_ACT,
        "the_authority": AUTHORITY,
        "the_arithmetic_of_the_act": {
            "the_live_record_before": before,
            "retired_by_this_act": retired,
            "the_live_record_after": live,
            "provenance_stamps_written": stamped,
        },
        "★_why_this_block_was_rewritten_rather_than_left_standing":
            "It was the plan's statement about its own STATE, and it said NOT APPLIED. The act "
            "happened, so leaving it would put a false statement about the record inside the "
            "record (#10). The plan cannot be regenerated after the act — its populations are no "
            "longer live and `populations()` STOPs — so the block is rewritten at the moment the "
            "state changes rather than by a later re-derivation that cannot exist.",
        "the_former_block_preserved_verbatim_#12": former,
    }
    PLAN.write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="")


# ── the check ────────────────────────────────────────────────────────────────────────────────────

def check_applied() -> int:
    """The check, in the two states this act can be in.

    BEFORE the act, what is live is the PLAN, which must still re-derive from the committed inputs.
    AFTER the act, the plan can no longer be re-derived by construction — its populations are no
    longer live — so what is checked instead is the applied state: the two retirements accounting
    for the former population together, this act's own records carrying the four things the ruling
    requires, the fifty-three stamps still present, and the sitting's own sums still reconciling.
    """
    backbone = load(BACKBONE, "the decisions register's data file")
    block = backbone.get(RETIRED_BLOCK)
    if not block:
        raise Stop("the data file carries no retired-entries block at all")

    mine = [r for r in block["entries"] if r["retired_by"] == RETIRING_ACT]
    if not mine:
        rebuilt = json.dumps(build_plan(), indent=1, ensure_ascii=False) + "\n"
        if not PLAN.exists():
            print("FAIL: the plan artifact is missing:", PLAN)
            return 1
        if PLAN.read_text(encoding="utf-8") != rebuilt:
            print("FAIL: the residue-discard plan does not re-derive:", PLAN)
            return 1
        print("the residue retirement has not been applied, and the planned one re-derives")
        return 0

    live = [e["id"] for e in backbone["decisions"]]
    retired = [r["the_entry"]["id"] for r in block["entries"]]
    both = sorted(set(live) & set(retired))
    if both:
        raise Stop(f"{both} appear in BOTH the live entries and the retired block. An entry is "
                   f"live or it is retired.")
    if len(set(retired)) != len(retired):
        raise Stop("an entry identity is carried twice inside the retired block")
    before = block["the_population_before_this_retirement"]
    if len(live) + len(retired) != before:
        raise Stop(f"the arithmetic does not account for the former population: {len(live)} live + "
                   f"{len(retired)} retired against {before} before. An entry is in neither block.")

    required = ("the_finding", "retired_on", "the_retiring_authority", "the_ruled_clause_verbatim",
                "which_ruling_of_the_sitting_retired_it", "the_reason")
    for record in mine:
        missing = [f for f in required if not record.get(f)]
        if missing:
            raise Stop(f"the retired record for {record['the_entry']['id']} carries no {missing} — "
                       f"the ruling requires all of them of every record")
        if record["the_ruled_clause_verbatim"] != RULED_CLAUSE:
            raise Stop(f"the retired record for {record['the_entry']['id']} does not carry the "
                       f"ruled clause verbatim")

    # The keeps' stamps, re-checked against the artifacts they were quoted from — a stamp removed
    # or rewritten fails on the day it happens.
    checked = load(CHECK, "the committed ratified-document check")
    recovery = load(RECOVERY, "the committed recovery artifact")
    by_entry = {e["id"]: e for e in backbone["decisions"]}
    expected = {}
    for row in checked["entries"]:
        if row["result"] == IN_RATIFIED:
            expected[row["id"]] = stamp_47(row)
        elif row["result"] == NO_RATIFICATION:
            expected[row["id"]] = stamp_6({r["id"]: r for r in recovery["entries"]}[row["id"]])
    for i, stamp in sorted(expected.items()):
        entry = by_entry.get(i)
        if entry is None:
            raise Stop(f"{i} is a ruled KEEP but is not in the live record")
        if stamp not in entry["status_source"]:
            raise Stop(f"{i}'s recorded deciding act is not on its entry — a ruled keep's "
                       f"provenance has been removed or rewritten")

    # The sitting's own sums, re-reconciled against the record as it stands.
    pop_now = {
        "backbone": backbone,
        "recovery": recovery,
        "the_29_withheld_sole_carriers":
            [r["the_entry"]["id"] for r in mine
             if r["which_ruling_of_the_sitting_retired_it"].startswith("Ruling 1")],
        "the_9_subject_not_found_there":
            [r["the_entry"]["id"] for r in mine
             if r["which_ruling_of_the_sitting_retired_it"].startswith("Ruling 3")],
        "the_47_subject_in_ratified_document":
            [r["id"] for r in checked["entries"] if r["result"] == IN_RATIFIED],
        "the_6_no_document_ratification_act":
            [r["id"] for r in checked["entries"] if r["result"] == NO_RATIFICATION],
        "the_discard_population": [r["the_entry"]["id"] for r in mine],
    }
    sums = the_arithmetic(pop_now, applied=True)

    if not PLAN.exists():
        raise Stop(f"the committed plan is missing: {PLAN}")
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    if APPLIED_STATE_KEY in plan:
        raise Stop("the residue retirement is applied, but the committed plan still carries its "
                   "NOT-APPLIED state block")
    performed = plan.get(PERFORMED_STATE_KEY)
    if not performed or performed.get("state") != "APPLIED":
        raise Stop("the committed plan does not record that this act was performed")
    if performed["the_arithmetic_of_the_act"]["retired_by_this_act"] != len(mine):
        raise Stop("the committed plan's recorded arithmetic disagrees with the data file's")

    locate_ruling()
    print(f"the residue discard re-checks: {len(live)} live + {len(retired)} retired = {before} "
          f"before; this act retired {len(mine)}; the sitting's sums reconcile "
          f"(keep {sums['the_keep_side']['the_sum']}, retired "
          f"{sums['the_retired_side']['the_sum']}, total "
          f"{sums['the_whole_population']['keep_plus_retired']}); every ruled keep carries its "
          f"recorded deciding act")
    return 0


def main(argv: list[str]) -> int:
    if "--check" in argv:
        return check_applied()

    if "--apply" in argv:
        result = apply_it()
        print(f"applied: {result['retired']} entries retired, {result['live']} live "
              f"(was {result['before']}), {result['stamped']} provenance stamps written")
        print("REGENERATE the register and every register-derived artifact by its own generator.")
        return 0

    plan = build_plan()
    PLAN.write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="")
    print("wrote", PLAN.relative_to(ROOT), "— NO register file was touched")
    pops = plan["the_populations"]
    print(f"  the 29 {len(pops['the_29_withheld_sole_carriers'])} + the 9 "
          f"{len(pops['the_9_subject_not_found_there'])} = "
          f"{len(plan['the_entries_this_act_would_retire'])} to retire; "
          f"the 47 {len(pops['the_47_subject_in_ratified_document'])} + the 6 "
          f"{len(pops['the_6_no_document_ratification_act'])} to stamp")
    a = plan["the_arithmetic"]
    print(f"  keep {a['the_keep_side']['the_sum']} / retired {a['the_retired_side']['the_sum']} / "
          f"total {a['the_whole_population']['keep_plus_retired']}; live record "
          f"{a['the_live_record']['before_this_act']} -> {a['the_live_record']['after_this_act']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
