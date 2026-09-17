#!/usr/bin/env python3
"""CHECK THE ROOT-RECORD REFERENCE MAP REPORT'S LONG LISTINGS AGAINST THE REPOSITORY.

WHY THIS EXISTS.  The reference map of the root record files (written 2026-09-16, under
`records/cc/reports/`) is 11,423 lines long, and the move dispatch will be written from it.  Its
prose and judgement sections are read by the writing side.  Its long listings are checked here,
mechanically, by a tool whose output can be re-run (dispatch
`records/cc/instructions/cc_instruction_reference_map_check_2026_09_17.md`).

HOW THE REPORT IS READ.  From its git BLOB, by the identity given as the first argument
(`git cat-file blob <identity>`), never from the working tree.  The second argument is the report's
working-tree path, and it is used for ONE thing only: its modification time, which every
difference below is compared against.  Nothing else is taken from that path.

WHAT IS CHECKED -- five things, each against the working tree as it stands when this runs:
  1. Section 2(b).5, the hit lines: every `path:line:content` line equals the named file's line;
     and an independent walk with the same regular expression over the same file types, whose
     difference with the listed hits is published in BOTH directions.
  2. Sections 2(b).1 and 2(b).2, the deciding lines: every quoted item of the form
     "NNN: `code`" or "NNN-MMM: `code`" occurs at that line, or inside that range, of the file
     its entry names.  "..." and the ellipsis character inside a quote match any text.
  3. Task 2(a), the counts: every listed file's figure is recomputed twice -- as matching lines
     and as individual matches -- and which of the two it equals (or neither) is published; plus
     the files the walk finds with a match that are not listed, and the reverse.
  4. Task 1, the root lists and their T/U marks: each list is recomputed from a listing of the
     repository root alone, and each mark from `git ls-files` (at most forty literal names per call).
  5. Section 2(c), coverage: every file whose text matches the coverage expression is classified
     exactly once in 2(c), or falls in the population 2(c).1 covers in one statement; files
     classified twice, files not classified, and classified files that no longer match are published.
  For every difference in checks 1, 3, 4 and 5, whether the file's modification time is later than
  the report's is published.  Whether a difference is a defect of the report is NOT decided here.

WHAT IS NOT CHECKED.  Whether any verdict (i)-(iv) of 2(b), or any class of 2(c), is right.  Those
are judgements, and the writing side reads them.  Nor the report's prose, its method section, its
tables' non-quoted columns, or 2(b).3 and 2(b).4.

A LINE THIS TOOL CANNOT PARSE IS PUBLISHED AS UNCHECKED, WITH ITS REASON -- NEVER SKIPPED.

THE WALK, AND WHAT BOUNDS IT.
  * Excluded at any depth, never entered, listed or read: directories named `polyph9-release`,
    `scratch_artifacts`, `external resarch summary`, `Claude outputs`, `Codex research inventory`,
    `.git`.  (The dispatch names them at their locations; excluding the names at any depth is a
    superset of that, and is also how the report's own searches excluded them.)
  * Hidden entries -- a name beginning with a dot -- are not walked, because the report's searches
    were made with ripgrep, which skips them by default (the report's method section says so).
  * A file with a NUL byte is binary and is not searched, for the same reason; the count and the
    names of files whose NUL appears only after the first block are published.  A file opening with
    a UTF-16 byte-order mark is transcoded first; a UTF-8 byte-order mark is dropped.
  * `.gitignore` is NOT applied, because the report's searches listed ignored files (its method
    section names three).
  * Symbolic links are not followed.
  Git is called for two things only: `git cat-file blob` for the report, and `git ls-files` for the
  Task 1 marks.

Run:
    python tools/audit/check_reference_map.py <report-blob-identity> <report-working-tree-path>
Writes `tools/audit/reference_map_check.json`.
"""
from __future__ import annotations

import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "reference_map_check.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

EXCLUDED_NAMES = {
    "polyph9-release", "scratch_artifacts", "external resarch summary",
    "Claude outputs", "Codex research inventory", ".git",
}

# The report's own stated search parameters, quoted from its Task 2(b) and 2(c).0 sections.
HIT_RX = re.compile(rb"cowork_|cc_instruction|cc_report|cc_\*|listdir|glob\(|iterdir|scandir")
HIT_EXTS = (".py", ".mjs", ".js", ".sh", ".ps1", ".bat", ".cmake")
COVERAGE_RX = re.compile(rb"(cc|cowork)_[A-Za-z0-9_]+\.md")

# Task 1's five lists, as the report's headings name them (sections 1.1 to 1.5).
def _l11(n): return (fnmatch.fnmatchcase(n, "cowork_handoff_entry_*.md")
                     or n in ("cowork_handoff.md", "cowork_handoff_archive.md"))
def _l12(n): return fnmatch.fnmatchcase(n, "cowork_rulings_*.md") or fnmatch.fnmatchcase(n, "cowork_ruling_*.md")
def _l13(n): return fnmatch.fnmatchcase(n, "cc_instruction_*.md")
def _l14(n): return fnmatch.fnmatchcase(n, "cc_*.md") and not _l13(n)
def _l15(n): return fnmatch.fnmatchcase(n, "cowork_*.md") and not _l11(n) and not _l12(n)

