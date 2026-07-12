#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# apply_l5_pass2_verdicts.py — fill the Layer-5 pass-2 blind samples with the
# second-reader verdicts. Read-only over the frozen samples produced by
# tools/audit/gen_pass2_sample_l5.py; it writes the verdict columns of
# tools/audit/l5/pass2_blind_reading.{csv,json} and pass2_blind_errorrate.{csv,json}
# from the committed verdict source tools/audit/l5/pass2_blind_verdicts.json.
#
# Pipeline: gen_pass2_sample_l5.py -> (empty samples) -> apply this -> (filled).
# The verdict SOURCE file records who judged each row: the reading sample by six
# independent BLIND source-only readers (one per file-group, no access to pass 1);
# the error-rate sample judged blind FIRST by the second reader personally at the
# code. This script only transcribes those verdicts into the sample artifacts.
#
# Determinism: no sampling here; the verdict source is a committed dict keyed by
# row_id, so re-running reproduces byte-identical filled samples.

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.join(HERE, "l5")
VERDICT_FIELDS = ["verdict", "assumes", "publishes", "consumers", "edges",
                  "flag", "reason", "source"]


def fill(basename, verdicts):
    jp = os.path.join(L5, basename + ".json")
    doc = json.load(open(jp, encoding="utf-8"))
    missing = []
    for r in doc["rows"]:
        v = verdicts.get(r["row_id"])
        if v is None:
            missing.append(r["row_id"])
            continue
        for f in VERDICT_FIELDS:
            r[f] = v.get(f, "")
    if missing:
        sys.stderr.write("FATAL: {} rows in {} have no verdict: {}\n".format(
            len(missing), basename, missing[:5]))
        sys.exit(2)
    json.dump(doc, open(jp, "w", encoding="utf-8"), indent=1, sort_keys=True)

    cp = os.path.join(L5, basename + ".csv")
    rows = sorted(doc["rows"], key=lambda x: x["process_order"])
    base_cols = ["process_order", "row_id", "population", "kind", "file", "line",
                 "label", "in_param_manifest_hint"]
    cols = base_cols + VERDICT_FIELDS
    with open(cp, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            row = {c: r.get(c, "") for c in cols}
            w.writerow(row)
    return len(rows)


def main():
    src = json.load(open(os.path.join(L5, "pass2_blind_verdicts.json"), encoding="utf-8"))
    nr = fill("pass2_blind_reading", src["reading"])
    ne = fill("pass2_blind_errorrate", src["errorrate"])
    print("filled reading sample: {} rows".format(nr))
    print("filled error-rate sample: {} rows".format(ne))


if __name__ == "__main__":
    main()
