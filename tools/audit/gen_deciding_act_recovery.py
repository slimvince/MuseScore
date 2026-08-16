#!/usr/bin/env python3
"""CAN A USER ACT BE RECOVERED FOR AN ENTRY THE DECISIONS REGISTER'S FIELDS COULD NOT NAME ONE FOR?

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §2 of `cowork_rulings_2026_08_16_preparation_return.md`,
taken at the return of the decisions-register filter.  The filter classified every entry of the
decisions register by reading the ENTRY'S OWN FIELDS, and proposed a soft-discard class for the
entries whose fields name no deciding act.  Before ruling on that class the user ordered THIS: an
investigation, not a question — *"for each entry, its own cited sources — open-items rows, records,
sections — are followed through the record and searched for a user act naming the entry's subject;
published per entry as ACT-FOUND (quoted, located) or NOTHING-FOUND."*

★ WHAT THIS PASS IS FOR, IN ONE SENTENCE.  The filter read the decisions register; this reads THE
RECORD THAT REGISTER POINTS AT.  A decision whose entry records no ratifier may still have been
ruled in a document the entry cites, and until somebody follows the citation nobody knows which.

★★ IT PROPOSES NOTHING AND IT DISCARDS NOTHING.  No entry is retired, edited, moved or marked; the
decisions register's data file and every file rendered from it are untouched by this tool, which
opens them for reading and writes only its own two outputs.  A soft-discard ruling is the user's,
it is put at this pass's return, and the user's own clause binds it when it comes: a soft-discard
record is a PROVENANCE verdict and not a judgment on soundness or usefulness.

WHAT IS DERIVED AND WHAT IS AUTHORED — the difference is the whole value of the output.
  DERIVED   the population, IMPORTED from the committed filter artifact and never restated (#6);
            every entry's fields, read from the decisions register's own data file; every citation,
            extracted from the entry's own recorded text; which citations resolve on disk; every
            located act, quoted from the document it was found in with its line; every count.
  AUTHORED  which of the entry's fields are read as CITED SOURCES; what counts as a USER ACT; and
            the block rule that decides whether an act and a subject are in the same place.  All
            three are published in the artifact beside the results they produced, so the rule can
            be checked against the evidence without opening this file.

★ HOW AN ENTRY'S SUBJECT IS RECOGNISED, and why nothing here is invented.  The decisions register
carries, per entry, a `patterns` list — the register's OWN recognizers for that entry's subject,
authored when the entry was written and used elsewhere to find the entry's restatements in the
record.  This pass uses those, together with the entry's identity.  So the subject test is the
record's own, not this tool's reading of what an entry is about.

★ THE BOUND ON HOW FAR A CITATION IS FOLLOWED, stated before the first result.  ONE LEVEL: the
documents the entry itself names, plus the dated ruling records where the entry records a date.  A
citation found INSIDE one of those documents is not followed further.  The bound is the dispatch's
own, and it is recorded in the artifact rather than left for a reader to infer.

★ WHAT A FOUND ACT IS AND WHAT IT IS NOT.  It is a passage, in a document the entry cites, that
carries a user-act marker AND matches the entry's own subject recognizers.  That is EVIDENCE FOR
THE USER TO READ, never a verdict: a passage can carry both and still be about something else, and
this tool does not paraphrase what it found — it quotes it, names where it is, and stops.  Nothing
here re-classifies any entry, and the filter's own proposed class is carried beside every result so
the two can be read together.

THE STOPS, so this cannot silently stop being an enumeration:
  * the committed filter artifact missing, or carrying no entry in the non-keep classes, STOPS it;
  * an imported entry identity the decisions register's data file does not carry STOPS it, and so
    does a non-keep entry of the data file that the import does not carry — BOTH directions;
  * an entry missing a field this pass reads STOPS it — an entry it cannot read at all is never
    quietly skipped;
  * a result outside the closed three-value vocabulary STOPS it;
  * a distribution that does not account for the population STOPS it;
  * a sentence of the ruling this pass serves that is no longer in its ruling record STOPS it, so
    the pass cannot outlive the words that ordered it.
Each is exercised by a probe recorded in the artifact, and every probe calls the very function the
walk calls, so the two cannot drift apart.

Run:
  python tools/audit/gen_deciding_act_recovery.py           # write the artifact and the surface
  python tools/audit/gen_deciding_act_recovery.py --check   # re-derive both, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
FILTER = "tools/audit/decisions_filter_classification.json"
BACKBONE = "tools/audit/decisions/backbone_decisions.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
OUT = ROOT / "tools" / "audit" / "deciding_act_recovery.json"
SURFACE = (ROOT / "ratification_surfaces"
           / "cowork_deciding_act_recovery_surface_2026_08_16.md")

# ── PINNED READING (user, 2026-08-16, §6 kind 1 of the preparation-return rulings) ────────────
#
# ★ WHY THIS PASS IS READ AT A COMMIT AND NOT AT THE TREE.  Its 72 ACT-FOUND / 194 NOTHING-FOUND
# result IS the evidence the soft-discard was ruled over, and the discard then retires 165 of the
# very entries this pass walked.  Read live, the pass would restate a completed measurement against
# the population the act it authorized changed — and every document it searched is a document a
# later session may edit.  Pinned, the artifact stands permanently as that evidence, still guarded
# against corruption, and permanently insensitive to the acts it authorized.
#
# ★ WHAT STAYS LIVE, DELIBERATELY.  The sentences of the ruling that ordered this pass are located
# in the ruling record AS IT STANDS on every run, exactly as before: the pass may not outlive the
# words that ordered it, and that assertion is about today's record rather than about the measured
# state.  It is the same split the sole-carrier tool draws.
#
# ★ WHY THE COMMIT IS NAMED HERE AND NOT INSIDE THE ARTIFACT.  The artifact carries no
# `derived_at_commit` field and MAY NOT GAIN ONE — the ruling requires it byte-unchanged, and
# adding a field is a change.  So the pin lives in the tool, and `establish_the_pin()` proves it on
# every run by reading THIS ARTIFACT ITSELF out of the git object at the pinned commit and
# requiring it to match the artifact on disk.
PINNED_COMMIT = "ddbf89d002b95ea4efc80e0833d903bc08ca00d1"
PINNED_COMMIT_IS = ("the commit that produced and committed this artifact — "
                    "`cc_instruction_preparation_second.md` Task 2, the run the user read before "
                    "ruling the soft-discard (`cc_report_preparation_second.md` §4)")

# The filter's own class names. This pass may not widen them and does not re-classify with them.
NO_ACT = "NO-DECIDING-ACT-FOUND"
AMBIGUOUS = "EVIDENCE-AMBIGUOUS"
NON_KEEP = (NO_ACT, AMBIGUOUS)

# The closed result vocabulary of THIS pass, from the ruling's own words plus the dispatch's A3.
ACT_FOUND = "ACT-FOUND"
NOTHING_FOUND = "NOTHING-FOUND"
UNRESOLVED = "CITATIONS-UNRESOLVED"
RESULTS = (ACT_FOUND, NOTHING_FOUND, UNRESOLVED)

# The fields of an entry this pass reads. A member missing one of these is a STOP.
REQUIRED_FIELDS = ("id", "group", "title", "plain", "home", "status", "date", "status_source",
                   "rationale", "verbatim")

# AUTHORED: which fields are read as the entry's CITED SOURCES, and why these four.
CITATION_FIELDS = ("home", "status_source", "rationale", "verbatim")
WHY_THESE_FIELDS = (
    "The dispatch names *the rows, records and sections its recorded status source and home name*. "
    "Those two are read, and two more with them: `rationale`, which is where an entry records the "
    "reasoning and the citation behind it, and `verbatim`, which is the entry's quotation from its "
    "home and therefore carries that home's own citations. The widening is declared rather than "
    "silent, and it runs in the direction that FINDS acts rather than the one that misses them — "
    "which is what a recovery pass is for. `title` and `plain` are the decisions register's own "
    "restatement "
    "and carry no citation."
)

# AUTHORED: the sentences of the ruling this pass serves, LOCATED in its record on every run.
RULING_SENTENCES = {
    "what was ordered":
        "for each entry, its own cited sources — open-items rows, records, sections — are followed "
        "through the record and searched for a user act naming the entry's subject; published per "
        "entry as ACT-FOUND (quoted, located) or NOTHING-FOUND",
    "when the discard is ruled":
        "The soft-discard ruling is put at that return, over evidence.",
    "the clause that binds the eventual discard":
        "every soft-discard record states, per entry, that it is a PROVENANCE verdict and not a "
        "judgment on soundness or usefulness",
    "what the keep side means":
        "The 411 DECIDING-ACT-NAMED entries are RATIFIED as the live record's confirmed side.",
    "nothing is discarded by the ordering":
        "no entry moves, nothing is discarded, and an unconfirmed row is still not cited as "
        "authority",
}

# AUTHORED: what counts as a USER ACT in a cited document. Every one is published beside the
# results, and every match is quoted, so a reader applies the test rather than trusting it.
USER_ACT_MARKERS = [
    ("a user-act marker", re.compile(
        r"user-ruled|user ruled|user-directed|user directed|user-ratified|user ratified|"
        r"ratified by the user|ruled by the user|the user ruled|the user's ruling|"
        r"user mandate|user-mandated|user-authored|user-accepted", re.I)),
    ("a numbered ruling named", re.compile(r"\bRuling\s+\d+\b")),
    ("a ratification event named", re.compile(
        r"\bratification event\b|\bratified AS DRAFTED\b|\bratified Decision\b", re.I)),
    ("a ruling record named", re.compile(r"cowork_rulings_[0-9a-z_]+\.md")),
    ("an explicit RULED marker", re.compile(r"\bRULED\b")),
]

# DERIVED from each entry's own text: the citations this pass follows.
PATH_CITATION = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-/]*\.(?:md|py|json|csv|cpp|h|txt)")
ROW_CITATION = re.compile(r"\bOI-(\d+)\b")
DATE_CITATION = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")

MAX_ACTS_RECORDED = 3          # every match is COUNTED; this bounds only what is quoted


class Stop(Exception):
    """The pass cannot be published as an enumeration. Never a warning, never an entry skipped."""


def normalized(text: str) -> str:
    """Whitespace collapsed and emphasis marks removed, so a quote survives line wrapping."""
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_ruling() -> dict[str, str]:
    """Every sentence of the ruling, LOCATED in its record. A missing one STOPS."""
    if not RULING.exists():
        raise Stop(f"the ruling record this pass serves is missing: {RULING}")
    text = normalized(RULING.read_text(encoding="utf-8"))
    missing = [name for name, quote in RULING_SENTENCES.items() if normalized(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling is no longer in its ruling record, so this pass would "
                   f"outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


def require_fields(entry: dict) -> None:
    """THE FIRST STOP. An entry this pass cannot read is never quietly skipped."""
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        raise Stop(f"entry {entry.get('id', '<no identity>')!r} carries no {missing} — the "
                   f"recovery cannot be run for it, and an entry it cannot read at all is a STOP "
                   f"rather than a skip")


def reconcile(imported: set[str], in_the_data_file: set[str]) -> None:
    """THE SECOND STOP — checked in BOTH directions (D-671)."""
    only_import = sorted(imported - in_the_data_file)
    only_data = sorted(in_the_data_file - imported)
    if only_import or only_data:
        raise Stop(
            "the imported non-keep population and the decisions register's data file do not carry "
            "the same entries — a derivation over a derived population is published WHOLE or not "
            f"at all (D-671). Imported and not in the data file: {only_import}. "
            f"Non-keep in the data file and not imported: {only_data}")


def require_reconciled_distribution(rows: list[dict], population_size: int) -> None:
    """THE FOURTH AND FIFTH STOPS. Every result in the vocabulary, and the counts accounting."""
    if len(rows) != population_size:
        raise Stop(f"the recovered rows ({len(rows)}) do not account for the population "
                   f"({population_size})")
    unknown = sorted({r["result"] for r in rows} - set(RESULTS))
    if unknown:
        raise Stop(f"a result outside this pass's closed three-value vocabulary: {unknown}")
    per_result: dict[str, int] = {}
    for row in rows:
        per_result[row["result"]] = per_result.get(row["result"], 0) + 1
    if sum(per_result.values()) != population_size:
        raise Stop("the per-result distribution does not sum to the population")


# ── the citations, extracted from the entry's own text ───────────────────────────────────────────

def citations_of(entry: dict) -> list[dict]:
    """Every followable citation the entry itself carries, with the field it was found in."""
    found: list[dict] = []
    seen: set[tuple[str, str]] = set()

    def add(kind: str, cited: str, field: str, quoted: str) -> None:
        if (kind, cited) in seen:
            return
        seen.add((kind, cited))
        found.append({"kind": kind, "cited": cited, "found_in_the_field": field,
                      "quoted_from_the_entry": quoted})

    for field in CITATION_FIELDS:
        text = entry.get(field) or ""
        if not isinstance(text, str):
            continue
        for match in PATH_CITATION.finditer(text):
            add("a document", match.group(0), field, _window(text, match))
        for match in ROW_CITATION.finditer(text):
            add("an open-items row", match.group(0), field, _window(text, match))
        for match in DATE_CITATION.finditer(text):
            add("a date", match.group(0), field, _window(text, match))
    date = (entry.get("date") or "").strip()
    if DATE_CITATION.fullmatch(date):
        add("a date", date, "date", date)
    return found


def _readable(text: str, width: int = 900) -> str:
    """A passage collapsed to one line, with markdown quote marks stripped from each line.

    A block quoted out of a document that is itself a blockquote arrives with a `>` opening every
    line; leaving them in makes the evidence read as nested quotation of something else, which is
    the opposite of what a quoted act should look like.
    """
    lines = [re.sub(r"^\s*>+\s?", "", line) for line in text.splitlines()]
    return " ".join(" ".join(lines).split())[:width]


def _window(text: str, match: re.Match, width: int = 80) -> str:
    start, end = max(0, match.start() - width), min(len(text), match.end() + width)
    return (("..." if start else "") + " ".join(text[start:end].split())
            + ("..." if end < len(text) else ""))


def git(*args: str) -> bytes:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


_TREE: dict[str, None] | None = None


def pinned_tree() -> dict[str, None]:
    """Every tracked path at the pinned commit — the file population this pass may search."""
    global _TREE
    if _TREE is None:
        listing = git("ls-tree", "-r", "--name-only", PINNED_COMMIT).decode("utf-8", "replace")
        _TREE = {line.strip().strip('"'): None for line in listing.split("\n") if line.strip()}
    return _TREE


def pinned_text(path: str, what: str) -> str:
    """One input, read from the git OBJECT at the pinned commit and never from the tree."""
    try:
        return git("show", f"{PINNED_COMMIT}:{path}").decode("utf-8", "replace")
    except Stop:
        raise Stop(f"{what} is not in the tree at the pinned commit "
                   f"{PINNED_COMMIT[:10]}: {path}")


def establish_the_pin() -> None:
    """The pin proves itself, on every run, before anything rests on it."""
    if not OUT.exists():
        raise Stop(f"the committed artifact is missing: {OUT}")
    rel = OUT.relative_to(ROOT).as_posix()
    # As TEXT rather than as bytes: the working tree carries the platform's line endings while a
    # git object carries the blob's own, so a byte comparison would report every artifact as moved.
    if git("show", f"{PINNED_COMMIT}:{rel}").decode("utf-8") != OUT.read_text(encoding="utf-8"):
        raise Stop(
            f"the committed artifact is NOT byte-identical to its own blob at the pinned commit "
            f"{PINNED_COMMIT[:10]}. Either the pin names the wrong commit or the artifact has been "
            f"rewritten since; both are STOPs, because this artifact is a ruling's evidence and "
            f"the ruling requires it byte-unchanged.")


def resolve(citation: dict) -> list[str]:
    """The repository files a citation points at, or an empty list where it points at nothing."""
    kind, cited = citation["kind"], citation["cited"]
    tree = pinned_tree()
    if kind == "a document":
        candidate = cited.split(":")[0].strip().strip(".,;)`\"'")
        if not candidate:
            return []
        return [candidate] if candidate.replace("\\", "/") in tree else []
    if kind == "an open-items row":
        candidate = f"open_items/{cited}.md"
        return [candidate] if candidate in tree else []
    if kind == "a date":
        year, month, day = DATE_CITATION.match(cited).groups()
        stamp = f"{year}_{month}_{day}"
        return sorted(p for p in tree
                      if "/" not in p and p.startswith("cowork_rulings_") and p.endswith(".md")
                      and stamp in p)
    return []


# ── the search ───────────────────────────────────────────────────────────────────────────────────

def act_bearing_blocks(text: str) -> list[dict]:
    """Every blank-line-separated block of a document that carries a user-act marker.

    The block is the unit because an act and the subject it decides have to be in the same PLACE
    for the one to be evidence about the other. A whole-document match would report a ruling on
    page one as evidence for a subject on page forty.
    """
    blocks: list[dict] = []
    line_no, buffer, start = 0, [], 1
    lines = text.splitlines()
    for index, line in enumerate(lines, start=1):
        line_no = index
        if line.strip():
            if not buffer:
                start = index
            buffer.append(line)
            continue
        if buffer:
            blocks.append({"line": start, "lines": len(buffer), "text": "\n".join(buffer)})
            buffer = []
    if buffer:
        blocks.append({"line": start, "lines": len(buffer), "text": "\n".join(buffer)})
    del line_no
    out = []
    for block in blocks:
        markers = [label for label, pattern in USER_ACT_MARKERS if pattern.search(block["text"])]
        if markers:
            out.append({**block, "user_act_markers": markers})
    return out


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


def recover(entry: dict, documents: dict[str, list[dict]]) -> dict:
    """ONE entry's recovery, over the documents its own citations resolve to."""
    cited = citations_of(entry)
    followed, searched, dangling = [], [], []
    for citation in cited:
        targets = resolve(citation)
        record = {**citation, "resolved_to": targets}
        followed.append(record)
        if targets:
            searched.extend(targets)
        else:
            dangling.append(citation["quoted_from_the_entry"])
    searched = sorted(set(searched))

    matchers, unusable = subject_matchers(entry)
    acts, total = [], 0
    for path in searched:
        for block in documents.get(path, []):
            hit = None
            for label, pattern in matchers:
                match = pattern.search(block["text"])
                if match:
                    hit = (label, match.group(0))
                    break
            if hit is None:
                continue
            total += 1
            if len(acts) < MAX_ACTS_RECORDED:
                acts.append({
                    "document": path,
                    "line": block["line"],
                    "the_passage_spans_lines": block["lines"],
                    "the_user_act_markers_the_passage_carries": block["user_act_markers"],
                    "what_matched_the_subject": hit[0],
                    "the_matched_text": hit[1],
                    "the_act_quoted": _readable(block["text"]),
                })

    if acts:
        result = ACT_FOUND
        why = ("a passage in a document this entry itself cites carries a user-act marker and "
               "matches the entry's own subject recogniser; it is quoted and located below, and "
               "reading it is the user's act, not this tool's")
    elif searched:
        result = NOTHING_FOUND
        why = ("every citation this entry carries was followed and every document it resolved to "
               "was searched; no passage in them carries both a user-act marker and a match of "
               "this entry's own subject recognisers")
    else:
        result = UNRESOLVED
        why = ("no citation this entry carries resolves to a file in the repository, so there was "
               "nothing to search; the dangling text is quoted below (the dispatch's A3 — a "
               "per-entry result, never a halt)")

    return {
        "id": entry["id"],
        "group": entry["group"],
        "title": entry["title"],
        "home": entry["home"],
        "status": entry["status"],
        "recorded_date": entry["date"],
        "result": result,
        "why_this_result": why,
        "what_the_entry_says_the_decision_is_quoted_from_the_register": entry["plain"],
        "what_was_followed": followed,
        "where_the_search_looked": searched,
        "acts_found_total": total,
        "acts_quoted_here": len(acts),
        "acts": acts,
        "dangling_citation_text_quoted": dangling if result == UNRESOLVED else [],
        "subject_recognisers_the_register_carries_that_would_not_compile": unusable,
    }


