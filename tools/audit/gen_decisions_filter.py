#!/usr/bin/env python3
"""CAN A DECIDING ACT BE NAMED FOR EACH ENTRY OF THE DECISIONS REGISTER — and what is the evidence?

THE RULING THIS EXISTS FOR.  User, 2026-08-13, Ruling 8 of
`cowork_rulings_2026_08_13_eighteenth_stop.md`, quoted whole because the whole of it is the test:

    "THE DECISIONS REGISTER IS FILTERED, NOT WHOLESALE RETIRED.  Soft-discard -- retired from the
    live record, not destroyed -- only those entries where **no deciding act can be named**.  *A
    decision ABOUT the code is legitimate; what is not a decision is an observation of what the code
    does, recorded as though it had been decided.*  **Note the register's origin:
    `cc_instruction_decision_harvest.md` lists production code comments as a harvest source**, so
    this class exists by construction."

WHAT THIS FILE DOES, AND THE ONE THING IT DOES NOT.  It walks every entry of the decisions
register's data file, extracts the evidence bearing on whether a deciding act can be named, quoting
each evidence value from the entry's own recorded text, and proposes one class per entry by a
published rule.  **IT DISCARDS NOTHING.**  No entry is retired, edited, moved or marked; the
register's data file and every rendered file it produces are untouched by this tool, which opens
them for reading and writes only its own two outputs.  The classification is a PROPOSAL on a ruling
surface, and the user rules.

THE STOP RULE IT IMPLEMENTS, from the ruled preparation-phase definition
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.1): *"a filter verdict
that cannot name the deciding act STOPS to the user rather than guessing"*.  The third class below,
EVIDENCE-AMBIGUOUS, is that stop rule in artifact form — those entries are proposed to NO fate and
go back to the user as questions.

WHAT IS DERIVED AND WHAT IS AUTHORED — the difference is the whole value of the output.
  DERIVED   the population, read whole from `tools/audit/decisions/backbone_decisions.json` and
            NEVER hand-listed; the entry identities of the rendered INDEX `DECISIONS.md`, read from
            that file and reconciled with the population in BOTH directions; every quoted evidence
            value, taken verbatim from the entry that carries it; the status vocabulary, read from
            the data file's own header rather than invented here; every count.
  AUTHORED  the recognizer patterns below, and the classification rule that reads them.  Both are
            published in the artifact beside the verdicts they produced, so the rule can be checked
            against the evidence without opening this file.

★ THE ONE JUDGMENT CALL IN THE RULE, DECLARED RATHER THAN BURIED.  A recorded DATE with nothing
naming an actor, a ruling record or a ratification event says WHEN something happened and not WHO
did it or WHERE it is recorded.  The rule sends that case to EVIDENCE-AMBIGUOUS rather than to
either outcome.  The reason: Ruling 8 licenses a soft-discard only where no deciding act can be
NAMED, and a bare date does not name one; but a date is a positive trace of an act, so reading it as
*no act* would be the guess the stop rule forbids.  Returning it to the user is the only reading
that is neither.

★ WHAT THE REGISTER-LEVEL RATIFICATION EVENTS DO NOT SUPPLY, stated because it is the strongest
counter-consideration to this whole classification and a reader must meet it.  `DECISIONS.md`'s own
preamble records eleven-plus ratification events over ranges of entries and then says of them: *"The
register-level ratification does not overwrite per-entry provenance -- an entry saying 'ratifier not
stated' still means the original record of THAT decision does not say; what the 2026-08-02
ratifications establish is that these entries are the standing decisions of record."*  So this tool
classifies the ORIGINAL deciding act behind each decision, which is what Ruling 8 asks about.  It is
NOT a reading of whether the entry was ratified as a register entry — that is a different act, it
happened, and it supplies no ratifier the original record never had.

★ THE OBSERVATION-SHAPE LIMB, AND ITS UNMEASURED REACH (#19).  Ruling 8's gloss names a second way
into the soft-discard class: content that is an observation of what the code does, recorded as
though decided.  Two mechanical signals for it are extracted — an entry homed in a production source
file (the harvest source the ruling itself names) and a status whose recorded source is a build-state
marker.  **Neither the recognizers' reach nor their error rate is measured**, and the artifact says
so of itself.  A reader may not take an entry's absence from that limb as evidence that it is not an
observation.

THE STOPS, so this cannot silently stop being an enumeration:
  * an entry missing any field the classification reads STOPS the tool — an entry it cannot classify
    at all is never quietly skipped;
  * a duplicate entry identity STOPS it;
  * a disagreement between the population and the rendered INDEX's entry identities STOPS it, in
    EITHER direction (the dispatch's assumption A2, made mechanical);
  * an entry whose status is outside the data file's own declared status vocabulary STOPS it;
  * a class distribution that does not reconcile with the population size STOPS it.
Each of the five is exercised by a probe recorded in the artifact, and every probe calls the very
function the walk calls, so the two cannot drift apart.

Run:
  python tools/audit/gen_decisions_filter.py           # write the artifact and the ruling surface
  python tools/audit/gen_decisions_filter.py --check   # re-derive both, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
BACKBONE = ROOT / "tools" / "audit" / "decisions" / "backbone_decisions.json"
INDEX = ROOT / "DECISIONS.md"
OUT = ROOT / "tools" / "audit" / "decisions_filter_classification.json"
SURFACE = (ROOT / "ratification_surfaces"
           / "cowork_decisions_filter_surface_2026_08_15.md")

# The three proposed classes. The vocabulary is the dispatch's own and this tool may not widen it.
NAMED = "DECIDING-ACT-NAMED"
NOT_FOUND = "NO-DECIDING-ACT-FOUND"
AMBIGUOUS = "EVIDENCE-AMBIGUOUS"

PROPOSED_FATE = {
    NAMED: "KEEP",
    NOT_FOUND: "SOFT-DISCARD candidate",
    AMBIGUOUS: "NEEDS-THE-USER",
}

# The fields the classification reads. An entry missing one of these is a STOP.
REQUIRED_FIELDS = ("id", "group", "title", "verbatim", "plain", "home", "status", "date",
                   "ratified_by", "status_source", "rationale")

# AUTHORED: the three fields searched for a provenance marker, and why only these three. They are
# the fields that record WHERE a decision comes from: the quotation from its home, the source of its
# status, and its recorded reasoning. `title` and `plain` are the decisions register's own
# restatement of the decision and record no provenance, so a marker found there would be narrative.
PROVENANCE_FIELDS = ("verbatim", "status_source", "rationale")

# AUTHORED: the tokens by which the decisions register says a value is absent. The data file's own
# header declares the meaning — "the record does not say - NEVER inferred" — and these are the
# spellings it uses in the fields.
ABSENT_TOKENS = {"not stated", "not-stated", "none", ""}


class Stop(Exception):
    """The enumeration cannot be published as one. Never a warning, never an entry skipped."""


# ── AUTHORED: the recognizers ────────────────────────────────────────────────────────────────────
#
# POSITIVE — text that NAMES a deciding act: who ruled, or at which record or event.
POSITIVE_RULING_RECORD = [
    ("a ruling record named", re.compile(r"cowork_rulings_[0-9a-z_]+\.md")),
    ("a numbered ruling named", re.compile(r"\bRuling\s+\d+\b")),
    ("a ratification event named", re.compile(
        r"\bratification event\b|\bratified Decision\s+[A-Z]?\d+|\bratified AS DRAFTED\b", re.I)),
    ("a dated user ruling named", re.compile(
        r"\bUser ruling of\s+20\d\d-\d\d-\d\d|\bUser,\s*20\d\d-\d\d-\d\d")),
]
POSITIVE_USER_ACT = [
    ("a user-act marker", re.compile(
        r"user-ruled|user ruled|user-directed|user directed|user-ratified|user ratified|"
        r"ratified by the user|ruled by the user|the user ruled|the user's ruling|"
        r"user mandate|user-mandated|user-authored|user-accepted", re.I)),
]

# NEGATIVE — text in which the record itself says the deciding act cannot be named, or in which the
# entry's ground is what the code IS rather than what anyone decided.
NEGATIVE_NO_RATIFIER_CLAUSE = [
    ("an explicit no-ratifier clause", re.compile(
        r"the record states no ratifier|ratifier (?:and date )?(?:are|is) not stated|"
        r"no ratifier(?: is)? (?:stated|recorded|named)|the record does not (?:say|state) who",
        re.I)),
]
NEGATIVE_BUILD_STATE = [
    ("a build-state marker as the status source", re.compile(
        r"\bBuilt\+Live\b|\bBuilt\b|\bWIRED\b|\bSIGNED\b|\bas-built\b|\bas built\b")),
]

# CONTEXT — extracted because a reader of the evidence should see it, and DELIBERATELY NOT USED by
# the rule. "derivation not recorded" is `CLAUDE.md`'s convention for a missing DEFENSE (why the
# decision was made), which is a different question from whether a deciding act can be named.
CONTEXT_MARKERS = [
    ("derivation not recorded — bears on the DEFENSE, not on the deciding act",
     re.compile(r"derivation not recorded", re.I)),
]

# AUTHORED: what counts as a production source file for the harvest-source limb. Ruling 8 names
# production code comments as a harvest source of this register, so an entry homed in one is an
# observation of what the code does by construction.
SOURCE_FILE_HOME = re.compile(r"^(src/|tools/[^/]*\.(?:cpp|h|hpp|py)\b)")

ISO_DATE = re.compile(r"^20\d\d-\d\d-\d\d$")

# The rendered INDEX's entry rows. One row per entry, opening with the entry identity.
INDEX_ROW = re.compile(r"^\|\s*(D-\d{3})\s*\|", re.M)


def quote(text: str, match: re.Match, width: int = 120) -> str:
    """The matched text with enough of its sentence around it to be checkable by eye."""
    start = max(0, match.start() - width // 2)
    end = min(len(text), match.end() + width // 2)
    fragment = text[start:end].replace("\n", " ").strip()
    return ("..." if start > 0 else "") + fragment + ("..." if end < len(text) else "")


def scan(entry: dict, recognizers: list) -> list[dict]:
    """Every recognizer hit across the provenance fields, each quoted with the field it came from."""
    hits = []
    for field in PROVENANCE_FIELDS:
        text = entry.get(field) or ""
        if not isinstance(text, str):
            continue
        for label, pattern in recognizers:
            match = pattern.search(text)
            if match:
                hits.append({"evidence": label, "field": field,
                             "matched": match.group(0), "quoted": quote(text, match)})
    return hits


def require_fields(entry: dict) -> None:
    """THE FIRST STOP. An entry the classification cannot read is never quietly skipped."""
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        raise Stop(f"entry {entry.get('id', '<no identity>')!r} carries no {missing} — the "
                   f"classification cannot be taken for it, and an entry it cannot classify at "
                   f"all is a STOP rather than a skip")


def normalize_status(value: str) -> str:
    """The comparison form. Declared, narrow, and applied to BOTH sides.

    The data file's header declares one absent-value spelling and its entries use another — a
    disagreement this tool RECORDS and does not repair (the register is not edited here, and a
    disagreement between a record and what it describes is evidence reserved for a later reading).
    Normalizing whitespace to the hyphen the header uses lets the classification proceed without
    either spelling being treated as an unknown status; every spelling that needed it is published
    in the artifact.
    """
    return value.strip().lower().replace(" ", "-")


def require_known_status(entry: dict, vocabulary: set[str]) -> None:
    """THE FOURTH STOP. A status outside the data file's own declared vocabulary."""
    status = entry["status"]
    root = normalize_status(status.split(":")[0])
    if root not in {normalize_status(v) for v in vocabulary}:
        raise Stop(f"entry {entry['id']} carries status {status!r}, whose opening {root!r} is "
                   f"outside the vocabulary the data file's own header declares: "
                   f"{sorted(vocabulary)}")