ROOT_LISTS = [
    ("1.1", "`cowork_handoff_entry_*.md`, `cowork_handoff.md`, `cowork_handoff_archive.md` at the root", _l11),
    ("1.2", "`cowork_rulings_*.md`, `cowork_ruling_*.md` at the root", _l12),
    ("1.3", "`cc_instruction_*.md` at the root", _l13),
    ("1.4", "every other `cc_*.md` at the root (not matching `cc_instruction_*.md`)", _l14),
    ("1.5", "every other `cowork_*.md` at the root (not in 1.1 or 1.2)", _l15),
]


class Stop(Exception):
    """A precondition of the check does not hold. Never a warning."""


def git(*args: str) -> bytes:
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args[:3])} ... failed: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def norm_path(p: str) -> str:
    return p.strip().replace("\\", "/")


def is_excluded_path(rel: str) -> bool:
    return any(part in EXCLUDED_NAMES for part in rel.split("/"))


def is_hidden_path(rel: str) -> bool:
    return any(part.startswith(".") for part in rel.split("/"))


def iso(ts: float | None) -> str | None:
    if ts is None:
        return None
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).isoformat(timespec="seconds")


# ── reading a file the way the report's search tool would ────────────────────────────────────
def load_bytes(abs_path: str) -> tuple[bytes | None, str]:
    """Return (text bytes, state). state is 'text', 'binary', 'binary-late-nul' or 'unreadable'."""
    try:
        with open(abs_path, "rb") as fh:
            data = fh.read()
    except OSError as e:
        return None, f"unreadable: {e.__class__.__name__}"
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        try:
            data = data.decode("utf-16").encode("utf-8")
        except UnicodeDecodeError:
            return None, "binary"
    elif data[:3] == b"\xef\xbb\xbf":
        data = data[3:]
    head = data[:8192]
    if b"\x00" in head:
        return None, "binary"
    if b"\x00" in data:
        return None, "binary-late-nul"
    return data, "text"


def split_lines(data: bytes) -> list[bytes]:
    lines = data.split(b"\n")
    if lines and lines[-1] == b"":
        lines.pop()
    return lines


class FileFacts:
    """mtime and existence, looked up once per path."""

    def __init__(self, report_mtime: float):
        self.report_mtime = report_mtime
        self._cache: dict[str, dict] = {}

    def of(self, rel: str) -> dict:
        if rel in self._cache:
            return self._cache[rel]
        facts: dict = {"path": rel}
        if is_excluded_path(rel):
            facts.update(exists=None, state="under an excluded location -- not examined",
                         mtime=None, modified_after_report=None)
        else:
            ap = os.path.join(ROOT, rel)
            if os.path.isfile(ap):
                m = os.stat(ap).st_mtime
                facts.update(exists=True, mtime=iso(m), modified_after_report=m > self.report_mtime)
            else:
                facts.update(exists=False, mtime=None, modified_after_report=None)
            if is_hidden_path(rel):
                facts["hidden"] = True
        self._cache[rel] = facts
        return facts


# ── the walk ─────────────────────────────────────────────────────────────────────────────────
def walk(expressions: list[tuple[str, re.Pattern]]) -> dict:
    all_files: list[str] = []
    binary: list[str] = []
    late_nul: list[str] = []
    unreadable: list[dict] = []
    hit_lines: dict[tuple[str, int], str] = {}
    hit_ext_case_only: list[str] = []
    expr_counts: dict[str, dict[str, tuple[int, int]]] = {n: {} for n, _ in expressions}
    coverage: set[str] = set()
    text_files = 0
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_NAMES and not d.startswith("."))
        for fn in sorted(files):
            if fn.startswith(".") or fn in EXCLUDED_NAMES:
                continue
            ap = os.path.join(dirpath, fn)
            if os.path.islink(ap):
                continue
            rel = os.path.relpath(ap, ROOT).replace("\\", "/")
            all_files.append(rel)
            data, state = load_bytes(ap)
            if data is None:
                if state == "binary":
                    binary.append(rel)
                elif state == "binary-late-nul":
                    late_nul.append(rel)
                else:
                    unreadable.append({"path": rel, "state": state})
                continue
            text_files += 1
            if COVERAGE_RX.search(data):
                coverage.add(rel)
            lines = None
            for name, rx in expressions:
                if not rx.search(data):
                    continue
                if lines is None:
                    lines = split_lines(data)
                nl = nm = 0
                for ln in lines:
                    k = len(rx.findall(ln))
                    if k:
                        nl += 1
                        nm += k
                expr_counts[name][rel] = (nl, nm)
            lower = fn.lower()
            if fn.endswith(HIT_EXTS):
                if HIT_RX.search(data):
                    if lines is None:
                        lines = split_lines(data)
                    for i, ln in enumerate(lines, 1):
                        if HIT_RX.search(ln):
                            hit_lines[(rel, i)] = ln.decode("utf-8", "replace")
            elif lower.endswith(HIT_EXTS) and HIT_RX.search(data):
                hit_ext_case_only.append(rel)
    return {
        "all_files": all_files, "binary": binary, "late_nul": late_nul, "unreadable": unreadable,
        "hit_lines": hit_lines, "hit_ext_case_only": hit_ext_case_only,
        "expr_counts": expr_counts, "coverage": coverage, "text_files": text_files,
    }


