#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_pass2_sample_l4.py — draw the two random row samples for the Layer-4
# (chord) certification audit, PASS 2 (EG-7 / OI-84 / OI-102). Read-only over
# the machine inventory produced by tools/audit/gen_inventory.py (the l4_*.csv
# raw tables); writes only sample manifests (never verdicts — the second reader
# fills those in by hand at the code).
#
# Sibling of tools/audit/gen_pass2_sample.py (the L1/L2 sampler); same shape,
# retargeted at tools/audit/l4/l4_*.csv. Kept as its own file because the L4
# instruction (Task 1) asks for a committed L4 sampler with NEW recorded seeds
# and a >=120 reading sample; the L1/L2 script's constants are frozen provenance
# and must not be edited.
#
# Two samples, two NEW fixed recorded seeds (different from every seed used so
# far — L1/L2 used 20260711 / 424242; the 20260712-20260715 band is reserved by
# the L3/L4-pass1 draws per the pass-2 instruction):
#   (1) READING sample (protocol P5 / instruction Task 1, point 1): >= 120 rows,
#       spread across the FIVE row kinds (function, literal, field, branch,
#       crosslayer) in proportion to their counts, with every deep-audited L4
#       file represented. Judged from scratch, blind to pass 1. seed=SEED_READING.
#   (2) ERROR-RATE sample (protocol P6 / instruction Task 1, point 1): 40 rows,
#       uniform over the deep-inventory domain (the SIX deep row kinds = the five
#       above plus decl; file-classification rows excluded — file_table.csv is a
#       designated-safe read, so the second reader is NOT blind to it and it
#       cannot serve a blind error-rate estimate). seed=SEED_ERROR.
#
# The domain is rebuilt from the RAW inventory files only (l4_*.csv), so running
# this does not read pass 1's dispositions and cannot leak them into the blind
# pass. The pass1_* artifacts under tools/audit/l4/ are NOT read here.
#
# Determinism: every input list is sorted by a stable key before sampling, so
# the draw depends only on the seed and the frozen inventory, not on filesystem
# order. Re-running reproduces byte-identical samples.

import copy
import csv
import json
import os
import sys
import random

HERE = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.join(HERE, "l4")
PARAM_MANIFEST = os.path.join(HERE, "..", "param_manifest.json")

SEED_READING = 20260801      # Task 1 blind independent second reading (NEW)
SEED_ERROR = 20260802        # Task 1 audit-error-rate sample (NEW, different)
READING_TARGET = 120         # base proportional target (coverage top-ups may add a few)
ERROR_N = 40                 # error-rate sample size (per instruction)

# The five row kinds the reading sample is stratified over (Task 1, point 1).
READING_KINDS = ["function", "literal", "field", "branch", "crosslayer"]
# The error-rate sample is uniform over the deep-inventory kinds (adds decl).
ERROR_KINDS = ["function", "literal", "field", "branch", "crosslayer", "decl"]

# Frozen domain sizes (self-check against inventory drift, cf. the L1/L2 sampler).
READING_DOMAIN = 2099        # 136 fn + 1067 lit + 262 field + 612 branch + 22 xlayer
ERROR_DOMAIN = 2121          # + 22 decl

# The 10 deep-audited files (manifest.json deep_audited_file_list) grouped into
# the three pass-1 scopes named by the instruction. Grouping is for coverage +
# reporting only; it does not affect the mechanical draw.
SCOPE = {
    "src/composing/analysis/chord/chordslicedecoder.cpp": "decoder",
    "src/composing/analysis/chord/chordslicedecoder.h": "decoder",
    "src/composing/analysis/decode/chordpathdecoder.h": "decoder",
    "src/composing/analysis/chord/chordanalyzer.cpp": "oracle",
    "src/composing/analysis/chord/chordanalyzer.h": "oracle",
    "src/composing/analysis/chord/analysisutils.h": "oracle",
    "src/composing/analysis/chord/chordsymbolformatter.cpp": "satellites",
    "src/composing/analysis/region/sparsechordrefinement.cpp": "satellites",
    "src/composing/analysis/region/sparsechordrefinement.h": "satellites",
    "src/composing/analysis/types/analysistypes.h": "satellites",
}


