#!/usr/bin/env python3
"""THE RATIFIED-DOCUMENT SUBJECT CHECK — for the 62 entries whose recovered act points at a
document ratification, is the entry's own subject actually IN the document that was ratified?

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §3(B2) of
`cowork_rulings_2026_08_16_preparation_return.md`: *"The 62 remaining ACT-FOUND entries are NOT
ruled — one further bounded derivation first: for each entry whose recovered act is a
document-ratification passage, the RATIFIED DOCUMENT ITSELF is checked for the entry's subject
recognizers (the register's own, again); subject found and quoted, or not found. The 62 are ruled
at that return, the sole-carrier guard applying to their eventual residue."*

★ WHY THE QUESTION IS WORTH ASKING.  The deciding-act recovery pass found, for 72 entries, a
passage in a document the entry itself cites that carries a user-act marker AND matches the entry's
own subject recognizers.  Ten of those are clear recoveries and the user KEPT them.  Among the
other 62, a recognizable shape appears: the recovered passage is a passage in which the user
ratified a WHOLE DOCUMENT, and it matched the entry's subject recognizers only because those words
happen to appear in the ratifying sentence.  Such a passage is evidence for the entry only if the
document that was ratified actually carries the entry's subject.  This derivation asks that, once,
mechanically.

★ IT PROPOSES NOTHING AND IT RULES NOTHING.  No entry is retired, edited, moved or marked; the
decisions register's data file and every file rendered from it are untouched by this tool, which
opens them for reading and writes only its own artifact and the residue surface.  The 62 are ruled
by the user at this return, over this evidence.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   the population — the recovery pass's ACT-FOUND entries MINUS the ten the user's own
            B1 ruling KEPT, both imported and neither hand-listed (#6, D-671); every recovered act,
            imported from the committed recovery artifact; every passage, re-read from the document
            at the measured commit and cross-checked against the quote the recovery pass published;
            every named document, extracted from the passage itself; every subject match, quoted
            with its span; every count.
  AUTHORED  what makes a passage a DOCUMENT RATIFICATION — the ratification words and the demand
            that the passage also name a document — and nothing else.  It is published in the
            artifact beside the results it produced.

★ HOW AN ENTRY'S SUBJECT IS RECOGNISED, and why nothing here is invented.  The decisions register
carries, per entry, a `patterns` list — its OWN recognizers for that entry's subject, authored when
the entry was written.  Those, with the entry's identity, are what a ratified document must match.
This is the same test the recovery pass used, which is what the ruling asks for in its own words:
*"the entry's subject recognizers (the register's own, again)"*.

★ THE DOCUMENT THE ACT ITSELF SITS IN IS NOT SEARCHED, and the reason is not a bound but a
duplication.  The recovery pass already searched exactly that document and reported what it found;
searching it again here would republish the recovery pass's own finding as if it were new evidence.
What is searched is every OTHER document the ratifying passage names.

THE STOPS, so this cannot silently stop being an enumeration:
  * the committed recovery artifact missing, or carrying no ACT-FOUND entry, STOPS it;
  * the ten B1 keeps not being locatable in the ruling record, or not numbering ten, or naming an
    entry the recovery pass did not return ACT-FOUND for, STOPS it — the population may not be
    hand-listed and may not be silently wrong;
  * an entry missing a field this pass reads STOPS it — never a skip;
  * a result outside the closed three-value vocabulary STOPS it;
  * a distribution that does not account for the population STOPS it;
  * a sentence of the ruling that ordered this derivation no longer in its ruling record STOPS it,
    so the derivation cannot outlive the words that ordered it.
Each is exercised by a probe recorded in the artifact, and every probe calls the very function the
walk calls, so the two cannot drift apart.

★ THE SURFACE'S BANNER CARRIES ITS RULED STATE, WRITTEN HERE RATHER THAN BY HAND (2026-08-18, on
the user's Ruling 2 of `cowork_rulings_2026_08_18_tenth_return.md`; executed by
`cc_instruction_preparation_eleventh_amended.md` Task 3).  The surface said of itself that nothing
on it was ruled, and it had been ruled — at the residue sitting of 2026-08-17.  **THE TREATMENT IS
IMPORTED FROM `tools/audit/gen_rulings_sort.py` (#6), which already carries it**: the qualification
is written at the GENERATOR and rendered into the document in the same act, and the former banner
text is preserved beside it (#12) with the former rendering left standing in git.  It is written at
the generator and not at the file because a hand edit to a generated document is not durable by
construction — the fourth surface's own correction survived one regeneration only by accident of what
that regeneration moved.

★ WHY THIS IS ADMISSIBLE UNDER THE STANDING MECHANISM FREEZE, answered at the site rather than
assumed away.  The freeze bars tool work that does not block the work.  **A governing surface stating
something false about itself is #10's own doc-truth subject**, not apparatus polish; and this act
creates NO new mechanism, because the treatment is imported from a tool that already carries it.

Run:
  python tools/audit/gen_ratified_document_check.py           # write the artifact and the surface
  python tools/audit/gen_ratified_document_check.py --check   # re-derive both, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
RECOVERY = "tools/audit/deciding_act_recovery.json"
SOLE_CARRIER = "tools/audit/sole_carrier_subclass.json"
BACKBONE = "tools/audit/decisions/backbone_decisions.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
RULING_PATH = "cowork_rulings_2026_08_16_preparation_return.md"
OUT = ROOT / "tools" / "audit" / "ratified_document_check.json"
SURFACE = (ROOT / "ratification_surfaces"
           / "cowork_discard_residue_surface_2026_08_16.md")

ACT_FOUND = "ACT-FOUND"
NOTHING_FOUND = "NOTHING-FOUND"

IN_RATIFIED = "SUBJECT-IN-RATIFIED-DOCUMENT"
NOT_FOUND_THERE = "SUBJECT-NOT-FOUND-THERE"
NO_RATIFICATION = "NO-DOCUMENT-RATIFICATION-ACT"
RESULTS = (IN_RATIFIED, NOT_FOUND_THERE, NO_RATIFICATION)

REQUIRED_FIELDS = ("id", "group", "title", "plain", "home", "status", "patterns")

# ★ THE ONE ROUTE THAT REACHED THE RENDERING FROM THE LIVE TREE IS PINNED — the EVIDENCE PIN's ruled
# class, applied to this member (`cc_instruction_preparation_eleventh_amended.md` Task 1, executing
# Ruling 1 of `cowork_rulings_2026_08_18_tenth_return.md` at the derivation Ruling 3 of
# `cowork_rulings_2026_08_18_eleventh_stop.md` sharpened).
#
# WHAT WAS ALREADY PINNED, AND WHAT WAS NOT.  Every JSON input this pass reads — the recovery
# artifact, the sole-carrier artifact, the decisions register's data file — and every document it
# searches are already read at the commit the committed artifact RECORDS, and `--check` re-derives
# there.  ONE route was not: the (B1) bullet the population is PARSED from was read from the
# WORKING-TREE ruling record, so an edit to that record could move both the artifact and the ruling
# surface generated from it.  That is the class rule's own hazard: *a document generated from a live
# data file is not evidence of what was PUT in front of the user unless its generation is PINNED.*
#
# ★ THE PIN IS DELIBERATELY NARROW, AND THE HALF IT DOES NOT TOUCH IS THE POINT.  `locate_ruling`
# still reads the ruling record AS IT STANDS on every run, and still STOPs when a sentence that
# ordered this derivation is no longer there.  Pinning that read too would have destroyed a LIVE
# guard the record values — the pass would then be unable to notice that the words permitting it had
# gone — so the pin fixes WHAT THE RENDERING READS and leaves WHAT THE PASS ASSERTS live.
#
# ★ WHAT THE PIN DOES NOT FREEZE.  The ruling record itself is not frozen: it is corrected by
# APPENDING, as this batch's own dated correction to it does, and every such correction is visible to
# the live assertion above.  A LATER RULING CAN UNPIN THIS MEMBER IN ONE EDIT.
RULING_PINNED_AT = "81e2ef1c2376e4dc7a5c69c62b188676239091f1"
RULING_PINNED_AT_IS = (
    "the commit the residue sitting was ruled at, DERIVED at the git objects under the "
    "landing-commit bound: the last commit touching "
    "`ratification_surfaces/cowork_discard_residue_surface_2026_08_16.md` dated at or before the "
    "commit that landed `cowork_rulings_2026_08_17_residue_sitting.md` in git — and the only "
    "commit that has ever touched that document")

# AUTHORED: what makes a passage a DOCUMENT RATIFICATION. Published beside every result.
RATIFICATION_WORDS = re.compile(
    r"\bratif(?:y|ies|ied|ication|ications)\b|\badopt(?:s|ed|ion)?\b|\bRULED\b|"
    r"\brule[sd]?\s+on\b|\bruling\s+on\b|\baccept(?:s|ed|ance)?\b|\bapprove[sd]?\b|"
    r"\bsign(?:ed)?[- ]off\b|\buser-ratified\b|\buser ratified\b", re.I)
DOCUMENT_NAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-/]*\.md")
SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+")

WHAT_MAKES_A_PASSAGE_A_DOCUMENT_RATIFICATION = (
    "A document is RATIFIED BY THE ACT when it is NAMED IN A SENTENCE OF THE PASSAGE THAT ALSO "
    "CARRIES A RATIFICATION WORD. The sentence, and not the whole passage, is the unit — and the "
    "narrowing is the point of this derivation rather than a refinement of it. The ruling asks "
    "what THE RATIFIED DOCUMENT says; a passage often names several documents, most of them "
    "mentioned rather than ratified, so admitting every name in the passage would send the search "
    "to documents the act never ratified and report their contents as if the act had ratified "
    "them. ★ WHAT THE WIDER READING WOULD HAVE ADMITTED IS NOT DISCARDED: every document named "
    "elsewhere in the passage is published per act, by name and counted, so the difference between "
    "the two readings is visible and a reader can ask for either. ★ WHERE THE NARROW READING IS "
    "STILL WIDE: any ratification word beside any document name inside one sentence admits it, "
    "which will call some sentences ratifications that a reader would not. That direction is the "
    "harmless one — a wrongly admitted document is then SEARCHED and reports either a subject "
    "match, which is evidence a reader can check at the quoted line, or SUBJECT-NOT-FOUND-THERE, "
    "which claims nothing. ★ WHERE IT IS DELIBERATELY NARROW AND THE LIMIT IS NAMED RATHER THAN "
    "PATCHED: a sentence ratifying a SECTION without naming its document is NOT admitted, because "
    "the document it would send the search to is the one the act already sits in, and that "
    "document was searched by the recovery pass. Such an act is counted and published below "
    "rather than silently dropped."
)

# AUTHORED: the sentences of the ruling this pass serves, LOCATED in its record on every run.
RULING_SENTENCES = {
    "what was ordered":
        "for each entry whose recovered act is a document-ratification passage, the RATIFIED "
        "DOCUMENT ITSELF is checked for the entry's subject recognizers (the register's own, "
        "again); subject found and quoted, or not found",
    "the 62 are not ruled yet":
        "The 62 remaining ACT-FOUND entries are NOT ruled",
    "the guard applies to their residue":
        "The 62 are ruled at that return, the sole-carrier guard applying to their eventual "
        "residue.",
    "the ten kept":
        "The ten clear recoveries are KEPT",
    "what a discard record must carry":
        "a provenance verdict, not a judgment on soundness or usefulness; the statement stands at "
        "its home and is met by the derivation",
    "what a sole-carrier member does not do":
        "Sole-carrier members do NOT ride the discard — they return to the user as a list",
}

# The bullet the ten B1 keeps are named in. The list is PARSED from it, never typed here.
B1_BULLET = re.compile(r"\(B1\)[^\n]*(?:\n(?!\s*-\s)[^\n]*)*")


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning, never an entry skipped."""


