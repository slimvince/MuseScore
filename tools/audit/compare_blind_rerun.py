#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# compare_blind_rerun.py — Task 2 comparison: diff the fully-blind re-run's
# from-scratch verdicts (blind_rerun_reading.json / blind_rerun_errorrate.json)
# against pass 1's recorded dispositions (pass1_dispositions.csv) on the SAME rows.
# Read-only; writes a comparison report to stdout.
#
# "issue-ness" normalisation so the two vocabularies compare:
#   pass 1 (verdict_class -> verdict):
#     CONST   : ESTABLISHED = clean ; UNFIT / DEAD = issue (manifest-gap / unfit)
#     CODE    : SURVIVES = clean ; RETIRES = issue
#     DERIVED : PUBLISHED = clean ; SILOED / TRAPPED / DUPLICATED = issue
#     PREMISE : FACT / THEORY = clean ; ASSUMPTION = issue (upward-dep #7 finding)
#     SCOPE   : the file tag (L1/L2/L3+) = clean classification ; RETIRES = flagged
#   this re-run: the explicit `flag` column ("issue" / "clean").
# Agreement is measured on issue-ness (did both treat the row as a finding or not).

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")


def load_pass1():
    idx = {}
    with open(os.path.join(L1L2, "pass1_dispositions.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            key = (r["kind"], r["file"], r["line"])
            idx.setdefault(key, []).append(r)
    return idx


def pass1_issue(r):
    vc, v = r["verdict_class"], r["verdict"]
    if vc == "CONST":
        return v in ("UNFIT", "DEAD")
    if vc == "CODE":
        return v == "RETIRES"
    if vc == "DERIVED":
        return v in ("SILOED", "TRAPPED", "DUPLICATED")
    if vc == "PREMISE":
        return v == "ASSUMPTION"
    if vc == "SCOPE":
        return v == "RETIRES"
    return False


def disambiguate(mine, cands):
    """Pick the pass-1 candidate row matching my row when several share (kind,file,line)."""
    if len(cands) == 1:
        return cands[0]
    kind = mine["kind"]
    if kind == "literal":
        val = str(mine.get("value", "")).strip()
        for c in cands:
            if c["ident"].strip() == val:
                return c
    if kind == "crosslayer":
        inc = mine.get("include", "")
        for c in cands:
            if c["ident"] == inc or c["ident"].endswith(os.path.basename(inc)):
                return c
    if kind == "function":
        nm = mine.get("name", "")
        for c in cands:
            if c["ident"] == nm or c["ident"].endswith(nm):
                return c
    if kind in ("field", "decl"):
        nm = mine.get("name", "")
        for c in cands:
            if c["ident"].endswith("." + nm) or c["ident"].endswith("::" + nm) or c["ident"] == nm:
                return c
    if kind == "branch":
        fn = mine.get("func", "")
        for c in cands:
            if fn and fn in c["ident"]:
                return c
    return cands[0]  # fall back to the first (same line, best effort)


def compare(sample_basename, pass1):
    with open(os.path.join(L1L2, sample_basename + ".json"), encoding="utf-8") as fh:
        data = json.load(fh)
    rows = sorted(data["rows"], key=lambda r: r["process_order"])
    agree = 0
    disagree = []
    unmatched = []
    for r in rows:
        key = (r["kind"], r["file"], r["line"])
        cands = pass1.get(key)
        if not cands:
            unmatched.append(r)
            continue
        p1 = disambiguate(r, cands)
        mine_issue = (r.get("flag") == "issue")
        p1_issue = pass1_issue(p1)
        if mine_issue == p1_issue:
            agree += 1
        else:
            disagree.append((r, p1, mine_issue, p1_issue))
    return rows, agree, disagree, unmatched


def main():
    pass1 = load_pass1()
    out = []
    for base, label in [("blind_rerun_reading", "READING (111)"),
                        ("blind_rerun_errorrate", "ERROR-RATE (40)")]:
        rows, agree, disagree, unmatched = compare(base, pass1)
        n = len(rows)
        out.append("=" * 78)
        out.append("{}  —  {} rows".format(label, n))
        out.append("  issue-ness AGREE : {}/{}  ({:.1f}%)".format(agree, n, 100.0 * agree / n))
        out.append("  issue-ness DISAGREE : {}".format(len(disagree)))
        out.append("  unmatched : {}".format(len(unmatched)))
        for r, p1, mi, pi in disagree:
            out.append("  ---- DISAGREE  #{} [{}] {} : {}".format(
                r["process_order"], r["kind"], r["file"].split("/")[-1], r.get("label", "")))
            out.append("       mine   : flag={} verdict={}  | {}".format(
                r.get("flag"), r.get("verdict"), r.get("reason", "")[:140]))
            out.append("       pass1  : {}/{} (issue={}) | {}".format(
                p1["verdict_class"], p1["verdict"], pi, p1["reason"][:140]))
        for r in unmatched:
            out.append("  ---- UNMATCHED #{} [{}] {}:{}".format(
                r["process_order"], r["kind"], r["file"], r["line"]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
