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
#
# THE UNIT LIST HAS ONE HOME (#6). Both the digit rule and the word rule below are built from
# it, so a unit added for one is a unit for the other and the two cannot drift apart.
UNIT = r"(%|pp\b|ticks\b|entries\b|entry\b|clusters\b|rows\b|documents\b|files\b|of\s+\d+)"

QUANTITY = re.compile(
    r"(?<![\w.#§:$-])"                       # not part of an identifier, a #ref, a §, a :line
    r"(\d{1,3}(?:[,   ]\d{3})+|\d+(?:\.\d+)?)"
    r""  # the class above holds four thousands separators this repository's prose uses:
    r""  # comma, narrow no-break space, no-break space, plain space. Superseded form follows: [,  , ]\d{3})+|\d+(?:\.\d+)?)"
    r"\s*" + UNIT + r"?"
)
# Numbers that are never a measured quantity in this project's prose.
NOT_A_QUANTITY = re.compile(
    r"^(?:19|20)\d{2}$"                      # a year
    r"|^\d{1,2}$"                            # small ordinals: "the 3 surfaces", "#5", "step 2"
)

# ── the same rule, for numbers written as words (added 2026-08-03, phase 1r) ──
# WHAT THIS CLOSES, and what it deliberately does not.  A count written `12 documents` is read
# by the digit rule; written `twelve documents` it was invisible, and nothing but the spelling
# differed.  That is a CLASS — the word forms of the rule already in force — so the word rule is
# built from the SAME unit list and carries the SAME exclusion: a spelled-out number with no
# recognized unit is ordinary prose ("one path per concern", "the three surfaces") and is not a
# quantity, exactly as `4` with no unit is not.
#
# WHAT IT IS NOT, stated because the reason it was asked for turns out to be wrong.  The
# phase-1r dispatch named `four local patches` as the specimen and gave SPELLING as the reason
# it was missed.  Measured, that diagnosis is refuted and the establishment artifact records it:
# the digit form `4 edits` is missed too, because the noun is not in the unit list and a small
# integer with no unit is excluded by construction.  Adding that noun would be tuning to the
# specimen, which this check's own establishment note forbids — so it is NOT added, and that
# miss stands as a stated blind spot rather than being closed by a special case.
NUMBER_WORD = (
    r"(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)[- ]"
    r"(?:one|two|three|four|five|six|seven|eight|nine)"
    r"|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety"
    r"|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen"
    r"|one|two|three|four|five|six|seven|eight|nine"
)
WORD_QUANTITY = re.compile(
    r"(?<![\w-])(" + NUMBER_WORD + r")\s+" + UNIT, re.I)

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


def bare_quantities(s: str, words: bool = True) -> list[str]:
    found = []
    if words:
        # A spelled-out number is a quantity only WITH a unit — the word analogue of the
        # small-ordinal exclusion below, and the whole of what the word rule adds.
        found += [m.group(0).strip() for m in WORD_QUANTITY.finditer(s)]
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


def check_text(text: str, name: str, words: bool = True) -> list[dict]:
    findings: list[dict] = []
    for line, s, is_heading in sentences(text):
        qs = [] if is_heading else bare_quantities(s, words=words)
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
    # ADDED 2026-08-03 (phase 1r), and it is a MEASURED FALSE POSITIVE, not a passing row.
    # The phase-1r dispatch's own §3 says this; it is an instruction about where edits landed,
    # not an assertion of a measured amount, and the check flags it because `files` is in the
    # unit list. It is recorded here rather than left out, because a control set chosen to make
    # a check look clean measures nothing (#19) — the same reason the row below was removed.
    "The insertions here are at three different depths in two files, so no single offset is "
    "correct anywhere.",
    # ADDED 2026-08-03 (phase 1s), and it is a SECOND MEASURED FALSE POSITIVE, recorded on the
    # same principle as the one above. The phase-1s dispatch's own §7 says this. `Task 2.3` is a
    # SECTION REFERENCE in a notation the check does not recognize: the quantity rule excludes
    # `§2.3` by its lookbehind on the section mark, and excludes a bare small integer by
    # construction, but a decimal-numbered cross-reference written without the mark is neither.
    # NOT closed by adding `Task` to an exclusion list — that is tuning to a specimen, which
    # `known_over_breadth_do_not_tune_it_away` forbids for the same reason in both directions.
    "**Task 2.3's fix reverting is an acceptable outcome** if it raises false denies.",
]