# ── git, by explicit hash ────────────────────────────────────────────────────────────────────────

def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def resolve(rev: str) -> str:
    sha = git("rev-parse", rev).strip()
    if len(sha) != 40:
        raise Stop(f"{rev} did not resolve to a full commit identity: {sha!r}")
    return sha


def tree_paths(commit: str) -> dict[str, str]:
    """Every BLOB of the named commit's tree, path to object identity."""
    out: dict[str, str] = {}
    for line in git("ls-tree", "-r", commit).split("\n"):
        if not line.strip():
            continue
        meta, path = line.split("\t", 1)
        _mode, kind, sha = meta.split()
        if kind == "blob":
            out[path.strip('"')] = sha
    return out


def blob_text(sha: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), "cat-file", "blob", sha], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"the blob {sha} could not be read from the git object store")
    return proc.stdout.decode("utf-8", "replace")


def json_at(commit: str, path: str, what: str) -> dict:
    """One of this pass's inputs, read AT THE MEASURED COMMIT and never from the tree.

    The same ground the sole-carrier guard states: the soft-discard this evidence is gathered for
    MOVES the decisions register and every artifact derived from it, so an input read live would be
    changed by the act the evidence is gathered for (#12; the OI-301 hazard). The LIVE assertion
    this pass carries is the ruling record, read as it stands on every run.
    """
    try:
        raw = git("show", f"{commit}:{path}")
    except Stop:
        raise Stop(f"{what} is not in the tree at the measured commit {commit[:10]}: {path}")
    return json.loads(raw)


