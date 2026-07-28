#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_decision_harvest.py — THE DECISION HARVEST (dispatch cc_instruction_decision_harvest.md).
#
# MECHANICAL, READ-ONLY, NO ADJUDICATION. Extract every decision-BEARING statement
# in the repository into ONE candidate list, so the later OI-207 adjudication pass
# spends its capacity on judging rather than on searching ~13 MB of prose. This
# instrument DOES NOT decide whether a candidate is really a decision, DOES NOT
# check any candidate against the code, and DOES NOT fill status or conformance —
# those are left EMPTY for the adjudication pass (OI-207/OI-208).
#
# Over-capture is intended (the adjudication discards; under-capture is the only
# real failure mode). Recall is ESTABLISHED separately by the seed-recall check
# (--seed-recall; Task 3, #19) against 10 known decisions.
#
# What it does:
#   * enumerates a fixed, deterministic corpus (governing docs, cowork_* design
#     docs, docs/, the register, cc_* reports, both archives, ARCHITECTURE.md,
#     AND production code COMMENT text — never code semantics);
#   * splits each Markdown file into UNITS (heading / bullet / table row /
#     paragraph / block-quote) and each source file into COMMENT BLOCKS;
#   * matches a wide signature set (case-insensitive) against each unit's text;
#   * for every unit with >=1 signature emits ONE candidate, carrying the text
#     VERBATIM plus enough context to stand alone, in the field shape a decisions
#     register consumes (Task 2), with status + conformance left empty;
#   * groups identical statements into dedup groups WITHOUT dropping any
#     occurrence (repetition is evidence of standing);
#   * emits decision_candidates.json (full), decision_candidates.csv (for reading),
#     and manifest.json (corpus git hash + instrument blob sha + counts, DERIVED).
#
# Determinism: no wall-clock, no randomness; fixed corpus order; stable sort;
# sequential IDs over the pinned corpus (stamped by git hash in the manifest, #16).

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # tools/audit/decisions -> repo root
OUTDIR = HERE  # tools/audit/decisions/

