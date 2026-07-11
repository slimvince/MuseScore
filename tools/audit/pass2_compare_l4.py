#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_compare_l4.py — Task-2 (post-unblind) comparison for the L4 audit pass 2.
# Joins the second reader's blind verdicts (pass2_blind_{reading,errorrate}.json)
# against pass 1's three dispositions (pass1_dispositions_{decoder,oracle,
# satellites}.csv) on the SAME inventory rows, classifies each row's agreement,
# and prints the reading + error-rate comparison + the error rate. Read-only.

import csv
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.join(HERE, "l4")


def base(f):
    return f.split("/")[-1]


def load_pass1():
    """One lookup keyed by (basename, line, kind) → dict(verdict, flag, src)."""
    idx = {}
    # decoder: kind,file,line,ident,context,population,verdict,fire_route,in_param_manifest,notes
    for r in csv.DictReader(open(os.path.join(L4, "pass1_dispositions_decoder.csv"), encoding="utf-8")):
        k = (base(r["file"]), r["line"].strip(), r["kind"].strip())
        idx.setdefault(k, []).append(dict(verdict=r["verdict"].strip(),
                                          flag=r.get("notes", ""), src="decoder",
                                          ident=r.get("ident", "")))
    # oracle: file,loc,kind,name,population,verdict_class,verdict,in_param_manifest,flagged,rationale
    # loc may be a RANGE ("268-381") — index by the start line so a start-line
    # sample key joins.
    for r in csv.DictReader(open(os.path.join(L4, "pass1_dispositions_oracle.csv"), encoding="utf-8")):
        loc = r["loc"].strip()
        start = loc.split("-")[0].strip()
        rec = dict(verdict=r["verdict"].strip(), vclass=r.get("verdict_class", ""),
                   flag=r.get("flagged", ""), src="oracle", ident=r.get("name", ""),
                   rationale=r.get("rationale", ""))
        for ln in {loc, start}:
            idx.setdefault((base(r["file"]), ln, r["kind"].strip()), []).append(rec)
    # satellites: file,line,kind,value,func,population,verdict_class,verdict,in_param_manifest,...,finding,note
    for r in csv.DictReader(open(os.path.join(L4, "pass1_dispositions_satellites.csv"), encoding="utf-8")):
        k = (base(r["file"]), r["line"].strip(), r["kind"].strip())
        idx.setdefault(k, []).append(dict(verdict=r["verdict"].strip(),
                                          vclass=r.get("verdict_class", ""),
                                          flag=r.get("finding", ""), src="satellites",
                                          ident=r.get("value", "") or r.get("func", ""),
                                          note=r.get("note", "")))
    return idx


# Normalize a pass-1 or pass-2 verdict string to a coarse family for agreement.
def fam(v):
    v = (v or "").upper()
    if v.startswith("ESTABLISHED"):
        return "ESTABLISHED"
    if v.startswith("UNFIT"):
        return "UNFIT"
    if v.startswith("DEAD"):
        return "DEAD"
    if "PUBLISHED" in v:
        return "PUBLISHED"
    if "SILOED" in v:
        return "SILOED"
    if "TRAPPED" in v:
        return "TRAPPED"
    if "DUPLICAT" in v:
        return "DUPLICATED"
    if v.startswith("SURVIVES") or v.startswith("RETIRES") or v == "SURVIVE":
        return "CODE"
    if v.startswith("FACT") or v.startswith("THEORY") or v.startswith("ASSUMPTION"):
        return "PREMISE"
    if "OUT-OF" in v or "SCOPE" in v:
        return "OUT-OF-SCOPE"
    return v or "?"


# Does my verdict-family agree with any pass-1 disposition family for the row?
# ESTABLISHED/UNFIT/DEAD are all "constant" verdicts; PUBLISHED/SURVIVES/etc for
# code+facts. We treat agreement at the row-issue level: same family OR both
# "no-issue" (ESTABLISHED / CODE-SURVIVES / PUBLISHED all = "clean, tracked").
CLEAN = {"ESTABLISHED", "CODE", "PUBLISHED", "PREMISE"}


def compare(sample_name, pass1):
    rows = json.load(open(os.path.join(L4, sample_name + ".json"), encoding="utf-8"))["rows"]
    results = []
    for r in rows:
        b = base(r["file"])
        line = str(r["line"]).strip()
        kind = r["kind"]
        my = r["verdict"]
        myfam = fam(my)
        cands = pass1.get((b, line, kind), [])
        # disambiguate literals by value when multiple share (file,line,kind)
        if len(cands) > 1 and kind == "literal":
            v = str(r.get("value", ""))
            narrowed = [c for c in cands if c.get("ident", "") == v]
            if narrowed:
                cands = narrowed
        if not cands:
            p1 = None
            p1fam = None
        else:
            p1 = cands[0]
            p1fam = fam(p1["verdict"])
        # classification
        if p1 is None:
            # No pass-1 disposition for this row.
            if myfam == "OUT-OF-SCOPE":
                cls = "CONCORDANT-EXCLUDED"   # both agree it's out of L4 scope
            else:
                cls = "NO-PASS1-ROW"
        elif myfam == p1fam:
            cls = "CONCORDANT"
        elif myfam in CLEAN and p1fam in CLEAN:
            cls = "CONCORDANT-CLEAN"          # both "clean/tracked", different axis label
        else:
            cls = "DISAGREE"
        results.append(dict(row=r, my=my, myfam=myfam,
                            p1=(p1["verdict"] if p1 else ""), p1fam=(p1fam or ""),
                            p1src=(p1["src"] if p1 else ""),
                            p1flag=((p1.get("flag") or "") if p1 else ""), cls=cls))
    return results


def main():
    pass1 = load_pass1()
    for s in ("pass2_blind_reading", "pass2_blind_errorrate"):
        res = compare(s, pass1)
        c = Counter(x["cls"] for x in res)
        print("==== %s : %d rows ====" % (s, len(res)))
        print("   ", dict(c))
        # list the non-concordant rows
        for x in res:
            if x["cls"] in ("DISAGREE", "NO-PASS1-ROW"):
                r = x["row"]
                print("    [%s] %s L%s %s val=%s :: MINE=%s | PASS1=%s (%s)" % (
                    x["cls"], base(r["file"]), r["line"], r["kind"],
                    r.get("value", ""), x["my"], x["p1"], x["p1src"]))
        # write per-row comparison artifact
        cols = ["cls", "file", "line", "kind", "value", "my_verdict", "my_flag",
                "pass1_verdict", "pass1_src", "pass1_flag"]
        with open(os.path.join(L4, s.replace("blind", "compare") + ".csv"), "w",
                  newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            for x in res:
                r = x["row"]
                w.writerow(dict(cls=x["cls"], file=base(r["file"]), line=r["line"],
                                kind=r["kind"], value=r.get("value", ""),
                                my_verdict=x["my"], my_flag=r.get("flag", ""),
                                pass1_verdict=x["p1"], pass1_src=x["p1src"],
                                pass1_flag=x["p1flag"]))
        if s.endswith("errorrate"):
            disagree = sum(1 for x in res if x["cls"] == "DISAGREE")
            print("   >>> ERROR RATE (substantive disagreements / 40) = %d/40 = %.1f%%"
                  % (disagree, 100.0 * disagree / len(res)))


if __name__ == "__main__":
    main()