# ── the checks that halt this pass ───────────────────────────────────────────────────────────────

def flatten(text: str) -> str:
    """Emphasis marks dropped and whitespace collapsed, so a quote survives line wrapping."""
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def one_line(text: str) -> str:
    """A passage collapsed to one line, with markdown quote marks stripped, and NOT truncated."""
    lines = [re.sub(r"^\s*>+\s?", "", line) for line in text.splitlines()]
    return " ".join(" ".join(lines).split())


def readable(text: str, width: int = 900) -> str:
    """`one_line` truncated — the recovery pass's own shape, so a re-read block can be compared
    with the quote that pass published."""
    return one_line(text)[:width]


def ruling_text() -> str:
    """The ruling record AS IT STANDS. Live on purpose — see `RULING_PINNED_AT`."""
    if not RULING.exists():
        raise Stop(f"the ruling record this pass serves is missing: {RULING}")
    return RULING.read_text(encoding="utf-8")


def pinned_ruling_text() -> str:
    """The ruling record AS THE RULED SURFACE WAS GENERATED FROM IT, read at the git object.

    A content-addressed read by explicit hash — the one shell mechanism the standing rule permits —
    so the population this pass parses, and the surface generated from it, cannot be moved by a
    later edit to the record. The reason is at `RULING_PINNED_AT` above.
    """
    try:
        return git("show", f"{RULING_PINNED_AT}:{RULING_PATH}")
    except Stop:
        raise Stop(f"the pinned ruling record could not be read at "
                   f"{RULING_PINNED_AT[:10]}:{RULING_PATH}")


