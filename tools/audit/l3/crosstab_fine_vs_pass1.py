#!/usr/bin/env python3
"""Crosstab the FROZEN pass-2 fine re-derivation against pass-1's dispositions
(EG-7 / OI-84 / OI-100, Task 3 — run AFTER the Task-2 freeze / unblind).

Joins my frozen fine labels (pass2_fine_relabel_*.json) to pass-1's per-row
verdict via the authoritative seed-fixed process_order join carried in
pass2_compare_*.csv (produced by the pass-2 report's pass2_compare_l3.py). Every
row lands in exactly one bucket:
  CONCORDANT           - my fine label matches pass-1 on the row's P2 axis
  GENUINE-DISAGREEMENT - my decided fine label contradicts pass-1
  UNRESOLVABLE         - my label is UNRESOLVABLE-FROM-PROSE (prose did not reach the axis)

Concordance map (JUDGMENT, documented; the counting is mechanical): pass-1 used a
SUPERSET vocabulary (NO-ISSUE / FORWARD-OK / MIXED-DEFERRED / BACK-EDGE(-NOTE) /
DEFERRED beyond the P2 set). On each P2 axis those map to a single P2 verdict:
  code axis      : my SURVIVES matches pass-1 in {SURVIVES,NO-ISSUE,FORWARD-OK,
                   MIXED-DEFERRED,BACK-EDGE,BACK-EDGE-NOTE} (all = live code, no RETIRES)
  derived axis   : my PUBLISHED matches pass-1 in {PUBLISHED,NO-ISSUE} (fact fine/consumed)
  constants axis : my ESTABLISHED<->ESTABLISHED, UNFIT<->UNFIT, DEAD<->DEAD exactly
No source read, no re-measure; pass-1 verdicts are read from the committed compare CSV.
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

CODE_LIVE_P1 = {"SURVIVES", "NO-ISSUE", "FORWARD-OK", "MIXED-DEFERRED", "BACK-EDGE", "BACK-EDGE-NOTE"}
DERIVED_OK_P1 = {"PUBLISHED", "NO-ISSUE"}


def bucket(my_fine, axis, p1):
    if my_fine == "UNRESOLVABLE-FROM-PROSE":
        return "UNRESOLVABLE"
    if axis == "code":
        return "CONCORDANT" if p1 in CODE_LIVE_P1 else "GENUINE-DISAGREEMENT"
    if axis == "derived":
        return "CONCORDANT" if p1 in DERIVED_OK_P1 else "GENUINE-DISAGREEMENT"
    if axis == "constants":
        return "CONCORDANT" if my_fine == p1 else "GENUINE-DISAGREEMENT"
    raise ValueError(axis)


# DT-2 mechanical manifest-sweep coverage: config-struct members
# (*Preferences/*Preset/*Weights) + named k* consts are all flagged not-in-manifest.
DT2_STRUCT = re.compile(r"::(?:.*)$")


def manifest_covered(label, p1):
    """Is an UNRESOLVABLE constant row independently covered by the DT-2 manifest sweep / L4 deferral?"""
    if p1 == "UNFIT":
        return "yes", "pass-1 UNFIT (not-in-manifest; DT-2/OI-91)"
    if p1 == "DEFERRED":
        return "yes", "L4-scope param, deferred to the L4 audit (DT-2 flags *Preferences too)"
    # pass-1 NO-ISSUE (filed as a plumbing struct member): DT-2 still flags *Preferences/*Preset/*Weights
    if re.search(r"(Preferences|Preset|Weights)::", label):
        return "yes", "DT-2 flags the *Preferences/*Preset/*Weights member (OI-91), though pass-1 filed the row NO-ISSUE"
    return "no", "NOT matched by the DT-2 struct-name patterns (dormant/default-OFF config bound); inert on production"


def process(sample):
    fine = json.load(open(os.path.join(HERE, f"pass2_fine_relabel_{sample}.json"), encoding="utf-8"))["rows"]
    finem = {r["process_order"]: r for r in fine}
    with open(os.path.join(HERE, f"pass2_compare_{sample}.csv"), encoding="utf-8") as fh:
        cmp = {int(r["process_order"]): r for r in csv.DictReader(fh)}
    assert set(finem) == set(cmp), f"{sample}: process_order mismatch"

    out = []
    for po in sorted(finem):
        f = finem[po]
        c = cmp[po]
        b = bucket(f["fine_verdict"], f["axis"], c["pass1_verdict"])
        cov = ("", "")
        if b == "UNRESOLVABLE" and f["axis"] == "constants":
            cov = manifest_covered(f["label"], c["pass1_verdict"])
        out.append({
            "process_order": po,
            "row_id": f["row_id"],
            "kind": f["kind"],
            "label": f["label"],
            "axis": f["axis"],
            "my_fine": f["fine_verdict"],
            "pass1_verdict": c["pass1_verdict"],
            "bucket": b,
            "manifest_covered": cov[0],
            "coverage_note": cov[1],
            "reason_code": f["reason_code"],
        })

    def tally(rows, key):
        d = {}
        for r in rows:
            d[r[key]] = d.get(r[key], 0) + 1
        return dict(sorted(d.items()))

    buckets = tally(out, "bucket")
    # per axis
    per_axis = {}
    for ax in ("code", "constants", "derived"):
        rs = [r for r in out if r["axis"] == ax]
        per_axis[ax] = {"n": len(rs), "buckets": tally(rs, "bucket")}
    # constants ESTABLISHED-vs-UNFIT breakdown (my fine x pass1)
    const_rows = [r for r in out if r["axis"] == "constants"]
    const_cross = {}
    for r in const_rows:
        k = f'{r["my_fine"]} x pass1_{r["pass1_verdict"]}'
        const_cross[k] = const_cross.get(k, 0) + 1
    # manifest coverage of unresolvable constants
    unres_const = [r for r in out if r["bucket"] == "UNRESOLVABLE" and r["axis"] == "constants"]
    covered = sum(1 for r in unres_const if r["manifest_covered"] == "yes")
    uncovered = [r["label"] for r in unres_const if r["manifest_covered"] == "no"]

    summary = {
        "sample": sample,
        "n": len(out),
        "buckets": buckets,
        "per_axis": per_axis,
        "constants_crosstab": dict(sorted(const_cross.items())),
        "unresolvable_constants": {
            "n": len(unres_const),
            "manifest_covered": covered,
            "uncovered_labels": uncovered,
        },
    }

    base = os.path.join(HERE, f"pass2_fine_relabel_crosstab_{sample}")
    cols = ["process_order", "row_id", "kind", "label", "axis", "my_fine",
            "pass1_verdict", "bucket", "manifest_covered", "coverage_note", "reason_code"]
    with open(base + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow(r)
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "rows": out}, f, indent=1)
    return summary


def main():
    s = {"reading": process("reading"), "errorrate": process("errorrate")}
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    sys.exit(main())