def _read_csv(name):
    with open(os.path.join(L4, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _load_manifest_sites():
    """(basename, line) and lowercase names present in param_manifest.json —
    a mechanical hint for the literal ESTABLISHED/UNFIT/DEAD manifest check.
    Reading the manifest is not reading pass-1 verdicts."""
    try:
        d = json.load(open(PARAM_MANIFEST, encoding="utf-8"))
    except Exception:
        return set(), set()
    sites, names = set(), set()
    for p in d.get("parameters", []):
        site = p.get("site", "")
        if ":" in site:
            base, ln = site.rsplit(":", 1)
            sites.add((os.path.basename(base), ln.strip()))
        nm = p.get("name", "")
        if nm:
            names.add(nm.lower())
    return sites, names


def load_rows():
    """Rebuild the deep-inventory domain from the RAW inventory tables."""
    rows = []
    man_sites, man_names = _load_manifest_sites()

    def add(kind, file, line, label, extra=None):
        rid = "{}|{}|{}|{}".format(kind, file, line, len(rows))
        r = {"row_id": rid, "kind": kind, "file": file, "line": str(line),
             "label": label, "scope": SCOPE.get(file, "?")}
        if extra:
            r.update(extra)
        rows.append(r)

    for r in _read_csv("l4_functions.csv"):
        add("function", r["file"], r["start_line"], "{}()".format(r["name"]),
            {"name": r["name"], "end_line": r.get("end_line", "")})

    for r in _read_csv("l4_literals.csv"):
        base = os.path.basename(r["file"])
        ctx = r.get("context", "")
        in_man = ((base, r["line"]) in man_sites
                  or any(n in ctx.lower() for n in man_names))
        add("literal", r["file"], r["line"],
            "{} in {}".format(r["value"], r.get("func", "")),
            {"value": r["value"], "func": r.get("func", ""),
             "context": ctx, "in_param_manifest_hint": "yes" if in_man else "no"})

    for r in _read_csv("l4_fields.csv"):
        add("field", r["file"], r["line"],
            "{}::{}".format(r.get("type_owner", ""), r["name"]),
            {"type_owner": r.get("type_owner", ""),
             "field_type": r.get("field_type", ""),
             "name": r["name"], "context": r.get("context", "")})

    for r in _read_csv("l4_branches.csv"):
        add("branch", r["file"], r["line"],
            "{} in {}".format(r.get("kind", ""), r.get("func", "")),
            {"branch_kind": r.get("kind", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l4_crosslayer.csv"):
        add("crosslayer", r["file"], r["line"],
            "include {} -> {}".format(r.get("include", ""), r.get("target_area", "")),
            {"include": r.get("include", ""), "resolved": r.get("resolved", ""),
             "target_area": r.get("target_area", "")})

    for r in _read_csv("l4_decls.csv"):
        add("decl", r["file"], r["line"], "{}".format(r.get("name", "")),
            {"type_owner": r.get("type_owner", ""), "name": r.get("name", ""),
             "context": r.get("context", "")})

    return rows


def stable_key(r):
    line = r["line"]
    lnum = int(line) if line.isdigit() else -1
    return (r["kind"], r["file"], lnum, r["row_id"])


def largest_remainder(counts, target):
    total = sum(counts.values())
    raw = {k: target * c / total for k, c in counts.items()}
    floor = {k: int(v) for k, v in raw.items()}
    used = sum(floor.values())
    rem = sorted(counts.keys(), key=lambda k: raw[k] - floor[k], reverse=True)
    i = 0
    while used < target:
        floor[rem[i % len(rem)]] += 1
        used += 1
        i += 1
    return floor


def draw_reading(rows):
    pool = [r for r in rows if r["kind"] in READING_KINDS]
    by_kind = {k: sorted([r for r in pool if r["kind"] == k], key=stable_key)
               for k in READING_KINDS}
    counts = {k: len(v) for k, v in by_kind.items()}
    alloc = largest_remainder(counts, READING_TARGET)

    rng = random.Random(SEED_READING)
    selected = {}
    for k in READING_KINDS:
        for r in rng.sample(by_kind[k], alloc[k]):
            selected[r["row_id"]] = r

    covered = {selected[i]["file"] for i in selected}
    need = set(SCOPE.keys())
    topups = []
    for f in sorted(need - covered):
        cand = sorted([r for r in pool if r["file"] == f and r["row_id"] not in selected],
                      key=stable_key)
        if not cand:
            cand = sorted([r for r in rows if r["file"] == f and r["row_id"] not in selected],
                          key=stable_key)
        if cand:
            pick = rng.choice(cand)
            selected[pick["row_id"]] = pick
            topups.append(pick["row_id"])

    ordered = [copy.deepcopy(selected[i]) for i in selected]
    rng.shuffle(ordered)
    for i, r in enumerate(ordered):
        r["process_order"] = i + 1

    meta = {
        "seed": SEED_READING, "target_base": READING_TARGET,
        "kind_counts": counts, "kind_allocation": alloc,
        "coverage_topups": topups, "n_selected": len(ordered),
        "deep_files": sorted(need),
        "files_covered": sorted({r["file"] for r in ordered}),
        "scope_breakdown": {s: sum(1 for r in ordered if r["scope"] == s)
                            for s in sorted({r["scope"] for r in ordered})},
    }
    return ordered, meta


def draw_error(rows):
    pool = sorted([r for r in rows if r["kind"] in ERROR_KINDS], key=stable_key)
    rng = random.Random(SEED_ERROR)
    picks = rng.sample(pool, ERROR_N)
    picks_sorted = [copy.deepcopy(r) for r in sorted(picks, key=stable_key)]
    rng.shuffle(picks_sorted)
    for i, r in enumerate(picks_sorted):
        r["process_order"] = i + 1
    meta = {
        "seed": SEED_ERROR, "n": ERROR_N, "domain_size": len(pool),
        "kind_breakdown": {k: sum(1 for r in picks if r["kind"] == k)
                           for k in sorted({r["kind"] for r in picks})},
        "scope_breakdown": {s: sum(1 for r in picks if r["scope"] == s)
                            for s in sorted({r["scope"] for r in picks})},
    }
    return picks_sorted, meta


def write_sample(basename, rows, meta, verdict_fields):
    cols = (["process_order", "row_id", "kind", "scope", "file", "line", "label",
             "in_param_manifest_hint"] + verdict_fields)
    csv_path = os.path.join(L4, basename + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            row = dict(r)
            for f in verdict_fields:
                row.setdefault(f, "")
            row.setdefault("in_param_manifest_hint", "")
            w.writerow(row)
    json_path = os.path.join(L4, basename + ".json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, indent=1, sort_keys=True)
    return csv_path, json_path


def main():
    rows = load_rows()
    reading_pool = sum(1 for r in rows if r["kind"] in READING_KINDS)
    error_pool = sum(1 for r in rows if r["kind"] in ERROR_KINDS)
    if reading_pool != READING_DOMAIN or error_pool != ERROR_DOMAIN:
        sys.stderr.write(
            "FATAL: reading_pool={} (expect {}), error_pool={} (expect {}). "
            "Inventory drift — do not sample.\n".format(
                reading_pool, READING_DOMAIN, error_pool, ERROR_DOMAIN))
        sys.exit(2)

    reading, r_meta = draw_reading(rows)
    err, e_meta = draw_error(rows)

    write_sample("pass2_blind_reading", reading, r_meta,
                 ["verdict", "assumes", "publishes", "consumers", "edges",
                  "flag", "reason"])
    write_sample("pass2_blind_errorrate", err, e_meta,
                 ["verdict", "assumes", "publishes", "consumers", "edges",
                  "flag", "reason"])

    print("reading sample: {} rows (seed {}), files {}/{}, scopes {}".format(
        r_meta["n_selected"], r_meta["seed"],
        len(r_meta["files_covered"]), len(r_meta["deep_files"]),
        r_meta["scope_breakdown"]))
    print("  kind allocation: {}".format(r_meta["kind_allocation"]))
    print("  coverage top-ups: {}".format(r_meta["coverage_topups"]))
    print("error-rate sample: {} rows (seed {}), kinds {}, scopes {}".format(
        e_meta["n"], e_meta["seed"], e_meta["kind_breakdown"],
        e_meta["scope_breakdown"]))


if __name__ == "__main__":
    main()
