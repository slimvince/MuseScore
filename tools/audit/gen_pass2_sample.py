#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_pass2_sample.py — draw the two random row samples for the L1/L2
# certification audit, PASS 2 (EG-7 / OI-84). Read-only over the machine
# inventory produced by tools/audit/gen_inventory.py; writes only sample
# manifests (never verdicts — the auditor fills those in by hand at the code).
#
# Two samples, two fixed recorded seeds:
#   (1) BLIND sample  (protocol P5 / instruction Task 1): >= 100 rows, spread
#       across the FIVE row kinds (functions, literals, fields, branches,
#       crosslayer) in proportion to their counts, with every L1/L2 file
#       represented. Judged from scratch, blind to pass 1.  seed = SEED_BLIND.
#   (2) ERROR-RATE sample (protocol P6 / instruction Task 4): 40 rows, uniform
#       over the FULL disposition domain (all six inventory row kinds PLUS the
#       file-classification rows = the exact set pass 1 disposed). Used to
#       measure the audit's own error rate.  seed = SEED_ERROR.
#
# The domain is rebuilt from the NON-VERDICT inventory files only
# (file_table.csv + l1l2_*.csv), so running this does not read pass 1's
# dispositions and cannot leak them into the blind pass.
#
# Determinism: every input list is sorted by a stable key before sampling, so
# the draw depends only on the seed and the frozen inventory, not on filesystem
# order. Re-running reproduces byte-identical samples.

import copy
import csv
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")

SEED_BLIND = 20260711        # Task 1 blind second reading
SEED_ERROR = 424242          # Task 4 audit-error-rate sample (different fixed seed)
BLIND_TARGET = 110           # base proportional target (coverage top-ups may add a few)
ERROR_N = 40                 # Task 4 sample size (Cowork's proposal)

# The five row kinds the blind sample is stratified over (Task 1, point 2).
BLIND_KINDS = ["function", "literal", "field", "branch", "crosslayer"]


