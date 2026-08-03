#!/usr/bin/env python3
"""Generate `tools/audit/decisions/phase1m_measurements.json` — the phase-1m measurements.

WHAT THIS IS.  The phase-1m dispatch
(`cc_instruction_phase1m_dispositions_and_measurements.md`) orders two MEASUREMENTS and
forbids acting on either:

  * Task 5 — the KIND test.  The user replaced the delegation-specificity criterion's
    third clause ("stable enough to be cited") with a test on the document's KIND: does
    it state what shall be (specification, contract, design, component spec, binding
    plan) or record what was found (audit, report, census, inventory, measurement
    artifact, probe, dossier of findings)?  This tool re-runs the whole home population
    under clauses (a)+(b) as measured at phase 1l — RE-VERIFIED here — plus the kind
    clause, and reports what would move.  NOTHING is applied: no entry's
    `nonspec_kind` is written by this tool, which only reads `backbone_decisions.json`.

  * Task 6 — the reading yield.  Measure the decision yield of the design documents
    already read in full, rank the documents still owed a full read by observable
    features, and state the proxy as a PREMISE (#17d) rather than a fact.

WHY A GENERATOR.  Principle #17(f): no hand-transcribed measurement numbers.  Every
count in the phase-1m report and in the dated notes on `open_items/OI-281.md` and
`open_items/OI-207.md` is computed here from the committed artifacts.  Only the two
AUTHORED tables below — `KIND` and `DELEGATION` — are judgments, and each carries the
citation it was judged from, read with the file tools in the phase-1m session.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : KIND (the kind judgment per document, with its citation)
             DELEGATION (clauses (a)+(b) per document, with its citation)
             READ_WAVES (which wave read which document, with its citation)
  derived  : the home population and every count over it; the read/owed partition off
             the same cluster artifacts the phase-1g triage derives its surface from;
             per-document sizes, cluster counts and by-name mentions; the yield figures.

Run:  python tools/audit/decisions/gen_phase1m_measurements.py [--check]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
CLUSTERS = os.path.join(HERE, "decision_clusters.json")
DISPOS = os.path.join(HERE, "cluster_dispositions.json")
OUT = os.path.join(HERE, "phase1m_measurements.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
import gen_phase1g_triage as triage          # noqa: E402  (the read set + the classification)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# Characters per token, measured on this repository's own prose by the phase-1d wave and
# re-used unchanged by phases 1f and 1g.
CHARS_PER_TOKEN = 3.04

# The three surfaces whose USER ratification is not in question — the same three phase 1l
# searched, and the only places a delegation can come from under the criterion.
RATIFIED_SURFACES = ["ARCHITECTURE.md", "CLAUDE.md", "cowork_engage_arc_plan.md"]

RULE, FINDING, KIND_UNCLEAR = "states-rules", "records-findings", "kind-unclear"

# ---------------------------------------------------------------------------
# AUTHORED (1/3) — the KIND judgment.  file -> (kind, citation).
# The operative question is the document's PURPOSE: does it state what shall be, or
# record what was found?  The banner's self-description is not the test — but the
# document's own opening sentence is the evidence for what it is FOR, so it is what is
# cited.  Every citation below was read with the file tools in the phase-1m session.
# ---------------------------------------------------------------------------
KIND: dict[str, tuple[str, str]] = {
    "cowork_layer3_keymode_design.md": (RULE,
        "`:1` 'Architectural Layer 3 — KEY/MODE — Architecture & Design'; SIGNED (user, "
        "2026-06-22). A layer specification: it states how the layer must behave."),
    "cowork_layer4_chordsymbol_design.md": (RULE,
        "`:1` 'Architectural Layer 4 — CHORD SYMBOL (with NON-CHORD TONES) — Architecture & "
        "Design'; SIGNED (user, 2026-06-24). A layer specification."),
    "cowork_layer5_function_design.md": (RULE,
        "`:1` 'Architectural Layer 5 — FUNCTION … — Architecture & Design'; SIGNED (user, "
        "2026-06-26). A layer specification."),
    "cowork_layer5_engagement_design.md": (RULE,
        "`:1` 'Layer-5 engagement design — Part 1: the CARRY and the SELECTION architecture'; "
        "`:2` 'READ-ONLY architectural design pass'. A design: it states how engaged Layer 5 "
        "must read the carry and select among the carried readings."),
    "cowork_bounded_context_design.md": (RULE,
        "`:1` 'Bounded context & selection-extension — cross-layer architecture & design'; "
        "SIGNED (user, 2026-07-02), and `:2-3` makes it a build GATE. A cross-layer contract."),
    "cowork_voiceleading_axis_design.md": (RULE,
        "`:1` 'The voice-leading axis (axis 2) — architecture and foundation components "
        "(design)'; AS-BUILT + SIGNED (user, 2026-07-03). A design."),
    "cowork_progression_schema_dictionary.md": (RULE,
        "`:1` 'The Harmonic Vocabulary — progression & substitution knowledge base (component "
        "spec)'; `:3` 'component spec … Specified by rule and content.' A component "
        "specification — the kind the dispatch names explicitly."),
    "cowork_confidence_contract.md": (RULE,
        "`:3-5` 'This is a **contract document** — it fixes definitions, normalization "
        "requirements, comparison rules, and calibration obligations'. It says in terms that "
        "it states what shall be."),
    "cowork_notation_output_contract.md": (RULE,
        "`:1` 'The notation output-surface contract — the A-native record'; `:6-7` 'This is "
        "the contract-drafting step'. A contract."),
    "cowork_stage5_fitter_design.md": (RULE,
        "`:1` 'Stage-5 Weight-Fitting (\"the fitter\") — Design'; SIGNED (user, 2026-07-04). A "
        "design: it states the protocol the fit must follow."),
    "cowork_prefit_gates.md": (RULE,
        "`:1-5` 'The pre-fit gates for the joint estimator … the four protocols … changing any "
        "protocol constant hereafter is a protocol amendment (#22), not a tuning act.' "
        "Protocols are rules."),
    "docs/scoring_model.md": (RULE,
        "`:2` 'LIVE MANDATORY REFERENCE — the scoring pipeline's one specification'. A "
        "specification. (Its §8 constraints are stated to remain in force; that the mechanism "
        "it describes is dormant is a subject question, not a kind question.)"),
    "docs/decoder_design.md": (RULE,
        "`:1-2` 'Stage 3 — Chord-Path Decoder Design … design-only, no production code'. A "
        "design."),
    "cowork_joint_key_chord_design.md": (RULE,
        "`:1` 'The joint key-and-chord step — architecture design'. A design. The kind test "
        "does not ask whether it is shelved — that was the clause the kind test REPLACES."),
    "cowork_engage_arc_plan.md": (RULE,
        "`:1-5` 'The Engage-Arc Path Forward — ratified, principle-grounded … The standing "
        "reference for the order of work … This document fixes the **order and the principle "
        "behind each step**'. A binding plan — the kind the dispatch names explicitly."),

    "cowork_score_census.md": (FINDING,
        "`:1-3` 'The score & corpus census — once-and-for-all, enumerated to closure … The "
        "definitive census of obtainable symbolic scores and harmonic ground-truth corpora'. A "
        "census. (See `kind_unclear_notes` — §8c inside it does state a rule.)"),
    "cowork_structural_integrity_audit.md": (FINDING,
        "`:1-2` 'Structural-Integrity Audit … Status: read-only grounded catalogue'; `:5-6` "
        "'Every fix named here is a later, separate, user-ratified refactor — this document "
        "queues them, it does not act.' An audit, by its own account."),
    "cowork_architecture_reassessment.md": (FINDING,
        "`:1-2` 'Architecture & Implementation-Plan RE-ASSESSMENT (2026-06-20) … Status: "
        "PLANNING RE-ASSESSMENT — ITS FOUR META-FINDINGS WERE RULED SUPERSEDED'. It records "
        "findings; the findings themselves were ruled superseded (OI-270)."),
    "docs/iteration_path1_summary.md": (FINDING,
        "`:1-2` 'Iteration Path 1 — Closing Summary … Status: ITERATION-ERA RECORD (path 1) … "
        "Not a current plan.' A closing record."),

    "docs/implementation_roadmap.md": (KIND_UNCLEAR,
        "BOTH at once. `:5-6` 'This document is the single tracker ensuring every review "
        "conclusion is addressed' — a tracking surface; `:10-11` 'Standing rule for this "
        "roadmap: an item may only be marked done with the evidence listed in its verify "
        "column' and `:141-164` the user-ratified engage criteria + retirement map — rules. "
        "The dispatch's own §6.1 names this population."),
    "docs/redesign_plan.md": (KIND_UNCLEAR,
        "A plan by kind (`:1` 'Redesign Plan — Layered Comprehensive Evidence Architecture'), "
        "converted to a record by a USER-RATIFIED banner (`:2-4`, ratified 2026-08-03): "
        "'SUPERSEDED AS A PLAN — RETAINED AS THE RECORD OF WHAT WAS TRIED AND CLOSED'. Kind "
        "and status disagree, and the banner here is not a self-description but a ruling."),
    "cowork_notation_adoption_increment.md": (KIND_UNCLEAR,
        "`:1` 'The notation-layer adoption increment — decision surface'. A decision surface "
        "presents options and records the rulings made on them: the options are findings, the "
        "rulings are rules. The dispatch's kind list contains no entry for this shape."),
}

# ---------------------------------------------------------------------------
# AUTHORED (2/3) — clauses (a)+(b): does a USER-RATIFIED surface delegate to the document
# BY NAME, FOR A STATED CONCERN?  file -> (verdict, citation).
# Every mention was re-derived mechanically this session (`mentions` in the emitted
# artifact) and then read in place to judge whether it delegates or merely cites.
# ---------------------------------------------------------------------------
DELEG_PASS, DELEG_FAIL, DELEG_UNCLEAR = "pass", "fail", "unclear"
DELEGATION: dict[str, tuple[str, str]] = {
    "cowork_layer3_keymode_design.md": (DELEG_PASS,
        "`ARCHITECTURE.md:1329` 'The ratified contract for this layer is …'"),
    "cowork_layer4_chordsymbol_design.md": (DELEG_PASS,
        "`ARCHITECTURE.md:1405` 'The ratified contract for this layer is …'"),
    "cowork_layer5_engagement_design.md": (DELEG_PASS,
        "`ARCHITECTURE.md:1483` the delegation pointer, AND independently "
        "`cowork_engage_arc_plan.md:41`, `:46`, `:53-55`"),
    "cowork_bounded_context_design.md": (DELEG_PASS,
        "`ARCHITECTURE.md:909-913` 'The ONE detailed cross-layer spec for this contract is …'"),
    "cowork_confidence_contract.md": (DELEG_PASS,
        "`ARCHITECTURE.md:948-949` '…are stated in full in `cowork_confidence_contract.md`'"),
    "cowork_notation_output_contract.md": (DELEG_PASS,
        "`ARCHITECTURE.md:73` '…contract `cowork_notation_output_contract.md`'"),
    "cowork_stage5_fitter_design.md": (DELEG_PASS,
        "`ARCHITECTURE.md:283` 'the fitting event's own design contract is …'"),
    "docs/scoring_model.md": (DELEG_PASS,
        "`CLAUDE.md:651-691` — a standing section naming it, making it a mandatory read and "
        "binding a same-commit sync rule to it"),
    "cowork_progression_schema_dictionary.md": (DELEG_PASS,
        "`ARCHITECTURE.md:4591` 'formalised as an independent knowledge-base component with "
        "its own spec (`…`)'; `:4539` declines to restate its content in terms"),
    "cowork_score_census.md": (DELEG_PASS,
        "`ARCHITECTURE.md:317` 'The constraint's own detailed block, with the per-licence-class "
        "pool table, is `cowork_score_census.md` §8c', inside a user-ratified passage; and "
        "`CLAUDE.md:388`"),
    "cowork_structural_integrity_audit.md": (DELEG_PASS,
        "`cowork_engage_arc_plan.md:4` (RATIFIED user 2026-07-07) 'It does not re-derive the "
        "fix details — those live in `cowork_structural_integrity_audit.md` (§3 fix-queue, §4 "
        "sequencing)'"),
    "cowork_joint_key_chord_design.md": (DELEG_PASS,
        "`cowork_engage_arc_plan.md:44` 'arc #10 — the joint key-and-chord step (`…`)' — by "
        "name, for a stated concern"),
    "cowork_engage_arc_plan.md": (DELEG_PASS,
        "`CLAUDE.md:130` names it for a stated concern — the MEASURE-BEFORE-BUILD gate, 'now "
        "the middle stage of the #17 funnel'"),

    "cowork_architecture_reassessment.md": (DELEG_FAIL,
        "NOT NAMED in any of the three surfaces (re-derived mechanically this session)"),
    "docs/decoder_design.md": (DELEG_FAIL,
        "NOT NAMED in any of the three surfaces (re-derived mechanically this session)"),
    "docs/implementation_roadmap.md": (DELEG_FAIL,
        "NOT NAMED in any of the three surfaces (re-derived mechanically this session) — "
        "though it calls itself 'the single tracker'"),
    "docs/iteration_path1_summary.md": (DELEG_FAIL,
        "NOT NAMED in any of the three surfaces (re-derived mechanically this session)"),
    "docs/redesign_plan.md": (DELEG_FAIL,
        "Named three times (`ARCHITECTURE.md:775`, `:789`, `:800`), each a citation ('Design "
        "reference: …'), and two sit inside blocks `ARCHITECTURE.md:783-786` itself banners "
        "SUPERSEDED, 'retained only as history — do not build to it'"),

    "cowork_voiceleading_axis_design.md": (DELEG_UNCLEAR,
        "`ARCHITECTURE.md:900` 'Criterion + build home: `…` §0/§5.3 (AS-BUILT)', `:928` "
        "'design-gated (`…`)', `:1507`. Each names a concern; none is the 'the ratified "
        "contract for X is Y' form. Does 'build home' delegate, or cite?"),
    "cowork_layer5_function_design.md": (DELEG_UNCLEAR,
        "`ARCHITECTURE.md:1480-1481` 'Full spec: `cowork_layer5_function_design.md`.' — two "
        "words of concern and nothing more, appended to a paragraph; compare `:1483` directly "
        "beneath it, which IS a delegation clause"),
    "cowork_prefit_gates.md": (DELEG_UNCLEAR,
        "`ARCHITECTURE.md:49` in a list of citations and `:280` 'Protocols ratified 2026-07-19 "
        "(`…`)' — attributions of where something was ratified, not instructions to read it "
        "instead of the section"),
    "cowork_notation_adoption_increment.md": (DELEG_UNCLEAR,
        "★ CORRECTION OF RECORD: phase 1l recorded this document as 'named in NONE of the "
        "three surfaces'. It is named in two — `ARCHITECTURE.md:4660` 'the pedal-point ruling "
        "of the notation-adoption increment (`…` §7 + §10)' and `CLAUDE.md:128` 'analysis in "
        "`…` §2'. Both name a concern; both are attributions of where a ruling's analysis "
        "lives, the same shape as `cowork_prefit_gates.md`, so the verdict is UNCLEAR, not "
        "FAIL"),
}

# ---------------------------------------------------------------------------
# AUTHORED (3/3) — which wave read which design document IN FULL.
# Phases 1d and 1f are the triage generator's own lists (its source of record, cited
# there to `cc_phase1d_enumeration_wave_report.md` and the OI-207 note of 2026-08-02);
# phase 1g's five are the triage's TASK2_FULL_READ; phases 1h…1l are the per-wave dated
# notes on `open_items/OI-207.md`, cited per wave below.
# ---------------------------------------------------------------------------
READ_WAVES: dict[str, tuple[list[str], str]] = {
    "1d": (list(triage.PHASE1D_READ),
           "`gen_phase1g_triage.py` PHASE1D_READ, sourced to "
           "`cc_phase1d_enumeration_wave_report.md`'s Task-1 table"),
    "1f": (list(triage.PHASE1F_READ),
           "`gen_phase1g_triage.py` PHASE1F_READ, sourced to the OI-207 dated note of "
           "2026-08-02 (`docs/beam_widening_design.md` is in BOTH lists)"),
    "1g": (list(triage.TASK2_FULL_READ),
           "`gen_phase1g_triage.py` TASK2_FULL_READ — the five the phase-1g dispatch sent to "
           "a full read in the same session"),
    "1h": (["cowork_layer3_keymode_design.md", "cowork_score_census.md",
            "cowork_joint_key_chord_design.md", "cowork_layer5_engagement_design.md",
            "cowork_voiceleading_axis_design.md"],
           "`open_items/OI-207.md:223-229` — the phase-1h note's own read table"),
    "1i": (["cowork_structural_integrity_audit.md"],
           "`open_items/OI-207.md`, the phase-1i dated note (D-401…D-405)"),
    "1j": (["cowork_progression_schema_dictionary.md"],
           "`open_items/OI-207.md`, the phase-1j dated note (D-406…D-414)"),
    "1k": (["docs/implementation_roadmap.md"],
           "`open_items/OI-207.md:1052-1055` — the phase-1k note (D-415…D-423)"),
    "1l": (["cowork_notation_adoption_increment.md"],
           "`open_items/OI-207.md:1119-1122` — the phase-1l note (D-424…D-426)"),
}


# ── derivation helpers ───────────────────────────────────────────────────────

def unresolved_by_file() -> tuple[dict[str, int], int]:
    """Per-file unresolved-cluster attributions over the design-document surface.

    Identical derivation to `gen_phase1g_triage.derive_unread`, minus its read-set
    filter, so the two artifacts cannot disagree about what the surface is.
    """
    clusters = json.load(open(CLUSTERS, encoding="utf-8"))["clusters"]
    by_id = {c["cluster_id"]: c for c in clusters}
    dispos = json.load(open(DISPOS, encoding="utf-8"))["dispositions"]
    counts: collections.Counter = collections.Counter()
    for d in dispos:
        if d["disposition"] != "unresolved":
            continue
        cl = by_id[d["cluster_id"]]
        files = cl["files"] or [cl["proposed_representative"]["file"]]
        surfaces = {triage.surface_of(f) for f in files}
        if None in surfaces or len(surfaces) > 1:
            continue
        for f in set(files):
            counts[f] += 1
    return dict(counts), len(counts)


def file_facts(rel: str) -> dict:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return {"exists": False, "bytes": 0, "lines": 0, "banner": None}
    raw = open(path, encoding="utf-8", errors="replace").read()
    head = "\n".join(raw.splitlines()[:14])
    words = ["SUPERSEDED", "SHELVED", "SIGNED", "USER-RATIFIED", "RATIFIED", "AS-BUILT",
             "DELIVERED", "DRAFT", "DESIGN", "LIVE"]
    banner = [w for w in words if re.search(r"\b" + re.escape(w) + r"\b", head)]
    return {"exists": True, "bytes": len(raw.encode("utf-8")),
            "lines": len(raw.splitlines()), "banner_words": banner}


def mentions_in_ratified_surfaces() -> dict[str, list[str]]:
    """Every by-name mention of any design document in the three user-ratified surfaces."""
    text = {s: open(os.path.join(ROOT, s), encoding="utf-8",
                    errors="replace").read().splitlines() for s in RATIFIED_SURFACES}
    out: dict[str, list[str]] = collections.defaultdict(list)
    names = set(KIND) | set(DELEGATION)
    for name in names:
        base = name.split("/")[-1]
        for s, lines in text.items():
            for i, line in enumerate(lines, 1):
                if base in line:
                    out[name].append(f"{s}:{i}")
    return dict(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate into memory and report whether the artifact matches")
    args = ap.parse_args()

    backbone = json.loads(open(BACKBONE, encoding="utf-8").read())
    decisions = backbone["decisions"]

    # ── Task 5 — the kind test over the home population ──────────────────────
    population = [d for d in decisions
                  if not d.get("home_is_layer_spec")
                  and d.get("nonspec_kind") in ("contract-home", "gap")]
    per_doc: dict[str, dict] = {}
    for d in population:
        doc = d["home"].split(":")[0]
        rec = per_doc.setdefault(doc, {"entries": [], "current": collections.Counter()})
        rec["entries"].append(d["id"])
        rec["current"][d["nonspec_kind"]] += 1

    unknown = sorted(set(per_doc) - set(KIND))
    if unknown:
        raise SystemExit(f"home document(s) with no authored KIND judgment: {unknown}")
    unknown = sorted(set(per_doc) - set(DELEGATION))
    if unknown:
        raise SystemExit(f"home document(s) with no authored DELEGATION judgment: {unknown}")

    mentions = mentions_in_ratified_surfaces()
    for doc, (verdict, _cite) in DELEGATION.items():
        named = bool(mentions.get(doc))
        if verdict == DELEG_FAIL and named and doc != "docs/redesign_plan.md":
            raise SystemExit(
                f"DELEGATION says {doc} is not named, but it is: {mentions[doc]}")

    kind_rows = []
    tally = collections.Counter()
    moves = {"in": [], "out": [], "ambiguous": []}
    for doc in sorted(per_doc, key=lambda k: (-len(per_doc[k]["entries"]), k)):
        rec = per_doc[doc]
        kind, kind_cite = KIND[doc]
        deleg, deleg_cite = DELEGATION[doc]
        # Precedence.  The criterion requires BOTH halves, so either half failing is
        # decisive and the other need not be judged: a document no user-ratified surface
        # delegates to is excluded whatever kind it is, and a findings-kind document is
        # excluded however specific the delegation.  Only where nothing is decisive —
        # an unclear delegation over a rule-stating kind, or an unclear KIND over a
        # delegation that passes — is the entry ambiguous.
        if deleg == DELEG_FAIL or kind == FINDING:
            verdict = "EXCLUDE"
        elif deleg == DELEG_PASS and kind == RULE:
            verdict = "ADMIT"
        else:
            verdict = "AMBIGUOUS"
        n = len(rec["entries"])
        tally[verdict] += n
        cur_ch = rec["current"]["contract-home"]
        cur_gap = rec["current"]["gap"]
        movement = "none"
        if verdict == "ADMIT" and cur_gap:
            movement, moves["in"] = "MOVES IN", moves["in"] + [(doc, cur_gap)]
        elif verdict == "EXCLUDE" and cur_ch:
            movement, moves["out"] = "MOVES OUT", moves["out"] + [(doc, cur_ch)]
        elif verdict == "AMBIGUOUS":
            moves["ambiguous"].append((doc, n, cur_ch, cur_gap))
        kind_rows.append({
            "document": doc, "entries": n, "entry_ids": rec["entries"],
            "current_contract_home": cur_ch, "current_gap": cur_gap,
            "kind": kind, "kind_citation": kind_cite,
            "delegation": deleg, "delegation_citation": deleg_cite,
            "verdict": verdict, "movement": movement,
            "mentions_in_ratified_surfaces": mentions.get(doc, []),
        })

    # ── Task 6 — the read/owed partition and the yield ───────────────────────
    unresolved, surface_files = unresolved_by_file()
    read: dict[str, list[str]] = {}
    for wave, (docs, _cite) in READ_WAVES.items():
        for doc in docs:
            read.setdefault(doc, []).append(wave)
    missing = sorted(d for d in read if d not in unresolved)
    if missing:
        raise SystemExit(f"read document(s) absent from the derived surface: {missing}")

    excluded = sorted(f for f, (cls, _r) in triage.CLASSIFICATION.items()
                      if cls != triage.LIVE and f not in read)
    owed = sorted(f for f in unresolved if f not in read and f not in excluded)

    homed = collections.Counter(d["home"].split(":")[0] for d in decisions)
    prov = collections.Counter()
    for d in decisions:
        for f in set(re.findall(r"reading \`([^\`]+)\` IN FULL", d["status_source"])):
            prov[f] += 1

    read_rows = []
    for doc in sorted(read, key=lambda k: (-homed.get(k, 0), k)):
        facts = file_facts(doc)
        read_rows.append({
            "document": doc, "waves": read[doc],
            "entries_homed_here": homed.get(doc, 0),
            "entries_whose_provenance_names_this_read": prov.get(doc, 0),
            "unresolved_clusters_now": unresolved.get(doc, 0),
            "lines": facts["lines"], "bytes": facts["bytes"],
            "banner_words": facts.get("banner_words", []),
            "named_in_ratified_surfaces": len(mentions.get(doc, [])),
        })

    owed_rows = []
    for doc in owed:
        facts = file_facts(doc)
        base = doc.split("/")[-1]
        named = []
        for s in RATIFIED_SURFACES:
            for i, line in enumerate(open(os.path.join(ROOT, s), encoding="utf-8",
                                          errors="replace").read().splitlines(), 1):
                if base in line:
                    named.append(f"{s}:{i}")
        owed_rows.append({
            "document": doc,
            "unresolved_clusters": unresolved.get(doc, 0),
            "lines": facts["lines"], "bytes": facts["bytes"],
            "est_tokens": round(facts["bytes"] / CHARS_PER_TOKEN),
            "banner_words": facts.get("banner_words", []),
            "named_in_ratified_surfaces": len(named),
            "named_where": named,
            "surface": "docs" if doc.startswith("docs/") else "cowork",
        })
    owed_rows.sort(key=lambda r: (-r["unresolved_clusters"], r["document"]))

    yields = [r["entries_homed_here"] for r in read_rows]
    yields_sorted = sorted(yields, reverse=True)
    total_y = sum(yields)
    top_n = 0
    acc = 0
    for y in yields_sorted:
        acc += y
        top_n += 1
        if total_y and acc >= 0.9 * total_y:
            break

    artifact = {
        "header": {
            "purpose": "phase-1m Tasks 5 and 6 — the KIND test measured and NOT applied, and "
                       "the reading yield measured with the owed partition ranked. Nothing "
                       "here changes any entry's home class or reorders any reading list.",
            "superseded": (
                "THE KIND TEST THIS TOOL MEASURES IS SUPERSEDED (user, 2026-08-03; register "
                "entry D-430, `CLAUDE.md` decisions-register rule (h)). The criterion's unit is "
                "now a SECTION of a document, not the document, which is what the kind test's "
                "own §6 structural finding pointed at. This tool is KEPT and kept CURRENT "
                "rather than frozen, for two reasons: its Task-6 partition is still the live "
                "read/owed derivation that `gen_phase1n_reading_regime.py` imports, and a "
                "generated artifact that no longer regenerates is the drift the project "
                "forbids. The consequence a reader must hold: from 2026-08-03 the task5 block "
                "re-runs a SUPERSEDED test against the CURRENT classes, so its `moves_in` and "
                "`moves_out` are no longer the pre-application figures the phase-1m report "
                "quotes — most visibly, `cowork_score_census.md`'s entries are now "
                "`contract-home` under the section criterion, so the kind test now reports "
                "them moving OUT. The pre-application measurement is preserved as the "
                "phase-1m dated note on `open_items/OI-281.md`; the section criterion's own "
                "measurement is the phase-1n note on the same row."),
            "generator": "tools/audit/decisions/gen_phase1m_measurements.py",
            "authored_inputs": ["KIND", "DELEGATION", "READ_WAVES"],
            "derived_from": ["backbone_decisions.json", "decision_clusters.json",
                             "cluster_dispositions.json", "gen_phase1g_triage.py",
                             "the three user-ratified surfaces", "the files themselves"],
            "read_wave_sources": {w: c for w, (_d, c) in READ_WAVES.items()},
        },
        "task5_kind_test": {
            "population_entries": len(population),
            "population_documents": len(per_doc),
            "current_classes": {
                "contract-home": sum(r["current_contract_home"] for r in kind_rows),
                "gap": sum(r["current_gap"] for r in kind_rows)},
            "verdict_totals": dict(tally),
            "entries_moving_in": sum(n for _d, n in moves["in"]),
            "entries_moving_out": sum(n for _d, n in moves["out"]),
            "entries_ambiguous": tally["AMBIGUOUS"],
            "moves_in": moves["in"], "moves_out": moves["out"],
            "ambiguous_documents": moves["ambiguous"],
            "rows": kind_rows,
        },
        "task6_reading_yield": {
            "design_document_surface": surface_files,
            "read_in_full": len(read),
            "user_accepted_exclusions_not_read": len(excluded),
            "owed_a_full_read": len(owed),
            "partition_check": len(read) + len(excluded) + len(owed) == surface_files,
            "yield_total_entries_homed_in_read_documents": total_y,
            "yield_max": max(yields) if yields else 0,
            "yield_min": min(yields) if yields else 0,
            "yield_zero_documents": sum(1 for y in yields if y == 0),
            "documents_carrying_90pct_of_yield": top_n,
            "owed_total_bytes": sum(r["bytes"] for r in owed_rows),
            "owed_est_tokens": sum(r["est_tokens"] for r in owed_rows),
            "owed_total_unresolved_clusters": sum(r["unresolved_clusters"] for r in owed_rows),
            "read_rows": read_rows,
            "owed_rows": owed_rows,
        },
    }

    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            print(f"STALE vs the data: {os.path.relpath(OUT, ROOT)}")
            return 1
        print("the phase-1m measurement artifact matches the data")
        return 0
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}: "
          f"task 5 — {len(population)} entries / {len(per_doc)} documents, "
          f"admit {tally['ADMIT']} exclude {tally['EXCLUDE']} ambiguous {tally['AMBIGUOUS']}; "
          f"task 6 — {len(read)} read, {len(excluded)} excluded, {len(owed)} owed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
