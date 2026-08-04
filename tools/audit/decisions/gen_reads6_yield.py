#!/usr/bin/env python3
"""READ WAVE 6's measured yield — the LAST owed wave — against the bands re-registered before it.

WHAT THIS IS.  The sixth and final instalment of the out-of-sample test the reading regime
registered.  The earlier instalments are `reads1_yield.json` … `reads5_yield.json`.  Wave 6 is the
whole remainder of the owed set, so when it lands the reading programme's owed population is empty.

THE SECOND REAL TEST OF THE PROXY.  Waves 2, 3 and 4 each fell inside ONE length tercile and could
not form the comparison that grades the proxy at all; ruling R5 re-packed the remainder so a wave
SPANS terciles, and wave 5 produced the first real test.  This is the second — and two observations
is still two.  Nothing here describes the proxy as validated.

WHERE THE BANDS COME FROM.  From `reads5_repack.json` -> the re-packed wave-6 `registered_bands`,
which carries each document's band and point read VERBATIM off the registration and was written
BEFORE this wave read anything (#17b).  The regime artifact itself is neither regenerated nor
written to — OI-316, and OI-328, which measured that re-running its generator flips the ordering key.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them; the low-yield reasons; and the prose
             observations.  Nothing else.
  derived  : every band, point and size fact (from the re-pack artifact and the regime); every
             entry's home, title and status (from the register data); every count and verdict; the
             per-tercile means and the discriminating test; the running read total; and the owed
             remainder.

Run:  python tools/audit/decisions/gen_reads6_yield.py [--check]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REGIME = os.path.join(HERE, "phase1n_reading_regime.json")
REPACK = os.path.join(HERE, "reads5_repack.json")
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
PRIOR = [os.path.join(HERE, f"reads{i}_yield.json") for i in (1, 2, 3, 4, 5)]
OUT = os.path.join(HERE, "reads6_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# -- AUTHORED — what this wave read, and what it entered from each read -------
WAVE = "reads-6"
WAVE_DISPATCH = "cc_instruction_reads_6.md"
WAVE_INDEX = 6
WAVE_READS: dict[str, list[str]] = {
    "cowork_union_search_record.md":            ["D-612", "D-613", "D-614"],
    "cowork_l1_l5_premise_debt_audit.md":       ["D-615"],
    "docs/stage4c_cadence_key_design.md":       ["D-616", "D-617"],
    "docs/architecture_joint_inference.md":     ["D-618", "D-619", "D-620", "D-621"],
    "cowork_layer3_reachback_design.md":        ["D-622", "D-623", "D-624"],
    "cowork_tpc_capability_design.md":          ["D-625", "D-626"],
    "cowork_layer1_extend_design.md":           ["D-627", "D-628"],
    "cowork_uncertain_resolver_investigation.md": ["D-629", "D-630"],
    "cowork_layer2_reslice_design.md":          ["D-631", "D-632"],
    "cowork_key_mode_inference_diagnosis.md":   ["D-633"],
    "cowork_delta_check_dispositions.md":       ["D-634", "D-635"],
    "cowork_phase5b_l4_build_plan.md":          ["D-636", "D-637"],
    "cowork_gate_policy_amendment.md":          ["D-638"],
}

LOW_YIELD_REASON = {
    "cowork_l1_l5_premise_debt_audit.md":
        "One entry from a 143-line audit, and the reason is ABSORPTION of the sharpest kind: this "
        "audit's own findings BECAME the Stage-3 entry gate. Its Tier-1 traps are `OPEN_ITEMS.md` "
        "OI-1 through OI-5 and its Tier-3 holes are OI-5 through OI-7 — every one already rowed, "
        "with the arc plan amended to carry the gate. What no row carries as a standing "
        "consequence is the Tier-2 statement: under #19 the validation basis of the hand-set "
        "scoring magnitudes is retroactively void.",
    "cowork_key_mode_inference_diagnosis.md":
        "One entry from a document that is a registered PREDICTION rather than a decision surface "
        "— six candidate causes, each with a written quantitative range recorded before anything "
        "was measured (#17b), which is what it was written to be. A prediction is not a decision, "
        "and its facts are already registered from their own homes. The residue is the one clause "
        "that binds any future diagnostic of the same shape: establish the classifier against the "
        "established column before reading its results.",
    "cowork_gate_policy_amendment.md":
        "One entry from the shortest document in the wave, and it is the most absorbed document "
        "the programme has read: the amendment it proposes was RATIFIED and folded into "
        "`CLAUDE.md`'s gate block, where **D-191** carries it. The residue is the root-cause "
        "attribution clause D-191's verbatim does not include — and it is entered at `CLAUDE.md`, "
        "the surface that owns the rule, not at the proposal.",
}

# -- AUTHORED — the observations this wave's own numbers support --------------
BAND_OBSERVATION = (
    "THE SECOND REAL TEST, AND IT AGREES WITH THE FIRST — which is worth exactly what two "
    "observations are worth and no more. Wave 5 was the first wave that could form the "
    "discriminating comparison at all, after ruling R5 re-packed the remainder to span terciles; "
    "this is the second and last. `the_discriminating_test` below is the informative result. The "
    "band pass beside it is NOT, for the reason every wave since the first has restated: every "
    "registered band has a minimum of 0, so a band running from 0 to its tercile maximum can only "
    "be missed by a document out-yielding every document of its tercile ever. THE SAME TWO LIMITS "
    "AS WAVE 5 STILL BIND: only two of the three terciles were still owed at the re-pack, because "
    "every long-tercile document was read in waves 1-4 under the length-descending ordering, so "
    "the comparison spans two ADJACENT bands rather than the proxy's range; and two waves are two "
    "observations, not a trend. The proxy is NOT validated by this wave and nothing rests on it "
    "(#17d)."
)
WHAT_SEPARATED_THEM = (
    "What separated the documents, stated as an observation and NOT as a re-fit — and it is the "
    "same thing wave 5 named, now visible in a population that includes three near-zero cases. "
    "The yield tracks ABSORPTION, not size. The highest-yielding document of this wave is a "
    "superseded architecture proposal whose MEASURED facts no successor carries — the signature's "
    "measured pin-wrong rate, the three reading-shaped producers' error rates — so its content was "
    "never absorbed anywhere. The lowest are documents whose content was read INTO something else "
    "and is already registered from there: an audit whose findings became the entry-gate rows, a "
    "premise-gate document that is a prediction rather than a decision, and a gate-policy proposal "
    "that was ratified into the governing document. A document that has been absorbed yields the "
    "residue its absorbing home does not carry; one that has not yields its whole content. Length "
    "predicts this only insofar as it correlates with it."
)
WAVE6_NOTE = (
    "This wave's read half again ran after a substantial ruling half — a 28-entry ratification, a "
    "pointer written into the governing document's principle #8, a duplicate register entry "
    "resolved, a delegation written and one deliberately not written, and the guard population "
    "classified per tool. The wave-6 grouping was nonetheless taken ENTIRE, which it had to be: it "
    "is the whole remainder."
)
THE_LAST_WAVE_NOTE = (
    "THIS IS THE LAST OWED WAVE. `reads5_repack.json` -> `the_remainder` groups the entire "
    "remaining owed set into waves 5 and 6, and wave 5 read its whole packing. So "
    "`still_owed_a_full_read` below is the programme's own answer to whether the owed set is "
    "empty, derived here rather than asserted — and it is derived the same way every wave since "
    "the first has derived it, from the regime's partition plus each completed wave's own count, "
    "because the regime artifact cannot be updated (OI-316, OI-328)."
)


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build() -> dict:
    regime = load(REGIME)
    repack = load(REPACK)
    backbone = load(BACKBONE)
    prior = [load(p) for p in PRIOR]
    by_id = {d["id"]: d for d in backbone["decisions"]}

    wave = next(w for w in repack["repacked_waves"] if w["wave"] == WAVE_INDEX)
    bands = {r["document"]: r for r in wave["registered_bands"]}
    planned = wave["documents"]

    for doc in planned:
        if doc not in WAVE_READS:
            raise SystemExit(f"the re-packed wave {WAVE_INDEX} names {doc}, which this wave did "
                             "not read; the authored list and the re-pack disagree")
    for doc in WAVE_READS:
        if doc not in planned:
            raise SystemExit(f"{doc} was read but is not in the re-packed wave-{WAVE_INDEX} "
                             "grouping; the authored list and the re-pack disagree")

    rows = []
    for doc, ids in WAVE_READS.items():
        r = bands[doc]
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

    per_t = {}
    for t in terciles:
        vals = [r["actual_yield"] for r in rows if r["length_tercile"] == t]
        pts = {r["predicted_yield_point"] for r in rows if r["length_tercile"] == t}
        per_t[t] = {"documents": len(vals),
                    "predicted_point": sorted(pts)[0] if len(pts) == 1 else sorted(pts),
                    "measured_mean": round(sum(vals) / len(vals), 2),
                    "measured_min": min(vals), "measured_max": max(vals),
                    "measured_yields": sorted(vals, reverse=True)}
    order_pred = [t for t in sorted(terciles, key=lambda t: -per_t[t]["predicted_point"])]
    order_meas = [t for t in sorted(terciles, key=lambda t: -per_t[t]["measured_mean"])]

    # the wave-5 comparison, read off that wave's own artifact rather than restated
    w5 = next(p for p in prior if p["header"]["wave"] == "reads-5")
    w5_test = w5["the_discriminating_test"]

    read_before = regime["partition"]["read_in_full"] + sum(
        p["counts"]["documents_read_in_full_this_wave"] for p in prior)
    surface = regime["partition"]["design_document_surface"]
    excluded = regime["partition"]["user_accepted_exclusions_not_read"]
    still_owed = surface - excluded - (read_before + n)

    return {
        "header": {
            "purpose": "READ WAVE 6's measured yield — the LAST owed wave — against the bands "
                       "re-registered for the re-packed wave before it was read, per "
                       "`reads5_repack.json`.",
            "generator": "tools/audit/decisions/gen_reads6_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "LOW_YIELD_REASON", "BAND_OBSERVATION",
                                "WHAT_SEPARATED_THEM", "WAVE6_NOTE", "THE_LAST_WAVE_NOTE"],
            "derived_from": ["reads5_repack.json (the re-packed grouping and every re-registered "
                             "band, itself read verbatim off the regime)",
                             "phase1n_reading_regime.json (the partition facts only)",
                             "reads1..reads5_yield.json (the earlier read counts, and wave 5's "
                             "own discriminating test, read off that artifact rather than "
                             "restated)",
                             "backbone_decisions.json (every home, status, class and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Unchanged from waves 1-5: OI-316 (the update protocol cannot be followed without "
                "refitting the registered bands on the data being graded, #20) and OI-328 (a "
                "measured, sharper instance — re-running the generator flips the ordering key, "
                "because a candidate proxy counts namings in user-ratified surfaces and the "
                "register's own homing work increments it for documents whose yield is already "
                "known).",
            "note_on_this_wave": WAVE6_NOTE,
            "note_on_this_being_the_last_wave": THE_LAST_WAVE_NOTE,
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_repack_grouped_into_wave_6": len(planned),
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
            "still_owed_a_full_read": still_owed,
            "the_owed_set_is_empty": still_owed == 0,
            "note": "Derived here from the regime's own partition plus the five earlier waves' "
                    "counts, because the regime artifact's own `partition.read_in_full` and "
                    "`owed_a_full_read` cannot be updated without refitting the registered bands "
                    "(OI-316) and cannot be updated at all without flipping the ordering key "
                    "(OI-328). A reader comparing this block with the regime artifact will find "
                    "them disagreeing BY DESIGN; this block is the current one.",
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "length_terciles_represented_in_this_wave": terciles,
            "what_the_band_test_is_worth":
                "Unchanged from waves 1-5: EVERY registered band has a minimum of 0, so "
                "`inside_the_registered_band` is close to unfalsifiable and a pass on it "
                "establishes almost nothing. The informative comparison is below.",
            "what_wave_6_adds": BAND_OBSERVATION,
            "what_separated_the_documents": WHAT_SEPARATED_THEM,
        },
        "the_discriminating_test": {
            "what_it_is": (
                "The comparison the re-pack exists to make possible, registered before this wave "
                "read anything: within ONE wave, do the documents of the longer length tercile "
                "out-yield the documents of the shorter one, in the order their registered point "
                "predictions assert?"),
            "per_tercile": per_t,
            "predicted_order_high_to_low": order_pred,
            "measured_order_high_to_low": order_meas,
            "the_predicted_ordering_holds": order_pred == order_meas,
            "the_second_observation_against_the_first": {
                "wave_5_ordering_held": w5_test["the_predicted_ordering_holds"],
                "wave_5_per_tercile": w5_test["per_tercile"],
                "how_to_read_the_pair":
                    "Wave 5 found the predicted ORDER holding and BOTH MAGNITUDES wrong in "
                    "OPPOSITE directions — the longer tercile below its registered point, the "
                    "shorter above its own, so the measured means far closer together than the "
                    "predictions. Compare the two `per_tercile` blocks directly rather than "
                    "through any restatement here. WHATEVER THE AGREEMENT, THE PROXY IS NOT "
                    "DESCRIBED AS VALIDATED: two observations of one comparison, both confined to "
                    "the two adjacent terciles that remained owed, cannot establish a correlation "
                    "whose 95 % interval on 36 documents already spanned most of the positive "
                    "range (#24). It is registered as it was and unvalidated (#17d).",
            },
            "what_a_failure_would_mean": (
                "A result, not a defect. The proxy stays registered as it was and unvalidated "
                "either way; nothing is re-fitted and the registered bands stand exactly as "
                "registered (#20)."),
            "the_two_limits_on_what_this_establishes": (
                "ONE: only two of the three length terciles were still owed at the re-pack, "
                "because every long-tercile document was read in waves 1-4 under the "
                "length-descending ordering — so the comparison spans two ADJACENT bands, not the "
                "proxy's range. TWO: this is the second and LAST wave, so the comparison has two "
                "observations and will get no more from this programme."),
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
            print("STALE: reads6_yield.json does not re-derive")
            return 1
        print("reads6_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  documents read {c['documents_read_in_full_this_wave']} · "
          f"entries {c['register_entries_produced']} · "
          f"still owed {built['the_running_read_count']['still_owed_a_full_read']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
