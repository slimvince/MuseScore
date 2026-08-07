#!/usr/bin/env python3
"""gen_finish_line_item1_routes.py -- the closing ROUTE for every entry of finish-line item 1.

Item 1 of `tools/audit/phase1_finish_line.json` is "Register entries whose home document is
named in NO user-ratified surface". Its closing act names two routes and they are NOT
equivalent; this tool records, per entry, which one would close it, with the reason.

DERIVED  - the population (imported from the finish-line generator, never re-listed, #6), each
           entry's subject fields, and every count.
AUTHORED - the per-entry ROUTE, its owning specification where one is named, whether that owner
           is UNAMBIGUOUS, and the reason. A route is a judgment about what work would discharge
           an entry; it is marked authored on every row so no reader takes it for a measured
           quantity (D-431).

The tool REFUSES to run if any entry of the population has no authored route, or if an authored
route names an entry the population does not carry -- so the register moving under the table is
a STOP rather than a silent partial answer.

Why RE-HOME is the preferred route, in the record's own words: register rule (e) says a decision
belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION, and the register "is the index
and pointer, never a substitute home"; and D-231's purposive clause (criterion C4) requires that
at completion the SPECIFICATIONS suffice to measure conformance against WITHOUT consulting the
register. A decision reachable only by following a pointer satisfies C1's letter and defeats C4.

Usage:
    python tools/audit/decisions/gen_finish_line_item1_routes.py [--check]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE.parent))

from gen_phase1_finish_line import build as build_finish_line   # noqa: E402  (#6 - imported)

OUT = HERE / "finish_line_item1_routes.json"

REHOME = "RE-HOME"
DELEGATION = "NEEDS A DELEGATION"
NO_HOME = "NO HOME EXISTS"

# The edit surface THIS dispatch authorizes. An entry whose owning specification lies outside it
# is classified but NOT executed -- stated so that a small executed set is read as a scope bound
# rather than as a judgment that the remaining entries have no owner.
EXECUTABLE_OWNER_PREFIX = "ARCHITECTURE.md"

# ---------------------------------------------------------------------------------------------
# The authored routes. (route, owning_specification_or_None, unambiguous, reason)
# ---------------------------------------------------------------------------------------------
ROUTES = {

    # ---- cowork_architecture_reassessment.md -- superseded meta-findings ----------------------
    "D-282": (NO_HOME, None, False,
              "Superseded meta-finding. Its live content is carried by D-115 and D-191, both of "
              "which are homed; writing it into a specification would put a second copy of a rule "
              "its successors already state, which #6 forbids. No specification owns a superseded "
              "finding AS a finding, so neither route applies."),
    "D-283": (NO_HOME, None, False,
              "Superseded meta-finding; the successors D-001 and D-096 are later, explicit and "
              "user-ratified on the same subject and are homed. Re-homing would duplicate them (#6)."),
    "D-284": (NO_HOME, None, False,
              "Superseded meta-finding; D-036 carries the standing doctrine and D-001/D-010 retired "
              "the mechanism it warned about. Re-homing would duplicate a homed rule (#6)."),
    "D-285": (NO_HOME, None, False,
              "Superseded meta-finding, absorbed by the ratified factorization's emission categories "
              "and the ornament-label increment. Re-homing would duplicate them (#6)."),

    # ---- cowork_architecture_review_2026_07.md -- ratified amendments -------------------------
    "D-494": (REHOME, "ARCHITECTURE.md Layer 5 (function/cadence) AND the Layer-3 key section",
              False,
              "One entry places obligations on TWO layers -- key-confirmation channels that do not "
              "need a cadence (Layer 5) and an enharmonic-identity rule for key spans (Layer 3). "
              "Which section carries a single amendment spanning both is not determinate."),
    "D-495": (REHOME, "ARCHITECTURE.md Layer 5 (cadence admission)", False,
              "The obligation is on cadence admission, which Layer 5 owns, but its trigger is the "
              "L1.5 phrase-boundary profile whose contract is delegated elsewhere. Which of the two "
              "carries a fallback rule spanning both is not determinate."),
    "D-496": (REHOME, "ARCHITECTURE.md §7 (The Knowledge Base)", False,
              "The one-store-or-two question is about the Harmonic Vocabulary's relation to the "
              "function layer's pairwise grammar. The amendment DEFERS the decision to the "
              "recognition-consumer build, so no section can yet state it as a rule -- what would be "
              "written is that a choice is owed."),
    "D-497": (REHOME, "ARCHITECTURE.md §6 (The Style System) / the preset constants", False,
              "The amendment requires an existing mark to be APPLIED to named constants and idioms, "
              "and the validating corpus named beside each. That is an obligation over a constant "
              "table rather than a rule a specification section states."),
    "D-498": (NO_HOME, None, False,
              "The entry records that a PRODUCT STANCE IS OWED for mostly-uncertain output and for "
              "non-tonal music. There is no decision content to write into a specification -- what is "
              "recorded is the absence of one. Neither route applies until the stance is taken."),
    "D-499": (NO_HOME, None, False,
              "Four documentation riders -- a consolidated ownership page, a mark, a property to be "
              "written down, a file format. Each is apparatus owed, not a rule a specification states."),
    "D-500": (DELEGATION, "cowork_score_census.md (the corpus decision surface)", False,
              "A ratified widening of the material the analysis is measured against. Its owner is the "
              "corpus census, whose delegation today reaches §8c only; widening a delegation is the "
              "act rule (g) reserves to the user."),

    # ---- cowork_audit_obligation_map.md ------------------------------------------------------
    "D-568": (REHOME, "ARCHITECTURE.md §2.14 (Layered AND Iterative Inference)", False,
              "A strategy statement about where precision work goes on each of two axes. It governs "
              "no single layer, and §2.14 states the inference shape rather than a work programme, so "
              "the owning section is not determinate."),

    # ---- cowork_census_full_needs_audit.md ---------------------------------------------------
    "D-513": (DELEGATION, "cowork_score_census.md", False,
              "A rule about what a corpus registry's content field does and does not establish. Its "
              "subject is the corpus census surface, whose delegation reaches §8c only."),
    "D-514": (DELEGATION, "cowork_score_census.md", False,
              "A record-only constraint on a newly acquired annotation set that overlaps the gate "
              "corpus. Its subject is corpus scope; the census owns it and the delegation does not reach it."),
    "D-515": (DELEGATION, "cowork_score_census.md", False,
              "A ground-truth need promoted to a tracked row of its own. Its subject is the needs "
              "vector the census owns."),
    "D-516": (DELEGATION, "cowork_score_census.md", False,
              "Two ground-truth classes adopted into the needs list. Same owner and same gap as D-515."),

    # ---- cowork_delta_check_dispositions.md --------------------------------------------------
    "D-635": (REHOME, "ARCHITECTURE.md Layer 3 (the backward re-reading facility)", True,
              "The entry states that reach-back is a real product requirement currently masked by the "
              "whole-score load, and that it must land WITH selection-based loading. The Layer-3 "
              "section already carries the reach-back facility and its shipped-off state, so the "
              "decision has a determinate place inside a section that owns the mechanism."),

    # ---- cowork_eg1_premise_checks.md --------------------------------------------------------
    "D-608": (REHOME, "ARCHITECTURE.md Layer 4 (the G4/C1 symmetric-root spelling-pin)", True,
              "A measured-false entry premise for a named Layer-4 mechanism the Layer-4 section "
              "already describes by name. The section owns the mechanism, so the finding has a "
              "determinate place in it."),
    "D-609": (REHOME, "ARCHITECTURE.md Layer 4 (the G1 commit/inherit/abstain ladder)", True,
              "The abstention rate rides on an unfitted seed constant in the Layer-4 decoder, whose "
              "commit/inherit/abstain ladder the Layer-4 section already describes by name."),

    # ---- cowork_eg2_scoping.md ---------------------------------------------------------------
    "D-564": (REHOME, "CLAUDE.md gate block (D), the cross-layer-budget caveat", False,
              "A correction of record to the caveat that apportions the residual across layers -- the "
              "over-grabbed-segmentation case corrupts the BASS and not only the pitch-class window. "
              "Its owner is a CLAUDE.md caveat block, which lies outside this dispatch's edit surface."),

    # ---- cowork_factorization_desk_simulation.md ---------------------------------------------
    "D-449": (REHOME, "the joint estimator's specification in ARCHITECTURE.md", False,
              "Factor granularity for the ratified factorization. The joint estimator is specified in "
              "the document's OPENING BANNER rather than in a section of its own, and a banner is not "
              "a section a decision can be sited inside; the owner is therefore not determinate."),
    "D-450": (REHOME, "the joint estimator's specification in ARCHITECTURE.md", False,
              "The key-signature/declared-mode prior conditions the initial key state only. Same owner "
              "and same indeterminacy as D-449."),
    "D-451": (REHOME, "CLAUDE.md principle #17(c), the desk-simulation stage", False,
              "A standing rule about what a desk simulation's table values may and may not become. Its "
              "owner is the premise gate in CLAUDE.md, outside this dispatch's edit surface."),
    "D-452": (REHOME, "CLAUDE.md principle #17(c), the desk-simulation stage", False,
              "A standing rule that every desk-simulation trace runs at identity weights. Same owner as D-451."),
    "D-453": (NO_HOME, None, False,
              "The desk simulation's VERDICT -- nine of ten traces passed and no finding reopens the "
              "structure. A verdict about a stage that has run is a finding, not a rule a specification "
              "states; what it ratifies is already homed as the factorization itself."),

    # ---- cowork_fb_redesign_design.md (LEGACY surface) ---------------------------------------
    "D-490": (REHOME, "docs/scoring_model.md or ARCHITECTURE.md §4.1 (ChordAnalyzer)", False,
              "A falsification of the fine-grain function override, on the LEGACY scorer awaiting "
              "deletion. Both surfaces describe that scorer and the record does not settle which owns "
              "a post-scoring override's retirement evidence."),
    "D-491": (REHOME, "docs/scoring_model.md or ARCHITECTURE.md §4.1 (ChordAnalyzer)", False,
              "A refutation of the vertically-fair repair of the same override. Same owner question as D-490."),
    "D-492": (REHOME, "docs/scoring_model.md or ARCHITECTURE.md §4.1 (ChordAnalyzer)", False,
              "The recommended redesign of the same override. Same owner question as D-490, and the "
              "recommendation is not adopted, so what a section would state is a proposal."),
    "D-493": (REHOME, "docs/scoring_model.md or ARCHITECTURE.md §4.1 (ChordAnalyzer)", False,
              "Records that the principled restriction is UN-COMPUTABLE today. Same owner question as D-490."),

    # ---- cowork_gateA_unification_design.md (LEGACY surface) ---------------------------------
    "D-510": (REHOME, "docs/scoring_model.md (the gates and post-scoring passes)", False,
              "Which promotion carry is correct, on the legacy scorer. docs/scoring_model.md is the "
              "authoritative reference for scoring terms and gates, but ARCHITECTURE.md §4.1 also "
              "describes the same surface; the record does not settle which owns a promotion primitive."),
    "D-511": (REHOME, "docs/scoring_model.md (the gates and post-scoring passes)", False,
              "One promotion primitive with a present-first dedup guard. Same owner question as D-510."),
    "D-512": (REHOME, "docs/scoring_model.md (the gates and post-scoring passes)", False,
              "Gate A's retirement condition. Same owner question as D-510."),

    # ---- cowork_idiom_discovery_design.md ----------------------------------------------------
    "D-542": (REHOME, "ARCHITECTURE.md §6.7 (the canonical style taxonomy)", False,
              "The discover-then-name protocol for the study that produces the taxonomy. §6.7 owns the "
              "taxonomy, not the method that discovers it, so the owning section is not determinate."),
    "D-543": (REHOME, "ARCHITECTURE.md §6.7 (the canonical style taxonomy)", False,
              "The encoding the study uses. Same owner question as D-542."),
    "D-544": (REHOME, "ARCHITECTURE.md §6.7 (the canonical style taxonomy)", False,
              "Confound control as a first-class validity gate for the study. Same owner question as D-542."),
    "D-545": (REHOME, "ARCHITECTURE.md §6.7 (the canonical style taxonomy)", False,
              "The extraction tool the study may use, and the prohibition on our own inference touching "
              "it. Same owner question as D-542."),

    # ---- cowork_information_loss_audit.md ----------------------------------------------------
    "D-581": (DELEGATION, "cowork_audit_protocol.md", False,
              "A four-verdict classification rule for an information-loss sweep. Its subject is audit "
              "method, which the audit protocol document homes (D-431, D-434, D-436, D-640, D-641); that "
              "document is itself named in no user-ratified surface, so the route runs through a delegation."),
    "D-582": (REHOME, "CLAUDE.md principle #12", False,
              "A recomputable collapse is not information loss -- which is the qualification principle "
              "#12 already carries in its own text. The owner is CLAUDE.md, outside this dispatch's edit surface."),
    "D-583": (DELEGATION, "cowork_audit_protocol.md", False,
              "The condition under which a known deferred loss is kept. Same owner and same gap as D-581."),

    # ---- cowork_layer1_extend_design.md ------------------------------------------------------
    "D-628": (REHOME, "ARCHITECTURE.md Layer 1 (the lossless note model)", True,
              "The finest meaningful extension step is the change-point, because within a slice the "
              "sounding set is constant. It is a bound on the note model's own extend operation, and "
              "the Layer-1 section is the specification of that model."),

    # ---- cowork_layer1_tone_collection_design.md ---------------------------------------------
    "D-569": (NO_HOME, None, False,
              "The user RULED on 2026-08-04 that this document is not a delegation target because the "
              "concern it designs was ABSORBED BY THE NOTE MODEL, and that its entries stay `gap` -- a "
              "delegation would be a second home for a concern that already has one (#6). Whether "
              "re-homing is nevertheless owed is a question that ruling did not put, so no route is "
              "proposed here."),
    "D-570": (NO_HOME, None, False,
              "Same ruling and same reason as D-569: an upstream layer's oracle is the score, recorded "
              "on a document the user ruled is not a delegation target with its entries left `gap`."),

    # ---- cowork_layer3_keymode_impl_design.md ------------------------------------------------
    "D-603": (REHOME, "CLAUDE.md gate block (A) / the measurement conventions", False,
              "How a behaviour-changing increment is graded while the pipeline is being rebuilt. A "
              "measurement convention, whose home is the gate block that publishes the conventions -- "
              "outside this dispatch's edit surface."),
    "D-604": (REHOME, "CLAUDE.md gate block (A), the grading conventions", False,
              "A defensible modal reading the ground truth cannot represent is a ground-truth limitation. "
              "That is a GRADING convention and belongs beside the four the gate block already states."),

    # ---- cowork_layer3_reachback_design.md ---------------------------------------------------
    "D-622": (REHOME, "ARCHITECTURE.md Layer 3 (the backward re-reading facility)", False,
              "The section owns the mechanism, so the SITE is determinate -- but the entry is the subject "
              "of an OPEN user ruling (OPEN_ITEMS.md OI-331): a live user-ratified entry, D-261, names "
              "the very proxy this one records as measured false, and all three candidate remedies change "
              "a user-ratified entry. Writing it into the specification would settle that by fiat."),
    "D-623": (REHOME, "ARCHITECTURE.md Layer 3 (the as-wired orchestrator)", True,
              "A selection-aware capability is a PARAMETER on the one orchestrator, never a sibling. The "
              "Layer-3 section already specifies that orchestrator and its seam by name, so the decision "
              "has a determinate place inside a section that owns the mechanism."),
    "D-624": (REHOME, "ARCHITECTURE.md Layer 3 (the backward re-reading facility)", True,
              "The hard bound and the score start are safety caps for a loop that never settles, never the "
              "amount of context a layer needs. It qualifies the reach-back facility the Layer-3 section "
              "already carries."),

    # ---- cowork_layer5_function_methods.md ---------------------------------------------------
    "D-584": (REHOME, "ARCHITECTURE.md Layer 5 (the function/cadence layer)", True,
              "The perfect/imperfect cadence call is made on the bass-derived inversion. The Layer-5 "
              "section specifies the cadence detector by name, so a rule about how its call is made has a "
              "determinate place in it."),
    "D-585": (REHOME, "ARCHITECTURE.md Layer 5 (the function/cadence layer)", True,
              "The bass-scale-degree prior is a soft tie-breaker and never a gate -- a constraint on what "
              "the function layer may do with an admitted prior."),
    "D-586": (REHOME, "ARCHITECTURE.md Layer 5 (the function/cadence layer)", True,
              "What the word naming this layer means in the literature, and that the project's own "
              "component is misnamed for the same confusion. It is a statement about this layer's own "
              "subject matter and the section is where a reader meets the name."),

    # ---- cowork_phase2_architecture_review.md ------------------------------------------------
    "D-579": (NO_HOME, None, False,
              "Recorded SUPERSEDED-IN-FACT: the anchor obligation describes an ordering the rebuilt layer "
              "stack already implements. What is live is the layer specifications themselves, so re-homing "
              "would duplicate them (#6)."),
    "D-580": (REHOME, "docs/scoring_model.md or ARCHITECTURE.md §4.1 (ChordAnalyzer)", False,
              "Which of the legacy post-scoring gates must survive the dissolution. Recorded DEFERRED, on "
              "the legacy surface, with the same two-candidate owner question as D-490."),

    # ---- cowork_phase5c_l5_build_plan.md -----------------------------------------------------
    "D-602": (REHOME, "CLAUDE.md gate block (A), the grading conventions", False,
              "A layer is judged on coverage-matched accuracy AND correct abstention, never on raw "
              "coverage. A measurement convention whose home is the gate block -- outside this dispatch's "
              "edit surface, and the abstain-aware convention it cites already lives there."),

    # ---- cowork_phrase_boundary_methods.md ---------------------------------------------------
    "D-607": (REHOME, "ARCHITECTURE.md Layer 1 (the L1.5 phrase-boundary primitive)", True,
              "A stated fact of absence bounding what the phrase-boundary extension may claim. The "
              "Layer-1 section is where the record sites the L1.5 primitive -- it carries that primitive's "
              "delegation pointer and states in its own words why it is sited there."),

    # ---- cowork_sensitive_cell_probe.md ------------------------------------------------------
    "D-532": (REHOME, "the joint estimator's specification in ARCHITECTURE.md", False,
              "A pooling level added to the chord-transition table. The joint estimator is specified in "
              "the opening banner rather than a section, so the owner is not determinate (as D-449)."),
    "D-533": (REHOME, "the joint estimator's specification in ARCHITECTURE.md", False,
              "The back-off rule for a continuation too rare to store. Same owner question as D-532."),
    "D-534": (REHOME, "the joint estimator's specification in ARCHITECTURE.md", False,
              "The missing-chord-tone penalty counted per chord factor. Same owner question as D-532."),
    "D-535": (NO_HOME, None, False,
              "The checking stage's VERDICT -- the counted tables overturn no desk-simulation verdict. A "
              "finding about a stage that has run, not a rule a specification states."),

    # ---- cowork_term_theory_grounding.md -----------------------------------------------------
    "D-473": (REHOME, "CLAUDE.md principle #1/#2 (the fact- and theory-basis rules)", False,
              "The labelling and cross-checking method for a theory-grounding pass. Its owner is the "
              "principle it operationalizes, outside this dispatch's edit surface."),
    "D-474": (REHOME, "CLAUDE.md principle #21", False,
              "★ The one entry whose content is ALREADY WRITTEN into its owning specification: principle "
              "#21 carries the fact-of-absence and names D-474 in terms. What is outstanding is the "
              "register's HOME field, which still points at the findings document. The route is a "
              "re-home, and it is a field correction rather than a piece of writing."),
    "D-475": (DELEGATION, "cowork_score_census.md", False,
              "That a held annotation set is not established as an instrument. Its subject is corpus "
              "establishment, which the census owns; the delegation does not reach it."),

    # ---- cowork_tpc_capability_design.md -----------------------------------------------------
    "D-625": (REHOME, "ARCHITECTURE.md §5.14 (Enharmonic Root Spelling) or the Layer-1.5 spelling view",
              False,
              "How spelling presence is tested. Two sections describe the spelling surface -- §5.14 the "
              "enharmonic disambiguation and the Layer-4 section the shared line-of-fifths primitive -- "
              "and the record does not settle which owns the predicate."),

    # ---- cowork_types_header_design.md -------------------------------------------------------
    "D-610": (NO_HOME, None, False,
              "A completed refactor's zero-churn property. It states what one relocation did, not a rule "
              "the code must go on satisfying; no specification section owns a finished move."),

    # ---- cowork_union_search_record.md -------------------------------------------------------
    "D-613": (DELEGATION, "cowork_score_census.md", False,
              "A confirmed absence of ground truth for implied polyphony, plus what the surviving voice "
              "labels actually measure. Corpus-establishment subject; the census owns it."),
    "D-614": (DELEGATION, "cowork_score_census.md", False,
              "Licence posture of every difficulty-grade label source. Corpus subject, and the census "
              "already carries the shipped-parameter licence-pool constraint at §8c -- but widening a "
              "delegation is the user's act."),

    # ---- docs/back_half_design.md ------------------------------------------------------------
    "D-531": (REHOME, "ARCHITECTURE.md §2.2 (Interface-Based Design for ML Substitutability)", False,
              "The hand-built emission is confirmed and the learned replacement is not triggered, retained "
              "as a fallback with a concrete trigger. §2.2 owns the substitutability property; whether it "
              "also owns a standing not-yet-triggered verdict is not settled by the record."),
    "D-539": (REHOME, "CLAUDE.md (the standing method rules)", False,
              "Decompose every error slice into structural, fitted and ceiling BEFORE building. A standing "
              "method rule whose home is the principles, outside this dispatch's edit surface."),

    # ---- docs/decoder_design.md --------------------------------------------------------------
    "D-325": (REHOME, "ARCHITECTURE.md Layer 4 (the per-slice chord decoder)", False,
              "An ordering constraint between a correction rule and widening the search. It governs the "
              "legacy correction surface AND the decoder's search, and the record does not settle which "
              "of the two sections carries a rule about their interaction."),
    "D-326": (REHOME, "ARCHITECTURE.md Layer 4 (the per-slice chord decoder)", False,
              "The search emits the whole path with alternatives and margins. The Layer-4 section "
              "specifies the carry, but this entry's subject is the SEARCH, which that section describes "
              "as dormant staging; which surface owns it is not determinate."),
    "D-327": (REHOME, "docs/scoring_model.md (the root-continuity guard)", False,
              "The guard reads reconstructed inversion credit rather than testing a sounding third. A "
              "legacy scoring term, with the same two-candidate owner question as D-490."),
    "D-328": (REHOME, "docs/scoring_model.md §8 (constraints and dead ends)", False,
              "A wider search cannot fix the arpeggio root failure. It is a recorded dead end for the "
              "legacy scorer, and §8 of the scoring model is where dead ends are collected -- but the "
              "finding is about the decoder's search, so the owner is not determinate."),

    # ---- docs/implementation_roadmap.md ------------------------------------------------------
    "D-419": (REHOME, "ARCHITECTURE.md §7 (The Knowledge Base) / the planned consumers block", False,
              "Until the recognition consumer is built, the function layer does not touch the vocabulary. "
              "The planned-consumers block names that consumer, but a build-ORDER rule is not a statement "
              "either section makes, so the owner is not determinate."),
    "D-421": (REHOME, "ARCHITECTURE.md §6.7 (the canonical style taxonomy)", False,
              "Idiom re-discovery rides every corpus wave on research material only, and a changed cluster "
              "set is its own ratification event. §6.7 owns the taxonomy; whether it owns the re-run "
              "protocol is the same question as D-542."),
    "D-422": (DELEGATION, "cowork_score_census.md", False,
              "The jazz fit waits on jazz ground truth. Recorded DEFERRED; its binding fact is a corpus "
              "fact, so the census is the owner and the delegation does not reach it."),
    "D-423": (REHOME, "docs/scoring_model.md §8 / ARCHITECTURE.md §4.1", False,
              "Three standing prohibitions over the LEGACY post-scoring gates plus the retirement stage. "
              "Explicitly legacy-scoped; the same two-candidate owner question as D-490."),

    # ---- docs/iter92_joint_bass_chord_scoring.md ---------------------------------------------
    "D-536": (REHOME, "docs/scoring_model.md (the bass/chord joint selection)", False,
              "The bass and chord are chosen together as a triple. A legacy-scorer change; same "
              "two-candidate owner question as D-490."),
    "D-537": (REHOME, "docs/scoring_model.md (§4 bonuses)", False,
              "The completeness bonus fires only for a root-position reading with all three tones present. "
              "A legacy scoring bonus with a guard; the scoring model's §4 is the nearest owner, but "
              "ARCHITECTURE.md §4.1 also specifies the scorer."),
    "D-538": (REHOME, "CLAUDE.md (the staging discipline for a multi-signal change)", False,
              "One signal at a time with the corpus re-measured between. A landing discipline rather than "
              "a scoring rule; its home is the project's standing rules, outside this dispatch's edit surface."),

    # ---- docs/iteration_path1_summary.md -----------------------------------------------------
    "D-280": (REHOME, "ARCHITECTURE.md §3.3 (the inference/presentation boundary)", False,
              "Gates read structured fields only, never a chord symbol string or a Roman numeral. §3.3 "
              "states the boundary this restricts, but the entry is an INPUT restriction on scoring, which "
              "docs/scoring_model.md also governs; the owner is not determinate."),
    "D-281": (REHOME, "CLAUDE.md gate block (C) / BUILD_AND_TEST.md (the measurement procedure)", False,
              "The batch tool must emit the structured fields on every alternative or the corpus figures "
              "silently revert. Its owner is the measurement procedure, outside this dispatch's edit surface."),

    # ---- docs/layer_architecture_audit.md ----------------------------------------------------
    "D-463": (REHOME, "docs/scoring_model.md / ARCHITECTURE.md §4.1", False,
              "Temporal signals inside the vertical scorer stay put, and the gate depending on one must "
              "move with them. Legacy-surface debt with the same two-candidate owner question as D-490."),
    "D-464": (REHOME, "ARCHITECTURE.md §5.3 (TemporalContext)", False,
              "No further progression-level signal may enter the single-step look-around structure. §5.3 "
              "specifies that structure, but the rule's other half concerns a planned progression-level "
              "structure that has no section, so the owner is not determinate."),
    "D-465": (REHOME, "docs/scoring_model.md §8 / ARCHITECTURE.md §4.1", False,
              "The three-test policy for judging a proposed post-scoring gate. Legacy-surface policy with "
              "the same two-candidate owner question as D-490."),

    # ---- docs/precision_metric_design.md -----------------------------------------------------
    "D-486": (REHOME, "CLAUDE.md gate block (A), the grading conventions", False,
              "A measurement publishes its coverage denominator and its per-corpus breakdown. A grading "
              "convention belonging beside the four the gate block already states -- outside this "
              "dispatch's edit surface."),

    # ---- docs/stage4b_design.md --------------------------------------------------------------
    "D-571": (NO_HOME, None, False,
              "Recorded SUPERSEDED-IN-FACT: a scoring change on the legacy key path, which the production "
              "arm no longer runs. No live specification owns a term on a superseded path."),
    # ★ RE-ROUTED 2026-08-04 under ruling R2 / register entry D-644 (dispatch
    # `cc_instruction_guard_fix_and_item1d.md`, Task 2.2). The former route was
    # `(NO_HOME, None, False, "Recorded SUPERSEDED-IN-FACT, same legacy key path and same reason
    # as D-571.")` — preserved here (#12) because it was correct under the rulings then in force:
    # R1/D-642 moves a superseded entry's obligation to its SUCCESSOR, and this entry has none.
    # R2/D-644 is what changed: where the content is a REMOVAL there is no successor to move it
    # to, and the owning specification instead states the current behaviour and records the
    # removal as a tried-and-closed line. That IS a home, so the route is RE-HOME, and §5.2 is
    # unambiguous — the precedent's own act was performed there for the sibling removal that
    # landed at the same increment (D-058).
    "D-572": (REHOME, "ARCHITECTURE.md §5.2 (the legacy key path)", True,
              "Recorded SUPERSEDED-IN-FACT on the legacy key path, and its content is a REMOVAL: "
              "the hard post-hoc declared-mode promotion was taken out outright rather than kept "
              "in a gated form. Under D-644 the owning specification states the current behaviour "
              "and records the removal as a tried-and-closed line — which is exactly what §5.2 "
              "already does for D-058, the piece-start shortcut removed at the same increment."),

    # ---- docs/stage4c_cadence_key_design.md --------------------------------------------------
    "D-616": (REHOME, "ARCHITECTURE.md Layer 3 (key scoring) or the resolver/section scope", False,
              "A global tonic anchor enters key scoring at RESOLVER/SECTION scope and never inside the "
              "window scorer. The scope it names spans the decoder and the resolver, and the resolver is "
              "retired from the production region path, so which section owns the rule is not determinate."),

    # ---- docs/stage4d_local_modulation_design.md ---------------------------------------------
    "D-605": (REHOME, "ARCHITECTURE.md Layer 3 (local key) / the key-area grouping", False,
              "The local-key hypothesis derives from key-agnostic signals only and never from the key-area "
              "grouping. The rule's two ends sit in different sections -- Layer 3 for the hypothesis and "
              "the key-area grouping for what it may not read -- so the owner is not determinate."),
    "D-606": (REHOME, "CLAUDE.md gate block (A), the grading conventions", False,
              "The binding metric for the modulation detector is modulation correctness, not the agreement "
              "percentage. A grading convention, and the entry itself cites the abstain-aware convention "
              "that already lives in the gate block."),

    # ---- docs/symbol_input_audit.md ----------------------------------------------------------
    "D-501": (REHOME, "ARCHITECTURE.md §3.3 (the inference/presentation boundary)", False,
              "A written chord symbol may be read only as a comparison or ground-truth label. §3.3 states "
              "the boundary, but the rule also binds MEASUREMENT TOOLS, which no ARCHITECTURE.md section "
              "governs; the owner is not determinate."),

    # ---- docs/unified_analysis_pipeline.md ---------------------------------------------------
    "D-469": (REHOME, "ARCHITECTURE.md §5.13 (Analyze-at-Tick Path Table)", False,
              "The tick-local path is left outside the unified pipeline by design. §5.13 tabulates that "
              "path, but the decision is about the pipeline's scope, which §11.5 and §3.3 also describe; "
              "the owner is not determinate."),
    "D-470": (REHOME, "ARCHITECTURE.md §5.3 (TemporalContext)", False,
              "The temporal-context extension fields are recorded during the analysis pass and never "
              "rebuilt by a consumer. §5.3 specifies those fields, but the rule binds the CONSUMERS, "
              "which §11.5 describes; the owner is not determinate."),
    "D-471": (REHOME, "ARCHITECTURE.md §11.5 (Region Analysis and the Chord Track)", False,
              "The sub-beat annotation duration gate is kept or dropped on a measured observation run with "
              "the verdict stated in advance. The annotation layers block sits in §11.5, but what is "
              "recorded is a measurement protocol rather than a rule; the owner is not determinate."),
    "D-472": (REHOME, "ARCHITECTURE.md §11.5 (Region Analysis and the Chord Track)", False,
              "Key areas are grouped by a smoothing pass over stabilized regions. The key-area grouping is "
              "described both there and in the Layer-6 section, which owns key-areas in the target "
              "architecture; the owner is not determinate."),
}


# ---------------------------------------------------------------------------------------------
# The OI-342 reading: what the OWNER JUDGMENT says, read instead of the `owner_is_unambiguous`
# column. Every test below is an EXACT PHRASE the authored reasons already contain -- no signal
# vocabulary is tuned to reproduce a verdict, because a cut tuned until it agrees is the
# "stable enough to be cited" failure repeating.
# ---------------------------------------------------------------------------------------------
EDIT_SURFACE_PHRASE = "outside this dispatch's edit surface"
DETERMINATE_PHRASE = "determinate"
NOT_DETERMINATE_PHRASE = "not determinate"
EXECUTABLE_OWNER_SUBSTRING = "ARCHITECTURE.md"


def _owner_judgment_reading(rows: list[dict]) -> dict:
    """Read the owner JUDGMENT rather than the column, over the open RE-HOME rows (OI-342)."""
    open_rehome = [r for r in rows if r["route"] == REHOME and not r["closed_by_this_wave"]]
    surface_only = [r for r in open_rehome if EDIT_SURFACE_PHRASE in r["reason"]]
    determinate = [r for r in open_rehome
                   if DETERMINATE_PHRASE in r["reason"]
                   and NOT_DETERMINATE_PHRASE not in r["reason"]]
    on_surface = [r for r in open_rehome
                  if EXECUTABLE_OWNER_SUBSTRING in (r["owning_specification"] or "")]
    column_true = [r for r in open_rehome if r["owner_is_unambiguous"]]

    return {
        "what_this_is": (
            "OPEN_ITEMS.md OI-342 records that the `owner_is_unambiguous` column carries the "
            "EDIT-SURFACE answer for part of this population, although the row already has a "
            "separate field for that. This block reads the owner JUDGMENT -- the recorded reason "
            "-- instead of the column, and reports where the two disagree. It CORRECTS NOTHING: "
            "the column is untouched and no count in it is re-authored."
        ),
        "how_each_set_is_cut": (
            "By an exact phrase the authored reasons already contain, never by a vocabulary "
            "assembled until the answer came out right. `disagreement` is the reasons containing "
            f"{EDIT_SURFACE_PHRASE!r}; `asserts_a_determinate_site` is the reasons containing "
            f"{DETERMINATE_PHRASE!r} and not {NOT_DETERMINATE_PHRASE!r}."
        ),
        "open_re_home_rows": len(open_rehome),
        "disagreement_column_says_ambiguous_reason_names_only_the_edit_surface": {
            "count": len(surface_only),
            "ids": [r["id"] for r in surface_only],
            "what_it_means": (
                "For each of these the recorded reason names a determinate site and then says it "
                "lies outside the edit surface. The column and the judgment disagree, and the "
                "artifact's own `executable_under_this_dispatch` field is what was supposed to "
                "carry the second answer."
            ),
            "what_is_NOT_claimed": (
                "That all of them have a determinate owner. OI-342 states in terms that three of "
                "them have a genuinely soft owner independent of the surface, and declines to "
                "propose a corrected count; nothing here proposes one either."
            ),
        },
        "asserts_a_determinate_site_although_the_column_says_otherwise": {
            "count": len(determinate),
            "ids": [r["id"] for r in determinate],
            "why_it_is_still_not_executable": (
                "The same reason states the blocker: the entry is the subject of an OPEN user "
                "ruling, so writing it into the specification would settle that ruling by fiat."
            ),
        },
        "rows_whose_owner_names_the_editable_surface": {
            "count": len(on_surface),
            "column_says_unambiguous": [r["id"] for r in column_true],
            "of_those_whose_reason_names_only_the_edit_surface": [
                r["id"] for r in on_surface if EDIT_SURFACE_PHRASE in r["reason"]],
            "consequence_for_this_wave": (
                "The disagreement OI-342 records is confined to rows whose owner is NOT on the "
                "editable surface, so it moves nothing this wave could execute. What it moves is "
                "what the column MEANS to a reader deciding how much of item 1 is closeable."
            ),
        },
        "the_executable_set_at_HEAD": {
            "count": len(column_true),
            "ids": [r["id"] for r in column_true],
            "derived_rather_than_read_off_a_stored_count": (
                "Computed from the rows at HEAD. It is empty because the preceding wave executed "
                "every member, not because none exists -- which is the reading OI-342 exists to "
                "keep a reader from making."
            ),
        },
    }


def _was_executed(entry_id: str) -> bool:
    """A RE-HOME whose owner is unambiguous AND lies inside this dispatch's edit surface."""
    route, owner, unambig, _ = ROUTES[entry_id]
    return bool(route == REHOME and unambig and owner and owner.startswith(EXECUTABLE_OWNER_PREFIX))


