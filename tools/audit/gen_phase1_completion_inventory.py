#!/usr/bin/env python3
"""Derive what D-231's PHASE 1 completion statement still requires.

THE RULING (user, 2026-08-04, dispatch `cc_instruction_phase1_completion_inventory.md` R1):
derive, as a MEASURED LIST, exactly what phase 1's completion statement still requires - not
from anyone's recollection, but from D-231's own text and from the register and open-items data.

THIS DERIVES.  IT DOES NOT COMPLETE.  No completion statement is written here, and this file
authorizes none.

HOW THE SET IS DERIVED, and what is authored:
  DERIVED  - D-231's phase-1 clause, located in `CLAUDE.md` by ANCHOR STRING and quoted (never
             by line number - the OI-330 lesson); the register's home classes, defense gaps and
             section-criterion verdicts, read off `backbone_decisions.json`; the open-row
             population and its OPEN subset, parsed by the SAME parser the non-gating apparatus
             declaration uses (#6 - imported, never copied); each candidate's gate verdict, taken
             from the committed apparatus artifact where that artifact carries one and from the
             row's own recorded words where it does not; the read-programme's completion, derived
             from the regime's partition plus each wave's own yield artifact.
  AUTHORED - the criteria read out of D-231's sentence (§ `the_requirement.criteria`); the
             falsity-signal vocabulary of the TRUE half's wider cut; the A1 settlement and its
             reasoning; and A2, the recollected list this wave GRADES rather than uses.

THE TWO STOPS.  The tool refuses to run if D-231's clause cannot be located by its anchors, and
refuses to run if a gate verdict it takes from the committed apparatus artifact names a row the
INDEX no longer carries open - so this table cannot drift away from either source silently.

Usage:
  python tools/audit/gen_phase1_completion_inventory.py           # write the artifact
  python tools/audit/gen_phase1_completion_inventory.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "decisions"))
from output_encoding import use_utf8_output              # noqa: E402  (path set above)
from gen_nongating_apparatus_rows import (               # noqa: E402  (#6 - one parser)
    parse_rows, FIRST_CUT_VOCAB,
)
from gen_outstanding_delegations import (                # noqa: E402  (#6 - one derivation)
    build as build_outstanding_delegations,
)
from gen_discard_records import (                        # noqa: E402  (#6 - one locator)
    build as build_discard_records,
)

use_utf8_output()   # OI-297 - the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
CLAUDE_MD = ROOT / "CLAUDE.md"
DECISIONS_MD = ROOT / "DECISIONS.md"
REGISTER = ROOT / "tools" / "audit" / "decisions" / "backbone_decisions.json"
APPARATUS = ROOT / "tools" / "audit" / "nongating_apparatus_rows.json"
DISPOSITION_MANIFEST = ROOT / "tools" / "audit" / "decisions" / "disposition_manifest.json"
REGIME = ROOT / "tools" / "audit" / "decisions" / "phase1n_reading_regime.json"
READS = [ROOT / "tools" / "audit" / "decisions" / f"reads{n}_yield.json" for n in range(1, 7)]
OI340 = ROOT / "open_items" / "OI-340.md"
OUT = ROOT / "tools" / "audit" / "phase1_completion_inventory.json"

# --------------------------------------------------------------------------- anchors (not lines)
CLAUSE_ANCHOR = "**ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN"
PHASE_1_ANCHOR = "**Phase 1 —"
PHASE_2_ANCHOR = "**Phase 2 —"
PHASE_3_ANCHOR = "**Phase 3 —"
RATIONALE_ANCHOR = "Rationale:"

# --------------------------------------------------------------------------- authored: A1
A1 = {
    "the_assumption_as_the_dispatch_states_it": (
        "That phase 1's completion statement NEEDS the disposition layer to be regenerable. If "
        "it does, OI-333 blocks this derivation and the repair falls under the freeze's "
        "blocks-the-work exception; if it does not, OI-333 stays rowed and untouched."
    ),
    "the_test_applied": (
        "Enumerate the claims D-231's phase-1 sentence obliges a completion statement to make, "
        "and ask of each whether it is FALSE or UNSUPPORTED without a re-derivation of the "
        "cluster-disposition layer."
    ),
    "verdict": "DOES NOT BLOCK",
    "why": [
        "The two halves' populations are read off the REGISTER's home data and the OPEN-ITEMS "
        "rows. Neither draws a figure from cluster_dispositions.json, and this artifact draws "
        "none.",
        "The register's own method declares the harvest a BACKSTOP, not the backbone - "
        "backbone_decisions.json header.method: 'The harvest's 15,224 candidates are a "
        "searchable index and a backstop, not the backbone'. The enumeration claim therefore "
        "rests on the specification-first reading and on the read-wave programme, which is "
        "complete (see `the_reads_are_done`), not on the disposition layer.",
        "The one claim that IS supported by the committed layer - that every harvested cluster "
        "carries a recorded disposition - is true AT THE COMMITTED ARTIFACT and needs no "
        "re-derivation to be stated.",
    ],
    "what_a_completion_statement_may_therefore_NOT_say": (
        "It may not publish a REFRESHED unresolved residual, and it may not describe the "
        "committed residual as current. The committed disposition layer was derived at a "
        "backbone of `disposition_manifest.inputs.backbone.decision_count` entries and the "
        "register now holds `counted.decisions_recorded`; every cluster restating an entry "
        "entered since still reads `unresolved`, so the committed residual OVERSTATES what is "
        "unresolved at HEAD, in a known direction, by an amount only a re-derivation can give. "
        "That is a bound on what may be said, not a blocked derivation."
    ),
    "consequence_for_this_wave": (
        "Task 1.3 applies: nothing is changed, and OI-333 stays rowed exactly as it is. The six "
        "invalid patterns are NOT escaped here."
    ),
}

# --------------------------------------------------------------------------- authored: criteria
CRITERIA = [
    {
        "id": "C1",
        "half": "COMPLETE",
        "clause": "every recorded decision is written into its owning specification",
        "what_it_obliges": (
            "Every entry of the decisions register is recorded in the specification that owns "
            "its subject. The register's own home_rule makes the outstanding classes explicit: "
            "`gap` (governs a layer, not findable from that layer's section) and `unhomed` "
            "(recorded only on a tracking surface, no home at all). `process` and "
            "`project-convention` are declared CORRECTLY homed and are not outstanding; "
            "`contract-home` is the fifth home case, admitted by D-430/D-432/D-546."
        ),
    },
    {
        "id": "C2",
        "half": "COMPLETE",
        "clause": "with its defense",
        "what_it_obliges": (
            "Each entry carries the research, measurement or constraint that decided it, at its "
            "home. The standing convention FORBIDS supplying one retroactively from memory: "
            "where the record gives none the entry reads 'derivation not recorded'. So this "
            "criterion is met by RECORDING a defense the record holds, or by stating the gap - "
            "never by writing one. The population is reported; whether each gap is fillable is "
            "not judged here."
        ),
    },
    {
        "id": "C3",
        "half": "TRUE",
        "clause": (
            "the specification text is corrected wherever it states something false at HEAD "
            "(the doc-sync debt)"
        ),
        "what_it_obliges": (
            "Every open row asserting that a specification states something false at HEAD is "
            "discharged. The population is derived below; the gating split is D-438's."
        ),
    },
    {
        "id": "C4",
        "half": "BOTH - the purposive clause, easily missed",
        "clause": (
            "so that conformance is thereafter measured against the specifications themselves - "
            "the decisions register remains the status ledger (supersession, shelving, the "
            "same-commit rule), never the conformance reference"
        ),
        "what_it_obliges": (
            "This is an obligation Cowork's framing of phase 1 as 'two halves' does not carry, "
            "and it is a THIRD requirement, not a restatement: at completion the SPECIFICATIONS "
            "must be sufficient to measure conformance against, WITHOUT consulting the register. "
            "A decision homed only in the register - or findable only through it - defeats the "
            "clause even where the register records it perfectly. It is what makes C1 a "
            "requirement about the specifications rather than about the register's fields."
        ),
    },
    {
        "id": "C5",
        "half": "TRUE - the reason the clause gives for itself",
        "clause": (
            "because a specification cannot be the compliance standard while it misdescribes the "
            "code"
        ),
        "what_it_obliges": (
            "The falsity that matters is falsity ABOUT THE CODE. This is the same line D-438's "
            "declaration draws inside the documentation rows, and it decides a question the "
            "outstanding set actually contains: a document that misdescribes ITSELF (a stale "
            "banner, a drifted anchor) is not covered by this sentence's stated reason, while a "
            "document that misdescribes the analysis is. The question is REPORTED, not settled - "
            "see `the_question_the_two_halves_do_not_settle`."
        ),
    },
]

# --------------------------------------------------------------------------- authored: signals
FALSITY_SIGNALS = [
    "doc-sync", "dt-12", "stale", "drift", "misdescrib", "false at head",
    "future-tense", "future-tenses", "out of sync", "no longer true", "doc drift",
    "present tense", "states something false", "no longer re-derive", "not in sync",
]
DOC_SUBJECT_VOCAB = [
    v for v in FIRST_CUT_VOCAB
    if v.lower() in {"doc-sync", "docs /", "doc", "documentation gap", "architecture doc"}
]

# --------------------------------------------------------------------------- authored: A2
A2_RECOLLECTED = [
    "OI-274", "OI-282", "OI-283", "OI-290", "OI-296", "OI-299",
    "OI-300", "OI-320", "OI-325", "OI-331", "OI-333",
]
A2_NOTE = (
    "Cowork's recollected list of the outstanding rows, recorded in the dispatch's premise "
    "ledger as assumption A2 and EXPLICITLY DEMOTED there from an input to a graded output. It "
    "is compared against the derived set below; a divergence is a finding about the "
    "recollection, never about the derivation. OI-274 is listed by Cowork as 'the body-tense "
    "half' and OI-283 as 'the remedy'; both are compared at row granularity, which is the only "
    "granularity the derivation has."
)


# ============================================================================= helpers
def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def locate_clause() -> dict:
    """Locate D-231's clause in CLAUDE.md by anchor string and quote its three phases."""
    text = read(CLAUDE_MD)
    i = text.find(CLAUSE_ANCHOR)
    if i < 0:
        raise SystemExit("STOP: D-231's clause anchor not found in CLAUDE.md - the derivation "
                         "cannot rest on a clause it did not locate.")
    for anchor in (PHASE_1_ANCHOR, PHASE_2_ANCHOR, PHASE_3_ANCHOR, RATIONALE_ANCHOR):
        if text.find(anchor, i) < 0:
            raise SystemExit(f"STOP: anchor {anchor!r} not found after D-231's clause opening.")
    p1 = text.find(PHASE_1_ANCHOR, i)
    p2 = text.find(PHASE_2_ANCHOR, i)
    p3 = text.find(PHASE_3_ANCHOR, i)
    p4 = text.find(RATIONALE_ANCHOR, i)

    def span(a: int, b: int) -> str:
        return re.sub(r"\s+", " ", text[a:b]).strip()

    return {
        "located_by": "anchor string, never a line number (the OI-330 lesson)",
        "clause_opening": span(i, p1),
        "phase_1_verbatim": span(p1, p2),
        "phase_2_verbatim": span(p2, p3),
        "phase_3_verbatim": span(p3, p4),
    }