# ── the report ───────────────────────────────────────────────────────────────────────────────
def find_line(lines: list[str], text: str, start: int = 0) -> int:
    for i in range(start, len(lines)):
        if lines[i] == text:
            return i
    raise Stop(f"the report has no line reading exactly: {text!r}")


def find_prefix(lines: list[str], prefix: str, start: int = 0) -> int:
    for i in range(start, len(lines)):
        if lines[i].startswith(prefix):
            return i
    raise Stop(f"the report has no line beginning: {prefix!r}")


def fenced_block(lines: list[str], start: int, fence: str) -> tuple[int, int]:
    """Return (first content index, closing fence index) of the first `fence` block after start."""
    o = find_prefix(lines, fence, start)
    c = find_line(lines, fence, o + 1)
    return o + 1, c


def split_cells(row: str) -> list[str]:
    """Split a Markdown table row on pipes that lie outside code spans."""
    cells, cur, tick = [], [], 0
    i = 0
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    while i < len(s):
        ch = s[i]
        if ch == "`":
            j = i
            while j < len(s) and s[j] == "`":
                j += 1
            run = j - i
            if tick == 0:
                tick = run
            elif tick == run:
                tick = 0
            cur.append(s[i:j])
            i = j
            continue
        if ch == "|" and tick == 0:
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


SPAN_RX = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")
LABEL_SPLIT = re.compile(r";|\.\s|—|\*\*|\||\(|\)")
SINGLE_RX = re.compile(r"^(\d+)$")
RANGE_RX = re.compile(r"^(\d+)\s*[–-]\s*(\d+)$")


def items_in(segment: str) -> list[dict]:
    """Every code span preceded by a colon whose label carries a digit."""
    out = []
    prev_end = 0
    for m in SPAN_RX.finditer(segment):
        before = segment[prev_end:m.start()]
        prev_end = m.end()
        if not re.search(r":\s*$", before):
            continue
        label = LABEL_SPLIT.split(re.sub(r":\s*$", "", before))[-1].strip()
        if not re.search(r"\d", label):
            continue
        code = m.group(2)
        if len(m.group(1)) > 1 and code.startswith(" ") and code.endswith(" "):
            code = code[1:-1]
        item = {"label": label, "code": code}
        s, r = SINGLE_RX.match(label), RANGE_RX.match(label)
        if s:
            item["first"] = item["last"] = int(s.group(1))
        elif r:
            item["first"], item["last"] = int(r.group(1)), int(r.group(2))
        else:
            item["unparsed"] = "the label before the quote is not one line number or one range"
        out.append(item)
    return out


def code_patterns(code: str) -> tuple[re.Pattern, re.Pattern, re.Pattern]:
    parts = re.split(r"\.\.\.|…", code)
    exact = re.compile(".*?".join(re.escape(p) for p in parts))
    across = re.compile(".*?".join(re.escape(p) for p in parts), re.S)
    normed = re.compile(".*?".join(re.escape(re.sub(r"\s+", " ", p)) for p in parts))
    return exact, across, normed


def match_item(item: dict, lines: list[str]) -> dict:
    exact, across, normed = code_patterns(item["code"])
    a, b = item["first"], item["last"]
    res = {"file_line_count": len(lines)}
    if a < 1 or b > len(lines) or a > b:
        res["verdict"] = "MISMATCH"
        res["reason"] = "the line or range lies outside the file"
    else:
        span = lines[a - 1:b]
        mode = None
        for k, ln in enumerate(span):
            if exact.search(ln):
                mode = f"exact, on line {a + k}"
                break
        if mode is None and b > a and across.search("\n".join(span)):
            mode = "exact, across the range"
        if mode is None and normed.search(re.sub(r"\s+", " ", " ".join(span))):
            mode = "after collapsing whitespace"
        if mode:
            res["verdict"] = "MATCH"
            res["mode"] = mode
        else:
            res["verdict"] = "MISMATCH"
            res["text_at_the_cited_lines"] = span
    if res["verdict"] == "MISMATCH":
        res["found_exactly_on_lines"] = [i for i, ln in enumerate(lines, 1) if exact.search(ln)][:20]
    return res


