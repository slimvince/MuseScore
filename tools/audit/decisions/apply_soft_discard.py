#!/usr/bin/env python3
"""THE RULED SOFT-DISCARD — planned, applied, and afterwards re-checked.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §3(A) of
`cowork_rulings_2026_08_16_preparation_return.md`: *"The 194 NOTHING-FOUND entries are
SOFT-DISCARDED — behind the sole-carrier guard."*  The discard population is therefore DERIVED —
the entries the deciding-act recovery pass returned NOTHING-FOUND for, MINUS the members the
sole-carrier guard withheld — and never hand-listed.

★ WHAT A SOFT-DISCARD IS, IN THE USER'S OWN WORDS, AND WHAT IT IS NOT.  Retired from the live
record, **not destroyed** (#12), and individually revivable the moment a deciding act is named.
Every retired record carries the ruled clause verbatim: *"a provenance verdict, not a judgment on
soundness or usefulness; the statement stands at its home and is met by the derivation."*  The
statement each retired entry records still stands at its home document; what is retired is the
decisions register's claim to be the AUTHORITY for it.

★ WHY THE RETIRED ENTRIES STAY IN THE DATA FILE.  A retired entry is moved WHOLE, unchanged, into a
RETIRED-ENTRIES block of the same data file — the shape `tools/audit/gen_discard_records.py` already
uses for a retired pointer, added there on the user's ruling of 2026-08-15.  It is never deleted,
so nothing is destroyed and a revival is a move back rather than a re-authoring.

THE THREE INVOCATIONS.
    --plan    (the default)  derive the population and PUBLISH WHAT WOULD CHANGE, writing no
                             register file at all.  This is the act that must run first: the
                             consequences of removing entries from the live record reach every
                             derivation over it, and they are measured before anything moves.
    --apply                  perform the move and the ten provenance stamps in the data file.
    --check                  re-verify the applied state: live + retired accounts for the whole
                             former population BY ARITHMETIC, no entry is in both blocks and none
                             is in neither, and every retired record carries all four things the
                             ruling requires of it.

THE STOPS, so this cannot silently stop being what it claims:
  * a missing input artifact, or one carrying no population, STOPS it;
  * the derived population and the decisions register's data file disagreeing in either direction
    STOPS it (D-671);
  * a discard-population member that is also a sole-carrier STOPS it — the guard would have been
    breached;
  * an entry in BOTH blocks, or the arithmetic not accounting for the former population, STOPS it;
  * a retired record missing its finding, its date, its authority or the ruled clause STOPS it —
    the ruling requires all four of every record;
  * a sentence of the ruling that ordered the discard no longer in its ruling record STOPS it.

Run:
  python tools/audit/decisions/apply_soft_discard.py            # plan only, writes no register file
  python tools/audit/decisions/apply_soft_discard.py --apply    # perform it
  python tools/audit/decisions/apply_soft_discard.py --check    # re-verify the applied state
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

sys.path.insert(0, str(HERE.parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

BACKBONE = HERE / "backbone_decisions.json"
RECOVERY = ROOT / "tools" / "audit" / "deciding_act_recovery.json"
GUARD = ROOT / "tools" / "audit" / "sole_carrier_subclass.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
PLAN = ROOT / "tools" / "audit" / "soft_discard_application.json"

RETIRED_BLOCK = "retired_entries"
NOTHING_FOUND = "NOTHING-FOUND"
SOLE_CARRIER = "SOLE-CARRIER"
RETIRED_ON = "2026-08-16"
# The act that PERFORMED the retirement, not the one that planned it. The third batch's Task 3
# derived and measured the act and REVERTED it; the fourth batch's Task 2 did the same. What
# performs it is the fifth batch's Task 1, under the reach ruling (§4) and the STANDING checks'
# treatment ruling (§6) that the third and fourth batches' STOPs made necessary. A record naming
# the planning dispatch as the retiring one would state something false about who did it.
RETIRING_ACT = ("CC, `cc_instruction_preparation_fifth.md` Task 1, on the user's rulings of "
                "2026-08-16 (§3 the discard, §4 its reach, §6 the STANDING checks' treatment)")
AUTHORITY = "cowork_rulings_2026_08_16_preparation_return.md §3 (A)"

RULED_CLAUSE = ("a provenance verdict, not a judgment on soundness or usefulness; the statement "
                "stands at its home and is met by the derivation")

RULING_SENTENCES = {
    "what was ruled":
        "The 194 NOTHING-FOUND entries are SOFT-DISCARDED — behind the sole-carrier guard.",
    "what a discard record must carry": RULED_CLAUSE,
    "nothing is destroyed":
        "Nothing destroyed (#12); every discard individually revivable when a deciding act is "
        "later named.",
    "what a sole-carrier member does not do":
        "Sole-carrier members do NOT ride the discard — they return to the user as a list",
}

REFERENCE = re.compile(r"\bD-\d+\b")
REFERENCE_FIELDS = ("status_source", "rationale", "plain", "home", "verbatim", "title")
B1_BULLET = re.compile(r"\(B1\)[^\n]*(?:\n(?!\s*-\s)[^\n]*)*")


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
        raise Stop("a sentence of the ruling that ordered this discard is no longer in its ruling "
                   f"record, so the act would outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


def load(path: Path, what: str) -> dict:
    if not path.exists():
        raise Stop(f"{what} is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def population() -> tuple[list[str], dict, dict, dict]:
    """The discard population, DERIVED and never hand-listed."""
    recovery = load(RECOVERY, "the committed recovery artifact")
    guard = load(GUARD, "the committed sole-carrier artifact")
    backbone = load(BACKBONE, "the decisions register's data file")

    nothing_found = {row["id"] for row in recovery["entries"] if row["result"] == NOTHING_FOUND}
    if not nothing_found:
        raise Stop("the committed recovery artifact carries no NOTHING-FOUND entry, so there is no "
                   "discard population — the import is not what this act assumes it is")
    withheld = {row["id"] for row in guard["entries"] if row["verdict"] == SOLE_CARRIER}

    discard = sorted(nothing_found - withheld)
    breached = sorted(set(discard) & withheld)
    if breached:
        raise Stop(f"the discard population contains sole-carrier members {breached} — the guard "
                   f"the ruling put in front of this act would be breached")

    live = {entry["id"] for entry in backbone["decisions"]}
    absent = sorted(i for i in discard if i not in live)
    if absent:
        raise Stop(f"the discard population names {absent}, which the decisions register's data "
                   f"file does not carry live — the two records disagree about the population and "
                   f"this act does not choose between them (D-671)")
    return discard, recovery, guard, backbone


def b1_keeps(act_found: set[str]) -> list[str]:
    """The ten entries the user's (B1) ruling KEPT — PARSED from the ruling record, never typed."""
    match = B1_BULLET.search(RULING.read_text(encoding="utf-8"))
    if not match:
        raise Stop("the ruling record carries no (B1) bullet, so the ten keeps cannot be imported")
    kept = sorted(set(re.findall(r"\bD-\d+\b", match.group(0))))
    if len(kept) != 10:
        raise Stop(f"the (B1) bullet names {len(kept)} register entries where the ruling says TEN: "
                   f"{kept}")
    stray = sorted(k for k in kept if k not in act_found)
    if stray:
        raise Stop(f"the (B1) bullet names {stray}, which the recovery pass did not return "
                   f"ACT-FOUND for")
    return kept