# ── The signature set ─────────────────────────────────────────────────────────
# Each entry: (name, regex-source, tier). tier "high" = strongly decision-bearing
# vocabulary (a ratification / shelving / falsification / exclusion / standing
# rule); tier "broad" = the wider net the dispatch mandates (often narrative but
# can bind). NO candidate is dropped by tier — the tier is an ENRICHMENT so the
# adjudication pass and the readable inventory can prioritize, never a filter.
# The dispatch's named signatures are all present; additions are marked (+).
SIGNATURES = [
    # ---- high-binding ----
    ("ratified",            r"ratif(?:ied|ication|y|ies)",              "high"),
    ("user-ratified",       r"user[- ]ratified",                        "high"),
    ("user-directed",       r"user[- ]direct(?:ed|ion|s)",             "high"),  # (+)
    ("ruled/ruling",        r"\brul(?:ed|ing|es)\b",                    "high"),
    ("adjudicated",         r"adjudicat(?:ed|ion|e)",                   "high"),
    ("shelved",             r"shelv(?:ed|ing|e)",                       "high"),
    ("falsified",           r"falsif(?:ied|y|ies|ication)",             "high"),
    ("refuted",             r"refut(?:ed|e|es|ation)",                  "high"),
    ("rejected",            r"reject(?:ed|s|ion)?",                     "high"),
    ("excluded",            r"exclud(?:ed|es|e)|exclusion",             "high"),
    ("dead end",            r"dead[- ]end",                             "high"),
    ("superseded",          r"supersed(?:ed|es|e|ing)",                 "high"),
    ("retired",             r"retir(?:ed|es|e|ement|ing)",              "high"),
    ("forbidden",           r"forbid(?:den|s)?",                        "high"),
    ("deprecated",          r"deprecat(?:ed|es|e|ion)",                 "high"),  # (+)
    ("constrained optimum", r"constrained optimum",                     "high"),
    ("replaced by",         r"replaced by",                             "high"),
    ("in favor of",         r"in favou?r of",                           "high"),
    ("the rule is",         r"the rule is|standing rule|standing (?:decision|requirement|instruction)",  "high"),
    ("must not",            r"must not|must never",                     "high"),
    ("do not (revert/…)",   r"do not\b",                                "high"),
    ("no longer",           r"no longer",                               "high"),
    ("not to be",           r"not to be\b",                             "high"),
    ("overturned",          r"overturn(?:ed|s)?",                       "high"),  # (+)
    ("withdrawn",           r"withdraw(?:n|s)?|withdrew",               "high"),  # (+)
    ("sanctioned",          r"sanction(?:ed|s)?",                       "high"),  # (+)
    ("corollary",           r"corollar(?:y|ies)",                       "high"),  # (+)
    ("premise",             r"premise",                                 "high"),
    ("STOP (#13)",          r"\bSTOP\b",                                "high"),  # (+) surprise-stop idiom
    ("do-not-merge/revert", r"do not (?:revert|restore|merge|let)",     "high"),  # (+)
    # ---- broad net ----
    ("decided/decision",    r"decid(?:ed|es|e)|decision",              "broad"),
    ("deferred",            r"deferr?(?:ed|s|al)?|\bdefer\b",           "broad"),
    ("held/parked",         r"\bparked?\b|\bshelve\b|\bheld\b(?! out)", "broad"),
    ("never",               r"\bnever\b",                               "broad"),
    ("we will/will not",    r"\bwe will\b|\bwill not\b|\bwon't\b",     "broad"),
    ("chosen/choice",       r"\bchosen\b|\bwe chose\b|the choice is",   "broad"),
    ("answered",            r"\banswered\b|the answer is",              "broad"),  # (+)
    ("carried over",        r"carried[- ]over|carries over|carry-over", "broad"),  # (+)
    ("delegated",           r"delegat(?:ed|es|e)",                      "broad"),  # (+)
    ("pre-ratified",        r"pre-ratif|ratification-gated",            "broad"),  # (+)
    ("verdict",             r"\bverdict\b",                             "broad"),  # (+)
]
COMPILED = [(n, re.compile(rx, re.IGNORECASE), t) for (n, rx, t) in SIGNATURES]

# ── Corpus enumeration (deterministic) ────────────────────────────────────────
GOVERNING = [
    "CLAUDE.md", "ARCHITECTURE.md", "STATUS.md", "STATUS_ARCHIVE.md",
    "cowork_handoff.md", "cowork_handoff_archive.md", "OPEN_ITEMS.md",
    "DEFECT_TYPES.md",
]


def _git(args):
    return subprocess.run(["git", "-C", REPO] + args, capture_output=True, text=True)


def head_commit():
    r = _git(["rev-parse", "HEAD"])
    return r.stdout.strip()


def tracked_set():
    """The git-tracked (committed + staged) file set, forward-slashed. NOT used to
    filter the corpus — the dispatch's directive is that under-capture is the only
    real failure mode, and many `cc_*` reports carrying rulings 'recorded nowhere
    else' are untracked working notes. Instead the harvest scans EVERYTHING and
    DISCLOSES which scanned files are untracked (manifest.reproducibility), so the
    #16 reproducibility bound is honest rather than silently over- or under-scoped:
    the corpus hash captures only tracked content, so a regeneration is exact only
    if the same untracked working-tree files are present."""
    r = _git(["ls-files"])
    return set(l.replace("\\", "/") for l in r.stdout.splitlines() if l.strip())


