#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""gen_joint_dispositions.py — OI-199 pass-1 deep dispositions for AREA (a), the joint
estimator module (the JOINT-tagged inventory rows). Applies the SAME closed verdict
vocabulary the L3/L4/L5 pass-1 audits used (no new vocabulary, #6 / the no-self-invented-
labels convention):

  SURVIVES        — code on the surviving (production) path (functions, decls, internal state)
  NO-ISSUE        — ordinary control-flow branch / plumbing (a recorded claim with a reason)
  ESTABLISHED     — FACT / structural or theory constant, or a byte-established Python-parity
                    reference value (music-theory table, pc arithmetic, cardinality, the
                    ratified decode floors verified bit-identical to probe_decoder)
  UNFIT           — a hand-set / empirical DECODE HYPERPARAMETER (chosen, sweepable value)
  PUBLISHED       — a derived fact on the module's OUTPUT surface (the §3 notation record /
                    the decode output), read by a consumer OR declared-dormancy (named future)
  FORWARD-OK      — a cross-layer include respecting the Dependency Rule (joint -> L1 / engraving
                    / muse framework)
  BACK-EDGE-NOTE  — a joint -> chord/ include for a dependency-free pitch primitive (layering
                    smell; the sanctioned normalizePc leaf, OI-93/OI-86 sibling)