# ── the five checks ──────────────────────────────────────────────────────────────────────────
def check_1(rlines, W, facts) -> dict:
    h = find_line(rlines, "### 2(b).5 Every hit line, verbatim, in Grep's order")
    first, close = fenced_block(rlines, h, "~~~~")
    listed: dict[tuple[str, int], tuple[int, str]] = {}
    unchecked, duplicates, mismatches = [], [], []
    for idx in range(first, close):
        raw = rlines[idx]
        m = re.match(r"^([^:]+):(\d+):(.*)$", raw)
        if not m:
            unchecked.append({"report_line": idx + 1, "text": raw, "reason": "not of the form path:line:content"})
            continue
        rel, ln, content = norm_path(m.group(1)), int(m.group(2)), m.group(3)
        key = (rel, ln)
        if key in listed:
            duplicates.append({"report_line": idx + 1, "text": raw, "first_listed_at_report_line": listed[key][0]})
            continue
        listed[key] = (idx + 1, content)
    file_cache: dict[str, list[str] | str] = {}
    matched = 0
    for (rel, ln), (rline, content) in listed.items():
        if rel not in file_cache:
            if is_excluded_path(rel):
                file_cache[rel] = "under an excluded location -- not examined"
            else:
                data, state = load_bytes(os.path.join(ROOT, rel)) if os.path.isfile(os.path.join(ROOT, rel)) else (None, "file does not exist")
                file_cache[rel] = [x.decode("utf-8", "replace") for x in split_lines(data)] if data is not None else state
        fl = file_cache[rel]
        if isinstance(fl, str):
            mismatches.append({"report_line": rline, "path": rel, "line": ln, "report_content": content,
                               "reason": fl, **{k: v for k, v in facts.of(rel).items() if k != "path"}})
            continue
        actual = fl[ln - 1] if 1 <= ln <= len(fl) else None
        if actual == content:
            matched += 1
            continue
        rec = {"report_line": rline, "path": rel, "line": ln, "report_content": content,
               "file_content": actual, **{k: v for k, v in facts.of(rel).items() if k != "path"}}
        if actual is None:
            rec["reason"] = "the file has fewer lines"
        elif actual.rstrip("\r") == content:
            rec["reason"] = "equal only after dropping a trailing carriage return from the file's line"
        elif actual.rstrip() == content.rstrip():
            rec["reason"] = "equal only after dropping trailing whitespace"
        else:
            rec["reason"] = "different text"
        mismatches.append(rec)
    walk_keys = set(W["hit_lines"])
    listed_keys = set(listed)
    listed_not_walked = []
    for rel, ln in sorted(listed_keys - walk_keys):
        listed_not_walked.append({"path": rel, "line": ln, "report_line": listed[(rel, ln)][0],
                                  "report_content": listed[(rel, ln)][1],
                                  **{k: v for k, v in facts.of(rel).items() if k != "path"}})
    walked_not_listed = []
    for rel, ln in sorted(walk_keys - listed_keys):
        walked_not_listed.append({"path": rel, "line": ln, "content": W["hit_lines"][(rel, ln)],
                                  **{k: v for k, v in facts.of(rel).items() if k != "path"}})
    return {
        "report_block": {"first_line": first + 1, "last_line": close},
        "listed_hit_lines": len(listed),
        "listed_equal_exactly": matched,
        "content_mismatches": mismatches,
        "unchecked": unchecked,
        "duplicate_listings": duplicates,
        "walk_hit_lines": len(walk_keys),
        "walk_hit_files": len({r for r, _ in walk_keys}),
        "listed_hit_files": len({r for r, _ in listed_keys}),
        "listed_but_not_found_by_the_walk": listed_not_walked,
        "found_by_the_walk_but_not_listed": walked_not_listed,
        "files_with_a_hit_whose_extension_matches_only_ignoring_case": W["hit_ext_case_only"],
    }


def resolve(name: str, basenames: dict[str, list[str]]) -> tuple[str | None, str | None]:
    rel = norm_path(name)
    if is_excluded_path(rel):
        return None, "the path lies under an excluded location"
    if os.path.isfile(os.path.join(ROOT, rel)):
        return rel, None
    if "/" in rel:
        return None, "no file at that path"
    cands = basenames.get(rel, [])
    if len(cands) == 1:
        return cands[0], None
    return None, f"a bare file name matching {len(cands)} walked files" + (f": {cands}" if cands else "")


