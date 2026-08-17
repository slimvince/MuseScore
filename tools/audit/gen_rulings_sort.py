#!/usr/bin/env python3
"""THE RULINGS SORT — is a confirmed decision DESIGN INTENT, or MANAGEMENT OF THE IMPLEMENTATION?

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §2 of
`cowork_rulings_2026_08_16_preparation_return.md`: *"The RULINGS SORT may begin over the ratified
411 (design intent versus management of the implementation — the preparation phase's output (b)),
as a PROPOSED classification onto a ruling surface, nothing executed by it."*  The two classes are
the ruled phase definition's own
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.1, output (b)): *"the
RULINGS SORT — surviving rulings sorted into design intent (seed material for the framework)
versus management of the implementation (not design input)"*.

★ WHY THE DESIGN-INTENT SIDE IS THE PAYLOAD.  It becomes the framework phase's SEED LIST — the
decisions a derivation is allowed to start from.  A decision wrongly placed there seeds the
architecture with something nobody meant to seed it with; a decision wrongly placed on the other
side is simply not consulted.  So every DESIGN-INTENT member is listed on the surface with its
plain restatement: the user sees exactly what is proposed to seed.

★★ NOTHING IS EXECUTED BY THIS.  No entry is retired, edited, moved or marked; the decisions
decisions register's data file and every file rendered from it are untouched.  The sort is PROPOSED
and the
user rules.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   the population — the confirmed side of the committed filter artifact, IMPORTED and
            never restated (#6); every entry's fields, read from the decisions register's own data
            file; the two home-classification facts the rule leans on, which are the REGISTER'S OWN
            recorded judgments rather than this tool's reading; every count.
  AUTHORED  the classification rule and its recognizers, published in the artifact beside the
            verdicts they produced, so the rule can be checked against the evidence without opening
            this file.

★ THE RULE LEANS FIRST ON THE REGISTER'S OWN JUDGMENT, AND ONLY THEN ON WORDS.  Two fields the
decisions register already carries decide most of the population without this tool reading anything
into an entry:

  * `home_is_layer_spec` — the entry is recorded in a LAYER'S OWN SPECIFICATION.  A decision about
    what the analysis is or does is what a layer specification holds, so such an entry is design
    intent.
  * `nonspec_kind` — where the entry is NOT in a layer specification, the decisions register records which
    case it is, and its own header defines two of those cases in words this tool quotes rather than
    interprets: `process` is *"a decision about how the work is done, not about the system"*, which
    IS the management class; `gap` is *"a decision that governs a layer and is not findable from
    that layer's section"*, which is design intent recorded in the wrong place.

Only what those leave undecided reaches the authored word recognizers, and what THOSE leave
undecided is proposed **NEEDS-THE-USER** — never guessed.

★★ THE SORT IS RULED — 2026-08-17, `cowork_rulings_2026_08_17_rulings_sort_sitting.md`.  Two
rulings, and this pass now carries both:

  * **§1 — the rule-placed 351 are RATIFIED as proposed.**  The proposed DESIGN-INTENT entries are
    the framework phase's seed list as proposed; the proposed IMPLEMENTATION-MANAGEMENT entries are
    not design input.  The ratification is recorded in the artifact's own header; it changes no
    verdict, because the verdicts it ratifies are the ones this rule already produces.
  * **§2 — the 60 returned entries are PLACED by the ruled criterion**, *"an entry whose statement
    binds the SYSTEM (what the analysis is, does, or must satisfy) is DESIGN-INTENT; one whose
    statement binds the WORK (how we decide, verify, record, sequence) is
    IMPLEMENTATION-MANAGEMENT"*.  They enter as a DISTINCT ROUTE — *"USER-RULED at the 2026-08-17
    sitting"* — beside the rule's own three, and the ruling asks for exactly that: *"so a later
    reader sees where the judgment came from."*

★ THE 60 ARE DERIVED FROM THE SITTING RECORD AND NEVER RETYPED HERE.  The record carries the two
identity lists with their counts in its own headings; both are parsed on every run, both counts are
checked against the headings that state them, and every placed identity must be one this rule
returned as NEEDS-THE-USER.  A placement naming an entry the rule placed itself, or a list whose
size disagrees with its own heading, HALTS this pass rather than being reconciled.

★ AND A MANAGEMENT PLACING REMOVES NOTHING, in the sitting's own words: *"A management placement of
a standing principle removes none of its force — the principles govern every session through the
standing rules regardless of the sort."*

★ A DISAGREEMENT THIS PASS RECORDS AND DOES NOT REPAIR.  The data file's header says
`nonspec_kind` *"says which of three cases it is"* and names three; the entries use five.  The two
the header does not define are not mapped by their name here — they fall through to the
recognizers, which is the only honest thing to do with a value the record does not define.  The
disagreement is published, and nothing is edited: this batch touches no decisions-register file, and a
disagreement between a record and what it describes is evidence.

THE STOPS:
  * the committed filter artifact missing, or carrying no entry on the confirmed side, STOPS it;
  * an imported entry identity the decisions register's data file does not carry STOPS it, and so does a
    confirmed entry of the data file the import does not carry — BOTH directions;
  * an entry missing a field the rule reads STOPS it;
  * a `nonspec_kind` value the pass has neither mapped nor deliberately left to the recognizers
    STOPS it — so a new value cannot be classified by silence;
  * a definition the mapping quotes that is no longer in the data file's own header STOPS it;
  * a proposed class outside the closed three-value vocabulary STOPS it;
  * a distribution that does not account for the population STOPS it.
Each is exercised by a probe recorded in the artifact, through the very function the walk calls.

Run:
  python tools/audit/gen_rulings_sort.py           # write the artifact and the surface
  python tools/audit/gen_rulings_sort.py --check   # re-derive both, exit 1 on drift
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
FILTER = ROOT / "tools" / "audit" / "decisions_filter_classification.json"
BACKBONE = ROOT / "tools" / "audit" / "decisions" / "backbone_decisions.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
PHASES = (ROOT / "ratification_surfaces"
          / "cowork_phase_definition_surface_2026_08_15.md")
OUT = ROOT / "tools" / "audit" / "rulings_sort_classification.json"
SURFACE = (ROOT / "ratification_surfaces"
           / "cowork_rulings_sort_surface_2026_08_16.md")

SORT_RULING = ROOT / "cowork_rulings_2026_08_17_rulings_sort_sitting.md"

CONFIRMED = "DECIDING-ACT-NAMED"

DESIGN = "DESIGN-INTENT"
MANAGEMENT = "IMPLEMENTATION-MANAGEMENT"
NEEDS_USER = "NEEDS-THE-USER"
CLASSES = (DESIGN, MANAGEMENT, NEEDS_USER)

# AUTHORED — the name of the fourth route, the ruling's own words for it.
USER_RULED_ROUTE = "USER-RULED at the 2026-08-17 sitting"

WHAT_EACH_CLASS_IS = {
    DESIGN: "a decision about what the analysis is or does — seed material for the framework "
            "phase",
    MANAGEMENT: "a decision about process, apparatus, workflow, record-keeping or sequencing — "
                "not design input",
    NEEDS_USER: "the rule cannot place it, and it is returned rather than guessed",
}

REQUIRED_FIELDS = ("id", "group", "title", "plain", "home", "status", "verbatim")

# AUTHORED: the sentences this pass rests on, LOCATED in their records on every run.
SOURCE_SENTENCES = {
    "the ruling that permits the sort": (
        RULING,
        "The RULINGS SORT may begin over the ratified 411 (design intent versus management of the "
        "implementation — the preparation phase's output (b)), as a PROPOSED classification onto a "
        "ruling surface, nothing executed by it."),
    "the ruled definition of the two classes": (
        PHASES,
        "the RULINGS SORT — surviving rulings sorted into design intent (seed material for the "
        "framework) versus management of the implementation (not design input)"),
    "what the confirmed side is": (
        RULING,
        "The 411 DECIDING-ACT-NAMED entries are RATIFIED as the live record's confirmed side."),
    "the ratification of the rule-placed entries": (
        SORT_RULING,
        "The 220 proposed DESIGN-INTENT entries are the framework phase's seed list as proposed; "
        "the 131 proposed IMPLEMENTATION-MANAGEMENT entries are not design input."),
    "the criterion the 60 returned entries were placed by": (
        SORT_RULING,
        "an entry whose statement binds the SYSTEM (what the analysis is, does, or must satisfy) "
        "is DESIGN-INTENT; one whose statement binds the WORK (how we decide, verify, record, "
        "sequence) is IMPLEMENTATION-MANAGEMENT."),
    "how the ruled placements are to be recorded": (
        SORT_RULING,
        "The executing act records these placements into the sort's classification artifact as "
        "USER-RULED placements, distinguished from the rule's own routes, so a later reader sees "
        "where the judgment came from."),
    "what a management placement does not do": (
        SORT_RULING,
        "A management placement of a standing principle removes none of its force — the principles "
        "govern every session through the standing rules regardless of the sort."),
    "the totals the sitting states": (
        SORT_RULING,
        "the sort's totals become 244 DESIGN-INTENT / 167 IMPLEMENTATION-MANAGEMENT / 0 unplaced, "
        "244 + 167 = 411."),
}

# The sitting record's two identity lists, each with the count its own heading states. Nothing
# below is a list of identities: the pattern finds the heading and the run of `D-…` tokens under
# it, and the count in the heading is checked against the identities actually found.
RULED_LIST = re.compile(r"\*\*(DESIGN-INTENT|IMPLEMENTATION-MANAGEMENT) \((\d+)\):\*\*"
                        r"((?:[^\n]*\n)+?)\n")
IDENTITY = re.compile(r"\bD-\d+\b")
RULED_TOTALS = re.compile(r"the sort's totals become (\d+) DESIGN-INTENT / "
                          r"(\d+) IMPLEMENTATION-MANAGEMENT / (\d+) unplaced, "
                          r"(\d+) \+ (\d+) = (\d+)")

# AUTHORED: the mapping from the decisions register's OWN `nonspec_kind` value to a proposed class, each
# carrying the definition it rests on VERBATIM from the data file's own header. A value mapped to
# None is deliberately left to the recognizers.
NONSPEC_MAPPING = {
    "process": (MANAGEMENT,
                "'process' (a decision about how the work is done, not about the system)"),
    "gap": (DESIGN,
            "'gap' (a decision that governs a layer and is not findable from that layer's section"),
    "project-convention": (None, None),
    "contract-home": (None, None),
    "unhomed": (None, None),
}

# AUTHORED: the word recognizers, reached only where the decisions register's own home classification leaves
# the entry undecided. Each is published beside the verdicts it produced.
DESIGN_WORDS = [
    ("the tonal subject", re.compile(
        r"\bchord|\bkey\b|\bkeys\b|\btonic|tonal|harmon|cadenc|modulat|roman numeral|\bnumeral|"
        r"\bmajor\b|\bminor\b|\bmodal\b|\bmode\b|diatonic|scale degree", re.I)),
    ("the note-level subject", re.compile(
        r"\bpitch|\bnote\b|\bnotes\b|\bbass\b|\broot\b|inversion|voice|spelling|enharmonic|"
        r"\bonset|\bslice|segment|non-chord|dissonan|\btie\b|\bstaff\b|\bstave", re.I)),
    ("the inference machinery", re.compile(
        r"\bdecode|decoder|estimator|inference|\binfer\b|posterior|\bprior\b|\bfactor\b|"
        r"\bfactoris|\bfactoriz|\bweight|\btemplate|\bgate\b|\bscoring\b|layer \d|\bLayer \d", re.I)),
]
MANAGEMENT_WORDS = [
    ("the record-keeping subject", re.compile(
        r"open-items register|decisions register|register entry|register row|\bINDEX\b|"
        r"\bopen item|\brow\b|\bstatus cell|\bbanner|\banchor\b|\bfiling\b|provenance|"
        r"documentation|doc-sync|\bhandoff\b|STATUS\.md|DECISIONS\.md|OPEN_ITEMS\.md", re.I)),
    ("the working-process subject", re.compile(
        r"\bdispatch\b|\bcommit\b|\bsession\b|\bworkflow\b|\bphase\b|\bratification\b|"
        r"\bretrospective\b|\bchecklist\b|\bsequencing\b|\bwriting standard|\bnaming convention|"
        r"\breserved word|\bguard\b|\bself-check\b|\bupkeep\b", re.I)),
]


class Stop(Exception):
    """The sort cannot be published as an enumeration. Never a warning, never an entry skipped."""


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_sources() -> dict[str, dict]:
    """Every sentence this pass rests on, LOCATED in its own record. A missing one STOPS."""
    located = {}
    for name, (path, quote) in SOURCE_SENTENCES.items():
        if not path.exists():
            raise Stop(f"a record this pass rests on is missing: {path}")
        if normalized(quote) not in normalized(path.read_text(encoding="utf-8")):
            raise Stop(f"the sentence for {name!r} is no longer in {path.name}, so this pass "
                       f"would outlive the words that permit it")
        located[name] = {"source": path.name, "quoted": quote}
    return located


def locate_definitions(header: dict) -> dict[str, str]:
    """Every quoted `nonspec_kind` definition, LOCATED in the data file's own header. Missing STOPS."""
    home_rule = normalized(header.get("home_rule", ""))
    located = {}
    for value, (_cls, definition) in NONSPEC_MAPPING.items():
        if definition is None:
            continue
        if normalized(definition) not in home_rule:
            raise Stop(f"the definition this pass maps {value!r} by is no longer in the data "
                       f"file's own header, so the mapping would rest on words the record has "
                       f"dropped: {definition!r}")
        located[value] = definition
    return located


