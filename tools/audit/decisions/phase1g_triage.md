# Phase 1g — the triage of the unread design documents

> **GENERATED FILE — do not hand-edit.** Generator `tools/audit/decisions/gen_phase1g_triage.py`; sources `decision_clusters.json` + `cluster_dispositions.json`. Every count below is computed from those artifacts at generation time; only the class and the verification prose are authored, and they live in the generator (#17f).
>
> **What this is.** The user's decision surface for an exclusion list. Phase 1's end state is the unread design-document population at zero **or** an explicit, user-accepted exclusion list. An exclusion list built on unread contents would be the blind sweep the guardrails forbid, so every proposed exclusion here is defended per file, by established supersession or established class — never by guess.
>
> **What this is NOT.** No document's status banner is edited by this pass. Classifying is not bannering. Nothing here is a ratification, and nothing here closes a register row.
>
> **★ THE EXCLUSION LIST IS ACCEPTED — the user, 2026-08-02, all 41 as tabled.** Recorded at `open_items/OI-207.md` (the dated note of that date), which states the acceptance covers exactly the 41 documents proposed for exclusion below, each with its per-file verification citation: 1 SUPERSEDED-ESTABLISHED, 1 EVIDENCE-FROZEN (its decision registered as **D-286**, and flagged as remaining the evidence base of the OPEN extent question [[OI-210]] — excluded from the DECISION read, not withdrawn from phase 3), and 39 REPORT/NARRATIVE in six evidenced families. **Phase 1's completion basis is therefore: the 80 LIVE-SPEC documents read IN FULL, plus this accepted 41-document exclusion.** What was accepted is the DOCUMENT LIST, not the cluster counts beside it: every count here is recomputed at each generation and falls as documents are read, because reading a design document in full resolves some of its clusters into register entries. A count that has moved is therefore not an amendment to what the user accepted.

## The population, derived

| | Count |
|---|---|
| Design documents owning at least one unresolved cluster | **143** |
| — read IN FULL by the phase-1d and phase-1f waves (distinct) | 22 |
| — **unread, and classified below** | **121** |
| Unresolved cluster attributions held by the unread set | 994 |

### ★ A correction of record: the unread population is 121, not 120

`open_items/OI-207.md` (the phase-1f dated note), `STATUS.md`, `DECISIONS.md` and `disposition_manifest.json` all record **23 read in full — 21 by phase 1d, plus `cowork_stage5_fitter_design.md` and `docs/beam_widening_design.md` by phase 1f — and 120 unread**. `docs/beam_widening_design.md` is in **both** lists: it is row 1 of the phase-1d Task-1 read-in-full table (`cc_phase1d_enumeration_wave_report.md:77`) and it is in the phase-1f note's own what-was-read table (`open_items/OI-207.md:559`). The DISTINCT read count is therefore **22**, and the unread population is **121**.

The commit that produced the 23/120 figures (`40739f38ba`) was itself a self-check correction of three other conflations in the same numbers; this double-count survived it. Nothing else depends on the figure — no disposition, no cluster count, no register entry moves — but the reading list does, so it is corrected here and rowed.

## The classes, and how each was decided

- **LIVE-SPEC** — standing force. **The DEFAULT: a document is LIVE-SPEC unless established otherwise.** Doubt keeps it IN the reading set (#19's direction of caution).
- **SUPERSEDED-ESTABLISHED** — the document claims supersession AND the claim is verified: the named successor exists, is registered, and covers the subject. An unverifiable claim → LIVE-SPEC.
- **REPORT/NARRATIVE** — a delivered-work report or session narrative with no specification force of its own. Any ruling of its own disqualifies it → LIVE-SPEC.
- **EVIDENCE-FROZEN** — a committed measurement document whose shelvings or falsifications are already registered; the rest is data.

**The mechanical half of the test.** Classifying by banner alone would rest on what a document says about itself. Every candidate for a non-LIVE-SPEC class was additionally swept for the **ruling vocabulary the disposition manifest publishes** (`disposition_manifest.json`, `ruling_vocabulary_exempting_BR11_BR12_BR13` — the same list BR-11/BR-12/BR-13 use to hold a unit back for a reader), and every hit was read to decide whether it is the document's OWN ruling or a citation of one recorded elsewhere. A hit that is the document's own ruling returns it to LIVE-SPEC.

**It changed the answer twice, which is why it was run.** `cowork_term_theory_grounding.md` opens “Nothing here decides anything” and carries five decisions marked ✅ DECIDED 2026-07-19 at `:330-351`; `cowork_layer5_function_methods.md` presents itself as a methods catalog and carries ★ DECIDED (user, 2026-06-26) at `:33`. Both are LIVE-SPEC.

## The result

| Class | Documents | Unresolved clusters | Proposed disposition |
|---|---|---|---|
| LIVE-SPEC | **80** | 826 | READ IN FULL |
| REPORT/NARRATIVE | **39** | 164 | EXCLUDE |
| SUPERSEDED-ESTABLISHED | **1** | 2 | EXCLUDE |
| EVIDENCE-FROZEN | **1** | 2 | EXCLUDE |
| **total** | **121** | **994** | |

**Proposed EXCLUDE: 41 documents / 168 clusters / 0.54 MB (≈187k tokens).**
**Remaining full-read set: 80 documents / 826 clusters / 1.80 MB (≈621k tokens)** — of which the five this session reads in full are 0.31 MB (≈108k tokens), leaving 1.49 MB (≈513k tokens) across 75 documents.

*(Token estimates use the 3.04 characters-per-token ratio phase 1d measured on this repository's own prose against the Read tool's accounting, and phase 1f re-used unchanged.)*

## The table — all 121 unread design documents

Ordered by unresolved cluster count, the priority map the manifest gives. “Verification” is mandatory for SUPERSEDED-ESTABLISHED and EVIDENCE-FROZEN; this pass supplies one for every REPORT/NARRATIVE too, because each of those is a proposed exclusion. For LIVE-SPEC the column gives the banner or opening statement that keeps the document in the set.

| # | Document | Clusters | Class | Verification / reason | Disposition |
|---|---|---|---|---|---|
| 1 | `cowork_layer4_chordsymbol_design.md` | 38 | LIVE-SPEC | Signed Layer-4 specification; the dispatch's own full-read set. READ IN FULL this session. | READ IN FULL |
| 2 | `cowork_layer5_function_design.md` | 35 | LIVE-SPEC | Signed Layer-5 specification; the dispatch's own full-read set. READ IN FULL this session. | READ IN FULL |
| 3 | `docs/scoring_model.md` | 35 | LIVE-SPEC | The authoritative scoring reference, a mandatory read for scoring sessions (`CLAUDE.md`) and the home of D-214…D-224. READ IN FULL this session. | READ IN FULL |
| 4 | `docs/decoder_design.md` | 33 | LIVE-SPEC | The decoder design; the dispatch's own full-read set. READ IN FULL this session. | READ IN FULL |
| 5 | `docs/redesign_plan.md` | 23 | LIVE-SPEC | The layered-evidence architecture plan; the dispatch's own full-read set. READ IN FULL this session. | READ IN FULL |
| 6 | `cowork_structural_integrity_audit.md` | 20 | LIVE-SPEC | A grounded catalogue that QUEUES named refactors as later user-ratified events; the queue is live. | READ IN FULL |
| 7 | `cowork_layer3_keymode_design.md` | 19 | LIVE-SPEC | Banner: SIGNED (user, 2026-06-22), WIRED — AS-BUILT Step 1, with named deferred follow-ups. | READ IN FULL |
| 8 | `cowork_progression_schema_dictionary.md` | 19 | LIVE-SPEC | A component specification with a §0 terms table; the Harmonic Vocabulary's own home (D-133). | READ IN FULL |
| 9 | `cowork_joint_key_chord_design.md` | 18 | LIVE-SPEC | Shelved by ratification (D-278) but retained as the architecture record; the design content itself — where the step lives, how key and chord couple — is registered nowhere. | READ IN FULL |
| 10 | `cowork_layer5_engagement_design.md` | 18 | LIVE-SPEC | A design pass (CC, 2026-07-07) whose downstream owner-decisions are enumerated for follow-on passes; the engage-era agenda's fate is itself unrecorded ([[OI-259]]). | READ IN FULL |
| 11 | `cowork_voiceleading_axis_design.md` | 18 | LIVE-SPEC | Banner: AS-BUILT + SIGNED (user, 2026-07-03), asks A1–A8 ratified. | READ IN FULL |
| 12 | `docs/implementation_roadmap.md` | 18 | LIVE-SPEC | The single tracker for every review conclusion, with two DO-NOT-FORGET structural refactors under a user mandate. | READ IN FULL |
| 13 | `cowork_notation_adoption_increment.md` | 17 | LIVE-SPEC | Banner: ★ USER-RATIFIED 2026-07-26, five recommendations adopted. | READ IN FULL |
| 14 | `cowork_phrase_boundary_design.md` | 17 | LIVE-SPEC | Banner: SIGNED (user, 2026-06-26), rev. 3. | READ IN FULL |
| 15 | `docs/key_path_design.md` | 17 | LIVE-SPEC | A ratification-gated design; its banner says UNCOMMITTED while the file is tracked — itself worth a reader. | READ IN FULL |
| 16 | `cowork_progression_schema_design.md` | 16 | LIVE-SPEC | Banner: ★ FULLY RATIFIED (user, 2026-07-02) — D5, D6, §4.5, §4.6. | READ IN FULL |
| 17 | `cowork_score_census.md` | 16 | LIVE-SPEC | Banner: v1 DELIVERED, for user disposition of the acquisition tiers. §8c is the HOME of the fitting-pool licence constraint that [[OI-271]] turns on. | READ IN FULL |
| 18 | `cowork_fb_redesign_design.md` | 15 | LIVE-SPEC | A design plus an explicit decision surface for a separately-ratified build event. | READ IN FULL |
| 19 | `cowork_idiom_discovery_design.md` | 15 | LIVE-SPEC | A design specification with a ratified extraction-tooling decision (D6) and resolved open items. | READ IN FULL |
| 20 | `cowork_layer1_note_model_design.md` | 15 | LIVE-SPEC | Banner: AS-BUILT — the Layer-1 specification. | READ IN FULL |
| 21 | `cowork_layer2_slicing_design.md` | 14 | LIVE-SPEC | Banner: AS-BUILT — the Layer-2 specification. | READ IN FULL |
| 22 | `cowork_target_architecture.md` | 14 | LIVE-SPEC | Demoted to detailed design and rationale, but explicitly retains the FULL statements of the contracts that `ARCHITECTURE.md` only summarises — a partial supersession, not a total one. | READ IN FULL |
| 23 | `cowork_phase2_architecture_review.md` | 13 | LIVE-SPEC | Carries the user's sequencing gate of 2026-06-17 (structural fixes before inference) and produces the architecture-fix order. | READ IN FULL |
| 24 | `docs/llm_integration.md` | 13 | LIVE-SPEC | The language-model design; its decisions are registered (D-139…D-143) but all DEFERRED, and the document is their detail. | READ IN FULL |
| 25 | `docs/phase4_recon.md` | 13 | REPORT/NARRATIVE | A dated read-only reconnaissance (`:3-4`) recommending an implementation shape; the retirement it scouted has since landed — [[OI-238]]'s resolution records that `prepareUserFacingHarmonicRegions` no longer exists in the production tree, verified at the code. Its ruling-vocabulary hits are ordinary prose (“convention”, “retired”, “must not proceed” inside a quoted dispatch condition). | **EXCLUDE** |
| 26 | `docs/score_inventory.md` | 13 | LIVE-SPEC | A mandatory read for any score-touching task (`CLAUDE.md`, Score corpora) with hard rules of its own. | READ IN FULL |
| 27 | `cowork_l1l3_stabilization_plan.md` | 12 | LIVE-SPEC | Carries the user-ratified ordering principle of 2026-06-25 (build-it-right before tune-precision) and the per-step gates. | READ IN FULL |
| 28 | `cowork_layer4_spec_review.md` | 12 | REPORT/NARRATIVE | Own header `:6`: “Status: findings only; the rewrite follows once these are agreed.” The reviewed document, `cowork_layer4_chordsymbol_design.md`, is in THIS session's full-read set, so the reviewed text is read directly rather than through its review. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 29 | `docs/layer_architecture_audit.md` | 12 | LIVE-SPEC | Claims supersession for LAYER 1 ONLY; the rest of the intended-vs-actual layer discussion carries no successor claim. | READ IN FULL |
| 30 | `cowork_census_full_needs_audit.md` | 11 | LIVE-SPEC | Banner: ★ DISPOSED (user, 2026-07-04) — four §6-C rulings (N18/N19 ADOPTED, N15 RATIFIED, N20 as its own needs row). | READ IN FULL |
| 31 | `docs/iter97_delta_characterization.md` | 11 | REPORT/NARRATIVE | “Read-only data report. No source changes were made” (`:3`), generated against a named iteration-era baseline. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 32 | `cowork_evidence_inventory.md` | 10 | LIVE-SPEC | The live catalog of every hint each layer finds, with standing obligations at [[OI-146]]. | READ IN FULL |
| 33 | `cowork_gateA_unification_design.md` | 10 | LIVE-SPEC | Explicitly “the ratification surface” for a separate user-ratified build event. | READ IN FULL |
| 34 | `cowork_layer3_reachback_design.md` | 10 | LIVE-SPEC | Banner: BUILT (capability, gated OFF); records the resolved build-decision form. | READ IN FULL |
| 35 | `cowork_layer5_function_methods.md` | 10 | LIVE-SPEC | `:33` ★ DECIDED (user, 2026-06-26) — output the Roman numeral; T/S/D is a derived read-out only. | READ IN FULL |
| 36 | `cowork_layer6_grouping_design.md` | 10 | LIVE-SPEC | Banner: AS-BUILT (2026-07-02) with a §5.1-a interpretation RULED at ratification. | READ IN FULL |
| 37 | `cowork_sensitive_cell_probe.md` | 10 | LIVE-SPEC | Banner: ★ USER-RATIFIED 2026-07-19 — options 1a, 2a, 3a, with two sharpenings. | READ IN FULL |
| 38 | `cowork_term_theory_grounding.md` | 10 | LIVE-SPEC | Its header says it decides nothing, but `:330-351` carry FIVE design decisions marked ✅ DECIDED 2026-07-19 and “ratified as of 2026-07-19”. The mechanical check caught this; the header is misleading. | READ IN FULL |
| 39 | `docs/stage4b_design.md` | 10 | LIVE-SPEC | A ratification-gated design carrying the user's choice of the staged demote-first approach (2026-06-14). | READ IN FULL |
| 40 | `cowork_architecture_review_2026_07.md` | 9 | LIVE-SPEC | Banner: AMENDMENTS A-1…A-10 RATIFIED (user, 2026-07-02) plus a ratified corpus expansion. | READ IN FULL |
| 41 | `cowork_l1l4_completion_ledger.md` | 9 | LIVE-SPEC | Banner: ★ L1–L4 COMPLETE — SIGN-OFF, with the residuals it defers by name. | READ IN FULL |
| 42 | `cowork_union_search_record.md` | 9 | LIVE-SPEC | Banner: ★ DISPOSED (user, 2026-07-04) — five approvals including a ratified negative ruling (N13). | READ IN FULL |
| 43 | `docs/back_half_design.md` | 9 | LIVE-SPEC | A design ready for user ratification whose §4 redirect is cited as ratified by two downstream stage designs. | READ IN FULL |
| 44 | `docs/mismatch_classification.md` | 9 | REPORT/NARRATIVE | A dated classification of one test run's 135 mismatches (`:3-5`), all from one synthetic catalog score. Its hits are the words “policy” and “convention”, used to pose OPEN annotation questions, not to answer them; the governing answer is registered — **D-304** (the analyzer always emits its fullest reading; simplifying happens only when comparing against a corpus). Flagged for the user: if the catalog's own annotation policy is still considered open, this document is where the question is stated. | **EXCLUDE** |
| 45 | `docs/unified_analysis_pipeline.md` | 9 | LIVE-SPEC | Records live design divergences by name (“A remains by design; C parked”) and a deferred Phase 4c. | READ IN FULL |
| 46 | `cowork_spec_polish_findings_a.md` | 8 | REPORT/NARRATIVE | Own banner `:3-5`: “✅ DISPOSITIONED (the merged Cowork doc pass, 2026-07-03). All 67 rows executed against the four documents … retained as the audit record; the row texts below describe the PRE-pass state.” The standard it applies is registered (**D-193**, the writing standards live in one place; **D-255**…**D-257**, the template rules). Its ruling-vocabulary hits are inside row texts describing offenders, not rulings of its own. | **EXCLUDE** |
| 47 | `docs/layer_audit_plan.md` | 8 | LIVE-SPEC | Carries the user's NORTH STAR of 2026-06-17 and defines the obligation-map output. | READ IN FULL |
| 48 | `docs/precision_metric_design.md` | 8 | LIVE-SPEC | A design-and-scoping deliverable for the ratification gate that precedes building any metric. | READ IN FULL |
| 49 | `cowork_factorization_desk_simulation.md` | 7 | LIVE-SPEC | Banner: ★ USER-RATIFIED 2026-07-19 — the §7 asks granted in full. | READ IN FULL |
| 50 | `cowork_implementation_review.md` | 7 | REPORT/NARRATIVE | `docs/implementation_roadmap.md:4-8` names this document as its source (“part 2 — as-built”) under the same single-tracker statement. Independently declared “partly stale; verified at current code” by `cowork_structural_integrity_audit.md:11-12`, which extends it and is itself LIVE-SPEC in the full-read set. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 51 | `cowork_joint_estimator_architecture.md` | 7 | LIVE-SPEC | The GOVERNING architecture decision (user-ratified 2026-07-14/17), named as such at `OPEN_ITEMS.md:15-18`. | READ IN FULL |
| 52 | `cowork_key_drift_research_grounding.md` | 7 | REPORT/NARRATIVE | Own header `:5-7`: “It GROUNDS the coming design conversation; it decides and builds nothing.” Published-fact grounding under principle #1. Its single ruling-vocabulary hit is a citation of the ratified baselines. | **EXCLUDE** |
| 53 | `cowork_l1l4_architecture_audit.md` | 7 | LIVE-SPEC | A resolution-updated audit with still-open migration debt scheduled for a later engagement. | READ IN FULL |
| 54 | `cowork_mode_key_chord_inference_discussion.md` | 7 | REPORT/NARRATIVE | Own header `:9`: “Nothing here authorizes a build.” Its subject question is SETTLED: [[OI-43]] ✅ SETTLED 2026-07-12 (the joint step SHELVED on both axes, row CLOSED) and [[OI-44]] ✅ DECLARED; the shelving is registered as **D-278** (SHELVED WITH EVIDENCE, ratified 2026-08-02). Its ruling-vocabulary hits are citations of that shelving. | **EXCLUDE** |
| 55 | `cowork_style_taxonomy_proposal.md` | 7 | LIVE-SPEC | Banner: RATIFIED (2026-06-30) · EXECUTED — and in possible tension with D-132, which records empirical grounding as future work. | READ IN FULL |
| 56 | `cowork_target_architecture_review.md` | 7 | REPORT/NARRATIVE | `docs/implementation_roadmap.md:4-8` names this document as its source (“part 1 — target architecture”) and itself as “the single tracker ensuring every review conclusion is addressed”; that roadmap is LIVE-SPEC and in the full-read set. Its own ruling-vocabulary hits are citations of decisions recorded elsewhere, not rulings. | **EXCLUDE** |
| 57 | `docs/duplication_audit.md` | 7 | REPORT/NARRATIVE | A dated read-only audit (`:1-10`) of duplication across the analysis pipeline. Zero ruling-vocabulary hits; the standing rule it measures against is registered (**D-073**, single implementation for shared logic; principle #6). | **EXCLUDE** |
| 58 | `cowork_audit_obligation_map.md` | 6 | LIVE-SPEC | Re-assessed 2026-06-20 — the supersession is explicitly PARTIAL (“supersedes parts of §B/§C/§E”). | READ IN FULL |
| 59 | `cowork_delta_check_dispositions.md` | 6 | LIVE-SPEC | Records proper-layer DISPOSITIONS verified at source plus the L4 build backlog. | READ IN FULL |
| 60 | `cowork_eg2_scoping.md` | 6 | LIVE-SPEC | The premise ledger of an OPEN gate row ([[OI-3]] — decision with the user). | READ IN FULL |
| 61 | `cowork_information_loss_audit.md` | 6 | LIVE-SPEC | A live catalogue of information-loss sites, each fix its own later ratified event. | READ IN FULL |
| 62 | `cowork_layer1_tone_collection_design.md` | 6 | LIVE-SPEC | The pre-rebuild Layer-1 design; no supersession is claimed in it, though Layer 1 was later rebuilt as the note model. | READ IN FULL |
| 63 | `cowork_phrase_boundary_methods.md` | 6 | LIVE-SPEC | `:8` ★ Proportionality (user-ratified 2026-06-26) — a ruling of its own. | READ IN FULL |
| 64 | `docs/phase5_recon.md` | 6 | REPORT/NARRATIVE | A dated read-only reconnaissance (`:3-5`) recommending an implementation shape. Its four hits are all the word “convention” used of an engraving text format. | **EXCLUDE** |
| 65 | `docs/stage4c_cadence_key_design.md` | 6 | LIVE-SPEC | A ratification-gated design resting on two named measured results. | READ IN FULL |
| 66 | `docs/symbol_input_audit.md` | 6 | LIVE-SPEC | `:37` and `:330` record OPEN user decisions (“Tool-side input uses requiring user decision: 2”). | READ IN FULL |
| 67 | `cowork_adjudication_dossier.md` | 5 | LIVE-SPEC | Banner: RATIFIED by the user 2026-07-10 — including the one genuine acceptance (A3). | READ IN FULL |
| 68 | `cowork_joint_estimator_factorization.md` | 5 | LIVE-SPEC | Banner: ★ USER-RATIFIED 2026-07-19 — the governing structure of the production estimator. | READ IN FULL |
| 69 | `cowork_layer1_extend_design.md` | 5 | LIVE-SPEC | A DRAFT for sign-off implementing the supplier side of the bounded-context contract. | READ IN FULL |
| 70 | `cowork_phase5c_l5_build_plan.md` | 5 | LIVE-SPEC | A build plan with a non-negotiable per-step method and per-step gates. | READ IN FULL |
| 71 | `cowork_tpc_capability_design.md` | 5 | LIVE-SPEC | Banner: BUILT (capability-only, no production consumer) — a declared dormancy. | READ IN FULL |
| 72 | `cowork_uncertain_resolver_investigation.md` | 5 | LIVE-SPEC | Banner: RESOLVED — user-ratified 2026-06-24; a ruling of its own. | READ IN FULL |
| 73 | `docs/format_symbol_audit.md` | 5 | REPORT/NARRATIVE | A dated read-only per-branch audit (`:3-5`). Its findings are tracked outside it — the F1–F5 pattern history is a project memory, and `docs/scoring_model.md` (in the full-read set) is the formatter's standing home. One ruling-vocabulary hit. | **EXCLUDE** |
| 74 | `docs/iter97_bir_false_categorization.md` | 5 | REPORT/NARRATIVE | “Read-only data report. No source changes were made” (`:3`); a per-case extraction against an iteration-era baseline, and the gate it categorizes is the batch stop, which `CLAUDE.md` block (C) records as SUPERSEDED at R10-b. One ruling-vocabulary hit. | **EXCLUDE** |
| 75 | `docs/key_detection_baroque_partial_signature.md` | 5 | LIVE-SPEC | Documents the partial-signature correction that is still live at the code ([[OI-98]] names it). | READ IN FULL |
| 76 | `cowork_functional_analysis_research_grounding.md` | 4 | REPORT/NARRATIVE | Own header `:3-8`: “published-fact grounding (principle #1) … Feeds the Layer 5 engagement design dispatch”. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 77 | `cowork_l1_l5_premise_debt_audit.md` | 4 | LIVE-SPEC | The retroactive #17 ledger for built code; three tiers of premise debt, several still open. | READ IN FULL |
| 78 | `cowork_phase5b_l4_build_plan.md` | 4 | LIVE-SPEC | A build plan with a non-negotiable per-step method. | READ IN FULL |
| 79 | `cowork_style_clustering_plan.md` | 4 | LIVE-SPEC | Banner: committed future direction, user-ratified 2026-06-29. | READ IN FULL |
| 80 | `docs/architecture_joint_inference.md` | 4 | LIVE-SPEC | An architecture direction, investigation-confirmed and “ratifiable”, with no recorded supersession banner. | READ IN FULL |
| 81 | `docs/divergence_d_recon.md` | 4 | REPORT/NARRATIVE | A dated read-only recon with an audience of “next session planning Phase 3c-impl” (`:3-5`). Zero ruling-vocabulary hits. | **EXCLUDE** |
| 82 | `docs/iter92_joint_bass_chord_scoring.md` | 4 | LIVE-SPEC | “Remains the authoritative reference for the JOINT formula and its guards”; D-224 is registered against it. | READ IN FULL |
| 83 | `docs/nct_detection_design.md` | 4 | LIVE-SPEC | The deferred non-chord-tone design; D-303 constrains its eventual shape and it is load-bearing at [[OI-55]]/[[OI-68]]. | READ IN FULL |
| 84 | `docs/policy2_coalescing_map.md` | 4 | REPORT/NARRATIVE | A dated read-only divergence map (`:3-4`). Its hits are the word “retired” recording that the Jazz path was retired — which is itself registered as **D-067** (Jazz mode retired, LIVE, home `ARCHITECTURE.md`). | **EXCLUDE** |
| 85 | `docs/quality_observations_iter76.md` | 4 | REPORT/NARRATIVE | A record of a user's visual inspection of four snapshot scores (`:3-6`) — observations against ground truth, not decisions. One ruling-vocabulary hit. | **EXCLUDE** |
| 86 | `docs/rfc_musescore_forum_post.md` | 4 | REPORT/NARRATIVE | “Draft for Vincent's review. **Not posted.**” (`:3-4`) — outward-facing copy, not a specification. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 87 | `docs/stage4d_local_modulation_design.md` | 4 | LIVE-SPEC | A ratification-gated design resting on named measured results. | READ IN FULL |
| 88 | `cowork_audit_protocol.md` | 3 | LIVE-SPEC | The HOME of registered decisions D-208, D-209, D-250, D-251, D-252. | READ IN FULL |
| 89 | `cowork_l1l4_review_charter.md` | 3 | LIVE-SPEC | The user-mandated review gate with its two aims stated as requirements. | READ IN FULL |
| 90 | `cowork_layer3_spec_language_sweep.md` | 3 | REPORT/NARRATIVE | A language-mechanical offender sweep applying the ratified writing standards (**D-193**), named as a worked example by `cowork_design_doc_template.md:19` — which phase 1d read in full and which is the standards' HOME. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 91 | `cowork_product_tool_register.md` | 3 | REPORT/NARRATIVE | Own banner `:3-8`: “Status: RESEARCH NOTE … **Nothing here is commissioned**; product work is out of scope until the architecture/algorithm/refactoring completion (standing rule).” It cites that standing rule rather than making one. | **EXCLUDE** |
| 92 | `cowork_score_census_plain_draft.md` | 3 | REPORT/NARRATIVE | The second census appendix, named at `cowork_score_census.md:5-11` on the same terms. One ruling-vocabulary hit, in a data row. | **EXCLUDE** |
| 93 | `cowork_upstream_merge_risk.md` | 3 | REPORT/NARRATIVE | Own banner `:3-7`: “Status: reference … A forward-looking inventory, **not** an active breakage and **not** a merge”; the git facts are transcribed CC findings and the deferral is “Cowork's architectural read”, not a ruling. The distribution rules that DO bind are registered — **D-117**, **D-197**, **D-259**, **D-316**. | **EXCLUDE** |
| 94 | `docs/iter90_bass_as_root_promotion_shelved.md` | 3 | LIVE-SPEC | A shelving with a standing prohibition at `:95` (“Do not pursue this as a chord-analyzer-local gate”). **D-302** covers the neighbouring inversion class and its recorded defense names the bass-as-root triad default — but not this prohibition verbatim, so the doubt keeps it IN. | READ IN FULL |
| 95 | `docs/llm_triage_design.md` | 3 | REPORT/NARRATIVE | “Status: Discussion only. No implementation committed. This document captures a design conversation … preserved so future planning sessions can pick up the shared context” (`:3-6`). Its governing question is RULED and registered — [[OI-56]] ✅ DECIDED 2026-07-13 (a HUMAN acts as ground truth; the judge as guidance, never a grader) = **D-205**; its one “must not” (`:106`) restates **D-294**. | **EXCLUDE** |
| 96 | `docs/three_paths_divergence_recon.md` | 3 | REPORT/NARRATIVE | A dated read-only recon of one chord's three readings (`:3-6`). Its hits are the word “policy” used of a display sort order, with the fix left as stated options, not a choice. | **EXCLUDE** |
| 97 | `cowork_audit_cadencekeyanchor.md` | 2 | REPORT/NARRATIVE | One of the Cowork second-opinion layer audits of the OI-84 certification programme (own header: “to reconcile with CC's primary audit”). [[OI-84]] is ✅ COMPLETE 2026-07-12 — every surviving layer certified on two passes — and the programme's findings are register rows OI-86…OI-140. Measured: phase 1d read FOUR siblings of this class in full (`cowork_audit_postscoringgates`, `_harmonicfunctionlayer`, `_regionanalyzer`, `_jointkeydecision`) and they produced ZERO register entries. Zero ruling-vocabulary hits of its own. | **EXCLUDE** |
| 98 | `cowork_audit_chordpostpasses_sparse.md` | 2 | REPORT/NARRATIVE | Same class and same verification as `cowork_audit_cadencekeyanchor.md` (OI-84 COMPLETE; findings rowed OI-86…OI-140; four read siblings yielded zero entries). Zero ruling-vocabulary hits. | **EXCLUDE** |
| 99 | `cowork_audit_keymodeanalyzer.md` | 2 | REPORT/NARRATIVE | Same class and same verification as `cowork_audit_cadencekeyanchor.md`. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 100 | `cowork_corpus_audit.md` | 2 | REPORT/NARRATIVE | Its findings are rowed and assigned: [[OI-57]] carries the surviving half (the extra-scores registry, ASSIGNED to the corpus-onboarding event [[OI-38]]) and records the other half superseded by the GT-corpus manifest discipline. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 101 | `cowork_idiom_discovery_findings.md` | 2 | LIVE-SPEC | The empirical basis of the ratified idiom set, and the point where that ratification and D-132 (empirical grounding as future work) may not agree. | READ IN FULL |
| 102 | `cowork_key_layer_design_opening.md` | 2 | SUPERSEDED-ESTABLISHED | Own banner `:3-8`: ⛔ SUPERSEDED 2026-07-17 by `cowork_joint_estimator_architecture.md`, “Do not build from this document”. Successor VERIFIED: it exists, its own line 3 records the user ratification of 2026-07-14, `OPEN_ITEMS.md:15-18` carries it as the governing architecture decision, and it is registered as **D-001** (key, mode and chord inferred by ONE joint decode, LIVE). It covers this document's whole subject — the key is one axis of the joint estimate, not a separable layer. | **EXCLUDE** |
| 103 | `cowork_layer2_reslice_design.md` | 2 | LIVE-SPEC | Banner: BUILT; records the §5 build-time decision that was taken. | READ IN FULL |
| 104 | `cowork_layer3_keymode_impl_design.md` | 2 | LIVE-SPEC | Pins the Layer-3 implementation decisions increment by increment. | READ IN FULL |
| 105 | `cowork_siloed_facts_audit.md` | 2 | REPORT/NARRATIVE | `OPEN_ITEMS.md:351-355` records, under a user challenge of 2026-07-10, that ALL 17 of this audit's findings are mapped to register rows, and gives the mapping finding-by-finding (1→OI-72 … 17→OI-74). One ruling-vocabulary hit. | **EXCLUDE** |
| 106 | `cowork_spec_polish_findings_b.md` | 2 | REPORT/NARRATIVE | Own banner `:3-5`: “✅ DISPOSITIONED … All 87 rows executed … Retained as the audit record; row texts describe the PRE-pass state.” Same standard and same registration as pass A. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 107 | `cowork_types_header_design.md` | 2 | LIVE-SPEC | Banner: BUILT / AS-BUILT with the D1/D2 and leaf-location decisions recorded. | READ IN FULL |
| 108 | `docs/extension_stripping_policy.md` | 2 | LIVE-SPEC | “Direction settled” — a stated policy with no register entry found for it. | READ IN FULL |
| 109 | `docs/musescore_parser_special_notations_recon.md` | 2 | REPORT/NARRATIVE | A dated read-only recon (`:3-4`) reporting which catalog entries MuseScore's parser accepts. Zero hits on the ruling half of the vocabulary. | **EXCLUDE** |
| 110 | `docs/p3_granularity_ab_3_1b.md` | 2 | EVIDENCE-FROZEN | A committed measurement document (its banner `:3-11`: “Measured evidence, committed as Stage-5 input”). Its one decision — `:70` “Whole-score is shelved. Do not re-attempt without resolving the granularity question” — is registered as **D-286** (whole-score interactive analysis SHELVED WITH EVIDENCE; the bounded window is the ratified reading), ratified by the user 2026-08-02 at the fourth ratification event. The remainder is the per-tick granularity-accuracy comparison, i.e. data. NOTE for the user: this is the evidence base of the OPEN extent question [[OI-210]]; excluding it from the DECISION read does not withdraw it from phase 3. | **EXCLUDE** |
| 111 | `cowork_audit_localmodulationdetector.md` | 1 | REPORT/NARRATIVE | Same class and same verification as `cowork_audit_cadencekeyanchor.md`. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 112 | `cowork_eg1_premise_checks.md` | 1 | LIVE-SPEC | Premise checks feeding an OPEN gate row; design decisions enumerated and assigned to owning layers. | READ IN FULL |
| 113 | `cowork_gate_policy_amendment.md` | 1 | LIVE-SPEC | The founding provenance of the two-tier gate policy now in `CLAUDE.md` block (B) — registered D-191; the document carries the derivation. | READ IN FULL |
| 114 | `cowork_idiom_entry_mapping.md` | 1 | REPORT/NARRATIVE | A data mapping of catalog entries onto the ratified idiom set, declared “**Provisional, easy to revise**” at `:5`. The taxonomy it implements is the decision, and that lives in `cowork_style_taxonomy_proposal.md` (RATIFIED 2026-06-30 · EXECUTED), which stays LIVE-SPEC. | **EXCLUDE** |
| 115 | `cowork_key_chord_joint_inference_grounding.md` | 1 | REPORT/NARRATIVE | Published-fact grounding for the joint-vs-separable question, FACT/THEORY/CONJECTURE-labelled (`:6-8`). The decision it grounds is registered — **D-001**, and `cowork_joint_estimator_architecture.md:5` cites this document as its grounding. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 116 | `cowork_key_mode_inference_diagnosis.md` | 1 | LIVE-SPEC | A Premise-Gate diagnosis opening whose row [[OI-141]] is still OPEN. | READ IN FULL |
| 117 | `cowork_l1l4_review_note.md` | 1 | REPORT/NARRATIVE | Own header `:5-7`: the docs-and-coherence half of the L1–L4 review, “mechanical status-tidy, no algorithmic contradiction”, with the one substantive question handed to CC. The gate it serves, `cowork_l1l4_review_charter.md`, stays LIVE-SPEC. Its single hit is a status observation. | **EXCLUDE** |
| 118 | `cowork_polyphony_phrase_harmony_research.md` | 1 | REPORT/NARRATIVE | Own header `:3-7`: “A durable, cited record of the deep search” in answer to a user question. Its ruling-vocabulary hits are citations of decisions recorded elsewhere. | **EXCLUDE** |
| 119 | `cowork_score_census_gt_draft.md` | 1 | REPORT/NARRATIVE | An appendix of `cowork_score_census.md`, which names it at `:5-11` as one of two “full evidence tables … retained verbatim” with `[verified]`/`[reported]` fact tags. The census itself is LIVE-SPEC and in the full-read set — it is the home of the fitting-pool licence constraint §8c that [[OI-271]] turns on. Its two hits are corpus-supersession notes in data rows. | **EXCLUDE** |
| 120 | `docs/chordlist_bug_report.md` | 1 | REPORT/NARRATIVE | An upstream bug-report draft for the chord-symbol parser fix. Its disposition is RULED and registered: [[OI-273]] ✅ RULED (user, 2026-08-02, option (i)) and **D-316** records the patch as a local patch with an UPSTREAMABLE distribution disposition. Zero ruling-vocabulary hits. | **EXCLUDE** |
| 121 | `docs/perf_p3_baseline.md` | 1 | REPORT/NARRATIVE | A dated measurement-only baseline (`:3-5`, “Measurement-only; zero production-code changes”). Superseded in substance by the 2026-07-28 analysis-cost profile and its rows [[OI-203]]/[[OI-215]]/[[OI-216]]/[[OI-217]]. Zero ruling-vocabulary hits. | **EXCLUDE** |

## Provenance

- Derived from `tools/audit/decisions/decision_clusters.json` and `tools/audit/decisions/cluster_dispositions.json` at the commit this file is committed in.
- The read set: `cc_phase1d_enumeration_wave_report.md` Task 1 (21 documents) and `open_items/OI-207.md` phase-1f dated note (2 documents, one of them a repeat).
- Dispatch: `cc_instruction_phase1g_triage.md`, Task 1. Author: CC, 2026-08-02.
- Nothing in this file is a ratification of a DECISION. The exclusion list was a proposal when this file was first generated and is now ACCEPTED (the user, 2026-08-02, all 41 as tabled — `open_items/OI-207.md`); the classification of the 80 LIVE-SPEC documents carries no such acceptance and needs none, since its disposition is to read them.