def check_2(rlines, W) -> dict:
    s = find_prefix(rlines, "### 2(b).1 ")
    e = find_prefix(rlines, "### 2(b).3 ", s)
    basenames: dict[str, list[str]] = {}
    for rel in W["all_files"]:
        basenames.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)
    entries = []   # (report_line, file_field, [segments])
    for idx in range(s, e):
        raw = rlines[idx]
        if raw.startswith("|"):
            cells = split_cells(raw)
            if all(re.fullmatch(r"\s*:?-{3,}:?\s*", c) for c in cells):
                continue
            entries.append((idx + 1, cells[0], cells[1:], "table row"))
        elif raw.startswith("- `"):
            m = re.match(r"^- (`[^`]+`)(.*)$", raw)
            if m:
                entries.append((idx + 1, m.group(1), [m.group(2)], "bullet"))
            else:
                entries.append((idx + 1, "", [raw[2:]], "bullet whose file field does not parse"))
    checked, mismatched, unchecked = [], [], []
    loaded: dict[str, list[str] | str] = {}
    for rline, field, segments, kind in entries:
        items = [it for seg in segments for it in items_in(seg)]
        if not items:
            continue
        paths = re.findall(r"`([^`]+)`", field)
        target, why = (None, None)
        if len(paths) != 1:
            why = f"the entry names {len(paths)} files in its file field: {paths}"
        else:
            target, why = resolve(paths[0], basenames)
        for it in items:
            base = {"report_line": rline, "entry": kind, "file_field": field.strip(), "label": it["label"], "code": it["code"]}
            if target is None:
                unchecked.append({**base, "reason": f"the file cannot be resolved to exactly one path: {why}"})
                continue
            base["file"] = target
            if "unparsed" in it:
                unchecked.append({**base, "reason": it["unparsed"]})
                continue
            if target not in loaded:
                data, state = load_bytes(os.path.join(ROOT, target))
                loaded[target] = [x.decode("utf-8", "replace").rstrip("\r") for x in split_lines(data)] if data is not None else state
            fl = loaded[target]
            if isinstance(fl, str):
                unchecked.append({**base, "reason": f"the file could not be read as text: {fl}"})
                continue
            res = match_item(it, fl)
            rec = {**base, **res}
            (checked if res["verdict"] == "MATCH" else mismatched).append(rec)
    return {
        "report_span": {"first_line": s + 1, "last_line": e},
        "items_matched": len(checked),
        "matched_by_mode": _count_by(checked, "mode"),
        "mismatches": mismatched,
        "unchecked": unchecked,
        "matched": checked,
    }


def _count_by(recs, key):
    out: dict[str, int] = {}
    for r in recs:
        k = re.sub(r"on line \d+", "on one line", r.get(key, ""))
        out[k] = out.get(k, 0) + 1
    return out


def parse_expressions(rlines) -> list[dict]:
    s = find_line(rlines, "## TASK 2(a) — text references, per expression, every file with a count")
    e = find_prefix(rlines, "## TASK 2(b)", s)
    out = []
    for idx in range(s, e):
        m = re.match(r"^### Expression (\d+) — `(.+)`$", rlines[idx])
        if not m:
            continue
        # An expression's listing may be split over several fenced blocks ("continued");
        # every block up to the next heading belongs to it.
        end = next((j for j in range(idx + 1, e) if rlines[j].startswith("#")), e)
        blocks, j = [], idx + 1
        while j < end:
            if rlines[j] == "```":
                c = find_line(rlines, "```", j + 1)
                if c >= end:
                    raise Stop(f"an unclosed code block under expression {m.group(1)} at report line {j + 1}")
                blocks.append((j + 1, c))
                j = c + 1
            else:
                j += 1
        if not blocks:
            raise Stop(f"no code block under expression {m.group(1)}")
        summary = None
        for k in range(blocks[-1][1] + 1, end):
            sm = re.match(r"^Grep's summary line: `(.*)`$", rlines[k])
            if sm:
                summary = {"report_line": k + 1, "text": sm.group(1)}
                break
        out.append({"number": int(m.group(1)), "expression": m.group(2), "heading_line": idx + 1,
                    "blocks": blocks, "summary": summary})
    if len(out) != 6:
        raise Stop(f"expected six expression headings in Task 2(a), found {len(out)}")
    return out


