#!/usr/bin/env python3
"""The PROCESS CHECK — scan a dispatch or a session report for three recorded failure shapes.

WHAT THIS IS.  Mechanism 2 of the phase-1p wave
(`cc_instruction_phase1p_home_rulings_and_mechanisms.md` §6.2).  Three rules that were being
broken by both the writing and the executing side are stated as prose in
`cowork_audit_protocol.md`'s dispatch-protocol section; this makes two of them mechanically
checkable and the third structurally enforced:

  1. A BARE QUANTITY not adjacent to an artifact-and-field or a document-and-line citation.
     Register entry D-431: "A quantity may not be copied into a dispatch or into a session
     report as a literal value.  It is named as an artifact and a field."
  2. A CLAIM ABOUT THE CODE with no `file:line` citation.  Same rule's premise clause: a claim
     of fact about the code, the corpus or the record is cited to the primary source it can be
     checked at.
  3. A MISSING SELF-CHECK SECTION.  Register entry D-434: every dispatch and every session
     report carries one, answering the five-item checklist.  Its absence is what makes the
     obligation a mechanism rather than a habit.

WHAT THIS TOOL IS NOT.  It reads TEXT.  It cannot tell a wrong premise from a right one, so the
premise failures that cost this project the most — a dispatch premise refuted at a commit, a
dispatch premise refuted at a control flow — are outside its reach WHEN THEY CARRY A CITATION.
It catches them only in the shape they usually arrive in: asserted with nothing to check them
against.  That limit is not a caveat bolted on afterwards; it is measured, per known instance,
by `--establish` (see below), and the measurement is the artifact
`tools/audit/process_check_establishment.json`.

ESTABLISHMENT (#19).  A measurement tool is trusted only after being positively established, never
because it is merely unfalsified.  `--establish` runs the check over the recorded instances of
each failure shape — the eight cited at D-434's home — and over a control set of text that is
correct, and reports the detection rate and the false-positive rate.  A check that does not find
the errors we already know about is not established, and reporting that is the right outcome.

Run:
    python tools/audit/process_check.py <file> [<file> ...]     # check documents
    python tools/audit/process_check.py --establish             # measure the check itself
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ESTABLISH_OUT = os.path.join(HERE, "process_check_establishment.json")

# ── what counts as a citation ────────────────────────────────────────────────
# An ARTIFACT-AND-FIELD citation: a .json/.csv path followed by an arrow and a field path, in
# either order of surrounding punctuation.  A DOCUMENT-AND-LINE citation: `path:123` or
# `path:12-34`, or a section mark, or an OI-/D- row reference.
CITE_ARTIFACT = re.compile(r"[\w./\\-]+\.(?:json|csv)`?\s*(?:→|->)\s*`?[\w.\[\]-]+")
CITE_LINE = re.compile(r"[\w./\\-]+\.(?:md|py|cpp|h|json|csv|txt)`?\s*:\s*\d+")
CITE_BARE_LINE = re.compile(r"`?:\d+(?:-\d+)?`?")
CITE_ROW = re.compile(r"\b(?:OI|D)-\d+\b")
CITE_SECTION = re.compile(r"§\s?[\w.]+")
CITE_COMMIT = re.compile(r"\b[0-9a-f]{7,40}\b")

CITES = [CITE_ARTIFACT, CITE_LINE, CITE_BARE_LINE, CITE_ROW, CITE_SECTION, CITE_COMMIT]

# ── what counts as a bare quantity ───────────────────────────────────────────
# A number that ASSERTS a measured amount.  Deliberately narrow: a count of things, a
# percentage, a ratio "N of M", a signed change.  Ordinary prose numbers ("one", "the three
# surfaces", a date, a principle number "#17", a section "§8c", a line ":193") are not
# quantities in this sense and are excluded by construction below.
QUANTITY = re.compile(
    r"(?<![\w.#§:$-])"                       # not part of an identifier, a #ref, a §, a :line
    r"(\d{1,3}(?:[,   ]\d{3})+|\d+(?:\.\d+)?)"
    r""  # the class above holds four thousands separators this repository's prose uses:
    r""  # comma, narrow no-break space, no-break space, plain space. Superseded form follows: [,  , ]\d{3})+|\d+(?:\.\d+)?)"
    r"\s*(%|pp\b|ticks\b|entries\b|entry\b|clusters\b|rows\b|documents\b|files\b|of\s+\d+)?"
)
# Numbers that are never a measured quantity in this project's prose.
NOT_A_QUANTITY = re.compile(
    r"^(?:19|20)\d{2}$"                      # a year
    r"|^\d{1,2}$"                            # small ordinals: "the 3 surfaces", "#5", "step 2"
)

# ── what counts as a claim about the code ────────────────────────────────────
# A sentence asserting runtime or structural fact about our own code.  The vocabulary is drawn
# from the recorded instances, not invented: reachability, defaults, call sites, firing.
CODE_CLAIM = re.compile(
    r"\b(?:"
    r"reachable|unreachable|dormant|compiled and dormant|"
    r"defaults? (?:to|true|false|ON|OFF)|"
    r"call sites?|callers?|"
    r"fires? \d|never fires|fires 0|"
    r"returns? (?:the|early|null|nullptr)|"
    r"the (?:record|legacy) arm runs|"
    r"is (?:LIVE|live) (?:production )?code|"
    r"runs on the (?:record|legacy) arm"
    r")\b")

# Files whose names mark them as code, for the citation test on a code claim.
CODE_CITE = re.compile(r"[\w./\\-]+\.(?:cpp|h|hpp|py|js|ts)`?\s*:\s*\d+")

# The heading must BE the document's own self-check, not merely mention the phrase. A heading
# may open with a section number or a marker; after that the words must come first. The loose
# form (anywhere in the heading) was tried and rejected during establishment: it passed the
# phase-1p dispatch on a heading that names the self-check MECHANISM, which is a different thing
# from the dispatch having run one.
SELF_CHECK_HEADING = re.compile(
    r"^#{1,6}\s+[^A-Za-z\n]{0,12}self[- ]check\b", re.I | re.M)


HEADING = re.compile(r"^\s{0,3}#{1,6}\s")


def sentences(text: str) -> list[tuple[int, str, bool]]:
    """(line number, sentence, is_heading) — units that keep their line for reporting.

    Headings are returned MARKED, not dropped: a heading numbered `### 3.1 The ruling` carries
    a number that is a section label and not a measured amount, so the quantity rule must not
    read it — but a heading can still make a claim, so the code-claim rule still sees it. This
    was the check's own first false-positive class, found by running it over the three dispatches
    it was built for and reported rather than tuned away silently.
    """
    out: list[tuple[int, str, bool]] = []
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        head = bool(HEADING.match(line))
        for part in re.split(r"(?<=[.;])\s+(?=[A-Z*`])", stripped):
            if part.strip():
                out.append((i, part.strip(), head))
    return out


def has_citation(s: str) -> bool:
    return any(rx.search(s) for rx in CITES)


def bare_quantities(s: str) -> list[str]:
    found = []
    for m in QUANTITY.finditer(s):
        val, unit = m.group(1), m.group(2)
        # A unit OVERRIDES the small-number exclusion. Without this the exclusion swallows the
        # very instances the rule was ruled on — "about 30 entries", "the set is 75 entries",
        # "38 of 143 read" are all two-digit and all measured amounts. Measured at --establish:
        # before the override, detection over the recorded instances was two of eight, and the
        # three it then missed were exactly these.
        if not unit and NOT_A_QUANTITY.match(val.replace(",", "").replace(" ", "").replace(" ", "")):
            continue
        found.append(m.group(0).strip())
    return found


def check_text(text: str, name: str) -> list[dict]:
    findings: list[dict] = []
    for line, s, is_heading in sentences(text):
        qs = [] if is_heading else bare_quantities(s)
        if qs and not has_citation(s):
            findings.append({"file": name, "line": line, "rule": "D-431 bare quantity",
                             "detail": ", ".join(qs[:4]), "sentence": s[:200]})
        if CODE_CLAIM.search(s) and not CODE_CITE.search(s):
            findings.append({"file": name, "line": line, "rule": "D-431 uncited code claim",
                             "detail": CODE_CLAIM.search(s).group(0), "sentence": s[:200]})
    if not SELF_CHECK_HEADING.search(text):
        findings.append({"file": name, "line": 0, "rule": "D-434 missing self-check section",
                         "detail": "no heading matching 'self-check'", "sentence": ""})
    return findings


# ── establishment (#19) ──────────────────────────────────────────────────────
# The eight instances cited at D-434's home, each reproduced here as the SHAPE it arrived in.
# Every one carries the row or artifact that records it, so a reader can check that the shape
# below is the shape the record describes and not a specimen written to be caught.
KNOWN_INSTANCES = [
    {"id": "a", "record": "OPEN_ITEMS.md OI-286",
     "what": "a dispatch premise about a delivered refactor, refuted at the commit",
     "text": "Half (1) of the mandate is still owed and parked against retiring code."},
    {"id": "b", "record": "OPEN_ITEMS.md OI-288",
     "what": "a dispatch premise about a live code path, refuted at the control flow",
     "text": "The gate layer is reachable on the live notation arm through the tick-local fallback."},
    {"id": "c", "record": "OPEN_ITEMS.md OI-288, its own text correction",
     "what": "a retirement-map citation that says what the cited rows do not",
     "text": "R1/R5/R6 delete both of them."},
    {"id": "d", "record": "OPEN_ITEMS.md OI-281",
     "what": "a criterion released at document granularity when its evidence was at section granularity",
     "text": "A document is a contract home when it is of a kind that states rules."},
    {"id": "e", "record": "STATUS.md, the phase-1l entry",
     "what": "a ratified-marker count estimated rather than derived",
     "text": "The register carries thirty-odd ratification markers, so about 30 entries are affected."},
    {"id": "f", "record": "OPEN_ITEMS.md OI-289",
     "what": "a LEGACY-mark set size three surfaces of record state differently",
     "text": "The LEGACY-marked set is 75 entries."},
    {"id": "g", "record": "tools/audit/decisions/phase1m_measurements.json task6_reading_yield",
     "what": "a reading-coverage count carried forward for three waves",
     "text": "38 of 143 design documents have been read in full."},
    {"id": "h", "record": "tools/audit/decisions/phase1n_reading_regime.json proxy.ordering_decision",
     "what": "a comparison asserted without its uncertainty, against #24",
     "text": "The key is the strongest of the three proxies, at 0.745 against 0.61 and 0.58."},
]

# Control text: correct sentences that must NOT be flagged.  Drawn from the same corpus's
# compliant prose, so a false positive here is a real false positive.
CONTROL = [
    "The counts are at `tools/audit/decisions/phase1p_delegation_bar.json` → `pre_apply_check`.",
    "The record arm returns early at `notationcomposingbridge.cpp:737` whenever the flag is set.",
    "`ARCHITECTURE.md:319` delegates the licence-pool constraint to the census §8c.",
    "The register's size is `tools/audit/decisions/backbone_decisions.json` -> `decisions`.",
    "Both call sites are on the legacy arm (`regionanalyzer.cpp:921`, "
    "`notationcomposingbridge.cpp:651`).",
    "The user ruled this on 2026-08-03 and it is register entry D-430.",
    "Three surfaces were searched; each mention was then read in place.",
    "The dispatch was written before the check existed, so it is itself unchecked by it.",
]


def establish() -> dict:
    rows = []
    for inst in KNOWN_INSTANCES:
        f = check_text(inst["text"] + "\n\n## Self-check\n", "<known-" + inst["id"] + ">")
        f = [x for x in f if x["rule"] != "D-434 missing self-check section"]
        rows.append({**inst, "detected": bool(f),
                     "rules_fired": sorted({x["rule"] for x in f})})
    fp = []
    for i, s in enumerate(CONTROL):
        f = check_text(s + "\n\n## Self-check\n", f"<control-{i}>")
        f = [x for x in f if x["rule"] != "D-434 missing self-check section"]
        fp.append({"text": s, "flagged": bool(f),
                   "rules_fired": sorted({x["rule"] for x in f})})
    detected = sum(1 for r in rows if r["detected"])
    flagged = sum(1 for r in fp if r["flagged"])
    return {
        "purpose": "Establishment (#19) of tools/audit/process_check.py: its detection power "
                   "against the recorded instances the rule was ruled on, and its "
                   "false-positive rate on text that is correct. Nothing here is a claim; "
                   "every row carries the record it came from.",
        "known_instances": {
            "total": len(rows), "detected": detected,
            "detection_rate": round(detected / len(rows), 3),
            "rows": rows,
        },
        "control": {
            "total": len(fp), "flagged": flagged,
            "false_positive_rate": round(flagged / len(fp), 3),
            "rows": fp,
        },
        "control_reclassified_during_establishment": [
            {"text": "The register is 431 entries at "
                     "`tools/audit/decisions/backbone_decisions.json`.",
             "was": "written into the control set as correct text",
             "now": "REMOVED from the control set — the check was right about it. It "
                    "transcribes a quantity and cites a FILE but no FIELD, and D-431 requires "
                    "an artifact AND a field. Recorded rather than deleted quietly, because a "
                    "control set silently edited to make a check look better measures "
                    "nothing (#19)."},
        ],
        "what_this_measures": "The check reads TEXT. A premise that is WRONG but CITED is "
                              "invisible to it by construction, so the instances it misses are "
                              "the ones that arrived with a citation to a secondary surface. "
                              "The detection rate below is therefore a property of the failure "
                              "shapes, not a score to be improved by tuning the patterns — "
                              "tuning them to catch a specific specimen would measure nothing.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="dispatch or report files to check")
    ap.add_argument("--establish", action="store_true",
                    help="measure the check against the recorded instances and a control set")
    ap.add_argument("--check", action="store_true",
                    help="with --establish: regenerate into memory and diff the artifact; "
                         "with --json: regenerate the scan artifact and diff it")
    ap.add_argument("--json", metavar="PATH",
                    help="write the findings to PATH as a generated artifact, so a report "
                         "cites the file rather than transcribing the findings (D-431)")
    args = ap.parse_args()

    if args.establish:
        art = establish()
        text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            have = open(ESTABLISH_OUT, encoding="utf-8").read() \
                if os.path.exists(ESTABLISH_OUT) else ""
            if have != text:
                print("STALE vs the check: process_check_establishment.json does not re-derive")
                return 1
            print("the process-check establishment artifact re-derives")
            return 0
        open(ESTABLISH_OUT, "w", encoding="utf-8", newline="").write(text)
        k, c = art["known_instances"], art["control"]
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")
        print(f"  detection over the recorded instances: {k['detected']}/{k['total']}")
        for r in k["rows"]:
            print(f"    {r['id']}  {'DETECTED' if r['detected'] else 'MISSED  '}  {r['what']}")
        print(f"  false positives on correct text: {c['flagged']}/{c['total']}")
        for r in c["rows"]:
            if r["flagged"]:
                print(f"    FLAGGED: {r['text'][:90]}")
        return 0

    if not args.files:
        ap.error("give one or more files, or --establish")
    findings: list[dict] = []
    for f in args.files:
        path = f if os.path.isabs(f) else os.path.join(ROOT, f)
        if not os.path.exists(path):
            print(f"no such file: {f}")
            return 2
        findings += check_text(open(path, encoding="utf-8", errors="replace").read(), f)
    if args.json:
        by_file: dict[str, list[dict]] = {}
        for x in findings:
            by_file.setdefault(x["file"], []).append(x)
        art = {
            "purpose": "A run of tools/audit/process_check.py over named dispatches or "
                       "reports. Generated so a report cites this file rather than "
                       "transcribing what the check found (D-431).",
            "rules": ["D-431 bare quantity", "D-431 uncited code claim",
                      "D-434 missing self-check section"],
            "files_scanned": list(args.files),
            "findings_total": len(findings),
            "by_file": {f: {"findings": len(v), "rows": v} for f, v in by_file.items()},
            "clean_files": [f for f in args.files if f not in by_file],
            "establishment": "tools/audit/process_check_establishment.json — the check's "
                             "measured detection power and false-positive rate. Read it "
                             "before reading a count here as coverage.",
        }
        text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
        path = args.json if os.path.isabs(args.json) else os.path.join(ROOT, args.json)
        if args.check:
            have = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
            if have != text:
                print(f"STALE vs the files: {args.json} does not re-derive")
                return 1
            print(f"{args.json} re-derives")
            return 0
        open(path, "w", encoding="utf-8", newline="").write(text)
        print(f"wrote {args.json}: {len(findings)} finding(s) over {len(args.files)} file(s)")

    for x in findings:
        where = f"{x['file']}:{x['line']}" if x["line"] else x["file"]
        print(f"  {where}  [{x['rule']}]  {x['detail']}")
        if x["sentence"]:
            print(f"      {x['sentence']}")
    print(f"{len(findings)} finding(s) over {len(args.files)} file(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
