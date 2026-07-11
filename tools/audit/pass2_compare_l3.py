#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_compare_l3.py — join the PASS-2 blind verdicts (this second reader) to
# the PASS-1 dispositions on the SAME rows, and classify every disagreement.
# Read-only; writes only comparison artifacts under tools/audit/l3/.
#
# The two passes use different verdict VOCABULARIES on purpose (pass 1 has the
# full protocol-P2 rubric — ESTABLISHED/UNFIT/DEAD, NO-ISSUE/SURVIVES/RETIRES,
# FORWARD-OK/MIXED-DEFERRED/BACK-EDGE(-NOTE), PUBLISHED, DEFERRED; this reader
# used a coarser 4-label set ESTABLISHED/SURVIVES/PUBLISHED/DEAD). A raw
# label-mismatch is therefore common and mostly a vocabulary-axis difference.
# What matters for certification is the SUBSTANTIVE axis: did either pass flag a
# correctness / dead / siloed issue the other missed? That is the "concordance"
# column below.

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
L3 = os.path.join(HERE, "l3")

# For each of MY verdicts, the set of PASS-1 verdicts that are SUBSTANTIVELY
# concordant (same conclusion; label differs only on the vocabulary axis).
# Anything outside these sets is a SUBSTANTIVE disagreement to inspect by hand.
CONCORDANT = {
    # my ESTABLISHED (a constant, or a numeric field default I read as a
    # constant): pass 1 ESTABLISHED (structural) / UNFIT (empirical tunable) —
    # both "a constant, in-bounds, no defect", the ESTABLISHED-vs-UNFIT split
    # being the structural/empirical sub-axis I collapsed — or NO-ISSUE (pass 1
    # read the same numeric FIELD default as a plumbing struct member, not a
    # constant row) or DEFERRED (an L4/L5 constant on the mixed leaf). DEAD would
    # be substantive (pass 1 found the constant dead).
    "ESTABLISHED": {"ESTABLISHED", "UNFIT", "NO-ISSUE", "DEFERRED"},
    # my SURVIVES (code / branch / include): pass 1 NO-ISSUE (control flow),
    # SURVIVES (survivor code), RETIRES (scheduled but live), or any cross
    # verdict (forward or a tracked layering note — none a correctness defect),
    # or DEFERRED (the L4/L5 part of a mixed file).
    "SURVIVES": {"NO-ISSUE", "SURVIVES", "RETIRES",
                 "FORWARD-OK", "MIXED-DEFERRED", "BACK-EDGE", "BACK-EDGE-NOTE",
                 "DEFERRED"},
    # my PUBLISHED (an output/plumbing field): pass 1 PUBLISHED, NO-ISSUE
    # (plumbing member), or DEFERRED (an L4/L5 field on the mixed DTO).
    "PUBLISHED": {"PUBLISHED", "NO-ISSUE", "DEFERRED"},
    # my DEAD is concordant ONLY with a pass-1 DEAD; against anything else it is
    # a substantive disagreement (I flagged a dead field pass 1 did not).
    "DEAD": {"DEAD"},
}


def load_pass1():
    idx = {}
    with open(os.path.join(L3, "pass1_dispositions.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            key = (r["file"], r["kind"], r["line"], r["ident"])
            idx[key] = r
    return idx


def my_ident(row):
    k = row["kind"]
    if k == "literal":
        return row.get("value", "")
    if k in ("field", "function", "decl"):
        return row.get("name", "")
    if k == "branch":
        return row.get("branch_kind", "")
    if k == "crosslayer":
        return row.get("include", "")
    return ""


def compare(sample_name, p1):
    with open(os.path.join(L3, sample_name), encoding="utf-8") as fh:
        rows = json.load(fh)["rows"]
    out = []
    for r in rows:
        key = (r["file"], r["kind"], r["line"], my_ident(r))
        p = p1.get(key)
        p1v = p["verdict"] if p else "<NOT-FOUND>"
        p1c = p["verdict_class"] if p else ""
        mine = r["verdict"]
        concordant = (p is not None) and (p1v in CONCORDANT.get(mine, set()))
        raw_agree = (mine == p1v)
        out.append({
            "process_order": r["process_order"],
            "file": r["file"], "line": r["line"], "kind": r["kind"],
            "ident": my_ident(r),
            "my_verdict": mine, "pass1_verdict": p1v, "pass1_class": p1c,
            "raw_agree": raw_agree,
            "concordance": "CONCORDANT" if concordant else "SUBSTANTIVE",
        })
    return out


def write_csv(name, rows):
    cols = ["process_order", "file", "line", "kind", "ident",
            "my_verdict", "pass1_verdict", "pass1_class", "raw_agree", "concordance"]
    with open(os.path.join(L3, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            w.writerow(r)


def summarize(label, rows):
    n = len(rows)
    raw_agree = sum(1 for r in rows if r["raw_agree"])
    concordant = sum(1 for r in rows if r["concordance"] == "CONCORDANT")
    substantive = [r for r in rows if r["concordance"] == "SUBSTANTIVE"]
    print("{}: {} rows | raw-label agree {}/{} ({:.1f}%) | substantively concordant {}/{} ({:.1f}%)".format(
        label, n, raw_agree, n, 100.0 * raw_agree / n,
        concordant, n, 100.0 * concordant / n))
    print("  raw-label DISAGREEMENTS: {}/{} ({:.1f}%)".format(
        n - raw_agree, n, 100.0 * (n - raw_agree) / n))
    print("  SUBSTANTIVE disagreements: {}".format(len(substantive)))
    for r in substantive:
        print("    - #{} {}:{} [{}] mine={} pass1={}".format(
            r["process_order"], r["file"], r["line"], r["kind"],
            r["my_verdict"], r["pass1_verdict"]))
    return {"n": n, "raw_agree": raw_agree, "concordant": concordant,
            "substantive": len(substantive)}


def crosstab(label, rows):
    from collections import Counter
    c = Counter((r["my_verdict"], r["pass1_verdict"]) for r in rows)
    print("  {} (my_verdict -> pass1_verdict : count):".format(label))
    for (mv, pv), n in sorted(c.items()):
        print("    {:12s} -> {:14s} : {}".format(mv, pv, n))


def main():
    p1 = load_pass1()
    reading = compare("pass2_blind_reading.json", p1)
    err = compare("pass2_blind_errorrate.json", p1)
    write_csv("pass2_compare_reading.csv", reading)
    write_csv("pass2_compare_errorrate.csv", err)
    rs = summarize("READING (116)", reading)
    crosstab("READING crosstab", reading)
    es = summarize("ERROR-RATE (40)", err)
    crosstab("ERROR-RATE crosstab", err)
    with open(os.path.join(L3, "pass2_compare_summary.json"), "w", encoding="utf-8") as fh:
        json.dump({"reading": rs, "errorrate": es}, fh, indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