def check_3(rlines, exprs, W, facts) -> dict:
    results = []
    for ex in exprs:
        name = f"expression {ex['number']}"
        counts = W["expr_counts"][name]
        listed: dict[str, tuple[int, int]] = {}
        unchecked, duplicates, per_file = [], [], []
        tallies = {"lines only": 0, "matches only": 0, "both": 0, "neither": 0, "not examined": 0}
        for idx in (i for first, close in ex["blocks"] for i in range(first, close)):
            raw = rlines[idx]
            m = re.match(r"^([^:]+):(\d+)$", raw)
            if not m:
                unchecked.append({"report_line": idx + 1, "text": raw, "reason": "not of the form path:count"})
                continue
            rel, fig = norm_path(m.group(1)), int(m.group(2))
            if rel in listed:
                duplicates.append({"report_line": idx + 1, "text": raw})
                continue
            listed[rel] = (idx + 1, fig)
            f = facts.of(rel)
            rec = {"report_line": idx + 1, "path": rel, "report_figure": fig}
            if rel in counts:
                nl, nm = counts[rel]
            elif f["exists"] and not is_hidden_path(rel):
                data, state = load_bytes(os.path.join(ROOT, rel))
                nl = nm = 0 if data is not None else None
                if data is None:
                    rec["file_state"] = state
            elif f["exists"]:
                data, state = load_bytes(os.path.join(ROOT, rel))
                if data is None:
                    nl = nm = None
                    rec["file_state"] = state
                else:
                    rx = dict(W["expr_rx"])[name]
                    ls = split_lines(data)
                    nl = sum(1 for ln in ls if rx.search(ln))
                    nm = sum(len(rx.findall(ln)) for ln in ls)
                    rec["note"] = "a hidden path, recomputed outside the walk"
            else:
                nl = nm = None
                rec["file_state"] = "not examined" if f["exists"] is None else "file does not exist"
            rec["matching_lines"], rec["individual_matches"] = nl, nm
            if nl is None:
                rec["equals"] = "not examined"
            elif fig == nl and fig == nm:
                rec["equals"] = "both"
            elif fig == nl:
                rec["equals"] = "lines only"
            elif fig == nm:
                rec["equals"] = "matches only"
            else:
                rec["equals"] = "neither"
            tallies[rec["equals"]] += 1
            if rec["equals"] in ("neither", "not examined"):
                rec.update({k: v for k, v in f.items() if k != "path"})
            per_file.append(rec)
        walk_only = [{"path": rel, "matching_lines": counts[rel][0], "individual_matches": counts[rel][1],
                      **{k: v for k, v in facts.of(rel).items() if k != "path"}}
                     for rel in sorted(set(counts) - set(listed))]
        listed_no_match = [r for r in per_file if r["matching_lines"] == 0]
        for r in listed_no_match:
            r.update({k: v for k, v in facts.of(r["path"]).items() if k != "path"})
        results.append({
            "expression": ex["expression"], "heading_line": ex["heading_line"],
            "report_blocks": [{"first_line": f + 1, "last_line": c} for f, c in ex["blocks"]],
            "report_summary_line": ex["summary"],
            "listed_files": len(listed),
            "sum_of_listed_figures": sum(v for _, v in listed.values()),
            "walk_files_with_a_match": len(counts),
            "walk_total_matching_lines": sum(v[0] for v in counts.values()),
            "walk_total_individual_matches": sum(v[1] for v in counts.values()),
            "per_file_tally_of_what_the_report_figure_equals": tallies,
            "listed_files_whose_figure_equals_neither_or_not_examined":
                [r for r in per_file if r["equals"] in ("neither", "not examined")],
            "listed_files_with_no_match_now": listed_no_match,
            "files_the_walk_finds_that_are_not_listed": walk_only,
            "unchecked": unchecked,
            "duplicate_listings": duplicates,
            "per_file": per_file,
        })
    return {"expressions": results}


def git_tracked(names: list[str]) -> set[str]:
    tracked: set[str] = set()
    for i in range(0, len(names), 40):
        batch = names[i:i + 40]
        out = git("--literal-pathspecs", "ls-files", "-z", "--", *batch)
        tracked.update(p for p in out.decode("utf-8", "replace").split("\0") if p)
    return tracked


def check_4(rlines, facts) -> dict:
    t1 = find_line(rlines, "## TASK 1 — the population to move")
    t2 = find_prefix(rlines, "## TASK 2(a)", t1)
    root_files = sorted(n for n in os.listdir(ROOT)
                        if n not in EXCLUDED_NAMES and os.path.isfile(os.path.join(ROOT, n)))
    report_lists = {}
    for sec, desc, pred in ROOT_LISTS:
        h = find_prefix(rlines, f"### {sec} ", t1)
        if h >= t2:
            raise Stop(f"Task 1 section {sec} not found")
        first, close = fenced_block(rlines, h, "```")
        entries, unchecked = [], []
        for idx in range(first, close):
            m = re.match(r"^([TU]) (\S.*)$", rlines[idx])
            if m:
                entries.append((idx + 1, m.group(1), m.group(2)))
            else:
                unchecked.append({"report_line": idx + 1, "text": rlines[idx], "reason": "not of the form 'T name' or 'U name'"})
        report_lists[sec] = (h, first, close, entries, unchecked, desc, pred)
    all_names = sorted({n for v in report_lists.values() for _, _, n in v[3]} | set(root_files))
    tracked = git_tracked(all_names)
    out = []
    for sec, (h, first, close, entries, unchecked, desc, pred) in report_lists.items():
        recomputed = [n for n in root_files if pred(n)]
        seen: dict[str, int] = {}
        dups = []
        for rl, mark, n in entries:
            if n in seen:
                dups.append({"report_line": rl, "name": n, "first_at_report_line": seen[n]})
            else:
                seen[n] = rl
        rep = {n: (rl, mark) for rl, mark, n in entries}
        in_report_not_root = [{"name": n, "report_line": rep[n][0], "report_mark": rep[n][1],
                               "in_another_recomputed_list": next((s for s, _, p in ROOT_LISTS if s != sec and n in root_files and p(n)), None),
                               **{k: v for k, v in facts.of(n).items() if k != "path"}}
                              for n in sorted(set(rep) - set(recomputed))]
        in_root_not_report = [{"name": n, "git_mark": "T" if n in tracked else "U",
                               **{k: v for k, v in facts.of(n).items() if k != "path"}}
                              for n in sorted(set(recomputed) - set(rep))]
        mark_diffs = [{"name": n, "report_line": rep[n][0], "report_mark": rep[n][1],
                       "git_mark": "T" if n in tracked else "U",
                       **{k: v for k, v in facts.of(n).items() if k != "path"}}
                      for n in sorted(set(rep) & set(recomputed))
                      if rep[n][1] != ("T" if n in tracked else "U")]
        out.append({
            "section": sec, "population": desc, "heading_line": h + 1,
            "report_block": {"first_line": first + 1, "last_line": close},
            "report_entries": len(entries),
            "report_T": sum(1 for _, m, _ in entries if m == "T"),
            "report_U": sum(1 for _, m, _ in entries if m == "U"),
            "recomputed_entries": len(recomputed),
            "recomputed_T": sum(1 for n in recomputed if n in tracked),
            "recomputed_U": sum(1 for n in recomputed if n not in tracked),
            "listed_but_not_in_the_recomputed_list": in_report_not_root,
            "in_the_recomputed_list_but_not_listed": in_root_not_report,
            "mark_differences": mark_diffs,
            "duplicate_listings": dups,
            "unchecked": unchecked,
        })
    return {"root_files_listed": len(root_files), "git_ls_files_calls": (len(all_names) + 39) // 40,
            "names_marked": len(all_names), "lists": out}