def require_unique(ids: list[str]) -> None:
    """THE SECOND STOP. A duplicate entry identity."""
    seen, duplicates = set(), []
    for i in ids:
        if i in seen:
            duplicates.append(i)
        seen.add(i)
    if duplicates:
        raise Stop(f"the population carries duplicate entry identities: {sorted(set(duplicates))}")


def reconcile(population: set[str], rendered: set[str]) -> None:
    """THE THIRD STOP — the dispatch's assumption A2, checked in BOTH directions."""
    only_data = sorted(population - rendered)
    only_index = sorted(rendered - population)
    if only_data or only_index:
        raise Stop(
            "the data file and the rendered INDEX do not carry the same entries — a derivation "
            "over a derived population is published WHOLE or not at all (D-671). "
            f"In the data file and not the INDEX: {only_data}. "
            f"In the INDEX and not the data file: {only_index}")


def require_reconciled_distribution(rows: list[dict], population_size: int) -> None:
    """THE FIFTH STOP. The classes must account for the population exactly once each."""
    total = sum(1 for _ in rows)
    if total != population_size:
        raise Stop(f"the classified rows ({total}) do not account for the population "
                   f"({population_size})")
    per_class = {}
    for row in rows:
        per_class[row["proposed_class"]] = per_class.get(row["proposed_class"], 0) + 1
    if sum(per_class.values()) != population_size:
        raise Stop("the per-class distribution does not sum to the population")
    unknown = sorted(c for c in per_class if c not in PROPOSED_FATE)
    if unknown:
        raise Stop(f"a class outside the dispatch's own three-value vocabulary: {unknown}")