def stamp_for(recovery_row: dict) -> str:
    """The provenance stamp for one (B1) keep: its recovered act, quoted and located."""
    if not recovery_row["acts"]:
        raise Stop(f"{recovery_row['id']} is a (B1) keep but the recovery artifact records no act "
                   f"for it, so there is nothing to stamp")
    act = recovery_row["acts"][0]
    return (" ★ THE DECIDING ACT RECOVERED AND KEPT (user's ruling of 2026-08-16, "
            f"{AUTHORITY.replace(' §3 (A)', ' §3 (B1)')}): a passage at `{act['document']}` line "
            f"{act['line']}, carrying {', '.join(act['the_user_act_markers_the_passage_carries'])} "
            f"and matching {act['what_matched_the_subject']}, reads — \"{act['the_act_quoted']}\" "
            "The act is quoted from `tools/audit/deciding_act_recovery.json`; no other field of "
            "this entry is touched.")


def retired_record(entry: dict, recovery_row: dict, filter_class: str) -> dict:
    return {
        "the_entry": entry,
        "retired_on": RETIRED_ON,
        "retired_by": RETIRING_ACT,
        "the_retiring_authority": AUTHORITY,
        "the_finding": (
            f"{filter_class} at the ratified decisions-register filter classification; "
            f"{NOTHING_FOUND} at the deciding-act recovery pass"),
        "the_finding_at_the_filter": filter_class,
        "the_finding_at_the_recovery_pass": recovery_row["result"],
        "why_the_recovery_pass_returned_that": recovery_row["why_this_result"],
        "the_reason": (
            "No deciding act could be named for this entry from its own recorded fields, and none "
            "could be recovered from the documents the entry itself cites. The sole-carrier guard "
            "did not withhold it: its status is not deferred, its home resolves, and its content "
            "is carried outside the decisions-register family."),
        "the_ruled_clause_verbatim": RULED_CLAUSE,
        "★_what_this_retirement_is_not":
            "It is NOT a finding that the decision is wrong, unsound or unwanted, and it is NOT a "
            "deletion. The statement this entry records STANDS AT ITS HOME and is met by the "
            "derivation, exactly as the ruled clause above says.",
        "how_it_is_revived":
            "By naming a deciding act for it. The entry is moved back into `decisions` unchanged; "
            "nothing has to be re-authored, because nothing was destroyed (#12).",
    }