# ── probes (#19) ─────────────────────────────────────────────────────────────────────────────────

def probes() -> list[dict]:
    out = []

    def probe(name: str, what: str, fn) -> None:
        try:
            fn()
        except Stop as exc:
            out.append({"probe": name, "what_was_fed": what, "raised": True, "message": str(exc)})
            return
        out.append({"probe": name, "what_was_fed": what, "raised": False,
                    "message": "NO STOP — this probe FAILED to establish its stop"})

    probe("a missing field", "an entry carrying every required field but `status_source`",
          lambda: require_fields({f: "x" for f in REQUIRED_FIELDS if f != "status_source"}))
    probe("an imported entry the data file does not carry",
          "imported {'D-001','D-002'} against a data file carrying {'D-001'}",
          lambda: reconcile({"D-001", "D-002"}, {"D-001"}))
    probe("a non-keep entry of the data file the import does not carry",
          "imported {'D-001'} against a data file carrying {'D-001','D-002'}",
          lambda: reconcile({"D-001"}, {"D-001", "D-002"}))
    probe("a result outside the closed vocabulary", "one row carrying the result 'INVENTED'",
          lambda: require_reconciled_distribution([{"result": "INVENTED"}], 1))
    probe("a distribution that does not account for the population",
          "one recovered row against a population of two",
          lambda: require_reconciled_distribution([{"result": ACT_FOUND}], 2))

    failed = [p["probe"] for p in out if not p["raised"]]
    if failed:
        raise Stop(f"a probe did not raise, so a STOP this tool claims cannot be shown to fire: "
                   f"{failed}")
    return out


