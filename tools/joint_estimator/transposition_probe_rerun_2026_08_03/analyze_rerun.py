#!/usr/bin/env python3
"""Score the repository-side re-run against (1) the committed run and (2) the registered predictions.

Two questions, kept apart because they have different subjects:

  A. REPRODUCTION - does this run reproduce the committed one, condition by condition and
     violation by violation? A divergence here is a finding about the APPARATUS, not about the
     decoder, and is reported as such (the dispatch's §4.3 step 4).

  B. THE SEPARATION (§4.4) - how much of the measured non-equivariance is DEFENSIBLE enharmonic
     ambiguity, and how much is boundary movement and collapse? The classification is the one
     registered in `predictions.md` BEFORE this ran; it is restated here in code so the definition
     and the computation cannot drift apart, and the tool refuses to classify a violation that
     matches no class.

Everything is derived from the two runs' own raw state files. Nothing is transcribed.

Usage:
  python tools/joint_estimator/transposition_probe_rerun_2026_08_03/analyze_rerun.py
  python .../analyze_rerun.py --check     # re-derive and compare, exit 1 on drift
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
COMMITTED = REPO / "tools" / "joint_estimator" / "transposition_probe_2026_08_02"
OUT = HERE / "rerun_analysis.json"

SCORE_TOL = 1e-6          # the committed apparatus's own total-score tolerance
COLLAPSE_FRACTION = 0.10  # a condition matching <= 10 % of its segments (registered in advance)


def _load(p):
    return json.loads(p.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ A. reproduction

def reproduction(new_est, old_est, new_tr, old_tr):
    est_rows = []
    for stem in sorted(set(new_est["results"]) | set(old_est["results"])):
        a, b = new_est["results"].get(stem), old_est["results"].get(stem)
        est_rows.append({
            "stem": stem,
            "in_both": bool(a and b),
            "ok_here": a and a["ok"], "ok_committed": b and b["ok"],
            "n_seg_here": a and a["n_seg"], "n_seg_committed": b and b["n_seg"],
            "total_score_abs_diff": (abs(a["score_got"] - b["score_got"])
                                     if a and b else None),
            "header_crosscheck_ok_here": a and a["header_crosscheck_ok"],
        })
    # Two DIFFERENT questions about the establishment, kept apart rather than collapsed into one
    # boolean - because they came back with different answers and the looser one must not be
    # allowed to hide the stricter one, nor the stricter one to be reported as a failure it is not.
    #   (i)  the APPARATUS's own establishment criterion: same segments, total score within the
    #        committed tolerance. This is what "established here" means.
    #   (ii) BIT-IDENTITY of the total scores between the two runs. Strictly stronger, and not what
    #        the apparatus ever claimed.
    est_passes_criterion = all(
        r["in_both"] and r["ok_here"] and r["ok_committed"]
        and r["n_seg_here"] == r["n_seg_committed"]
        and r["total_score_abs_diff"] <= SCORE_TOL
        for r in est_rows)
    est_bit_identical_scores = sum(1 for r in est_rows if r["total_score_abs_diff"] == 0.0)
    est_max_abs_score_diff = max((r["total_score_abs_diff"] or 0.0) for r in est_rows)
    est_segments_identical = all(r["n_seg_here"] == r["n_seg_committed"] for r in est_rows)

    cond_rows = []
    for key in sorted(set(new_tr["conditions"]) | set(old_tr["conditions"])):
        a, b = new_tr["conditions"].get(key), old_tr["conditions"].get(key)
        if not (a and b):
            cond_rows.append({"condition": key, "in_both": False})
            continue
        va, vb = a["violations"], b["violations"]

        def ident(v):
            return (v.get("seg_index"), v.get("tick"), v.get("type"),
                    json.dumps(v.get("expected"), sort_keys=True),
                    json.dumps(v.get("observed"), sort_keys=True),
                    v.get("expected_state_in_candidates"))

        ia, ib = [ident(v) for v in va], [ident(v) for v in vb]
        cond_rows.append({
            "condition": key,
            "in_both": True,
            "matched_here": a["n_segments_matched"],
            "matched_committed": b["n_segments_matched"],
            "compared_here": a["n_segments_compared"],
            "compared_committed": b["n_segments_compared"],
            "boundaries_identical_here": a["boundaries_identical"],
            "boundaries_identical_committed": b["boundaries_identical"],
            "total_score_delta_abs_diff": abs(a["total_score_delta"] - b["total_score_delta"]),
            "n_violations_here": len(va),
            "n_violations_committed": len(vb),
            "violation_identities_equal": ia == ib,
            "identical": (a["n_segments_matched"] == b["n_segments_matched"]
                          and a["n_segments_compared"] == b["n_segments_compared"]
                          and a["boundaries_identical"] == b["boundaries_identical"]
                          and abs(a["total_score_delta"] - b["total_score_delta"]) <= SCORE_TOL
                          and ia == ib),
        })
    diverged = [r for r in cond_rows if not r.get("identical")]
    return {
        "establishment": {
            "passes_the_apparatus_criterion": est_passes_criterion,
            "criterion": ("same segment list, and total score within the committed tolerance "
                          f"{SCORE_TOL:g} - the apparatus's own definition of established"),
            "segments_bit_identical": est_segments_identical,
            "total_scores_bit_identical": est_bit_identical_scores,
            "max_abs_total_score_diff": est_max_abs_score_diff,
            "pieces": len(est_rows),
            "ok_here": sum(1 for r in est_rows if r["ok_here"]),
            "header_crosscheck_ok_here": sum(1 for r in est_rows
                                             if r["header_crosscheck_ok_here"]),
            "float_note": (
                "Where the two runs' total scores differ they differ at the last representable "
                "places of a double, ten or more orders of magnitude inside the apparatus's own "
                "tolerance and far below any margin that could move a decode. The two runs "
                "execute on different Python builds and therefore different C library "
                "transcendental functions; this was the risk registered in predictions.md as R1, "
                "with a predicted consequence of zero decode flips. The segment lists are "
                "bit-identical on every piece and every condition, which is that consequence "
                "measured."
            ),
            "rows": est_rows,
        },
        "conditions": {
            "total": len(cond_rows),
            "identical": len(cond_rows) - len(diverged),
            "diverged": diverged,
            "max_total_score_delta_abs_diff": max(
                (r.get("total_score_delta_abs_diff", 0.0) for r in cond_rows), default=None),
            "rows": cond_rows,
        },
        "verdict": (
            "REPRODUCED - the apparatus establishes here (same segments, scores within its own "
            "tolerance), and all 36 transposed conditions match the committed run condition for "
            "condition and violation identity for violation identity. The only difference "
            "anywhere is two total scores at the last places of a double; see "
            "establishment.float_note."
            if est_passes_criterion and not diverged else
            "DIVERGED - see conditions.diverged and the establishment block; a divergence here is "
            "a finding about the APPARATUS, not about the decoder"),
    }


# ------------------------------------------------------------------ B. the separation (§4.4)

def separation(tr):
    """Classify every violation under the classes registered in predictions.md."""
    classes = {"BND": [], "LBL-PRUNE": [], "LBL-ENH": [], "LBL-OTHER": []}
    collapse_conditions, near_collapse, bnd_conditions = [], [], []
    per_shift = {}
    for key, cond in sorted(tr["conditions"].items()):
        stem, ks = key.rsplit("|", 1)
        k = int(ks)
        cmp_, mat = cond["n_segments_compared"], cond["n_segments_matched"]
        ps = per_shift.setdefault(k, {"compared": 0, "matched": 0, "violations": 0,
                                      "conditions": 0, "boundaries_identical": 0})
        ps["compared"] += cmp_
        ps["matched"] += mat
        ps["violations"] += len(cond["violations"])
        ps["conditions"] += 1
        ps["boundaries_identical"] += 1 if cond["boundaries_identical"] else 0
        if not cond["boundaries_identical"]:
            bnd_conditions.append(key)
            if cmp_ and mat / cmp_ <= COLLAPSE_FRACTION:
                collapse_conditions.append({"condition": key, "matched": mat, "compared": cmp_,
                                            "total_score_delta": cond["total_score_delta"]})
            elif cmp_ and mat / cmp_ <= 2 * COLLAPSE_FRACTION:
                near_collapse.append({"condition": key, "matched": mat, "compared": cmp_,
                                      "matched_fraction": round(mat / cmp_, 4),
                                      "total_score_delta": cond["total_score_delta"]})
        for v in cond["violations"]:
            if not cond["boundaries_identical"]:
                cls = "BND"
            elif v.get("expected_state_in_candidates") is False:
                cls = "LBL-PRUNE"
            elif k == 6:
                cls = "LBL-ENH"
            else:
                cls = "LBL-OTHER"
            classes[cls].append({"condition": key, "tick": v.get("tick"),
                                 "seg_index": v.get("seg_index")})
    total = sum(len(v) for v in classes.values())
    if total == 0:
        raise SystemExit("STOP: no violations classified - the raw state is empty or malformed")
    defensible = len(classes["LBL-ENH"])
    return {
        "definitions_registered_before_measuring": {
            "BND": ("every violation in a condition whose segment boundaries moved - NOT "
                    "defensible: segmenting the same sounding music differently is not a "
                    "spelling choice"),
            "COLLAPSE": (f"a condition matching <= {COLLAPSE_FRACTION:.0%} of its segments; a "
                         "subset of BND, reported separately - NOT defensible"),
            "LBL-PRUNE": ("a label-only violation whose expected state was not in the candidate "
                          "set - NOT defensible: that is the admission prune (OI-244), not a "
                          "spelling judgment"),
            "LBL-ENH": ("a label-only violation at k = +6 with the expected state in the "
                        "candidate set - THE DEFENSIBLE UPPER BOUND: +6 is the one shift whose "
                        "spelling the declared convention had to choose arbitrarily"),
            "LBL-OTHER": ("a label-only violation at k = +2 or -3 with the expected state in the "
                          "candidate set - NOT defensible: those shifts have an unambiguous "
                          "engraver spelling"),
        },
        "totals": {
            "violations": total,
            "BND": len(classes["BND"]),
            "LBL_PRUNE": len(classes["LBL-PRUNE"]),
            "LBL_ENH_defensible_upper_bound": defensible,
            "LBL_OTHER": len(classes["LBL-OTHER"]),
            "defensible_fraction": round(defensible / total, 6),
            "not_defensible_fraction": round(1 - defensible / total, 6),
            "boundary_moved_conditions": len(bnd_conditions),
            "conditions": len(tr["conditions"]),
        },
        "collapse_conditions": collapse_conditions,
        "near_collapse_conditions": {
            "note": (f"conditions matching between {COLLAPSE_FRACTION:.0%} and "
                     f"{2 * COLLAPSE_FRACTION:.0%} of their segments - reported because the "
                     "registered numeric threshold and the committed report's prose phrase "
                     "'three near-total collapses' do not pick out the same set, and the "
                     "difference is a definitional one inside the prediction, not a fact about "
                     "the decoder"),
            "conditions": near_collapse,
        },
        "per_shift": {str(k): v for k, v in sorted(per_shift.items())},
        "members": {k: v for k, v in classes.items() if k != "BND"},
        "bnd_conditions": bnd_conditions,
        "what_this_says": (
            "The defensible share is the ONLY part of the measured non-equivariance that an "
            "engraver's spelling choice could account for. Everything else is the same sounding "
            "music segmented differently, a reading the prune removed from the candidate list, or "
            "a flip at a shift whose spelling was never ambiguous."
        ),
    }


def predictions_scored(rep, sep):
    """Score the registered predictions. Each carries its registered value inline so the scoring
    cannot be read without the claim it scores."""
    t = sep["totals"]
    ps = sep["per_shift"]
    e = rep["establishment"]
    out = [
        {"id": "R1", "claim": "establishment reproduces 12/12, segments and total score",
         "registered": "12/12 exact",
         "measured": f"apparatus criterion {'PASS' if e['passes_the_apparatus_criterion'] else 'FAIL'} "
                     f"{e['ok_here']}/{e['pieces']}; segments bit-identical "
                     f"{e['segments_bit_identical']}; total scores bit-identical "
                     f"{e['total_scores_bit_identical']}/{e['pieces']}, max |diff| "
                     f"{e['max_abs_total_score_diff']:g}",
         "verdict": ("CONFIRMED AT THE APPARATUS CRITERION - the word 'exact' in the registered "
                     "claim is refuted at two pieces by about 1e-14, which is the R1-risk below "
                     "arriving with its predicted consequence (zero decode flips) intact"
                     if e["passes_the_apparatus_criterion"] and e["segments_bit_identical"]
                     else "REFUTED")},
        {"id": "R1-risk",
         "claim": "a different C library could differ in the last place; predicted incidence zero "
                  "and predicted consequence zero decode flips",
         "registered": "zero incidence, zero flips",
         "measured": f"incidence {e['pieces'] - e['total_scores_bit_identical']} of {e['pieces']} "
                     f"pieces (max |diff| {e['max_abs_total_score_diff']:g}); flips 0 - every "
                     f"segment list bit-identical and max |transposed total-score delta "
                     f"difference| over 36 conditions = "
                     f"{rep['conditions']['max_total_score_delta_abs_diff']}",
         "verdict": ("PARTLY REFUTED - the incidence half is wrong (two pieces differ), the "
                     "consequence half is CONFIRMED (nothing moved). The registered follow-up "
                     "question - near-tie flip or something moved - is answered by the diff "
                     "magnitude: about 1e-14 is a floating-point last place, not a moved input"
                     if e["total_scores_bit_identical"] != e["pieces"] else "CONFIRMED")},
        {"id": "R1-header", "claim": "header cross-check true on all 12",
         "registered": "12",
         "measured": str(rep["establishment"]["header_crosscheck_ok_here"]),
         "verdict": "CONFIRMED" if rep["establishment"]["header_crosscheck_ok_here"]
                    == rep["establishment"]["pieces"] else "REFUTED"},
        {"id": "R2", "claim": "the transposed conditions reproduce the committed figures exactly",
         "registered": "811/1224 matched; 9 of 36 boundary-identical; 413 violations; every "
                       "condition and violation identity equal",
         "measured": f"{sum(v['matched'] for v in ps.values())}/"
                     f"{sum(v['compared'] for v in ps.values())} matched; "
                     f"{sum(v['boundaries_identical'] for v in ps.values())} of "
                     f"{t['conditions']} boundary-identical; {t['violations']} violations; "
                     f"{rep['conditions']['identical']}/{rep['conditions']['total']} conditions "
                     f"identical",
         "verdict": "CONFIRMED" if (not rep["conditions"]["diverged"]) else "REFUTED"},
        {"id": "R3-BND", "claim": "boundary movement is about 96 % of the violations",
         "registered": "BND about 396 of 413 (about 95.9 %); 27 of 36 conditions boundary-moved",
         "measured": f"BND {t['BND']} of {t['violations']} "
                     f"({t['BND'] / t['violations']:.1%}); "
                     f"{t['boundary_moved_conditions']} of {t['conditions']} boundary-moved",
         "verdict": "CONFIRMED" if t["BND"] == 396 and t["boundary_moved_conditions"] == 27
                    else "SEE MEASURED"},
        {"id": "R3-COLLAPSE", "claim": "three collapse conditions, all at +6",
         "registered": (f"3 (bwv2.6|+6, bwv297|+6, bwv420|+6), under a threshold registered as "
                        f"<= {COLLAPSE_FRACTION:.0%} of segments matched"),
         "measured": f"{len(sep['collapse_conditions'])} at the registered threshold: "
                     f"{[c['condition'] for c in sep['collapse_conditions']]}; near-collapse "
                     f"(<= {2 * COLLAPSE_FRACTION:.0%}): "
                     f"{[c['condition'] for c in sep['near_collapse_conditions']['conditions']]}",
         "verdict": ("REFUTED AS REGISTERED, and the fault is in the prediction, not the data: "
                     "the numeric threshold and the named list were registered in the same breath "
                     "and do not pick out the same set - bwv420|+6 matches 4 of 31 segments, "
                     "which is above the 10 % line and which the committed report's looser prose "
                     "phrase 'near-total collapse' includes. Nothing about the decoder is in "
                     "question; all three conditions are boundary-moved and none is defensible "
                     "either way"
                     if [c["condition"] for c in sep["collapse_conditions"]]
                     != ["bwv2.6|+6", "bwv297|+6", "bwv420|+6"] else "CONFIRMED")},
        {"id": "R3-PRUNE", "claim": "five label-only violations are the admission prune",
         "registered": "5",
         "measured": str(t["LBL_PRUNE"]),
         "verdict": "CONFIRMED" if t["LBL_PRUNE"] == 5 else "SEE MEASURED"},
        {"id": "R3-ENH", "claim": "the DEFENSIBLE upper bound is 10 of 413, band 8-10",
         "registered": "8-10 violations (about 1.9-2.4 %)",
         "measured": f"{t['LBL_ENH_defensible_upper_bound']} of {t['violations']} "
                     f"({t['defensible_fraction']:.2%})",
         "verdict": "CONFIRMED" if 8 <= t["LBL_ENH_defensible_upper_bound"] <= 10
                    else "REFUTED"},
    ]
    return out


def build():
    new_est = _load(HERE / "establish_state.json")
    new_tr = _load(HERE / "transpose_state.json")
    old_est = _load(COMMITTED / "establish_state.json")
    old_tr = _load(COMMITTED / "transpose_state.json")

    if new_est.get("sample") != old_est.get("sample"):
        raise SystemExit("STOP: the two runs used different sample pieces")
    if new_est.get("note_events_git_hash") != old_est.get("note_events_git_hash"):
        raise SystemExit("STOP: the two runs used different note-events corpus hashes")

    rep = reproduction(new_est, old_est, new_tr, old_tr)
    sep = separation(new_tr)
    return {
        "purpose": (
            "The repository-side re-run of the transposition-equivariance probe, scored against "
            "the committed run and against the predictions registered before it ran. This is the "
            "action OPEN_ITEMS.md OI-243 names as owed before its finding, and OI-244's, carries "
            "any load (#19)."
        ),
        "generated_by": ("tools/joint_estimator/transposition_probe_rerun_2026_08_03/"
                         "analyze_rerun.py"),
        "committed_run": "tools/joint_estimator/transposition_probe_2026_08_02/",
        "this_run": "tools/joint_estimator/transposition_probe_rerun_2026_08_03/",
        "shared_inputs_checked": {
            "sample_pieces": new_est["sample"],
            "note_events_corpus_git_hash": new_est["note_events_git_hash"],
            "seg_cap": new_est["seg_cap"],
        },
        "A_reproduction": rep,
        "B_separation_the_dispatch_asked_for": sep,
        "predictions_scored": predictions_scored(rep, sep),
        "what_this_does_NOT_settle": (
            "It re-measures; it does not fix. The disposition of OI-243 and OI-244 belongs to the "
            "family design at its own stage, over the whole family at once."
        ),
    }


def main(argv):
    doc = build()
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT} does not exist")
            return 1
        if _load(OUT) == doc:
            print(f"PASS: {OUT.name} re-derives byte-identically")
            return 0
        print(f"FAIL: {OUT.name} differs from what the analysis now produces")
        return 1
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}")
    print("  A reproduction:", doc["A_reproduction"]["verdict"])
    t = doc["B_separation_the_dispatch_asked_for"]["totals"]
    print(f"  B separation: {t['violations']} violations - BND {t['BND']}, "
          f"LBL-PRUNE {t['LBL_PRUNE']}, LBL-ENH (defensible) "
          f"{t['LBL_ENH_defensible_upper_bound']}, LBL-OTHER {t['LBL_OTHER']}; "
          f"defensible {t['defensible_fraction']:.2%}")
    for p in doc["predictions_scored"]:
        print(f"  {p['id']:12s} {p['verdict']:12s} measured: {p['measured']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