def absent(value: str) -> bool:
    return (value or "").strip().lower() in ABSENT_TOKENS


def classify(entry: dict) -> dict:
    """The published rule, applied to one entry. Every branch records the evidence it fired on."""
    ratifiers = [r for r in entry["ratified_by"] if not absent(r)]
    date = (entry["date"] or "").strip()
    dated = bool(ISO_DATE.match(date))

    positive = []
    if ratifiers:
        positive.append({"evidence": "a recorded ratifier", "field": "ratified_by",
                         "matched": ", ".join(ratifiers),
                         "quoted": json.dumps(entry["ratified_by"], ensure_ascii=False)})
    positive += scan(entry, POSITIVE_RULING_RECORD)
    positive += scan(entry, POSITIVE_USER_ACT)

    negative = list(scan(entry, NEGATIVE_NO_RATIFIER_CLAUSE))
    if not ratifiers:
        negative.append({"evidence": "the register's own absent-value token in the ratifier field",
                         "field": "ratified_by", "matched": ", ".join(entry["ratified_by"]),
                         "quoted": json.dumps(entry["ratified_by"], ensure_ascii=False)})
    if not dated:
        negative.append({"evidence": "the register's own absent-value token in the date field",
                         "field": "date", "matched": date, "quoted": date})
    home = (entry["home"] or "")
    if SOURCE_FILE_HOME.match(home):
        negative.append({"evidence": "harvest-source provenance — the entry is homed in a "
                                     "production source file, the harvest source Ruling 8 names",
                         "field": "home", "matched": home, "quoted": home})
    for hit in scan(entry, NEGATIVE_BUILD_STATE):
        if hit["field"] == "status_source":
            hit = dict(hit)
            hit["evidence"] = ("observation-shaped ground — the status's recorded source is a "
                               "build-state marker")
            negative.append(hit)

    context = scan(entry, CONTEXT_MARKERS)

    if positive:
        proposed = NAMED
        shape = "+".join(sorted({h["evidence"] for h in positive}))
        ground = ("the entry's own record names the deciding act, in the evidence quoted below")
    elif dated:
        proposed = AMBIGUOUS
        shape = "a-date-with-no-named-actor-record-or-event"
        ground = ("the entry records WHEN, and nothing in it names WHO or WHERE. A bare date does "
                  "not name a deciding act, so Ruling 8's soft-discard is not licensed; but a date "
                  "is a positive trace of an act, so reading it as no act would be a guess. It "
                  "returns to the user.")
    else:
        proposed = NOT_FOUND
        shapes = sorted({h["evidence"] for h in negative})
        shape = "+".join(shapes)
        ground = ("nothing in the entry names a ratifier, a date, a ruling record or a "
                  "ratification event; the evidence below is what the entry says instead")

    return {
        "id": entry["id"],
        "group": entry["group"],
        "title": entry["title"],
        "home": entry["home"],
        "status": entry["status"],
        # Carried so a reader can apply Ruling 8's OWN test — is this a decision about the code, or
        # an observation of what the code does? — without opening the register. Both are quoted
        # from the entry; neither is used by the rule.
        "plain_restatement_quoted_from_the_entry": entry["plain"],
        "recorded_status_source_quoted_from_the_entry": entry["status_source"],
        "proposed_class": proposed,
        "proposed_fate": PROPOSED_FATE[proposed],
        "evidence_shape": shape,
        "why_this_class": ground,
        "positive_evidence": positive,
        "negative_evidence": negative,
        "context_only_not_used_by_the_rule": context,
    }


