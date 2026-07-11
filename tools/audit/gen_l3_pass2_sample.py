#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_l3_pass2_sample.py — draw the two random row samples for the Layer-3
# (key/mode) certification audit, PASS 2 (EG-7 / OI-84), and merge the
# auditor's hand-authored verdicts into the final blind artifacts.
#
# Adapted from tools/audit/gen_pass2_sample.py (the L1/L2 pass-2 sampler).
# Read-only over the machine inventory produced by tools/audit/gen_inventory.py
# --layer l3 (tools/audit/l3/l3_*.csv). It NEVER writes verdicts itself — the
# auditor judges each sampled row from the code by hand and records the verdict
# in a separate hand-authored file (pass2_reading_verdicts.json /
# pass2_errorrate_verdicts.json, keyed by row_id). This script only (a) selects
# rows deterministically and (b) merges those authored verdicts into the final
# artifacts, so the sample SELECTION stays purely mechanical and the final
# CSV/JSON is always regenerated, never hand-edited.
#
# Two samples, two NEW fixed recorded seeds (different from 20260712/20260713,
# the pass-1 seeds the instruction reserved):
#   (1) READING sample  (protocol P5 / Task 1, point 1): >= 110 rows, spread
#       across the FIVE row kinds (function, literal, field, branch, crosslayer)
#       in proportion to their counts, with every layer-3 file represented.
#       This mirrors the L1/L2 pass-2 stratification exactly: the sixth kind
#       (decl, 12 rows) is excluded from the proportional strata but remains
#       reachable via the per-file coverage top-up and is fully present in the
#       error-rate domain below.  seed = SEED_READING.
#   (2) ERROR-RATE sample (protocol P6 / Task 2, point 3): 40 rows, uniform
#       over the FULL layer-3 inventory (all SIX row kinds = 1943 rows). Judged
#       blind FIRST; the disagreement fraction vs pass 1 is the audit's measured
#       error rate.  seed = SEED_ERROR.
#
# The domain is rebuilt from the inventory CSVs only, so running this does not
# read pass 1's dispositions and cannot leak them into the blind pass.
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
L3 = os.path.join(HERE, "l3")

SEED_READING = 20260714      # Task 1 blind second reading (NEW seed)
SEED_ERROR = 20260715        # Task 2 audit-error-rate sample (NEW seed)
READING_TARGET = 110         # base proportional target (coverage top-ups may add a few)
ERROR_N = 40                 # error-rate sample size (Cowork's proposal)
DOMAIN_EXPECTED = 1943       # the layer-3 inventory row count (77+957+502+301+12+94)

# The five row kinds the reading sample is stratified over (Task 1, point 1),
# matching the L1/L2 pass-2 precedent. 'decl' (12 rows) is excluded here but is
# reachable via coverage top-up and is in the full error-rate domain.
READING_KINDS = ["function", "literal", "field", "branch", "crosslayer"]