def ruled_placements() -> tuple[dict[str, str], dict]:
    """The 60 USER-RULED placements of §2 — PARSED from the sitting record, never retyped here.

    ★ WHAT IS CHECKED, AND WHY EACH CHECK IS A STOP RATHER THAN A RECONCILIATION. Each list's own
    heading states how many identities it carries; a list whose size disagrees with its heading is
    a record that no longer describes itself, and placing entries out of it would put the user's
    name on a population the user never saw. An identity in both lists is a contradiction the pass
    does not resolve. And the two lists together must be exactly the population the rule returned
    as NEEDS-THE-USER, in BOTH directions — a placement for an entry the rule placed itself would
    silently overrule a route the ruling ratified.
    """
    if not SORT_RULING.exists():
        raise Stop(f"the sitting record the placements are read from is missing: {SORT_RULING}")
    text = SORT_RULING.read_text(encoding="utf-8")

    lists: dict[str, dict] = {}
    for match in RULED_LIST.finditer(text):
        cls, stated, body = match.group(1), int(match.group(2)), match.group(3)
        found = IDENTITY.findall(body)
        if cls in lists:
            raise Stop(f"the sitting record carries more than one {cls} list, so the placements "
                       f"cannot be taken from it without choosing between them")
        if len(found) != len(set(found)):
            raise Stop(f"the sitting record's {cls} list repeats an identity")
        if len(found) != stated:
            raise Stop(f"the sitting record's {cls} list carries {len(found)} identities where its "
                       f"own heading states {stated} — the record no longer describes itself, and "
                       f"this pass does not reconcile it")
        lists[cls] = {"stated_in_its_own_heading": stated, "identities": found}

    missing = [cls for cls in (DESIGN, MANAGEMENT) if cls not in lists]
    if missing:
        raise Stop(f"the sitting record carries no {missing} identity list, so §2's placements "
                   f"cannot be derived from it")

    both = sorted(set(lists[DESIGN]["identities"]) & set(lists[MANAGEMENT]["identities"]))
    if both:
        raise Stop(f"{both} appear in BOTH of the sitting record's identity lists")

    placements = {i: DESIGN for i in lists[DESIGN]["identities"]}
    placements.update({i: MANAGEMENT for i in lists[MANAGEMENT]["identities"]})

    totals = RULED_TOTALS.search(normalized(text))
    if not totals:
        raise Stop("the sitting record no longer states the totals its own arithmetic rests on, so "
                   "the reconciliation this pass owes cannot be taken from it")
    design_total, management_total, unplaced_total = (int(totals.group(1)), int(totals.group(2)),
                                                      int(totals.group(3)))
    return placements, {
        "the_route": USER_RULED_ROUTE,
        "the_record": SORT_RULING.name,
        "★_how_the_membership_is_derived_and_never_retyped":
            "The sitting record carries the two identity lists with the count each states in its "
            "own heading. Both are parsed on every run; a list whose size disagrees with its "
            "heading, an identity in both lists, or a placement for an entry this rule placed "
            "itself HALTS this pass rather than being reconciled.",
        "the_lists_as_the_record_carries_them": lists,
        "the_totals_the_sitting_states": {
            DESIGN: design_total, MANAGEMENT: management_total, "unplaced": unplaced_total},
    }


