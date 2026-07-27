#!/usr/bin/env python3
"""Register integrity check for OPEN_ITEMS.md (index + per-item detail files).

The register was split on 2026-07-26 (user-ratified option 1) from a single large
`OPEN_ITEMS.md` into a lean INDEX (`OPEN_ITEMS.md`) plus one detail file per item under
`open_items/OI-<n>.md`.

This instrument runs in TWO modes:

LIVING MODE (default; writes `open_items/register_check.json`) — the standing register-health
check, valid on the CURRENT tree no matter how many items are added after the split
(OI-201, OI-202, … no longer false-fail the way a baseline-only count check does):

  (a) INDEX rows ↔ detail files are a BIJECTION — every ID appears in BOTH the INDEX and as a
      detail file, no duplicates anywhere, no orphans either way;
  (b) NO detail file carries a STATUS of its own (the two-place drift killer, checked
      mechanically): the status-authoritative header sentinel must be present, and NO
      `| OPEN` / `| ✅ RESOLVED`-style status CELL may appear OUTSIDE the single verbatim
      historical row block (the row itself is the item's verbatim pre-split/created row and
      keeps its own status cell — that is the ONE allowed place; a narrative resolution note
      is prose, not a pipe-delimited status cell, and is unaffected);
  (c) for the ORIGINAL split items (those present at the frozen baseline `cb246a7580`), the
      detail row stays BYTE-IDENTICAL to the pre-split row (the historical guarantee below,
      UNWEAKENED); post-baseline items are checked structurally (a)+(b) only, never against
      the baseline (there is no baseline row to compare against — inventing one would be a
      false premise).

SPLIT-BASELINE MODE (`--split-baseline`; writes `open_items/split_reconciliation.json`) — the
historical split-event reconciliation, UNCHANGED, documenting that the 2026-07-26 split lost
and added nothing (#12 / the ratified doc-split discipline, #17f):

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

Exit code 0 iff every check passes; any mismatch is a non-zero exit (a STOP).
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
REPORT_PATH = os.path.join(DETAIL_DIR, "split_reconciliation.json")   # split-baseline mode
LIVING_REPORT_PATH = os.path.join(DETAIL_DIR, "register_check.json")  # living mode (default)

# A register ROW begins with the item ID in the FIRST table cell: "| OI-<n> | ...".
# (An OI-<n> appearing later in a row's prose is a cross-reference, not a row, and is ignored.)
ROW_RE = re.compile(r"^\|\s*(OI-\d+)\s*\|")

# The status-authoritative header sentinel every detail file must carry (a substring match, so
# it is robust to the em-dash/encoding of the surrounding text).
SENTINEL_SUBSTR = "STATUS IS AUTHORITATIVE IN THE INDEX"

# A pipe-delimited STATUS cell: a table cell whose content opens with a register status token
# (optionally the ✅ mark). This is what a detail file may NOT carry outside its one verbatim
# historical row block — the two-place-status drift killer. Prose (no leading pipe) is exempt.
STATUS_CELL_RE = re.compile(
    r"\|\s*(?:✅\s*)?"
    r"(?:OPEN|RESOLVED|COMPLETE|PROBED|DECLARED|DEFERRED|MERGED|SUPERSEDED|EXECUTED)\b"
)


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


def check_status_discipline(oid):
    """Living-mode check (b): the detail file must carry the header sentinel and NO status
    cell of its own outside the one verbatim historical row block.

    Returns a list of violation strings (empty == compliant)."""
    path = os.path.join(DETAIL_DIR, f"{oid}.md")
    if not os.path.isfile(path):
        return ["detail-file-missing"]
    violations = []
    sentinel_present = False
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\r\n")
            if SENTINEL_SUBSTR in line:
                sentinel_present = True
            if ROW_RE.match(line):
                continue  # the item's own verbatim row — its status cell is the allowed one
            if STATUS_CELL_RE.search(line):
                violations.append("stray-status-cell: " + line.strip()[:90])
    if not sentinel_present:
        violations.append("sentinel-line-missing")
    return violations


def detail_file_ids():
    """The set of item IDs that have a detail file under open_items/."""
    return {
        f[:-3] for f in os.listdir(DETAIL_DIR)
        if re.fullmatch(r"OI-\d+\.md", f)
    }


def run_living(args):
    """Default mode — the standing register-health check on the current tree."""
    presplit_rows, _ = read_presplit_rows(args.baseline)
    baseline_ids = set(presplit_rows)          # the original split items (byte-verbatim guarantee)
    index_ids = read_index_ids(INDEX_PATH)
    index_id_set = set(index_ids)
    detail_ids = detail_file_ids()

    index_dupes = sorted({x for x in index_ids if index_ids.count(x) > 1})
    orphan_index = sorted(index_id_set - detail_ids, key=lambda s: int(s.split("-")[1]))  # in index, no detail
    orphan_detail = sorted(detail_ids - index_id_set, key=lambda s: int(s.split("-")[1]))  # detail, not in index
    bijection_ok = (index_id_set == detail_ids) and not index_dupes

    per_item = []
    all_ok = True
    for oid in sorted(index_id_set | detail_ids, key=lambda s: int(s.split("-")[1])):
        index_present = oid in index_id_set
        detail_present = oid in detail_ids
        is_baseline = oid in baseline_ids
        status_violations = check_status_discipline(oid) if detail_present else ["detail-file-missing"]
        if is_baseline and detail_present:
            detail_row, _ = read_detail_row(oid)
            verbatim_ok = detail_row == presplit_rows[oid]
        else:
            verbatim_ok = None  # post-baseline: structural check only, no baseline row to compare
        ok = (
            index_present and detail_present
            and not status_violations
            and verbatim_ok is not False
        )
        all_ok = all_ok and ok
        per_item.append({
            "id": oid,
            "post_baseline": not is_baseline,
            "index_present": index_present,
            "detail_present": detail_present,
            "status_discipline_ok": not status_violations,
            "status_violations": status_violations,
            "baseline_verbatim_ok": verbatim_ok,  # None == not applicable (post-baseline)
            "ok": ok,
        })

    overall_ok = all_ok and bijection_ok
    report = {
        "mode": "living",
        "baseline_commit": args.baseline,
        "index_item_count": len(index_id_set),
        "detail_file_count": len(detail_ids),
        "baseline_item_count": len(baseline_ids),
        "post_baseline_ids": sorted(index_id_set - baseline_ids, key=lambda s: int(s.split("-")[1])),
        "bijection_ok": bijection_ok,
        "index_duplicate_ids": index_dupes,
        "index_without_detail_file": orphan_index,
        "detail_file_without_index_row": orphan_detail,
        "status_discipline_violations": [
            {"id": r["id"], "violations": r["status_violations"]}
            for r in per_item if not r["status_discipline_ok"]
        ],
        "baseline_content_mismatches": [
            r["id"] for r in per_item if r["baseline_verbatim_ok"] is False
        ],
        "overall_ok": overall_ok,
        "per_item": per_item,
    }

    with open(LIVING_REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"living mode: index={len(index_id_set)} detail={len(detail_ids)} "
          f"baseline={len(baseline_ids)} post-baseline={len(report['post_baseline_ids'])}")
    if overall_ok:
        print(f"OVERALL PASS — bijection holds, no detail file carries a status of its own, "
              f"and all {len(baseline_ids)} original items stay byte-verbatim "
              f"(report: {os.path.relpath(LIVING_REPORT_PATH, REPO_ROOT)})")
        return 0
    print("OVERALL FAIL — register integrity broken:")
    for key in ("index_duplicate_ids", "index_without_detail_file",
                "detail_file_without_index_row", "status_discipline_violations",
                "baseline_content_mismatches"):
        if report[key]:
            print(f"  {key}: {report[key]}")
    return 1


def run_split_baseline(args):
    """Historical split-event reconciliation — UNCHANGED from the original instrument."""
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


def main():
    # Console-output robustness (OI-137 class): a violation string can echo a register status
    # cell containing non-ASCII (e.g. the ✅ mark), which crashes a cp1252 stdout. Degrade to a
    # replacement char instead of raising — the utf-8 JSON report stays the authoritative surface.
    try:
        sys.stdout.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", default=BASELINE_COMMIT,
                    help="pre-split baseline commit (default: %(default)s)")
    ap.add_argument("--split-baseline", action="store_true",
                    help="run the historical split-event reconciliation "
                         "(writes open_items/split_reconciliation.json) instead of the "
                         "default living register-health check "
                         "(writes open_items/register_check.json)")
    args = ap.parse_args()
    if args.split_baseline:
        return run_split_baseline(args)
    return run_living(args)


if __name__ == "__main__":
    sys.exit(main())
