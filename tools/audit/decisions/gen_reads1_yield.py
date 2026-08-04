#!/usr/bin/env python3
"""READ WAVE 1's measured yield, graded against the bands registered BEFORE the reads.

WHAT THIS IS.  `phase1n_reading_regime.json` registered, before any owed document was read, a
predicted yield band and a point prediction for every owed document, so that the length proxy
would be tested OUT OF SAMPLE as a by-product of the reading rather than by a separate study
(#17b, #19, #20).  This artifact is the first instalment of that test: the six documents the
first dedicated read wave read in full, each with the band it was registered with, the yield it
actually produced, and the verdict.

WHY THE REGISTERED ROWS ARE READ AND NOT RECOMPUTED, stated because it is the load-bearing
choice here.  The regime's `bands.registration` field instructs each read wave to write its
actual yield into `actual_yield_when_read` on the owed row it read.  Doing that through
`gen_phase1n_reading_regime.py` would ALSO move the prediction: that generator recomputes the
bands from the terciles of the READ set's own length distribution, and a document that has just
been read joins the read set — so regenerating after a read replaces the registered prediction
with one fitted on data that now includes the very documents being graded.  A prediction that
moves when it is tested is not a registration, and overwriting it would lose the record (#12).
So this wave does NOT update that generator's read-wave table, and this artifact reads the
registered rows off the regime artifact as they stand.  The gap is rowed, not worked around
(`OPEN_ITEMS.md` OI-316).

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them.  Nothing else.
  derived  : every band, every point prediction and every size fact (read off the regime
             artifact); every entry's home, title and status (read off the register data); every
             count and every verdict.

Run:  python tools/audit/decisions/gen_reads1_yield.py [--check]
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
OUT = os.path.join(HERE, "reads1_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── AUTHORED — what this wave read, and what it entered from each read ────────
# The reading order is the regime's own (`owed_rows` sorted by `reading_order`); this wave took
# its wave-1 packing entire.  The entry lists are this session's own, one per document read.
WAVE = "reads-1"
WAVE_DISPATCH = "cc_instruction_reads_1.md"
WAVE_READS: dict[str, list[str]] = {
    "docs/llm_integration.md":
        ["D-440", "D-441", "D-442", "D-443", "D-444", "D-445", "D-446", "D-447", "D-448"],
    "cowork_factorization_desk_simulation.md":
        ["D-449", "D-450", "D-451", "D-452", "D-453"],
    "docs/key_path_design.md":
        [],
    "cowork_layer6_grouping_design.md":
        ["D-454", "D-455", "D-456", "D-457", "D-458", "D-459", "D-460", "D-461", "D-462"],
    "docs/layer_architecture_audit.md":
        ["D-463", "D-464", "D-465"],
    "cowork_target_architecture.md":
        ["D-466", "D-467"],
}

ZERO_YIELD_REASON = {
    "docs/key_path_design.md":
        "Read in full and yielded nothing. The document is an unratified DRAFT whose own banner "
        "puts it under a ratification hold, and its content is a proposal — a key HMM, its "
        "measurement plan, and four open questions put to the user — not a record of anything "
        "decided. Its one load-bearing finding (a path fixes about a tenth of the target class; "
        "the bulk is a consistently-wrong emission that stickiness entrenches rather than fixes) "
        "is already carried by D-283/D-284/D-289 as the same result reached from three other "
        "directions. Its statements of past decisions belong to other homes, and one of them is "
        "the wave's largest finding rather than an entry (OI-315). This matches the read set's "
        "own pattern: every DRAFT-bannered document read so far has yielded zero.",
}


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build() -> dict:
    regime = load(REGIME)
    backbone = load(BACKBONE)
    by_id = {d["id"]: d for d in backbone["decisions"]}

    owed = {r["document"]: r for r in regime["owed_rows"]}
    planned = regime["schedule"]["waves"][0]["documents"]

    rows = []
    for doc in planned:
        if doc not in WAVE_READS:
            raise SystemExit(f"wave 1 of the schedule names {doc}, which this wave did not read; "
                             "the authored list and the schedule disagree")
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
            "inside_the_registered_band": lo <= actual <= hi,
            "against_the_point_prediction":
                "above" if actual > r["predicted_yield_point"] else
                ("below" if actual < r["predicted_yield_point"] else "equal"),
            "entries": [{"id": i, "home": by_id[i]["home"], "status": by_id[i]["status"],
                         "title": by_id[i]["title"]} for i in ids],
        }
        if doc in ZERO_YIELD_REASON:
            row["zero_yield_reason"] = ZERO_YIELD_REASON[doc]
        rows.append(row)
    rows.sort(key=lambda x: x["reading_order"])

    n = len(rows)
    inside = sum(1 for r in rows if r["inside_the_registered_band"])
    above = sum(1 for r in rows if r["against_the_point_prediction"] == "above")
    below = sum(1 for r in rows if r["against_the_point_prediction"] == "below")
    total = sum(r["actual_yield"] for r in rows)
    homed_elsewhere = sum(r["of_which_homed_in_the_owning_specification"] for r in rows)

    return {
        "header": {
            "purpose": "READ WAVE 1's measured yield against the bands registered before the "
                       "reads, per `phase1n_reading_regime.json` -> bands.registration.",
            "generator": "tools/audit/decisions/gen_reads1_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "ZERO_YIELD_REASON"],
            "derived_from": ["phase1n_reading_regime.json (every band, point and size fact)",
                             "backbone_decisions.json (every home, status and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Its generator recomputes the registered bands from the terciles of the READ "
                "set, which a read wave changes. Regenerating after a read would replace the "
                "registered prediction with one fitted on data including the documents being "
                "graded, destroying the registration (#12, #20). Rowed at OI-316.",
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_schedule_packed_into_wave_1": len(planned),
            "register_entries_produced": total,
            "entries_homed_in_the_document_read": total - homed_elsewhere,
            "entries_homed_in_the_owning_specification_instead": homed_elsewhere,
            "documents_yielding_zero": sum(1 for r in rows if r["actual_yield"] == 0),
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "what_the_band_test_is_worth":
                "Stated rather than left for a reader to infer: EVERY registered band has a "
                "minimum of 0, because every length tercile of the read set contains at least "
                "one zero-yield document. A band running from 0 to its tercile maximum can only "
                "be missed by a document yielding MORE than any document of its tercile ever "
                "has, so `inside_the_registered_band` is close to unfalsifiable and a pass on "
                "it establishes almost nothing. The informative comparison is against "
                "`predicted_yield_point`, reported beside it. The band rule was registered as "
                "deliberately wide (`bands.rule`); this is what that width costs when the "
                "prediction is finally graded.",
            "the_proxy_is_not_established_by_this_wave":
                "Six documents, of which five sit in two adjacent terciles, is not a test that "
                "settles a correlation whose 95% interval on 36 documents already spanned 0.44 "
                "to 0.83 (#24). What this wave contributes is six out-of-sample observations "
                "recorded against a prediction registered before them; no bound rests on the "
                "proxy and `no_tail_is_bounded` is untouched.",
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
            print("STALE: reads1_yield.json does not re-derive")
            return 1
        print("reads1_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    t = built["the_out_of_sample_test"]
    print(f"documents read in full: {c['documents_read_in_full_this_wave']} "
          f"(wave-1 packing: {c['documents_the_schedule_packed_into_wave_1']})")
    print(f"register entries produced: {c['register_entries_produced']}  "
          f"(zero-yield documents: {c['documents_yielding_zero']})")
    print(f"inside the registered band: {t['documents_inside_their_registered_band']}"
          f"/{c['documents_read_in_full_this_wave']}   "
          f"above the point prediction: {t['above_the_point_prediction']}   "
          f"below: {t['below_the_point_prediction']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