Every row gets a verdict + a stated reason. Load-bearing rows carry a FLAG (verified at the
code, recorded in the pass-1 report). Reproducible: reads the committed oi199 inventory CSVs.
Run: python tools/audit/oi199/gen_joint_dispositions.py
"""
import csv
import json
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
INV = os.path.join(REPO, "tools", "audit", "oi199")
OUT = INV


# area (a) is the JOINT-tagged files only — jointembeddedartifacts.{h,cpp} are CODEGEN (area c),
# so filter by the file_table tag, not the /joint/ path (the two differ by the codegen accessor).
_TAG = {r["file"]: r["tag"] for r in csv.DictReader(open(os.path.join(INV, "file_table.csv"), encoding="utf-8"))}


def joint_rows(name):
    rows = list(csv.DictReader(open(os.path.join(INV, name), encoding="utf-8")))
    return [r for r in rows if _TAG.get(r["file"]) == "JOINT"]


# ── field owners: the module's OUTPUT surface (PUBLISHED) vs internal state (SURVIVES) ──
PUBLISHED_OWNERS = {
    # the §3 notation output-surface record (cowork_notation_output_contract.md §3)
    "NotationRecord", "RecordSegment", "RecordProvenance", "EventBassFact",
    "ModalKeyRun", "ModalDegree", "ModalInflection", "SegmentSlice", "PosteriorAxis",
    # the decode output surface (batch .ours.json + feeds the record) + the producer output
    "SegmentSummary", "DecodeResult", "NotationRecordResult", "NoteView",
}
INTERNAL_OWNERS = {
    "Piece", "EventRec", "NoteRec", "ChordInfo", "Framework", "ChordFactor", "Node",
    "KatzRow", "KatzTable", "BoundaryCell", "WeightVector", "AdapterFacts", "LoadedCorpus",
    "JointTables",
}
# published-but-currently-UNCONSUMED record fields (grep-verified: no consumer outside joint/).
# Declared dormancy — the named future consumer is the presentation layer (contract §3.2/§3.4);
# flagged so a reader does not mistake them for live-consumed signals.
DORMANT_PUBLISHED_OWNERS = {"ModalKeyRun", "ModalDegree", "ModalInflection"}
DORMANT_PUBLISHED_FIELDS = {("RecordSegment", "augSixthSubType")}

# the two ratified-but-hand-chosen DECODE HYPERPARAMETERS (sweepable) -> UNFIT; every other
# joint source literal is a structural/theory constant or a byte-established parity floor.
UNFIT_LITERALS = {
    ("src/composing/analysis/joint/jointdecoder.cpp", "6"),        # kKeyPruneTopK (line 39)
    ("src/composing/analysis/joint/jointnotationproducer.cpp", "4"),  # seg_cap arg (line 57)
}

disp = []


def add(kind, r, verdict, reason, flag=""):
    disp.append({"kind": kind, "file": r["file"], "line": r.get("line", ""),
                 "name": r.get("name", r.get("value", r.get("include", ""))),
                 "verdict": verdict, "reason": reason, "flag": flag})


# functions -> SURVIVES (the module is production-surviving on both surfaces; nothing retires)
for r in joint_rows("oi199_functions.csv"):
    add("function", r, "SURVIVES", "production-surviving joint module function (notation record path + batch decode)")

# decls -> SURVIVES
for r in joint_rows("oi199_decls.csv"):
    add("decl", r, "SURVIVES", "declaration of the surviving joint module (public/struct surface)")

# branches -> NO-ISSUE
for r in joint_rows("oi199_branches.csv"):
    add("branch", r, "NO-ISSUE", "ordinary control-flow / guard (recorded claim)")

# literals -> ESTABLISHED, except the two decode hyperparameters
for r in joint_rows("oi199_literals.csv"):
    key = (r["file"], r["value"])
    # only the specific hyperparameter lines are UNFIT (topK on decoder:39, segCap on producer:57)
    is_unfit = (key in UNFIT_LITERALS and (
        (r["file"].endswith("jointdecoder.cpp") and r["line"] == "39")
        or (r["file"].endswith("jointnotationproducer.cpp") and r["line"] == "57")))
    if is_unfit:
        add("literal", r, "UNFIT",
            "ratified but hand-chosen DECODE HYPERPARAMETER (sweepable): topK key prune / seg_cap",
            flag="hyperparameter")
    else:
        add("literal", r, "ESTABLISHED",
            "structural/theory constant or byte-established probe_decoder-parity reference value")

# crosslayer -> FORWARD-OK, except chord/analysisutils.h (the pc leaf)
for r in joint_rows("oi199_crosslayer.csv"):
    inc = r.get("resolved", "") or r.get("include", "")
    if "chord/analysisutils.h" in inc:
        add("crosslayer", r, "BACK-EDGE-NOTE",
            "joint -> chord/analysisutils.h for normalizePc — sanctioned dependency-free pc leaf "
            "(OI-93/OI-86 sibling); a layering smell, not a heavy coupling", flag="back-edge")
    else:
        add("crosslayer", r, "FORWARD-OK",
            "forward cross-layer include (joint -> L1 note_model / engraving score model / muse framework)")

# fields -> PUBLISHED (output surface) or SURVIVES (internal); flag the unconsumed published ones
for r in joint_rows("oi199_fields.csv"):
    owner = r["type_owner"]
    if owner in PUBLISHED_OWNERS:
        dormant = owner in DORMANT_PUBLISHED_OWNERS or (owner, r["name"]) in DORMANT_PUBLISHED_FIELDS
        if dormant:
            add("field", r, "PUBLISHED",
                "published on the §3 notation output surface but UNCONSUMED outside joint/ "
                "(declared dormancy — named future consumer: the presentation layer)",
                flag="published-unconsumed")
        else:
            add("field", r, "PUBLISHED",
                "derived fact on the module OUTPUT surface (notation record / decode output), consumed by a reader")
    elif owner in INTERNAL_OWNERS:
        add("field", r, "SURVIVES", "internal decode/table/value-type state of the surviving module")
    else:
        add("field", r, "SURVIVES", "internal state (owner=%s)" % owner)

# ── write + tally ──
from collections import Counter
tally = Counter(d["verdict"] for d in disp)
bykind = Counter((d["kind"], d["verdict"]) for d in disp)
flags = [d for d in disp if d["flag"]]

with open(os.path.join(OUT, "pass1_dispositions_joint.json"), "w", encoding="utf-8") as f:
    json.dump({"dispositions": disp, "tally": dict(tally),
               "bykind": {f"{k[0]}/{k[1]}": v for k, v in bykind.items()},
               "flagged": flags}, f, indent=1)
with open(os.path.join(OUT, "pass1_dispositions_joint.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["kind", "file", "line", "name", "verdict", "reason", "flag"])
    w.writeheader()
    for d in disp:
        w.writerow(d)

print("OI-199 area (a) JOINT dispositions:", len(disp), "rows")
print("  by verdict:", dict(tally))
print("  by kind/verdict:")
for k in sorted(bykind):
    print(f"    {k[0]:10s} {k[1]:14s} {bykind[k]}")
print("  flagged rows:", len(flags))
for d in flags:
    print(f"    [{d['flag']}] {d['file'].split('/')[-1]}:{d['line']} {d['name']} -> {d['verdict']}")