def build() -> dict:
    fl = build_finish_line()
    item1 = fl["THE_FINISH_LINE"][0]
    by_doc = item1["population"]["entry_ids_by_document"]
    pop = [i for ids in by_doc.values() for i in ids]

    missing = [i for i in pop if i not in ROUTES]
    # An entry that has LEFT item 1 is expected in exactly TWO ways, and anything else is the
    # register moving under the table and is still a STOP.
    #   * a wave RE-HOMED it — the homing is what removes it from the population; reported CLOSED;
    #   * ruling R3's entry-level re-cut DISCHARGED it (2026-08-04) — the entry is still `gap` in
    #     the register, and what removed it from the item is the ruling rather than an act on the
    #     document. Its route classification is kept and it is reported as discharged, because
    #     the application of R1 downstream reads this class and must still find it.
    recut = fl["★_the_entry_level_re_cut"]["direction_1_entries_the_entry_cut_DROPS"]
    discharged_doc = {i: doc
                      for per_item in recut["ids_by_item"].values()
                      for doc, ids in per_item.items()
                      for i in ids}
    discharged_ids = set(discharged_doc)

    left = [i for i in ROUTES if i not in pop]
    closed = sorted(i for i in left if _was_executed(i))
    discharged = sorted(i for i in left if i in discharged_ids and not _was_executed(i))
    stray = sorted(i for i in left if not _was_executed(i) and i not in discharged_ids)
    if missing:
        raise SystemExit("STOP: entries of item 1 with no authored route: " + ", ".join(sorted(missing)))
    if stray:
        raise SystemExit("STOP: authored routes for entries item 1 does not carry, which this wave "
                         "did not re-home and no entry-level ruling discharged (the register moved "
                         "under the table): " + ", ".join(stray))

    rows = []
    for i in discharged:
        route, owner, unambig, reason = ROUTES[i]
        rows.append({
            "id": i,
            "home_document": discharged_doc[i],
            "route": route,
            "owning_specification": owner,
            "owner_is_unambiguous": unambig,
            "executable_under_this_dispatch": False,
            "closed_by_this_wave": False,
            "discharged_by_the_entry_level_re_cut": True,
            "reason": reason,
            "authored": "the route, the owner, the unambiguity verdict and the reason",
        })
    for i in closed:
        route, owner, unambig, reason = ROUTES[i]
        rows.append({
            "id": i,
            "home_document": "ARCHITECTURE.md (re-homed 2026-08-04 — no longer in item 1)",
            "route": route,
            "owning_specification": owner,
            "owner_is_unambiguous": unambig,
            "executable_under_this_dispatch": True,
            "closed_by_this_wave": True,
            "reason": reason,
            "authored": "the route, the owner, the unambiguity verdict and the reason",
        })
    for doc, ids in by_doc.items():
        for i in ids:
            route, owner, unambig, reason = ROUTES[i]
            rows.append({
                "id": i,
                "home_document": doc,
                "route": route,
                "owning_specification": owner,
                "owner_is_unambiguous": unambig,
                "executable_under_this_dispatch": _was_executed(i),
                "closed_by_this_wave": False,
                "reason": reason,
                "authored": "the route, the owner, the unambiguity verdict and the reason",
            })

    rehome = [r for r in rows if r["route"] == REHOME]
    deleg = [r for r in rows if r["route"] == DELEGATION]
    nohome = [r for r in rows if r["route"] == NO_HOME]
    execu = [r for r in rows if r["executable_under_this_dispatch"]]
    closed_rows = [r for r in rows if r["closed_by_this_wave"]]

    return {
        "purpose": "The closing ROUTE for every entry of finish-line item 1, with the reason per "
                   "entry. Derived population, authored routes. NOT a completion statement and not "
                   "an authorization for any fix, design or inference change.",
        "generated_by": "tools/audit/decisions/gen_finish_line_item1_routes.py",
        "generated_for": "cc_instruction_finish_line_item1.md (Task 3.2, ruling R3)",
        "derived_at_head_from": [
            "tools/audit/decisions/gen_phase1_finish_line.py -> build() (imported, not repeated, #6)",
        ],
        "what_is_authored_and_what_is_derived": {
            "derived": "the population, each entry's home document, and every count",
            "authored": "the route per entry, the owning specification where one is named, the "
                        "unambiguity verdict, and the reason",
            "why_it_matters": "A route is a judgment about what work would discharge an entry. It "
                              "is marked authored on every row so no reader takes it for a measured "
                              "quantity (D-431).",
        },
        "why_re_home_is_preferred": (
            "Register rule (e): a decision belongs, wherever possible, in the OWNING LAYER'S "
            "SPECIFICATION, and the register is 'the index and pointer, never a substitute home'. "
            "D-231's purposive clause (criterion C4) requires that at completion the SPECIFICATIONS "
            "suffice to measure conformance against WITHOUT consulting the register -- so a decision "
            "reachable only by following a pointer satisfies C1's letter and defeats C4."
        ),
        "what_this_dispatch_may_execute": {
            "surface": "ARCHITECTURE.md only",
            "why": "The standing authorization covers src/composing/, notationaccessibility.cpp and "
                   "ARCHITECTURE.md. Entries whose owning specification is CLAUDE.md, "
                   "docs/scoring_model.md or BUILD_AND_TEST.md are classified here and NOT executed.",
            "consequence_stated_plainly": "A small executed set is a SCOPE BOUND, not a verdict that "
                                          "the remaining entries have no owner. The route column says "
                                          "which do.",
        },
        "★_findings_the_classification_produced": {
            "1_C1_reaches_entries_whose_re_homing_#6_would_FORBID": (
                "Several entries are recorded superseded or absorbed, and their live content is "
                "carried by named successors that ARE homed. Writing them into a specification would "
                "put a second copy of a homed rule, which #6 forbids. So criterion C1, read literally "
                "over the whole register, obliges an act the principles prohibit for part of its "
                "population. Reported, not resolved -- whether C1 reaches superseded entries is the "
                "user's, and nothing here assumes an answer."
            ),
            "2_some_entries_record_that_something_is_OWED_rather_than_decided": (
                "A ratified amendment requiring a product stance to be written, and four documentation "
                "riders, have no decision content to home -- what is recorded is the absence of a "
                "decision. Neither route applies until the decision is taken."
            ),
            "3_one_entry_is_already_written_into_its_owning_specification": (
                "D-474's content is in CLAUDE.md principle #21, which names the entry in terms. What "
                "is outstanding is the register's HOME FIELD, not the writing. It is the one member of "
                "this item for which C1 is substantively satisfied and only the bookkeeping is not."
            ),
            "4_the_two_ruled_documents_are_in_this_population": (
                "cowork_layer1_tone_collection_design.md's two entries sit here although the user "
                "ruled on 2026-08-04 that it is NOT a delegation target and that its entries stay "
                "`gap`. The ruling closed the DELEGATION question and did not put the re-homing one, "
                "so no route is proposed for them."
            ),
            "5_one_entry_is_blocked_by_an_open_user_ruling": (
                "D-622's owning section is determinate, but OPEN_ITEMS.md OI-331 has the user deciding "
                "whether D-261 or D-622 survives. Writing it into the specification would settle that "
                "by fiat, so it is held out of the executed set although its owner is not in doubt."
            ),
        },
        "★_the_owner_judgment_read_rather_than_the_column": _owner_judgment_reading(rows),
        "the_NO_HOME_class_is_dispositioned_under_ruling_R1_elsewhere": (
            "tools/audit/decisions/r1_superseded_reach.json applies the user's ruling R1 of "
            "2026-08-04 to every member of this table's NO-HOME class: the successor the record "
            "names for each entry's live content, whether that successor is homed, and the "
            "disposition that follows. The route column here is UNCHANGED and no disposition or "
            "count is restated (D-431, #6)."
        ),
        "counted": {
            "entries": len(rows),
            "documents": len(by_doc),
            "route_RE_HOME": len(rehome),
            "route_NEEDS_A_DELEGATION": len(deleg),
            "route_NO_HOME_EXISTS": len(nohome),
            "re_home_with_an_unambiguous_owner": len([r for r in rehome if r["owner_is_unambiguous"]]),
            "executable_under_this_dispatch": len(execu),
            "closed_by_this_wave_and_no_longer_in_item_1": len(closed_rows),
            "still_open_in_item_1_at_HEAD": len(rows) - len(closed_rows),
        },
        "executed_this_wave": sorted(r["id"] for r in closed_rows),
        "rows": rows,
    }


def main(argv) -> int:
    data = build()
    text = json.dumps(data, indent=1, ensure_ascii=False)
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT.name} does not exist")
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print(f"FAIL: {OUT.name} differs from what the generator now produces")
            return 1
        c = data["counted"]
        print(f"PASS: {OUT.name} re-derives byte-identically "
              f"({c['entries']} entries over {c['documents']} documents; "
              f"{c['route_RE_HOME']} re-home / {c['route_NEEDS_A_DELEGATION']} delegation / "
              f"{c['route_NO_HOME_EXISTS']} no-home)")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