def _run(text: str, name: str, words: bool = True) -> list[dict]:
    f = check_text(text + "\n\n## Self-check\n", name, words=words)
    return [x for x in f if x["rule"] != "D-434 missing self-check section"]


# The word-form change is maintenance on a KEPT mechanism (D-436), so it is re-established
# rather than asserted: the same two sets are run with the word rule OFF and ON, and BOTH
# figures are published. A rise in the false-positive rate is the condition the phase-1r
# dispatch names for reverting it, so it must be visible and not inferred.
WORD_PROBE = [
    {"text": "Twelve documents yielded zero.", "should_flag": True,
     "why": "A measured count with a recognized unit, written as a word. The digit form "
            "`12 documents` is flagged; nothing but the spelling differs."},
    {"text": "The pass moved twenty-seven entries.", "should_flag": True,
     "why": "Same class, compound word form."},
    {"text": "One fix is designed once over the whole enumerated family, never per symptom.",
     "should_flag": False,
     "why": "`CLAUDE.md`'s own rule heading. A word number with no unit is ordinary prose."},
    {"text": "Three phases, strictly ordered.", "should_flag": False,
     "why": "`CLAUDE.md`'s own text. No unit, so not a quantity — as `3` with no unit is not."},
    {"text": "There are exactly two admissible confidence classes.", "should_flag": False,
     "why": "A rule, not a measurement; `classes` is not a unit."},
    {"text": "`CLAUDE.md` carries four edits to code this project does not own.",
     "should_flag": False,
     "why": "THE SPECIMEN THE DISPATCH NAMED, and the word rule does NOT catch it — `edits` "
            "is not in the unit list, so the DIGIT form is missed too. Recorded as a "
            "not-detected probe rather than closed by adding the noun, which would be tuning "
            "to the specimen."},
]