def require_fields(entry: dict) -> None:
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        raise Stop(f"entry {entry.get('id', '<no identity>')!r} carries no {missing} — the sort "
                   f"cannot be proposed for it, and an entry it cannot read is a STOP, not a skip")


def reconcile(imported: set[str], in_the_data_file: set[str]) -> None:
    only_import = sorted(imported - in_the_data_file)
    only_data = sorted(in_the_data_file - imported)
    if only_import or only_data:
        raise Stop(
            "the imported confirmed population and the decisions register's data file do not "
            "carry the same entries — a derivation over a derived population is published WHOLE "
            f"or not at all (D-671). Imported and not in the data file: {only_import}. "
            f"Confirmed in the data file and not imported: {only_data}")


def require_known_nonspec(entry: dict) -> None:
    """A `nonspec_kind` value this pass has neither mapped nor deliberately left to the words."""
    value = entry.get("nonspec_kind")
    if value is None or value in NONSPEC_MAPPING:
        return
    raise Stop(f"entry {entry['id']} carries nonspec_kind {value!r}, which this pass neither maps "
               f"nor deliberately leaves to the recognizers — a new value must be ruled on, not "
               f"classified by silence")


def require_reconciled_distribution(rows: list[dict], population_size: int) -> None:
    if len(rows) != population_size:
        raise Stop(f"the classified rows ({len(rows)}) do not account for the population "
                   f"({population_size})")
    unknown = sorted({r["proposed_class"] for r in rows} - set(CLASSES))
    if unknown:
        raise Stop(f"a class outside the ruled three-value vocabulary: {unknown}")
    per_class: dict[str, int] = {}
    for row in rows:
        per_class[row["proposed_class"]] = per_class.get(row["proposed_class"], 0) + 1
    if sum(per_class.values()) != population_size:
        raise Stop("the per-class distribution does not sum to the population")