# --------------------------------------------------------- R1: C1's reach over SUPERSEDED entries
#
# The ruling's ONE authored home is `cowork_audit_protocol.md`'s dispatch-protocol section (#6).
# It is QUOTED HERE IN FULL and located by anchor, never restated - which is also what the rule
# ruled in the same act requires of a citation that invokes a ruling.
PROTOCOL_MD = ROOT / "cowork_audit_protocol.md"
R1_SECTION_ANCHOR = ("### Criterion C1 reaches every decision whose content is LIVE — a superseded "
                     "entry's obligation moves to its successor")

# R2 (user, 2026-08-04, `cc_instruction_guard_fix_and_item1d.md`): the shape D-642 leaves open — a
# superseded entry whose content is a REMOVAL, which has no successor to move the obligation to.
# Its ONE authored home is the same protocol section, and it is quoted from there in full (D-643).
ARCHITECTURE_MD = ROOT / "ARCHITECTURE.md"
R2_SECTION_ANCHOR = ("### Where a superseded decision's content is a REMOVAL, the specification "
                     "states the current behaviour and records the removal as a tried-and-closed "
                     "line")

# The PRECEDENT R2 rests on, located in `ARCHITECTURE.md` by its own anchors and quoted whole.
# NEVER by line number: the dispatch that transmitted R2 cited this block by a line range that had
# already drifted past it, which is the D-307 failure the anchor machinery exists to prevent.
R2_PRECEDENT_START = ("**★ CORRECTED 2026-08-04 (phase 1z; `OPEN_ITEMS.md` OI-315, register entry "
                      "D-058)")
R2_PRECEDENT_CURRENT_BEHAVIOUR = "**There is no piece-start exception — the opening is note-based.**"
R2_PRECEDENT_TRIED_AND_CLOSED = "**Tried and closed on the key opening"

# The sentence of D-231's phase-1 clause R1 rests on.  LOCATED inside the derived quote of the
# clause rather than typed here as the record of it - if the clause is reworded, this STOPS.
R1_OPERATIVE_SENTENCE = (
    "the decisions register remains the status ledger (supersession, shelving, the same-commit "
    "rule), never the conformance reference"
)


def r1_ruling_verbatim() -> str:
    """Quote R1's section from its home IN FULL, located by its own heading."""
    text = read(PROTOCOL_MD)
    i = text.find(R1_SECTION_ANCHOR)
    if i < 0:
        raise SystemExit(
            "STOP: R1's section could not be located in cowork_audit_protocol.md by its heading. "
            "A ruling this file invokes must be quoted from its home in full, and a quote that "
            "cannot be located may not be published from anywhere else.")
    j = text.find("\n### ", i + len(R1_SECTION_ANCHOR))
    if j < 0:
        j = len(text)
    return re.sub(r"\s+", " ", text[i:j]).strip()


def r2_ruling_verbatim() -> str:
    """Quote R2's section from its home IN FULL, located by its own heading (D-643)."""
    text = read(PROTOCOL_MD)
    i = text.find(R2_SECTION_ANCHOR)
    if i < 0:
        raise SystemExit(
            "STOP: R2's section could not be located in cowork_audit_protocol.md by its heading. "
            "A ruling this file invokes must be quoted from its home in full, and a quote that "
            "cannot be located may not be published from anywhere else.")
    j = text.find("\n### ", i + len(R2_SECTION_ANCHOR))
    if j < 0:
        j = len(text)
    return re.sub(r"\s+", " ", text[i:j]).strip()


def r2_precedent_verbatim() -> dict:
    """The precedent R2 names, quoted WHOLE out of ARCHITECTURE.md and located by its anchors.

    The dispatch that transmitted R2 cited this block by a LINE RANGE, and that range had already
    drifted past it — the previous wave's homing insertions moved it. Quoting it by anchor is what
    keeps the citation from going stale silently, and a rewording STOPS this derivation rather
    than leaving a paraphrase of a precedent nobody re-read standing in the record.
    """
    text = read(ARCHITECTURE_MD)
    i = text.find(R2_PRECEDENT_START)
    if i < 0:
        raise SystemExit(
            "STOP: the precedent R2 rests on could not be located in ARCHITECTURE.md by its "
            "correction anchor. R2 is stated to BE that precedent, so it may not be published "
            "against a block this tool did not read.")
    k = text.find(R2_PRECEDENT_TRIED_AND_CLOSED, i)
    if k < 0:
        raise SystemExit(
            "STOP: the precedent's tried-and-closed line is no longer present after its "
            "correction anchor. R2's second half is the half that line demonstrates, and a "
            "precedent missing it is not the precedent the ruling names.")
    if R2_PRECEDENT_CURRENT_BEHAVIOUR not in text[i:k]:
        raise SystemExit(
            "STOP: the precedent's current-behaviour statement is no longer present between its "
            "correction anchor and its tried-and-closed line. R2's first half is the half that "
            "statement demonstrates.")
    end = text.find("\n\n", k)
    if end < 0:
        end = len(text)
    return {
        "located_in": "ARCHITECTURE.md §5.2, by anchor string — never by line number",
        "why_never_by_line_number": (
            "The dispatch that transmitted R2 cited this block as `ARCHITECTURE.md:3510-3525`, and "
            "that range had already drifted past it: the preceding wave's homing insertions moved "
            "the block down. The citation was to the right block and the wrong coordinate, which "
            "is the D-307 failure exactly — a line number quoted in prose is not a register anchor, "
            "so nothing maintains it. Reported rather than silently corrected, and the block is "
            "re-located by its own words on every run."
        ),
        "the_precedent_quoted_IN_FULL": re.sub(r"\s+", " ", text[i:end]).strip(),
        "the_two_halves_it_demonstrates": {
            "states_the_current_behaviour": R2_PRECEDENT_CURRENT_BEHAVIOUR,
            "records_the_removal_as_tried_and_closed": R2_PRECEDENT_TRIED_AND_CLOSED + " …",
        },
    }