def enumerate_corpus():
    """Return an ordered list of (category, relpath). Category order fixes the
    candidate-ID assignment order; within a category the paths are sorted."""
    cats = []  # (rank, category, [relpaths])

    def md_glob(prefix_dir, pat, exclude=()):
        import glob
        out = []
        for p in glob.glob(os.path.join(REPO, prefix_dir, pat)):
            rel = os.path.relpath(p, REPO).replace("\\", "/")
            if rel in exclude:
                continue
            out.append(rel)
        return sorted(out)

    # 1 governing
    gov = [f for f in GOVERNING if os.path.exists(os.path.join(REPO, f))]
    cats.append((1, "governing", gov))

    # 2 cowork_* design docs (root), minus the two handoff files already in gov
    cowork = md_glob("", "cowork_*.md",
                     exclude=("cowork_handoff.md", "cowork_handoff_archive.md"))
    cats.append((2, "cowork_docs", cowork))

    # 3 docs/
    docs = md_glob("docs", "*.md")
    cats.append((3, "docs", docs))

    # 4 open_items/
    oi = md_glob("open_items", "*.md")
    cats.append((4, "open_items", oi))

    # 5 cc_* reports (root) — every cc_*.md (238 are *_report.md; the rest are
    #   dispatches/notes that also carry rulings). Over-capture is free.
    cc = md_glob("", "cc_*.md")
    cats.append((5, "cc_reports", cc))

    # 6 production code COMMENT text: src/composing, src/notation (C++), tools/**.py
    code = []
    for base in ("src/composing", "src/notation"):
        for root, _dirs, files in os.walk(os.path.join(REPO, base)):
            for fn in files:
                if fn.endswith((".cpp", ".h", ".hpp", ".cc")):
                    code.append(os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/"))
    for root, _dirs, files in os.walk(os.path.join(REPO, "tools")):
        # exclude THIS instrument's own dir (self-match) and pycache
        rr = os.path.relpath(root, REPO).replace("\\", "/")
        if rr.startswith("tools/audit/decisions") or "__pycache__" in rr:
            continue
        for fn in files:
            if fn.endswith(".py"):
                code.append(os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/"))
    cats.append((6, "code_comments", sorted(set(code))))

    ordered = []
    for _rank, cat, paths in sorted(cats):
        for p in paths:
            ordered.append((cat, p))   # scan everything; untracked disclosed in manifest (#16)
    return ordered


# ── Markdown unit splitter ────────────────────────────────────────────────────
_H = re.compile(r"^\s{0,3}#{1,6}\s")
_LIST = re.compile(r"^(\s*)(?:[-*+]\s|\d+[.)]\s)")


def _classify(line):
    s = line.strip()
    if s == "":
        return "blank"
    if _H.match(line):
        return "heading"
    if s.startswith("|"):
        return "table"
    if s.startswith(">"):
        return "quote"
    if _LIST.match(line):
        return "listitem"
    return "text"


def split_markdown_units(lines):
    """Yield (start_line, end_line, kind, text) 1-indexed. A unit is the enclosing
    bullet / table row / heading / block-quote / paragraph — the granularity the
    dispatch names ('the enclosing bullet/paragraph')."""
    units = []
    i = 0
    n = len(lines)
    while i < n:
        cls = _classify(lines[i])
        start = i
        if cls == "blank":
            i += 1
            continue
        if cls == "heading":
            units.append((start + 1, start + 1, "heading", lines[i]))
            i += 1
            continue
        if cls == "table":
            units.append((start + 1, start + 1, "table_row", lines[i]))
            i += 1
            continue
        if cls == "quote":
            j = i + 1
            while j < n and _classify(lines[j]) == "quote":
                j += 1
            units.append((start + 1, j, "blockquote", "\n".join(lines[i:j])))
            i = j
            continue
        if cls == "listitem":
            # consume wrapped continuation ('text' lines) up to next structural line/blank
            j = i + 1
            while j < n:
                cj = _classify(lines[j])
                if cj in ("blank", "listitem", "heading", "table", "quote"):
                    break
                j += 1
            units.append((start + 1, j, "bullet", "\n".join(lines[i:j])))
            i = j
            continue
        # paragraph: consecutive 'text' lines
        j = i + 1
        while j < n and _classify(lines[j]) == "text":
            j += 1
        units.append((start + 1, j, "paragraph", "\n".join(lines[i:j])))
        i = j
    return units


# ── Code comment extractor ────────────────────────────────────────────────────
def split_code_comment_units(relpath, lines):
    """Yield (start_line, end_line, kind, text) for COMMENT text only. C++: runs
    of //-lines grouped; /* */ blocks. Python: runs of #-lines; ''' / \"\"\"
    docstrings. Code semantics are never matched — only the comment/docstring text."""
    units = []
    is_py = relpath.endswith(".py")
    n = len(lines)
    i = 0
    in_block = False
    block_start = 0
    block_buf = []
    block_delim = None  # '*/' for C, or the triple-quote for py

    def flush_line_run(run_start, run_lines):
        if run_lines:
            units.append((run_start + 1, run_start + len(run_lines),
                          "code_comment", "\n".join(run_lines)))

    if is_py:
        # docstrings + # comments. Simple triple-quote state machine + #-runs.
        run_start = None
        run_lines = []
        while i < n:
            ln = lines[i]
            if in_block:
                block_buf.append(ln)
                if block_delim in ln:
                    units.append((block_start + 1, i + 1, "docstring", "\n".join(block_buf)))
                    in_block = False
                    block_buf = []
                i += 1
                continue
            stripped = ln.strip()
            # start of a docstring line (heuristic: line begins with a triple quote)
            m = re.match(r'[rbuRBU]?("""|\'\'\')', stripped)
            if m:
                delim = m.group(1)
                # single-line docstring?
                rest = stripped[m.end():]
                if delim in rest:
                    units.append((i + 1, i + 1, "docstring", ln))
                else:
                    in_block = True
                    block_start = i
                    block_delim = delim
                    block_buf = [ln]
                # end any # run
                flush_line_run(run_start, run_lines) if run_lines else None
                run_lines = []
                run_start = None
                i += 1
                continue
            # # comment (whole-line or trailing)
            hash_idx = ln.find("#")
            if hash_idx != -1 and "#" in ln:
                # crude: ignore # inside an obvious string on the same line is
                # acceptable over-capture; take text after the first #.
                ctext = ln[hash_idx:]
                if run_start is None:
                    run_start = i
                run_lines.append(ctext)
                i += 1
                continue
            # non-comment line ends a # run
            if run_lines:
                flush_line_run(run_start, run_lines)
                run_lines = []
                run_start = None
            i += 1
        if run_lines:
            flush_line_run(run_start, run_lines)
        return units

    # C/C++
    run_start = None
    run_lines = []
    while i < n:
        ln = lines[i]
        if in_block:
            block_buf.append(ln)
            if "*/" in ln:
                units.append((block_start + 1, i + 1, "block_comment", "\n".join(block_buf)))
                in_block = False
                block_buf = []
            i += 1
            continue
        # block comment start (that does not close on the same line)
        bidx = ln.find("/*")
        lidx = ln.find("//")
        # Prefer whichever comes first
        if bidx != -1 and (lidx == -1 or bidx < lidx):
            if "*/" in ln[bidx + 2:]:
                units.append((i + 1, i + 1, "block_comment", ln[bidx:]))
            else:
                in_block = True
                block_start = i
                block_buf = [ln[bidx:]]
            if run_lines:
                flush_line_run(run_start, run_lines)
                run_lines = []
                run_start = None
            i += 1
            continue
        if lidx != -1:
            ctext = ln[lidx:]
            if run_start is None:
                run_start = i
            run_lines.append(ctext)
            i += 1
            continue
        # non-comment line ends a // run
        if run_lines:
            flush_line_run(run_start, run_lines)
            run_lines = []
            run_start = None
        i += 1
    if run_lines:
        flush_line_run(run_start, run_lines)
    return units


# ── Metadata extractors ───────────────────────────────────────────────────────
_DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
_HASH = re.compile(r"\b([0-9a-f]{7,40})\b")
_OIREF = re.compile(r"\bOI-\d+\b")
_FILEREF = re.compile(r"\b[\w./-]+\.(?:md|json|py|cpp|h|txt|musicxml|csv)\b")
_TOOLPATH = re.compile(r"\btools/[\w./-]+")


def _looks_like_hash(tok):
    return bool(re.search(r"[0-9]", tok)) and bool(re.search(r"[a-f]", tok)) and not tok.isdigit()


def extract_meta(text, ctx):
    blob = text + "\n" + ctx
    dates = sorted(set(_DATE.findall(blob)))
    # ratifier
    who = []
    low = blob.lower()
    if re.search(r"user[- ]ratif|ratified by the user|the user'?s? rul|user[- ]direct|\(user[,)]|user ruled|user'?s? ruling|by the user", low):
        who.append("user")
    if re.search(r"cowork[- ]ratif|ratified by cowork|\(cowork", low):
        who.append("cowork")
    if re.search(r"\bcc[- ]ratif|ratified by cc\b", low):
        who.append("cc")
    who = sorted(set(who))
    # evidence pointers
    ev = []
    ev += [h for h in _HASH.findall(blob) if _looks_like_hash(h)]
    ev += _OIREF.findall(blob)
    ev += _FILEREF.findall(blob)
    ev += _TOOLPATH.findall(blob)
    # dedup preserving order, cap
    seen = set()
    ev_out = []
    for e in ev:
        if e not in seen:
            seen.add(e)
            ev_out.append(e)
    return dates, who, ev_out[:24]


def normalize(text):
    t = text.lower()
    t = re.sub(r"[`*_#>|]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


# ── Harvest ───────────────────────────────────────────────────────────────────
def read_lines(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read().split("\n")


def harvest():
    corpus = enumerate_corpus()
    raw = []  # pre-ID candidate dicts
    per_file_counts = {}
    for cat, rel in corpus:
        lines = read_lines(rel)
        if cat == "code_comments":
            units = split_code_comment_units(rel, lines)
        else:
            units = split_markdown_units(lines)
        fcount = 0
        for (s, e, kind, text) in units:
            hits = []
            tiers = set()
            for (name, rx, tier) in COMPILED:
                if rx.search(text):
                    hits.append(name)
                    tiers.add(tier)
            if not hits:
                continue
            # context: 2 lines either side of the unit
            cb = "\n".join(lines[max(0, s - 1 - 2):s - 1]).strip()
            ce = "\n".join(lines[e:min(len(lines), e + 2)]).strip()
            dates, who, ev = extract_meta(text, cb + "\n" + ce)
            raw.append({
                "category": cat,
                "file": rel,
                "start_line": s,
                "end_line": e,
                "unit_kind": kind,
                "matched_signatures": hits,
                "tier": "high" if "high" in tiers else "broad",
                "text": text,
                "context_before": cb,
                "context_after": ce,
                "date": dates[0] if dates else "",
                "dates_all": dates,
                "ratified_by": who,
                "evidence_pointer": ev,
                "norm": normalize(text),
            })
            fcount += 1
        if fcount:
            per_file_counts[rel] = fcount

    # stable sort → sequential IDs (deterministic over the pinned corpus)
    cat_rank = {"governing": 1, "cowork_docs": 2, "docs": 3, "open_items": 4,
                "cc_reports": 5, "code_comments": 6}
    raw.sort(key=lambda c: (cat_rank[c["category"]], c["file"], c["start_line"]))
    for idx, c in enumerate(raw, 1):
        c["id"] = "DH-%05d" % idx
        c["fingerprint"] = hashlib.sha1(
            ("%s:%d:%s" % (c["file"], c["start_line"], c["norm"])).encode("utf-8")
        ).hexdigest()[:12]

    # dedup grouping (LINK, never DROP)
    groups = {}
    for c in raw:
        groups.setdefault(c["norm"], []).append(c)
    for norm, members in groups.items():
        key = hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]
        locs = [{"id": m["id"], "file": m["file"], "line": m["start_line"]} for m in members]
        for m in members:
            m["dedup_key"] = key
            m["dedup_group_size"] = len(members)
            m["linked_occurrences"] = [l for l in locs if l["id"] != m["id"]]

    return raw, per_file_counts, corpus


def to_register_record(c):
    """Task 2: the field shape a decisions index consumes. status + conformance
    are LEFT EMPTY for the adjudication pass (OI-207/OI-208)."""
    occ = [{"file": c["file"], "line": c["start_line"]}] + c["linked_occurrences"]
    return {
        "id": c["id"],
        "decision_text": c["text"],            # the author's own words, verbatim
        "date": c["date"],
        "ratified_by": c["ratified_by"],
        "status": "",                           # EMPTY — adjudication fills
        "conformance": "",                      # EMPTY — adjudication fills
        "evidence_pointer": c["evidence_pointer"],
        "source_occurrences": occ,
        # harvest provenance (kept beside the register fields):
        "category": c["category"],
        "unit_kind": c["unit_kind"],
        "tier": c["tier"],
        "matched_signatures": c["matched_signatures"],
        "context_before": c["context_before"],
        "context_after": c["context_after"],
        "dedup_key": c["dedup_key"],
        "dedup_group_size": c["dedup_group_size"],
        "fingerprint": c["fingerprint"],
    }


def write_outputs(raw, per_file_counts, corpus):
    records = [to_register_record(c) for c in raw]

    # reproducibility disclosure (#16): which scanned files are NOT git-tracked, so a
    # re-runner knows the corpus hash alone does not pin them.
    TRACKED = tracked_set()
    untracked = sorted(p for (_cat, p) in corpus if p not in TRACKED)

    # counts
    by_cat = {}
    by_tier = {"high": 0, "broad": 0}
    by_sig = {}
    for c in raw:
        by_cat[c["category"]] = by_cat.get(c["category"], 0) + 1
        by_tier[c["tier"]] += 1
        for s in c["matched_signatures"]:
            by_sig[s] = by_sig.get(s, 0) + 1
    n_groups = len(set(c["dedup_key"] for c in raw))

    header = {
        "instrument": "tools/audit/decisions/gen_decision_harvest.py",
        "purpose": "OI-207/OI-208 decision harvest — mechanical candidate list, "
                   "status+conformance EMPTY for the adjudication pass",
        "head_commit": head_commit(),
        "total_candidates": len(raw),
        "distinct_statements": n_groups,
        "by_category": by_cat,
        "by_tier": by_tier,
    }

    # full JSON
    with open(os.path.join(OUTDIR, "decision_candidates.json"), "w", encoding="utf-8") as fh:
        json.dump({"header": header, "candidates": records}, fh, indent=1, sort_keys=False)

    # CSV for reading
    with open(os.path.join(OUTDIR, "decision_candidates.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "category", "file", "line", "unit_kind", "tier",
                    "matched_signatures", "date", "ratified_by", "evidence_pointer",
                    "dedup_group_size", "status", "conformance", "decision_text"])
        for c in raw:
            w.writerow([
                c["id"], c["category"], c["file"], c["start_line"], c["unit_kind"],
                c["tier"], ";".join(c["matched_signatures"]), c["date"],
                ";".join(c["ratified_by"]), ";".join(c["evidence_pointer"][:8]),
                c["dedup_group_size"], "", "",
                c["text"].replace("\r", " "),
            ])

    # manifest (DERIVED, #17f)
    blob = hashlib.sha1(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    manifest = {
        "instrument": "tools/audit/decisions/gen_decision_harvest.py",
        "instrument_blob_sha": blob,
        "audit": "OI-207 decision-conformance audit — the decision harvest (input for OI-208)",
        "head_commit": head_commit(),
        "corpus_hash": head_commit()[:10],
        "scope": {
            "governing": GOVERNING,
            "cowork_docs": "cowork_*.md (root)",
            "docs": "docs/*.md",
            "open_items": "open_items/*.md",
            "cc_reports": "cc_*.md (root)",
            "code_comments": "src/composing/**, src/notation/** (C++ //,/* */); "
                             "tools/**/*.py (#, docstrings) — COMMENT TEXT ONLY",
        },
        "corpus_file_count": len(corpus),
        "signatures": [{"name": n, "tier": t, "regex": rx} for (n, rx, t) in SIGNATURES],
        "context_rule": "unit = enclosing Markdown block (heading / bullet / table "
                        "row / block-quote / paragraph) or code COMMENT block; plus "
                        "2 lines of context either side; one candidate per unit, all "
                        "its matched signatures listed.",
        "dedup_rule": "identical normalized text is LINKED (dedup_key, "
                      "linked_occurrences), NEVER dropped.",
        "totals": {
            "total_candidates": len(raw),
            "distinct_statements": n_groups,
            "by_category": by_cat,
            "by_tier": by_tier,
        },
        "candidates_per_file": dict(sorted(per_file_counts.items(),
                                           key=lambda kv: (-kv[1], kv[0]))),
        "signature_hit_counts": dict(sorted(by_sig.items(), key=lambda kv: (-kv[1], kv[0]))),
        "outputs": ["decision_candidates.json", "decision_candidates.csv",
                    "decision_inventory.md (hand-curated readable face)"],
        "reproducibility": {
            "corpus_hash_covers": "git-tracked content only (the HEAD commit)",
            "untracked_files_scanned_count": len(untracked),
            "untracked_files_scanned": untracked,
            "note": "The harvest scans EVERYTHING in scope (over-capture is free; many "
                    "cc_* reports carrying rulings are untracked working notes, and "
                    "under-capture is the only real failure mode). Therefore a "
                    "regeneration reproduces this candidate list exactly only if the "
                    "same untracked working-tree files are present. The corpus_hash "
                    "pins the tracked portion; the untracked list above pins the rest.",
        },
        "NOTE": "status and conformance are EMPTY by design — this pass does NOT "
                "adjudicate. Recall established by --seed-recall (#19).",
    }
    with open(os.path.join(OUTDIR, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=False)

    return header, by_sig


# ── Seed recall (Task 3, #19) ─────────────────────────────────────────────────
# 10 decisions we already KNOW exist. For each: the decision's PRIMARY-STATEMENT
# home file(s) and distinctive locating substrings of the primary statement (not
# a mere summary reference). A rigorous establishment reports BOTH caught-anywhere
# (does the net surface it at all) AND caught-at-home (is the authoritative
# statement itself harvested, so the adjudication pass reaches the source). A miss
# means the signature list is wrong — cheaper to learn now than at adjudication.
SEEDS = [
    ("1 Stage-3.1b shelving of whole-score interactive analysis",
     ["src/notation/internal/notationcomposingbridge.cpp", "docs/p3_granularity_ab_3_1b.md"],
     ["whole-score decode was SHELVED", "Q1 RE-DECIDED", "was shelved"]),
    ("2 joint-native record ruling (Decision A2)",
     ["cowork_notation_output_contract.md"],
     ["Decision A2", "one output surface the notation path reads"]),
    ("3 two-mode key ruling + published un-rounded modal reading (C1)",
     ["cowork_notation_output_contract.md"],
     ["un-rounded modal reading", "un-rounded publication of modal"]),
    ("4 embedded-tables ruling (Decision D1)",
     ["cowork_notation_output_contract.md"],
     ["per Decision D1", "Decision D1"]),
    ("5 pedal-point ruling + voice-independence sharpening",
     ["cowork_notation_adoption_increment.md"],
     ["pedal-point ruling", "voice-independence sharpening", "voice-independent pedal"]),
    ("6 decision-neutrality corollary (CLAUDE.md)",
     ["CLAUDE.md"],
     ["Decision-neutrality of the existing implementation", "decision-neutrality corollary"]),
    ("7 full-candidate-list amendment to the output contract",
     ["cowork_notation_output_contract.md"],
     ["FULL scoreable candidate lists", "publish the FULL", "candidate lists"]),
    ("8 never-merge-upstream distribution constraint (CLAUDE.md)",
     ["CLAUDE.md"],
     ["FORK-LOCAL ONLY", "NEVER merge upstream", "NEVER be pushed or merged"]),
    ("9 ratified robust-unit regression stop",
     ["CLAUDE.md"],
     ["THE ROBUST-UNIT REGRESSION STOP", "granularity-robust union-of-boundaries"]),
    ("10 ordering rule: retirement map precedes the reviews",
     ["open_items/OI-205.md", "OPEN_ITEMS.md"],
     ["AFTER the OI-180 retirement map", "post-map, pre-review", "BEFORE the OI-198"]),
]


def _blob(c):
    return (c["text"] + "\n" + c["context_before"] + "\n" + c["context_after"]).lower()


def seed_recall(raw):
    results = []
    for (name, home_files, needles) in SEEDS:
        hits = []          # every candidate that matches a needle (anywhere)
        home_hits = []     # matches whose file is a declared home file
        for c in raw:
            blob = _blob(c)
            nd_hit = next((nd for nd in needles if nd.lower() in blob), None)
            if not nd_hit:
                continue
            loc = {"id": c["id"], "file": c["file"], "line": c["start_line"], "needle": nd_hit}
            hits.append(loc)
            if home_files and c["file"] in home_files:
                home_hits.append(loc)
        results.append({
            "seed": name,
            "caught_anywhere": bool(hits),
            "caught_at_home": bool(home_hits),
            "n_hits": len(hits),
            "home_files": home_files,
            "home_hit": home_hits[0] if home_hits else None,
            "sample_hit": hits[0] if hits else None,
        })
    return results


def main():
    ap = argparse.ArgumentParser(description="Decision harvest (OI-207/OI-208): mechanical candidate list.")
    ap.add_argument("--seed-recall", action="store_true",
                    help="also run the 10-seed recall establishment (Task 3, #19)")
    args = ap.parse_args()

    raw, per_file_counts, corpus = harvest()
    if not raw:
        sys.stderr.write("FATAL: harvest produced ZERO candidates — signatures/scan broke.\n")
        sys.exit(2)
    header, by_sig = write_outputs(raw, per_file_counts, corpus)

    print("decision harvest complete.")
    print("  corpus files scanned : %d" % len(corpus))
    print("  total candidates     : %d" % header["total_candidates"])
    print("  distinct statements  : %d" % header["distinct_statements"])
    print("  by category          : %s" % json.dumps(header["by_category"]))
    print("  by tier              : %s" % json.dumps(header["by_tier"]))

    if args.seed_recall:
        res = seed_recall(raw)
        n_any = sum(1 for r in res if r["caught_anywhere"])
        n_home = sum(1 for r in res if r["caught_at_home"])
        print("\nseed recall: %d/%d caught-anywhere ; %d/%d caught-at-home" %
              (n_any, len(res), n_home, len(res)))
        for r in res:
            mark = "OK  " if r["caught_at_home"] else ("ANY " if r["caught_anywhere"] else "MISS")
            print("  [%s] %s  (hits=%d)" % (mark, r["seed"], r["n_hits"]))
            if r["home_hit"]:
                print("        home @ %s:%d (%s) [needle: %s]" %
                      (r["home_hit"]["file"], r["home_hit"]["line"],
                       r["home_hit"]["id"], r["home_hit"]["needle"]))
            elif r["sample_hit"]:
                print("        anywhere @ %s:%d (%s) [needle: %s]" %
                      (r["sample_hit"]["file"], r["sample_hit"]["line"],
                       r["sample_hit"]["id"], r["sample_hit"]["needle"]))
        with open(os.path.join(OUTDIR, "seed_recall.json"), "w", encoding="utf-8") as fh:
            json.dump({"head_commit": head_commit(), "caught_anywhere": n_any,
                       "caught_at_home": n_home, "total": len(res), "results": res},
                      fh, indent=1)


if __name__ == "__main__":
    main()