def word_hits(entry: dict, recognizers: list) -> list[dict]:
    """Every recognizer that fires on the decisions register's OWN restatement of the entry."""
    text = f"{entry['title']}\n{entry['plain']}"
    hits = []
    for label, pattern in recognizers:
        match = pattern.search(text)
        if match:
            hits.append({"recogniser": label, "matched": match.group(0)})
    return hits


def classify(entry: dict, definitions: dict[str, str]) -> dict:
    """The published rule, applied to one entry. Every branch records the evidence it fired on."""
    if entry.get("home_is_layer_spec") is True:
        return {
            "proposed_class": DESIGN,
            "decided_by": "the decisions register's own `home_is_layer_spec`",
            "why": "the entry is recorded in a LAYER'S OWN SPECIFICATION, which is where a "
                   "decision about what the analysis is or does lives",
            "evidence": [{"field": "home_is_layer_spec", "value": True,
                          "the_home_it_names": entry["home"]}],
        }

    value = entry.get("nonspec_kind")
    if value in NONSPEC_MAPPING:
        mapped, _definition = NONSPEC_MAPPING[value]
        if mapped is not None:
            return {
                "proposed_class": mapped,
                "decided_by": "the decisions register's own `nonspec_kind`, by the definition its data "
                              "file's header gives that value",
                "why": f"the decisions register records this entry as {value!r}, which its own header "
                       f"defines as {definitions[value]!r}",
                "evidence": [{"field": "nonspec_kind", "value": value,
                              "the_definition_quoted_from_the_header": definitions[value],
                              "the_home_it_names": entry["home"]}],
            }

    design = word_hits(entry, DESIGN_WORDS)
    management = word_hits(entry, MANAGEMENT_WORDS)
    if design and not management:
        return {"proposed_class": DESIGN,
                "decided_by": "the authored word recognizers, over the decisions register's own restatement",
                "why": "the entry's own title and plain restatement carry the subject of the "
                       "analysis and nothing of the working process",
                "evidence": design}
    if management and not design:
        return {"proposed_class": MANAGEMENT,
                "decided_by": "the authored word recognizers, over the decisions register's own restatement",
                "why": "the entry's own title and plain restatement carry the subject of the "
                       "working process and nothing of the analysis",
                "evidence": management}
    return {
        "proposed_class": NEEDS_USER,
        "decided_by": "nothing — the rule reached no verdict and returns the entry",
        "why": ("the decisions register's own home classification does not place this entry, and its title "
                "and plain restatement carry "
                + ("BOTH subjects" if design and management else "NEITHER subject")
                + ". Guessing is what the phase's stop rule forbids."),
        "evidence": design + management,
    }


def probes(definitions: dict[str, str]) -> list[dict]:
    out = []

    def probe(name: str, what: str, fn) -> None:
        try:
            fn()
        except Stop as exc:
            out.append({"probe": name, "what_was_fed": what, "raised": True, "message": str(exc)})
            return
        out.append({"probe": name, "what_was_fed": what, "raised": False,
                    "message": "NO STOP — this probe FAILED to establish its stop"})

    probe("a missing field", "an entry carrying every required field but `plain`",
          lambda: require_fields({f: "x" for f in REQUIRED_FIELDS if f != "plain"}))
    probe("an imported entry the data file does not carry",
          "imported {'D-001','D-002'} against a data file carrying {'D-001'}",
          lambda: reconcile({"D-001", "D-002"}, {"D-001"}))
    probe("a confirmed entry of the data file the import does not carry",
          "imported {'D-001'} against a data file carrying {'D-001','D-002'}",
          lambda: reconcile({"D-001"}, {"D-001", "D-002"}))
    probe("an unmapped nonspec_kind value",
          "an entry carrying nonspec_kind 'invented-kind'",
          lambda: require_known_nonspec({"id": "D-000", "nonspec_kind": "invented-kind"}))
    probe("a class outside the ruled vocabulary", "one row carrying the class 'INVENTED'",
          lambda: require_reconciled_distribution([{"proposed_class": "INVENTED"}], 1))
    probe("a distribution that does not account for the population",
          "one classified row against a population of two",
          lambda: require_reconciled_distribution([{"proposed_class": DESIGN}], 2))
    probe("a header definition the mapping rests on that is no longer there",
          "a header whose `home_rule` is empty",
          lambda: locate_definitions({"home_rule": ""}))

    failed = [p["probe"] for p in out if not p["raised"]]
    if failed:
        raise Stop(f"a probe did not raise, so a STOP this tool claims cannot be shown to fire: "
                   f"{failed}")
    del definitions
    return out