def c1_reach_over_a_removal() -> dict:
    """R2, recorded beside R1's block because it bounds the same criterion's reach."""
    return {
        "the_ruling_quoted_IN_FULL_from_its_home": r2_ruling_verbatim(),
        "its_home": "cowork_audit_protocol.md, the dispatch-protocol section, beside D-431, D-434, "
                    "D-436, D-640, D-641, D-642 and D-643. Register entry D-644. Located by "
                    "heading and quoted whole on every run (D-643).",
        "why_it_is_recorded_HERE_beside_R1": (
            "R1/D-642 moves a superseded entry's obligation to its SUCCESSOR. A removal has no "
            "successor — nothing later states the rule, because the rule is that the mechanism is "
            "gone — so such an entry falls through D-642 entirely: the register records it "
            "superseded, no specification carries it, and criterion C1 has no closing act to "
            "name. R2 supplies the closing act, so it belongs where C1's reach is recorded."
        ),
        "what_it_obliges_and_it_is_TWO_acts": (
            "(1) the owning specification STATES THE CURRENT BEHAVIOUR — which is D-231's doc-sync "
            "half, since a specification that goes on asserting a removed mechanism in the present "
            "tense misdescribes the code; and (2) it RECORDS THE REMOVAL AS A TRIED-AND-CLOSED "
            "LINE, so a later reader meets it before retrying. Neither half alone suffices: (1) "
            "without (2) loses the information that the alternative was tried (#12), and (2) "
            "without (1) leaves the specification false at HEAD."
        ),
        "★_it_is_PRECEDENT_not_a_new_rule": r2_precedent_verbatim(),
        "what_R2_does_NOT_authorize": (
            "No fix to the analysis, no design, no inference change, and no re-classification of "
            "any entry's home CLASS. It says what the owning specification owes for one shape of "
            "entry, and nothing else."
        ),
        "where_it_is_applied": (
            "tools/audit/decisions/r1_superseded_reach.json, over the member of item 1's NO-HOME "
            "class whose content is a removal. No verdict or count is restated here (D-431)."
        ),
    }


WITHDRAWN_BASIS_HEADING = "## The reading, at the ruling's own text"
WITHDRAWN_BASIS_END = "## What this row does NOT say"


def withdrawn_basis_grounds() -> list[str]:
    """CC's four grounds against the WITHDRAWN basis, read off OPEN_ITEMS.md's OI-340 detail file.

    Derived rather than restated so the preservation obligation (#12) cannot go stale silently:
    if the row is reworded or its list changes length, this STOPS instead of publishing a
    paraphrase of a refutation that no longer reads that way.
    """
    text = read(OI340)
    i = text.find(WITHDRAWN_BASIS_HEADING)
    j = text.find(WITHDRAWN_BASIS_END)
    if i < 0 or j < 0 or j <= i:
        raise SystemExit(
            "STOP: OI-340's reading section could not be located by its own headings. The "
            "withdrawn basis's four grounds are preserved BY DERIVATION (#12) and may not be "
            "restated from anywhere else.")
    grounds, cur = [], None
    for line in text[i:j].splitlines():
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            if cur is not None:
                grounds.append(cur)
            cur = m.group(2).strip()
        elif cur is not None:
            if line.strip():
                cur += " " + line.strip()
            else:
                grounds.append(cur)
                cur = None
    if cur is not None:
        grounds.append(cur)
    grounds = [re.sub(r"\s+", " ", g).strip() for g in grounds]
    if len(grounds) != 4:
        raise SystemExit(
            f"STOP: OI-340's refutation is recorded as {len(grounds)} ground(s), not the four the "
            "withdrawal preserves. A count that has moved means the row was rewritten, and the "
            "preserved grounds may not be published from a stale reading of it.")
    return grounds


def c1_reach_over_superseded(clause: dict) -> dict:
    """R1, recorded where the C1 criteria live, with the clause it rests on quoted from HEAD."""
    p1 = clause["phase_1_verbatim"]
    if R1_OPERATIVE_SENTENCE not in p1:
        raise SystemExit(
            "STOP: the sentence R1 rests on is not present in D-231's phase-1 clause at HEAD. A "
            "ruling recorded against a clause that no longer says what it was read out of may not "
            "be published as an application of it.")
    return {
        "the_ruling_quoted_IN_FULL_from_its_home": r1_ruling_verbatim(),
        "its_home": "cowork_audit_protocol.md, the dispatch-protocol section, beside D-431, D-434, "
                    "D-436, D-640 and D-641. Located by heading and quoted whole on every run — "
                    "the branch of a ruling that supports a claim is never quoted alone (the rule "
                    "ruled in the same act).",
        "what_it_changes_about_C1": (
            "C1's population. C1 obliges every RECORDED decision to be written into its owning "
            "specification; R1 reads that as every decision whose CONTENT IS LIVE. A superseded "
            "entry is not thereby exempt - the obligation moves to the successor that carries its "
            "live content, and is discharged only where that successor is itself homed."
        ),
        "the_clause_it_rests_on": {
            "the_sentence": R1_OPERATIVE_SENTENCE,
            "located_in": "the derived quote at `the_requirement.phase_1_verbatim`, which carries "
                          "D-231's phase-1 clause ENTIRE at HEAD - including the half that does "
                          "not support R1. Nothing is quoted here in a shorter form than the "
                          "clause has.",
            "what_R1_takes_from_it": (
                "The clause assigns SUPERSESSION to the register and CONFORMANCE to the "
                "specifications, and names supersession and shelving as two distinct things the "
                "register is the ledger OF. A superseded decision is therefore not something "
                "conformance is measured against."
            ),
            "what_the_sentence_does_NOT_settle": (
                "It says nothing about an entry whose supersession names no successor, and "
                "nothing about one whose successor is itself unhomed. R1 answers the second and "
                "is silent on the first; where the register names no carrier, the application "
                "reports that and proposes nothing."
            ),
        },
        "★_the_WITHDRAWN_basis_and_why_it_was_withdrawn": {
            "what_was_claimed": (
                "The preceding dispatch (`cc_instruction_finish_line_item1b.md`) presented R1 as "
                "an APPLICATION of OI-272's per-kind home scheme to the superseded kind, and "
                "declared that reading as its assumption A2 with an instruction to STOP if the "
                "scheme would not carry it."
            ),
            "the_status_of_that_claim": "WITHDRAWN by the user, 2026-08-04, in the ruling that "
                                        "replaces it. R1's substance is unchanged; its basis is "
                                        "D-231's own clause above and no longer OI-272.",
            "why_the_withdrawal_is_recorded_rather_than_dropped": (
                "A wrong basis retracted is evidence (#12), and the four grounds below are what "
                "a later session would otherwise re-derive. They are read off the row that made "
                "them rather than restated here."
            ),
            "CCs_four_grounds_preserved": withdrawn_basis_grounds(),
            "grounds_source": "open_items/OI-340.md, the section '"
                              + WITHDRAWN_BASIS_HEADING.lstrip('# ') + "', parsed on every run",
        },
        "what_R1_does_NOT_authorize": (
            "No fix to the analysis, no design, no inference change, and no re-classification of "
            "any entry's home CLASS. It decides which entries criterion C1 reaches and nothing "
            "else."
        ),
        "where_it_is_applied": (
            "tools/audit/decisions/r1_superseded_reach.json, over finish-line item 1's NO-HOME "
            "class. No verdict or count is restated here (D-431)."
        ),
    }


def register_facts() -> dict:
    reg = json.loads(read(REGISTER))
    D = reg["decisions"]
    num = lambda e: int(e["id"].split("-")[1])                       # noqa: E731

    by_kind: dict[str, list] = {}
    for e in D:
        by_kind.setdefault(e.get("nonspec_kind") or "homed-in-a-layer-specification", []).append(e)

    gaps = by_kind.get("gap", [])
    gap_section_classified = [e for e in gaps if "home_section" in e]
    gap_unclassified = [e for e in gaps if "home_section" not in e]

    excl_reason: dict[str, list[str]] = {}
    for e in gap_section_classified:
        excl_reason.setdefault(e["home_section"]["decided_by"], []).append(e["id"])

    gap_by_doc: dict[str, int] = {}
    for e in gaps:
        gap_by_doc[e["home"].split(":")[0]] = gap_by_doc.get(e["home"].split(":")[0], 0) + 1

    no_defense = [e for e in D if not e.get("rationale")]
    said_not_recorded = [e for e in D
                         if "derivation not recorded" in (e.get("rationale") or "").lower()]

    write_list = reg["section_home_criterion"].get("write_list", [])
    dispositions = reg["section_home_criterion"].get("write_list_dispositions_2026_08_04", {})

    return {
        "decisions_recorded": len(D),
        "by_home_class": {k: len(v) for k, v in sorted(by_kind.items())},
        "gaps": gaps,
        "gap_section_classified": gap_section_classified,
        "gap_unclassified": gap_unclassified,
        "gap_unclassified_all_from_the_read_waves": all(num(e) >= 440 for e in gap_unclassified),
        "gap_unclassified_lowest_id": min((e["id"] for e in gap_unclassified), default=None),
        "excl_reason": excl_reason,
        "gap_by_doc": dict(sorted(gap_by_doc.items(), key=lambda kv: (-kv[1], kv[0]))),
        "unhomed": by_kind.get("unhomed", []),
        "no_defense": no_defense,
        "said_not_recorded": said_not_recorded,
        "write_list": write_list,
        "write_list_dispositions": dispositions,
    }


