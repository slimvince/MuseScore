#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_pass2_sample_l5.py — draw the two random row samples for the Layer-5
# (function) + instruments certification audit, PASS 2 (EG-7 / OI-84 / OI-116).
# Read-only over the machine inventory produced by tools/audit/gen_inventory.py
# (the l5_*.csv raw tables); writes only sample manifests (never verdicts — the
# second reader fills those in by hand at the code).
#
# Sibling of tools/audit/gen_pass2_sample_l4.py (the L4 sampler); same shape,
# retargeted at tools/audit/l5/l5_*.csv and extended in two ways the L5 pass-2
# instruction (Task 1) requires:
#   (1) the reading sample is stratified across the FOUR L5 populations in
#       proportion to their row counts, AND across the row kinds within each
#       population (a two-level proportional allocation) — not a single-level
#       kind stratification as in L1/L2/L4;
#   (2) L5 carries a seventh deep row kind, `io` (the instrument reads/writes
#       seam named by the pass-1 partition focus), so io is a first-class kind
#       in both samples.
#
# Two samples, two NEW fixed recorded seeds (different from every seed used so
# far in the EG-7 audit — L1/L2 used 20260711 / 424242; the 20260712-20260715
# band was the L3 pass-1/pass-2 draws; L4 pass-2 used 20260801 / 20260802):
#   (1) READING sample (protocol P5 / instruction Task 1, point 1): >= 140 rows,
#       spread across the four populations in proportion to their counts and
#       across the seven deep row kinds within each, with every deep-audited L5
#       file represented (coverage top-ups). Judged from scratch, blind to
#       pass 1. seed = SEED_READING.
#   (2) ERROR-RATE sample (protocol P6 / instruction Task 1, point 1): 40 rows,
#       UNIFORM over the whole 3372-row deep inventory (per the instruction —
#       "uniformly random over the whole 3372"). seed = SEED_ERROR.
#
# The domain is rebuilt from the RAW inventory files only (l5_*.csv), so running
# this does not read pass 1's dispositions and cannot leak them into the blind
# pass. The pass1_dispositions_* artifacts under tools/audit/l5/ are NOT read.
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
L5 = os.path.join(HERE, "l5")
PARAM_MANIFEST = os.path.join(HERE, "..", "param_manifest.json")

SEED_READING = 20260901      # Task 1 blind independent second reading (NEW)
SEED_ERROR = 20260902        # Task 1 audit-error-rate sample (NEW, different)
READING_TARGET = 140         # base proportional target (coverage top-ups may add a few)
ERROR_N = 40                 # error-rate sample size (per instruction)

# All seven deep row kinds present in the L5 inventory.
ALL_KINDS = ["function", "literal", "field", "branch", "crosslayer", "io", "decl"]

# Frozen domain sizes (self-check against inventory drift, cf. the L4 sampler).
KIND_DOMAIN = {"function": 326, "literal": 772, "field": 307, "branch": 1685,
               "crosslayer": 131, "io": 123, "decl": 28}
TOTAL_DOMAIN = 3372

# The four L5 populations, defined by file (manifest.json deep_audited_file_list +
# pass1_partition.json population_partition and its instrument sub-split). The
# grouping drives the two-level proportional draw and the coverage/reporting; it
# is the same partition pass 1 dispositioned under.
DORMANT_RESOLVER_FILES = [
    "src/composing/analysis/function/forwardoverride.cpp",
    "src/composing/analysis/function/forwardoverride.h",
    "src/composing/analysis/function/functioncadence.cpp",
    "src/composing/analysis/function/functioncadence.h",
    "src/composing/analysis/function/functionmodulation.cpp",
    "src/composing/analysis/function/functionmodulation.h",
    "src/composing/analysis/function/functionoutput.cpp",
    "src/composing/analysis/function/functionoutput.h",
    "src/composing/analysis/function/functionprogression.cpp",
    "src/composing/analysis/function/functionprogression.h",
    "src/composing/analysis/function/functionrelationallabel.cpp",
    "src/composing/analysis/function/functionrelationallabel.h",
    "src/composing/analysis/function/functionresolver.cpp",
    "src/composing/analysis/function/functionresolver.h",
    "src/composing/analysis/function/functionromannumeral.cpp",
    "src/composing/analysis/function/functionromannumeral.h",
    "src/composing/analysis/function/tonicizationlabeler.cpp",
    "src/composing/analysis/function/tonicizationlabeler.h",
    "src/composing/analysis/progression/progressionrecognizer.cpp",
    "src/composing/analysis/progression/progressionrecognizer.h",
]
INSTRUMENT_CORE_FILES = [
    "tools/compare_analyses.py",
    "tools/dcml_parser.py",
    "tools/compare_rn.py",
    "tools/characterise_bir_false.py",
    "tools/a8_rebaseline_measure.py",
    "tools/robust_stop_diff.py",
    "tools/run_bach_preset.py",
]
INSTRUMENT_GRADING_FILES = [
    "tools/analyze_inversion_errors.py",
    "tools/music21_batch.py",
    "tools/oracle_root_metric.py",
    "tools/calibration_fit.py",
    "tools/c1_reliability.py",
    "tools/stage5_fit_driver.py",
]
HARNESS_FILES = [
    "tools/batch_analyze.cpp",
]

