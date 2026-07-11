#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_compare.py — Task 2 of the L1/L2 audit pass 2: diff the blind second
# reading (pass2_blind_sample.csv) against pass 1's dispositions
# (pass1_dispositions.csv) on the SAME rows, matched by (kind, file, line), and
# report the flagged/clean agreement. Writes tools/audit/l1l2/pass2_compare.txt.
#
# The comparison is at the FLAGGED-vs-CLEAN level: my flag != CLEAN vs pass 1's
# verdict being in a concern family (UNFIT / ASSUMPTION / SURVIVES-MIXED /
# RETIRES). A DIFF here is not necessarily a substantive disagreement — most are
# recording-granularity (pass 1 propagates module-level SURVIVES-MIXED to every
# branch; records dormancy in prose, not the row verdict). The report diagnoses
# each DIFF class by hand.

import csv
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")
FLAGGED = {"UNFIT", "ASSUMPTION", "SURVIVES-MIXED", "RETIRES"}


def main():
    blind = list(csv.DictReader(open(os.path.join(L1L2, "pass2_blind_sample.csv"),
                                     newline="", encoding="utf-8")))
    p1 = list(csv.DictReader(open(os.path.join(L1L2, "pass1_dispositions.csv"),
                                  newline="", encoding="utf-8")))
    idx = defaultdict(list)
    for r in p1:
        idx[(r["kind"], r["file"], r["line"])].append((r["verdict_class"], r["verdict"]))

    rows = []
    agree = disagree = nomatch = 0
    for b in sorted(blind, key=lambda x: int(x["process_order"])):
        m = idx.get((b["kind"], b["file"], b["line"]), [])
        if not m:
            nomatch += 1
            rows.append((b["process_order"], b["kind"], os.path.basename(b["file"]),
                         b["line"], b["verdict"], b["flag"], "NO-MATCH", "", "NOMATCH"))
            continue
        p1verds = sorted(set(v for (_, v) in m))
        p1flag = any(v in FLAGGED for v in p1verds)
        mine = b["flag"] != "CLEAN"
        same = (mine == p1flag)
        agree += same
        disagree += (not same)
        rows.append((b["process_order"], b["kind"], os.path.basename(b["file"]),
                     b["line"], b["verdict"], b["flag"], "/".join(p1verds),
                     "P1-FLAG" if p1flag else "P1-CLEAN", "AGREE" if same else "DIFF"))

    with open(os.path.join(L1L2, "pass2_compare.txt"), "w", encoding="utf-8") as fh:
        fh.write("=== ROW-BY-ROW (my verdict/flag vs pass1 verdict) ===\n")
        fh.write("po|kind|file|line|MINE_verdict|MINE_flag|P1_verdict|P1_flagclass|match\n")
        for r in rows:
            fh.write("|".join(str(x) for x in r) + "\n")
        fh.write("\nflagged/clean-level: AGREE=%d DIFF=%d NOMATCH=%d of %d\n"
                 % (agree, disagree, nomatch, len(blind)))
        fh.write("\n=== DIFF rows ===\n")
        for r in rows:
            if r[-1] == "DIFF":
                fh.write("|".join(str(x) for x in r) + "\n")
    print("flagged/clean-level: AGREE=%d DIFF=%d NOMATCH=%d of %d" % (agree, disagree, nomatch, len(blind)))


if __name__ == "__main__":
    main()
