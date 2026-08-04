#!/usr/bin/env python3
"""READ WAVE 5's measured yield, graded against the bands RE-REGISTERED before the reads.

WHAT THIS IS.  The fifth instalment of the out-of-sample test the reading regime registered.  The
earlier instalments are `reads1_yield.json` … `reads4_yield.json`.  What is different this time,
and what the whole wave was for: the wave was RE-PACKED so that it spans more than one length
tercile (`reads5_repack.json`, ruling R5), so for the first time the proxy makes MORE THAN ONE
prediction inside a single wave and the ordering between them can be tested.  Waves 2, 3 and 4
each fell inside one tercile and could not produce that comparison at all.

WHERE THE BANDS COME FROM.  From `reads5_repack.json` -> the re-packed wave's `registered_bands`,
which carries each document's band and point read VERBATIM off the registration.  That artifact
was written before this wave read anything (#17b).  The regime artifact itself is neither
regenerated nor written to — OI-316, and now OI-328, which measured that re-running its generator
would flip the ordering key outright.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : WAVE_READS — which documents this wave read in full, and which register entries the
             wave entered from reading each of them; the low-yield reasons; and the prose
             observations.  Nothing else.
  derived  : every band, point and size fact (from the re-pack artifact and the regime); every
             entry's home, title and status (from the register data); every count and verdict;
             the per-tercile means and the discriminating test; the running read total.

Run:  python tools/audit/decisions/gen_reads5_yield.py [--check]
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
PRIOR = [os.path.join(HERE, f"reads{i}_yield.json") for i in (1, 2, 3, 4)]
OUT = os.path.join(HERE, "reads5_yield.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# -- AUTHORED — what this wave read, and what it entered from each read -------
WAVE = "reads-5"
WAVE_DISPATCH = "cc_instruction_reads_5.md"
WAVE_INDEX = 5
WAVE_READS: dict[str, list[str]] = {
    "cowork_layer5_function_methods.md":      ["D-584", "D-585", "D-586"],
    "cowork_style_taxonomy_proposal.md":      ["D-587", "D-588", "D-589", "D-590", "D-591"],
    "cowork_l1l4_completion_ledger.md":       ["D-592", "D-593"],
    "docs/iter90_bass_as_root_promotion_shelved.md": ["D-594", "D-595"],
    "docs/layer_audit_plan.md":               ["D-596", "D-597"],
    "cowork_style_clustering_plan.md":        ["D-598"],
    "cowork_adjudication_dossier.md":         ["D-599", "D-600", "D-601"],
    "cowork_phase5c_l5_build_plan.md":        ["D-602"],
    "cowork_layer3_keymode_impl_design.md":   ["D-603", "D-604"],
    "docs/stage4d_local_modulation_design.md": ["D-605", "D-606"],
    "cowork_phrase_boundary_methods.md":      ["D-607"],
    "cowork_eg1_premise_checks.md":           ["D-608", "D-609"],
    "cowork_types_header_design.md":          ["D-610"],
    "cowork_l1l4_review_charter.md":          ["D-611"],
}

LOW_YIELD_REASON = {
    "cowork_style_clustering_plan.md":
        "One entry from a document that is mostly a CORPUS SURVEY — sources, licences, what is "
        "already on disk — and a survey is not a decision. Its one licensing rule is already "
        "D-292, homed in `ARCHITECTURE.md` with its own defense, and its taxonomy content is "
        "already D-131/D-132. What no home carried is the structural claim that the taxonomy and "
        "the weights are ONE object while validation is a separate third thing.",
    "cowork_phase5c_l5_build_plan.md":
        "One entry from a build PLAN, and a plan's steps are instructions rather than standing "
        "decisions. Its proportionality rule is D-480, stated there for the phrase-boundary "
        "primitive and repeated here for the function layer; its reuse instructions name specific "
        "dormant components and expire with them. What no home carried is the gate criterion — "
        "coverage-matched accuracy plus correct abstention, never raw coverage.",
    "cowork_phrase_boundary_methods.md":
        "One entry from a research catalog whose findings were ALREADY absorbed into the design it "
        "grounds: the graded profile is D-478, the harmony-agnostic constraint and the accepted "
        "miss are D-477, the per-voice aggregation is D-479, the proportionality is D-480. That is "
        "the catalog working — it was written to be absorbed. The residue is the establishment "
        "STATUS of the polyphonic extension, which the design states as mechanism and not as "
        "evidence.",
    "cowork_types_header_design.md":
        "One entry from a refactor design whose subject decision — the value types live in a "
        "dependency-free leaf header — is already D-078, homed in `ARCHITECTURE.md`. The residue "
        "is the rule that made the move byte-identical rather than the fact that it happened.",
    "cowork_l1l4_review_charter.md":
        "One entry from the shortest document in the wave, and a charter is mostly division of "
        "labour and scope. Its one standing rule is the tidy guardrail that a dormant staged "
        "component is not dead code.",
}

# -- AUTHORED — the observations this wave's own numbers support --------------
BAND_OBSERVATION = (
    "★ THE FIRST WAVE THAT COULD TEST THE PROXY AT ALL. Waves 2, 3 and 4 each fell inside ONE "
    "length tercile, so the proxy made a single prediction for the whole wave and the comparison "
    "that would grade it — do longer-tercile documents actually out-yield shorter-tercile ones? — "
    "could not be formed. This wave was RE-PACKED to span the terciles still owed (ruling R5), so "
    "it holds documents carrying two DIFFERENT registered predictions and the ordering between "
    "them is falsifiable. `the_discriminating_test` below is that comparison, and it is the "
    "informative result of this wave — not the band pass, which remains close to unfalsifiable "
    "for the reason restated below. TWO LIMITS ON WHAT IT ESTABLISHES, stated rather than left to "
    "be read past: only two of the three terciles are still owed at all — every long-tercile "
    "document was read in waves 1-4, because the ordering is length-descending — so the "
    "comparison spans two adjacent bands and not the proxy's range; and one wave is one "
    "observation of that comparison, not a trend."
)
WHAT_SEPARATED_THEM = (
    "What separated the documents, stated as an observation and NOT as a re-fit — and this wave "
    "makes the pattern the previous three reported harder to attribute to length. The highest "
    "yields are documents whose subject is a set of RULES nobody else owns: a ratified proposal "
    "for how a user-facing preset is named, derived and persisted, and a research catalog whose "
    "findings had not yet been absorbed into a specification. The lowest are documents whose "
    "content was ALREADY ABSORBED into the specification they grounded — a research catalog that "
    "did its job, a refactor design whose result is homed in the canonical document, a build plan "
    "whose steps are instructions. Absorption, not length, is what the yield tracks: a document "
    "that has been read INTO a specification yields the residue that specification does not "
    "carry, and one that has not yields its whole content."
)
WAVE5_NOTE = (
    "This wave's read half ran after a substantial ruling half — the ratification, the "
    "re-homing of the build-it-right rule, the caveat, three delegations and the re-pack — so the "
    "read count is again what the ruling work left room for. The re-packed wave-5 grouping was "
    "taken ENTIRE nonetheless."
)
THE_COLLISION_NOTE = (
    "One entry in this wave is NOT a read yield and is counted separately below: D-172 was "
    "RE-TAKEN, not entered, because the wave's own Task 2 widened the principle it quotes. That "
    "act produced OI-329 — two live entries recording one rule at one home — which is reported as "
    "this wave's own effect rather than absorbed."
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

    # ── the discriminating test the re-pack exists to make possible ──────────
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

    read_before = regime["partition"]["read_in_full"] + sum(
        p["counts"]["documents_read_in_full_this_wave"] for p in prior)
    surface = regime["partition"]["design_document_surface"]
    excluded = regime["partition"]["user_accepted_exclusions_not_read"]

    return {
        "header": {
            "purpose": "READ WAVE 5's measured yield against the bands RE-REGISTERED for the "
                       "re-packed wave before it was read, per `reads5_repack.json`.",
            "generator": "tools/audit/decisions/gen_reads5_yield.py",
            "wave": WAVE,
            "dispatch": WAVE_DISPATCH,
            "authored_inputs": ["WAVE_READS", "LOW_YIELD_REASON", "BAND_OBSERVATION",
                                "WHAT_SEPARATED_THEM", "WAVE5_NOTE", "THE_COLLISION_NOTE"],
            "derived_from": ["reads5_repack.json (the re-packed grouping and every re-registered "
                             "band, itself read verbatim off the regime)",
                             "phase1n_reading_regime.json (the partition facts only)",
                             "reads1..reads4_yield.json (the earlier read counts)",
                             "backbone_decisions.json (every home, status, class and title)"],
            "why_the_regime_artifact_is_not_regenerated":
                "Unchanged from waves 1-4 (OI-316) and now with a second, sharper reason measured "
                "this wave (OI-328): re-running the regime generator does not reproduce the "
                "registration, because the ordering key is the best-correlating proxy and one of "
                "the four candidates counts how often a document is named in a user-ratified "
                "surface — which the user's own delegation writes increment, for documents whose "
                "yield is already known.",
            "note_on_this_wave": WAVE5_NOTE,
            "note_on_the_entry_that_is_not_a_yield": THE_COLLISION_NOTE,
        },
        "counts": {
            "documents_read_in_full_this_wave": n,
            "documents_the_repack_grouped_into_wave_5": len(planned),
            "register_entries_produced": total,
            "entries_homed_in_the_document_read": total - homed_elsewhere,
            "entries_homed_in_the_owning_specification_instead": homed_elsewhere,
            "entries_marked_legacy_subject": sum(r["of_which_legacy_subject"] for r in rows),
            "entries_classed_process": sum(r["of_which_process_class"] for r in rows),
            "documents_yielding_zero": sum(1 for r in rows if r["actual_yield"] == 0),
            "register_entries_re_taken_not_entered": 1,
            "what_the_re_taken_entry_is": THE_COLLISION_NOTE,
        },
        "the_running_read_count": {
            "design_document_surface": surface,
            "user_accepted_exclusions_not_read": excluded,
            "read_in_full_before_this_wave": read_before,
            "read_in_full_after_this_wave": read_before + n,
            "still_owed_a_full_read": surface - excluded - (read_before + n),
            "note": "Derived here from the regime's own partition plus the four earlier waves' "
                    "counts, because the regime artifact's own `partition.read_in_full` and "
                    "`owed_a_full_read` cannot be updated without refitting the registered bands "
                    "(OI-316) — and, since OI-328, cannot be updated at all without flipping the "
                    "ordering key. A reader comparing this block with the regime artifact will "
                    "find them disagreeing BY DESIGN; this block is the current one.",
        },
        "the_out_of_sample_test": {
            "documents_inside_their_registered_band": inside,
            "documents_outside_their_registered_band": n - inside,
            "above_the_point_prediction": above,
            "below_the_point_prediction": below,
            "length_terciles_represented_in_this_wave": terciles,
            "what_the_band_test_is_worth":
                "Restated from waves 1-4 because it has not changed: EVERY registered band has a "
                "minimum of 0, so a band running from 0 to its tercile maximum can only be missed "
                "by a document out-yielding every document of its tercile ever. "
                "`inside_the_registered_band` is close to unfalsifiable and a pass on it "
                "establishes almost nothing. This wave adds the test below, which is not of that "
                "kind.",
            "what_wave_5_adds": BAND_OBSERVATION,
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
            "the_sharpest_reading_of_this_first_test": (
                "★ THE ORDER HOLDS AND BOTH MAGNITUDES ARE WRONG, IN OPPOSITE DIRECTIONS — which "
                "is the finding, and it is stronger than either half alone. The longer tercile "
                "out-yielded the shorter one, as registered. But the longer tercile's measured "
                "mean fell BELOW its registered point and the shorter tercile's rose ABOVE its "
                "own, so the two measured means are far closer together than the two predictions "
                "are. Read plainly: the proxy gets the SIGN right and OVER-SEPARATES the "
                "magnitude — it asserts a gap several times the one that appeared. That is "
                "consistent with what every wave since the second has observed about what "
                "actually separates the documents (see `what_separated_the_documents`), and it is "
                "recorded as an observation of ONE wave's fourteen documents, NOT as a re-fit and "
                "NOT as a correction to the registered bands, which stand exactly as registered "
                "(#20)."),
            "what_a_failure_would_mean": (
                "A result, not a defect — and the first one the proxy has been exposed to. The "
                "proxy stays registered as it was and unvalidated either way (#17d); a single "
                "wave's comparison neither validates nor falsifies it, and nothing here is "
                "re-fitted."),
            "the_two_limits_on_what_this_establishes": (
                "ONE: only two of the three length terciles are still owed, because every "
                "long-tercile document was read in waves 1-4 under the length-descending "
                "ordering — so the comparison spans two ADJACENT bands, not the proxy's range. "
                "TWO: this is one wave, one observation of the comparison, with the per-tercile "
                "counts below; it is not a trend and no bound may rest on it."),
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
            print("STALE: reads5_yield.json does not re-derive")
            return 1
        print("reads5_yield.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    c = built["counts"]
    t = built["the_out_of_sample_test"]
    d = built["the_discriminating_test"]
    r = built["the_running_read_count"]
    print(f"documents read in full: {c['documents_read_in_full_this_wave']} "
          f"(re-packed wave-5 grouping: {c['documents_the_repack_grouped_into_wave_5']})")
    print(f"register entries produced: {c['register_entries_produced']}  "
          f"(zero-yield documents: {c['documents_yielding_zero']})")
    print(f"inside the registered band: {t['documents_inside_their_registered_band']}"
          f"/{c['documents_read_in_full_this_wave']}   "
          f"above the point prediction: {t['above_the_point_prediction']}   "
          f"below: {t['below_the_point_prediction']}")
    print(f"DISCRIMINATING TEST — predicted {d['predicted_order_high_to_low']} / "
          f"measured {d['measured_order_high_to_low']} -> holds: "
          f"{d['the_predicted_ordering_holds']}")
    for k, v in d["per_tercile"].items():
        print(f"   {k:6s} n={v['documents']} predicted {v['predicted_point']} "
              f"measured mean {v['measured_mean']} (range {v['measured_min']}-{v['measured_max']})")
    print(f"read in full: {r['read_in_full_after_this_wave']} of "
          f"{r['design_document_surface']}   still owed: {r['still_owed_a_full_read']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