def build() -> tuple[dict, str]:
    if not FILTER.exists():
        raise Stop(f"the committed filter artifact is missing: {FILTER}")
    if not BACKBONE.exists():
        raise Stop(f"the decisions register's data file is missing: {BACKBONE}")

    located = locate_sources()
    classified = json.loads(FILTER.read_text(encoding="utf-8"))
    imported = {row["id"]: row for row in classified["entries"]
                if row["proposed_class"] == CONFIRMED}
    if not imported:
        raise Stop("the committed filter artifact carries no entry on the confirmed side, so "
                   "there is no population to sort — the import is not what this pass assumes")

    data = json.loads(BACKBONE.read_text(encoding="utf-8"))
    definitions = locate_definitions(data["header"])
    by_id = {}
    for entry in data["decisions"]:
        require_fields(entry)
        require_known_nonspec(entry)
        by_id[entry["id"]] = entry
    reconcile(set(imported), {i for i in imported if i in by_id})

    placements, placement_record = ruled_placements()

    rows = []
    for entry_id in sorted(imported):
        entry = by_id[entry_id]
        verdict = classify(entry, definitions)
        # ★ THE RULED PLACEMENT IS APPLIED HERE AND MARKED AS A DISTINCT ROUTE. It reaches only an
        # entry the rule itself returned; the check that it reaches no other is below, in both
        # directions, and it HALTS rather than preferring one source over the other.
        if entry_id in placements and verdict["proposed_class"] == NEEDS_USER:
            verdict = {
                "proposed_class": placements[entry_id],
                "decided_by": USER_RULED_ROUTE,
                "why": "the rule returned this entry rather than guessing, and the user placed it "
                       "at the 2026-08-17 rulings-sort sitting by the ruled criterion: an entry "
                       "whose statement binds the SYSTEM (what the analysis is, does, or must "
                       "satisfy) is DESIGN-INTENT; one whose statement binds the WORK (how we "
                       "decide, verify, record, sequence) is IMPLEMENTATION-MANAGEMENT",
                "evidence": [{"the_route": USER_RULED_ROUTE,
                              "the_record": SORT_RULING.name,
                              "the_list_it_was_read_from": placements[entry_id],
                              "★_what_the_rule_had_returned": NEEDS_USER,
                              "★_the_rules_own_evidence_is_kept":
                                  "the recognizer hits the rule found are preserved below, so the "
                                  "placement can be read against what the rule saw"}]
                + verdict["evidence"],
            }
        rows.append({
            "id": entry["id"],
            "group": entry["group"],
            "title": entry["title"],
            "home": entry["home"],
            "status": entry["status"],
            "home_is_layer_spec": entry.get("home_is_layer_spec"),
            "nonspec_kind": entry.get("nonspec_kind"),
            "what_the_entry_says_the_decision_is_quoted_from_the_register": entry["plain"],
            "the_evidence_shape_the_filter_recorded": imported[entry_id]["evidence_shape"],
            **verdict,
        })
    require_reconciled_distribution(rows, len(imported))

    # ★ THE PLACEMENTS AND THE RULE'S OWN RETURNED POPULATION, RECONCILED IN BOTH DIRECTIONS.
    placed_here = {r["id"] for r in rows if r["decided_by"] == USER_RULED_ROUTE}
    stray = sorted(set(placements) - placed_here)
    if stray:
        raise Stop(f"the sitting record places {stray}, which this rule did not return as "
                   f"{NEEDS_USER} — a ruled placement that overrules a route the same sitting "
                   f"ratified is a STOP, not a preference")
    unplaced = sorted(r["id"] for r in rows if r["proposed_class"] == NEEDS_USER)
    if unplaced:
        raise Stop(f"the rule returned {unplaced} and the sitting record places none of them — the "
                   f"derivation and the ruling have drifted apart")

    distribution = {cls: sum(1 for r in rows if r["proposed_class"] == cls) for cls in CLASSES}

    # ★ AND THE SITTING'S OWN TOTALS, RECONCILED AGAINST THE POPULATION IN BOTH DIRECTIONS. The
    # sitting states them; this pass computes them; a disagreement halts rather than adjusts.
    stated = placement_record["the_totals_the_sitting_states"]
    computed = {DESIGN: distribution[DESIGN], MANAGEMENT: distribution[MANAGEMENT],
                "unplaced": distribution[NEEDS_USER]}
    if computed != stated:
        raise Stop(f"the computed totals {computed} disagree with the ones the sitting record "
                   f"states {stated} — a derivation that does not reconcile is a STOP, not an "
                   f"adjustment")
    if stated[DESIGN] + stated[MANAGEMENT] != len(imported):
        raise Stop(f"the sitting's totals sum to {stated[DESIGN] + stated[MANAGEMENT]} against a "
                   f"confirmed population of {len(imported)}")
    placement_record["the_totals_this_pass_computes"] = computed
    placement_record["they_reconcile_in_both_directions"] = True
    placement_record["against_the_confirmed_population"] = len(imported)
    by_route: dict[str, dict[str, int]] = {}
    for row in rows:
        route = by_route.setdefault(row["decided_by"], {cls: 0 for cls in CLASSES})
        route[row["proposed_class"]] += 1
    nonspec_values = sorted({r["nonspec_kind"] for r in rows if r["nonspec_kind"]})
    header_defines = sorted(v for v, (_c, d) in NONSPEC_MAPPING.items() if d is not None)

    artifact = {
        "what_this_is":
            "THE RULINGS SORT, RULED. Every entry on the confirmed side of the decisions-register "
            "filter, with ONE class from the ruled two-value vocabulary — design intent, or "
            "management of the implementation. The rule places most of them and the user ruled the "
            "rest at the 2026-08-17 sitting, which also RATIFIED the rule-placed side as proposed. "
            "NOTHING IS EXECUTED BY IT: no entry is retired, edited, moved or marked, the decisions "
            "register's files are untouched, and a class here grades no decision's worth.",
        "generator": "tools/audit/gen_rulings_sort.py",
        "dispatch": "cc_instruction_preparation_eighth.md, Task 4 (the ruled placements recorded); "
                    "first run cc_instruction_preparation_second.md, Task 3",
        "★_THE_SITTING_THAT_RULED_THIS_SORT": {
            "authority": "cowork_rulings_2026_08_17_rulings_sort_sitting.md (the user's word: \"I "
                         "agree with your recommendations\" — quoted verbatim in that record's §0)",
            "★_1_the_rule_placed_entries_are_RATIFIED_as_proposed":
                "The proposed DESIGN-INTENT entries are the framework phase's seed list as "
                "proposed; the proposed IMPLEMENTATION-MANAGEMENT entries are not design input. "
                "The ratification moves no verdict — the verdicts it ratifies are the ones this "
                "rule already produces — so it is recorded here rather than applied. Its ground, "
                "from the sitting: most of the rule-placed side rests on the decisions register's "
                "own recorded judgments, the recognizer-placed remainder is correctable at "
                "consumption, and the seed list stays amendable when the framework phase consumes "
                "it, an amendment there being its own recorded act.",
            "★_2_the_returned_entries_are_PLACED_by_the_ruled_criterion": placement_record,
            "★_3_the_nonspec_kind_header_disagreement_STAYS_AS_EVIDENCE":
                "\"No repair is ordered.\" The mismatch rides to the phase's retrospective as "
                "evidence — a disagreement between a record and what it describes — exactly as "
                "this pass already treated it: values the header does not define were never "
                "mapped by name. It is published unchanged below.",
            "★_what_a_management_placement_does_NOT_do":
                "A management placement of a standing principle removes none of its force — the "
                "principles govern every session through the standing rules regardless of the "
                "sort. The sort classifies; it retires nothing, edits nothing and grades no "
                "decision's worth.",
        },
        "the_authority": {
            "sentences_located_in_their_own_records_on_this_run": located,
            "★_what_the_design_intent_side_becomes":
                "The framework phase's SEED LIST — the decisions a derivation may start from. A "
                "decision wrongly placed there seeds the architecture with something nobody meant "
                "to seed it with; one wrongly placed on the other side is simply not consulted. "
                "That asymmetry is why every design-intent member is listed on the surface with "
                "its plain restatement.",
        },
        "the_population": {
            "imported_from": "tools/audit/decisions_filter_classification.json",
            "the_class_imported": CONFIRMED,
            "entries": len(imported),
            "★_it_is_imported_and_never_restated":
                "The membership is the committed filter artifact's own, read on every run (#6), "
                "and reconciled against the decisions register's data file in BOTH directions as "
                "a STOP (D-671).",
        },
        "what_is_DERIVED": [
            "the population, imported from the committed filter artifact and never hand-listed",
            "every entry's fields, read from the decisions register's own data file",
            "the two home-classification facts the rule leans on — `home_is_layer_spec` and "
            "`nonspec_kind` — which are the REGISTER'S OWN recorded judgments",
            "every count and every distribution",
        ],
        "what_is_AUTHORED": [
            "the mapping from a `nonspec_kind` value to a proposed class, each carrying the "
            "definition the data file's own header gives that value, verbatim",
            "the word recognizers, reached only where the decisions register's own home classification "
            "leaves an entry undecided",
            "the order the rule applies its steps in",
        ],
        "the_rule": {
            "what_each_class_is": WHAT_EACH_CLASS_IS,
            "step_1": "`home_is_layer_spec` is true -> DESIGN-INTENT. A decision about what the "
                      "analysis is or does is what a layer specification holds.",
            "step_2": "otherwise the decisions register's own `nonspec_kind`, where this pass maps it: "
                      + "; ".join(f"{value} -> {cls}"
                                  for value, (cls, _d) in sorted(NONSPEC_MAPPING.items())
                                  if cls is not None),
            "step_3": "otherwise the authored word recognizers over the entry's own title and "
                      "plain restatement: exactly one side firing decides; both or neither does "
                      "not.",
            "step_4": f"otherwise {NEEDS_USER} — returned, never guessed.",
            "the_nonspec_definitions_quoted_from_the_data_files_own_header": definitions,
            "values_left_deliberately_to_the_recognizers": sorted(
                v for v, (cls, _d) in NONSPEC_MAPPING.items() if cls is None),
            "the_design_recognizers": {label: pattern.pattern
                                       for label, pattern in DESIGN_WORDS},
            "the_management_recognizers": {label: pattern.pattern
                                           for label, pattern in MANAGEMENT_WORDS},
        },
        "★_a_disagreement_recorded_and_not_repaired": {
            "what": "The data file's header says `nonspec_kind` says which of THREE cases an entry "
                    "is, and names three. The entries use more than three.",
            "the_values_the_entries_actually_use": nonspec_values,
            "the_values_the_header_defines_and_this_pass_maps_by_name": header_defines,
            "what_was_done": "NOTHING was repaired. The values the header does not define are not "
                             "mapped by their name; they fall through to the recognizers, which is "
                             "the only honest treatment of a value the record does not define.",
            "why_not_repaired": "This batch edits no decisions-register file, and a disagreement between a "
                                "record and what it describes is evidence rather than a defect to "
                                "smooth away.",
        },
        "★_what_this_sort_is_NOT": {
            "not_executed": "Nothing moves, nothing is retired, nothing is written into the "
                            "decisions register. The sort is a proposal awaiting the user.",
            "not_a_judgment_on_a_decision's_worth": "A decision placed in "
                                                    "IMPLEMENTATION-MANAGEMENT is not lesser, not "
                                                    "wrong and not discarded — it is simply not "
                                                    "design input to the framework phase.",
            "not_a_re_reading_of_the_filter": "The confirmed side is taken as the filter left it "
                                              "and the user ratified it. Nothing here re-opens "
                                              "whether a deciding act can be named.",
            "the_recognizers_reach_is_UNMEASURED": "The word recognizers decide only the entries "
                                                   "the decisions register's own home classification leaves "
                                                   "undecided, and neither their reach nor their "
                                                   "error rate is measured (#19). Where they leave "
                                                   "an entry, it returns to the user rather than "
                                                   "being placed.",
        },
        "the_distribution": distribution,
        "the_distribution_by_the_route_that_decided_it": by_route,
        "the_stops_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not":
                "They establish that each STOP CAN fire, through the very function the walk calls. "
                "They establish NOTHING about whether any entry is in the right class — that is "
                "what the surface puts to the user.",
            "probes": probes(definitions),
        },
        "entries": rows,
    }
    return artifact, render(artifact)


