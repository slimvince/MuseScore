#!/usr/bin/env python3
"""OI-207 adjudication, Task 3 — give every harvested cluster a recorded disposition.

A layer OVER the harvest (`decision_candidates.json`) and the clustering
(`decision_clusters.json`), which it never writes.  It reads the hand-authored
backbone (`backbone_decisions.json` — the adjudication's Task-1/Task-2 judgment,
enumerated by reading the ARCHITECTURE.md layer specifications in full) and
assigns each of the 14,460 clusters exactly one disposition from the ratified
vocabulary.

The permitted dispositions (OI-207 dispatch, Task 3):

    restates        the cluster restates a backbone decision (named)
    not-a-decision  narrative, an instruction to a working session, a heading
    boilerplate     the labelled boilerplate bucket, confirmed
    no-spec-home    a decision whose only recorded home is outside a layer
                    specification — the valuable class, which feeds Task 4
    unresolved      could not be told.  Permitted and wanted: an honest
                    unresolved beats a guessed disposition, and the count is
                    itself a finding about the record's legibility.

Every disposition is produced by a NUMBERED, STATED bulk rule; the rule that
fired and the number of clusters it covered are both recorded, so the judgment
is reviewable rather than hidden inside a total.  No cluster may carry more than
one disposition and none may carry none — `--check` proves both.

Usage
    python tools/audit/decisions/gen_cluster_dispositions.py --verify
        Establishment pass (#19): every backbone verbatim quote must be found in
        the file it is cited to.  Exits nonzero on any miss.

    python tools/audit/decisions/gen_cluster_dispositions.py
        Writes cluster_dispositions.json / .csv / disposition_manifest.json.

    python tools/audit/decisions/gen_cluster_dispositions.py --check
        Re-reads the emitted artifacts and proves the coverage guarantee.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent

CANDIDATES = HERE / "decision_candidates.json"
CLUSTERS = HERE / "decision_clusters.json"
BACKBONE = HERE / "backbone_decisions.json"

OUT_JSON = HERE / "cluster_dispositions.json"
OUT_CSV = HERE / "cluster_dispositions.csv"
OUT_MANIFEST = HERE / "disposition_manifest.json"

DISPOSITIONS = ("restates", "not-a-decision", "boilerplate", "no-spec-home", "unresolved")

# ── The bulk rules, in the order they are applied.  First match wins. ─────────
# Each entry: (rule id, the rule as it is stated in the report).
RULES = [
    ("BR-1", "The clustering layer already labelled this cluster boilerplate "
             "(a recurring heading, table header row, or standing dispatch instruction line). "
             "Confirmed, not re-judged."),
    ("BR-2", "Every occurrence in the cluster is a section HEADING. A heading names a subject; "
             "it does not state a decision."),
    ("BR-3", "The cluster's text matches at least one backbone decision whose home IS a layer "
             "specification. Recorded as restating that decision (named)."),
    ("BR-4", "The cluster's text matches one or more backbone decisions, ALL of which are recorded "
             "outside any layer specification. Recorded as a decision with no layer-specification "
             "home (named) — the Task-4 documentation-gap class."),
    ("BR-5", "The text is an instruction to a working session or dispatch scaffolding "
             "(a read-only / no-src-change banner, a push or commit instruction, a session-start "
             "reading instruction, a build-and-test instruction), not a decision about the system."),
    ("BR-6", "A Claude Code session report or dispatch whose text is a measurement or delivery "
             "narrative (it carries a figure, a test count, a commit hash, or a delivery/verification "
             "verb) and matches no backbone decision. A report of work done, not a ruling."),
    ("BR-7", "A table row admitted by the harvest's BROAD signature tier only — an inventory or "
             "status cell, not a stated decision."),
    ("BR-8", "Residual: none of the above applies. Recorded UNRESOLVED — the honest outcome, and "
             "the count is a finding about the record's legibility."),
]

HEADING_KINDS = {"heading"}

SESSION_INSTRUCTION_PATTERNS = [
    r"\bread[- ]only\b.*\b(no|zero)\b.*\b(src/|code|behavior|behaviour|commit|build)\b",
    r"\bno\s+`?src/`?\s+change\b",
    r"\bpush(ed)?\s+(to\s+)?origin\b",
    r"\bat\s+(the\s+)?session\s+start\b",
    r"\bread\s+(this|these|the following)\b.*\bbefore\b",
    r"\brun\s+the\s+(tests|suites|build)\b",
    r"\bboth\s+test\s+suites\s+must\s+pass\b",
    r"\bcommit\s+only\s+when\s+explicitly\s+asked\b",
    r"\bexit:\$\?\b",
    r"\bgtest_filter\b",
    r"^\s*```",
    r"\bdo\s+NOT\s+(ask|stop|proceed)\b",
    r"\bdispatch\b.*\b(task\s+\d|scope|hard stop)\b",
    r"\bstanding self-check\b",
]

REPORT_NARRATIVE_PATTERNS = [
    r"\b(delivered|verified|measured|reproduced|regenerated|re-ran|re-run)\b",
    r"\b\d+/\d+\b",
    r"\bbyte-identical\b",
    r"\b[0-9a-f]{8,10}\b",
    r"\bPASS\b|\bFAIL\b",
    r"\b\d+(\.\d+)?\s?%",
    r"\bcommit\b",
    r"\btests?\s+(pass|green)\b",
]


def norm(text: str) -> str:
    """Normalize for quote matching: drop markdown blockquote markers and collapse whitespace."""
    lines = [re.sub(r"^\s*>+\s?", "", ln) for ln in text.splitlines()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO,
                                       text=True).strip()
    except Exception:
        return "unknown"


# ── Establishment: every backbone quote must be findable at its cited home ────

def find_start_line(lines: list[str], needle: str, span: int) -> int | None:
    """First 1-based line at which `needle` (normalized) starts, or None."""
    # A window of span+4 lines starting anywhere at or before the true start still contains the
    # needle, so the FIRST match is up to 4 lines early. The LAST match is the true start.
    window = span + 4
    last = None
    for i in range(len(lines)):
        if not lines[i]:
            continue
        joined = re.sub(r"\s+", " ", " ".join(lines[i:i + window])).strip()
        if needle in joined:
            last = i + 1
    return last


def verify_backbone(backbone: dict) -> int:
    """Establishment (#19): every verbatim quote must exist at its cited home, AND the cited
    line number must be where it actually starts (DT-12 — a stale anchor is a defect type)."""
    misses, drifted, unanchored = [], [], []
    text_cache: dict[str, str] = {}
    line_cache: dict[str, list[str]] = {}
    for d in backbone["decisions"]:
        home = d["home"]
        parts = home.split(":")
        fname = parts[0]
        cited = None
        if len(parts) > 1:
            m = re.match(r"(\d+)", parts[1])
            if m:
                cited = int(m.group(1))
        path = REPO / fname
        if fname not in text_cache:
            if not path.exists():
                misses.append((d["id"], home, "home file does not exist"))
                text_cache[fname] = ""
                line_cache[fname] = []
                continue
            raw = path.read_text(encoding="utf-8", errors="replace")
            text_cache[fname] = norm(raw)
            line_cache[fname] = [re.sub(r"\s+", " ", re.sub(r"^\s*>+\s?", "", ln)).strip()
                                 for ln in raw.splitlines()]
        needle = norm(d["verbatim"])
        if not needle:
            misses.append((d["id"], home, "empty verbatim"))
            continue
        if needle not in text_cache[fname]:
            misses.append((d["id"], home, "verbatim NOT FOUND in the cited home"))
            continue
        if cited is None:
            unanchored.append((d["id"], home))
            continue
        found = find_start_line(line_cache[fname], needle, len(d["verbatim"].splitlines()))
        if found is None:
            misses.append((d["id"], home, "found in the file but not resolvable to a start line"))
        elif found != cited:
            drifted.append((d["id"], home, found))

    n = len(backbone["decisions"])
    print(f"backbone decisions: {n}")
    print(f"verbatim quotes found at their cited home: {n - len(misses)}/{n}")
    print(f"cited line numbers correct: {n - len(misses) - len(drifted) - len(unanchored)}"
          f"/{n - len(misses) - len(unanchored)}"
          f"   ({len(unanchored)} cited to a file with no line number, by design)")
    for mid, home, why in misses:
        print(f"  MISS {mid} ({home}): {why}")
    for mid, home, found in drifted:
        print(f"  LINE DRIFT {mid}: cited {home}, actually starts at line {found}")
    return 1 if (misses or drifted) else 0


# ── The disposition pass ─────────────────────────────────────────────────────

def build_matchers(backbone: dict):
    out = []
    for d in backbone["decisions"]:
        pats = [re.compile(p, re.IGNORECASE) for p in d.get("patterns", [])]
        out.append((d["id"], bool(d.get("home_is_layer_spec")), pats))
    return out


def disposition_pass(candidates, clusters, backbone):
    by_id = {c["id"]: c for c in candidates}
    matchers = build_matchers(backbone)
    sess = [re.compile(p, re.IGNORECASE | re.MULTILINE) for p in SESSION_INSTRUCTION_PATTERNS]
    rep = [re.compile(p, re.IGNORECASE) for p in REPORT_NARRATIVE_PATTERNS]

    rows = []
    rule_counts = {rid: 0 for rid, _ in RULES}
    disp_counts = {d: 0 for d in DISPOSITIONS}

    for cl in clusters:
        members = [by_id[m] for m in cl["member_ids"] if m in by_id]
        texts = []
        seen = set()
        for m in members:
            t = m["decision_text"]
            if t not in seen:
                seen.add(t)
                texts.append(t)
        joined = "\n".join(texts)
        kinds = {m["unit_kind"] for m in members}
        cats = {m["category"] for m in members}
        tiers = {m["tier"] for m in members}

        named, named_spec, named_nospec = [], [], []
        for did, is_spec, pats in matchers:
            if any(p.search(joined) for p in pats):
                named.append(did)
                (named_spec if is_spec else named_nospec).append(did)

        if cl.get("boilerplate_class"):
            rule, disp, decs = "BR-1", "boilerplate", []
        elif kinds and kinds <= HEADING_KINDS:
            rule, disp, decs = "BR-2", "not-a-decision", []
        elif named_spec:
            rule, disp, decs = "BR-3", "restates", named
        elif named_nospec:
            rule, disp, decs = "BR-4", "no-spec-home", named_nospec
        elif any(p.search(joined) for p in sess):
            rule, disp, decs = "BR-5", "not-a-decision", []
        elif cats == {"cc_reports"} and any(p.search(joined) for p in rep):
            rule, disp, decs = "BR-6", "not-a-decision", []
        elif kinds == {"table_row"} and tiers == {"broad"}:
            rule, disp, decs = "BR-7", "not-a-decision", []
        else:
            rule, disp, decs = "BR-8", "unresolved", []

        rule_counts[rule] += 1
        disp_counts[disp] += 1
        rows.append({
            "cluster_id": cl["cluster_id"],
            "size": cl["size"],
            "disposition": disp,
            "rule": rule,
            "decisions": decs,
            "categories": sorted(cats),
            "unit_kinds": sorted(kinds),
            "files": cl["files"][:5] if cl.get("files") else sorted({
                o["file"] for m in members for o in m["source_occurrences"]})[:5],
        })

    return rows, rule_counts, disp_counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="establishment pass: every backbone verbatim quote must be found "
                         "at its cited home")
    ap.add_argument("--check", action="store_true",
                    help="re-read the emitted artifacts and prove the coverage guarantee")
    args = ap.parse_args()

    backbone = json.loads(BACKBONE.read_text(encoding="utf-8"))

    if args.verify:
        return verify_backbone(backbone)

    if args.check:
        data = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        clusters = json.loads(CLUSTERS.read_text(encoding="utf-8"))["clusters"]
        rows = data["dispositions"]
        ids_in = {c["cluster_id"] for c in clusters}
        ids_out = [r["cluster_id"] for r in rows]
        ok = True
        if len(ids_out) != len(set(ids_out)):
            print("FAIL: a cluster carries more than one disposition")
            ok = False
        if set(ids_out) != ids_in:
            print(f"FAIL: coverage — {len(ids_in - set(ids_out))} cluster(s) carry no disposition")
            ok = False
        bad = [r["cluster_id"] for r in rows if r["disposition"] not in DISPOSITIONS]
        if bad:
            print(f"FAIL: {len(bad)} disposition(s) outside the permitted vocabulary")
            ok = False
        print(f"clusters in:  {len(ids_in)}")
        print(f"dispositioned: {len(set(ids_out))}")
        print("OVERALL " + ("PASS" if ok else "FAIL"))
        return 0 if ok else 1

    cand = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    clus = json.loads(CLUSTERS.read_text(encoding="utf-8"))
    candidates = cand["candidates"]
    clusters = clus["clusters"]

    rows, rule_counts, disp_counts = disposition_pass(candidates, clusters, backbone)

    covered_occurrences = sum(r["size"] for r in rows)

    header = {
        "instrument": "tools/audit/decisions/gen_cluster_dispositions.py",
        "purpose": "OI-207 adjudication Task 3 — one recorded disposition per harvested cluster, "
                   "by numbered bulk rule. NO cluster is left without one.",
        "inputs": {
            "candidates": {"file": str(CANDIDATES.relative_to(REPO)).replace("\\", "/"),
                           "sha256": sha256_of(CANDIDATES),
                           "total_candidates": len(candidates)},
            "clusters": {"file": str(CLUSTERS.relative_to(REPO)).replace("\\", "/"),
                         "sha256": sha256_of(CLUSTERS),
                         "cluster_count": len(clusters)},
            "backbone": {"file": str(BACKBONE.relative_to(REPO)).replace("\\", "/"),
                         "sha256": sha256_of(BACKBONE),
                         "decision_count": len(backbone["decisions"])},
        },
        "head_commit": head_commit(),
        "disposition_vocabulary": list(DISPOSITIONS),
        "rules": [{"id": rid, "rule": text, "clusters": rule_counts[rid]} for rid, text in RULES],
        "disposition_counts": disp_counts,
        "completeness_check": {
            "clusters": len(clusters),
            "dispositioned": len(rows),
            "occurrences_covered": covered_occurrences,
            "occurrences_total": len(candidates),
            "complete": len(rows) == len(clusters) and covered_occurrences == len(candidates),
        },
    }

    OUT_JSON.write_text(json.dumps({"header": header, "dispositions": rows},
                                   indent=1, ensure_ascii=False), encoding="utf-8")
    OUT_MANIFEST.write_text(json.dumps(header, indent=1, ensure_ascii=False), encoding="utf-8")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["cluster_id", "size", "disposition", "rule", "decisions",
                    "categories", "unit_kinds", "files"])
        for r in rows:
            w.writerow([r["cluster_id"], r["size"], r["disposition"], r["rule"],
                        ";".join(r["decisions"]), ";".join(r["categories"]),
                        ";".join(r["unit_kinds"]), ";".join(r["files"])])

    print(f"clusters dispositioned: {len(rows)}/{len(clusters)}")
    print(f"occurrences covered:    {covered_occurrences}/{len(candidates)}")
    for rid, text in RULES:
        print(f"  {rid}: {rule_counts[rid]:>6}   {text[:72]}")
    print("dispositions: " + ", ".join(f"{k}={v}" for k, v in disp_counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