def probes(vocabulary: set[str]) -> list[dict]:
    """#19 — the five STOPs, each shown able to fire, each through the walk's own function."""
    out = []

    def probe(name: str, what: str, fn) -> None:
        try:
            fn()
        except Stop as exc:
            out.append({"probe": name, "what_was_fed": what, "raised": True,
                        "message": str(exc)})
            return
        out.append({"probe": name, "what_was_fed": what, "raised": False,
                    "message": "NO STOP — this probe FAILED to establish its stop"})

    probe("a missing field", "an entry carrying every required field but `status_source`",
          lambda: require_fields({f: "x" for f in REQUIRED_FIELDS if f != "status_source"}))
    probe("a duplicate entry identity", "the identity list ['D-001', 'D-002', 'D-001']",
          lambda: require_unique(["D-001", "D-002", "D-001"]))
    probe("an entry in the data file and not the rendered INDEX",
          "population {'D-001','D-002'} against a rendered set {'D-001'}",
          lambda: reconcile({"D-001", "D-002"}, {"D-001"}))
    probe("an entry in the rendered INDEX and not the data file",
          "population {'D-001'} against a rendered set {'D-001','D-002'}",
          lambda: reconcile({"D-001"}, {"D-001", "D-002"}))
    probe("a status outside the data file's own vocabulary",
          "an entry carrying status 'invented-status'",
          lambda: require_known_status({"id": "D-000", "status": "invented-status"}, vocabulary))
    probe("a distribution that does not account for the population",
          "one classified row against a population of two",
          lambda: require_reconciled_distribution(
              [{"proposed_class": NAMED}], 2))

    failed = [p["probe"] for p in out if not p["raised"]]
    if failed:
        raise Stop(f"a probe did not raise, so a STOP this tool claims cannot be shown to fire: "
                   f"{failed}")
    return out