def consequences(discard: set[str], backbone: dict) -> dict:
    """What removing these entries from the LIVE record reaches — measured before anything moves."""
    surviving = [e for e in backbone["decisions"] if e["id"] not in discard]
    pointing: list[dict] = []
    for entry in surviving:
        named = set()
        for field in REFERENCE_FIELDS:
            value = entry.get(field)
            if isinstance(value, str):
                named.update(REFERENCE.findall(value))
        hits = sorted(named & discard)
        if hits:
            pointing.append({"the_surviving_entry": entry["id"], "names_retired_entries": hits})
    per_group: dict[str, int] = {}
    for entry in backbone["decisions"]:
        if entry["id"] in discard:
            per_group[entry["group"]] = per_group.get(entry["group"], 0) + 1
    per_status: dict[str, int] = {}
    for entry in backbone["decisions"]:
        if entry["id"] in discard:
            per_status[entry["status"]] = per_status.get(entry["status"], 0) + 1
    return {
        "★_why_this_block_exists":
            "Removing entries from the live record reaches every derivation over that record. The "
            "reach is MEASURED here, before anything moves, rather than discovered by a guard "
            "turning red after the act.",
        "surviving_entries_that_NAME_a_retired_entry": {
            "★_why_it_matters":
                "The decisions register's own establishment pass checks that every `D-…` "
                "cross-reference in an entry resolves to an entry the record holds. A surviving "
                "entry naming a retired one would report as DANGLING unless the retired block is "
                "among the entries that pass consults — which is what makes teaching that pass "
                "about the block a requirement of the act rather than a tidy-up after it.",
            "count": len(pointing),
            "entries": pointing,
        },
        "the_discard_population_by_group": dict(sorted(per_group.items())),
        "the_discard_population_by_recorded_status": dict(sorted(per_status.items())),
    }


