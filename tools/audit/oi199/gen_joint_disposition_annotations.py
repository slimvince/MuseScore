#!/usr/bin/env python3
"""OI-199 joint P3/P4 dispatch, Task 3 — annotate the FROZEN pass-1 joint dispositions with the two
evidence columns the certified L4 decoder rows carried and the pass-1 joint rows did not:

  * fire_route         — which Task-1 fire-count characterization exercises the row's mechanism
                         (decode:candidate-admission / decode:DP / decode:content-posterior /
                          fact-adapter / record-assembly / route-A:tests / n/a:structural).
  * in_param_manifest  — whether the row's symbol is registered in tools/param_manifest.json
                         (the fit-surface inventory). Parallels the L4 decoder's OI-103 gap.

READ-ONLY over the frozen CSV: this writes a SEPARATE artifact (…_annotations.csv), it NEVER rewrites
pass1_dispositions_joint.csv (#10/#12 — the frozen rows are the record of what pass 1 verdicted). The
mapping is by (file, kind, name); the decoder-function names are mapped specifically, everything else by
file. The measured per-route fire RATES live in the report + joint_firecount_{fit,large}.json — this
column records the ROUTE (which measurement), not the rate, one link per row.
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
FROZEN = os.path.join(HERE, "pass1_dispositions_joint.csv")
OUT = os.path.join(HERE, "pass1_dispositions_joint_annotations.csv")
MANIFEST = os.path.join(REPO, "tools", "param_manifest.json")

# decoder function names -> specific fire route (jointdecoder.cpp).
ADMISSION_FNS = {"candidateStates", "candidateKeys", "chromaticRootPc"}
DP_FNS = {"decodePiece", "sigLess", "prefixSig", "fullSig", "better", "betterPrefix", "summarize",
          "loadPiecesFromNoteEvents"}
CONTENT_FNS = {"segmentContentScore", "segmentFeatures", "weightedContent", "computePosteriorSlice",
               "cadenceFired", "eventBassPc", "popcount", "stateEnc", "keyEnc", "keyString"}


def manifest_symbols(path):
    """Collect every parameter symbol name registered in param_manifest.json."""
    syms = set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return syms

    def walk(o):
        if isinstance(o, dict):
            for k in ("name", "symbol", "cpp_symbol", "param", "identifier"):
                if k in o and isinstance(o[k], str):
                    syms.add(o[k])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(data)
    return syms


def fire_route(kind, file, name):
    base = os.path.basename(file)
    if base == "jointdecoder.cpp":
        if name in ADMISSION_FNS:
            return "decode:candidate-admission"
        if name in DP_FNS:
            return "decode:DP"
        if name in CONTENT_FNS:
            return "decode:content-posterior"
        # branch / literal / field rows in the decoder TU: the decode fire counters cover them
        if kind in ("branch",):
            return "decode:DP"
        if kind in ("function",):
            return "decode:DP"
        return "route-A:tests"
    if base == "jointfactadapter.cpp":
        return "fact-adapter (buildAdapterFacts; not a decode branch)"
    if base in ("jointnotationrecord.cpp", "jointnotationproducer.cpp", "jointrender.cpp"):
        return "record-assembly"
    if kind in ("literal", "decl", "field", "crosslayer"):
        return "n/a:structural (route-A:tests exercises the reader)"
    return "route-A:tests"


def main():
    syms = manifest_symbols(MANIFEST)
    n_in_manifest = 0
    rows_out = []
    with open(FROZEN, "r", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        fieldnames = list(rd.fieldnames) + ["fire_route", "in_param_manifest"]
        for r in rd:
            name = (r.get("name") or "").strip()
            kind = (r.get("kind") or "").strip()
            file = (r.get("file") or "").strip()
            in_m = "yes" if name and name in syms else "no"
            if in_m == "yes":
                n_in_manifest += 1
            r["fire_route"] = fire_route(kind, file, name)
            r["in_param_manifest"] = in_m
            rows_out.append(r)

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=fieldnames)
        wr.writeheader()
        wr.writerows(rows_out)

    # route tally for the report
    tally = {}
    for r in rows_out:
        tally[r["fire_route"]] = tally.get(r["fire_route"], 0) + 1
    print("rows annotated:", len(rows_out))
    print("in_param_manifest yes:", n_in_manifest, "/", len(rows_out))
    print("fire_route tally:")
    for k in sorted(tally):
        print(f"  {tally[k]:5d}  {k}")
    print("wrote", OUT)


if __name__ == "__main__":
    sys.exit(main())