def locate_ruling(raw: str) -> dict[str, str]:
    text = flatten(raw)
    missing = [name for name, quote in RULING_SENTENCES.items() if flatten(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling that ordered this derivation is no longer in its "
                   f"ruling record, so the derivation would outlive the words that ordered it: "
                   f"{missing}")
    return dict(RULING_SENTENCES)


def b1_keeps(raw: str, act_found: set[str]) -> tuple[list[str], str]:
    """The ten entries the user's B1 ruling KEPT — PARSED from the ruling record, never typed."""
    match = B1_BULLET.search(raw)
    if not match:
        raise Stop("the ruling record carries no (B1) bullet, so the ten keeps cannot be imported "
                   "and the population of this pass cannot be derived")
    bullet = match.group(0)
    kept = sorted(set(re.findall(r"\bD-\d+\b", bullet)))
    if len(kept) != 10:
        raise Stop(f"the (B1) bullet names {len(kept)} register entries where the ruling says TEN: "
                   f"{kept}. The population is not hand-corrected — this halts.")
    stray = sorted(k for k in kept if k not in act_found)
    if stray:
        raise Stop(f"the (B1) bullet names {stray}, which the recovery pass did not return "
                   f"ACT-FOUND for. The two records disagree about the population and this pass "
                   f"does not choose between them.")
    return kept, flatten(bullet).strip()


def require_fields(entry: dict) -> None:
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        raise Stop(f"entry {entry.get('id', '<no identity>')!r} carries no {missing} — the check "
                   f"cannot be run for it, and an entry it cannot read at all is a STOP rather "
                   f"than a skip")


def require_reconciled_distribution(rows: list[dict], population_size: int) -> None:
    if len(rows) != population_size:
        raise Stop(f"the checked rows ({len(rows)}) do not account for the population "
                   f"({population_size})")
    unknown = sorted({r["result"] for r in rows} - set(RESULTS))
    if unknown:
        raise Stop(f"a result outside this pass's closed three-value vocabulary: {unknown}")
    per = {r: sum(1 for row in rows if row["result"] == r) for r in RESULTS}
    if sum(per.values()) != population_size:
        raise Stop("the per-result distribution does not account for the population")


# ── the walk ─────────────────────────────────────────────────────────────────────────────────────

def subject_matchers(entry: dict) -> tuple[list[tuple[str, re.Pattern]], list[str]]:
    """The entry's OWN subject recognizers: its identity, and the decisions register's `patterns`."""
    matchers: list[tuple[str, re.Pattern]] = [
        ("the entry's own identity", re.compile(re.escape(entry["id"])))]
    unusable: list[str] = []
    for pattern in entry.get("patterns") or []:
        try:
            matchers.append((f"the decisions register's own recogniser `{pattern}`",
                             re.compile(pattern, re.I)))
        except re.error as exc:
            unusable.append(f"{pattern!r} — {exc}")
    return matchers, unusable


def passage_of(act: dict, paths: dict[str, str], text_cache: dict[str, str]) -> dict:
    """The act's passage, RE-READ from its document at the measured commit and cross-checked.

    The recovery pass recorded a document, a line and a span, and quoted the passage truncated. A
    document can have moved under those coordinates since, so the re-read block is compared with
    the quote that pass published; where the two disagree the coordinate is reported as no longer
    resolving and the PUBLISHED QUOTE is used, which is the evidence the record actually carries.
    """
    document, line, span = act["document"], act["line"], act["the_passage_spans_lines"]
    recorded = act["the_act_quoted"]
    if document not in paths:
        return {"text": recorded, "coordinate_still_resolves": False,
                "why": "the document the act was found in is not in the tree at the measured "
                       "commit; the quote the recovery pass published is used instead"}
    if document not in text_cache:
        text_cache[document] = blob_text(paths[document])
    lines = text_cache[document].splitlines()
    block = "\n".join(lines[line - 1:line - 1 + span])
    if readable(block, width=len(recorded)) == recorded:
        return {"text": block, "coordinate_still_resolves": True, "why": ""}
    return {"text": recorded, "coordinate_still_resolves": False,
            "why": f"the block at `{document}` line {line} no longer reads as the quote the "
                   f"recovery pass published; that published quote is used instead, and this act "
                   f"is counted among the coordinates that no longer resolve"}


def check(entry: dict, recovery_row: dict, paths: dict[str, str],
          text_cache: dict[str, str]) -> dict:
    matchers, unusable = subject_matchers(entry)
    acts_out: list[dict] = []
    dangling: list[dict] = []
    matches: list[dict] = []
    section_only = 0

    for act in recovery_row["acts"]:
        passage = passage_of(act, paths, text_cache)
        text = one_line(passage["text"])
        has_words = bool(RATIFICATION_WORDS.search(text))

        ratified: list[str] = []
        for sentence in SENTENCE_BOUNDARY.split(text):
            if not RATIFICATION_WORDS.search(sentence):
                continue
            for name in DOCUMENT_NAME.findall(sentence):
                if name != act["document"] and name not in ratified:
                    ratified.append(name)
        elsewhere = [n for n in dict.fromkeys(DOCUMENT_NAME.findall(text))
                     if n != act["document"] and n not in ratified]
        named = ratified
        is_ratification = bool(ratified)
        if has_words and not ratified:
            section_only += 1

        searched: list[dict] = []
        for name in named:
            if name not in paths:
                dangling.append({"the_name_quoted": name,
                                 "named_in": f"{act['document']} line {act['line']}"})
                searched.append({"the_ratified_document": name, "located": False})
                continue
            if name not in text_cache:
                text_cache[name] = blob_text(paths[name])
            hit = None
            for label, pattern in matchers:
                found = pattern.search(text_cache[name])
                if found:
                    where = text_cache[name].count("\n", 0, found.start()) + 1
                    hit = {"what_matched_the_subject": label,
                           "the_matched_text": found.group(0),
                           "at_line": where,
                           "the_passage_quoted": readable(
                               "\n".join(text_cache[name].splitlines()[where - 1:where + 4]))}
                    break
            searched.append({"the_ratified_document": name, "located": True,
                             "subject_found": hit is not None, "the_match": hit})
            if hit is not None:
                matches.append({"the_ratified_document": name, **hit})

        acts_out.append({
            "the_act_is_at": f"{act['document']} line {act['line']}",
            "the_passage_spans_lines": act["the_passage_spans_lines"],
            "coordinate_still_resolves": passage["coordinate_still_resolves"],
            "note_about_the_coordinate": passage["why"],
            "carries_a_ratification_word": has_words,
            "the_documents_this_act_ratifies": ratified,
            "documents_named_elsewhere_in_the_passage_and_NOT_searched": elsewhere,
            "★_what_the_second_list_is":
                "documents the passage mentions outside any sentence carrying a ratification word. "
                "The wider reading would have searched these too; they are published so the "
                "difference between the two readings is visible rather than silently taken.",
            "is_a_document_ratification": is_ratification,
            "the_act_quoted": readable(text),
            "the_documents_searched": searched,
        })

    ratifying = [a for a in acts_out if a["is_a_document_ratification"]]
    if not ratifying:
        result = NO_RATIFICATION
        why = ("none of this entry's recovered acts ratifies, rules on or adopts a document other "
               "than the one the act itself sits in, so there is no ratified document to check; "
               "the recovery pass's own evidence stands unchanged and unqualified by this pass")
    elif matches:
        result = IN_RATIFIED
        why = ("a document the recovered act ratifies carries this entry's own subject recogniser, "
               "quoted and located below — which is what would make a document-level ratification "
               "evidence about THIS entry rather than about the document as a whole")
    else:
        result = NOT_FOUND_THERE
        why = ("the recovered act ratifies a document, that document was located and searched with "
               "this entry's own subject recognizers, and none of them matches anywhere in it")

    return {
        "id": entry["id"],
        "group": entry["group"],
        "title": entry["title"],
        "home": entry["home"],
        "status": entry["status"],
        "what_the_entry_says_the_decision_is_quoted_from_the_register": entry["plain"],
        "the_class_the_filter_proposed": recovery_row["the_class_the_filter_proposed"],
        "result": result,
        "why_this_result": why,
        "acts_the_recovery_pass_recorded": len(recovery_row["acts"]),
        "acts_that_are_document_ratifications": len(ratifying),
        "acts_carrying_a_ratification_word_but_ratifying_no_document_other_than_their_own":
            section_only,
        "documents_the_wider_reading_would_have_searched_and_this_one_did_not": sorted(
            {name for act in acts_out
             for name in act["documents_named_elsewhere_in_the_passage_and_NOT_searched"]}),
        "the_subject_matches_found_in_ratified_documents": matches,
        "ratified_documents_that_could_not_be_located": dangling,
        "subject_recognisers_the_register_carries_that_would_not_compile": unusable,
        "acts": acts_out,
    }


# ── probes (#19) ─────────────────────────────────────────────────────────────────────────────────

def probes() -> list[dict]:
    out: list[dict] = []

    def probe(name: str, what: str, fn) -> None:
        try:
            fn()
        except Stop as exc:
            out.append({"probe": name, "what_was_fed": what, "raised": True, "message": str(exc)})
            return
        out.append({"probe": name, "what_was_fed": what, "raised": False,
                    "message": "NO STOP — this probe FAILED to establish its stop"})

    probe("a missing field", "an entry carrying every required field but `patterns`",
          lambda: require_fields({f: "x" for f in REQUIRED_FIELDS if f != "patterns"}))
    probe("a (B1) bullet naming the wrong number of entries",
          "a bullet naming D-001 and D-002 where the ruling says ten",
          lambda: b1_keeps("- (B1) The ten clear recoveries are KEPT — D-001, D-002.\n",
                           {"D-001", "D-002"}))
    probe("a (B1) keep the recovery pass did not return ACT-FOUND for",
          "a bullet naming ten entries of which one is not ACT-FOUND",
          lambda: b1_keeps("- (B1) KEPT — D-001, D-002, D-003, D-004, D-005, D-006, D-007, "
                           "D-008, D-009, D-010.\n",
                           {f"D-{n:03d}" for n in range(1, 10)}))
    probe("no (B1) bullet at all", "a ruling record carrying no (B1) bullet",
          lambda: b1_keeps("nothing here names the keeps\n", set()))
    probe("a result outside the closed vocabulary", "one row carrying the result 'INVENTED'",
          lambda: require_reconciled_distribution([{"result": "INVENTED"}], 1))
    probe("a distribution that does not account for the population",
          "one checked row against a population of two",
          lambda: require_reconciled_distribution([{"result": IN_RATIFIED}], 2))
    probe("a ruling sentence no longer in the ruling record",
          "a ruling record whose text is a single unrelated line",
          lambda: locate_ruling("this record no longer carries the ruling"))

    failed = [p["probe"] for p in out if not p["raised"]]
    if failed:
        raise Stop(f"a probe did not raise, so a STOP this tool claims cannot be shown to fire: "
                   f"{failed}")
    return out


# ── the build ────────────────────────────────────────────────────────────────────────────────────

def build(commit: str) -> tuple[dict, str]:
    raw_ruling = ruling_text()
    ruling = locate_ruling(raw_ruling)

    recovered = json_at(commit, RECOVERY, "the committed recovery artifact")
    by_recovery = {row["id"]: row for row in recovered["entries"]}
    act_found = {i for i, row in by_recovery.items() if row["result"] == ACT_FOUND}
    if not act_found:
        raise Stop("the committed recovery artifact carries no ACT-FOUND entry, so there is no "
                   "population for this pass — the import is not what it assumes it is")

    # The population is parsed from the PINNED record; the assertion above is taken on the LIVE one.
    kept, kept_quoted = b1_keeps(pinned_ruling_text(), act_found)
    population = sorted(act_found - set(kept))

    data = json_at(commit, BACKBONE, "the decisions register's data file")
    by_id: dict[str, dict] = {}
    for entry in data["decisions"]:
        by_id[entry["id"]] = entry
    absent = sorted(i for i in population if i not in by_id)
    if absent:
        raise Stop(f"the population names {absent}, which the decisions register's data file does "
                   f"not carry at the measured commit")
    for entry_id in population:
        require_fields(by_id[entry_id])

    guard = json_at(commit, SOLE_CARRIER, "the committed sole-carrier artifact")

    paths = tree_paths(commit)
    text_cache: dict[str, str] = {}
    rows = [check(by_id[i], by_recovery[i], paths, text_cache) for i in population]
    require_reconciled_distribution(rows, len(population))

    distribution = {r: sum(1 for row in rows if row["result"] == r) for r in RESULTS}
    drifted = sorted({row["id"] for row in rows
                      for act in row["acts"] if not act["coordinate_still_resolves"]})

    artifact = {
        "what_this_is":
            "THE RATIFIED-DOCUMENT SUBJECT CHECK. For the 62 ACT-FOUND entries the user's ruling of "
            "2026-08-16 §3(B2) did NOT rule, each recovered act is established as a document "
            "ratification or not, and where it is, the RATIFIED DOCUMENT is searched for that "
            "entry's own subject recognizers. NOTHING IS RULED, DISCARDED, RETIRED, EDITED OR "
            "MARKED BY THIS TOOL, and the decisions register's files are untouched by it.",
        "generator": "tools/audit/gen_ratified_document_check.py",
        "dispatch": "cc_instruction_preparation_third.md, Task 2",
        "derived_at_commit": commit,
        "★_why_the_commit_is_recorded":
            "Every input and every document this pass reads is taken at THIS commit, from the git "
            "objects by explicit hash, and `--check` re-derives there rather than at whatever the "
            "head happens to be. The soft-discard this evidence is gathered for MOVES the "
            "decisions register and the artifacts derived from it, so an input read live would be "
            "changed by the act the evidence is gathered for (#12; the OI-301 hazard). What is "
            "read LIVE is the ruling record — both the sentences that ordered this derivation and "
            "the bullet the population is parsed from.",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §3 (B2)",
            "every_sentence_located_in_that_record_on_this_run": ruling,
            "★_the_clause_that_binds_the_discard_ruling_when_it_is_put":
                ruling["what a discard record must carry"],
        },
        "the_population": {
            "★_how_it_is_derived_and_never_hand_listed":
                "The recovery pass's ACT-FOUND entries, MINUS the ten the user's own (B1) ruling "
                "KEPT. The first side is imported from the committed recovery artifact; the second "
                "is PARSED from the (B1) bullet of the ruling record itself, and a bullet naming "
                "any number other than ten, or naming an entry the recovery pass did not return "
                "ACT-FOUND for, halts this pass rather than being corrected (D-671).",
            "act_found_entries": len(act_found),
            "the_ten_the_B1_ruling_kept": kept,
            "the_B1_bullet_quoted_from_the_ruling_record": kept_quoted,
            "entries_checked_here": len(population),
            "the_entries_checked_here": population,
        },
        "what_is_DERIVED": [
            "the population, imported and parsed, never hand-listed",
            "every recovered act, imported from the committed recovery artifact",
            "every passage, re-read from its document at the measured commit and cross-checked "
            "against the quote the recovery pass published",
            "every document name, extracted from the passage itself",
            "every subject match, quoted with the line it was found at",
            "every count and every distribution",
        ],
        "what_is_AUTHORED": [
            "what makes a passage a document ratification — published in full below",
        ],
        "the_rule": {
            "what_makes_a_passage_a_document_ratification":
                WHAT_MAKES_A_PASSAGE_A_DOCUMENT_RATIFICATION,
            "the_ratification_words": RATIFICATION_WORDS.pattern,
            "the_document_name_pattern": DOCUMENT_NAME.pattern,
            "★_how_a_subject_is_recognised":
                "By the entry's own identity and by the `patterns` list the decisions register "
                "carries for that entry — the register's OWN recognizers, authored when the entry "
                "was written. The ruling asks for exactly this in its own words: the entry's "
                "subject recognizers, the register's own, again.",
            "★_the_document_the_act_sits_in_is_not_searched":
                "Not a bound but a duplication: the recovery pass already searched that document "
                "and published what it found there. Searching it again here would republish that "
                "finding as if it were new evidence.",
            "the_result_vocabulary": {
                IN_RATIFIED: "a document the recovered act ratifies carries this entry's own "
                             "subject recogniser. The document is named and the passage quoted.",
                NOT_FOUND_THERE: "the act ratifies a document, that document was located and "
                                 "searched, and no recogniser of this entry matches in it.",
                NO_RATIFICATION: "none of the entry's recovered acts ratifies a document other "
                                 "than the one it sits in, so there was nothing further to check.",
            },
        },
        "★_what_a_result_here_is_NOT": {
            "a_SUBJECT_IN_RATIFIED_DOCUMENT_is_not_a_verdict":
                "It is evidence that a document-level ratification reaches this entry's subject. "
                "Whether that makes the act a DECIDING act for this entry is the user's reading.",
            "a_SUBJECT_NOT_FOUND_THERE_is_not_a_finding_that_the_entry_was_never_decided":
                "It says the ratified document does not carry the entry's own recognizers. An act "
                "recorded somewhere neither the entry nor this pass reaches is outside it by "
                "construction.",
            "a_NO_DOCUMENT_RATIFICATION_ACT_is_not_a_weakening":
                "It says the shape this derivation was ordered to test is not present. The "
                "recovery pass's evidence for such an entry stands exactly as it stood.",
            "nothing_here_grades_a_decision":
                "Not its content, not its conformance, not whether the code obeys it — and nothing "
                "here is a judgment on soundness or usefulness.",
        },
        "the_distribution": distribution,
        "acts_whose_recorded_coordinates_no_longer_resolve": {
            "★_why_this_is_published":
                "The recovery pass recorded a document, a line and a span. A document can move "
                "under those coordinates, and reading whatever now sits at a line would silently "
                "grade the wrong passage. Every re-read block is therefore compared with the quote "
                "that pass published; where they disagree the published quote is used and the "
                "entry is named here.",
            "entries": drifted,
            "count": len(drifted),
        },
        "the_stops_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not":
                "They establish that each STOP CAN fire, each through the very function the walk "
                "calls, so the two cannot drift apart. They establish NOTHING about whether any "
                "entry's result is right — that is what the residue surface puts to the user.",
            "probes": probes(),
        },
        "entries": rows,
    }
    return artifact, render_surface(artifact, guard, recovered)


