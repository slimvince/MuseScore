#!/usr/bin/env python3
"""Reconciliation check for the OPEN_ITEMS.md register split (index + per-item detail files).

The register was split on 2026-07-26 (user-ratified option 1) from a single large
`OPEN_ITEMS.md` into a lean INDEX (`OPEN_ITEMS.md`) plus one detail file per item under
`open_items/OI-<n>.md`. This instrument proves, mechanically and byte-for-byte, that the
split lost and added nothing (#12 / the ratified doc-split discipline, #17f):

  (a) every item ID present in the pre-split file exists in the INDEX AND has a detail file;
  (b) every detail file's moved content is BYTE-IDENTICAL to the corresponding pre-split
      row's content (the ONLY declared transformation is that each detail file prepends a
      fixed three-line header — the ID+name line, the status-authoritative disclaimer, and
      the section line — which is excluded from the comparison; the row text itself is kept
      verbatim, table pipes included, no row-to-prose unwrapping);
  (c) no item is lost, none added (pre-split ID set == index ID set == detail-file ID set).

Line-ending note: comparison strips only trailing CR/LF from each single-line row, so it is
robust to a CRLF-vs-LF checkout (`.gitattributes` `text=auto`); it is content-preserving —
each register row is a single line, so no internal byte is affected.

The pre-split file is read from git at the baseline commit (the commit immediately BEFORE the
split), so the reconciliation is reproducible from the object store, not from a transient copy.

Writes `open_items/split_reconciliation.json` (counts + per-item verdict). Exit code 0 iff every
item reconciles; any mismatch is a non-zero exit (a STOP).
"""
import argparse
import json
import os
import re
import subprocess
import sys

# The commit immediately BEFORE the register split (the pre-split OPEN_ITEMS.md lives here).
BASELINE_COMMIT = "cb246a7580"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(REPO_ROOT, "OPEN_ITEMS.md")
DETAIL_DIR = os.path.join(REPO_ROOT, "open_items")
REPORT_PATH = os.path.join(DETAIL_DIR, "split_reconciliation.json")

# A register ROW begins with the item ID in the FIRST table cell: "| OI-<n> | ...".
# (An OI-<n> appearing later in a row's prose is a cross-reference, not a row, and is ignored.)
ROW_RE = re.compile(r"^\|\s*(OI-\d+)\s*\|")


def _row_id(line):
    m = ROW_RE.match(line)
    return m.group(1) if m else None


def read_presplit_rows(commit):
    """id -> verbatim pre-split row line (trailing CR/LF stripped)."""
    blob = subprocess.check_output(
        ["git", "show", f"{commit}:OPEN_ITEMS.md"], cwd=REPO_ROOT
    ).decode("utf-8")
    rows = {}
    dupes = []
    for line in blob.split("\n"):
        oid = _row_id(line)
        if oid is None:
            continue
        if oid in rows:
            dupes.append(oid)
        rows[oid] = line.rstrip("\r\n")
    return rows, dupes


def read_index_ids(path):
    """Ordered list of item IDs heading a row in the post-split index."""
    ids = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            oid = _row_id(line)
            if oid is not None:
                ids.append(oid)
    return ids


def read_detail_row(oid):
    """The single moved row line in a detail file (or None if the file/row is absent)."""
    path = os.path.join(DETAIL_DIR, f"{oid}.md")
    if not os.path.isfile(path):
        return None, "detail-file-missing"
    matches = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if _row_id(line) is not None:
                matches.append(line.rstrip("\r\n"))
    if len(matches) == 0:
        return None, "no-row-in-detail-file"
    if len(matches) > 1:
        return None, "multiple-rows-in-detail-file"
    return matches[0], None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline", default=BASELINE_COMMIT,
                    help="pre-split baseline commit (default: %(default)s)")
    args = ap.parse_args()

    presplit_rows, presplit_dupes = read_presplit_rows(args.baseline)
    index_ids = read_index_ids(INDEX_PATH)
    presplit_ids = set(presplit_rows)
    index_id_set = set(index_ids)

    index_dupes = sorted({x for x in index_ids if index_ids.count(x) > 1})

    per_item = []
    all_ok = True
    for oid in sorted(presplit_ids, key=lambda s: int(s.split("-")[1])):
        detail_row, detail_err = read_detail_row(oid)
        index_present = oid in index_id_set
        detail_present = detail_row is not None
        content_match = detail_present and detail_row == presplit_rows[oid]
        ok = index_present and detail_present and content_match
        all_ok = all_ok and ok
        per_item.append({
            "id": oid,
            "index_present": index_present,
            "detail_present": detail_present,
            "content_byte_identical": content_match,
            "detail_error": detail_err,
            "ok": ok,
        })

    missing_from_index = sorted(presplit_ids - index_id_set, key=lambda s: int(s.split("-")[1]))
    added_in_index = sorted(index_id_set - presplit_ids, key=lambda s: int(s.split("-")[1]))
    detail_ids = {
        f[:-3] for f in os.listdir(DETAIL_DIR)
        if re.fullmatch(r"OI-\d+\.md", f)
    }
    missing_detail = sorted(presplit_ids - detail_ids, key=lambda s: int(s.split("-")[1]))
    extra_detail = sorted(detail_ids - presplit_ids, key=lambda s: int(s.split("-")[1]))

    counts_ok = (
        len(presplit_ids) == len(index_id_set) == len(detail_ids)
        and not presplit_dupes and not index_dupes
        and not missing_from_index and not added_in_index
        and not missing_detail and not extra_detail
    )
    overall_ok = all_ok and counts_ok

    report = {
        "baseline_commit": args.baseline,
        "presplit_item_count": len(presplit_ids),
        "index_item_count": len(index_id_set),
        "detail_file_count": len(detail_ids),
        "counts_equal": len(presplit_ids) == len(index_id_set) == len(detail_ids),
        "presplit_duplicate_ids": sorted(set(presplit_dupes)),
        "index_duplicate_ids": index_dupes,
        "missing_from_index": missing_from_index,
        "added_in_index": added_in_index,
        "missing_detail_file": missing_detail,
        "extra_detail_file": extra_detail,
        "content_mismatches": [r["id"] for r in per_item if not r["content_byte_identical"]],
        "overall_ok": overall_ok,
        "per_item": per_item,
    }

    with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"baseline {args.baseline}: presplit={len(presplit_ids)} index={len(index_id_set)} "
          f"detail={len(detail_ids)}")
    if overall_ok:
        print(f"OVERALL PASS — all {len(presplit_ids)} items reconcile byte-for-byte "
              f"(report: {os.path.relpath(REPORT_PATH, REPO_ROOT)})")
        return 0
    print("OVERALL FAIL — reconciliation mismatch:")
    for key in ("presplit_duplicate_ids", "index_duplicate_ids", "missing_from_index",
                "added_in_index", "missing_detail_file", "extra_detail_file", "content_mismatches"):
        if report[key]:
            print(f"  {key}: {report[key]}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