POP_OF_FILE = {}
for f in DORMANT_RESOLVER_FILES:
    POP_OF_FILE[f] = "dormant_resolver"
for f in INSTRUMENT_CORE_FILES:
    POP_OF_FILE[f] = "instrument_core"
for f in INSTRUMENT_GRADING_FILES:
    POP_OF_FILE[f] = "instrument_grading_fitting"
for f in HARNESS_FILES:
    POP_OF_FILE[f] = "harness"

POPULATIONS = ["dormant_resolver", "instrument_core",
               "instrument_grading_fitting", "harness"]
# Expected per-population row counts (pass1_partition.json / instruction).
POP_DOMAIN = {"dormant_resolver": 815, "instrument_core": 954,
              "instrument_grading_fitting": 733, "harness": 870}

ALL_DEEP_FILES = (DORMANT_RESOLVER_FILES + INSTRUMENT_CORE_FILES +
                  INSTRUMENT_GRADING_FILES + HARNESS_FILES)


def _read_csv(name):
    with open(os.path.join(L5, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _load_manifest_sites():
    """(basename, line) and lowercase names present in param_manifest.json — a
    mechanical hint for the literal ESTABLISHED/UNFIT/DEAD manifest check.
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
    """Rebuild the deep-inventory domain (all 3372 rows) from the RAW tables."""
    rows = []
    man_sites, man_names = _load_manifest_sites()
    occ = {}  # (kind,file,line) -> running occurrence index for a stable row_id

    def add(kind, file, line, label, extra=None):
        key = (kind, file, str(line))
        idx = occ.get(key, 0)
        occ[key] = idx + 1
        rid = "{}|{}|{}#{}".format(kind, file, line, idx)
        r = {"row_id": rid, "kind": kind, "file": file, "line": str(line),
             "label": label, "population": POP_OF_FILE.get(file, "?")}
        if extra:
            r.update(extra)
        rows.append(r)

    for r in _read_csv("l5_functions.csv"):
        add("function", r["file"], r["start_line"], "{}()".format(r["name"]),
            {"name": r["name"], "end_line": r.get("end_line", "")})

    for r in _read_csv("l5_literals.csv"):
        base = os.path.basename(r["file"])
        ctx = r.get("context", "")
        in_man = ((base, r["line"]) in man_sites
                  or any(n in ctx.lower() for n in man_names))
        add("literal", r["file"], r["line"],
            "{} in {}".format(r["value"], r.get("func", "")),
            {"value": r["value"], "func": r.get("func", ""),
             "context": ctx, "in_param_manifest_hint": "yes" if in_man else "no"})

    for r in _read_csv("l5_fields.csv"):
        add("field", r["file"], r["line"],
            "{}::{}".format(r.get("type_owner", ""), r["name"]),
            {"type_owner": r.get("type_owner", ""),
             "field_type": r.get("field_type", ""),
             "name": r["name"], "context": r.get("context", "")})

    for r in _read_csv("l5_branches.csv"):
        add("branch", r["file"], r["line"],
            "{} in {}".format(r.get("kind", ""), r.get("func", "")),
            {"branch_kind": r.get("kind", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l5_crosslayer.csv"):
        add("crosslayer", r["file"], r["line"],
            "include {} -> {}".format(r.get("include", ""), r.get("target_area", "")),
            {"include": r.get("include", ""), "resolved": r.get("resolved", ""),
             "target_area": r.get("target_area", "")})

    for r in _read_csv("l5_io.csv"):
        add("io", r["file"], r["line"],
            "{} in {}".format(r.get("call", ""), r.get("func", "")),
            {"call": r.get("call", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l5_decls.csv"):
        add("decl", r["file"], r["line"], "{}".format(r.get("name", "")),
            {"type_owner": r.get("type_owner", ""), "name": r.get("name", ""),
             "context": r.get("context", "")})

    return rows


def stable_key(r):
    line = r["line"]
    lnum = int(line) if line.isdigit() else -1
    return (r["kind"], r["file"], lnum, r["row_id"])


def largest_remainder(counts, target):
    """Proportional allocation of `target` across keys by their counts, with the
    largest-remainder method. Keys with count 0 get 0."""
    total = sum(counts.values())
    if total == 0 or target <= 0:
        return {k: 0 for k in counts}
    raw = {k: target * c / total for k, c in counts.items()}
    floor = {k: int(v) for k, v in raw.items()}
    used = sum(floor.values())
    rem = sorted([k for k in counts if counts[k] > 0],
                 key=lambda k: (raw[k] - floor[k], k), reverse=True)
    i = 0
    while used < target and rem:
        floor[rem[i % len(rem)]] += 1
        used += 1
        i += 1
    return floor


def draw_reading(rows):
    """Two-level proportional draw: populations in proportion to their row
    counts, then kinds within each population in proportion to their counts."""
    rng = random.Random(SEED_READING)

    pop_counts = {p: sum(1 for r in rows if r["population"] == p)
                  for p in POPULATIONS}
    pop_alloc = largest_remainder(pop_counts, READING_TARGET)

    selected = {}
    kind_alloc_by_pop = {}
    for p in POPULATIONS:
        pop_rows = [r for r in rows if r["population"] == p]
        by_kind = {k: sorted([r for r in pop_rows if r["kind"] == k], key=stable_key)
                   for k in ALL_KINDS}
        kcounts = {k: len(v) for k, v in by_kind.items()}
        kalloc = largest_remainder(kcounts, pop_alloc[p])
        kind_alloc_by_pop[p] = kalloc
        for k in ALL_KINDS:
            take = min(kalloc[k], len(by_kind[k]))
            for r in rng.sample(by_kind[k], take):
                selected[r["row_id"]] = r

    # Coverage top-ups: every deep-audited file must appear at least once.
    covered = {selected[i]["file"] for i in selected}
    topups = []
    for f in sorted(set(ALL_DEEP_FILES) - covered):
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
        "population_counts": pop_counts, "population_allocation": pop_alloc,
        "kind_allocation_by_population": kind_alloc_by_pop,
        "coverage_topups": topups, "n_selected": len(ordered),
        "deep_files": sorted(set(ALL_DEEP_FILES)),
        "files_covered": sorted({r["file"] for r in ordered}),
        "population_breakdown": {p: sum(1 for r in ordered if r["population"] == p)
                                 for p in POPULATIONS},
        "kind_breakdown": {k: sum(1 for r in ordered if r["kind"] == k)
                           for k in ALL_KINDS},
    }
    return ordered, meta


def draw_error(rows):
    """Uniform draw of ERROR_N rows over the WHOLE 3372-row deep inventory."""
    pool = sorted(rows, key=stable_key)
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
        "population_breakdown": {p: sum(1 for r in picks if r["population"] == p)
                                 for p in sorted({r["population"] for r in picks})},
    }
    return picks_sorted, meta


def write_sample(basename, rows, meta, verdict_fields):
    cols = (["process_order", "row_id", "population", "kind", "file", "line",
             "label", "in_param_manifest_hint"] + verdict_fields)
    csv_path = os.path.join(L5, basename + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            row = dict(r)
            for f in verdict_fields:
                row.setdefault(f, "")
            row.setdefault("in_param_manifest_hint", "")
            w.writerow(row)
    json_path = os.path.join(L5, basename + ".json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, indent=1, sort_keys=True)
    return csv_path, json_path


def main():
    rows = load_rows()

    # Self-check against inventory drift before sampling.
    got_kinds = {k: sum(1 for r in rows if r["kind"] == k) for k in ALL_KINDS}
    got_pops = {p: sum(1 for r in rows if r["population"] == p) for p in POPULATIONS}
    unknown = [r["row_id"] for r in rows if r["population"] == "?"]
    if len(rows) != TOTAL_DOMAIN or got_kinds != KIND_DOMAIN or got_pops != POP_DOMAIN or unknown:
        sys.stderr.write(
            "FATAL: inventory drift. total={} (expect {}); kinds={} (expect {}); "
            "pops={} (expect {}); unknown-population rows={}\n".format(
                len(rows), TOTAL_DOMAIN, got_kinds, KIND_DOMAIN,
                got_pops, POP_DOMAIN, unknown[:5]))
        sys.exit(2)

    reading, r_meta = draw_reading(rows)
    err, e_meta = draw_error(rows)

    verdict_fields = ["verdict", "assumes", "publishes", "consumers", "edges",
                      "flag", "reason"]
    write_sample("pass2_blind_reading", reading, r_meta, verdict_fields)
    write_sample("pass2_blind_errorrate", err, e_meta, verdict_fields)

    print("reading sample: {} rows (seed {})".format(r_meta["n_selected"], r_meta["seed"]))
    print("  population allocation: {}".format(r_meta["population_allocation"]))
    print("  population breakdown : {}".format(r_meta["population_breakdown"]))
    print("  kind breakdown       : {}".format(r_meta["kind_breakdown"]))
    print("  files covered {}/{}, coverage top-ups: {}".format(
        len(r_meta["files_covered"]), len(r_meta["deep_files"]),
        len(r_meta["coverage_topups"])))
    print("error-rate sample: {} rows (seed {}), uniform over {} rows".format(
        e_meta["n"], e_meta["seed"], e_meta["domain_size"]))
    print("  kind breakdown      : {}".format(e_meta["kind_breakdown"]))
    print("  population breakdown: {}".format(e_meta["population_breakdown"]))


if __name__ == "__main__":
    main()
