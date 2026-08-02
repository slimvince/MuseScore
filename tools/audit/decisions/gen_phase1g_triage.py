#!/usr/bin/env python3
"""Generate `tools/audit/decisions/phase1g_triage.md` — the phase-1g triage table.

WHAT THIS IS.  Phase 1f closed the derived reading list at 143 design documents on the
`cowork_*` / `docs/` surface, of which a measured remainder had never been read.  This
tool derives that remainder MECHANICALLY from the committed cluster artifacts (never by
hand), joins it with the per-file classification this pass made by reading each
document's title, status banner and opening section, and emits the one table that is the
user's decision surface for an exclusion list.

WHY A GENERATOR.  Principle #17(f): no hand-transcribed measurement numbers.  Every
count in the emitted table — the cluster attributions, the class totals, the byte sizes,
the token estimate — is computed here from the artifacts on disk.  Only the CLASS and
the VERIFICATION prose are authored, and they live in `CLASSIFICATION` below, which is
this tool's source of record.

DERIVATION.  A design document is on the surface when it owns at least one cluster whose
recorded disposition is `unresolved` and whose occurrences all sit on the `cowork_*` or
`docs/` design-document surface (a cluster spanning more than one surface is the
manifest's own `mixed sources` bucket and is excluded here exactly as it is there).
`cowork_handoff.md` and `cowork_handoff_archive.md` are the handoff and archive
surfaces, not design documents, and are excluded by name.

Run:  python tools/audit/decisions/gen_phase1g_triage.py [--check]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CLUSTERS = os.path.join(HERE, "decision_clusters.json")
DISPOS = os.path.join(HERE, "cluster_dispositions.json")
OUT = os.path.join(HERE, "phase1g_triage.md")

# Characters per token, measured on this repository's own prose by the phase-1d wave
# against the Read tool's accounting (STATUS_ARCHIVE.md: 789,462 characters / 259,766
# tokens) and re-used unchanged by phase 1f.
CHARS_PER_TOKEN = 3.04

# ---------------------------------------------------------------------------
# The read set.  Phase 1d's twenty-one are enumerated in its own report's Task-1
# table (`cc_phase1d_enumeration_wave_report.md`); phase 1f's two are in the OI-207
# dated note of 2026-08-02.  `docs/beam_widening_design.md` is in BOTH lists, so the
# DISTINCT read count is 22 and the unread population is 121 — see the emitted
# document's "correction of record" section.
# ---------------------------------------------------------------------------
PHASE1D_READ = [
    "docs/beam_widening_design.md",
    "cowork_bounded_context_design.md",
    "cowork_spec_language_sweep.md",
    "docs/stage6_functional_layer_design.md",
    "docs/scoped_joint_design.md",
    "cowork_phase5_branch_backfill_spec.md",
    "cowork_architecture_reassessment.md",
    "cowork_layer5_spec_review.md",
    "cowork_design_doc_template.md",
    "cowork_prefit_gates.md",
    "docs/iteration_path1_summary.md",
    "cowork_engage_arc_plan.md",
    "cowork_audit_postscoringgates.md",
    "cowork_confidence_contract.md",
    "cowork_premise_gate_reflection.md",
    "cowork_audit_harmonicfunctionlayer.md",
    "cowork_prune_pass_checklist.md",
    "cowork_audit_regionanalyzer.md",
    "cowork_audit_jointkeydecision.md",
    "cowork_audit_remaining_layers.md",
    "cowork_notation_output_contract.md",
]
PHASE1F_READ = [
    "cowork_stage5_fitter_design.md",
    "docs/beam_widening_design.md",
]

# The five the phase-1g dispatch names as LIVE-SPEC on their face and sends to a full
# read in the same session.
TASK2_FULL_READ = [
    "cowork_layer4_chordsymbol_design.md",
    "docs/decoder_design.md",
    "cowork_layer5_function_design.md",
    "docs/scoring_model.md",
    "docs/redesign_plan.md",
]

LIVE, SUPERSEDED, REPORT, EVIDENCE = (
    "LIVE-SPEC", "SUPERSEDED-ESTABLISHED", "REPORT/NARRATIVE", "EVIDENCE-FROZEN")

# ---------------------------------------------------------------------------
# The classification.  file -> (class, verification-or-reason).
# For SUPERSEDED-ESTABLISHED and EVIDENCE-FROZEN the verification citation is
# mandatory (the dispatch).  This pass also gives one for every REPORT/NARRATIVE,
# because each of those is a proposed exclusion and an exclusion without evidence is
# the blind sweep the guardrails forbid.
# ---------------------------------------------------------------------------
CLASSIFICATION: dict[str, tuple[str, str]] = {
    # ---- SUPERSEDED-ESTABLISHED -------------------------------------------------
    "cowork_key_layer_design_opening.md": (SUPERSEDED,
        "Own banner `:3-8`: ⛔ SUPERSEDED 2026-07-17 by `cowork_joint_estimator_architecture.md`, "
        "“Do not build from this document”. Successor VERIFIED: it exists, its own line 3 records "
        "the user ratification of 2026-07-14, `OPEN_ITEMS.md:15-18` carries it as the governing "
        "architecture decision, and it is registered as **D-001** (key, mode and chord inferred by ONE "
        "joint decode, LIVE). It covers this document's whole subject — the key is one axis of the "
        "joint estimate, not a separable layer."),

    # ---- EVIDENCE-FROZEN --------------------------------------------------------
    "docs/p3_granularity_ab_3_1b.md": (EVIDENCE,
        "A committed measurement document (its banner `:3-11`: “Measured evidence, committed as "
        "Stage-5 input”). Its one decision — `:70` “Whole-score is shelved. Do not re-attempt "
        "without resolving the granularity question” — is registered as **D-286** (whole-score "
        "interactive analysis SHELVED WITH EVIDENCE; the bounded window is the ratified reading), "
        "ratified by the user 2026-08-02 at the fourth ratification event. The remainder is the "
        "per-tick granularity-accuracy comparison, i.e. data. NOTE for the user: this is the evidence "
        "base of the OPEN extent question [[OI-210]]; excluding it from the DECISION read does not "
        "withdraw it from phase 3."),

    # ---- REPORT/NARRATIVE -------------------------------------------------------
    "cowork_audit_cadencekeyanchor.md": (REPORT,
        "One of the Cowork second-opinion layer audits of the OI-84 certification programme "
        "(own header: “to reconcile with CC's primary audit”). [[OI-84]] is ✅ COMPLETE "
        "2026-07-12 — every surviving layer certified on two passes — and the programme's findings "
        "are register rows OI-86…OI-140. Measured: phase 1d read FOUR siblings of this class in full "
        "(`cowork_audit_postscoringgates`, `_harmonicfunctionlayer`, `_regionanalyzer`, "
        "`_jointkeydecision`) and they produced ZERO register entries. Zero ruling-vocabulary hits of "
        "its own."),
    "cowork_audit_chordpostpasses_sparse.md": (REPORT,
        "Same class and same verification as `cowork_audit_cadencekeyanchor.md` (OI-84 COMPLETE; "
        "findings rowed OI-86…OI-140; four read siblings yielded zero entries). Zero "
        "ruling-vocabulary hits."),
    "cowork_audit_keymodeanalyzer.md": (REPORT,
        "Same class and same verification as `cowork_audit_cadencekeyanchor.md`. Zero "
        "ruling-vocabulary hits."),
    "cowork_audit_localmodulationdetector.md": (REPORT,
        "Same class and same verification as `cowork_audit_cadencekeyanchor.md`. Zero "
        "ruling-vocabulary hits."),
    "cowork_spec_polish_findings_a.md": (REPORT,
        "Own banner `:3-5`: “✅ DISPOSITIONED (the merged Cowork doc pass, 2026-07-03). All 67 rows "
        "executed against the four documents … retained as the audit record; the row texts below "
        "describe the PRE-pass state.” The standard it applies is registered (**D-193**, the writing "
        "standards live in one place; **D-255**…**D-257**, the template rules). Its ruling-vocabulary "
        "hits are inside row texts describing offenders, not rulings of its own."),
    "cowork_spec_polish_findings_b.md": (REPORT,
        "Own banner `:3-5`: “✅ DISPOSITIONED … All 87 rows executed … Retained as the audit record; "
        "row texts describe the PRE-pass state.” Same standard and same registration as pass A. Zero "
        "ruling-vocabulary hits."),
    "cowork_layer3_spec_language_sweep.md": (REPORT,
        "A language-mechanical offender sweep applying the ratified writing standards (**D-193**), "
        "named as a worked example by `cowork_design_doc_template.md:19` — which phase 1d read in "
        "full and which is the standards' HOME. Zero ruling-vocabulary hits."),
    "cowork_layer4_spec_review.md": (REPORT,
        "Own header `:6`: “Status: findings only; the rewrite follows once these are agreed.” The "
        "reviewed document, `cowork_layer4_chordsymbol_design.md`, is in THIS session's full-read set, "
        "so the reviewed text is read directly rather than through its review. Zero ruling-vocabulary "
        "hits."),
    "cowork_target_architecture_review.md": (REPORT,
        "`docs/implementation_roadmap.md:4-8` names this document as its source (“part 1 — target "
        "architecture”) and itself as “the single tracker ensuring every review conclusion is "
        "addressed”; that roadmap is LIVE-SPEC and in the full-read set. Its own ruling-vocabulary "
        "hits are citations of decisions recorded elsewhere, not rulings."),
    "cowork_implementation_review.md": (REPORT,
        "`docs/implementation_roadmap.md:4-8` names this document as its source (“part 2 — "
        "as-built”) under the same single-tracker statement. Independently declared “partly stale; "
        "verified at current code” by `cowork_structural_integrity_audit.md:11-12`, which extends it "
        "and is itself LIVE-SPEC in the full-read set. Zero ruling-vocabulary hits."),
    "cowork_key_drift_research_grounding.md": (REPORT,
        "Own header `:5-7`: “It GROUNDS the coming design conversation; it decides and builds "
        "nothing.” Published-fact grounding under principle #1. Its single ruling-vocabulary hit is a "
        "citation of the ratified baselines."),
    "cowork_key_chord_joint_inference_grounding.md": (REPORT,
        "Published-fact grounding for the joint-vs-separable question, FACT/THEORY/CONJECTURE-labelled "
        "(`:6-8`). The decision it grounds is registered — **D-001**, and "
        "`cowork_joint_estimator_architecture.md:5` cites this document as its grounding. Zero "
        "ruling-vocabulary hits."),
    "cowork_functional_analysis_research_grounding.md": (REPORT,
        "Own header `:3-8`: “published-fact grounding (principle #1) … Feeds the Layer 5 engagement "
        "design dispatch”. Zero ruling-vocabulary hits."),
    "cowork_polyphony_phrase_harmony_research.md": (REPORT,
        "Own header `:3-7`: “A durable, cited record of the deep search” in answer to a user "
        "question. Its ruling-vocabulary hits are citations of decisions recorded elsewhere."),
    "cowork_score_census_gt_draft.md": (REPORT,
        "An appendix of `cowork_score_census.md`, which names it at `:5-11` as one of two “full "
        "evidence tables … retained verbatim” with `[verified]`/`[reported]` fact tags. The census "
        "itself is LIVE-SPEC and in the full-read set — it is the home of the fitting-pool licence "
        "constraint §8c that [[OI-271]] turns on. Its two hits are corpus-supersession notes in data "
        "rows."),
    "cowork_score_census_plain_draft.md": (REPORT,
        "The second census appendix, named at `cowork_score_census.md:5-11` on the same terms. One "
        "ruling-vocabulary hit, in a data row."),
    "cowork_mode_key_chord_inference_discussion.md": (REPORT,
        "Own header `:9`: “Nothing here authorizes a build.” Its subject question is SETTLED: "
        "[[OI-43]] ✅ SETTLED 2026-07-12 (the joint step SHELVED on both axes, row CLOSED) and "
        "[[OI-44]] ✅ DECLARED; the shelving is registered as **D-278** (SHELVED WITH EVIDENCE, "
        "ratified 2026-08-02). Its ruling-vocabulary hits are citations of that shelving."),
    "cowork_siloed_facts_audit.md": (REPORT,
        "`OPEN_ITEMS.md:351-355` records, under a user challenge of 2026-07-10, that ALL 17 of this "
        "audit's findings are mapped to register rows, and gives the mapping finding-by-finding "
        "(1→OI-72 … 17→OI-74). One ruling-vocabulary hit."),
    "cowork_corpus_audit.md": (REPORT,
        "Its findings are rowed and assigned: [[OI-57]] carries the surviving half (the extra-scores "
        "registry, ASSIGNED to the corpus-onboarding event [[OI-38]]) and records the other half "
        "superseded by the GT-corpus manifest discipline. Zero ruling-vocabulary hits."),
    "cowork_l1l4_review_note.md": (REPORT,
        "Own header `:5-7`: the docs-and-coherence half of the L1–L4 review, “mechanical status-tidy, "
        "no algorithmic contradiction”, with the one substantive question handed to CC. The gate it "
        "serves, `cowork_l1l4_review_charter.md`, stays LIVE-SPEC. Its single hit is a status "
        "observation."),
    "cowork_product_tool_register.md": (REPORT,
        "Own banner `:3-8`: “Status: RESEARCH NOTE … **Nothing here is commissioned**; product work "
        "is out of scope until the architecture/algorithm/refactoring completion (standing rule).” It "
        "cites that standing rule rather than making one."),
    "cowork_upstream_merge_risk.md": (REPORT,
        "Own banner `:3-7`: “Status: reference … A forward-looking inventory, **not** an active "
        "breakage and **not** a merge”; the git facts are transcribed CC findings and the deferral is "
        "“Cowork's architectural read”, not a ruling. The distribution rules that DO bind are "
        "registered — **D-117**, **D-197**, **D-259**, **D-316**."),
    "cowork_idiom_entry_mapping.md": (REPORT,
        "A data mapping of catalog entries onto the ratified idiom set, declared “**Provisional, easy "
        "to revise**” at `:5`. The taxonomy it implements is the decision, and that lives in "
        "`cowork_style_taxonomy_proposal.md` (RATIFIED 2026-06-30 · EXECUTED), which stays LIVE-SPEC."),
    "docs/phase4_recon.md": (REPORT,
        "A dated read-only reconnaissance (`:3-4`) recommending an implementation shape; the "
        "retirement it scouted has since landed — [[OI-238]]'s resolution records that "
        "`prepareUserFacingHarmonicRegions` no longer exists in the production tree, verified at the "
        "code. Its ruling-vocabulary hits are ordinary prose (“convention”, “retired”, “must not "
        "proceed” inside a quoted dispatch condition)."),
    "docs/phase5_recon.md": (REPORT,
        "A dated read-only reconnaissance (`:3-5`) recommending an implementation shape. Its four "
        "hits are all the word “convention” used of an engraving text format."),
    "docs/divergence_d_recon.md": (REPORT,
        "A dated read-only recon with an audience of “next session planning Phase 3c-impl” (`:3-5`). "
        "Zero ruling-vocabulary hits."),
    "docs/three_paths_divergence_recon.md": (REPORT,
        "A dated read-only recon of one chord's three readings (`:3-6`). Its hits are the word "
        "“policy” used of a display sort order, with the fix left as stated options, not a choice."),
    "docs/musescore_parser_special_notations_recon.md": (REPORT,
        "A dated read-only recon (`:3-4`) reporting which catalog entries MuseScore's parser accepts. "
        "Zero hits on the ruling half of the vocabulary."),
    "docs/policy2_coalescing_map.md": (REPORT,
        "A dated read-only divergence map (`:3-4`). Its hits are the word “retired” recording that "
        "the Jazz path was retired — which is itself registered as **D-067** (Jazz mode retired, LIVE, "
        "home `ARCHITECTURE.md`)."),
    "docs/mismatch_classification.md": (REPORT,
        "A dated classification of one test run's 135 mismatches (`:3-5`), all from one synthetic "
        "catalog score. Its hits are the words “policy” and “convention”, used to pose OPEN "
        "annotation questions, not to answer them; the governing answer is registered — **D-304** "
        "(the analyzer always emits its fullest reading; simplifying happens only when comparing "
        "against a corpus). Flagged for the user: if the catalog's own annotation policy is still "
        "considered open, this document is where the question is stated."),
    "docs/format_symbol_audit.md": (REPORT,
        "A dated read-only per-branch audit (`:3-5`). Its findings are tracked outside it — the "
        "F1–F5 pattern history is a project memory, and `docs/scoring_model.md` (in the full-read "
        "set) is the formatter's standing home. One ruling-vocabulary hit."),
    "docs/duplication_audit.md": (REPORT,
        "A dated read-only audit (`:1-10`) of duplication across the analysis pipeline. Zero "
        "ruling-vocabulary hits; the standing rule it measures against is registered (**D-073**, "
        "single implementation for shared logic; principle #6)."),
    "docs/quality_observations_iter76.md": (REPORT,
        "A record of a user's visual inspection of four snapshot scores (`:3-6`) — observations "
        "against ground truth, not decisions. One ruling-vocabulary hit."),
    "docs/perf_p3_baseline.md": (REPORT,
        "A dated measurement-only baseline (`:3-5`, “Measurement-only; zero production-code "
        "changes”). Superseded in substance by the 2026-07-28 analysis-cost profile and its rows "
        "[[OI-203]]/[[OI-215]]/[[OI-216]]/[[OI-217]]. Zero ruling-vocabulary hits."),
    "docs/iter97_delta_characterization.md": (REPORT,
        "“Read-only data report. No source changes were made” (`:3`), generated against a named "
        "iteration-era baseline. Zero ruling-vocabulary hits."),
    "docs/iter97_bir_false_categorization.md": (REPORT,
        "“Read-only data report. No source changes were made” (`:3`); a per-case extraction against "
        "an iteration-era baseline, and the gate it categorizes is the batch stop, which "
        "`CLAUDE.md` block (C) records as SUPERSEDED at R10-b. One ruling-vocabulary hit."),
    "docs/rfc_musescore_forum_post.md": (REPORT,
        "“Draft for Vincent's review. **Not posted.**” (`:3-4`) — outward-facing copy, not a "
        "specification. Zero ruling-vocabulary hits."),
    "docs/chordlist_bug_report.md": (REPORT,
        "An upstream bug-report draft for the chord-symbol parser fix. Its disposition is RULED and "
        "registered: [[OI-273]] ✅ RULED (user, 2026-08-02, option (i)) and **D-316** records the "
        "patch as a local patch with an UPSTREAMABLE distribution disposition. Zero "
        "ruling-vocabulary hits."),
    "docs/llm_triage_design.md": (REPORT,
        "“Status: Discussion only. No implementation committed. This document captures a design "
        "conversation … preserved so future planning sessions can pick up the shared context” "
        "(`:3-6`). Its governing question is RULED and registered — [[OI-56]] ✅ DECIDED "
        "2026-07-13 (a HUMAN acts as ground truth; the judge as guidance, never a grader) = **D-205**; "
        "its one “must not” (`:106`) restates **D-294**."),
}

# Short reasons for the LIVE-SPEC rows.  Not verifications (none is owed) — the banner
# or opening statement that keeps each document in the reading set.
LIVE_REASON: dict[str, str] = {
    "cowork_layer4_chordsymbol_design.md": "Signed Layer-4 specification; the dispatch's own full-read set. READ IN FULL this session.",
    "cowork_layer5_function_design.md": "Signed Layer-5 specification; the dispatch's own full-read set. READ IN FULL this session.",
    "docs/decoder_design.md": "The decoder design; the dispatch's own full-read set. READ IN FULL this session.",
    "docs/scoring_model.md": "The authoritative scoring reference, a mandatory read for scoring sessions (`CLAUDE.md`) and the home of D-214…D-224. READ IN FULL this session.",
    "docs/redesign_plan.md": "The layered-evidence architecture plan; the dispatch's own full-read set. READ IN FULL this session.",
    "cowork_layer3_keymode_design.md": "Banner: SIGNED (user, 2026-06-22), WIRED — AS-BUILT Step 1, with named deferred follow-ups.",
    "cowork_score_census.md": "Banner: v1 DELIVERED, for user disposition of the acquisition tiers. §8c is the HOME of the fitting-pool licence constraint that [[OI-271]] turns on.",
    "cowork_joint_key_chord_design.md": "Shelved by ratification (D-278) but retained as the architecture record; the design content itself — where the step lives, how key and chord couple — is registered nowhere.",
    "cowork_layer5_engagement_design.md": "A design pass (CC, 2026-07-07) whose downstream owner-decisions are enumerated for follow-on passes; the engage-era agenda's fate is itself unrecorded ([[OI-259]]).",
    "cowork_structural_integrity_audit.md": "A grounded catalogue that QUEUES named refactors as later user-ratified events; the queue is live.",
    "cowork_voiceleading_axis_design.md": "Banner: AS-BUILT + SIGNED (user, 2026-07-03), asks A1–A8 ratified.",
    "cowork_progression_schema_dictionary.md": "A component specification with a §0 terms table; the Harmonic Vocabulary's own home (D-133).",
    "docs/implementation_roadmap.md": "The single tracker for every review conclusion, with two DO-NOT-FORGET structural refactors under a user mandate.",
    "cowork_notation_adoption_increment.md": "Banner: ★ USER-RATIFIED 2026-07-26, five recommendations adopted.",
    "cowork_phrase_boundary_design.md": "Banner: SIGNED (user, 2026-06-26), rev. 3.",
    "docs/key_path_design.md": "A ratification-gated design; its banner says UNCOMMITTED while the file is tracked — itself worth a reader.",
    "cowork_progression_schema_design.md": "Banner: ★ FULLY RATIFIED (user, 2026-07-02) — D5, D6, §4.5, §4.6.",
    "cowork_fb_redesign_design.md": "A design plus an explicit decision surface for a separately-ratified build event.",
    "cowork_idiom_discovery_design.md": "A design specification with a ratified extraction-tooling decision (D6) and resolved open items.",
    "cowork_layer1_note_model_design.md": "Banner: AS-BUILT — the Layer-1 specification.",
    "cowork_layer2_slicing_design.md": "Banner: AS-BUILT — the Layer-2 specification.",
    "cowork_target_architecture.md": "Demoted to detailed design and rationale, but explicitly retains the FULL statements of the contracts that `ARCHITECTURE.md` only summarises — a partial supersession, not a total one.",
    "docs/score_inventory.md": "A mandatory read for any score-touching task (`CLAUDE.md`, Score corpora) with hard rules of its own.",
    "cowork_census_full_needs_audit.md": "Banner: ★ DISPOSED (user, 2026-07-04) — four §6-C rulings (N18/N19 ADOPTED, N15 RATIFIED, N20 as its own needs row).",
    "cowork_phase2_architecture_review.md": "Carries the user's sequencing gate of 2026-06-17 (structural fixes before inference) and produces the architecture-fix order.",
    "docs/llm_integration.md": "The language-model design; its decisions are registered (D-139…D-143) but all DEFERRED, and the document is their detail.",
    "cowork_l1l3_stabilization_plan.md": "Carries the user-ratified ordering principle of 2026-06-25 (build-it-right before tune-precision) and the per-step gates.",
    "docs/layer_architecture_audit.md": "Claims supersession for LAYER 1 ONLY; the rest of the intended-vs-actual layer discussion carries no successor claim.",
    "cowork_evidence_inventory.md": "The live catalog of every hint each layer finds, with standing obligations at [[OI-146]].",
    "cowork_gateA_unification_design.md": "Explicitly “the ratification surface” for a separate user-ratified build event.",
    "cowork_layer3_reachback_design.md": "Banner: BUILT (capability, gated OFF); records the resolved build-decision form.",
    "cowork_layer5_function_methods.md": "`:33` ★ DECIDED (user, 2026-06-26) — output the Roman numeral; T/S/D is a derived read-out only.",
    "cowork_layer6_grouping_design.md": "Banner: AS-BUILT (2026-07-02) with a §5.1-a interpretation RULED at ratification.",
    "cowork_sensitive_cell_probe.md": "Banner: ★ USER-RATIFIED 2026-07-19 — options 1a, 2a, 3a, with two sharpenings.",
    "cowork_term_theory_grounding.md": "Its header says it decides nothing, but `:330-351` carry FIVE design decisions marked ✅ DECIDED 2026-07-19 and “ratified as of 2026-07-19”. The mechanical check caught this; the header is misleading.",
    "docs/stage4b_design.md": "A ratification-gated design carrying the user's choice of the staged demote-first approach (2026-06-14).",
    "cowork_architecture_review_2026_07.md": "Banner: AMENDMENTS A-1…A-10 RATIFIED (user, 2026-07-02) plus a ratified corpus expansion.",
    "cowork_l1l4_completion_ledger.md": "Banner: ★ L1–L4 COMPLETE — SIGN-OFF, with the residuals it defers by name.",
    "cowork_union_search_record.md": "Banner: ★ DISPOSED (user, 2026-07-04) — five approvals including a ratified negative ruling (N13).",
    "docs/back_half_design.md": "A design ready for user ratification whose §4 redirect is cited as ratified by two downstream stage designs.",
    "docs/unified_analysis_pipeline.md": "Records live design divergences by name (“A remains by design; C parked”) and a deferred Phase 4c.",
    "docs/layer_audit_plan.md": "Carries the user's NORTH STAR of 2026-06-17 and defines the obligation-map output.",
    "docs/precision_metric_design.md": "A design-and-scoping deliverable for the ratification gate that precedes building any metric.",
    "cowork_factorization_desk_simulation.md": "Banner: ★ USER-RATIFIED 2026-07-19 — the §7 asks granted in full.",
    "cowork_joint_estimator_architecture.md": "The GOVERNING architecture decision (user-ratified 2026-07-14/17), named as such at `OPEN_ITEMS.md:15-18`.",
    "cowork_l1l4_architecture_audit.md": "A resolution-updated audit with still-open migration debt scheduled for a later engagement.",
    "cowork_style_taxonomy_proposal.md": "Banner: RATIFIED (2026-06-30) · EXECUTED — and in possible tension with D-132, which records empirical grounding as future work.",
    "cowork_audit_obligation_map.md": "Re-assessed 2026-06-20 — the supersession is explicitly PARTIAL (“supersedes parts of §B/§C/§E”).",
    "cowork_delta_check_dispositions.md": "Records proper-layer DISPOSITIONS verified at source plus the L4 build backlog.",
    "cowork_eg2_scoping.md": "The premise ledger of an OPEN gate row ([[OI-3]] — decision with the user).",
    "cowork_information_loss_audit.md": "A live catalogue of information-loss sites, each fix its own later ratified event.",
    "cowork_layer1_tone_collection_design.md": "The pre-rebuild Layer-1 design; no supersession is claimed in it, though Layer 1 was later rebuilt as the note model.",
    "cowork_phrase_boundary_methods.md": "`:8` ★ Proportionality (user-ratified 2026-06-26) — a ruling of its own.",
    "docs/stage4c_cadence_key_design.md": "A ratification-gated design resting on two named measured results.",
    "docs/symbol_input_audit.md": "`:37` and `:330` record OPEN user decisions (“Tool-side input uses requiring user decision: 2”).",
    "cowork_adjudication_dossier.md": "Banner: RATIFIED by the user 2026-07-10 — including the one genuine acceptance (A3).",
    "cowork_joint_estimator_factorization.md": "Banner: ★ USER-RATIFIED 2026-07-19 — the governing structure of the production estimator.",
    "cowork_layer1_extend_design.md": "A DRAFT for sign-off implementing the supplier side of the bounded-context contract.",
    "cowork_phase5c_l5_build_plan.md": "A build plan with a non-negotiable per-step method and per-step gates.",
    "cowork_tpc_capability_design.md": "Banner: BUILT (capability-only, no production consumer) — a declared dormancy.",
    "cowork_uncertain_resolver_investigation.md": "Banner: RESOLVED — user-ratified 2026-06-24; a ruling of its own.",
    "docs/key_detection_baroque_partial_signature.md": "Documents the partial-signature correction that is still live at the code ([[OI-98]] names it).",
    "cowork_l1_l5_premise_debt_audit.md": "The retroactive #17 ledger for built code; three tiers of premise debt, several still open.",
    "cowork_phase5b_l4_build_plan.md": "A build plan with a non-negotiable per-step method.",
    "cowork_style_clustering_plan.md": "Banner: committed future direction, user-ratified 2026-06-29.",
    "docs/architecture_joint_inference.md": "An architecture direction, investigation-confirmed and “ratifiable”, with no recorded supersession banner.",
    "docs/iter92_joint_bass_chord_scoring.md": "“Remains the authoritative reference for the JOINT formula and its guards”; D-224 is registered against it.",
    "docs/nct_detection_design.md": "The deferred non-chord-tone design; D-303 constrains its eventual shape and it is load-bearing at [[OI-55]]/[[OI-68]].",
    "docs/stage4d_local_modulation_design.md": "A ratification-gated design resting on named measured results.",
    "cowork_audit_protocol.md": "The HOME of registered decisions D-208, D-209, D-250, D-251, D-252.",
    "cowork_l1l4_review_charter.md": "The user-mandated review gate with its two aims stated as requirements.",
    "docs/iter90_bass_as_root_promotion_shelved.md": "A shelving with a standing prohibition at `:95` (“Do not pursue this as a chord-analyzer-local gate”). **D-302** covers the neighbouring inversion class and its recorded defense names the bass-as-root triad default — but not this prohibition verbatim, so the doubt keeps it IN.",
    "cowork_idiom_discovery_findings.md": "The empirical basis of the ratified idiom set, and the point where that ratification and D-132 (empirical grounding as future work) may not agree.",
    "cowork_layer2_reslice_design.md": "Banner: BUILT; records the §5 build-time decision that was taken.",
    "cowork_layer3_keymode_impl_design.md": "Pins the Layer-3 implementation decisions increment by increment.",
    "cowork_types_header_design.md": "Banner: BUILT / AS-BUILT with the D1/D2 and leaf-location decisions recorded.",
    "docs/extension_stripping_policy.md": "“Direction settled” — a stated policy with no register entry found for it.",
    "cowork_eg1_premise_checks.md": "Premise checks feeding an OPEN gate row; design decisions enumerated and assigned to owning layers.",
    "cowork_gate_policy_amendment.md": "The founding provenance of the two-tier gate policy now in `CLAUDE.md` block (B) — registered D-191; the document carries the derivation.",
    "cowork_key_mode_inference_diagnosis.md": "A Premise-Gate diagnosis opening whose row [[OI-141]] is still OPEN.",
}


def surface_of(path: str) -> str | None:
    p = path.replace("\\", "/")
    if p.startswith("docs/"):
        return "docs"
    if p.startswith("cowork_") and p.endswith(".md") and p not in (
            "cowork_handoff.md", "cowork_handoff_archive.md"):
        return "cowork"
    return None


def derive_unread() -> dict[str, int]:
    clusters = json.load(open(CLUSTERS, encoding="utf-8"))["clusters"]
    by_id = {c["cluster_id"]: c for c in clusters}
    dispos = json.load(open(DISPOS, encoding="utf-8"))["dispositions"]
    counts: collections.Counter = collections.Counter()
    for d in dispos:
        if d["disposition"] != "unresolved":
            continue
        cl = by_id[d["cluster_id"]]
        files = cl["files"] or [cl["proposed_representative"]["file"]]
        surfaces = {surface_of(f) for f in files}
        if None in surfaces or len(surfaces) > 1:
            continue                       # the manifest's own mixed-sources bucket
        for f in set(files):
            counts[f] += 1
    read = set(PHASE1D_READ) | set(PHASE1F_READ)
    missing = read - set(counts)
    if missing:
        raise SystemExit(f"read-set file(s) absent from the derived surface: {sorted(missing)}")
    return {f: n for f, n in counts.items() if f not in read}, len(counts), read


def build(unread: dict[str, int], surface_total: int, read: set) -> str:
    unknown = sorted(set(unread) - set(CLASSIFICATION) - set(LIVE_REASON))
    if unknown:
        raise SystemExit(f"unclassified file(s): {unknown}")
    stale = sorted((set(CLASSIFICATION) | set(LIVE_REASON)) - set(unread))
    if stale:
        raise SystemExit(f"classification rows for file(s) not in the unread set: {stale}")
    both = sorted(set(CLASSIFICATION) & set(LIVE_REASON))
    if both:
        raise SystemExit(f"file(s) carry a class AND a live-reason row: {both}")

    def cls(f):
        return CLASSIFICATION[f][0] if f in CLASSIFICATION else LIVE
    def note(f):
        return CLASSIFICATION[f][1] if f in CLASSIFICATION else LIVE_REASON.get(f, "")

    order = sorted(unread, key=lambda f: (-unread[f], f))
    by_class = collections.Counter(cls(f) for f in order)
    clusters_by_class: collections.Counter = collections.Counter()
    for f in order:
        clusters_by_class[cls(f)] += unread[f]

    live_files = [f for f in order if cls(f) == LIVE]
    excl_files = [f for f in order if cls(f) != LIVE]
    live_bytes = sum(os.path.getsize(os.path.join(ROOT, f)) for f in live_files)
    excl_bytes = sum(os.path.getsize(os.path.join(ROOT, f)) for f in excl_files)
    task2_bytes = sum(os.path.getsize(os.path.join(ROOT, f)) for f in TASK2_FULL_READ)
    rest_bytes = live_bytes - task2_bytes

    L = []
    A = L.append
    A("# Phase 1g — the triage of the unread design documents")
    A("")
    A("> **GENERATED FILE — do not hand-edit.** Generator "
      "`tools/audit/decisions/gen_phase1g_triage.py`; sources "
      "`decision_clusters.json` + `cluster_dispositions.json`. Every count below is "
      "computed from those artifacts at generation time; only the class and the "
      "verification prose are authored, and they live in the generator (#17f).")
    A(">")
    A("> **What this is.** The user's decision surface for an exclusion list. Phase 1's "
      "end state is the unread design-document population at zero **or** an explicit, "
      "user-accepted exclusion list. An exclusion list built on unread contents would be "
      "the blind sweep the guardrails forbid, so every proposed exclusion here is "
      "defended per file, by established supersession or established class — never by "
      "guess.")
    A(">")
    A("> **What this is NOT.** No document's status banner is edited by this pass. "
      "Classifying is not bannering. Nothing here is a ratification, and nothing here "
      "closes a register row.")
    A(">")
    A("> **★ THE EXCLUSION LIST IS ACCEPTED — the user, 2026-08-02, all 41 as tabled.** "
      "Recorded at `open_items/OI-207.md` (the dated note of that date), which states the "
      "acceptance covers exactly the 41 documents proposed for exclusion below, each with "
      "its per-file verification citation: 1 SUPERSEDED-ESTABLISHED, 1 EVIDENCE-FROZEN "
      "(its decision registered as **D-286**, and flagged as remaining the evidence base "
      "of the OPEN extent question [[OI-210]] — excluded from the DECISION read, not "
      "withdrawn from phase 3), and 39 REPORT/NARRATIVE in six evidenced families. "
      "**Phase 1's completion basis is therefore: the 80 LIVE-SPEC documents read IN FULL, "
      "plus this accepted 41-document exclusion.** What was accepted is the DOCUMENT LIST, "
      "not the cluster counts beside it: every count here is recomputed at each generation "
      "and falls as documents are read, because reading a design document in full resolves "
      "some of its clusters into register entries. A count that has moved is therefore not "
      "an amendment to what the user accepted.")
    A("")
    A("## The population, derived")
    A("")
    A(f"| | Count |")
    A("|---|---|")
    A(f"| Design documents owning at least one unresolved cluster | **{surface_total}** |")
    A(f"| — read IN FULL by the phase-1d and phase-1f waves (distinct) | {len(read)} |")
    A(f"| — **unread, and classified below** | **{len(unread)}** |")
    A(f"| Unresolved cluster attributions held by the unread set | {sum(unread.values())} |")
    A("")
    A("### ★ A correction of record: the unread population is 121, not 120")
    A("")
    A("`open_items/OI-207.md` (the phase-1f dated note), `STATUS.md`, `DECISIONS.md` and "
      "`disposition_manifest.json` all record **23 read in full — 21 by phase 1d, plus "
      "`cowork_stage5_fitter_design.md` and `docs/beam_widening_design.md` by phase 1f — "
      "and 120 unread**. `docs/beam_widening_design.md` is in **both** lists: it is row 1 "
      "of the phase-1d Task-1 read-in-full table "
      "(`cc_phase1d_enumeration_wave_report.md:77`) and it is in the phase-1f note's own "
      "what-was-read table (`open_items/OI-207.md:559`). The DISTINCT read count is "
      f"therefore **{len(read)}**, and the unread population is **{len(unread)}**.")
    A("")
    A("The commit that produced the 23/120 figures (`40739f38ba`) was itself a "
      "self-check correction of three other conflations in the same numbers; this "
      "double-count survived it. Nothing else depends on the figure — no disposition, "
      "no cluster count, no register entry moves — but the reading list does, so it is "
      "corrected here and rowed.")
    A("")
    A("## The classes, and how each was decided")
    A("")
    A("- **LIVE-SPEC** — standing force. **The DEFAULT: a document is LIVE-SPEC unless "
      "established otherwise.** Doubt keeps it IN the reading set (#19's direction of "
      "caution).")
    A("- **SUPERSEDED-ESTABLISHED** — the document claims supersession AND the claim is "
      "verified: the named successor exists, is registered, and covers the subject. An "
      "unverifiable claim → LIVE-SPEC.")
    A("- **REPORT/NARRATIVE** — a delivered-work report or session narrative with no "
      "specification force of its own. Any ruling of its own disqualifies it → LIVE-SPEC.")
    A("- **EVIDENCE-FROZEN** — a committed measurement document whose shelvings or "
      "falsifications are already registered; the rest is data.")
    A("")
    A("**The mechanical half of the test.** Classifying by banner alone would rest on "
      "what a document says about itself. Every candidate for a non-LIVE-SPEC class was "
      "additionally swept for the **ruling vocabulary the disposition manifest "
      "publishes** (`disposition_manifest.json`, "
      "`ruling_vocabulary_exempting_BR11_BR12_BR13` — the same list BR-11/BR-12/BR-13 "
      "use to hold a unit back for a reader), and every hit was read to decide whether "
      "it is the document's OWN ruling or a citation of one recorded elsewhere. A hit "
      "that is the document's own ruling returns it to LIVE-SPEC.")
    A("")
    A("**It changed the answer twice, which is why it was run.** "
      "`cowork_term_theory_grounding.md` opens “Nothing here decides anything” and "
      "carries five decisions marked ✅ DECIDED 2026-07-19 at `:330-351`; "
      "`cowork_layer5_function_methods.md` presents itself as a methods catalog and "
      "carries ★ DECIDED (user, 2026-06-26) at `:33`. Both are LIVE-SPEC.")
    A("")
    A("## The result")
    A("")
    A("| Class | Documents | Unresolved clusters | Proposed disposition |")
    A("|---|---|---|---|")
    for k in (LIVE, REPORT, SUPERSEDED, EVIDENCE):
        disp = "READ IN FULL" if k == LIVE else "EXCLUDE"
        A(f"| {k} | **{by_class.get(k, 0)}** | {clusters_by_class.get(k, 0)} | {disp} |")
    A(f"| **total** | **{len(order)}** | **{sum(unread.values())}** | |")
    A("")
    A(f"**Proposed EXCLUDE: {len(excl_files)} documents / "
      f"{sum(unread[f] for f in excl_files)} clusters / "
      f"{excl_bytes/1048576:.2f} MB (≈{excl_bytes/CHARS_PER_TOKEN/1000:.0f}k tokens).**")
    A(f"**Remaining full-read set: {len(live_files)} documents / "
      f"{sum(unread[f] for f in live_files)} clusters / "
      f"{live_bytes/1048576:.2f} MB (≈{live_bytes/CHARS_PER_TOKEN/1000:.0f}k tokens)** — of "
      f"which the five this session reads in full are {task2_bytes/1048576:.2f} MB "
      f"(≈{task2_bytes/CHARS_PER_TOKEN/1000:.0f}k tokens), leaving "
      f"{rest_bytes/1048576:.2f} MB (≈{rest_bytes/CHARS_PER_TOKEN/1000:.0f}k tokens) "
      f"across {len(live_files) - len(TASK2_FULL_READ)} documents.")
    A("")
    A("*(Token estimates use the 3.04 characters-per-token ratio phase 1d measured on "
      "this repository's own prose against the Read tool's accounting, and phase 1f "
      "re-used unchanged.)*")
    A("")
    A("## The table — all "
      f"{len(order)} unread design documents")
    A("")
    A("Ordered by unresolved cluster count, the priority map the manifest gives. "
      "“Verification” is mandatory for SUPERSEDED-ESTABLISHED and EVIDENCE-FROZEN; this "
      "pass supplies one for every REPORT/NARRATIVE too, because each of those is a "
      "proposed exclusion. For LIVE-SPEC the column gives the banner or opening "
      "statement that keeps the document in the set.")
    A("")
    A("| # | Document | Clusters | Class | Verification / reason | Disposition |")
    A("|---|---|---|---|---|---|")
    for i, f in enumerate(order, 1):
        k = cls(f)
        disp = "READ IN FULL" if k == LIVE else "**EXCLUDE**"
        A(f"| {i} | `{f}` | {unread[f]} | {k} | {note(f)} | {disp} |")
    A("")
    A("## Provenance")
    A("")
    A("- Derived from `tools/audit/decisions/decision_clusters.json` and "
      "`tools/audit/decisions/cluster_dispositions.json` at the commit this file is "
      "committed in.")
    A("- The read set: `cc_phase1d_enumeration_wave_report.md` Task 1 (21 documents) and "
      "`open_items/OI-207.md` phase-1f dated note (2 documents, one of them a repeat).")
    A("- Dispatch: `cc_instruction_phase1g_triage.md`, Task 1. Author: CC, 2026-08-02.")
    A("- Nothing in this file is a ratification of a DECISION. The exclusion list was a "
      "proposal when this file was first generated and is now ACCEPTED (the user, "
      "2026-08-02, all 41 as tabled — `open_items/OI-207.md`); the classification of the "
      "80 LIVE-SPEC documents carries no such acceptance and needs none, since its "
      "disposition is to read them.")
    A("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate and report drift instead of writing")
    args = ap.parse_args()
    os.chdir(ROOT)
    unread, surface_total, read = derive_unread()
    text = build(unread, surface_total, read)
    if args.check:
        if not os.path.exists(OUT):
            print("MISSING:", OUT)
            return 1
        # Read in text mode, as the sibling register generator does (#6): universal
        # newlines make the comparison independent of the checkout's line-ending
        # configuration, which is the OI-195 lesson applied to a drift guard.
        cur = open(OUT, encoding="utf-8").read()
        if cur != text:
            print("DRIFT: phase1g_triage.md differs from a fresh generation")
            return 1
        print("OK: phase1g_triage.md reproduces from the data")
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {OUT}: {len(unread)} rows, "
          f"{sum(unread.values())} unresolved cluster attributions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