def establish() -> dict:
    rows = []
    for inst in KNOWN_INSTANCES:
        f = _run(inst["text"], "<known-" + inst["id"] + ">")
        rows.append({**inst, "detected": bool(f),
                     "rules_fired": sorted({x["rule"] for x in f})})
    fp = []
    for i, s in enumerate(CONTROL):
        f = _run(s, f"<control-{i}>")
        fp.append({"text": s, "flagged": bool(f),
                   "rules_fired": sorted({x["rule"] for x in f})})
    detected = sum(1 for r in rows if r["detected"])
    flagged = sum(1 for r in fp if r["flagged"])

    # the same two sets, with the word rule off — the before/after the dispatch requires
    off_known = sum(1 for i in KNOWN_INSTANCES if _run(i["text"], "<k>", words=False))
    off_ctrl = sum(1 for s in CONTROL if _run(s, "<c>", words=False))
    probe = [{**p,
              "flagged": bool(_run(p["text"], "<probe>")),
              "flagged_without_the_word_rule": bool(_run(p["text"], "<probe>", words=False))}
             for p in WORD_PROBE]
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
        "word_form_extension_2026_08_03": {
            "what_changed": "The bare-quantity rule now reads numbers written as WORDS as well "
                            "as digits, from the SAME unit list (one home, #6) and under the "
                            "SAME exclusion: a spelled-out number with no recognized unit is "
                            "ordinary prose, exactly as a small integer with no unit is.",
            "why_it_is_maintenance_and_not_tuning": "It closes a CLASS — every word form of a "
                                                    "rule already in force — rather than a "
                                                    "specimen. D-436 keeps a mechanism on "
                                                    "measured detection and a false-positive "
                                                    "rate at or near zero, so both are "
                                                    "re-measured here and published either way.",
            "the_dispatch_premise_is_REFUTED": "The phase-1r dispatch ordered this change on "
                                               "the ground that `four local patches` was missed "
                                               "BECAUSE it was spelled out. It was not: the "
                                               "digit form `4 edits` is missed too, because "
                                               "`edits` is not in the unit list and a small "
                                               "integer with no unit is excluded by "
                                               "construction. See the probe row whose "
                                               "`should_flag` is false and whose `why` says so. "
                                               "The noun was NOT added to the unit list — that "
                                               "would be tuning to the named specimen, which "
                                               "`what_this_measures` below forbids — so the "
                                               "specimen remains a stated blind spot.",
            "detection_over_the_recorded_instances": {
                "with_the_word_rule": detected, "without_it": off_known, "of": len(rows)},
            "false_positives_on_the_control_set": {
                "with_the_word_rule": flagged, "without_it": off_ctrl, "of": len(fp)},
            "the_false_positive_this_change_costs": "ONE, and it is published rather than "
                "designed around. The phase-1r dispatch's own §3 sentence — 'the insertions "
                "here are at three different depths in two files' — is flagged, because `files` "
                "is in the shared unit list. It was added to the control set when the check "
                "found it, so the rate above shows the rise. JUDGMENT, recorded as one: it is "
                "KEPT. The false positive is not a class the word rule introduces — the DIGIT "
                "form `in 2 files` is flagged identically by the rule already in force, so "
                "reverting the word rule would not remove the false positive, only make the "
                "check disagree with itself about how a number is spelled. The condition the "
                "dispatch set for reverting is a MATERIAL rise; one instance, whose cause "
                "pre-dates the change, is reported as not material and is left for the user to "
                "overrule.",
            "probe": probe,
            "the_user_ruled_on_it_2026_08_03": "KEPT, and the ground adopted is the one given "
                "above: the DIGIT form is flagged identically, so reverting the word rule would "
                "not remove the false positive — it would only make the check disagree with "
                "itself about how a number is spelled. The rates are published either way "
                "(phase 1s, ruling Y4).",
        },
        "known_over_breadth_do_not_tune_it_away": {
            "what_it_is": "The bare-quantity rule flags a STRUCTURAL DESCRIPTION that happens "
                          "to carry a number and a unit noun — 'the insertions are at three "
                          "different depths in two files' — as a bare quantity. The check is "
                          "not wrong about it: D-431's letter makes a count with a unit a "
                          "quantity, and 'two files' is one.",
            "why_it_is_recorded_here": "So a later session does not read it as a defect and "
                                       "close it by adding a noun allowlist, or by removing "
                                       "`files` from the unit list. Either would be TUNING TO "
                                       "A SPECIMEN, which `what_this_measures` below forbids "
                                       "for the same reason in the other direction: a pattern "
                                       "adjusted until a particular sentence stops firing "
                                       "measures that sentence and nothing else.",
            "the_user_ruled_it_ACCEPTED_2026_08_03": "The word rule is kept, both rates are "
                                                     "published, and the one control false "
                                                     "positive stands as a known property of "
                                                     "the check rather than a defect to design "
                                                     "around (phase 1s, ruling Y4). The "
                                                     "control row is in `control` above, "
                                                     "flagged, so the published "
                                                     "false-positive rate INCLUDES it.",
            "a_second_class_measured_2026_08_03": "A SECTION REFERENCE written without the "
                "section mark — `Task 2.3` — is read as a bare quantity. The mark itself is "
                "excluded by the quantity rule's lookbehind and a bare small integer is "
                "excluded by construction, so this is the one cross-reference notation that "
                "falls between them. Found by running the check over the phase-1s dispatch, "
                "added to the control set so the published rate includes it, and NOT closed by "
                "special-casing the word — for the same reason as above, in the same "
                "direction.",
            "what_would_legitimately_change_it": "A rule change ruled on its own merits — for "
                                                 "instance, if D-431 were amended to exempt "
                                                 "structural descriptions from the quantity "
                                                 "rule. That is a ruling about the RULE, not a "
                                                 "pattern edit, and it would arrive with its "
                                                 "own re-establishment under D-436.",
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