# ── the residue surface, rendered FROM the artifacts ─────────────────────────────────────────────

def render_surface(a: dict, guard: dict, recovered: dict) -> str:
    L: list[str] = []

    def add(line: str = "") -> None:
        L.append(line)

    withheld = [row for row in guard["entries"]
                if row["verdict"] == "SOLE-CARRIER"
                and row["the_result_the_recovery_pass_returned"] == NOTHING_FOUND]
    nothing_found = [row for row in guard["entries"]
                     if row["the_result_the_recovery_pass_returned"] == NOTHING_FOUND]
    executed = len(nothing_found) - len(withheld)
    clause = a["the_ruling_that_ordered_it"]["★_the_clause_that_binds_the_discard_ruling_when_it_is_put"]

    add("# The soft-discard's residue — what the guard withheld, and what the check over the 62 "
        "found")
    add()
    add("> **STATUS: RULED, 2026-08-17. NOTHING IS EXECUTED BY IT.** This surface was a ruling")
    add("> surface awaiting the user; **the user ruled it at the residue sitting of 2026-08-17,")
    add("> whose record is `cowork_rulings_2026_08_17_residue_sitting.md`** — the authority for what")
    add("> was ruled and what was not, none of which is restated here (#6). **The banner it replaces")
    add("> read \"STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED.\" — true when it")
    add("> was written, and made untrue by the sitting; the former rendering stands in git at the")
    add("> commits that carried it (#12).** No entry on this")
    add("> surface has been discarded, retired, edited, moved or marked BY THIS SURFACE, and the two")
    add("> derivations it reports performed no decisions-register mutation of any kind. Generated by")
    add("> `tools/audit/gen_ratified_document_check.py` from")
    add("> `tools/audit/ratified_document_check.json` and `tools/audit/sole_carrier_subclass.json`,")
    add("> so no count and no member list below is typed by hand (#17f). Per the standing")
    add("> presentation rule (`cowork_rulings_2026_08_15_batch_return.md` §5) every identifier used")
    add("> below is re-explained from scratch in §0 before any question rests on it.")
    add(">")
    add("> **The user's own clause, which binds every discard record and is quoted verbatim:** a")
    add(f"> soft-discard record is *\"{clause}\"*.")
    add()

    add("## 0. The referents, re-explained from scratch (read this section first)")
    add()
    add("- **The decisions register** — the project's record of WHAT WAS DECIDED about how this")
    add("  system works and whether each decision still stands. It has three surfaces: a data file")
    add("  (`tools/audit/decisions/backbone_decisions.json`), which is the only one ever edited;")
    add("  a rendered INDEX (`DECISIONS.md`); and rendered group files (`decisions/group_*.md`).")
    add("- **An entry** — one row of that record: a decision's title, the verbatim words it was")
    add("  recorded in at its home document, a plain restatement, where it is recorded, its status,")
    add("  the date and ratifier its original record states, and its recorded reasoning.")
    add("- **A deciding act** — the event in which somebody decided: a user ruling, a ratification,")
    add("  a shelving, a falsification. Naming one means naming who decided, or when, or at which")
    add("  record or event it is written down.")
    add("- **The filter** — the first of three passes. It read each entry's OWN FIELDS and proposed")
    add("  one class per entry: a deciding act is named (the KEEP side, which the user has since")
    add("  RATIFIED), no deciding act was found, or the evidence is ambiguous. The last two are the")
    add("  **non-keep population**.")
    add("- **The deciding-act recovery pass** — the second. For every non-keep entry it followed")
    add("  the entry's OWN cited sources through the record and searched them for a user act naming")
    add("  that entry's subject, returning ACT-FOUND (quoted and located) or NOTHING-FOUND.")
    add("- **Soft-discard** — retired from the live record, **not destroyed** (#12), and")
    add("  individually revivable the moment a deciding act is named. It is a PROVENANCE verdict")
    add("  and never a judgment on whether the decision is sound or useful.")
    add("- **The sole-carrier guard** — the third, and the subject of §2. A derived subclass of")
    add("  entries that may be the ONLY place their content is carried. Its members do NOT ride the")
    add("  discard: they come back to the user as the list in §2.")
    add("- **A subject recogniser** — a search pattern the decisions register carries FOR AN ENTRY,")
    add("  authored when that entry was written. Wherever this surface says an entry's subject was")
    add("  looked for, these are what was looked for, never this side's reading of what the entry")
    add("  is about.")
    add("- **The preparation phase** — the first of the six phases the user ruled on 2026-08-15")
    add("  (`cowork_rulings_2026_08_15_phase_definition_sitting.md`). Turning the project's own")
    add("  record into usable inputs for the later derivation; the filtered decisions register is")
    add("  the first of its named outputs.")
    add()

    add("## 1. What the user ruled, and what comes back here")
    add()
    add("The ruling is `cowork_rulings_2026_08_16_preparation_return.md` §3, and it has three")
    add("limbs. **(A)** the entries the recovery pass returned NOTHING-FOUND for are")
    add("SOFT-DISCARDED — *behind the sole-carrier guard*. **(B1)** ten clear recoveries are KEPT.")
    add("**(B2)** the remaining ACT-FOUND entries are NOT ruled until one further bounded")
    add("derivation has run. This surface carries the two things that ruling sends back to the")
    add("user, and nothing else:")
    add()
    add(f"- **§2 — the {len(withheld)} entries the sole-carrier guard WITHHELD from the discard.**")
    add("  They are not discarded, and this surface does not propose that they should be.")
    add(f"- **§3 — the {a['the_population']['entries_checked_here']} entries of (B2), each with the")
    add("  result of the check the ruling ordered.**")
    add()
    add("**The discard arithmetic, to the digit, so the two halves can be checked against each")
    add("other:**")
    add()
    add("| | entries |")
    add("|---|---|")
    add(f"| the recovery pass returned NOTHING-FOUND for | {len(nothing_found)} |")
    add(f"| of which the sole-carrier guard WITHHELD | {len(withheld)} |")
    add(f"| leaving the executed discard population | {executed} |")
    add()

    add("## 2. The sole-carrier guard — what it is, and every entry it withheld")
    add()
    add("**Why the guard exists, in the user's own question.** The user asked whether the discard")
    add("risks losing a genuinely good idea that should have been used as input when designing or")
    add("building the analysis. Three standing nets catch almost all of that — the disposition")
    add("discipline over every specification statement, the audit's something-missing verdict, and")
    add("the fact-gate — and ONE residual class escapes all three: an idea whose only carrier is")
    add("the decisions-register entry itself, typically a proposal that was deferred and never")
    add("built. The guard is that class, derived.")
    add()
    add("**The rule, which has no threshold and no hand-picked member.** An entry is a")
    add("SOLE-CARRIER if ANY of three signals fires:")
    add()
    add("- **(i)** its recorded status is `deferred` — the value the decisions register's own")
    add("  header defines as *\"decided to be built later; the decision itself stands\"*;")
    add("- **(ii)** its home cannot be located — the document is not in the tracked tree, or the")
    add("  cited line is one that document does not reach, or the recorded section's heading is")
    add("  not in it;")
    add("- **(iii)** its content is found nowhere outside the decisions-register family — the")
    add("  entry's verbatim quotation, normalized by the decisions register's OWN normalization,")
    add("  is not in any searched tracked file outside `DECISIONS.md`, `decisions/` and")
    add("  `tools/audit/`.")
    add()
    add("**What each signal found over the whole non-keep population "
        f"({guard['the_population']['entries']} entries):**")
    add()
    add("| signal | entries it fired for |")
    add("|---|---|")
    for signal, count in guard["how_many_entries_each_signal_fired_for"].items():
        add(f"| {signal} | {count} |")
    add()
    add("**★ TWO OF THE THREE SIGNALS CAME BACK EMPTY, AND THAT IS A RESULT RATHER THAN A")
    add("MALFUNCTION.** Each of the three is shown, in the artifact, BOTH to fire on a case that")
    add("should fire it and to stay quiet on one that should not — so an empty signal cannot be")
    add("mistaken for one that cannot fire at all (#19). What the two empty ones say is that every")
    add("non-keep entry's home resolves at the measured commit and that every one of their")
    add("verbatim quotations is carried outside the decisions-register family. That agrees with")
    add("two standing checks that assert the same thing by different routes — the decisions")
    add("register's own establishment pass, which finds every verbatim at its cited home, and the")
    add("home classification, which re-derives every home section from the documents' own")
    add("headings — so it is corroboration and not an assumption.")
    add()
    add(f"### The {len(withheld)} entries WITHHELD from the discard")
    add()
    add("Each is an entry the recovery pass returned NOTHING-FOUND for — so it would otherwise")
    add("have ridden the discard — and which at least one signal flagged. **They return to the")
    add("user as a list; nothing here proposes what should happen to them.** The ruling's own")
    add("provision is that the keepers are carried into the framework phase's candidate")
    add("enumeration as UNTRUSTED CANDIDATES, never as decisions.")
    add()
    for row in withheld:
        add(f"- **{row['id']}** — {row['title']}")
        add(f"  - *What the entry says the decision is:* "
            f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
        add(f"  - *Recorded at* `{row['home']}`; *status* `{row['status']}`; "
            f"*the filter proposed* {row['the_class_the_filter_proposed']}")
        add(f"  - *Signals that fired:* " + "; ".join(row["the_signals_that_fired"]))
    add()

    add("## 3. The check over the 62 — every entry, with what the ratified document said")
    add()
    add("**What was ordered, quoted:**")
    add()
    add(f"> {a['the_ruling_that_ordered_it']['every_sentence_located_in_that_record_on_this_run']['what was ordered']}")
    add()
    add("**Why the question is worth asking.** The recovery pass found, for these entries, a")
    add("passage in a document the entry itself cites that carries a user-act marker AND matches")
    add("the entry's own subject recognizers. Among them a recognizable shape appears: the")
    add("passage is one in which the user ratified a WHOLE DOCUMENT, and it matched the entry's")
    add("recognizers only because those words happen to occur in the ratifying sentence. Such a")
    add("passage is evidence about THIS entry only if the document that was ratified actually")
    add("carries the entry's subject. That is what was checked.")
    add()
    add("**How the population was derived, and why it is not typed anywhere.** It is the recovery")
    add("pass's ACT-FOUND entries minus the ten the (B1) limb KEPT. The ten are PARSED from the")
    add("ruling record's own bullet on every run; a bullet naming any number other than ten, or")
    add("naming an entry the recovery pass did not return ACT-FOUND for, halts the derivation")
    add("rather than being corrected.")
    add()
    add(f"- ACT-FOUND entries: **{a['the_population']['act_found_entries']}**")
    add(f"- The ten KEPT by (B1): {', '.join('**' + k + '**' for k in a['the_population']['the_ten_the_B1_ruling_kept'])}")
    add(f"- Checked here: **{a['the_population']['entries_checked_here']}**")
    add()
    add("| result | entries |")
    add("|---|---|")
    for result in RESULTS:
        add(f"| {result} | {a['the_distribution'][result]} |")
    add()
    add("**What each result does and does not claim:**")
    add()
    for name, text in a["★_what_a_result_here_is_NOT"].items():
        add(f"- **{name.replace('_', ' ')}.** {text}")
    add()
    add("**★ WHERE THE RECOGNIZER IS WIDE AND WHERE IT IS NARROW, stated before the results.** "
        + a["the_rule"]["what_makes_a_passage_a_document_ratification"])
    add()
    drift = a["acts_whose_recorded_coordinates_no_longer_resolve"]
    add(f"**★ COORDINATES THAT NO LONGER RESOLVE: {drift['count']} entries.** "
        + drift["★_why_this_is_published"])
    if drift["entries"]:
        add()
        add("The entries affected: " + ", ".join(f"**{i}**" for i in drift["entries"]) + ".")
    add()

    for result in RESULTS:
        members = [row for row in a["entries"] if row["result"] == result]
        add(f"### {result} — {len(members)} entries")
        add()
        if not members:
            add("*None.*")
            add()
            continue
        for row in members:
            add(f"- **{row['id']}** — {row['title']}")
            add(f"  - *What the entry says the decision is:* "
                f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
            add(f"  - *Recorded at* `{row['home']}`; *status* `{row['status']}`; "
                f"*the filter proposed* {row['the_class_the_filter_proposed']}")
            add(f"  - *Recovered acts:* {row['acts_the_recovery_pass_recorded']}, of which "
                f"{row['acts_that_are_document_ratifications']} ratify a document other than "
                f"their own")
            for match in row["the_subject_matches_found_in_ratified_documents"]:
                add(f"  - *Subject found in* `{match['the_ratified_document']}` line "
                    f"{match['at_line']} — matched by {match['what_matched_the_subject']} "
                    f"(`{match['the_matched_text']}`)")
                add(f"    > {match['the_passage_quoted']}")
            for stranded in row["ratified_documents_that_could_not_be_located"]:
                add(f"  - *A ratified document that could not be located:* "
                    f"`{stranded['the_name_quoted']}` (named at {stranded['named_in']})")
        add()

    add("## 4. What this surface does NOT do, and must not be read as doing")
    add()
    add("- **It rules nothing and discards nothing.** Both halves are evidence for the user's")
    add("  ruling.")
    add("- **It re-classifies no entry.** The filter's proposed class and the recovery pass's")
    add("  result ride beside every row and are unchanged by anything here.")
    add("- **It edits no decisions-register file.** The two derivations it reports performed no")
    add("  mutation of the data file, the rendered INDEX or the group files.")
    add("- **It grades no decision's content**, its conformance, or whether the code obeys it —")
    add("  and nothing here is a judgment on soundness or usefulness.")
    add("- **It performs no archiving, no mining and no fact-gate admission.**")
    add()
    add("*Generated by `tools/audit/gen_ratified_document_check.py` from")
    add("`tools/audit/ratified_document_check.json` and `tools/audit/sole_carrier_subclass.json`.")
    add("Reproduce: `python tools/audit/gen_ratified_document_check.py --check`.*")
    add()
    return "\n".join(L)


def main(argv: list[str]) -> int:
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        committed = json.loads(OUT.read_text(encoding="utf-8"))
        recorded = committed.get("derived_at_commit")
        if not recorded:
            print("FAIL: the committed artifact records no commit to re-derive at")
            return 1
        artifact, surface = build(recorded)
        drift = 0
        if json.dumps(artifact, indent=1, ensure_ascii=False) + "\n" != OUT.read_text(
                encoding="utf-8"):
            print("FAIL: the ratified-document check does not re-derive at", recorded[:10])
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("FAIL: the residue surface does not re-derive:", SURFACE)
            drift = 1
        if not drift:
            print(f"the ratified-document check re-derives at {recorded[:10]}")
        return drift

    # ★ THE WRITE PATH BUILDS AT THE COMMIT THE COMMITTED ARTIFACT RECORDS, NOT AT HEAD (2026-08-18,
    # `cc_instruction_preparation_eleventh_amended.md` Task 3; DECLARED AS A JUDGMENT in that
    # batch's report and close, never slipped in).  This pass is EPOCH-PINNED: `--check` has always
    # re-derived at the commit the artifact records, while the write path resolved HEAD — so the two
    # paths asked different questions, and the write path could only ever have folded whatever the
    # tree currently says into the record of a completed act, which is the OI-301 hazard exactly.
    # MEASURED rather than argued: run at HEAD it does not merely differ, it STOPS, because nine
    # entries of its population are no longer live in the decisions register's data file — the
    # soft-discard it was gathered for retired them. The change is what makes the ruled banner
    # qualification renderable at all (Ruling 2 of `cowork_rulings_2026_08_18_tenth_return.md` orders
    # it rendered into the document in the same act), and it agrees the write path with the pin the
    # check already carried. The first run of a fresh pass, with no committed artifact, still
    # resolves HEAD.
    commit = resolve("HEAD")
    if OUT.exists():
        recorded = json.loads(OUT.read_text(encoding="utf-8")).get("derived_at_commit")
        if recorded:
            commit = recorded
    artifact, surface = build(commit)
    OUT.write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print("wrote", SURFACE.relative_to(ROOT))
    print(f"  population {artifact['the_population']['entries_checked_here']} at {commit[:10]}")
    for result in RESULTS:
        print(f"  {result}: {artifact['the_distribution'][result]}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