def check_5(rlines, report_lists_raw, W, facts) -> dict:
    s = find_prefix(rlines, "## TASK 2(c)")
    e = find_line(rlines, "## Declared", s)
    section = None
    bullets: dict[str, list[dict]] = {}
    unchecked = []
    for idx in range(s, e):
        raw = rlines[idx]
        hm = re.match(r"^### (2\(c\)\.\d+)", raw)
        if hm:
            section = hm.group(1)
            continue
        if not raw.startswith("- `"):
            continue
        m = re.match(r"^- `([^`]+)` — \*\*([^*]+)\*\*", raw)
        if not m:
            unchecked.append({"report_line": idx + 1, "text": raw, "reason": "a bullet not of the form - `path` — **CLASS**"})
            continue
        rel = norm_path(m.group(1))
        bullets.setdefault(rel, []).append({"report_line": idx + 1, "section": section, "class": m.group(2)})
    statement_population = set(report_lists_raw)
    P = W["coverage"]
    twice, not_classified, bullet_and_statement = [], [], []
    for rel in sorted(bullets):
        if len(bullets[rel]) >= 2:
            twice.append({"path": rel, "classifications": bullets[rel],
                          "also_in_the_2c1_statement_population": rel in statement_population,
                          "matches_now": rel in P,
                          **{k: v for k, v in facts.of(rel).items() if k != "path"}})
    for rel in sorted(P):
        b = bullets.get(rel, [])
        in_s = rel in statement_population
        if len(b) >= 2:
            continue
        elif len(b) == 1 and in_s and b[0]["section"] != "2(c).1":
            bullet_and_statement.append({"path": rel, "classification": b[0],
                                         **{k: v for k, v in facts.of(rel).items() if k != "path"}})
        elif not b and not in_s:
            not_classified.append({"path": rel, **{k: v for k, v in facts.of(rel).items() if k != "path"}})
    binary, late = set(W["binary"]), set(W["late_nul"])
    no_longer = []
    for rel in sorted(set(bullets) - P):
        f = facts.of(rel)
        if f["exists"] is None:
            state = "under an excluded location"
        elif not f["exists"]:
            state = "file does not exist"
        elif f.get("hidden"):
            state = "a hidden path, not walked"
        elif rel in binary or rel in late:
            state = "binary, not searched"
        else:
            state = "exists and does not match"
        no_longer.append({"path": rel, "classifications": bullets[rel], "state": state,
                          **{k: v for k, v in f.items() if k != "path"}})
    statement_no_match = sorted(statement_population - P)
    return {
        "report_span": {"first_line": s + 1, "last_line": e},
        "coverage_expression": COVERAGE_RX.pattern.decode(),
        "walk_files_matching": len(P),
        "classified_paths": len(bullets),
        "classification_bullets": sum(len(v) for v in bullets.values()),
        "statement_population_size": len(statement_population),
        "statement_population_note": ("the root files the report's Task 1 sections 1.1 to 1.4 list; "
                                      "2(c).1 covers those among them that contain a match"),
        "classified_twice": twice,
        "classified_by_a_bullet_outside_2c1_and_also_in_the_2c1_statement_population": bullet_and_statement,
        "not_classified": not_classified,
        "classified_but_no_longer_matching": no_longer,
        "statement_population_members_with_no_match_now": statement_no_match,
        "unchecked": unchecked,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_reference_map.py <report-blob-identity> <report-working-tree-path>")
        return 2
    blob, report_path = argv
    if not re.fullmatch(r"[0-9a-f]{40}", blob):
        raise Stop(f"not a full blob identity: {blob!r}")
    kind = git("cat-file", "-t", blob).decode().strip()
    if kind != "blob":
        raise Stop(f"{blob} is a {kind}, not a blob")
    text = git("cat-file", "blob", blob).decode("utf-8")
    rlines = [ln.rstrip("\r") for ln in text.split("\n")]
    rp = os.path.join(ROOT, norm_path(report_path))
    if not os.path.isfile(rp):
        raise Stop(f"no file at the report path given: {report_path}")
    report_mtime = os.stat(rp).st_mtime
    facts = FileFacts(report_mtime)

    exprs = parse_expressions(rlines)
    expr_rx = [(f"expression {x['number']}", re.compile(x["expression"].encode())) for x in exprs]
    t0 = time.time()
    W = walk(expr_rx)
    W["expr_rx"] = expr_rx
    walk_seconds = round(time.time() - t0, 1)

    c4 = check_4(rlines, facts)
    report_lists_raw = []
    t1 = find_line(rlines, "## TASK 1 — the population to move")
    for sec in ("1.1", "1.2", "1.3", "1.4"):
        h = find_prefix(rlines, f"### {sec} ", t1)
        first, close = fenced_block(rlines, h, "```")
        for idx in range(first, close):
            m = re.match(r"^([TU]) (\S.*)$", rlines[idx])
            if m:
                report_lists_raw.append(m.group(2))

    result = {
        "generator": "tools/audit/check_reference_map.py",
        "command": "python tools/audit/check_reference_map.py " + " ".join(argv),
        "run_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "report": {"blob": blob, "working_tree_path_for_mtime_only": norm_path(report_path),
                   "mtime": iso(report_mtime), "lines": len(rlines)},
        "what_is_checked": [
            "1: section 2(b).5 hit lines against the files, and an independent walk, both directions",
            "2: sections 2(b).1 and 2(b).2 quoted items 'NNN: `code`' / 'NNN-MMM: `code`' against the files",
            "3: Task 2(a) per-file figures recomputed as matching lines and as individual matches; walk differences both directions",
            "4: Task 1 root lists recomputed from a root listing, marks from git ls-files",
            "5: section 2(c) coverage of the files matching the coverage expression",
        ],
        "what_is_not_checked": ("whether any verdict (i)-(iv) of 2(b), or any class of 2(c), is right -- those are "
                                "judgements the writing side reads; nor the report's prose, method section, "
                                "non-quoted table columns, 2(b).3 or 2(b).4"),
        "unparsed_policy": "a line or item this tool cannot parse is published as unchecked with its reason, never skipped",
        "later_change_field": ("every difference carries 'modified_after_report': true when the file's mtime is later "
                               "than the report's, false when not, null when the file is absent or not examined; "
                               "no difference is judged a defect of the report"),
        "walk": {
            "rules": ["directories named " + ", ".join(sorted(EXCLUDED_NAMES)) + " are not entered, at any depth",
                      "names beginning with a dot are not walked (ripgrep's default)",
                      "a file with a NUL byte is binary and not searched; UTF-16 with a byte-order mark is transcoded; a UTF-8 byte-order mark is dropped",
                      ".gitignore is not applied",
                      "symbolic links are not followed"],
            "seconds": walk_seconds,
            "files_walked": len(W["all_files"]),
            "text_files_searched": W["text_files"],
            "binary_files_not_searched": len(W["binary"]),
            "files_whose_nul_byte_is_after_the_first_block": W["late_nul"],
            "unreadable_files": W["unreadable"],
        },
        "check_1_hit_lines": check_1(rlines, W, facts),
        "check_2_deciding_lines": check_2(rlines, W),
        "check_3_counts": check_3(rlines, exprs, W, facts),
        "check_4_root_lists": c4,
        "check_5_coverage": check_5(rlines, report_lists_raw, W, facts),
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    c1, c2, c5 = result["check_1_hit_lines"], result["check_2_deciding_lines"], result["check_5_coverage"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"walk: {result['walk']['files_walked']} files, {walk_seconds}s")
    print(f"check 1: {len(c1['content_mismatches'])} content mismatches, {len(c1['unchecked'])} unchecked, "
          f"{len(c1['listed_but_not_found_by_the_walk'])} listed-not-walked, "
          f"{len(c1['found_by_the_walk_but_not_listed'])} walked-not-listed")
    print(f"check 2: {c2['items_matched']} matched, {len(c2['mismatches'])} mismatched, {len(c2['unchecked'])} unchecked")
    for x in result["check_3_counts"]["expressions"]:
        print(f"check 3 {x['expression']}: {x['per_file_tally_of_what_the_report_figure_equals']}, "
              f"walk-only {len(x['files_the_walk_finds_that_are_not_listed'])}")
    for x in c4["lists"]:
        print(f"check 4 {x['section']}: listed-not-root {len(x['listed_but_not_in_the_recomputed_list'])}, "
              f"root-not-listed {len(x['in_the_recomputed_list_but_not_listed'])}, mark diffs {len(x['mark_differences'])}")
    print(f"check 5: twice {len(c5['classified_twice'])}, not classified {len(c5['not_classified'])}, "
          f"no longer matching {len(c5['classified_but_no_longer_matching'])}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as e:
        print(f"STOP: {e}")
        sys.exit(1)