def _read_csv(name):
    path = os.path.join(L3, name)
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_rows():
    """Rebuild the full 1943-row layer-3 inventory domain from the l3_*.csv files.

    Returns a list of row dicts, each with a stable 'row_id', a 'kind', the
    owning 'file', a 'line', and a short 'label' for the auditor to orient by.
    """
    rows = []

    def add(kind, file, line, label, extra=None):
        rid = "{}|{}|{}|{}".format(kind, file, line, len(rows))
        r = {"row_id": rid, "kind": kind, "file": file, "line": str(line),
             "label": label}
        if extra:
            r.update(extra)
        rows.append(r)

    for r in _read_csv("l3_functions.csv"):
        add("function", r["file"], r["start_line"],
            "{}()".format(r["name"]),
            {"name": r["name"], "end_line": r.get("end_line", "")})

    for r in _read_csv("l3_literals.csv"):
        add("literal", r["file"], r["line"],
            "{} in {}".format(r["value"], r.get("func", "")),
            {"value": r["value"], "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l3_branches.csv"):
        add("branch", r["file"], r["line"],
            "{} in {}".format(r.get("kind", ""), r.get("func", "")),
            {"branch_kind": r.get("kind", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l3_fields.csv"):
        add("field", r["file"], r["line"],
            "{}::{}".format(r.get("type_owner", ""), r["name"]),
            {"type_owner": r.get("type_owner", ""), "field_type": r.get("field_type", ""),
             "name": r["name"], "context": r.get("context", "")})

    for r in _read_csv("l3_decls.csv"):
        add("decl", r["file"], r["line"],
            "{}".format(r.get("name", "")),
            {"type_owner": r.get("type_owner", ""), "name": r.get("name", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l3_crosslayer.csv"):
        add("crosslayer", r["file"], r["line"],
            "include {} -> {}".format(r.get("include", ""), r.get("target_area", "")),
            {"include": r.get("include", ""), "resolved": r.get("resolved", ""),
             "target_area": r.get("target_area", "")})

    return rows


def stable_key(r):
    line = r["line"]
    lnum = int(line) if line.isdigit() else -1
    return (r["kind"], r["file"], lnum, r["row_id"])


def largest_remainder(counts, target):
    """Allocate `target` across kinds proportional to counts; largest remainder."""
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


def l3_files(rows):
    """Every file that appears in the layer-3 inventory (the coverage set)."""
    return {r["file"] for r in rows}


def draw_reading(rows):
    pool = [r for r in rows if r["kind"] in READING_KINDS]
    by_kind = {k: sorted([r for r in pool if r["kind"] == k], key=stable_key)
               for k in READING_KINDS}
    counts = {k: len(v) for k, v in by_kind.items()}
    alloc = largest_remainder(counts, READING_TARGET)

    rng = random.Random(SEED_READING)
    selected = {}
    for k in READING_KINDS:
        picks = rng.sample(by_kind[k], alloc[k])
        for r in picks:
            selected[r["row_id"]] = r

    # Coverage guarantee: every layer-3 file must appear at least once.
    covered_files = {selected[i]["file"] for i in selected}
    need = l3_files(rows)
    topups = []
    for f in sorted(need - covered_files):
        cand = sorted([r for r in pool if r["file"] == f and r["row_id"] not in selected],
                      key=stable_key)
        if not cand:
            # File has no row in the five sampled kinds — fall back to ANY row.
            cand = sorted([r for r in rows if r["file"] == f and r["row_id"] not in selected],
                          key=stable_key)
        if cand:
            pick = rng.choice(cand)
            selected[pick["row_id"]] = pick
            topups.append(pick["row_id"])

    ordered = [copy.deepcopy(selected[i]) for i in selected]
    rng.shuffle(ordered)   # the random processing order the auditor works through
    for i, r in enumerate(ordered):
        r["process_order"] = i + 1

    meta = {
        "seed": SEED_READING,
        "target_base": READING_TARGET,
        "kind_counts": counts,
        "kind_allocation": alloc,
        "coverage_topups": topups,
        "n_selected": len(ordered),
        "l3_files": sorted(need),
        "files_covered": sorted({r["file"] for r in ordered}),
    }
    return ordered, meta


def draw_error(rows):
    pool = sorted(rows, key=stable_key)   # full 1943-row domain, all six kinds
    rng = random.Random(SEED_ERROR)
    picks = rng.sample(pool, ERROR_N)
    picks_sorted = [copy.deepcopy(r) for r in sorted(picks, key=stable_key)]
    for i, r in enumerate(picks_sorted):
        r["process_order"] = i + 1
    meta = {
        "seed": SEED_ERROR,
        "n": ERROR_N,
        "domain_size": len(pool),
        "kind_breakdown": {k: sum(1 for r in picks if r["kind"] == k)
                           for k in sorted({r["kind"] for r in picks})},
    }
    return picks_sorted, meta


def load_verdicts(name):
    """Hand-authored verdicts, keyed by the sample's process_order (a stable
    1..N index fixed by the seed). Absent file -> empty (skeleton)."""
    path = os.path.join(L3, name)
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def merge_verdicts(rows, verdicts):
    """Attach 'verdict' and 'reasoning' to each row from the authored file
    (keyed by str(process_order)). Returns (merged_rows, n_missing). Never
    invents a verdict — an unjudged row stays blank and is counted missing.
    """
    out = []
    missing = 0
    for r in rows:
        r = dict(r)
        v = verdicts.get(str(r["process_order"]))
        if v is None:
            r["verdict"] = ""
            r["reasoning"] = ""
            missing += 1
        else:
            r["verdict"] = v.get("verdict", "")
            r["reasoning"] = v.get("reasoning", "")
            if not r["verdict"]:
                missing += 1
        out.append(r)
    return out, missing


def write_sample(basename, rows, meta):
    cols = ["process_order", "row_id", "kind", "file", "line", "label",
            "verdict", "reasoning"]
    csv_path = os.path.join(L3, basename + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            row = dict(r)
            for f in ("verdict", "reasoning"):
                row.setdefault(f, "")
            w.writerow(row)
    json_path = os.path.join(L3, basename + ".json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, indent=1, sort_keys=True)
    return csv_path, json_path


def main():
    rows = load_rows()
    total = len(rows)
    if total != DOMAIN_EXPECTED:
        sys.stderr.write(
            "FATAL: rebuilt domain = {} rows, expected {}. "
            "Inventory drift — do not sample.\n".format(total, DOMAIN_EXPECTED))
        sys.exit(2)

    reading, reading_meta = draw_reading(rows)
    err, err_meta = draw_error(rows)

    reading_v = load_verdicts("pass2_reading_verdicts.json")
    err_v = load_verdicts("pass2_errorrate_verdicts.json")
    reading, r_missing = merge_verdicts(reading, reading_v)
    err, e_missing = merge_verdicts(err, err_v)
    reading_meta["verdicts_missing"] = r_missing
    err_meta["verdicts_missing"] = e_missing

    write_sample("pass2_blind_reading", reading, reading_meta)
    write_sample("pass2_blind_errorrate", err, err_meta)

    # Reproducibility stamp (#16): inherit the inventory's corpus hash + producing
    # commit from tools/audit/l3/manifest.json so the samples are pinned to the same
    # frozen inventory pass 1 ran under.
    inv_manifest = {}
    inv_path = os.path.join(L3, "manifest.json")
    if os.path.exists(inv_path):
        with open(inv_path, encoding="utf-8") as fh:
            inv_manifest = json.load(fh)
    manifest = {
        "instrument": "tools/audit/gen_l3_pass2_sample.py",
        "audit": "EG-7 Layer-3 (key/mode) certification, PASS 2 (blind reading + error rate)",
        "domain_rows": total,
        "reading_sample": {"seed": SEED_READING, "n": reading_meta["n_selected"],
                           "target_base": READING_TARGET, "kinds": READING_KINDS,
                           "files_covered": len(reading_meta["files_covered"]),
                           "verdicts_missing": r_missing},
        "errorrate_sample": {"seed": SEED_ERROR, "n": ERROR_N,
                             "verdicts_missing": e_missing},
        "inventory_instrument": inv_manifest.get("instrument"),
        "inventory_head_commit": inv_manifest.get("head_commit"),
        "corpus_hash": inv_manifest.get("corpus_hash"),
    }
    with open(os.path.join(L3, "pass2_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)

    print("domain rows: {}".format(total))
    print("reading sample: {} rows (seed {}), files covered {}/{}, verdicts missing {}".format(
        reading_meta["n_selected"], reading_meta["seed"],
        len(reading_meta["files_covered"]), len(reading_meta["l3_files"]),
        r_missing))
    print("  kind allocation: {}".format(reading_meta["kind_allocation"]))
    print("  coverage top-ups: {}".format(reading_meta["coverage_topups"]))
    print("error-rate sample: {} rows (seed {}), kinds {}, verdicts missing {}".format(
        err_meta["n"], err_meta["seed"], err_meta["kind_breakdown"], e_missing))
    if r_missing or e_missing:
        print("NOTE: skeleton written; author verdicts then re-run to merge.")


if __name__ == "__main__":
    main()