def reads_facts() -> dict:
    regime = json.loads(read(REGIME))
    per_wave, docs = [], []
    for p in READS:
        y = json.loads(read(p))
        names = [r["document"] for r in y["rows"]]
        docs += names
        per_wave.append({"artifact": p.name, "documents_read_in_full": len(names)})
    part = regime["partition"]
    total_read = part["read_in_full"] + len(docs)
    return {
        "the_regime_partition": part,
        "per_wave": per_wave,
        "documents_read_by_the_waves": len(docs),
        "read_in_full_after_wave_6": total_read,
        "still_owed_a_full_read": part["design_document_surface"]
        - part["user_accepted_exclusions_not_read"] - total_read,
        "the_owed_set_is_empty": (part["design_document_surface"]
                                  - part["user_accepted_exclusions_not_read"] - total_read) == 0,
        "derived_here_rather_than_asserted": (
            "The regime's own partition plus each wave's own yield artifact. The regime artifact "
            "is NOT regenerated (OI-316, OI-328) and its own partition fields are stale by "
            "design; this recomputation is the current one, and it reproduces "
            "reads6_yield.json -> the_running_read_count independently."
        ),
        "documents_the_waves_read": sorted(docs),
    }


HOME_GRANULARITY_CLAIM = (
    "Every entry whose class is `contract-home` or `gap` therefore carries a `home_section` block"
)


def scope_block_facts(reads: dict, reg: dict) -> dict:
    """The register's own published statements about itself, checked against HEAD."""
    scope = json.loads(read(REGISTER))["header"]["scope"]
    disp = json.loads(read(DISPOSITION_MANIFEST))
    rendered = read(DECISIONS_MD)
    regime = json.loads(read(REGIME))

    computed_unresolved = None
    m = re.search(r"\|\s*—\s*unresolved\s*\|\s*(\d+)\s*\|", rendered)
    if m:
        computed_unresolved = int(m.group(1))
    quoted = re.findall(r"([\d,]+) clusters carry the ['‘]unresolved['’] disposition",
                        scope.get("measured_remainder", ""))

    text = scope.get("not_read_in_full", "")
    named_literally = sorted(set(re.findall(r"((?:cowork_|docs/)[a-z0-9_/]+\.md)", text)))
    named_by_glob = sorted(set(re.findall(r"([a-z0-9_]*\*[a-z0-9_]*\.md)", text)))
    named_archives = sorted(set(re.findall(r"([A-Z][A-Z_]*ARCHIVE\.md)", text))
                            | {d for d in re.findall(r"(cowork_[a-z0-9_]*archive[a-z0-9_]*\.md)",
                                                     text)})

    read_by_waves = set(reads["documents_the_waves_read"])
    read_before = {r["document"] for r in regime.get("read_rows", [])}
    excluded = {r["document"] for r in regime.get("owed_rows", [])}   # owed, then read

    def expand(glob: str) -> list[str]:
        rx = re.compile("^" + re.escape(glob).replace(r"\*", ".*") + "$")
        return sorted(d for d in (read_by_waves | read_before) if rx.match(d))

    # ── every verdict below is DERIVED from the checks beside it, never authored ──────────
    # (2026-08-04, ruling R3: the three statements were corrected, and a verdict that stayed an
    #  authored string would be the very defect this block exists to catch, one level up.)
    named_read = sorted(d for d in named_literally
                        if d in read_by_waves or d in read_before)
    glob_read = sorted({d for g in named_by_glob for d in expand(g)})
    s1_ok = not named_read and not glob_read

    remainder_raw = scope.get("measured_remainder", "")
    s2_is_template = "{" in remainder_raw and "}" in remainder_raw
    s2_ok = s2_is_template and not quoted

    ch_missing = sum(1 for e in json.loads(read(REGISTER))["decisions"]
                     if e.get("nonspec_kind") == "contract-home" and "home_section" not in e)
    gap_missing = len(reg["gap_unclassified"])
    s3_ok = ch_missing == 0 and gap_missing == 0

    corrections = scope.get("corrections_2026_08_04")

    return {
        "why_this_is_here": (
            "The register's scope block is AUTHORED PROSE rendered into the generated "
            "DECISIONS.md by gen_decisions_register.py, and one further published claim about "
            "the register's own fields is checked beside it. Each is checked against HEAD "
            "because a completion statement resting on DECISIONS.md rests on them."
        ),
        "★_all_three_were_corrected_2026_08_04": {
            "ruling": "User, 2026-08-04 (R3), at `OPEN_ITEMS.md` OI-334.",
            "how_each_was_corrected": (
                "(1) and (2) by editing the scope block, with the former wordings preserved "
                "verbatim (#12) at `backbone_decisions.json` -> "
                "`header.scope.corrections_2026_08_04`; (2) additionally by making the field a "
                "TEMPLATE the register generator fills from computed data (#17f / D-431). (3) NOT "
                "in prose: the home-classification apply mode was RUN under ruling R2, after the "
                "phase-1q record was snapshotted and the snapshot established, so the claim "
                "became true rather than being re-worded."
            ),
            "the_correction_block_the_register_now_publishes": corrections,
            "every_verdict_below_is_derived_from_its_own_checks": (
                "A verdict left as an authored string would go stale exactly as the statements it "
                "grades did. Each is now computed from the fields beside it, so this block "
                "re-reports the state at HEAD on every run."
            ),
        },
        "statement_1_not_read_in_full": {
            "the_published_text": text,
            "documents_it_names_literally": named_literally,
            "of_those_read_in_full_by_the_read_waves": sorted(
                d for d in named_literally if d in read_by_waves),
            "of_those_read_in_full_before_the_waves": sorted(
                d for d in named_literally if d not in read_by_waves and d in read_before),
            "of_those_still_unread_and_correctly_so": sorted(
                d for d in named_literally
                if d not in read_by_waves and d not in read_before),
            "glob_patterns_it_names": {
                g: {"read_in_full_at_head": expand(g)} for g in named_by_glob
            },
            "archives_it_names_which_remain_correctly_unread": named_archives,
            "documents_it_names_that_HAVE_been_read_in_full": named_read + glob_read,
            "verdict": (
                "TRUE AT HEAD. The sentence names no document that has been read in full."
                if s1_ok else
                "FALSE AT HEAD. The sentence names document(s) - literally or by glob - that have "
                "since been read in full, and the yield of each is on the record."
            ),
        },
        "statement_2_measured_remainder": {
            "the_authored_field": remainder_raw,
            "it_is_a_template_the_generator_fills": s2_is_template,
            "the_unresolved_figure_it_hand_carries": quoted,
            "the_figure_the_same_file_computes": computed_unresolved,
            "the_backbone_the_committed_layer_was_derived_at":
                disp["inputs"]["backbone"]["decision_count"],
            "verdict": (
                "TRUE AT HEAD. The field carries no hand-written figure: it is a template whose "
                "every figure `gen_decisions_register.py` fills from the same computed data it "
                "renders the coverage table from, and an unfilled placeholder stops that "
                "generator (#17f / D-431)."
                if s2_ok else
                "FALSE AT HEAD. The field hand-carries a figure into a generated file, which is "
                "what D-431/#17f forbids - and the quoted figure disagrees with the computed "
                "table in the SAME generated file."
            ),
        },
        "statement_3_the_home_granularity_claim": {
            "the_published_claim": HOME_GRANULARITY_CLAIM,
            "present_in_the_rendered_register": HOME_GRANULARITY_CLAIM in rendered,
            "contract_home_entries_without_a_home_section_block": ch_missing,
            "gap_entries_without_a_home_section_block": gap_missing,
            "verdict": (
                "TRUE AT HEAD. Every `contract-home` and every `gap` entry carries a "
                "`home_section` block. It became true rather than being re-worded: the apply mode "
                "was RUN on 2026-08-04 under ruling R2, after the phase-1q record was snapshotted "
                "and the snapshot established (OI-305 / OI-319)."
                if s3_ok else
                "FALSE AT HEAD for the entries with no `home_section` block, whose only writer is "
                "`gen_home_classification.py`'s apply mode (OI-305 / OI-319)."
            ),
        },
    }


