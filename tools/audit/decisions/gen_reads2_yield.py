#!/usr/bin/env python3
"""READ WAVE 2's measured yield, graded against the bands registered BEFORE the reads.

WHAT THIS IS.  `phase1n_reading_regime.json` registered, before any owed document was read, a
predicted yield band and a point prediction for every owed document, so that the length proxy
would be tested OUT OF SAMPLE as a by-product of the reading rather than by a separate study
(#17b, #19, #20).  This artifact is the second instalment of that test: the documents the
second dedicated read wave read in full, each with the band it was registered with, the yield
it actually produced, and the verdict.  The first instalment is `reads1_yield.json`.

WHY THE REGISTERED ROWS ARE READ AND NOT RECOMPUTED.  Unchanged from wave 1, and the reason is
`OPEN_ITEMS.md` OI-316: the regime's own update protocol tells each wave to write its yield
into `actual_yield_when_read`, but the only lawful route to that field recomputes the bands
from the terciles of the READ set — which a read wave changes — so following the protocol would
replace the registered prediction with one fitted on data that now contains the documents being
graded (#20) and would lose the registered value (#12).  So the regime artifact and
`gen_phase1m_measurements.READ_WAVES` are again left untouched, and this artifact reads the
registered rows off the regime as they stand.  The divergence (the regime's owed count does not
move; the read count moves here and in the OI-207 note) is the rowed defect, not a stalled wave.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them.  Nothing else.
  derived  : every band, every point prediction and every size fact (read off the regime
             artifact); every entry's home, title and status (read off the register data); every
             count and every verdict; the running read total (read off the regime's own
             partition plus wave 1's artifact, never restated).

Run:  python tools/audit/decisions/gen_reads2_yield.py [--check]
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
OUT = os.path.join(HERE, "reads2_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── AUTHORED — what this wave read, and what it entered from each read ────────
# The reading order is the regime's own; this wave took its wave-2 packing entire.
WAVE = "reads-2"
WAVE_DISPATCH = "cc_instruction_reads_2.md"
WAVE_INDEX = 2
WAVE_READS: dict[str, list[str]] = {
    "docs/unified_analysis_pipeline.md":
        ["D-469", "D-470", "D-471", "D-472"],
    "cowork_term_theory_grounding.md":
        ["D-473", "D-474", "D-475"],
    "cowork_phrase_boundary_design.md":
        ["D-476", "D-477", "D-478", "D-479", "D-480",
         "D-481", "D-482", "D-483", "D-484", "D-485"],
    "docs/precision_metric_design.md":
        ["D-486"],
    "docs/score_inventory.md":
        ["D-487", "D-488", "D-489"],
    "cowork_fb_redesign_design.md":
        ["D-490", "D-491", "D-492", "D-493"],
    "cowork_architecture_review_2026_07.md":
        ["D-494", "D-495", "D-496", "D-497", "D-498", "D-499", "D-500"],
    "docs/symbol_input_audit.md":
        ["D-501"],
}

LOW_YIELD_REASON = {
    "docs/precision_metric_design.md":
        "One entry from 383 lines, and the reason is the read set's own DRAFT pattern with one "
        "exception. The document is an unratified draft whose banner reads 'DRAFT — UNCOMMITTED' "
        "and which closes 'awaiting Cowork/user ratification before any metric is built' — and "
        "wave 1 recorded that every DRAFT-bannered document read so far had yielded zero. This "
        "one does not, because unlike those its central design was subsequently BUILT and "
        "RATIFIED elsewhere: the fixed-grid duration-weighted union-of-boundaries unit it "
        "designs is the governing hard stop of `CLAUDE.md` gate block (A) (R10-b, 2026-07-06), "
        "and its recommended grid choice (union-of-boundaries, exact) is the one adopted. So "
        "almost everything decision-bearing in it is REGISTERED ALREADY at that block, and what "
        "is left is the one reporting rule the block honours but never states as a rule.",
    "docs/symbol_input_audit.md":
        "One entry from 346 lines. The audit's operating principle is the user's, and its "
        "production half is already registered twice (D-066, D-305); its findings are a "
        "classification of call sites rather than decisions; and its three outstanding "
        "questions were all resolved by DELETION, which D-067 already records. What the register "
        "did not carry is the principle's TOOL clause, which is what the audit's own categories "
        "are graded against.",
}


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build() -> dict:
    regime = load(REGIME)
    backbone = load(BACKBONE)
    wave1 = load(WAVE1)
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

    read_before = (regime["partition"]["read_in_full"]
                   + wave1["counts"]["documents_read_in_full_this_wave"])
    surface = regime["partition"]["design_document_surface"]
    excluded = regime["partition"]["user_accepted_exclusions_not_read"]

    return {
        "header": {
            "purpose": "READ WAVE 2's measured yield against the bands registered before the "
                       "reads, per `phase1n_reading_regime.json` -> bands.registration.",
            "generator": "tools/audit/decisions/gen_reads2_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "LOW_YIELD_REASON"],
            "derived_from": ["phase1n_reading_regime.json (every band, point, size and "
                             "partition fact)",
                             "reads1_yield.json (wave 1's read count)",
                             "backbone_decisions.json (every home, status and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Unchanged from wave 1 and rowed at OI-316: the generator recomputes the "
                "registered bands from the terciles of the READ set, so following the regime's "
                "own update protocol would refit the prediction on the documents being graded "
                "(#20) and lose the registered value (#12).",
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_schedule_packed_into_wave_2": len(planned),
            "register_entries_produced": total,
            "entries_homed_in_the_document_read": total - homed_elsewhere,
            "entries_homed_in_the_owning_specification_instead": homed_elsewhere,
            "documents_yielding_zero": sum(1 for r in rows if r["actual_yield"] == 0),
        },
        "the_running_read_count": {
            "design_document_surface": surface,
            "user_accepted_exclusions_not_read": excluded,
            "read_in_full_before_this_wave": read_before,
            "read_in_full_after_this_wave": read_before + n,
            "still_owed_a_full_read": surface - excluded - (read_before + n),
            "note": "Derived here from the regime's own partition plus wave 1's count, because "
                    "the regime artifact's own `partition.read_in_full` and `owed_a_full_read` "
                    "cannot be updated without refitting the registered bands (OI-316). A reader "
                    "comparing this block with the regime artifact will find them disagreeing "
                    "BY DESIGN; this block is the current one.",
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "what_the_band_test_is_worth":
                "Restated from wave 1 because it has not changed and a reader of this artifact "
                "alone would otherwise read a clean pass: EVERY registered band has a minimum "
                "of 0, so a band running from 0 to its tercile maximum can only be missed by a "
                "document out-yielding every document of its tercile ever. "
                "`inside_the_registered_band` is therefore close to unfalsifiable and a pass on "
                "it establishes almost nothing. The informative comparison is the point "
                "prediction, reported beside it.",
            "what_wave_2_adds_that_wave_1_could_not":
                "All eight of this wave's documents fall in ONE length tercile (medium), so "
                "every one carries the same registered band and the same point prediction while "
                "their measured yields differ by an order of magnitude. Within this wave, "
                "therefore, the length proxy has no resolving power AT ALL — it makes one "
                "prediction for eight documents — and what actually separated them is visible "
                "in the rows: a SIGNED layer specification and a ratified amendment list yielded "
                "most of the entries, while an unratified draft and an audit whose findings were "
                "already registered yielded one each. That is a statement about this wave's own "
                "eight observations and is NOT a re-fit of the proxy, which stays registered as "
                "it was and unvalidated (#17d).",
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
            print("STALE: reads2_yield.json does not re-derive")
            return 1
        print("reads2_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    t = built["the_out_of_sample_test"]
    r = built["the_running_read_count"]
    print(f"documents read in full: {c['documents_read_in_full_this_wave']} "
          f"(wave-2 packing: {c['documents_the_schedule_packed_into_wave_2']})")
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