def _read_csv(name):
    path = os.path.join(L1L2, name)
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_rows():
    """Rebuild the full disposition domain from the non-verdict inventory files.

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

    # file-classification rows (kind=file) — part of the pass-1 disposition set.
    for r in _read_csv("file_table.csv"):
        add("file", r["file"], "", r.get("tag", ""),
            {"tag": r.get("tag", ""), "reason": r.get("reason", "")})

    for r in _read_csv("l1l2_functions.csv"):
        add("function", r["file"], r["start_line"],
            "{}()".format(r["name"]),
            {"name": r["name"], "end_line": r.get("end_line", "")})

    for r in _read_csv("l1l2_literals.csv"):
        add("literal", r["file"], r["line"],
            "{} in {}".format(r["value"], r.get("func", "")),
            {"value": r["value"], "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_fields.csv"):
        add("field", r["file"], r["line"],
            "{}::{}".format(r.get("type_owner", ""), r["name"]),
            {"type_owner": r.get("type_owner", ""), "field_type": r.get("field_type", ""),
             "name": r["name"], "context": r.get("context", "")})

    for r in _read_csv("l1l2_branches.csv"):
        add("branch", r["file"], r["line"],
            "{} in {}".format(r.get("kind", ""), r.get("func", "")),
            {"branch_kind": r.get("kind", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_decls.csv"):
        add("decl", r["file"], r["line"],
            "{}".format(r.get("name", "")),
            {"type_owner": r.get("type_owner", ""), "name": r.get("name", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_crosslayer.csv"):
        add("crosslayer", r["file"], r["line"],
            "include {} -> {}".format(r.get("include", ""), r.get("target_area", "")),
            {"include": r.get("include", ""), "resolved": r.get("resolved", ""),
             "target_area": r.get("target_area", "")})

    return rows


def stable_key(r):
    # kind, file, numeric-line (line may be ''), then row_id tail for uniqueness.
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


def l1l2_files(rows):
    """Every file tagged L1 or L2 by the first pass (from the file rows)."""
    out = set()
    for r in rows:
        if r["kind"] == "file" and r.get("tag") in ("L1", "L2"):
            out.add(r["file"])
    return out


def draw_blind(rows):
    pool = [r for r in rows if r["kind"] in BLIND_KINDS]
    by_kind = {k: sorted([r for r in pool if r["kind"] == k], key=stable_key)
               for k in BLIND_KINDS}
    counts = {k: len(v) for k, v in by_kind.items()}
    alloc = largest_remainder(counts, BLIND_TARGET)

    rng = random.Random(SEED_BLIND)
    selected = {}
    for k in BLIND_KINDS:
        picks = rng.sample(by_kind[k], alloc[k])
        for r in picks:
            selected[r["row_id"]] = r

    # Coverage guarantee: every L1/L2 file must appear at least once.
    covered_files = {selected[i]["file"] for i in selected}
    need = l1l2_files(rows)
    topups = []
    for f in sorted(need - covered_files):
        cand = sorted([r for r in pool if r["file"] == f and r["row_id"] not in selected],
                      key=stable_key)
        if not cand:
            # File has no row in the five sampled kinds — fall back to ANY row of it.
            cand = sorted([r for r in rows if r["file"] == f and r["row_id"] not in selected],
                          key=stable_key)
        if cand:
            pick = rng.choice(cand)
            selected[pick["row_id"]] = pick
            topups.append(pick["row_id"])

    # Deep-copy the selected rows before stamping process_order: load_rows()
    # hands out shared dict objects, and the error-rate draw below stamps the
    # SAME objects if a row is picked by both samples — copying isolates them.
    ordered = [copy.deepcopy(selected[i]) for i in selected]
    rng.shuffle(ordered)   # the random processing order the auditor works through
    for i, r in enumerate(ordered):
        r["process_order"] = i + 1

    meta = {
        "seed": SEED_BLIND,
        "target_base": BLIND_TARGET,
        "kind_counts": counts,
        "kind_allocation": alloc,
        "coverage_topups": topups,
        "n_selected": len(ordered),
        "l1l2_files": sorted(need),
        "files_covered": sorted({r["file"] for r in ordered}),
    }
    return ordered, meta


def draw_error(rows):
    pool = sorted(rows, key=stable_key)   # full domain, all kinds incl. file + decl
    rng = random.Random(SEED_ERROR)
    picks = rng.sample(pool, ERROR_N)
    # Deep-copy before stamping process_order (shared dict objects — see draw_blind).
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


def write_sample(basename, rows, meta, verdict_fields):
    cols = ["process_order", "row_id", "kind", "file", "line", "label"] + verdict_fields
    csv_path = os.path.join(L1L2, basename + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            row = dict(r)
            for f in verdict_fields:
                row.setdefault(f, "")
            w.writerow(row)
    json_path = os.path.join(L1L2, basename + ".json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, indent=1, sort_keys=True)
    return csv_path, json_path


def main():
    rows = load_rows()
    total = len(rows)
    if total != 688:
        # The pass-1 disposition domain is 688 rows (472 inventory + 216 file).
        # A mismatch means the frozen inventory changed under us — stop loudly.
        sys.stderr.write(
            "FATAL: rebuilt domain = {} rows, expected 688. "
            "Inventory drift — do not sample.\n".format(total))
        sys.exit(2)

    blind, blind_meta = draw_blind(rows)
    err, err_meta = draw_error(rows)

    write_sample("pass2_blind_sample", blind, blind_meta,
                 ["verdict", "flag", "reason"])
    write_sample("pass2_errorrate_sample", err, err_meta,
                 ["pass1_verdict", "pass2_check", "agree", "note"])

    print("domain rows: {}".format(total))
    print("blind sample: {} rows (seed {}), files covered {}/{}".format(
        blind_meta["n_selected"], blind_meta["seed"],
        len(blind_meta["files_covered"]), len(blind_meta["l1l2_files"])))
    print("  kind allocation: {}".format(blind_meta["kind_allocation"]))
    print("  coverage top-ups: {}".format(blind_meta["coverage_topups"]))
    print("error-rate sample: {} rows (seed {}), kinds {}".format(
        err_meta["n"], err_meta["seed"], err_meta["kind_breakdown"]))


if __name__ == "__main__":
    main()