def build() -> tuple[dict, str]:
    if not BACKBONE.exists():
        raise Stop(f"the decisions register's data file is missing: {BACKBONE}")
    if not INDEX.exists():
        raise Stop(f"the rendered INDEX is missing: {INDEX}")

    data = json.loads(BACKBONE.read_text(encoding="utf-8"))
    entries = data["decisions"]
    vocabulary = set(data["header"]["status_vocabulary"].keys())

    require_unique([e.get("id", "<no identity>") for e in entries])
    for entry in entries:
        require_fields(entry)
        require_known_status(entry, vocabulary)

    rendered = set(INDEX_ROW.findall(INDEX.read_text(encoding="utf-8")))
    population = {e["id"] for e in entries}
    reconcile(population, rendered)

    rows = [classify(e) for e in entries]
    require_reconciled_distribution(rows, len(entries))

    per_class = {c: [r for r in rows if r["proposed_class"] == c]
                 for c in (NAMED, NOT_FOUND, AMBIGUOUS)}
    shapes = {}
    for c, members in per_class.items():
        tally = {}
        for r in members:
            tally[r["evidence_shape"]] = tally.get(r["evidence_shape"], 0) + 1
        shapes[c] = dict(sorted(tally.items(), key=lambda kv: (-kv[1], kv[0])))

    ratifier_values = sorted({v for e in entries for v in e["ratified_by"]})
    status_values = sorted({e["status"] for e in entries})
    off_vocabulary_spellings = sorted(
        s for s in status_values
        if s.split(":")[0].strip() not in vocabulary
        and normalize_status(s.split(":")[0]) in {normalize_status(v) for v in vocabulary})

    artifact = {
        "what_this_is":
            "THE DECISIONS-REGISTER FILTER, PROPOSED AND NOT EXECUTED. Every entry of the decisions "
            "register's data file, with the evidence bearing on whether a deciding act can be named "
            "for it quoted from the entry's own recorded text, and one proposed class per entry by "
            "the published rule below. NOTHING IS DISCARDED, RETIRED, EDITED OR MARKED BY THIS "
            "TOOL, and the register's data file and rendered files are untouched.",
        "generator": "tools/audit/gen_decisions_filter.py",
        "dispatch": "cc_instruction_preparation_opening.md, Task 2",
        "the_ruling": {
            "source": "cowork_rulings_2026_08_13_eighteenth_stop.md §2, Ruling 8",
            "quoted_whole":
                "THE DECISIONS REGISTER IS FILTERED, NOT WHOLESALE RETIRED. Soft-discard — retired "
                "from the live record, not destroyed — only those entries where no deciding act can "
                "be named. A decision ABOUT the code is legitimate; what is not a decision is an "
                "observation of what the code does, recorded as though it had been decided. Note "
                "the register's origin: `cc_instruction_decision_harvest.md` lists production code "
                "comments as a harvest source, so this class exists by construction.",
            "the_stop_rule_source":
                "ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md §3.1",
            "the_stop_rule_quoted":
                "a filter verdict that cannot name the deciding act STOPS to the user rather than "
                "guessing; a fact-gate refusal is recorded, never argued around",
            "how_this_tool_obeys_it":
                "The EVIDENCE-AMBIGUOUS class is that stop rule in artifact form: an entry the "
                "rule cannot place returns to the user rather than being guessed either way.",
        },
        "what_is_DERIVED": [
            "the population — every entry of tools/audit/decisions/backbone_decisions.json, never "
            "hand-listed",
            "the rendered INDEX's entry identities, reconciled with the population in BOTH "
            "directions",
            "every quoted evidence value, taken verbatim from the entry that carries it",
            "the status vocabulary, read from the data file's own header",
            "every count and every distribution",
        ],
        "what_is_AUTHORED": [
            "the recognizer patterns, published below beside the verdicts they produced",
            "the classification rule, published below",
            "which three fields are searched for a provenance marker, and why",
        ],
        "the_rule": {
            "fields_searched_for_a_provenance_marker": list(PROVENANCE_FIELDS),
            "why_only_those_three":
                "They are the fields that record WHERE a decision comes from: the quotation from "
                "its home, the source of its status, and its recorded reasoning. `title` and "
                "`plain` are the decisions register's own restatement of the decision and record no "
                "provenance, so a marker found in them would be narrative rather than evidence.",
            "step_1": f"any POSITIVE evidence -> {NAMED} (proposed {PROPOSED_FATE[NAMED]})",
            "step_2": f"no POSITIVE evidence and a recorded ISO date -> {AMBIGUOUS} (proposed "
                      f"{PROPOSED_FATE[AMBIGUOUS]})",
            "step_3": f"no POSITIVE evidence and no recorded date -> {NOT_FOUND} (proposed "
                      f"{PROPOSED_FATE[NOT_FOUND]})",
            "★_the_one_judgment_call_declared":
                "A recorded DATE with nothing naming an actor, a ruling record or a ratification "
                "event says WHEN and not WHO or WHERE. It goes to EVIDENCE-AMBIGUOUS rather than to "
                "either outcome: Ruling 8 licenses a soft-discard only where no deciding act can be "
                "NAMED and a bare date names none, while reading a date as no act at all would be "
                "the guess the stop rule forbids.",
            "positive_recognizers": {label: pattern.pattern for label, pattern
                                     in POSITIVE_RULING_RECORD + POSITIVE_USER_ACT},
            "negative_recognizers": {label: pattern.pattern for label, pattern
                                     in NEGATIVE_NO_RATIFIER_CLAUSE + NEGATIVE_BUILD_STATE},
            "context_recognizers_not_used_by_the_rule": {
                label: pattern.pattern for label, pattern in CONTEXT_MARKERS},
            "absent_value_tokens": sorted(ABSENT_TOKENS),
            "every_ratified_by_value_in_the_population": ratifier_values,
            "every_status_value_in_the_population": status_values,
        },
        "★_a_disagreement_found_while_walking_the_population_and_RECORDED_not_repaired": {
            "what": "The data file's header declares a status vocabulary; its entries use a "
                    "different spelling of one of those values. The status field is not an input "
                    "to the classification, so nothing here turns on it — but a walk of the whole "
                    "population found it, and a finding is surfaced rather than silently smoothed.",
            "the_declared_vocabulary": sorted(vocabulary),
            "spellings_the_entries_use_that_the_header_does_not":
                off_vocabulary_spellings,
            "what_was_done": "NOTHING was repaired. The comparison normalizes whitespace to the "
                             "hyphen the header uses, on BOTH sides, so the classification could "
                             "proceed; the register's data file is byte-unchanged by this run.",
            "why_not_repaired": "This batch edits no register file, and a disagreement between a "
                                "record and what it describes is evidence rather than a defect to "
                                "smooth away — the rule the user ruled into `CLAUDE.md` on "
                                "2026-08-15 in place of D-231's truth half.",
        },
        "★_what_this_classification_is_not": {
            "not_a_reading_of_the_register_level_ratifications":
                "DECISIONS.md's own preamble records ratification events over ranges of entries and "
                "then says of them: \"The register-level ratification does not overwrite per-entry "
                "provenance — an entry saying 'ratifier not stated' still means the original record "
                "of THAT decision does not say; what the 2026-08-02 ratifications establish is that "
                "these entries are the standing decisions of record.\" This tool classifies the "
                "ORIGINAL deciding act behind each decision, which is what Ruling 8 asks about. "
                "That those events happened, and that they supply no ratifier the original record "
                "never had, are both true and neither is a verdict of this tool.",
            "not_a_judgment_about_whether_a_decision_is_good_or_still_right":
                "Nothing here grades a decision's content, its conformance, or whether the code "
                "obeys it.",
            "the_observation_shape_limb_has_UNMEASURED_reach":
                "Ruling 8's gloss names content that is an observation of what the code does, "
                "recorded as though decided. Two mechanical signals for it are extracted — an entry "
                "homed in a production source file, and a status whose recorded source is a "
                "build-state marker. NEITHER THE RECOGNIZERS' REACH NOR THEIR ERROR RATE IS "
                "MEASURED (#19). An entry's absence from that limb is not evidence that it is not "
                "an observation.",
        },
        "the_population": {
            "entries_in_the_data_file": len(entries),
            "entry_identities_in_the_rendered_INDEX": len(rendered),
            "reconciled_both_ways": True,
            "★_reconciliation_is_a_STOP_not_a_report":
                "A disagreement in either direction halts this tool before it writes, so a "
                "committed artifact reporting a reconciled population is the only kind that can "
                "exist (D-671 — a derivation over a derived population is published whole or not "
                "at all).",
        },
        "the_distribution": {c: len(members) for c, members in per_class.items()},
        "the_evidence_shapes_within_each_class": shapes,
        "the_stops_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not":
                "They establish that each of the five STOPs CAN fire, each through the very "
                "function the walk calls, so the two cannot drift apart. They establish NOTHING "
                "about whether any entry is in the right class — that is what the ruling surface "
                "puts to the user.",
            "probes": probes(vocabulary),
        },
        "entries": rows,
    }
    return artifact, render(artifact)