# ── the build ────────────────────────────────────────────────────────────────────────────────────

def build() -> tuple[dict, str]:
    establish_the_pin()

    ruling = locate_ruling()

    classified = json.loads(pinned_text(FILTER, "the committed filter artifact"))
    imported = {row["id"]: row for row in classified["entries"]
                if row["proposed_class"] in NON_KEEP}
    if not imported:
        raise Stop("the committed filter artifact carries no entry in the non-keep classes, so "
                   "there is no population to recover over — the import is not what this pass "
                   "assumes it is")

    data = json.loads(pinned_text(BACKBONE, "the decisions register's data file"))
    by_id = {}
    for entry in data["decisions"]:
        require_fields(entry)
        by_id[entry["id"]] = entry
    non_keep_in_data = {row["id"] for row in classified["entries"]
                        if row["proposed_class"] in NON_KEEP and row["id"] in by_id}
    reconcile(set(imported), non_keep_in_data)

    # Every document any member cites, read once and split into act-bearing blocks once.
    wanted: set[str] = set()
    for entry_id in imported:
        for citation in citations_of(by_id[entry_id]):
            wanted.update(resolve(citation))
    documents: dict[str, list[dict]] = {}
    unreadable: list[str] = []
    for path in sorted(wanted):
        try:
            documents[path] = act_bearing_blocks(pinned_text(path, "a cited document"))
        except Stop as exc:
            unreadable.append(f"{path} — {exc}")

    rows = [recover(by_id[entry_id], documents) for entry_id in sorted(imported)]
    for row in rows:
        row["the_class_the_filter_proposed"] = imported[row["id"]]["proposed_class"]
        row["the_evidence_shape_the_filter_recorded"] = imported[row["id"]]["evidence_shape"]
    require_reconciled_distribution(rows, len(imported))

    # How CONCENTRATED the recovered evidence is. One large user-ratified passage can match many
    # entries' subject recognizers at once, and an ACT-FOUND resting only on such a passage is
    # weaker evidence than one resting on a passage written about that entry. Measured rather than
    # left for a reader to notice, on the same ground the caller-check publishes who does the
    # naming.
    carried: dict[tuple[str, int], list[str]] = {}
    spans: dict[tuple[str, int], int] = {}
    for row in rows:
        for act in row["acts"]:
            place = (act["document"], act["line"])
            carried.setdefault(place, []).append(row["id"])
            spans[place] = act["the_passage_spans_lines"]
    concentration = [{"document": document, "line": line,
                      "the_passage_spans_lines": spans[(document, line)],
                      "entries_whose_recovered_evidence_it_carries": len(ids),
                      "the_entries": sorted(ids)}
                     for (document, line), ids in sorted(
                         carried.items(), key=lambda kv: (-len(kv[1]), kv[0]))]
    single = sorted(r["id"] for r in rows
                    if r["result"] == ACT_FOUND and r["acts_found_total"] == 1)

    distribution = {result: sum(1 for r in rows if r["result"] == result) for result in RESULTS}
    by_filter_class = {
        cls: {result: sum(1 for r in rows
                          if r["the_class_the_filter_proposed"] == cls and r["result"] == result)
              for result in RESULTS}
        for cls in NON_KEEP}
    shapes: dict[str, dict[str, int]] = {}
    for row in rows:
        if row["result"] != NOTHING_FOUND:
            continue
        shape = row["the_evidence_shape_the_filter_recorded"]
        shapes[shape] = shapes.get(shape, 0) + 1
    shapes = dict(sorted(shapes.items(), key=lambda kv: (-kv[1], kv[0])))

    artifact = {
        "what_this_is":
            "THE DECIDING-ACT RECOVERY PASS. For every entry the committed decisions-register "
            "filter could not name a deciding act for, this follows the entry's OWN cited sources "
            "through the record and reports whether a USER ACT naming that entry's subject can be "
            "found in them. IT PROPOSES NOTHING AND IT DISCARDS NOTHING: no entry is retired, "
            "edited, moved or marked, and the decisions register's files are untouched.",
        "generator": "tools/audit/gen_deciding_act_recovery.py",
        "dispatch": "cc_instruction_preparation_second.md, Task 2",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §2",
            "every_sentence_located_in_that_record_on_this_run": ruling,
            "★_it_is_an_investigation_and_not_a_question":
                "The ruling orders it under the standing investigate-by-default mandate rather "
                "than putting it as a choice. What returns to the user is the EVIDENCE; the "
                "soft-discard ruling is put at this return, over that evidence.",
            "★_the_clause_that_will_bind_the_eventual_discard_ruling":
                ruling["the clause that binds the eventual discard"],
        },
        "the_population": {
            "imported_from": "tools/audit/decisions_filter_classification.json",
            "the_classes_imported": list(NON_KEEP),
            "entries": len(imported),
            "★_it_is_imported_and_never_restated":
                "The membership is the committed filter artifact's own, read on every run (#6), so "
                "this pass and the filter cannot disagree about who is in the non-keep population. "
                "The reconciliation against the decisions register's data file is a STOP in BOTH "
                "directions, so a derivation over a derived population is published whole or not "
                "at all (D-671).",
        },
        "what_is_DERIVED": [
            "the population, imported from the committed filter artifact and never hand-listed",
            "every entry's fields, read from the decisions register's own data file",
            "every citation, extracted from the entry's own recorded text and quoted with it",
            "which citations resolve to a file in the repository and which do not",
            "every located act, quoted from the document it was found in, with its line",
            "every count and every distribution",
        ],
        "what_is_AUTHORED": [
            "which of the entry's fields are read as its cited sources, and why",
            "what counts as a user act in a cited document — published in full below",
            "the block rule: an act and a subject must be in the same blank-line-separated passage",
        ],
        "the_rule": {
            "fields_read_as_cited_sources": list(CITATION_FIELDS),
            "why_these_fields": WHY_THESE_FIELDS,
            "★_how_far_a_citation_is_followed":
                "ONE LEVEL. The documents the entry itself names, plus the dated ruling records "
                "where the entry records a date. A citation found INSIDE one of those documents is "
                "not followed further. The bound is the dispatch's own and is stated here rather "
                "than left for a reader to infer.",
            "★_how_a_subject_is_recognised":
                "By the entry's own identity and by the `patterns` list the decisions register "
                "carries for that entry — the register's OWN recognizers for its subject, authored "
                "when the entry was written. The subject test is therefore the record's, not this "
                "tool's reading of what an entry is about.",
            "the_user_act_markers": {label: pattern.pattern
                                     for label, pattern in USER_ACT_MARKERS},
            "★_the_block_rule_and_why_it_exists":
                "An act and the subject it decides must be in the same blank-line-separated "
                "passage. A whole-document match would report a ruling on the first page as "
                "evidence about a subject on the fortieth.",
            "★_where_the_block_rule_is_VACUOUS_and_it_is_named_rather_than_patched":
                "A document with no blank lines — a JSON artifact, a CSV table — is ONE block, so "
                "the locality the rule buys is not bought there: an act marker anywhere in such a "
                "file and a subject match anywhere in it are read as being in the same place. NO "
                "SIZE THRESHOLD IS IMPOSED to fix it, because a hand-picked number over varying "
                "data is the shape this record has twice declined. Instead every recovered "
                "passage publishes HOW MANY LINES IT SPANS, so a reader sees at once whether the "
                "evidence is a paragraph or a whole file, and the concentration table publishes "
                "the same span beside the count of entries each passage carries.",
            "the_result_vocabulary": {
                ACT_FOUND: "a passage in a cited document carries a user-act marker and matches "
                           "the entry's own subject recogniser. The passage is quoted and located.",
                NOTHING_FOUND: "every citation was followed and every document it resolved to was "
                               "searched; nothing in them carries both.",
                UNRESOLVED: "no citation this entry carries resolves to a file in the repository, "
                            "so there was nothing to search. The dangling text is quoted.",
            },
        },
        "★_what_a_result_here_is_NOT": {
            "an_ACT_FOUND_is_not_a_verdict":
                "It is evidence for the user to read. A passage can carry a user-act marker and "
                "match a subject recogniser and still be about something else; this tool quotes "
                "what it found, names where it is, and stops. It does not paraphrase the act and "
                "it re-classifies no entry — the filter's own proposed class is carried beside "
                "every result so the two are read together.",
            "a_NOTHING_FOUND_is_not_a_finding_that_no_act_exists":
                "It is a statement about the documents this entry's OWN citations reach, at one "
                "level, searched with the decisions register's own subject recognizers. An act "
                "recorded "
                "somewhere the entry does not cite is outside this pass by construction, and the "
                "one-level bound is exactly where that limit sits.",
            "nothing_here_grades_a_decision":
                "Not its content, not its conformance, not whether the code obeys it. And nothing "
                "here is a judgment on soundness or usefulness — the user's own clause, which "
                "binds the discard ruling when it is put.",
        },
        "the_distribution": distribution,
        "★_how_concentrated_the_recovered_evidence_is": {
            "why_it_is_published": "One large user-ratified passage can match many entries' "
                                   "subject recognizers at once. An ACT-FOUND resting only on such "
                                   "a passage is weaker evidence than one resting on a passage "
                                   "written about that entry, and the difference is visible here "
                                   "as a count rather than left for a reader to notice.",
            "entries_whose_whole_recovered_evidence_is_ONE_passage": single,
            "passages_by_how_many_entries_they_carry": concentration,
        },
        "the_distribution_within_each_class_the_filter_proposed": by_filter_class,
        "the_evidence_shapes_among_the_NOTHING_FOUND_entries": shapes,
        "documents_searched": {
            "count": len(documents),
            "documents": sorted(documents),
            "documents_a_citation_reached_but_could_not_be_read": unreadable,
        },
        "the_stops_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not":
                "They establish that each STOP CAN fire, each through the very function the walk "
                "calls, so the two cannot drift apart. They establish NOTHING about whether any "
                "entry's result is right — that is what the surface puts to the user.",
            "probes": probes(),
        },
        "entries": rows,
    }
    return artifact, render(artifact)