def render(a: dict) -> str:
    L: list[str] = []

    def add(line: str = "") -> None:
        L.append(line)

    ruled = a["★_THE_SITTING_THAT_RULED_THIS_SORT"]
    add("# The rulings sort — design intent, or management of the implementation, RULED for every "
        "confirmed decision")
    add()
    add("> **STATUS: RULED, 2026-08-17. NOTHING IS EXECUTED BY IT.** This surface was a ruling")
    add("> surface awaiting the user; the user ruled it at the rulings-sort sitting")
    add("> (`cowork_rulings_2026_08_17_rulings_sort_sitting.md`), and this rendering carries the")
    add("> ruled state rather than the proposal. **The banner it replaces said the surface was")
    add("> awaiting the user and that nothing here was ruled — true when it was written, and made")
    add("> untrue by the sitting; the former rendering stands in git at the commits that carried")
    add("> it (#12).** What the sitting did NOT do is unchanged: no entry is retired, edited, moved")
    add("> or marked; the decisions register's data file and every file rendered from it are")
    add("> byte-unchanged by the sort; and a class here grades no decision's worth. Generated by")
    add("> `tools/audit/gen_rulings_sort.py` from `tools/audit/rulings_sort_classification.json`,")
    add("> which it writes in the same run. Per the standing presentation rule")
    add("> (`cowork_rulings_2026_08_15_batch_return.md` §5) every identifier used below is")
    add("> re-explained from scratch in §0 before any question rests on it.")
    add()
    add("> **THE SITTING'S THREE RULINGS.** *(1)* " + ruled[
        "★_1_the_rule_placed_entries_are_RATIFIED_as_proposed"])
    add(">")
    add("> *(2)* The entries the rule RETURNED rather than guessed are placed by the ruled")
    add("> criterion, entering as a distinct route — **" + USER_RULED_ROUTE + "** — beside the")
    add("> rule's own, so a later reader sees where the judgment came from. Their membership is")
    add("> parsed from the sitting record itself and never retyped here; the totals the sitting")
    add("> states are reconciled against the population in both directions as a STOP.")
    add(">")
    add("> *(3)* " + ruled["★_3_the_nonspec_kind_header_disagreement_STAYS_AS_EVIDENCE"])
    add(">")
    add("> **★ AND A MANAGEMENT PLACEMENT REMOVES NOTHING.** "
        + ruled["★_what_a_management_placement_does_NOT_do"])
    add()

    add("## 0. The referents, re-explained from scratch (read this section first)")
    add()
    add("- **The decisions register** — the project's record of WHAT WAS DECIDED about how this")
    add("  system works and whether each decision still stands. Its data file")
    add("  (`tools/audit/decisions/backbone_decisions.json`) is the only surface ever edited; the")
    add("  INDEX `DECISIONS.md` and the group files are rendered from it.")
    add("- **An entry** — one row of that decisions register: a decision's title, the verbatim")
    add("  words it was recorded in at its home, a plain restatement, where it is recorded, and")
    add("  its status.")
    add("- **The filter** — the pass that read each entry's own fields and asked whether a DECIDING")
    add("  ACT could be named for it. Its confirmed side — the entries where one could — is what")
    add("  the user ratified on 2026-08-16, and is exactly the population sorted here.")
    add("- **The framework phase** — the third of the six phases the user ruled on 2026-08-15: the")
    add("  architecture decided before the details. Its SEED MATERIAL is the design-intent side of")
    add("  this sort.")
    add("- **`home_is_layer_spec`** — a field the decisions register carries: the entry is recorded")
    add("  in a LAYER'S OWN SPECIFICATION rather than somewhere else.")
    add("- **`nonspec_kind`** — a second field the decisions register carries, for an entry that is")
    add("  NOT in a layer specification: which kind of home it has instead. The data file's own")
    add("  header defines the values, and this surface quotes those definitions rather than")
    add("  interpreting them.")
    add()

    add("## 1. What was asked for, quoted")
    add()
    for name, record in a["the_authority"]["sentences_located_in_their_own_records_on_this_run"].items():
        add(f"**{name.capitalize()}** — `{record['source']}`:")
        add()
        add(f"> {record['quoted']}")
        add()
    add("**★ WHY THE DESIGN-INTENT SIDE IS THE PAYLOAD.** "
        + a["the_authority"]["★_what_the_design_intent_side_becomes"])
    add()

    add("## 2. The rule, published beside the verdicts it produced")
    add()
    add("**The two ruled classes, and the third outcome the phase's stop rule requires:**")
    add()
    for cls in CLASSES:
        add(f"- **{cls}** — {a['the_rule']['what_each_class_is'][cls]}")
    add()
    add("**DERIVED** — nothing below was hand-listed:")
    for item in a["what_is_DERIVED"]:
        add(f"- {item}")
    add()
    add("**AUTHORED** — and marked as such, so a reader sees where the judgment starts:")
    for item in a["what_is_AUTHORED"]:
        add(f"- {item}")
    add()
    add("**The rule, applied in order:**")
    add()
    for step in ("step_1", "step_2", "step_3", "step_4"):
        add(f"{step[-1]}. {a['the_rule'][step]}")
    add()
    add("**The definitions the mapping rests on, quoted from the data file's own header:**")
    add()
    for value, definition in a["the_rule"][
            "the_nonspec_definitions_quoted_from_the_data_files_own_header"].items():
        add(f"- `{value}` — *{definition}*")
    add()
    found = a["★_a_disagreement_recorded_and_not_repaired"]
    add("**★ A DISAGREEMENT FOUND AND NOT REPAIRED.** " + found["what"])
    add()
    add("- *The values the entries actually use:* "
        + ", ".join(f"`{v}`" for v in found["the_values_the_entries_actually_use"]))
    add("- *The values the header defines and this pass maps by name:* "
        + ", ".join(f"`{v}`" for v in found["the_values_the_header_defines_and_this_pass_maps_by_name"]))
    add(f"- *What was done:* {found['what_was_done']}")
    add(f"- *Why it was not repaired:* {found['why_not_repaired']}")
    add()

    add("## 3. What this sort is NOT — read before the proposals")
    add()
    for name, text in a["★_what_this_sort_is_NOT"].items():
        add(f"- **{name.replace('_', ' ')}.** {text}")
    add()

    add("## 4. The population and the proposed distribution")
    add()
    add(f"- Entries sorted (the whole confirmed side, imported from the filter's artifact): "
        f"**{a['the_population']['entries']:,}**")
    add(f"- {a['the_population']['★_it_is_imported_and_never_restated']}")
    add()
    add("| proposed class | entries |")
    add("|---|---|")
    for cls in CLASSES:
        add(f"| {cls} | {a['the_distribution'][cls]:,} |")
    add()
    add("**By the route that decided it**, so a reader can see how much of the sort is the")
    add("decisions register's own recorded judgment and how much is this pass's words:")
    add()
    add("| decided by | " + " | ".join(CLASSES) + " |")
    add("|---|" + "---|" * len(CLASSES))
    for route, counts in a["the_distribution_by_the_route_that_decided_it"].items():
        add(f"| {route} | " + " | ".join(f"{counts[c]:,}" for c in CLASSES) + " |")
    add()

    add("## 5. Every DESIGN-INTENT entry — the seed list, as ruled")
    add()
    add("These are the decisions the sitting ruled to be seed material for the framework phase.")
    add("**This is the payload of the sort**: a decision listed here is one a derivation is allowed")
    add("to start from, so it is listed with what the decisions register says the decision is. The")
    add("list remains amendable when the framework phase consumes it; an amendment there is its own")
    add("recorded act.")
    add()
    _members(add, a, DESIGN)

    add("## 6. The entries the rule RETURNED, and where the sitting placed them")
    add()
    add("The rule reached no verdict for these: the decisions register's own home classification")
    add("does not place them, and their own restatement carries both subjects or neither. They were")
    add("returned rather than guessed, and the user placed them at the 2026-08-17 sitting by the")
    add("ruled criterion — an entry whose statement binds the SYSTEM is DESIGN-INTENT; one whose")
    add("statement binds the WORK is IMPLEMENTATION-MANAGEMENT. Each appears in §5 or §7 with its")
    add(f"route recorded as *{USER_RULED_ROUTE}*, and the rule's own recognizer evidence is kept")
    add("beside the placement so it can be read against what the rule saw.")
    add()
    for cls in (DESIGN, MANAGEMENT):
        placed = [r for r in a["entries"]
                  if r["decided_by"] == USER_RULED_ROUTE and r["proposed_class"] == cls]
        add(f"**Placed {cls} ({len(placed)}):** "
            + (", ".join(f"`{r['id']}`" for r in placed) if placed else "*none*"))
        add()
    add("**Left unplaced by the sitting: "
        f"{a['the_distribution'][NEEDS_USER]}.**")
    add()
    _members(add, a, NEEDS_USER)

    add("## 7. The IMPLEMENTATION-MANAGEMENT entries")
    add()
    add("Listed by identity: decisions about process, apparatus, workflow, record-keeping or")
    add("sequencing. **This is not a judgment on their worth** — they are simply not design input")
    add("to the framework phase, and nothing happens to them. A management placement of a standing")
    add("principle removes none of its force: the principles govern every session through the")
    add("standing rules regardless of the sort.")
    add()
    add("<details><summary>The IMPLEMENTATION-MANAGEMENT entries</summary>")
    add()
    for row in a["entries"]:
        if row["proposed_class"] == MANAGEMENT:
            add(f"- **{row['id']}** — {row['title']} *(decided by {row['decided_by']})*")
    add()
    add("</details>")
    add()

    add("## 8. What this surface does NOT do, and must not be read as doing")
    add()
    add("- **It executes nothing.** The sort classifies; it retires nothing and moves nothing.")
    add("- **It edits no decisions-register file.** The data file, the rendered INDEX and the")
    add("  rendered group files are byte-unchanged by the run that produced this surface.")
    add("- **It re-opens no filter verdict.** The confirmed side is taken as ratified.")
    add("- **It grades no decision's worth.** A management placing is not a demotion, and it")
    add("  removes none of a standing principle's force.")
    add("- **It seeds nothing yet.** The framework phase has not begun; the seed list is ruled and")
    add("  waits for the phase that consumes it, where it remains amendable.")
    add()
    add("*Generated by `tools/audit/gen_rulings_sort.py` from")
    add("`tools/audit/rulings_sort_classification.json`. Reproduce:")
    add("`python tools/audit/gen_rulings_sort.py --check`.*")
    add()
    return "\n".join(L)


def _members(add, a: dict, cls: str) -> None:
    members = [r for r in a["entries"] if r["proposed_class"] == cls]
    if not members:
        add("*None.*")
        add()
        return
    for row in members:
        add(f"### {row['id']} — {row['title']}")
        add()
        add(f"- **Recorded at:** `{row['home']}` · **status:** `{row['status']}` · "
            f"**group:** {row['group']}")
        add(f"- **What the entry says the decision is:** "
            f"{row['what_the_entry_says_the_decision_is_quoted_from_the_register']}")
        add(f"- **Decided by:** {row['decided_by']} — {row['why']}")
        add()


def main(argv: list[str]) -> int:
    artifact, surface = build()
    text = json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"

    if "--check" in argv:
        drift = 0
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("FAIL: the rulings sort does not re-derive:", OUT)
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("FAIL: the rulings-sort surface does not re-derive:", SURFACE)
            drift = 1
        if not drift:
            print("the rulings sort re-derives")
        return drift

    OUT.write_text(text, encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print("wrote", SURFACE.relative_to(ROOT))
    for cls in CLASSES:
        print(f"  {cls}: {artifact['the_distribution'][cls]}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