def gate_verdicts() -> dict:
    app = json.loads(read(APPARATUS))
    return {i["id"]: i for i in app["items"]}


ROW_SAYS_GATES = re.compile(r"\*\*GATES\*\*|\bGATES\b(?! nothing)")
ROW_SAYS_APPARATUS = re.compile(r"apparatus row|gates nothing|gate no stage", re.IGNORECASE)

# The third state the user's Ruling 69 of 2026-08-13 creates (register entry D-677). It is the
# record's own word, not an invented token: amended #10 calls the class DISCARDED.
DISCARDED = "DISCARDED"


def classify_d438(row: dict, authored: dict) -> dict:
    """D-438's verdict for one row, from the three sources it has always had.

    UNCHANGED by the discard input, deliberately. D-438 asks whether the row's subject bears on the
    analysis; a discard verdict answers a different question — whether the finding is worth fixing
    — and folding the second into the first would destroy the ability to say which of the two took
    a row out of the gate (#12).
    """
    rid = row["id"]
    if rid in authored:
        a = authored[rid]
        return {
            "verdict": a["verdict"],
            "source": "the committed non-gating apparatus declaration (authored, D-438)",
            "ground": a.get("gate_ground") or a.get("class_basis"),
        }
    blob = row["status_column"] + " " + row["title"]
    if ROW_SAYS_APPARATUS.search(blob):
        return {"verdict": "NON-GATING", "source": "the row's own recorded words",
                "ground": "the row states it is an apparatus row and gates nothing"}
    if ROW_SAYS_GATES.search(blob):
        return {"verdict": "GATES", "source": "the row's own recorded words",
                "ground": "the row states it gates"}
    return {"verdict": "GATES", "source": "D-438's default",
            "ground": "the row's own text does not settle it, so it gates"}


def classify_gate(row: dict, authored: dict, discarded_ids: set) -> dict:
    """The gate verdict, with the DISCARD input the user's Ruling 69 makes one of its inputs.

    The order is the ruling's own and is stated so it is not rearranged. D-438's verdict is taken
    FIRST and is kept beside the result whatever happens (#12). A conforming discard record then
    takes the row out of the gate — amended #10's *no row, no gate, no capacity* reaching a row
    already on the books, which is exactly what Ruling 69 settles. Where D-438 already says the row
    does not gate, the discard changes nothing about gating and is recorded beside the verdict
    rather than replacing it: two grounds for the same state is not a conflict.

    The #19 carve-out does not need re-deciding here and is not re-decided: a discard record naming
    a row the carve-out keeps gating never reaches this function, because the locator STOPS on it.
    """
    d438 = classify_d438(row, authored)
    if row["id"] not in discarded_ids:
        return d438
    if d438["verdict"] != "GATES":
        out = dict(d438)
        out["★_a_conforming_discard_record_also_stands_against_this_row"] = (
            "It moves nothing here: D-438 already puts the row outside the gate. Recorded so the "
            "row is not read as gating-free for one reason when the record holds two."
        )
        return out
    return {
        "verdict": DISCARDED,
        "source": "the row's DISCARD record, consumed as an input to this derivation under the "
                  "user's Ruling 69 of 2026-08-13 (D-677)",
        "ground": (
            "Amended #10 (D-174): a discarded finding is not an open obligation — no row, no gate, "
            "no capacity. Ruling 69 makes that reach a row already on the books THROUGH this "
            "derivation rather than by a hand-edited verdict, and the record's three elements were "
            "located at the record itself before it was consumed."
        ),
        "the_record": "tools/audit/discard_records.json → conforming (D-431 — no element is "
                      "restated here)",
        "★_the_D_438_verdict_it_replaces": d438,
        "what_it_does_NOT_do": (
            "The row STAYS OPEN and its status cell is untouched — a discard is not a resolution. "
            "What ends is the obligation, not the row."
        ),
    }