# ── the ruling surface, rendered FROM the artifact ───────────────────────────────────────────────

def render(a: dict) -> str:
    L: list[str] = []

    def add(line: str = "") -> None:
        L.append(line)

    add("# The deciding-act recovery pass — what the record itself says about the entries the "
        "decisions register's own fields could not place")
    add()
    add("> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING HAS BEEN")
    add("> DISCARDED.** No entry has been retired, edited, moved or marked; the decisions")
    add("> register's data file and every file rendered from it are byte-unchanged. Generated by")
    add("> `tools/audit/gen_deciding_act_recovery.py` from")
    add("> `tools/audit/deciding_act_recovery.json`, which it writes in the same run. Per the")
    add("> standing presentation rule (`cowork_rulings_2026_08_15_batch_return.md` §5) every")
    add("> identifier used below is re-explained from scratch in §0 before any question rests on")
    add("> it.")
    add(">")
    add("> **The user's own clause, which binds the discard ruling when it is put:** a soft-discard")
    add(f"> record is *\"{a['the_ruling_that_ordered_it']['★_the_clause_that_will_bind_the_eventual_discard_ruling']}\"*.")
    add()

    add("## 0. The referents, re-explained from scratch (read this section first)")
    add()
    add("- **The decisions register** — the project's record of WHAT WAS DECIDED about how this")
    add("  system works and whether each decision still stands. It has three surfaces: a data file")
    add("  (`tools/audit/decisions/backbone_decisions.json`), which is the only thing ever edited;")
    add("  a rendered INDEX (`DECISIONS.md`); and rendered group files (`decisions/group_*.md`).")
    add("- **An entry** — one row of that register: a decision's title, the verbatim words it was")
    add("  recorded in at its home document, a plain restatement, where it is recorded, its status,")
    add("  the date and ratifier its original record states, the source of its status, and its")
    add("  recorded reasoning.")
    add("- **A deciding act** — the event in which somebody decided: a user ruling, a")
    add("  ratification, a shelving, a falsification. Naming one means naming who decided, or")
    add("  when, or at which record or event it is written down.")
    add("- **The filter** — the pass that ran before this one. It read each entry's OWN FIELDS and")
    add("  proposed one class per entry: a deciding act is named, no deciding act was found, or the")
    add("  evidence is ambiguous. Its artifact is")
    add("  `tools/audit/decisions_filter_classification.json` and its surface is")
    add("  `ratification_surfaces/cowork_decisions_filter_surface_2026_08_15.md`.")
    add("- **The non-keep population** — the entries the filter placed in the two classes other")
    add("  than *a deciding act is named*. THIS pass covers all of them and nothing else.")
    add("- **Soft-discard** — retired from the live record, **not destroyed** (#12). Nothing on")
    add("  this surface performs one, and no entry here is proposed for one.")
    add("- **The preparation phase** — the first of the six phases the user ruled on 2026-08-15")
    add("  (`cowork_rulings_2026_08_15_phase_definition_sitting.md`). Turning the project's own")
    add("  record into usable inputs for the later derivation; the filtered decisions register is")
    add("  the first of its named outputs.")
    add()

    add("## 1. What this pass was ordered to do, and what it is not")
    add()
    add(f"The ruling is {a['the_ruling_that_ordered_it']['source']}, and what it ordered is quoted:")
    add()
    add(f"> {a['the_ruling_that_ordered_it']['every_sentence_located_in_that_record_on_this_run']['what was ordered']}")
    add()
    add(a["the_ruling_that_ordered_it"]["★_it_is_an_investigation_and_not_a_question"])
    add()
    add("**The filter read the decisions register. This reads the record that register points")
    add("at.** A decision whose entry records no ratifier may still have been ruled in a document")
    add("the entry cites, and until somebody follows the citation nobody knows which.")
    add()
    for name, text in a["★_what_a_result_here_is_NOT"].items():
        add(f"- **{name.replace('_', ' ')}.** {text}")
    add()

    add("## 2. The rule, published beside the results it produced")
    add()
    add("**DERIVED** — nothing below was hand-listed:")
    for item in a["what_is_DERIVED"]:
        add(f"- {item}")
    add()
    add("**AUTHORED** — and marked as such, so a reader sees where the judgment starts:")
    for item in a["what_is_AUTHORED"]:
        add(f"- {item}")
    add()
    add("**The fields read as an entry's cited sources:** "
        + ", ".join(f"`{f}`" for f in a["the_rule"]["fields_read_as_cited_sources"])
        + ". " + a["the_rule"]["why_these_fields"])
    add()
    add("**★ HOW FAR A CITATION IS FOLLOWED.** " + a["the_rule"]["★_how_far_a_citation_is_followed"])
    add()
    add("**★ HOW AN ENTRY'S SUBJECT IS RECOGNISED.** "
        + a["the_rule"]["★_how_a_subject_is_recognised"])
    add()
    add("**★ THE BLOCK RULE.** " + a["the_rule"]["★_the_block_rule_and_why_it_exists"])
    add()
    add("**What counts as a user act:**")
    add()
    for label in a["the_rule"]["the_user_act_markers"]:
        add(f"- {label}")
    add()

    add("## 3. The population and the result")
    add()
    add(f"- Entries covered (the whole non-keep population, imported from the filter's artifact): "
        f"**{a['the_population']['entries']:,}**")
    add(f"- {a['the_population']['★_it_is_imported_and_never_restated']}")
    add()
    add("| result | entries |")
    add("|---|---|")
    for result in RESULTS:
        add(f"| {result} | {a['the_distribution'][result]:,} |")
    add()
    add("**Split by the class the filter proposed**, so the two readings can be compared:")
    add()
    add("| the filter's class | " + " | ".join(RESULTS) + " |")
    add("|---|" + "---|" * len(RESULTS))
    for cls in NON_KEEP:
        cells = " | ".join(f"{a['the_distribution_within_each_class_the_filter_proposed'][cls][r]:,}"
                           for r in RESULTS)
        add(f"| {cls} | {cells} |")
    add()
    add(f"Documents searched: **{a['documents_searched']['count']:,}**.")
    add()
    concentration = a["★_how_concentrated_the_recovered_evidence_is"]
    add("**★ HOW CONCENTRATED THE RECOVERED EVIDENCE IS.** " + concentration["why_it_is_published"])
    add()
    add("- Entries whose whole recovered evidence is ONE passage: "
        f"**{len(concentration['entries_whose_whole_recovered_evidence_is_ONE_passage']):,}**")
    add()
    add("| passage | lines it spans | entries whose evidence it carries |")
    add("|---|---|---|")
    for record in concentration["passages_by_how_many_entries_they_carry"][:12]:
        add(f"| `{record['document']}` line {record['line']} | "
            f"{record['the_passage_spans_lines']:,} | "
            f"{record['entries_whose_recovered_evidence_it_carries']:,} |")
    add()
    add("*(The full table, and which entries each passage carries, is in the artifact.)*")
    add()
    add("**★ WHERE THE BLOCK RULE IS VACUOUS.** "
        + a["the_rule"]["★_where_the_block_rule_is_VACUOUS_and_it_is_named_rather_than_patched"])
    add()

    add("## 4. Every ACT-FOUND entry, with the act quoted and located")
    add()
    add("These are the entries where a passage in a document the entry ITSELF cites carries a")
    add("user-act marker and matches the entry's own subject recogniser. **Reading them is the")
    add("user's act.** Nothing is re-classified here, and the class the filter proposed is carried")
    add("beside each one.")
    add()
    found = [r for r in a["entries"] if r["result"] == ACT_FOUND]
    if not found:
        add("*None.*")
        add()
    for row in found:
        add(f"### {row['id']} — {row['title']}")
        add()
        add(f"- **Recorded at:** `{row['home']}` · **status:** `{row['status']}` · "
            f"**the filter proposed:** {row['the_class_the_filter_proposed']}")
        add(f"- **What the entry says the decision is:** "
            f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
        add(f"- **Passages found:** {row['acts_found_total']:,} "
            f"(quoted here: {row['acts_quoted_here']:,})")
        for act in row["acts"]:
            matched_by = act["what_matched_the_subject"]
            add(f"  - **`{act['document']}` line {act['line']}** "
                f"(a passage of {act['the_passage_spans_lines']:,} lines) — carries "
                + ", ".join(act["the_user_act_markers_the_passage_carries"])
                + f"; matched by {matched_by} (`{act['the_matched_text']}`)")
            add(f"    > {act['the_act_quoted']}")
        add()

    add("## 5. Every NOTHING-FOUND entry, grouped by the evidence shape the filter recorded")
    add()
    add("Every citation these entries carry was followed and every document it resolved to was")
    add("searched. **A NOTHING-FOUND is not a finding that no act exists** — it is a statement")
    add("about the documents the entry's own citations reach, at one level.")
    add()
    for shape, count in a["the_evidence_shapes_among_the_NOTHING_FOUND_entries"].items():
        add(f"### Evidence shape: `{shape}` — {count:,} entries")
        add()
        for row in a["entries"]:
            if (row["result"] != NOTHING_FOUND
                    or row["the_evidence_shape_the_filter_recorded"] != shape):
                continue
            add(f"- **{row['id']}** — {row['title']}")
            add(f"  - *What the entry says the decision is:* "
                f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
            add(f"  - *Recorded at* `{row['home']}`; "
                f"{len(row['where_the_search_looked'])} document(s) searched")
        add()

    add("## 6. Every CITATIONS-UNRESOLVED entry, with the dangling text quoted")
    add()
    add("These entries carry no citation that resolves to a file in the repository, so there was")
    add("nothing to search. This is a per-entry result and never a halt.")
    add()
    stranded = [r for r in a["entries"] if r["result"] == UNRESOLVED]
    if not stranded:
        add("*None.*")
        add()
    for row in stranded:
        add(f"### {row['id']} — {row['title']}")
        add()
        add(f"- **Recorded at:** `{row['home']}` · **the filter proposed:** "
            f"{row['the_class_the_filter_proposed']}")
        add(f"- **What the entry says the decision is:** "
            f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
        for text in row["dangling_citation_text_quoted"]:
            add(f"  - *dangling:* {text}")
        add()

    add("## 7. What this surface does NOT do, and must not be read as doing")
    add()
    add("- **It discards nothing and proposes nothing.** It recovers evidence for the user's")
    add("  ruling, which is put at this return.")
    add("- **It re-classifies no entry.** The filter's proposed class is carried beside every")
    add("  result and is unchanged by anything here.")
    add("- **It edits no decisions-register file.** The data file, the rendered INDEX and the group")
    add("  files are byte-unchanged by the run that produced this surface.")
    add("- **It writes no decisions-register entry**, which the filtering ruling bars until the")
    add("  user rules.")
    add("- **It grades no decision's content**, its conformance, or whether the code obeys it —")
    add("  and nothing here is a judgment on soundness or usefulness.")
    add("- **It performs no rulings sort, no mining, no archiving and no fact-gate admission.**")
    add()
    add("*Generated by `tools/audit/gen_deciding_act_recovery.py` from")
    add("`tools/audit/deciding_act_recovery.json`. Reproduce:")
    add("`python tools/audit/gen_deciding_act_recovery.py --check`.*")
    add()
    return "\n".join(L)


def main(argv: list[str]) -> int:
    artifact, surface = build()
    text = json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"

    if "--check" in argv:
        drift = 0
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("FAIL: the recovery pass does not re-derive:", OUT)
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("FAIL: the recovery surface does not re-derive:", SURFACE)
            drift = 1
        if not drift:
            print("the deciding-act recovery re-derives")
        return drift

    OUT.write_text(text, encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print("wrote", SURFACE.relative_to(ROOT))
    for result in RESULTS:
        print(f"  {result}: {artifact['the_distribution'][result]}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