# ── the ruling surface, rendered FROM the artifact ───────────────────────────────────────────────

def render(a: dict) -> str:
    L: list[str] = []

    def add(line: str = "") -> None:
        L.append(line)

    add("# The decisions-register filter — a proposed class for every entry, and NOTHING discarded")
    add()
    add("> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING HAS BEEN")
    add("> DISCARDED; the decisions register stays under the filtering ruling until the user")
    add("> rules.** Generated by `tools/audit/gen_decisions_filter.py` from")
    add("> `tools/audit/decisions_filter_classification.json`, which it writes in the same run. No")
    add("> entry has been retired, edited, moved or marked; the register's data file and every")
    add("> rendered file it produces are byte-unchanged. Per the standing presentation rule")
    add("> (`cowork_rulings_2026_08_15_batch_return.md` §5) every identifier used below is")
    add("> re-explained from scratch in §0 before any question rests on it.")
    add()

    add("## 0. The referents, re-explained from scratch (read this section first)")
    add()
    add("- **The decisions register** — the project's record of WHAT WAS DECIDED about how this")
    add("  system works and whether each decision still stands. It has three surfaces: a data file")
    add("  (`tools/audit/decisions/backbone_decisions.json`), which is the only thing ever edited;")
    add("  a rendered INDEX (`DECISIONS.md`); and rendered group files (`decisions/group_*.md`).")
    add("  The two rendered surfaces are generated from the data file and are never hand-written.")
    add("- **An entry** — one row of that register: a decision's title, the verbatim words it was")
    add("  recorded in at its home document, a plain restatement, where it is recorded, its status,")
    add("  the date and ratifier its original record states, the source of its status, and its")
    add("  recorded reasoning.")
    add("- **A deciding act** — the event in which somebody decided: a user ruling, a ratification,")
    add("  a shelving, a falsification. Naming one means naming who decided, or when, or at which")
    add("  record or event it is written down.")
    add("- **Ruling 8** — the user's ruling of 2026-08-13")
    add("  (`cowork_rulings_2026_08_13_eighteenth_stop.md` §2), quoted whole in §1 below. It is the")
    add("  whole authority for this surface.")
    add("- **Soft-discard** — Ruling 8's own word: retired from the live record, **not destroyed**")
    add("  (#12). Nothing on this surface performs one; every proposal below is a candidacy.")
    add("- **The preparation phase** — the first of the six phases the user ruled on 2026-08-15")
    add("  (`cowork_rulings_2026_08_15_phase_definition_sitting.md` §2). Its purpose is to turn the")
    add("  project's own record into usable inputs for the later derivation, and the filtered")
    add("  decisions register is the first of its named outputs.")
    add("- **The stop rule this surface obeys** — from that phase's ruled definition")
    add(f"  (`{a['the_ruling']['the_stop_rule_source']}`): "
        f"*\"{a['the_ruling']['the_stop_rule_quoted']}.\"* "
        f"{a['the_ruling']['how_this_tool_obeys_it']}")
    add("- **The fact-gate** — the admission test in front of the empirical findings ledger, named")
    add("  here only because that stop rule mentions it. Nothing on this surface passes through it.")
    add()

    add("## 1. The ruling this surface serves, quoted whole")
    add()
    add(f"> {a['the_ruling']['quoted_whole']}")
    add()
    add(f"*Source: {a['the_ruling']['source']}.*")
    add()

    add("## 2. What was derived, what was authored, and the rule")
    add()
    add("**DERIVED** — nothing below was hand-listed:")
    for item in a["what_is_DERIVED"]:
        add(f"- {item}")
    add()
    add("**AUTHORED** — and marked as such on its face, so a reader sees where the judgment starts:")
    for item in a["what_is_AUTHORED"]:
        add(f"- {item}")
    add()
    add("**The rule, applied to every entry in order:**")
    add()
    add(f"1. {a['the_rule']['step_1']}")
    add(f"2. {a['the_rule']['step_2']}")
    add(f"3. {a['the_rule']['step_3']}")
    add()
    add("**★ THE ONE JUDGMENT CALL, DECLARED RATHER THAN BURIED.** "
        + a["the_rule"]["★_the_one_judgment_call_declared"])
    add()
    add("**The fields searched for a provenance marker:** "
        + ", ".join(f"`{f}`" for f in a["the_rule"]["fields_searched_for_a_provenance_marker"])
        + ". " + a["the_rule"]["why_only_those_three"])
    add()

    add("## 3. What this classification is NOT — read before the proposals")
    add()
    for key, text in a["★_what_this_classification_is_not"].items():
        add(f"- **{key.replace('_', ' ')}.** {text}")
    add()

    add("## 4. The population, and the reconciliation that guards it")
    add()
    add(f"- Entries in the data file: **{a['the_population']['entries_in_the_data_file']:,}**")
    add("- Entry identities in the rendered INDEX: "
        f"**{a['the_population']['entry_identities_in_the_rendered_INDEX']:,}**")
    add(f"- {a['the_population']['★_reconciliation_is_a_STOP_not_a_report']}")
    add()
    add("**The proposed distribution:**")
    add()
    add("| proposed class | proposed fate | entries |")
    add("|---|---|---|")
    for cls in (NAMED, AMBIGUOUS, NOT_FOUND):
        add(f"| {cls} | {PROPOSED_FATE[cls]} | {a['the_distribution'][cls]:,} |")
    add()
    add("**The evidence shapes inside each class** — what the entries of a class actually carry, so")
    add("the class is not read as one undifferentiated mass:")
    add()
    for cls in (NAMED, AMBIGUOUS, NOT_FOUND):
        add(f"*{cls}:*")
        add()
        for shape, count in a["the_evidence_shapes_within_each_class"][cls].items():
            add(f"- `{shape}` — {count:,}")
        add()

    add("## 5. Every proposed SOFT-DISCARD candidate, with its quoted evidence")
    add()
    add("These are the entries where the rule found nothing naming a deciding act — no ratifier, no")
    add("date, no ruling record, no ratification event. **Ruling 8 licenses a soft-discard here and")
    add("this surface performs none.** Each is listed with what the entry says instead.")
    add()
    add("**★ RULING 8 HAS A SECOND LIMB AND THIS TOOL DOES NOT DECIDE IT.** The ruling's own gloss")
    add("is that *a decision ABOUT the code is legitimate; what is not a decision is an observation")
    add("of what the code does, recorded as though it had been decided.* That is a question about")
    add("CONTENT, and no recognizer settles it. So every member below carries two further quotations")
    add("from its own entry — what the entry says the decision is, and the source it gives for its")
    add("status — so the limb can be applied by reading rather than by opening the register. Where")
    add("that reading finds a decision, the entry belongs in the live record whatever its provenance")
    add("field says, and this listing is the place to say so.")
    add()
    _render_members(add, a, NOT_FOUND)

    add("## 6. Every proposed NEEDS-THE-USER entry, with its quoted evidence")
    add()
    add("These are the entries the rule refuses to place. Each records WHEN something happened and")
    add("names no actor, no ruling record and no ratification event. Under the phase's stop rule")
    add("they return to the user rather than being guessed either way.")
    add()
    _render_members(add, a, AMBIGUOUS)

    add("## 7. The proposed KEEP entries")
    add()
    add("Listed by identity only: the rule found evidence naming a deciding act in each, the")
    add("evidence is quoted per entry in the artifact, and nothing is proposed to happen to them.")
    add()
    kept = [r for r in a["entries"] if r["proposed_class"] == NAMED]
    add("<details><summary>The proposed KEEP entries (DERIVED)</summary>")
    add()
    for row in kept:
        add(f"- **{row['id']}** — {row['title']} *(`{row['evidence_shape']}`)*")
    add()
    add("</details>")
    add()

    found = a["★_a_disagreement_found_while_walking_the_population_and_RECORDED_not_repaired"]
    add("## 7a. One disagreement found while walking the population, recorded and not repaired")
    add()
    add(f"{found['what']}")
    add()
    add("- **The vocabulary the data file's header declares:** "
        + ", ".join(f"`{v}`" for v in found["the_declared_vocabulary"]))
    add("- **The spelling its entries use that the header does not:** "
        + ", ".join(f"`{v}`" for v in found["spellings_the_entries_use_that_the_header_does_not"]))
    add(f"- **What was done:** {found['what_was_done']}")
    add(f"- **Why it was not repaired:** {found['why_not_repaired']}")
    add()

    add("## 8. What this surface does NOT do, and must not be read as doing")
    add()
    add("- **It discards nothing.** Every proposal is a candidacy awaiting the user; soft-discard is")
    add("  retirement from the live record and destroys nothing (#12).")
    add("- **It edits no entry and no register file.** The data file, the rendered INDEX and the")
    add("  rendered group files are byte-unchanged by the run that produced this surface.")
    add("- **It writes no decisions-register entry**, which the filtering ruling bars until the user")
    add("  rules on this surface.")
    add("- **It grades no decision's content**, its conformance, or whether the code obeys it.")
    add("- **It performs no rulings sort, no mining, no archiving and no fact-gate admission** —")
    add("  those are the preparation phase's other outputs and none of them is started here.")
    add()
    add("*Generated by `tools/audit/gen_decisions_filter.py` from")
    add("`tools/audit/decisions_filter_classification.json`. Reproduce:")
    add("`python tools/audit/gen_decisions_filter.py --check`.*")
    add()
    return "\n".join(L)