def build_plan() -> dict:
    ruling = locate_ruling()
    discard, recovery, guard, backbone = population()
    by_recovery = {row["id"]: row for row in recovery["entries"]}
    act_found = {i for i, row in by_recovery.items() if row["result"] == "ACT-FOUND"}
    kept = b1_keeps(act_found)

    nothing_found = sorted(i for i, row in by_recovery.items() if row["result"] == NOTHING_FOUND)
    withheld = sorted(row["id"] for row in guard["entries"]
                      if row["verdict"] == SOLE_CARRIER and row["id"] in set(nothing_found))
    live_now = len(backbone["decisions"])
    already = backbone.get(RETIRED_BLOCK)

    return {
        "what_this_is":
            "THE RULED SOFT-DISCARD, DERIVED AND PLANNED. The population, the arithmetic, the "
            "shape of every retired record, the ten provenance stamps, and the measured reach of "
            "the act over the record that consumes the decisions register. Running this file "
            "without `--apply` writes NO register file of any kind.",
        "generator": "tools/audit/decisions/apply_soft_discard.py",
        "dispatch": "cc_instruction_preparation_third.md, Task 3",
        "the_ruling_that_ordered_it": {
            "source": AUTHORITY,
            "every_sentence_located_in_that_record_on_this_run": ruling,
            "★_the_clause_every_retired_record_carries_verbatim": RULED_CLAUSE,
        },
        "the_inputs_pinned_by_hash": {
            "the_recovery_artifact": {"file": "tools/audit/deciding_act_recovery.json",
                                      "sha256": sha256_of(RECOVERY)},
            "the_sole_carrier_artifact": {"file": "tools/audit/sole_carrier_subclass.json",
                                          "sha256": sha256_of(GUARD)},
            "the_decisions_register_data_file": {
                "file": "tools/audit/decisions/backbone_decisions.json",
                "sha256": sha256_of(BACKBONE)},
        },
        "the_arithmetic": {
            "★_how_the_population_is_derived":
                "The entries the deciding-act recovery pass returned NOTHING-FOUND for, MINUS the "
                "members the sole-carrier guard withheld. Never hand-listed, and a member that is "
                "both halts this act.",
            "returned_NOTHING_FOUND_by_the_recovery_pass": len(nothing_found),
            "withheld_by_the_sole_carrier_guard": len(withheld),
            "the_executed_discard_population": len(discard),
            "it_balances": len(nothing_found) == len(withheld) + len(discard),
            "the_live_record_before_this_act": live_now,
            "the_live_record_after_this_act": live_now - len(discard),
            "a_retired_block_already_exists": already is not None,
        },
        "the_entries_withheld_by_the_guard_and_NOT_discarded": withheld,
        "the_entries_this_act_would_retire": discard,
        "the_ten_B1_keeps_whose_provenance_is_stamped": {
            "★_how_they_are_derived": "PARSED from the ruling record's own (B1) bullet on every "
                                      "run; a bullet naming any number other than ten, or naming "
                                      "an entry the recovery pass did not return ACT-FOUND for, "
                                      "halts this act rather than being corrected.",
            "entries": kept,
            "the_stamp_each_would_receive": {i: stamp_for(by_recovery[i]) for i in kept},
        },
        "what_the_act_reaches": consequences(set(discard), backbone),
        "★_the_act_was_PLANNED_AND_MEASURED_AND_NOT_PERFORMED": {
            "state": "NOT APPLIED",
            "what_happened": "The act was applied to the working tree, the whole guard set was run "
                             "at the edited tree, the reach was read off it, and the edit was "
                             "REVERTED — every touched file proven byte-identical to its committed "
                             "blob by hashing both. Nothing was committed.",
            "why": "Assumption A3 of the dispatch that ordered the act — that the mutation's reach "
                   "is the decisions-register family and its derived views ONLY — is FALSIFIED by "
                   "that run, and the dispatch's own instruction on that outcome is a "
                   "STOP-and-report. The reach includes both gate-bearing phase-1 derivations, "
                   "which do not merely go stale: they HALT.",
            "where_the_measurement_is_recorded":
                "cc_report_preparation_third.md §4, and THE PREPARATION THIRD BATCH section of "
                "cowork_away_returns.md — the complete captured output of every check that turned "
                "red, quoted from the run.",
            "★_what_a_reader_must_not_conclude":
                "That the ruling is in doubt. The user ruled the discard; what this measurement "
                "establishes is that performing it inside the bounds the dispatch set is not "
                "possible, because the act reaches authored judgments and gate-bearing derivations "
                "the dispatch does not authorize touching. What is owed is a ruling on that reach, "
                "not a re-decision of the discard.",
        },
        "★_what_this_act_does_NOT_do": {
            "it_destroys_nothing":
                "Every retired entry is moved WHOLE and unchanged into a retired block of the same "
                "data file. Nothing is deleted and every discard is individually revivable (#12).",
            "it_judges_no_decision":
                "The ruled clause every record carries says it: a provenance verdict, not a "
                "judgment on soundness or usefulness. The statement stands at its home.",
            "it_touches_no_other_field":
                "The ten provenance stamps append to `status_source` and to nothing else; no "
                "other field of any entry, retired or surviving, is altered.",
            "it_rules_nothing_about_the_62":
                "The entries the user's (B2) limb left unruled are untouched by this act.",
        },
    }


