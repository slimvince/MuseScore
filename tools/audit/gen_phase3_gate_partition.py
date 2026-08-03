#!/usr/bin/env python3
"""Generate the phase-3 gate partition: which phase-2 items the family design waits on.

WHY THIS IS A GENERATED FILE (D-431): the partition is a PREDICTION about where surprises
live, and #3 says predictions of that shape are what this project is worst at. It is therefore
recorded before any classified item runs, with every load-bearing citation LOCATED IN THE FILE
IT CITES rather than transcribed, so a quote that has drifted is reported instead of read.

WHAT IS AUTHORED AND WHAT IS DERIVED — stated so the artifact is not mistaken for a measurement.
  AUTHORED: the per-item verdict and its reason (a judgment about a search space, made against
            the stated criterion), and the scope basis each verdict rests on.
  DERIVED : the item enumeration's SOURCE quotes (located in their files, with the line where
            each was found reported beside the line it was expected at), the totals, and the
            arithmetic of the check table.
The tool refuses to invent a verdict: an item with no verdict, or a verdict with no reason,
is a STOP, and an authored quote that cannot be located in its cited file is a STOP.

Usage:
  python tools/audit/gen_phase3_gate_partition.py            # write the artifact
  python tools/audit/gen_phase3_gate_partition.py --check    # re-derive and compare, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "tools" / "audit" / "phase3_gate_partition.json"

GATING = "GATING"
NON_GATING = "NON-GATING"

# --------------------------------------------------------------------------------------
# The ruling this artifact records, and the criterion it is measured under — both verbatim
# from the dispatch that carries them (cc_instruction_phase1o_gate_partition_and_probe_rerun.md).
# --------------------------------------------------------------------------------------
THE_RULING = (
    "The user has ruled that the family design waits only on the phase-2 channels that could "
    "plausibly find another member of the family named at F1. The rule this preserves is F3 "
    "(one fix designed once over the whole enumerated family); the gate's purpose is that the "
    "family be KNOWN before it is designed for, not that every unrelated measurement finish "
    "first. THE GATE IS NARROWED, NOT OPENED."
)

THE_CRITERION = (
    "For each channel: could this channel's search space contain a statement, measurement or "
    "code fact about (a) what the decoder or the emission READS - struck versus sounding tones, "
    "note counting, pitch representation - or (b) how candidates are ADMITTED?"
)

THE_DEFAULT = (
    "Where the channel's scope does not settle it, classify GATING - the default on doubt is to "
    "keep waiting."
)

# The family the gate exists to protect (F1 of the dispatch's premise ledger, read at the rows).
THE_FAMILY = [
    "OI-215", "OI-226", "OI-227", "OI-228", "OI-243", "OI-244", "OI-246", "OI-277",
]

# --------------------------------------------------------------------------------------
# The enumeration. Every item carries the source that PUTS IT IN PHASE 2, quoted, and the
# source is located in its file by the tool.
# --------------------------------------------------------------------------------------
RULE_SOURCE = {
    "file": "CLAUDE.md",
    # Re-aimed 2026-08-03 from the generator's own drift report (1002 -> 1026), per citation and
    # never by an assumed shift: this session's register-section insertion moved every line below
    # it in CLAUDE.md, and the same file also carries a second insertion with a different offset.
    "expected_line": 1026,
    "quote": "**Phase 2 - issue-finding is EXHAUSTED with measured coverage:** the remaining audit partitions",
    "what_it_is": (
        "The defining source for phase 2. The user-directed three-phase rule (register entry "
        "D-231), Conventions section, 2026-08-02. Its phase-2 clause names, in order: the "
        "remaining audit partitions; the blind second pass with its seeded error rate; the "
        "enumerated discovery channels (populations, oracles, invariants, residual "
        "decomposition, concept gaps, requirement side); the per-search detection-power "
        "report; and the bounded trust statement."
    ),
}

CHANNEL_ENUMERATION_SOURCE = {
    "file": "cowork_oi200_perspective_inventory.md",
    "expected_line": 104,
    "quote": "## §4 The perspective inventory - the channels, each with its principle, precedent, and proposed probes",
    "what_it_is": (
        "The only place in the record where 'the enumerated discovery channels' the rule names "
        "are actually enumerated: ten channels, §4, each with its principle, precedent and "
        "proposed probes; the sequenced program is §6."
    ),
    "status_of_this_source": {
        "banner_expected_line": 3,
        "banner_quote": "> **STATUS: DRAFT for discussion (Cowork, 2026-08-01).** Prepared at the user's direction while the",
        "consequence": (
            "REPORTED, NOT WORKED AROUND. The rule D-231 states is user-directed and binding; the "
            "enumeration it points at is an unratified Cowork draft whose own §9 says its one "
            "requested decision - adopt, amend or reject the §6 program - has not been taken. So "
            "the six channel subjects the rule names ARE binding, and the ten-channel structure "
            "this partition classifies against is a draft. Every verdict below is therefore stated "
            "against the SUBJECT the rule names, with the draft's channel number as a locator only."
        ),
    },
}

ITEMS = [
    # ---------------------------------------------------------------- audit partitions
    {
        "id": "P2-A2",
        "name": "OI-199 audit partition 2 - the new instruments (the measurement tools)",
        "kind": "audit partition",
        "named_by_the_rule": True,
        "rule_phrase": "the remaining audit partitions",
        "source": {
            "file": "open_items/OI-199.md",
            "expected_line": 17,
            "quote": "ordering rules: **1 = the joint module (DONE this session), 2 = the new instruments (Cowork's amendment -",
        },
        "scope_basis": (
            "The deep-row inventory puts ~4,479 of the 6,375 rows in this area: the measurement "
            "tools under tools/. That population INCLUDES the pure-Python reference decoder and "
            "the table generators."
        ),
        "verdict": GATING,
        "reason": (
            "Not a doubt call - demonstrated. Three of the eight family rows locate their "
            "mechanism inside this partition's own population: OI-243 at probe_decoder.py:743 "
            "(the canonical per-tonic spelling anchor), OI-244 at probe_decoder.py:1039-1052 (the "
            "absolute-tonic-pc prune tie-break), and OI-277 at gen_note_tables.py:385-410 (the "
            "fitted table counted per note record). A search space that has already produced "
            "family members can produce another."
        ),
        "family_rows_this_item_has_already_produced": ["OI-243", "OI-244", "OI-277"],
    },
    {
        "id": "P2-A3",
        "name": "OI-199 audit partition 3 - the record path and the seams",
        "kind": "audit partition",
        "named_by_the_rule": True,
        "rule_phrase": "the remaining audit partitions",
        "source": {
            "file": "open_items/OI-199.md",
            "expected_line": 18,
            "quote": "every steering figure came from them, #19; needs a 2-3-way sub-split), 3 = the record path/seams.**",
        },
        "scope_basis": (
            "818 deep rows over the record path and the four record-arm seams - the code that "
            "decides what SCORE INPUT reaches the record producer and what the produced record "
            "becomes."
        ),
        "verdict": GATING,
        "reason": (
            "The seams own the input-scoping half of 'what the model reads': OI-212 records that "
            "produceNotationRecord takes no tick range and every seam analyzes the whole score, "
            "and OI-247 records the signature prior read from staff 0 at tick 0 with no "
            "excludeStaves or eligibility check. Both are statements about what the decoder is "
            "fed. Under the stated default this would be GATING on doubt alone; it does not need "
            "the default."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    # ---------------------------------------------------------------- the blind second pass
    {
        "id": "P2-P2",
        "name": "OI-199 pass 2 - the blind second reading with its seeded error rate",
        "kind": "blind pass",
        "named_by_the_rule": True,
        "rule_phrase": "the blind second pass with its seeded error rate",
        "source": {
            "file": "open_items/OI-199.md",
            "expected_line": 24,
            "quote": "COMPROMISED at the source - OI-222 (DT-20): `STATUS.md` (a mandatory read) + the inline §S both leaked",
        },
        "scope_basis": (
            "A fresh-session blind second reading of the whole audited scope at full vocabulary, "
            "plus the whole-scope defect-signature sweep. The scope includes the joint module, "
            "where the emission and the admission gates live."
        ),
        "verdict": GATING,
        "reason": (
            "Not a doubt call - demonstrated. The pass-2 work already run produced three of the "
            "eight family rows: OI-226 (candidate admission entered production with no ratified "
            "basis), OI-227 (the FIT-gate sibling of the empty-decode cliff) and OI-228 (the "
            "emission reads struck, not sounding, tones). The remaining pass-2 scope is the same "
            "search space."
        ),
        "family_rows_this_item_has_already_produced": ["OI-226", "OI-227", "OI-228"],
    },
    # ---------------------------------------------------------------- the six named channels
    {
        "id": "P2-C1",
        "name": "Populations - vary the input (perspective inventory channel 1)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "populations",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 113,
            "quote": "### Channel 1 - Population variation (vary the INPUT)",
        },
        "scope_basis": (
            "Music fed to the system from outside every envelope it was shaped on: the OI-38 "
            "repertoire expansion, the notation-feature census, and synthetic extreme textures."
        ),
        "verdict": GATING,
        "reason": (
            "Not a doubt call - the channel's own recorded precedent is the admission family "
            "itself: the orchestral set is what made OI-215 and OI-227 visible, and both are (b) "
            "admission facts. Its proposed probes reach (a) directly too - sustained and doubled "
            "textures are exactly where struck-versus-sounding and note-count weighting differ."
        ),
        "family_rows_this_item_has_already_produced": ["OI-215", "OI-227"],
    },
    {
        "id": "P2-C2",
        "name": "Oracles - vary the reference (perspective inventory channel 2)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "oracles",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 129,
            "quote": "### Channel 2 - Oracle multiplication (vary the REFERENCE)",
        },
        "scope_basis": (
            "An independent second derivation of the same quantity: published harmonic-analysis "
            "systems on our corpora, a second implementation or theory re-derivation of each of "
            "our own published derived facts, and the ground-truth ceiling (OI-179) as the "
            "oracle of the oracle."
        ),
        "verdict": GATING,
        "reason": (
            "A second derivation of a published derived fact is exactly the shape that names an "
            "input-representation difference: two implementations that agree on the model and "
            "disagree on the answer differ in what they read. The C++/Python decode parity "
            "establishment is this channel already run over the decode, and the family's "
            "questions (per-note versus per-pitch-class weighting, struck versus sounding "
            "membership) are the kind a parity disagreement localizes."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-C3",
        "name": "Invariants - vary the question (perspective inventory channel 3)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "invariants",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 142,
            "quote": "### Channel 3 - Invariant and metamorphic checks (vary the QUESTION)",
        },
        "scope_basis": (
            "Theory-derived relations checked mechanically over whole corpora: transposition, "
            "octave doubling, uniform time-stretching, part order, and the no-information-loss "
            "property."
        ),
        "verdict": GATING,
        "reason": (
            "Not a doubt call - demonstrated twice. OI-243 and OI-244 are this channel's "
            "transposition probe; OI-277 is its octave-doubling probe. Three of the eight family "
            "rows, and two of its five proposed relations are unrun."
        ),
        "family_rows_this_item_has_already_produced": ["OI-243", "OI-244", "OI-277"],
    },
    {
        "id": "P2-C5",
        "name": "Residual decomposition - vary the grain (perspective inventory channel 5)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "residual decomposition",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 170,
            "quote": "### Channel 5 - Residual decomposition (vary the GRAIN of attention)",
        },
        "scope_basis": (
            "One systematic pass clustering the current robust-unit failing runs by texture, "
            "position and mechanism until every mass either cites a row or gets one. Gated on "
            "the ground-truth ceiling (OI-179)."
        ),
        "verdict": GATING,
        "reason": (
            "Clustering the failing mass BY TEXTURE is the one decomposition whose output "
            "classes are input-representation classes: a mass concentrated at sustained or "
            "doubled writing is the struck-versus-sounding and note-count signatures arriving "
            "from the residual side. The channel's own precedent, the fifth-substitution family "
            "OI-192, was named this way."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-C6",
        "name": "Concept gaps - vary the conceptual frame (perspective inventory channel 6)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "concept gaps",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 183,
            "quote": "### Channel 6 - Public-research comparison (vary the CONCEPTUAL FRAME)",
        },
        "scope_basis": (
            "The concept inventories of the published lines - voice-leading models, meter and "
            "hypermeter, phrase and cadence schemata, function beside scale-degree theory, "
            "neo-Riemannian models, expectation models - each recorded as modeled by us, "
            "excluded with a ruling, or absent with no ruling."
        ),
        "verdict": GATING,
        "reason": (
            "The channel's scope does not settle it, so the stated default applies - AND there "
            "is a positive path, so the default is not doing the work alone: the published lines "
            "differ from us precisely in what they take as input (pitch-class profiles versus "
            "note-level events, duration-weighted versus onset-weighted membership) and in what "
            "chord vocabularies they admit, so a concept-inventory comparison can produce both "
            "an (a) and a (b) fact."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-C7",
        "name": "Requirement side - vary the direction (perspective inventory channel 7)",
        "kind": "discovery channel",
        "named_by_the_rule": True,
        "rule_phrase": "requirement side",
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 199,
            "quote": "### Channel 7 - Requirement-side enumeration (vary the DIRECTION - outside-in)",
        },
        "scope_basis": (
            "Each user-visible task enumerated inward to the mechanism that serves it, and "
            "whether that mechanism is established on the population the task implies."
        ),
        "verdict": GATING,
        "reason": (
            "A task implies a population, and a population is what makes an input-representation "
            "defect visible: 'analyze a symphony' is what put OI-209 on the record and OI-209 is "
            "why the chorale-shaped envelope became a stated problem. The channel also reaches "
            "the input-scoping half directly - which span and which staves a task should have "
            "the analyzer read is the OI-212/OI-247 question asked from the requirement side."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    # ------------------------------- the inventory's other four channels, not named by the rule
    {
        "id": "P2-C4",
        "name": "Prediction-first operation (perspective inventory channel 4)",
        "kind": "standing obligation",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 161,
            "quote": "### Channel 4 - Prediction-first operation (vary the EXPECTATION)",
        },
        "scope_basis": (
            "The inventory states 'Proposed probe: none new - the channel is already mandated' "
            "(#17b): it is an obligation carried BY the other probes, not a search of its own."
        ),
        "verdict": NON_GATING,
        "reason": (
            "It generates no observation. A rule that every other probe writes its bands first "
            "cannot itself contain a statement about what the decoder reads; whatever it "
            "contributes to the family arrives through whichever probe carries it, and those are "
            "classified on their own lines above. Narrowing here removes nothing from the wait."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-C8",
        "name": "Fresh-reader passes with measured power (perspective inventory channel 8)",
        "kind": "discovery channel",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 212,
            "quote": "### Channel 8 - Fresh-reader passes with measured power (vary the OBSERVER)",
        },
        "scope_basis": (
            "The inventory says of this channel 'already scheduled - OI-199 pass 2 and "
            "partitions 2-3 run exactly this'. It is the same work as P2-P2, P2-A2 and P2-A3, "
            "which the rule names separately."
        ),
        "verdict": GATING,
        "reason": (
            "GATING because it IS items P2-P2/P2-A2/P2-A3 under the inventory's name for them, "
            "and those are gating. It is listed so the enumeration is complete and so no reader "
            "concludes a channel was dropped; it adds no wait of its own."
        ),
        "family_rows_this_item_has_already_produced": ["OI-226", "OI-227", "OI-228"],
        "duplicate_of": ["P2-P2", "P2-A2", "P2-A3"],
    },
    {
        "id": "P2-C9",
        "name": "History mining (perspective inventory channel 9)",
        "kind": "discovery channel",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 225,
            "quote": "### Channel 9 - History mining (vary the TIME of observation)",
        },
        "scope_basis": (
            "Re-reading old rulings, shelvings, falsifications and dead ends against the current "
            "tree. The inventory calls the OI-207 adjudication this channel run to completion; "
            "OI-207's own row says the pass is NOT exhaustive and a second pass over the "
            "unresolved residual is owed."
        ),
        "verdict": GATING,
        "reason": (
            "Demonstrated: OI-275 - the SIGNED Layer-4 specification's complete-candidate-listing "
            "decision standing against the production decoder's admission - is this channel's "
            "product and is a (b) fact about admission; the user's ruling on it made D-329 the "
            "family design's ratified admission premise. The residual second pass is the same "
            "search space."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-C10",
        "name": "Defect-signature sweeps (perspective inventory channel 10)",
        "kind": "discovery channel",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "cowork_oi200_perspective_inventory.md",
            "expected_line": 234,
            "quote": "### Channel 10 - Defect-signature sweeps (the honest limit, stated)",
        },
        "scope_basis": (
            "Sweeps for instances of the DEFECT_TYPES.md catalog's already-named classes. The "
            "inventory states in terms that they cannot find a class nobody has named."
        ),
        "verdict": GATING,
        "reason": (
            "The stated default, applied honestly. The channel cannot find a new CLASS, but the "
            "family's classes are already named, so a sweep for them can find another INSTANCE - "
            "another site that reads struck where the design says sounding, another admission "
            "gate with no basis. That is a family member, and the criterion asks about members, "
            "not classes."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    # ---------------------------------------------------------------- the rest of phase 2
    {
        "id": "P2-TRUST",
        "name": "The per-search detection-power reports and the bounded trust statement",
        "kind": "accounting act",
        "named_by_the_rule": True,
        "rule_phrase": "each search reporting its detection power, ending in the bounded trust statement",
        "source": {
            "file": "CLAUDE.md",
            "expected_line": 1029,   # re-aimed 2026-08-03 from the drift report (1005 -> 1029)
            "quote": "each search reporting its detection power, ending in the bounded trust statement - every",
        },
        "scope_basis": (
            "An accounting act OVER the channels: each search's miss rate, each declared "
            "envelope, and the statement that bounds what the whole program can claim."
        ),
        "verdict": NON_GATING,
        "reason": (
            "It examines the searches, not the system. Nothing it can produce is a statement, "
            "measurement or code fact about what the decoder reads or how candidates are "
            "admitted - it reports how much the searches that DO look at those things may have "
            "missed. This is the one item where the narrowing bites: the family design need not "
            "wait for phase 2's trust statement to be WRITTEN, only for the gating searches to "
            "have RUN. What it still governs is unchanged - the completeness claim phase 2 ends "
            "with is not made until it exists."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-OI288a",
        "name": "OI-288 half (a) - the P4 fallback fire rate within the legacy arm",
        "kind": "measurement owed",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "open_items/OI-288.md",
            "expected_line": 104,
            "quote": "**Half (a) - the fire rate within the legacy arm, on real repertoire - is unchanged and unscheduled",
        },
        "scope_basis": (
            "How often the legacy P4 tick-local fallback fires GIVEN the legacy arm ran, on the "
            "23 committed large scores. The row's own note settles the scope: the control-flow "
            "half is answered on both production surfaces, so the measurement bounds how much "
            "behaviour rides on a path scheduled for deletion 'and nothing more'."
        ),
        "verdict": NON_GATING,
        "reason": (
            "Not the default's doubt case - the row's scope IS settled, by its own text. The "
            "subject is the LEGACY chord path, which is not the joint decoder and does not read "
            "the joint emission; its fire rate cannot be a statement about what the joint "
            "decoder reads or how the joint decoder admits candidates. It bounds a deletion "
            "risk, which is a different question."
        ),
        "family_rows_this_item_has_already_produced": [],
    },
    {
        "id": "P2-OI283",
        "name": "OI-283 - the decisions register's own coverage claim (a #17f/#19 obligation)",
        "kind": "establishment obligation",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "OPEN_ITEMS.md",
            "expected_line": 312,
            "quote": "| OI-283 | The decisions register's coverage claim states a stale `ARCHITECTURE.md` line count, and nothing keeps it current |",
        },
        "scope_basis": (
            "What the register claims to have read, and whether the claim is current. The claim "
            "bounds which parts of the canonical document any decision-conformance finding can "
            "have come from."
        ),
        "verdict": GATING,
        "reason": (
            "Two independent grounds, and the exemption below does not need either. On the "
            "criterion: an unread range of the canonical document can hold a decision about the "
            "input surface, so the coverage claim is a bound on where an (a) or (b) fact could "
            "still be hiding, and the scope does not settle that - the default applies. On the "
            "exemption: it is a #19 establishment obligation, and those always gate."
        ),
        "family_rows_this_item_has_already_produced": [],
        "exempt_as_establishment_obligation": True,
    },
    {
        "id": "P2-OI289",
        "name": "OI-289 - the LEGACY-marked register entries, swept and never verified (a #19 obligation)",
        "kind": "establishment obligation",
        "named_by_the_rule": False,
        "rule_phrase": None,
        "source": {
            "file": "OPEN_ITEMS.md",
            "expected_line": 318,
            "quote": "| OI-289 | The 80 LEGACY-marked register entries were SWEPT, never verified - and two of them were wrong |",
        },
        "scope_basis": (
            "Every LEGACY-marked register entry re-verified against a live-reachability test. "
            "The set size is re-derived from the data, never quoted from the record."
        ),
        "verdict": GATING,
        "reason": (
            "Two independent grounds, as with OI-283. On the criterion: D-329 - complete "
            "candidate listing, the family design's ratified admission premise - is itself a "
            "marked entry whose marking already failed once, so this verification's search space "
            "demonstrably contains (b) admission facts. On the exemption: it is a #19 "
            "establishment obligation, and those always gate."
        ),
        "family_rows_this_item_has_already_produced": [],
        "exempt_as_establishment_obligation": True,
    },
]

# --------------------------------------------------------------------------------------
# Assumption A1 of the dispatch's premise ledger, and what the enumeration above returns.
# --------------------------------------------------------------------------------------
A1 = {
    "as_stated_in_the_dispatch": (
        "That phase 2's channel program is the measurement-tools partition of OI-199, the "
        "record-seams partition, OI-199 pass 2, the remaining perspective-inventory channels, "
        "and OI-179."
    ),
    "its_declared_source": "a session handoff block, which is a secondary surface",
    "verdict": "DIFFERS - reported, not reconciled",
    "differences": [
        {
            "kind": "scope of the channel half",
            "finding": (
                "A1 says 'the remaining perspective-inventory channels'. The rule does not say "
                "that: it names SIX subjects - populations, oracles, invariants, residual "
                "decomposition, concept gaps, requirement side - and the inventory has TEN "
                "channels. The four the rule does not name are 4, 8, 9 and 10, which the "
                "inventory's own §6 says 'are already standing law or already scheduled'. Two of "
                "the four turn out to matter: channel 8 IS the audit passes the rule names "
                "separately, and channel 9 (history mining) is the OI-207 residual second pass, "
                "which is gating on this partition's own criterion and which 'the remaining "
                "perspective-inventory channels' would have swept in without saying so."
            ),
        },
        {
            "kind": "OI-179's position",
            "finding": (
                "A1 lists OI-179 (the ground-truth ceiling) as an item of the program beside the "
                "channels. The record does not put it there: the rule's parenthetical does not "
                "name it, and the inventory locates it INSIDE two channels - as probe (c) of "
                "channel 2 ('the oracle-of-the-oracle and is already rowed') and as the gate on "
                "channel 5 ('gated on the ground-truth ceiling (OI-179), which should therefore "
                "be scheduled before or with it'). It is not classified separately here, because "
                "classifying a probe separately from the channel that contains it would let the "
                "two answer differently."
            ),
        },
        {
            "kind": "items A1 does not mention",
            "finding": (
                "A1 names no non-channel item. The record puts three more in phase 2: the "
                "per-search detection-power reports and the bounded trust statement (the rule's "
                "own closing clause), OI-288 half (a) ('It enters phase 2's program as before'), "
                "and - by the dispatch's own §3.2 - OI-283 and OI-289. Two of those five are the "
                "only NON-GATING verdicts in this partition, so an enumeration that omitted them "
                "would have produced a partition that narrows nothing."
            ),
        },
        {
            "kind": "the enumeration's source is a draft",
            "finding": (
                "The rule that binds is user-directed; the enumeration it points at is an "
                "unratified Cowork draft (STATUS: DRAFT for discussion, 2026-08-01) whose own §9 "
                "records that its one requested decision has not been taken. Nothing here depends "
                "on the draft's authority - each verdict is stated against the SUBJECT the rule "
                "names - but a reader must not take the ten-channel structure for a ratified "
                "program."
            ),
        },
    ],
}


# --------------------------------------------------------------------------------------
# The SECOND assumption about the channel enumeration, declared by the phase-1u dispatch and
# checked at the inventory document itself (not at the session report it came from). Recorded
# here beside A1 because it is the same premise, narrowed, and a reader comparing the two must
# not have to reconstruct which wave said what.
# --------------------------------------------------------------------------------------
A1_PHASE1U = {
    "as_stated_in_the_dispatch": (
        "That the inventory holds TEN channels, and that of the four the rule's phase-2 clause "
        "omits, the fresh-reader channel and history mining are the two that matter - the latter "
        "being the OI-207 residual second pass, which gates."
    ),
    "its_declared_source": (
        "a session report (the phase-1o report), which is a secondary surface; the dispatch "
        "labelled it an ASSUMPTION for exactly that reason and ordered it checked at the "
        "document before anything rested on it."
    ),
    "how_it_was_checked": (
        "cowork_oi200_perspective_inventory.md read in full, and the rule's own clause read at "
        "CLAUDE.md. Both are primary sources for what they respectively state."
    ),
    "verdict": "PARTLY CONFIRMED, PARTLY DIFFERENT - reported, not reconciled",
    "findings": [
        {
            "kind": "the channel count",
            "verdict": "CONFIRMED",
            "finding": (
                "The inventory's section 4 enumerates ten channels, headed 'Channel 1' through "
                "'Channel 10'. The rule's clause names six subjects, which map onto channels 1, "
                "2, 3, 5, 6 and 7; the four it does not name are 4, 8, 9 and 10. Both halves of "
                "the arithmetic hold at the documents."
            ),
        },
        {
            "kind": "which omissions matter",
            "verdict": "DIFFERENT",
            "finding": (
                "'The fresh-reader channel and history mining are the two that matter' is not "
                "what the document supports, because it merges two different senses of matter. "
                "On the sense that decides anything - does the omission add a GATING wait the "
                "rule's six subjects would not otherwise have named? - the answer is channel 9 "
                "AND channel 10, not 8 and 9: channel 10 (defect-signature sweeps) is a distinct "
                "search the rule names nowhere and is GATING on this partition's own verdict. "
                "Channel 8 matters in the other sense: it is a distinct search, but it IS the "
                "audit passes the rule names separately, so counting it as an additional wait "
                "would double-count work already enumerated - which is why this partition "
                "carries it with an explicit duplicate_of. Channel 4 is not a distinct search at "
                "all; the inventory says of it 'Proposed probe: none new - the channel is already "
                "mandated'. Under either sense taken alone, the phrase names the wrong pair."
            ),
        },
        {
            "kind": "the inventory's own claim about channel 9 is stale at HEAD",
            "verdict": "DIFFERENT - and this one is a statement of fact in the draft, not a "
                       "reading of it",
            "finding": (
                "The inventory says of history mining: 'Proposed probe: none new - the "
                "adjudication is this channel run to completion.' The OI-207 adjudication is not "
                "run to completion at HEAD. Its residual second pass RAN on 2026-08-02, and work "
                "continues on both of its faces: the unresolved cluster residual is a live figure "
                "(tools/audit/decisions/disposition_manifest.json -> "
                "disposition_counts.unresolved) and the owed full document reads are tracked on "
                "the row itself. So the dispatch's gloss - 'history mining, being the OI-207 "
                "residual second pass' - is also imprecise in the other direction: what remains "
                "of this channel is the CONTINUING residual and reading work, not an unrun second "
                "pass. The verdict GATING is unaffected either way; what is corrected is the "
                "description of why."
            ),
        },
    ],
    "what_this_does_not_change": (
        "No verdict in this partition moves. A1 of phase 1u was a premise about the ENUMERATION, "
        "and the enumeration each verdict is stated against is the SUBJECT the rule names, with "
        "the draft's channel number used as a locator only - which is the property that makes "
        "the partition survive a correction to the draft."
    ),
}


# --------------------------------------------------------------------------------------
# WHAT THE PARTITION MEASURED — recorded 2026-08-03 when the user ACCEPTED the verdicts
# (eleventh ruling set, AA1: "accept, and record that the ruling's measured effect was
# small"). The verdicts above are unchanged; this block is the accounting the acceptance
# ordered, and the counts in it are DERIVED from the items rather than authored.
# --------------------------------------------------------------------------------------
THE_ACCEPTANCE = (
    "The per-item verdicts above are ACCEPTED as generated (user, 2026-08-03). Nothing in "
    "the partition was re-argued or re-classified at the acceptance; what the acceptance "
    "added is the record below of what the partition's effect actually was, because a "
    "narrowing ruling whose measured effect is small must say so where the ruling is read."
)

# Cowork's planning claim for this option, quoted from the decision surface that carried it
# (cc_instruction_phase1u_partition_record_and_directory.md §2). The quote is preserved HERE
# because .gitignore excludes /cc_instruction_*.md as a class, so the surface that made the
# claim is not itself in the record (#12 -- the claim survives its source).
THE_REFUTED_PLANNING_PREDICTION = {
    "the_claim_verbatim": (
        "removes the largest share of the blocking for the smallest loss of rigor"
    ),
    "who_made_it_and_where": (
        "Cowork, on the decision surface that put this option to the user "
        "(cc_instruction_phase1u_partition_record_and_directory.md, section 2). Not a user "
        "statement: the ruling is the user's, the prediction that recommended it is Cowork's."
    ),
    "verdict": "REFUTED",
    "what_actually_happened": (
        "The loss of rigor is indeed small - that half holds. The blocking removed is NOT the "
        "largest share and is not a large share: the counts below show the great majority of "
        "items GATING, most of them on demonstrated grounds rather than on the doubt default, "
        "and the narrowing reaches exactly one item that any search would have had to run "
        "anyway. A reader arriving at this ruling later must meet the result, not inherit the "
        "expectation that sold it."
    ),
    "why_this_is_recorded_and_not_quietly_dropped": (
        "CLAUDE.md #17(b) applied to a PLANNING claim: a written quantitative expectation that "
        "misses its band is the finding, and the same rule that forbids smoothing a measurement "
        "result forbids smoothing the prediction that justified the measurement. The RULING "
        "stands - it was ruled by the user on its own terms and is not disturbed by its "
        "advocate's forecast being wrong."
    ),
}

# What the narrowing actually buys, stated once in plain words. The item it names is derived
# below by verdict, never transcribed.
WHERE_THE_NARROWING_BITES = (
    "The family design need not wait for phase 2's bounded trust statement to be WRITTEN, "
    "only for the gating searches to have RUN. That is the whole of the practical effect. "
    "What the trust statement still governs is unchanged: the completeness claim phase 2 "
    "ends with is not made until it exists."
)


def _default_sentences(reason: str):
    """Return the sentences of an authored reason that speak about the doubt default, so the
    classification below can be CHECKED against the words rather than trusted."""
    out = []
    for sent in re.split(r"(?<=[.;])\s+", reason):
        if re.search(r"\bdefault\b", sent, re.I):
            out.append(sent.strip())
    return out


def measured_effect(items):
    """Derive what the partition measured. Every figure here is computed from the items."""
    gating = [i for i in items if i["verdict"] == GATING]
    non_gating = [i for i in items if i["verdict"] == NON_GATING]

    # STRUCTURAL, not a reading of prose: an item's search space HAS ALREADY produced a member
    # of the family. This is the strongest form the criterion can be satisfied in.
    produced = {i["id"]: i["family_rows_this_item_has_already_produced"]
                for i in items if i.get("family_rows_this_item_has_already_produced")}
    covered = sorted({r for rows in produced.values() for r in rows})
    demonstrated = [i for i in gating if i["id"] in produced]
    # An item marked duplicate_of adds no wait of its own; counting it as a distinct producing
    # search would overstate how many independent spaces have drawn blood.
    demonstrated_distinct = [i for i in demonstrated if not i.get("duplicate_of")]

    establishment = [i for i in gating if i.get("exempt_as_establishment_obligation")]

    # The doubt default: the sentences that speak about it, carried verbatim and NOT scored.
    # See how_the_doubt_default_was_counted below for why there is no count here.
    default_use = [{"id": i["id"], "sentences": _default_sentences(i["reason"])}
                   for i in gating if _default_sentences(i["reason"])]

    return {
        "the_acceptance": THE_ACCEPTANCE,
        "headline": (
            "MOST ITEMS GATE, AND THE NARROWING BITES IN ONE PLACE. The ruling is a real "
            "narrowing and a small one."
        ),
        "counts": {
            "items": len(items),
            "gating": len(gating),
            "non_gating": len(non_gating),
            "gating_whose_space_has_already_produced_a_family_row": len(demonstrated),
            "gating_whose_space_has_already_produced_a_family_row_ids": [i["id"] for i in demonstrated],
            "of_those_independent_searches_not_duplicates": len(demonstrated_distinct),
            "of_those_independent_searches_not_duplicates_ids": [i["id"] for i in demonstrated_distinct],
            "gating_as_establishment_obligations": len(establishment),
            "gating_as_establishment_obligations_ids": [i["id"] for i in establishment],
            "gating_items_whose_reason_discusses_the_doubt_default": len(default_use),
            "gating_items_whose_reason_discusses_the_doubt_default_ids": [d["id"] for d in default_use],
        },
        "how_the_doubt_default_was_counted": {
            "the_answer": "IT IS NOT COUNTED, DELIBERATELY.",
            "why": (
                "Whether an item gates BECAUSE of the doubt default or gates anyway and merely "
                "mentions it is a judgment about authored prose, and two attempts to decide it "
                "mechanically inside this tool both got it wrong: a substring test read P2-A3 as "
                "resting on the default when its reason says in terms that 'it does not need the "
                "default', and a phrase list then read P2-C6 as disclaiming the default when its "
                "reason says the default applies AND a positive path exists beside it. A text "
                "test standing in for that judgment is a structural proxy for a behavioural "
                "quantity, unvalidated - the substitution CLAUDE.md #17(d) forbids, and the same "
                "substitution register entry D-436 was ruled to withdraw elsewhere. So the "
                "sentences are carried verbatim and the reader judges."
            ),
            "what_is_safe_to_say": (
                "The structural counts above are safe because they read fields, not prose: an "
                "item's search space either has already produced a family row or it has not, and "
                "an item either carries the establishment-obligation flag or it does not."
            ),
            "the_sentences_that_discuss_the_default": default_use,
        },
        "what_demonstrated_means_here": (
            "Not that the item is judged likely to yield another family member, but that its "
            "search space HAS ALREADY yielded one. That is the strongest form the criterion "
            "can be satisfied in, and it is why most of the wait is not a doubt call."
        ),
        "family_rows_already_produced_by_item": produced,
        "family_rows_of_the_eight_already_traced_to_an_item": covered,
        "family_rows_of_the_eight_not_yet_traced_to_any_item": sorted(
            set(THE_FAMILY) - set(covered)),
        "where_the_narrowing_bites": WHERE_THE_NARROWING_BITES,
        "the_refuted_planning_prediction": THE_REFUTED_PLANNING_PREDICTION,
        "what_this_does_NOT_change": (
            "No fix, no design and no inference change is authorized by the acceptance, and "
            "phase 1 is not complete. The gate is narrowed, not opened - the same statement "
            "the ruling itself carries."
        ),
    }


def _norm(s: str) -> str:
    """Normalize for location: collapse whitespace, and fold the dash and quote characters the
    record uses into ASCII so an authored quote need not carry them byte-exactly."""
    s = s.replace("—", "-").replace("–", "-").replace("‑", "-")
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("→", "->").replace("≥", ">=").replace("≤", "<=")
    s = s.replace("★", "*").replace("⭐", "*")
    return re.sub(r"\s+", " ", s).strip()


def locate(rel_path: str, quote: str, expected_line: int | None):
    """Locate a quote in a repository file. Returns the verification record. A quote that
    cannot be located is a STOP; a quote located at a different line is reported as drift."""
    p = ROOT / rel_path
    if not p.exists():
        return {"file": rel_path, "found": False, "why": "file does not exist"}
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    want = _norm(quote)
    hits = [i + 1 for i, ln in enumerate(lines) if want in _norm(ln)]
    rec = {
        "file": rel_path,
        "quote": quote,
        "expected_line": expected_line,
        "found_lines": hits,
        "found": bool(hits),
    }
    if hits and expected_line is not None:
        rec["anchor_ok"] = expected_line in hits
        if not rec["anchor_ok"]:
            rec["drift"] = {"expected": expected_line, "actual": hits}
    return rec


def build():
    verifications = []

    def _v(rec):
        verifications.append(rec)
        return rec

    _v(locate(RULE_SOURCE["file"], RULE_SOURCE["quote"], RULE_SOURCE["expected_line"]))
    _v(locate(CHANNEL_ENUMERATION_SOURCE["file"], CHANNEL_ENUMERATION_SOURCE["quote"],
              CHANNEL_ENUMERATION_SOURCE["expected_line"]))
    st = CHANNEL_ENUMERATION_SOURCE["status_of_this_source"]
    _v(locate(CHANNEL_ENUMERATION_SOURCE["file"], st["banner_quote"], st["banner_expected_line"]))

    items = []
    for it in ITEMS:
        if it["verdict"] not in (GATING, NON_GATING):
            raise SystemExit(f"STOP: {it['id']} carries no verdict")
        if not it.get("reason"):
            raise SystemExit(f"STOP: {it['id']} carries a verdict with no reason")
        rec = _v(locate(it["source"]["file"], it["source"]["quote"],
                        it["source"].get("expected_line")))
        out = dict(it)
        out["source_verification"] = rec
        # The check the ruling requires: filled in as each item RUNS, never at authoring time.
        out["the_check"] = {
            "has_run": False,
            "produced_a_family_member": None,
            "recorded_by": None,
            "note": (
                "Filled in when this item runs. A NON-GATING item that yields a family member "
                "is a #13 STOP: the partition was wrong and the gate widens."
            ),
        }
        items.append(out)

    unlocated = [v for v in verifications if not v.get("found")]
    drifted = [v for v in verifications if v.get("found") and v.get("anchor_ok") is False]

    gating = [i["id"] for i in items if i["verdict"] == GATING]
    non_gating = [i["id"] for i in items if i["verdict"] == NON_GATING]

    return {
        "purpose": (
            "The phase-3 gate partition: which items of phase 2 the struck-versus-sounding "
            "family design waits on, and which it does not. NARROWING THE GATE DOES NOT OPEN "
            "IT - this artifact authorizes no fix, no design and no inference change."
        ),
        "generated_by": "tools/audit/gen_phase3_gate_partition.py",
        "generated_for": "cc_instruction_phase1o_gate_partition_and_probe_rerun.md, Tasks 1-2",
        "the_ruling": THE_RULING,
        "the_criterion": THE_CRITERION,
        "the_default_on_doubt": THE_DEFAULT,
        "the_family_the_gate_protects": THE_FAMILY,
        "what_is_authored_and_what_is_derived": {
            "authored": "the per-item verdict, its reason, and the scope basis it rests on",
            "derived": (
                "every source quote's location in the file it cites (with the line where it was "
                "found beside the line it was expected at), the totals, and the check table's "
                "arithmetic"
            ),
            "why_it_matters": (
                "This is a PREDICTION about where surprises live, not a measurement. Recording "
                "it before the classified items run is what makes it falsifiable."
            ),
        },
        "the_enumeration_source": RULE_SOURCE,
        "the_channel_enumeration_source": CHANNEL_ENUMERATION_SOURCE,
        "items": items,
        "totals": {
            "items": len(items),
            "gating": len(gating),
            "non_gating": len(non_gating),
            "gating_ids": gating,
            "non_gating_ids": non_gating,
            "named_by_the_rule": sum(1 for i in items if i["named_by_the_rule"]),
            "establishment_obligations_exempt": [
                i["id"] for i in items if i.get("exempt_as_establishment_obligation")
            ],
        },
        "the_stop": (
            "A NON-GATING item that yields a family member is a #13 STOP. It means the "
            "partition was wrong; the gate widens to include that item, the family enumeration "
            "is re-opened, and any family design already begun stops until it is closed again."
        ),
        "the_check": (
            "As each item runs, its `the_check` block records whether it produced a family "
            "member. The partition is falsified by a NON-GATING item scoring true; it is "
            "corroborated, never proven, by GATING items scoring either way."
        ),
        "what_the_partition_measured": measured_effect(items),
        "assumption_A1_of_the_dispatch": A1,
        "assumption_A1_of_the_phase1u_dispatch": A1_PHASE1U,
        "quote_verification": {
            "checked": len(verifications),
            "located": len(verifications) - len(unlocated),
            "unlocated": unlocated,
            "anchor_drift": drifted,
            "records": verifications,
        },
    }


def main(argv):
    doc = build()
    if doc["quote_verification"]["unlocated"]:
        print("STOP: some authored quotes could not be located in the files they cite:")
        for u in doc["quote_verification"]["unlocated"]:
            print("  ", u)
        return 1
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT} does not exist")
            return 1
        have = json.loads(OUT.read_text(encoding="utf-8"))
        if have == doc:
            print(f"PASS: {OUT.name} re-derives byte-identically "
                  f"({doc['totals']['gating']} gating / {doc['totals']['non_gating']} non-gating "
                  f"of {doc['totals']['items']}; {doc['quote_verification']['located']}/"
                  f"{doc['quote_verification']['checked']} quotes located)")
            return 0
        print(f"FAIL: {OUT.name} differs from what the generator now produces")
        return 1
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"  items {doc['totals']['items']}: GATING {doc['totals']['gating']}, "
          f"NON-GATING {doc['totals']['non_gating']} {doc['totals']['non_gating_ids']}")
    print(f"  quotes located {doc['quote_verification']['located']}/"
          f"{doc['quote_verification']['checked']}; "
          f"anchor drift {len(doc['quote_verification']['anchor_drift'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
