#!/usr/bin/env python3
"""READ WAVE 3's measured yield, graded against the bands registered BEFORE the reads.

WHAT THIS IS.  `phase1n_reading_regime.json` registered, before any owed document was read, a
predicted yield band and a point prediction for every owed document, so that the length proxy
would be tested OUT OF SAMPLE as a by-product of the reading rather than by a separate study
(#17b, #19, #20).  This is the third instalment of that test: the documents the third dedicated
read wave read in full, each with the band it was registered with, the yield it actually
produced, and the verdict.  The earlier instalments are `reads1_yield.json` and
`reads2_yield.json`.

WHY THE REGISTERED ROWS ARE READ AND NOT RECOMPUTED.  Unchanged from waves 1 and 2, and the
reason is `OPEN_ITEMS.md` OI-316: the regime's own update protocol tells each wave to write its
yield into `actual_yield_when_read`, but the only lawful route to that field recomputes the
bands from the terciles of the READ set — which a read wave changes — so following the protocol
would replace the registered prediction with one fitted on data that now contains the documents
being graded (#20) and would lose the registered value (#12).  So the regime artifact and
`gen_phase1m_measurements.READ_WAVES` are again left untouched, and this artifact reads the
registered rows off the regime as they stand.  The divergence (the regime's owed count does not
move; the read count moves here and in the OI-207 note) is the rowed defect, not a stalled wave.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them; and the two prose observations.  Nothing
             else.
  derived  : every band, every point prediction and every size fact (read off the regime
             artifact); every entry's home, title and status (read off the register data); every
             count and every verdict; the running read total (read off the regime's own
             partition plus waves 1 and 2, never restated).

Run:  python tools/audit/decisions/gen_reads3_yield.py [--check]
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
WAVE1 = os.path.join(HERE, "reads1_yield.json")
WAVE2 = os.path.join(HERE, "reads2_yield.json")
OUT = os.path.join(HERE, "reads3_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# -- AUTHORED — what this wave read, and what it entered from each read -------
# The reading order is the regime's own; this wave took its wave-3 packing entire.
WAVE = "reads-3"
WAVE_DISPATCH = "cc_instruction_reads_3.md"
WAVE_INDEX = 3
WAVE_READS: dict[str, list[str]] = {
    "cowork_progression_schema_design.md":
        ["D-502", "D-503", "D-504", "D-505",
         "D-506", "D-507", "D-508", "D-509"],
    "cowork_gateA_unification_design.md":
        ["D-510", "D-511", "D-512"],
    "cowork_census_full_needs_audit.md":
        ["D-513", "D-514", "D-515", "D-516"],
    "cowork_layer1_note_model_design.md":
        ["D-517", "D-518", "D-519", "D-520"],
    "cowork_evidence_inventory.md":
        ["D-521", "D-522", "D-523"],
    "cowork_joint_estimator_architecture.md":
        ["D-524", "D-525", "D-526", "D-527", "D-528", "D-529", "D-530"],
    "cowork_sensitive_cell_probe.md":
        ["D-532", "D-533", "D-534", "D-535"],
    "docs/iter92_joint_bass_chord_scoring.md":
        ["D-536", "D-537", "D-538"],
    "docs/back_half_design.md":
        ["D-531", "D-539"],
    "cowork_layer2_slicing_design.md":
        ["D-540", "D-541"],
    "cowork_idiom_discovery_design.md":
        ["D-542", "D-543", "D-544", "D-545"],
}

LOW_YIELD_REASON = {
    "docs/back_half_design.md":
        "Two entries from 242 lines, and the reason is that this document's headline finding is "
        "ALREADY REGISTERED from a weaker home. Its convergent finding — that inference "
        "structure cannot move an error the emission model consistently prefers, so precision "
        "lives in the emission and the functional labelling — is D-289, whose only recorded home "
        "is a session-handoff archive while its full derivation is here. The wave did not "
        "duplicate it; it recorded the better home as an OI-296-class observation. What is left "
        "is the ratified fork resolution and the standing decompose-before-building method.",
    "cowork_layer2_slicing_design.md":
        "Two entries from 239 lines, and the reason is that this layer is the register's "
        "best-covered: D-041 through D-050 already carry the slicer's founding decisions, "
        "including the two the document's own decision list leads with (a boundary at every "
        "onset AND every release; explicit empty slices). What was NOT carried is the pair "
        "entered here — the warning that slices are not equal-weight units, and the metric-weight "
        "contract that made 'derived on demand' concrete.",
}

# -- AUTHORED — the two observations this wave's own numbers support ----------
BAND_OBSERVATION = (
    "All eleven of this wave's documents fall in ONE length tercile, exactly as all eight of "
    "wave 2's did — so for the second consecutive wave the proxy makes a SINGLE prediction for "
    "the whole packing while the measured yields differ by a factor of four. Within this wave "
    "the length proxy again has no resolving power at all. Reported as an observation about "
    "these eleven observations and explicitly NOT as a re-fit: the proxy stays registered as it "
    "was and unvalidated (#17d)."
)
WHAT_SEPARATED_THEM = (
    "What separated them, stated as an observation and not as a model: the two highest yields "
    "are a FULLY RATIFIED component specification and the GOVERNING architecture document, both "
    "of which state ratified rules densely; the two lowest are a document whose headline finding "
    "is already registered from another home, and a layer specification the register already "
    "covers well. Neither is a length effect. This is the same shape wave 2 reported and it is "
    "now seen twice, which is worth recording and is still not a fit."
)


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build() -> dict:
    regime = load(REGIME)
    backbone = load(BACKBONE)
    wave1 = load(WAVE1)
    wave2 = load(WAVE2)
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
            "of_which_legacy_subject": sum(1 for i in ids
                                           if by_id[i].get("legacy_subject")),
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

    read_before = (regime["partition"]["read_in_full"]
                   + wave1["counts"]["documents_read_in_full_this_wave"]
                   + wave2["counts"]["documents_read_in_full_this_wave"])
    surface = regime["partition"]["design_document_surface"]
    excluded = regime["partition"]["user_accepted_exclusions_not_read"]

    return {
        "header": {
            "purpose": "READ WAVE 3's measured yield against the bands registered before the "
                       "reads, per `phase1n_reading_regime.json` -> bands.registration.",
            "generator": "tools/audit/decisions/gen_reads3_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "LOW_YIELD_REASON", "BAND_OBSERVATION",
                                "WHAT_SEPARATED_THEM"],
            "derived_from": ["phase1n_reading_regime.json (every band, point, size and "
                             "partition fact)",
                             "reads1_yield.json + reads2_yield.json (the earlier read counts)",
                             "backbone_decisions.json (every home, status and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Unchanged from waves 1 and 2 and rowed at OI-316: the generator recomputes the "
                "registered bands from the terciles of the READ set, so following the regime's "
                "own update protocol would refit the prediction on the documents being graded "
                "(#20) and lose the registered value (#12).",
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_schedule_packed_into_wave_3": len(planned),
            "register_entries_produced": total,
            "entries_homed_in_the_document_read": total - homed_elsewhere,
            "entries_homed_in_the_owning_specification_instead": homed_elsewhere,
            "entries_marked_legacy_subject": sum(r["of_which_legacy_subject"] for r in rows),
            "documents_yielding_zero": sum(1 for r in rows if r["actual_yield"] == 0),
        },
        "the_running_read_count": {
            "design_document_surface": surface,
            "user_accepted_exclusions_not_read": excluded,
            "read_in_full_before_this_wave": read_before,
            "read_in_full_after_this_wave": read_before + n,
            "still_owed_a_full_read": surface - excluded - (read_before + n),
            "note": "Derived here from the regime's own partition plus the two earlier waves' "
                    "counts, because the regime artifact's own `partition.read_in_full` and "
                    "`owed_a_full_read` cannot be updated without refitting the registered bands "
                    "(OI-316). A reader comparing this block with the regime artifact will find "
                    "them disagreeing BY DESIGN; this block is the current one.",
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "length_terciles_represented_in_this_wave": terciles,
            "what_the_band_test_is_worth":
                "Restated from waves 1 and 2 because it has not changed and a reader of this "
                "artifact alone would otherwise read a clean pass as evidence: EVERY registered "
                "band has a minimum of 0, so a band running from 0 to its tercile maximum can "
                "only be missed by a document out-yielding every document of its tercile ever. "
                "`inside_the_registered_band` is therefore close to unfalsifiable and a pass on "
                "it establishes almost nothing. The informative comparison is the point "
                "prediction, reported beside it — and BOTH are reported here, per the wave "
                "dispatch's own instruction not to describe a band pass as validating the proxy.",
            "what_wave_3_adds": BAND_OBSERVATION,
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
            print("STALE: reads3_yield.json does not re-derive")
            return 1
        print("reads3_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    t = built["the_out_of_sample_test"]
    r = built["the_running_read_count"]
    print(f"documents read in full: {c['documents_read_in_full_this_wave']} "
          f"(wave-3 packing: {c['documents_the_schedule_packed_into_wave_3']})")
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