def build() -> dict:
    clause = locate_clause()
    # R1 (user, 2026-08-04) is recorded ON criterion C1, which is where a reader meets the
    # obligation it bounds. CRITERIA stays the authored constant; the ruling is attached at build
    # time because the clause it rests on and the withdrawn basis's grounds are both DERIVED.
    criteria = [dict(c) for c in CRITERIA]
    c1 = [c for c in criteria if c["id"] == "C1"]
    if len(c1) != 1:
        raise SystemExit("STOP: the criteria list does not carry exactly one C1 - the ruling that "
                         "bounds C1's reach has no unambiguous place to be recorded.")
    c1[0]["★_the_reach_of_C1_over_SUPERSEDED_entries"] = c1_reach_over_superseded(clause)
    c1[0]["★_the_reach_of_C1_over_a_superseded_entry_whose_content_is_a_REMOVAL"] = \
        c1_reach_over_a_removal()
    reg = register_facts()
    reads = reads_facts()
    scope = scope_block_facts(reads, reg)
    authored = gate_verdicts()
    outstanding = build_outstanding_delegations()   # #6 - the ONE derivation, imported not copied
    discards = build_discard_records()              # #6 - the ONE locator, imported not copied
    discarded_ids = {e["row"] for e in discards["conforming"]}

    rows = parse_rows()
    open_rows = [r for r in rows if r["open"]]
    by_id = {r["id"]: r for r in rows}

    stray = sorted(i for i in authored if i not in {r["id"] for r in open_rows})
    if stray:
        raise SystemExit("STOP: the committed apparatus declaration carries verdicts for rows "
                         "the INDEX no longer carries open: " + ", ".join(stray))

    # ---- the TRUE half, two nested cuts -------------------------------------------------
    narrow, wide = [], []
    for r in open_rows:
        subj = r["subject_column"].lower()
        blob = (r["title"] + " " + r["description_column"] + " " + r["status_column"]).lower()
        hits_subject = sorted({v for v in DOC_SUBJECT_VOCAB if v.lower() in subj})
        hits_text = sorted({s for s in FALSITY_SIGNALS if s in blob or s in subj})
        rec = {
            "id": r["id"],
            "title": r["title"][:220],
            "subject_column": r["subject_column"],
            "matched_on_the_subject_column": hits_subject,
            "matched_falsity_signals": hits_text,
            "gate": classify_gate(r, authored, discarded_ids),
            "★_the_same_verdict_with_the_discard_input_OFF": classify_gate(r, authored, set()),
        }
        if hits_subject:
            narrow.append(rec)
        if hits_subject or hits_text:
            wide.append(rec)

    narrow_ids = {r["id"] for r in narrow}
    wide_only = [r for r in wide if r["id"] not in narrow_ids]

    # the record's OWN authored classification of the same question
    by_ground: dict[str, list[str]] = {}
    for rid, a in authored.items():
        if a["verdict"] == "GATES":
            by_ground.setdefault(a["gate_ground"], []).append(rid)
    spec_truth = sorted(by_ground.get("specification truth", []))
    spec_completeness = sorted(by_ground.get("specification completeness", []))

    # ---- the gating split over the whole derived population --------------------------------
    gating = sorted(r["id"] for r in wide if r["gate"]["verdict"] == "GATES")
    non_gating = sorted(r["id"] for r in wide if r["gate"]["verdict"] == "NON-GATING")
    discarded = sorted(r["id"] for r in wide if r["gate"]["verdict"] == DISCARDED)

    # ---- the SAME cut with the discard input OFF, and the movement between them ------------
    #
    # The user's Ruling 69 is applied to a POPULATION, so the movement it causes is reported BOTH
    # WAYS rather than asserted: the cut is recomputed with the input off, and the difference must
    # be exactly the rows carrying a conforming discard record. Any other mover is a STOP — that is
    # the dispatch's own assumption A3, made mechanical rather than remembered.
    gating_off = sorted(r["id"] for r in wide
                        if r["★_the_same_verdict_with_the_discard_input_OFF"]["verdict"] == "GATES")
    non_gating_off = sorted(
        r["id"] for r in wide
        if r["★_the_same_verdict_with_the_discard_input_OFF"]["verdict"] == "NON-GATING")
    left_the_gate = sorted(set(gating_off) - set(gating))
    joined_the_gate = sorted(set(gating) - set(gating_off))
    if joined_the_gate:
        raise SystemExit(
            "STOP: the discard input put row(s) INTO the gate: " + ", ".join(joined_the_gate)
            + ". A discard can only take a row out; a row entering the gate means this input is "
            "doing something the ruling does not describe.")
    unexplained = sorted(r for r in left_the_gate if r not in discarded_ids)
    if unexplained:
        raise SystemExit(
            "STOP: row(s) left the gate with no conforming discard record: "
            + ", ".join(unexplained)
            + ". The both-ways recomputation must differ ONLY by rows carrying one.")
    unmoved = sorted(r for r in discarded_ids if r in gating)
    if unmoved:
        raise SystemExit(
            "STOP: row(s) carry a conforming discard record and are still in the gating set: "
            + ", ".join(unmoved) + ". The input was read and not applied.")
    if sorted(non_gating_off) != sorted(non_gating):
        raise SystemExit(
            "STOP: the discard input moved the NON-GATING set, which it may not touch: "
            + ", ".join(sorted(set(non_gating) ^ set(non_gating_off))) + ".")

    # The cut as it stood BEFORE the user's Ruling 56 moved D-639's reach IN set to the gating
    # side. It is DERIVED from the declaration's own record of what it moved, and it exists so the
    # reach derivation's population does not move when that derivation's own result is applied —
    # which would be circular. See the block it feeds for the full reason.
    app = json.loads(read(APPARATUS))
    moved_by_56 = list(app.get("★_the_ruling_56_application", {}).get("rows_moved", []))
    wide_ids = {r["id"] for r in wide}
    stray_moved = sorted(i for i in moved_by_56 if i not in wide_ids)
    if stray_moved:
        raise SystemExit(
            "STOP: the apparatus declaration records rows moved by Ruling 56 that this cut does "
            "not carry: " + ", ".join(stray_moved) + ". The reach derivation grades rows of the "
            "wide cut, so a moved row outside it means the two populations have come apart.")
    non_gating_before_56 = sorted(set(non_gating) | set(moved_by_56))

    # ---- A2, graded ------------------------------------------------------------------------
    derived_row_population = sorted({r["id"] for r in wide})
    a2_closed = [i for i in A2_RECOLLECTED if i in by_id and not by_id[i]["open"]]
    a2_absent = [i for i in A2_RECOLLECTED if i not in by_id]
    a2_hit = [i for i in A2_RECOLLECTED if i in derived_row_population]
    a2_miss = [i for i in A2_RECOLLECTED
               if i not in derived_row_population and i not in a2_closed and i not in a2_absent]
    derived_not_recollected = [i for i in derived_row_population if i not in A2_RECOLLECTED]

    return {
        "purpose": (
            "What D-231's PHASE 1 completion statement still requires, derived from D-231's own "
            "text and from the register and open-items data. THIS DERIVES; IT DOES NOT COMPLETE."
        ),
        "generated_by": "tools/audit/gen_phase1_completion_inventory.py",
        "generated_for": "cc_instruction_phase1_completion_inventory.md",
        "the_ruling": (
            "User, 2026-08-04 (R1): derive, as a measured list, exactly what phase 1's completion "
            "statement still requires - not from anyone's recollection."
        ),
        "what_this_file_does_not_do": (
            "It writes no completion statement, not even a partial one; it authorizes no fix, no "
            "design and no inference change; and it moves no register entry's class."
        ),
        "what_is_authored_and_what_is_derived": {
            "derived": (
                "D-231's clause, located by anchor and quoted; every register count and class; "
                "the open-row population and its OPEN subset (the apparatus declaration's own "
                "parser, imported); each candidate's gate verdict; the read programme's "
                "completion; the two scope-block checks"
            ),
            "authored": (
                "the criteria read out of D-231's sentence; the falsity-signal vocabulary; the A1 "
                "settlement; A2, the recollected list this file GRADES"
            ),
        },
        "the_requirement": {
            "source": "CLAUDE.md, the Conventions section; register entry D-231",
            **clause,
            "criteria": criteria,
        },
        "a1_does_the_completion_statement_rest_on_the_disposition_layer": A1,
        "the_reads_are_done": reads,
        "the_complete_half": {
            "criterion": "C1 and C2",
            "register_population": reg["decisions_recorded"],
            "by_home_class": reg["by_home_class"],
            "class_1_documentation_gap": {
                "what_it_is": (
                    "The register's own home_rule: a decision that governs a layer and is not "
                    "findable from that layer's section - a documentation gap carrying an "
                    "OPEN_ITEMS.md row. This is C1's outstanding population."
                ),
                "count": len(reg["gaps"]),
                "by_home_document": reg["gap_by_doc"],
                "ids": sorted(e["id"] for e in reg["gaps"]),
            },
            "class_1a_gap_whose_home_FAILS_the_section_criterion": {
                "what_it_is": (
                    "Entries carrying a home_section block whose verdict is EXCLUDE: the home "
                    "document exists and was graded, and the criteria in force (clause (a), "
                    "D-432, D-430) reject it. These are gaps WITH a measured reason."
                ),
                "count": len(reg["gap_section_classified"]),
                "by_reason": {k: {"count": len(v), "ids": sorted(v)}
                              for k, v in sorted(reg["excl_reason"].items())},
            },
            "class_1b_gap_NOT_YET_section_classified": {
                "what_it_is": (
                    "Gap-homed entries carrying NO home_section block at all. Their only writer "
                    "is gen_home_classification.py's apply mode, which is UNRUN under OI-305 / "
                    "OI-319 - so these entries have never been graded against the criteria in "
                    "force, and the completion statement cannot say they have."
                ),
                "count": len(reg["gap_unclassified"]),
                "every_one_entered_by_the_read_waves":
                    reg["gap_unclassified_all_from_the_read_waves"],
                "lowest_id": reg["gap_unclassified_lowest_id"],
                "the_row_that_owns_it": ["OI-305", "OI-319"],
                "what_DECISIONS_md_currently_claims": (
                    "'Every entry whose class is contract-home or gap therefore carries a "
                    "home_section block' - which this count contradicts at HEAD."
                ),
            },
            "class_2_recorded_only_on_a_tracking_surface": {
                "what_it_is": (
                    "The register's `unhomed` class: no home at all - the decision is recorded "
                    "only on a session handoff block or a superseded status archive."
                ),
                "count": len(reg["unhomed"]),
                "ids_and_homes": {e["id"]: e["home"] for e in sorted(reg["unhomed"],
                                                                    key=lambda x: x["id"])},
            },
            "class_3_defense_not_recorded": {
                "what_it_is": (
                    "C2's population. The standing convention forbids writing a defense "
                    "retroactively from memory, so this class is discharged by RECORDING a "
                    "defense the record holds or by stating the gap - never by inventing one. "
                    "The population is reported; no judgment about fillability is made here."
                ),
                "entries_with_no_rationale_at_all": {
                    "count": len(reg["no_defense"]),
                    "ids": sorted(e["id"] for e in reg["no_defense"]),
                },
                "entries_whose_rationale_says_derivation_not_recorded": {
                    "count": len(reg["said_not_recorded"]),
                    "ids": sorted(e["id"] for e in reg["said_not_recorded"]),
                },
            },
            "the_write_list_state": {
                "what_it_is": (
                    "The OI-293 / OI-327 write list: the homes the record MEANS to keep. Its "
                    "STATE is DERIVED, never read off the list - see the correction below."
                ),
                "★_corrected_2026-08-04_and_why": (
                    "This block used to report each row's authored `disposition_2026_08_04` "
                    "field, and the figure below used to be the list's MEMBERSHIP. Both were "
                    "wrong in the same way and in the same direction. The list carries no status, "
                    "and #12 keeps a satisfied ask in it rather than deleting it, so its "
                    "membership counts asks EVER MADE; and READ WAVE 6 answered two rows by "
                    "appending a SECOND field (`disposition_2026_08_04_wave6`) beside the first, "
                    "so reading only the first published 'NOT WRITTEN - WITHHELD' for a document "
                    "the user had since delegated to. Both are now derived at HEAD from the "
                    "delegation grades and the home data - OI-335, ruling R4 of 2026-08-04."
                ),
                "derived_at": "tools/audit/decisions/outstanding_delegations.json",
                "members": outstanding["the_write_list_at_head"]["members"],
                "state_summary": outstanding["the_write_list_at_head"]["summary"],
            },
        },
        "the_true_half": {
            "criterion": "C3",
            "the_records_own_authored_classification": {
                "what_it_is": (
                    "The committed non-gating apparatus declaration already carries an AUTHORED "
                    "per-row ground for every open row whose subject column matches its "
                    "documentation vocabulary. Two of its grounds are phase 1's own words."
                ),
                "gate_ground_specification_truth": spec_truth,
                "gate_ground_specification_completeness": spec_completeness,
            },
            "the_narrow_cut": {
                "what_it_is": (
                    "Open rows whose SUBJECT COLUMN carries the documentation vocabulary - the "
                    "same first cut the apparatus declaration uses."
                ),
                "count": len(narrow),
                "ids": sorted(r["id"] for r in narrow),
            },
            "the_wide_cut": {
                "what_it_is": (
                    "The narrow cut UNION every open row whose own text carries a "
                    "specification-falsity signal. Deliberately over-inclusive: an over-included "
                    "row simply carries its own gate verdict and is judged nowhere here."
                ),
                "★_THE_OVER_INCLUSION_IS_A_STATED_BOUND_and_is_NOT_measured": {
                    "the_ruling": (
                        "User, 2026-08-11, executed 2026-08-12 under dispatch "
                        "`cc_instruction_sitting_outcome_and_bound.md` Task 2. Two rulings meet "
                        "here: the item-7 reach derivation is ABANDONED rather than re-routed, and "
                        "this cut's over-inclusion is RECORDED AS A STATED BOUND in Ruling 59's "
                        "shape - advisory with the bound stated - and is NOT measured."
                    ),
                    "the_bound": (
                        "Membership is decided by an AUTHORED keyword vocabulary matched anywhere "
                        "in a row's title, description column, status column or subject column. "
                        "The over-inclusion that construction produces is deliberate and is "
                        "declared in the field above; HOW MUCH of it there is has never been "
                        "measured, and no measurement of it is seeded. So this population is a "
                        "CANDIDATE SET whose boundary is advisory: no statement about its "
                        "composition may be read as a measured property of it, in either "
                        "direction - a row carrying no signal is not thereby unowed, which the "
                        "reads-programme block below already says in its own words."
                    ),
                    "what_is_NOT_withdrawn": (
                        "Nothing above or below is retracted. Every member stands, every gate "
                        "verdict stands, and each is sourced where it was sourced. The bound "
                        "states what the membership BOUNDARY is worth; it says of no member that "
                        "it is wrongly in or wrongly out."
                    ),
                    "and_the_consuming_item_names_a_SECOND_class_this_cut_does_not_separate": (
                        "The finish line's TRUE-half item whose rows GATE states its own scope as "
                        "`Each row records a statement in a document of record that is false at "
                        "HEAD, or an obligation that keeps one from being checkable`. The second "
                        "clause is a different kind of thing from the first, and D-639's test - "
                        "does this row record a document stating something false - does not reach "
                        "it at all. This cut does not separate the two classes and was never "
                        "built to. That is why a reach verdict taken over this population would "
                        "not mean what the same verdict means over the population the reach "
                        "machinery was built for."
                    ),
                    "why_no_measurement_of_the_over_inclusion_is_SEEDED": (
                        "The ruling's own three grounds. (1) The amended #10 worth test discards "
                        "it: an unmeasured over-inclusion risks neither something being built "
                        "that fails the maximum-precision objective nor code becoming "
                        "incomparable against its specification. (2) The over-inclusion is "
                        "SELF-DECLARED in this cut's own field, so it is a stated bound and not a "
                        "hidden defect - which is the distinction D-654 turns on. (3) Most of the "
                        "gating population waits on user rulings, scheduled events, the phase "
                        "order or the `src/` freeze, as the per-row sizing at "
                        "`tools/audit/gating_row_sizing.json` records - no count is restated here "
                        "(D-431) - so measuring the over-inclusion would not open the gate."
                    ),
                    "where_the_finding_was_made": (
                        "`cowork_away_returns.md`, the STOP section of the abandoned reach "
                        "derivation batch, which states the finding and the three routes out in "
                        "full; none is restated here (#6). The abandonment and its ground are "
                        "recorded at that same section."
                    ),
                    "what_this_record_does_NOT_move": (
                        "No member enters or leaves this cut, no gate verdict moves, no row is "
                        "written and no status cell changes. It is not a mechanism change: what "
                        "the cut selects is untouched, and D-436 reserves a mechanism change to "
                        "the user."
                    ),
                },
                "count": len(wide),
                "ids": sorted(r["id"] for r in wide),
                "rows_the_narrow_cut_misses": sorted(r["id"] for r in wide_only),
            },
            "rows": sorted(wide, key=lambda r: (int(r["id"].split("-")[1]))),
        },
        "the_gating_split": {
            "the_test": (
                "D-438: does the row's subject bear on the analysis, its inputs, or an instrument "
                "a measurement depends on? If yes it gates. An establishment obligation (#19) "
                "always gates, whatever its subject."
            ),
            "applied_over": "the wide cut",
            "gates": {"count": len(gating), "ids": gating},
            "non_gating": {"count": len(non_gating), "ids": non_gating},
            "★_discarded_and_therefore_not_gating": {
                "what_it_is": (
                    "The third class the user's Ruling 69 of 2026-08-13 creates (D-677): rows whose "
                    "D-438 verdict is GATES and which carry a CONFORMING discard record — one "
                    "carrying its finding, its date and its reason, each located at the record "
                    "itself. They do not gate. THEY ARE NOT RESOLVED AND NOT APPARATUS: each stays "
                    "OPEN with its status cell untouched, and each keeps its D-438 verdict beside "
                    "the result so a reader can see which of the two questions took it out of the "
                    "gate."
                ),
                "why_it_is_a_class_of_its_own_rather_than_folded_into_non_gating": (
                    "The non-gating class is the APPARATUS class — rows D-438's test puts outside "
                    "the gate because their subject does not bear on the analysis — and the finish "
                    "line's item over it says so in its own name. A discarded row is outside the "
                    "gate for a different reason, and filing it there would make that item's name "
                    "false of one of its members. Folding it in would also lose which question "
                    "answered the row (#12)."
                ),
                "count": len(discarded),
                "ids": discarded,
                "the_records": "tools/audit/discard_records.json → conforming. No element of any "
                               "record is restated here (D-431).",
            },
            "★_the_discard_input_reported_BOTH_WAYS": {
                "why": (
                    "Ruling 69 changes what a derivation READS, so the movement it causes is shown "
                    "rather than asserted: the same cut is recomputed with the input OFF and the "
                    "two are diffed. The pre-input cut is kept beside the result (#12) so a reader "
                    "comparing artifacts can see exactly what moved and by what."
                ),
                "with_the_input_OFF": {"gates": {"count": len(gating_off), "ids": gating_off},
                                       "non_gating": {"count": len(non_gating_off),
                                                      "ids": non_gating_off}},
                "with_the_input_ON": {"gates": {"count": len(gating), "ids": gating},
                                      "non_gating": {"count": len(non_gating), "ids": non_gating},
                                      "discarded": {"count": len(discarded), "ids": discarded}},
                "rows_that_LEFT_the_gate": left_the_gate,
                "rows_that_JOINED_the_gate": joined_the_gate,
                "the_STOPs_that_are_armed": [
                    "a row that JOINS the gate under this input — a discard can only take a row "
                    "out",
                    "a row that LEAVES the gate carrying no conforming discard record — the "
                    "movement must be explained by the input and by nothing else",
                    "a row carrying a conforming discard record that is still gating — the input "
                    "read and not applied",
                    "any movement in the NON-GATING set, which this input may not touch",
                ],
                "★_a_result_where_NOTHING_MOVES_is_a_correct_outcome": (
                    "It would mean no row of this population carries a conforming discard record, "
                    "which is a fact about the record and not a failure of the derivation. Nothing "
                    "here is adjusted to produce a movement."
                ),
            },
            "non_gating_before_the_ruling_56_application": {
                "what_it_is": (
                    "The same cut taken BEFORE the user's Ruling 56 moved D-639's reach derivation's "
                    "IN set to the gating side — that is, the rows the apparatus declaration classes "
                    "non-gating on D-438's criterion alone."
                ),
                "why_it_is_published": (
                    "It is the population the reach derivation grades, and it must not move when "
                    "that derivation's own result is applied. Without it the two are circular: the "
                    "derivation's verdicts would leave the set they were graded over, its STOP would "
                    "fire, retiring them would empty the IN set, and the application would reverse "
                    "itself on the next regeneration. This cut is invariant under the application, "
                    "so the fixed point is the one the ruling intends."
                ),
                "count": len(non_gating_before_56),
                "ids": non_gating_before_56,
                "moved_by_the_ruling": moved_by_56,
                "derived_from": ("tools/audit/nongating_apparatus_rows.json → "
                                 "★_the_ruling_56_application.rows_moved"),
                "★_this_cut_IS_a_reported_widening_and_the_user_has_ACCEPTED_it": {
                    "what_was_widened": (
                        "Ruling 56 named no machinery. Publishing this second cut, and pointing the "
                        "reach derivation at it, is the smallest thing that removes the circularity "
                        "described above — and it is more than the ruling's letter said. It was "
                        "REPORTED at `cowork_away_returns.md` §1.17 in the act that took it, with "
                        "the one edit that reverses it and that edit's consequence stated beside it."
                    ),
                    "the_ruling": (
                        "User, 2026-08-11, Ruling 57 of "
                        "`cowork_rulings_2026_08_11_thirteenth_stop.md`: the §1.17 reported widening "
                        "is ACCEPTED. The pre-application cut this block publishes, and the reach "
                        "derivation's reading of it, STAND."
                    ),
                    "the_ground_the_ruling_gives": (
                        "Without them Ruling 56 is circular and inapplicable, and the stated reversal "
                        "edit would reverse the user's own ruling. Accepted on the reported-widening "
                        "ground, D-654 — a widening REPORTED is reviewable and a widening HIDDEN is "
                        "not; the narrow-letter default for every future licence is unchanged."
                    ),
                    "what_the_acceptance_does_NOT_move": (
                        "No verdict, no criterion, no row and no count moved by this machinery when "
                        "it was built, and none moves by its acceptance. D-438 and its criterion are "
                        "untouched and still decide every other row; the two cuts differ by exactly "
                        "the rows the apparatus declaration records as moved."
                    ),
                },
            },
            "where_each_verdict_came_from": {
                "the committed apparatus declaration":
                    sorted(r["id"] for r in wide
                           if r["gate"]["source"].startswith("the committed")),
                "the row's own recorded words":
                    sorted(r["id"] for r in wide
                           if r["gate"]["source"] == "the row's own recorded words"),
                "D-438's default":
                    sorted(r["id"] for r in wide if r["gate"]["source"] == "D-438's default"),
                "the row's DISCARD record (the user's Ruling 69, D-677)":
                    sorted(r["id"] for r in wide
                           if r["gate"]["source"].startswith("the row's DISCARD record")),
            },
        },
        "what_the_register_says_about_itself_that_is_no_longer_true": scope,
        "the_question_the_two_halves_do_not_settle": {
            "the_question": (
                "Does phase 1's TRUE half reach a document's account of ITSELF - a status banner, "
                "an as-built anchor, a missing supersession note - or only its account of the "
                "analysis?"
            ),
            "why_it_is_live": (
                "D-231's own reason for the half is 'because a specification cannot be the "
                "compliance standard while it misdescribes the code', which names the code. "
                "D-438's declaration draws the same line and classes banner/anchor rows as "
                "apparatus. On that reading OI-332 - three documents that misdescribe their own "
                "state - is outside the TRUE half, and its non-gating verdict follows. On the "
                "plain reading of 'states something false at HEAD' it is inside."
            ),
            "who_settles_it": "the user. It is reported, not decided.",
            "what_turns_on_it": (
                "Whether the completion statement must wait on the apparatus-classed doc rows, "
                "which the non-gating declaration explicitly leaves open and owed."
            ),
        },
        "what_the_completion_statement_COULD_already_say": {
            "note": (
                "Derived, and stated here as facts that are established - NOT as draft text. "
                "The statement itself is not written in this wave and this list is not one."
            ),
            "facts": [
                {
                    "fact": "The owed reading set is empty.",
                    "derived_from": (
                        "the regime's partition plus each wave's own yield artifact, recomputed "
                        "in `the_reads_are_done` rather than taken from any wave's assertion"
                    ),
                },
                {
                    "fact": (
                        "Of the register's entries, the ones whose home the register's own "
                        "home_rule declares CORRECT are: homed in a layer specification, "
                        "contract-home, process, and project-convention."
                    ),
                    "count": sum(v for k, v in reg["by_home_class"].items()
                                 if k not in ("gap", "unhomed")),
                    "of": reg["decisions_recorded"],
                },
                {
                    "fact": (
                        "Every harvested cluster carries a recorded disposition at the committed "
                        "artifact, so no harvested statement was silently passed over."
                    ),
                    "qualification": (
                        "True of the committed layer only. It cannot be refreshed at HEAD "
                        "(OI-333), so no CURRENT residual may be published - see A1."
                    ),
                },
                {
                    "fact": (
                        "The home classification was applied in full over the pre-wave "
                        "population: every entry entered before the read waves carries a "
                        "home_section block with the criterion that decided it."
                    ),
                    "qualification": (
                        "It stops there. The entries the read waves entered carry none, because "
                        "the applier is unrun (OI-305 / OI-319)."
                    ),
                },
            ],
        },
        "the_shape_of_what_remains": {
            "note": "Derived from the blocks above; every figure is computed, none transcribed.",
            "complete_half": {
                "entries_not_homed_in_a_specification_that_owns_them":
                    len(reg["gaps"]) + len(reg["unhomed"]),
                "of_which_never_graded_against_the_criteria_in_force":
                    len(reg["gap_unclassified"]),
                "entries_whose_defense_the_record_does_not_state": len(reg["no_defense"]),
                "documents_awaiting_a_delegation_only_the_user_may_write":
                    len(outstanding["THE_OUTSTANDING_SET"]["members"]),
                "★_that_figure_is_now_DERIVED_not_the_write_lists_membership": (
                    "It is the count of documents that still lose entries to the DELEGATION HALF "
                    "where an admitting delegation already exists - the only class a delegation "
                    "the user writes would move. Derived at "
                    "`tools/audit/decisions/outstanding_delegations.json`; the full partition, "
                    "including the classes for which a delegation is NOT the remedy, is there and "
                    "is not restated here (D-431). OI-335."
                ),
                "entries_lost_for_want_of_a_delegation_all_classes":
                    outstanding["counted"]["lost_for_want_of_a_delegation"],
                "of_which_a_widening_would_move":
                    outstanding["counted"]["of_which_a_widening_would_move"],
            },
            "true_half": {
                "open_rows_in_the_wide_cut": len(wide),
                "of_which_gate": len(gating),
                "of_which_apparatus_and_therefore_non_gating": len(non_gating),
                "rows_the_records_own_authored_classification_puts_on_specification_truth":
                    len(spec_truth),
            },
            "outside_both_halves_and_owed_before_the_statement": {
                "what": (
                    "The register's own published account of itself states things that are no "
                    "longer true at HEAD (see `what_the_register_says_about_itself_that_is_no_"
                    "longer_true`, and OPEN_ITEMS.md OI-334). A completion statement resting on "
                    "DECISIONS.md rests on them."
                ),
                "statements_checked": len(
                    [k for k in scope if k.startswith("statement_")]),
            },
        },
        "the_recollection_grade": {
            "what_this_is": A2_NOTE,
            "a2_as_recollected": A2_RECOLLECTED,
            "carried_by_the_derivation": sorted(a2_hit),
            "recollected_but_NOT_in_the_derived_population": {
                i: {
                    "subject_column": by_id[i]["subject_column"],
                    "gate": classify_gate(by_id[i], authored, discarded_ids),
                    "why_this_cut_does_not_reach_it": (
                        "The TRUE half's cut searches for a row asserting that a SPECIFICATION "
                        "states something false at HEAD. This row's subject column and text "
                        "carry no such signal - which does not make the row unowed: it may be "
                        "outstanding on the COMPLETE half or as an establishment obligation "
                        "(#19), neither of which this cut searches."
                    ),
                } for i in sorted(a2_miss)
            },
            "recollected_but_already_CLOSED_in_the_index": sorted(a2_closed),
            "recollected_but_absent_from_the_index_entirely": sorted(a2_absent),
            "derived_but_NOT_recollected": derived_not_recollected,
            "how_to_read_it": (
                "The derivation is the answer; this block measures the recollection against it. "
                "A recollected row that the derivation does not carry is not thereby wrong - it "
                "may be outstanding on a ground this cut does not search (the COMPLETE half, or "
                "an establishment obligation) - and each is stated rather than scored."
            ),
        },
        "counted": {
            "decisions_recorded": reg["decisions_recorded"],
            "open_rows_in_the_index": len(open_rows),
            "true_half_wide_cut": len(wide),
            "true_half_gating": len(gating),
            "complete_half_gap": len(reg["gaps"]),
            "complete_half_unhomed": len(reg["unhomed"]),
            "complete_half_defense_gaps": len(reg["no_defense"]),
        },
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT)
            return 1
        print("OK: phase-1 completion inventory re-derives byte-identically.")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print("wrote", OUT)
    c = art["counted"]
    print(f"  register {c['decisions_recorded']} entries; open rows {c['open_rows_in_the_index']}")
    print(f"  COMPLETE half: gap {c['complete_half_gap']}, unhomed {c['complete_half_unhomed']}, "
          f"defense gaps {c['complete_half_defense_gaps']}")
    print(f"  TRUE half: {c['true_half_wide_cut']} candidates, {c['true_half_gating']} gating")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
