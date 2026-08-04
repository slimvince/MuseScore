#!/usr/bin/env python3
"""READ WAVE 4's measured yield, graded against the bands registered BEFORE the reads.

WHAT THIS IS.  `phase1n_reading_regime.json` registered, before any owed document was read, a
predicted yield band and a point prediction for every owed document, so that the length proxy
would be tested OUT OF SAMPLE as a by-product of the reading rather than by a separate study
(#17b, #19, #20).  This is the fourth instalment of that test.  The earlier instalments are
`reads1_yield.json`, `reads2_yield.json` and `reads3_yield.json`.

WHY THE REGISTERED ROWS ARE READ AND NOT RECOMPUTED.  Unchanged from waves 1–3, and the reason
is `OPEN_ITEMS.md` OI-316: the regime's own update protocol tells each wave to write its yield
into `actual_yield_when_read`, but the only lawful route to that field recomputes the bands from
the terciles of the READ set — which a read wave changes — so following the protocol would
replace the registered prediction with one fitted on data that now contains the documents being
graded (#20) and would lose the registered value (#12).  So the regime artifact and
`gen_phase1m_measurements.READ_WAVES` are again left untouched.  The divergence is the rowed
defect, not a stalled wave — now FOUR waves deep.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them; the low-yield reasons; and the two prose
             observations.  Nothing else.
  derived  : every band, every point prediction and every size fact (read off the regime
             artifact); every entry's home, title and status (read off the register data); every
             count and every verdict; the running read total.

Run:  python tools/audit/decisions/gen_reads4_yield.py [--check]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REGIME = os.path.join(HERE, "phase1n_reading_regime.json")
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
PRIOR = [os.path.join(HERE, f"reads{i}_yield.json") for i in (1, 2, 3)]
OUT = os.path.join(HERE, "reads4_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# -- AUTHORED — what this wave read, and what it entered from each read -------
WAVE = "reads-4"
WAVE_DISPATCH = "cc_instruction_reads_4.md"
WAVE_INDEX = 4
WAVE_READS: dict[str, list[str]] = {
    "cowork_audit_protocol.md":
        ["D-547", "D-548", "D-549", "D-550", "D-551", "D-552"],
    "docs/extension_stripping_policy.md":
        ["D-553"],
    "cowork_idiom_discovery_findings.md":
        ["D-554", "D-555", "D-556"],
    "cowork_l1l3_stabilization_plan.md":
        ["D-557", "D-558", "D-559"],
    "docs/nct_detection_design.md":
        ["D-560"],
    "cowork_eg2_scoping.md":
        ["D-561", "D-562", "D-563", "D-564"],
    "cowork_joint_estimator_factorization.md":
        ["D-565"],
    "cowork_audit_obligation_map.md":
        ["D-566", "D-567", "D-568"],
    "cowork_layer1_tone_collection_design.md":
        ["D-569", "D-570"],
    "docs/stage4b_design.md":
        ["D-571", "D-572", "D-573", "D-574"],
    "docs/key_detection_baroque_partial_signature.md":
        ["D-575", "D-576"],
    "cowork_l1l4_architecture_audit.md":
        ["D-577", "D-578"],
    "cowork_phase2_architecture_review.md":
        ["D-579", "D-580"],
    "cowork_information_loss_audit.md":
        ["D-581", "D-582", "D-583"],
}

LOW_YIELD_REASON = {
    "docs/extension_stripping_policy.md":
        "One entry from 232 lines, and the reason is that the document's headline rule is "
        "ALREADY REGISTERED from its owning specification: the analyzer always emits its fullest "
        "reading and simplification happens only on the comparison side is D-304, homed in "
        "`ARCHITECTURE.md`, with its measured defense. What that home does NOT carry is the "
        "comparison side's own rule — that the reference corpus's convention is discovered per "
        "entry rather than declared — and that is the entry.",
    "docs/nct_detection_design.md":
        "One entry from 219 lines, and the reason is the same shape: the deferral AND the "
        "constraint on the eventual design's shape are D-303, homed in `ARCHITECTURE.md`. What "
        "no home carried is the evidence-admissibility clause — that voice slots and stem "
        "direction are structural notational metadata rather than user-written analytical "
        "claims — which binds any voice-tracking work whether or not the detector is built.",
    "cowork_joint_estimator_factorization.md":
        "One entry from 214 lines, and the reason is that this is the register's best-covered "
        "specification: the ratified structure, the factor roster and the desk simulation's "
        "amendments are already carried (D-004, D-006, D-098, D-449, D-450, D-524…D-530, "
        "D-533). What was not carried is the tie-break rule, which entered the specification a "
        "day AFTER the ratification it sits inside, on a measurement made during the C++ "
        "module build.",
}

# -- AUTHORED — the observations this wave's own numbers support --------------
BAND_OBSERVATION = (
    "All fourteen of this wave's documents fall in ONE length tercile — the THIRD consecutive "
    "wave to do so, after wave 2's eight and wave 3's eleven. The proxy therefore made a SINGLE "
    "prediction for the whole packing for the third time running, while the measured yields "
    "differ six-fold within it. Within this wave the length proxy again has no resolving power "
    "at all. Reported as an observation about these fourteen observations and explicitly NOT as "
    "a re-fit: the proxy stays registered as it was and unvalidated (#17d). Three consecutive "
    "single-tercile waves is itself a fact about the SCHEDULE rather than the proxy — the "
    "regime packs waves by estimated token cost, and length is what that estimate is built "
    "from, so a wave packed to a token budget is close to a wave packed by length."
)
WHAT_SEPARATED_THEM = (
    "What separated them, stated as an observation and not as a model, and it is the same "
    "separation waves 2 and 3 reported — now seen three times. The highest yields are documents "
    "that STATE RULES densely and are nobody else's subject: a protocol whose every section is "
    "a rule, a scoping document written entirely as premise-ledger discipline, and a plan whose "
    "own ordering principle is user-ratified. The lowest are documents whose headline rule is "
    "already registered from the specification that owns it — where the wave's yield is the "
    "residue the owning home does not carry, which is one or two clauses rather than none. "
    "Neither is a length effect."
)
WAVE4_NOTE = (
    "This wave's read half ran AFTER its ruling half, which the dispatch ordered as the wave's "
    "first duty, so the read count is what the ruling work left room for rather than what the "
    "schedule packed. The wave-4 packing was taken ENTIRE nonetheless."
)


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build() -> dict:
    regime = load(REGIME)
    backbone = load(BACKBONE)
    prior = [load(p) for p in PRIOR]
    by_id = {d["id"]: d for d in backbone["decisions"]}

    owed = {r["document"]: r for r in regime["owed_rows"]}
    waves = {w["wave"]: w for w in regime["schedule"]["waves"]}
    planned = waves[WAVE_INDEX]["documents"]

    for doc in planned:
        if doc not in WAVE_READS:
            raise SystemExit(f"wave {WAVE_INDEX} of the schedule names {doc}, which this wave "
                             "did not read; the authored list and the schedule disagree")
    for doc in WAVE_READS:
        if doc not in planned:
            raise SystemExit(f"{doc} was read but is not in the schedule's wave-{WAVE_INDEX} "
                             "packing; the authored list and the schedule disagree")

    rows = []
    for doc, ids in WAVE_READS.items():
        if doc not in owed:
            raise SystemExit(f"{doc} is not an owed row of the regime artifact")
        r = owed[doc]
        missing = [i for i in ids if i not in by_id]
        if missing:
            raise SystemExit(f"{doc}: entered ids not in the register: {missing}")
        lo, hi = r["predicted_yield_band"]
        actual = len(ids)
        homed_here = sum(1 for i in ids if by_id[i]["home"].split(":")[0] == doc)
        row = {
            "document": doc,
            "reading_order": r["reading_order"],
            "lines": r["lines"],
            "length_tercile": r["length_tercile"],
            "unresolved_clusters_at_registration": r["unresolved_clusters"],
            "predicted_yield_band": [lo, hi],
            "predicted_yield_point": r["predicted_yield_point"],
            "actual_yield": actual,
            "of_which_homed_in_this_document": homed_here,
            "of_which_homed_in_the_owning_specification": actual - homed_here,
            "of_which_legacy_subject": sum(1 for i in ids if by_id[i].get("legacy_subject")),
            "of_which_process_class": sum(1 for i in ids
                                          if by_id[i].get("nonspec_kind") == "process"),
            "inside_the_registered_band": lo <= actual <= hi,
            "against_the_point_prediction":
                "above" if actual > r["predicted_yield_point"] else
                ("below" if actual < r["predicted_yield_point"] else "equal"),
            "entries": [{"id": i, "home": by_id[i]["home"], "status": by_id[i]["status"],
                         "title": by_id[i]["title"]} for i in ids],
        }
        if doc in LOW_YIELD_REASON:
            row["low_yield_reason"] = LOW_YIELD_REASON[doc]
        rows.append(row)
    rows.sort(key=lambda x: x["reading_order"])

    n = len(rows)
    inside = sum(1 for r in rows if r["inside_the_registered_band"])
    above = sum(1 for r in rows if r["against_the_point_prediction"] == "above")
    below = sum(1 for r in rows if r["against_the_point_prediction"] == "below")
    total = sum(r["actual_yield"] for r in rows)
    homed_elsewhere = sum(r["of_which_homed_in_the_owning_specification"] for r in rows)
    terciles = sorted({r["length_tercile"] for r in rows})

    read_before = regime["partition"]["read_in_full"] + sum(
        p["counts"]["documents_read_in_full_this_wave"] for p in prior)
    surface = regime["partition"]["design_document_surface"]
    excluded = regime["partition"]["user_accepted_exclusions_not_read"]

    return {
        "header": {
            "purpose": "READ WAVE 4's measured yield against the bands registered before the "
                       "reads, per `phase1n_reading_regime.json` -> bands.registration.",
            "generator": "tools/audit/decisions/gen_reads4_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "LOW_YIELD_REASON", "BAND_OBSERVATION",
                                "WHAT_SEPARATED_THEM", "WAVE4_NOTE"],
            "derived_from": ["phase1n_reading_regime.json (every band, point, size and "
                             "partition fact)",
                             "reads1_yield.json + reads2_yield.json + reads3_yield.json "
                             "(the earlier read counts)",
                             "backbone_decisions.json (every home, status, class and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Unchanged from waves 1-3 and rowed at OI-316, now FOUR waves deep: the "
                "generator recomputes the registered bands from the terciles of the READ set, "
                "so following the regime's own update protocol would refit the prediction on "
                "the documents being graded (#20) and lose the registered value (#12).",
            "note_on_this_wave": WAVE4_NOTE,
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_schedule_packed_into_wave_4": len(planned),
            "register_entries_produced": total,
            "entries_homed_in_the_document_read": total - homed_elsewhere,
            "entries_homed_in_the_owning_specification_instead": homed_elsewhere,
            "entries_marked_legacy_subject": sum(r["of_which_legacy_subject"] for r in rows),
            "entries_classed_process": sum(r["of_which_process_class"] for r in rows),
            "documents_yielding_zero": sum(1 for r in rows if r["actual_yield"] == 0),
        },
        "the_running_read_count": {
            "design_document_surface": surface,
            "user_accepted_exclusions_not_read": excluded,
            "read_in_full_before_this_wave": read_before,
            "read_in_full_after_this_wave": read_before + n,
            "still_owed_a_full_read": surface - excluded - (read_before + n),
            "note": "Derived here from the regime's own partition plus the three earlier waves' "
                    "counts, because the regime artifact's own `partition.read_in_full` and "
                    "`owed_a_full_read` cannot be updated without refitting the registered "
                    "bands (OI-316). A reader comparing this block with the regime artifact "
                    "will find them disagreeing BY DESIGN; this block is the current one.",
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "length_terciles_represented_in_this_wave": terciles,
            "what_the_band_test_is_worth":
                "Restated from waves 1-3 because it has not changed and a reader of this "
                "artifact alone would otherwise read a clean pass as evidence: EVERY registered "
                "band has a minimum of 0, so a band running from 0 to its tercile maximum can "
                "only be missed by a document out-yielding every document of its tercile ever. "
                "`inside_the_registered_band` is therefore close to unfalsifiable and a pass on "
                "it establishes almost nothing. The informative comparison is the point "
                "prediction, reported beside it — and BOTH are reported here, per the wave "
                "dispatch's own instruction not to describe a band pass as validating the "
                "proxy.",
            "what_wave_4_adds": BAND_OBSERVATION,
            "what_separated_the_documents": WHAT_SEPARATED_THEM,
        },
        "rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="rebuild into memory and report whether the artifact matches")
    args = ap.parse_args()

    built = build()
    if args.check:
        if not os.path.exists(OUT):
            print("STALE: the artifact does not exist")
            return 1
        if load(OUT) != built:
            print("STALE: reads4_yield.json does not re-derive")
            return 1
        print("reads4_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    t = built["the_out_of_sample_test"]
    r = built["the_running_read_count"]
    print(f"documents read in full: {c['documents_read_in_full_this_wave']} "
          f"(wave-4 packing: {c['documents_the_schedule_packed_into_wave_4']})")
    print(f"register entries produced: {c['register_entries_produced']}  "
          f"(zero-yield documents: {c['documents_yielding_zero']})")
    print(f"inside the registered band: {t['documents_inside_their_registered_band']}"
          f"/{c['documents_read_in_full_this_wave']}   "
          f"above the point prediction: {t['above_the_point_prediction']}   "
          f"below: {t['below_the_point_prediction']}")
    print(f"read in full: {r['read_in_full_after_this_wave']} of "
          f"{r['design_document_surface']}   still owed: {r['still_owed_a_full_read']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