# ── the act ──────────────────────────────────────────────────────────────────────────────────────

def apply_it() -> dict:
    plan = build_plan()
    discard = set(plan["the_entries_this_act_would_retire"])
    kept = plan["the_ten_B1_keeps_whose_provenance_is_stamped"]["entries"]
    stamps = plan["the_ten_B1_keeps_whose_provenance_is_stamped"]["the_stamp_each_would_receive"]

    backbone = load(BACKBONE, "the decisions register's data file")
    if backbone.get(RETIRED_BLOCK):
        raise Stop("the data file already carries a retired-entries block. This act adds one; "
                   "retiring a second population is a separate act with its own ruling.")

    recovery = load(RECOVERY, "the committed recovery artifact")
    by_recovery = {row["id"]: row for row in recovery["entries"]}
    filter_class = {row["id"]: row["the_class_the_filter_proposed"] for row in recovery["entries"]}

    before = len(backbone["decisions"])
    surviving, retired = [], []
    for entry in backbone["decisions"]:
        if entry["id"] in discard:
            retired.append(retired_record(entry, by_recovery[entry["id"]],
                                          filter_class[entry["id"]]))
            continue
        if entry["id"] in kept:
            entry["status_source"] = entry["status_source"] + stamps[entry["id"]]
        surviving.append(entry)

    if len(surviving) + len(retired) != before:
        raise Stop(f"the move does not account for the former population: {len(surviving)} live + "
                   f"{len(retired)} retired against {before} before")

    backbone["decisions"] = surviving
    backbone[RETIRED_BLOCK] = {
        "what_this_is":
            "THE RETIRED-ENTRIES BLOCK. Entries SOFT-DISCARDED from the live record by the user's "
            "ruling of 2026-08-16 §3(A) — retired, NOT destroyed (#12), each moved here WHOLE and "
            "unchanged, and each individually revivable the moment a deciding act is named for it. "
            "Nothing in this block is rendered into the register's INDEX or its group files: a "
            "retired entry has left the LIVE record, which is what the discard is.",
        "the_retiring_authority": AUTHORITY,
        "retired_on": RETIRED_ON,
        "retired_by": RETIRING_ACT,
        "the_ruled_clause_every_record_carries_verbatim": RULED_CLAUSE,
        "the_population_before_this_retirement": before,
        "★_the_stops_this_block_carries_so_it_cannot_become_a_hole": [
            "an entry identity appearing in BOTH `decisions` and this block halts the renderer and "
            "every reconciliation over the data file — a retired entry re-appearing live is the "
            "failure this block exists to make impossible;",
            "live entries plus retired entries must equal `the_population_before_this_retirement` "
            "exactly — an entry in NEITHER block is caught by that arithmetic, which is why the "
            "former population is recorded here rather than remembered;",
            "a retired record missing its finding, its date, its retiring authority or the ruled "
            "clause halts the act's own check — the ruling requires all four of every record;",
            "a `D-…` cross-reference in a surviving entry still resolves when it names a RETIRED "
            "entry: the decisions register's establishment pass consults this block beside the "
            "live entries, so retiring an entry cannot silently turn another entry's reference "
            "into a dangling one.",
        ],
        "entries": retired,
    }

    BACKBONE.write_text(json.dumps(backbone, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="")
    restamp_plan(len(retired), len(surviving), before)
    return {"retired": len(retired), "live": len(surviving), "before": before,
            "stamped": len(kept)}


APPLIED_STATE_KEY = "★_the_act_was_PLANNED_AND_MEASURED_AND_NOT_PERFORMED"
PERFORMED_STATE_KEY = "★_the_act_was_PLANNED_MEASURED_TWICE_AND_THEN_PERFORMED"


def restamp_plan(retired: int, live: int, before: int) -> None:
    """Re-stamp the committed plan's state block, because the act it describes has happened.

    The plan cannot be REGENERATED after the act — its population is no longer live, so
    `population()` STOPs by construction, which is that guard working. What would otherwise
    survive is a committed artifact whose own state block says NOT APPLIED about an act that was
    applied, and a check that no longer looks at it. So the one block whose subject is the act's
    STATE is rewritten here, at the moment the state changes, and `--check` reads it back. No
    other field of the plan moves: the population, the arithmetic, the ten stamps and the measured
    reach are the planning act's record and are not re-derived against the record the act changed.
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
        },
        "★_why_this_block_was_rewritten_rather_than_left_standing":
            "It was the plan's statement about its own STATE, and it said NOT APPLIED. The act "
            "happened, so leaving it would put a false statement about the record inside the "
            "record (#10). The plan cannot be regenerated after the act — its population is no "
            "longer live and `population()` STOPs — so the block is rewritten at the moment the "
            "state changes rather than by a later re-derivation that cannot exist.",
        "the_former_block_preserved_verbatim_#12": former,
    }
    PLAN.write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="")


# ── the check ────────────────────────────────────────────────────────────────────────────────────

def check_applied() -> int:
    """The check, in the two states this act can be in.

    BEFORE the act, what is live is the PLAN: the ruling's sentences must still be in its ruling
    record, the population must still be derivable from the committed artifacts, and the committed
    plan must still re-derive from them.  AFTER the act, the plan can no longer be re-derived by
    construction — its population is no longer live — so what is checked instead is the applied
    state's own arithmetic and the four things the ruling requires of every retired record.
    """
    backbone = load(BACKBONE, "the decisions register's data file")
    block = backbone.get(RETIRED_BLOCK)
    if not block:
        locate_ruling()
        rebuilt = json.dumps(build_plan(), indent=1, ensure_ascii=False) + "\n"
        if not PLAN.exists():
            print("FAIL: the plan artifact is missing:", PLAN)
            return 1
        if PLAN.read_text(encoding="utf-8") != rebuilt:
            print("FAIL: the soft-discard plan does not re-derive:", PLAN)
            return 1
        print("no retirement has been applied, and the planned one re-derives")
        return 0

    live = [e["id"] for e in backbone["decisions"]]
    retired = [r["the_entry"]["id"] for r in block["entries"]]
    both = sorted(set(live) & set(retired))
    if both:
        raise Stop(f"{both} appear in BOTH the live entries and the retired block. An entry is "
                   f"live or it is retired.")
    if len(set(live)) != len(live) or len(set(retired)) != len(retired):
        raise Stop("an entry identity is carried twice inside one block")
    before = block["the_population_before_this_retirement"]
    if len(live) + len(retired) != before:
        raise Stop(f"the arithmetic does not account for the former population: {len(live)} live + "
                   f"{len(retired)} retired against {before} before. An entry is in neither block.")

    required = ("the_finding", "retired_on", "the_retiring_authority",
                "the_ruled_clause_verbatim")
    for record in block["entries"]:
        missing = [f for f in required if not record.get(f)]
        if missing:
            raise Stop(f"the retired record for {record['the_entry']['id']} carries no {missing} — "
                       f"the ruling requires all four of every record")
        if record["the_ruled_clause_verbatim"] != RULED_CLAUSE:
            raise Stop(f"the retired record for {record['the_entry']['id']} does not carry the "
                       f"ruled clause verbatim")

    # The plan's own statement about the act's STATE must agree with the state on disk. A plan
    # still saying NOT APPLIED beside an applied retirement is a false statement about the record
    # inside the record, and nothing else would catch it — the plan cannot be re-derived once the
    # act has happened.
    if not PLAN.exists():
        raise Stop(f"the committed plan is missing: {PLAN}")
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    if APPLIED_STATE_KEY in plan:
        raise Stop("the retirement is applied, but the committed plan still carries its "
                   "NOT-APPLIED state block")
    performed = plan.get(PERFORMED_STATE_KEY)
    if not performed or performed.get("state") != "APPLIED":
        raise Stop("the committed plan does not record that this act was performed")
    # ★ THE PLAN'S ARITHMETIC IS ABOUT *THIS* ACT, AND THE BLOCK MAY HOLD MORE THAN ONE.
    # This comparison formerly read the block's WHOLE retired population and the WHOLE live record
    # back into the plan's three recorded figures — which is right while the block holds exactly one
    # retirement and false the moment a second, separately ruled act appends to it (the residue
    # sitting's, 2026-08-17). Re-derived after that act, `len(retired)` is every retirement's total
    # and `len(live)` is the record after all of them, so the check reported a disagreement that is
    # not one: the plan's figures were, and remain, a true statement about the act it planned.
    # WHAT IS ASSERTED INSTEAD is narrower and stays true across every later retirement: the number
    # of records in the block that THIS act retired, read off their own `retired_by` field, must be
    # the number the plan records; the plan's before-figure must still be the block's former
    # population; and its own two figures must be self-consistent. A plan whose arithmetic was
    # rewritten still fails, which is what this check exists for. The block-level arithmetic — live
    # plus retired accounting for the former population — is asserted above and is untouched.
    mine = [r for r in block["entries"] if r.get("retired_by") == RETIRING_ACT]
    recorded = performed["the_arithmetic_of_the_act"]
    if (recorded.get("the_live_record_before") != before
            or recorded.get("retired_by_this_act") != len(mine)
            or recorded.get("the_live_record_after")
            != recorded.get("the_live_record_before", 0) - len(mine)):
        raise Stop("the committed plan's recorded arithmetic disagrees with the data file's: the "
                   f"plan records {recorded}, while the block's former population is {before} and "
                   f"{len(mine)} record(s) carry this act's own `retired_by`")

    locate_ruling()
    print(f"the soft-discard re-checks: {len(live)} live + {len(retired)} retired = {before} "
          f"before, no entry in both blocks and none in neither, every retired record carrying "
          f"its finding, its date, its authority and the ruled clause")
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
    arithmetic = plan["the_arithmetic"]
    print(f"  NOTHING-FOUND {arithmetic['returned_NOTHING_FOUND_by_the_recovery_pass']} = "
          f"withheld {arithmetic['withheld_by_the_sole_carrier_guard']} + discard "
          f"{arithmetic['the_executed_discard_population']} "
          f"({'balances' if arithmetic['it_balances'] else 'DOES NOT BALANCE'})")
    print(f"  live record {arithmetic['the_live_record_before_this_act']} -> "
          f"{arithmetic['the_live_record_after_this_act']}")
    reach = plan["what_the_act_reaches"]["surviving_entries_that_NAME_a_retired_entry"]
    print(f"  surviving entries naming a retired entry: {reach['count']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