def _render_members(add, a: dict, cls: str) -> None:
    members = [r for r in a["entries"] if r["proposed_class"] == cls]
    for row in members:
        add(f"### {row['id']} — {row['title']}")
        add()
        add(f"- **Recorded at:** `{row['home']}` · **status:** `{row['status']}` · "
            f"**group:** {row['group']}")
        add(f"- **What the entry says the decision is:** {row['plain_restatement_quoted_from_the_entry']}")
        add(f"- **The source the entry gives for its status:** {row['recorded_status_source_quoted_from_the_entry']}")
        add(f"- **Why this class:** {row['why_this_class']}")
        add("- **The evidence the rule fired on:**")
        for hit in row["negative_evidence"]:
            add(f"  - *{hit['evidence']}* — in the `{hit['field']}` field: "
                f"`{hit['matched']}`")
        for hit in row["context_only_not_used_by_the_rule"]:
            add(f"  - *(context, not used by the rule)* {hit['evidence']} — in the "
                f"`{hit['field']}` field")
        add()


def main(argv: list[str]) -> int:
    artifact, surface = build()
    text = json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"

    if "--check" in argv:
        drift = 0
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("FAIL: the classification does not re-derive:", OUT)
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("FAIL: the ruling surface does not re-derive:", SURFACE)
            drift = 1
        if not drift:
            print("the decisions-register filter re-derives")
        return drift

    OUT.write_text(text, encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print("wrote", SURFACE.relative_to(ROOT))
    for cls in (NAMED, AMBIGUOUS, NOT_FOUND):
        print(f"  {cls}: {artifact['the_distribution'][cls]} "
              f"(proposed {PROPOSED_FATE[cls]})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
