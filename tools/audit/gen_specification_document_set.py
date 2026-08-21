#!/usr/bin/env python3
"""THE SPECIFICATION DOCUMENT SET — derived from `ARCHITECTURE.md`'s admitted delegations.

Dispatch: `cc_instruction_successor_plan_landing_and_step_zero.md`, Task 1 (Cowork, 2026-08-21),
executing Ruling 6 of `cowork_rulings_2026_08_21_successor_plan_sitting.md`.

WHAT IT IS FOR.  The successor plan
(`cowork_specification_reconstruction_plan_successor_2026_08_21.md` §5) needs to know WHICH
documents specify the analysis.  The ruling fixes the answer in three limbs: `ARCHITECTURE.md`
itself (the analysis layers' sections, the joint estimator's standing-rules section, document
governance); every document `ARCHITECTURE.md` delegates to in a form the delegation-form rule
admits; and `docs/scoring_model.md`.  This tool derives that set and publishes it whole.

WHAT IS DERIVED AND WHAT IS AUTHORED, stated because the difference is the whole value:

  DERIVED  -- the CANDIDATE POPULATION: every naming of another `.md` document anywhere in
              `ARCHITECTURE.md`, scanned from the file itself, with the line and the line's own
              text; the member list, from the authored grades; the three limb-1 regions' line
              ranges, from the file's own headings; every count; the reconciliation against the
              delegation seed, in both directions, with its miss rate; and whether each member's
              file exists at the tree.
  AUTHORED -- the GRADE per named target document, under `CLAUDE.md` decisions-register rule (i)
              with rules (h) and (k)/(k1); for an ADMITTED target, the anchor of the naming that
              GOVERNS, and the scope (document, or the sections the naming names); and the two
              declared properties per member -- LIVE or DORMANT, and the declared establishment
              status -- each as an anchor into the file that declares it.

THE GRADING UNIT IS THE TARGET DOCUMENT, NOT THE NAMING, AND THAT IS RULE (k1)'S OWN SHAPE:
"WHERE A DOCUMENT IS NAMED IN BOTH AN ADMITTING AND AN EXCLUDED FORM, THE STRONGEST NAMING
GOVERNS".  So one grade is authored per target, the governing naming is anchored, and EVERY OTHER
naming of that target is published verbatim beside it, derived, so a reader can see what else the
document says and challenge the choice of governing naming.  This is the construction
`gen_phase1p_delegation_bar.py` already uses over the register's home population (#6).

THE FORM VOCABULARY.  Four of the five classes are the bar's own, quoted from `CLAUDE.md` and
located there on every run:

  explicit-delegation-clause      ADMITTED   -- "The ratified contract for this layer is X"
  named-home-with-sections        ADMITTED   -- "Criterion + build home: X §0/§5.3"
  bare-appended-citation          EXCLUDED   -- "Full spec: X."
  provenance-attribution          EXCLUDED   -- a naming inside a list of citations, or a
                                                parenthetical recording where something was ratified
  naming-that-delegates-no-concern EXCLUDED  -- THIS TOOL'S OWN residue class, declared as such and
                                                not the bar's: a naming that is neither a citation
                                                nor a delegation -- a filename inside a directory
                                                listing, a document named as superseded, a document
                                                named as one to be created.  It admits nothing, so
                                                the residue class can only narrow the set, never
                                                widen it.

WHAT THE SEED IS AND IS NOT (assumption A3 of the dispatch).  The delegation grades at
`tools/audit/decisions/phase1p_delegation_bar.py` were produced to answer *where does a register
entry live*, over the ENTRIES' home documents -- not to enumerate every delegation
`ARCHITECTURE.md` writes.  It is read here as a SEED and never as the population.  It is
reconciled BOTH WAYS: every seed-admitted delegation sited in `ARCHITECTURE.md` must be re-found at
the text (a seed-admitted delegation the text does not carry STOPS the tool), and every
text-found admitted delegation absent from the seed is NAMED.  The miss rate against the seed is
published as part of the derivation's name (D-661) at
`the_seed_reconciliation.miss_rate_against_the_seed`.

THE STOPS, so this cannot silently stop being a derivation:
  1. a scanned target with no authored grade STOPS the tool -- a document named by a later edit
     cannot enter the population unclassified;
  2. an authored grade for a target the scan does not find STOPS it, which is the same demand in
     the other direction;
  3. an anchor that is missing, or that matches more than once, STOPS it -- so no citation is ever
     emitted from a coordinate that has drifted;
  4. an ADMITTED target whose governing anchor does not sit on a line that names that target STOPS
     it;
  5. a grade outside the five-class vocabulary, or an ADMITTED grade with no anchor, or a
     `sections` scope with no sections, STOPS it;
  6. a seed-admitted delegation sited in `ARCHITECTURE.md` whose anchor is not found at the text
     STOPS it (A3's own condition, made mechanical);
  7. a limb-1 region heading that is missing or ambiguous STOPS it;
  8. an authored property quote whose anchor is not found at its cited file STOPS it (the
     quote-fidelity check).

NO RECOGNIZER OVER PROSE DECIDES A GRADE (F42, F84).  The scan finds NAMINGS -- a mechanical
identity, a filename in the text.  Every judgment about whether a naming delegates is authored,
one entry per target, each naming what it was made from.

WHAT THIS DOES NOT DO.  It edits no document.  It restores nothing, reverts nothing and corrects
nothing.  It closes no open-items row and writes no decisions-register entry.  It derives no
specification, admits no fact, and takes no view on whether any member's content is right.

Usage:
  python tools/audit/gen_specification_document_set.py            # write the artifact
  python tools/audit/gen_specification_document_set.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()

ROOT = Path(__file__).resolve().parent.parent.parent
ARCH = ROOT / "ARCHITECTURE.md"
CLAUDE = ROOT / "CLAUDE.md"
OUT = ROOT / "tools" / "audit" / "specification_document_set.json"


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning, never a skipped record."""


# ── the five form classes ────────────────────────────────────────────────────────────────────────
CLAUSE = "explicit-delegation-clause"
NAMED_SECTIONS = "named-home-with-sections"
BARE_CITATION = "bare-appended-citation"
PROVENANCE = "provenance-attribution"
NO_CONCERN = "naming-that-delegates-no-concern"

ADMITTING = {CLAUSE, NAMED_SECTIONS}
FORMS_VOCABULARY = {CLAUSE, NAMED_SECTIONS, BARE_CITATION, PROVENANCE, NO_CONCERN}

# ── AUTHORED — the clauses of `CLAUDE.md` that decide a grade, located there on every run ─────────
DECIDING_CLAUSES = {
    "rule_(i)_admitted": "**ADMITTED:** an **explicit",
    "rule_(i)_not_admitted": 'a **bare appended citation** — *"Full spec: X."*',
    "rule_(h)_granularity": "a delegation naming a DOCUMENT reaches ALL of its sections",
    "rule_(k)_a_glob_confers_nothing": "A glob pattern and a trailing ellipsis CONFER NOTHING",
    "rule_(k1)_the_strongest_naming_governs": "THE STRONGEST NAMING GOVERNS",
}

# ── AUTHORED — the three limb-1 regions the ruling names, by heading ──────────────────────────────
# Each is located by its heading text; the line range is DERIVED from the file's own headings.
LIMB_1_REGIONS = [
    ("the analysis layers' sections (filed as children of §3.3)",
     ["#### Layer 1 — the lossless note model (Built+Live)",
      "#### Layer 2 — the deterministic change-point slicer (Built+Live — consumed by L3)",
      "#### Layer 3 — key/mode is the sequence decoder (Built+Dormant)",
      "#### Layer 4 — the per-slice chord-symbol decoder (Built+Dormant — not wired)",
      "#### Layer 5 — the function/cadence layer (Built+Dormant — design ratified; consumed by L6)",
      "#### Layer 6 — the grouping layer (Design-only — v1 spec)"]),
    ("the joint estimator's standing-rules section (above the table of contents)",
     ["## The joint estimator — the standing rules of the production inference layer"]),
    ("document governance",
     ["## Document governance and the standing architecture notes"]),
]

# ── AUTHORED — the grade per named target document ────────────────────────────────────────────────
#   target -> dict(form, why, anchor=None, scope=None, sections=None, before=0, after=0)
# `anchor` is required for an ADMITTED grade and is a distinctive substring of the line carrying the
# GOVERNING naming; `before`/`after` say how many lines of context the emitted verbatim passage
# carries.  For an EXCLUDED grade no anchor is authored: every naming of that target is published
# verbatim from the scan, and the grade covers the target as a whole.
def g(form, why, anchor=None, scope=None, sections=None, before=0, after=0):
    return {"form": form, "why": why, "anchor": anchor, "scope": scope,
            "sections": sections, "before": before, "after": after}


GRADES: dict[str, dict] = {
    # ── ADMITTED ────────────────────────────────────────────────────────────────────────────────
    "cowork_joint_estimator_architecture.md": g(
        CLAUSE,
        "The canonical document's own opening banner declares a user-ratified GOVERNING DECISION "
        "and names this document as where it is read. Graded a delegation clause on the strength "
        "of what is delegated — the governing architecture decision itself — rather than on the "
        "word 'see'. Same grade and same ground as the seed's.",
        anchor="`cowork_joint_estimator_architecture.md`.** Key, mode, and chord are inferred",
        scope="document", before=1),
    "cowork_prefit_gates.md": g(
        CLAUSE,
        "The bar's first named form: 'The ratified contract for the PRE-FIT PROTOCOLS … is X, "
        "which this section points at and does not restate'. The paragraph itself says that the "
        "weaker naming two lines above it is a citation inside a list, which rule (i) does not "
        "admit — so the document states its own application of (k1).",
        anchor="the piece-bootstrap interval — is `cowork_prefit_gates.md`",
        scope="document", before=2, after=2),
    "cowork_notation_output_contract.md": g(
        NAMED_SECTIONS,
        "A JUDGMENT, recorded as one, and the seed's: the naming sits inside a parenthesis, which "
        "the bar associates with the excluded provenance form — but it names the document's ROLE "
        "('contract') and the SECTIONS it delegates, and it records no ratification event. The "
        "excluded parenthetical form is the one that records WHERE SOMETHING WAS RATIFIED; this "
        "one names a home. The section list is §2–§3.4, widened 2026-08-03 from §3.1–§3.4 on the "
        "user's direction, as the naming's own parenthesis states.",
        anchor="as-built, DORMANT; contract `cowork_notation_output_contract.md`",
        scope="sections", sections=["§2", "§3.1", "§3.2", "§3.3", "§3.4"], after=2),
    "cowork_joint_estimator_factorization.md": g(
        CLAUSE,
        "The bar's first named form: 'The ratified contract for the estimator's factor structure "
        "— … — is X, which this section points at and does not restate'. It supplements two "
        "weaker namings (a 'spec:' line and a parenthetical citation with line numbers), so (k1) "
        "governs and the strongest naming decides.",
        anchor="is `cowork_joint_estimator_factorization.md`, which this section points at",
        scope="document", before=2),
    "cowork_stage5_fitter_design.md": g(
        CLAUSE,
        "A delegation clause of the 'the X for this Y is Z' shape — 'the fitting event's own "
        "design contract is X … which this specification points at and does not restate'. Same "
        "grade and same ground as the seed's.",
        anchor="the fitting event's own design contract is `cowork_stage5_fitter_design.md`",
        scope="document"),
    "cowork_score_census.md": g(
        CLAUSE,
        "The bar's first named form — 'The ratified home for corpus-content, corpus-tier and "
        "corpus-acquisition decisions is X' — and DOCUMENT-LEVEL by its own terms. It is the "
        "strongest of three admitting namings: the §8c pool-table pointer and the §1/§3/§4/§8/§8b/"
        "§8c section list are both weaker, and (k1) makes the strongest govern. The reach is "
        "judged PER SECTION under rule (h), which the delegation's own sentence says.",
        anchor="`cowork_score_census.md` — a document-level delegation whose reach is judged per section",
        scope="document", before=1, after=3),
    "cowork_progression_schema_dictionary.md": g(
        CLAUSE,
        "The bar's third named form, word for word: 'formalised as an independent knowledge-base "
        "component with its own spec (X)'. The document-governance clause names it EXPLICITLY as "
        "well, by filename, which rule (k) admits; both namings admit and this is the stronger.",
        anchor="(`cowork_progression_schema_dictionary.md`): a static, curated",
        scope="document", before=1),
    "cowork_progression_schema_design.md": g(
        CLAUSE,
        "The document-governance hierarchy names this document BY FILENAME among the per-component "
        "design docs that 'are the authoritative detail for their own scope — the rules, the "
        "mechanisms, the per-layer decisions-with-alternatives'. Graded a delegation clause "
        "because the predicate delegates a stated concern rather than appending a pointer. Rule "
        "(k) admits the members named EXPLICITLY and withholds the glob and the trailing ellipsis, "
        "neither of which this grade rests on. The document's own weaker naming, 'Spec: <doc>.', "
        "is the bar's not-admitted example word for word, and (k1) makes the stronger govern.",
        anchor="`cowork_progression_schema_design.md`, the phrase-boundary design, …) are the **authoritative detail**",
        scope="document", before=1, after=1),
    "cowork_target_architecture.md": g(
        CLAUSE,
        "A subject-is-X naming with a delegating predicate: the document IS 'the detailed-rationale "
        "reference for those contracts (the historical north-star, the full statements, the "
        "supporting evidence)'. That is the shape of the bar's first admitted form, and the "
        "concern it delegates is stated in the same breath. §2.15 restates the same delegation in "
        "its own voice ('Their detailed statements live in the target-architecture doc'), and the "
        "target document's own banner agrees in terms ('demoted to a detailed design & rationale "
        "reference — it holds the full statements of the contracts'). The three weaker namings — "
        "'full ratified statements: X §2', a parenthetical recording a ratification, and a "
        "parenthetical citation of the 4-layer target — are excluded forms, and (k1) makes this "
        "one govern. ★ ABSENT FROM THE SEED, and the reason is A3: the seed's population is the "
        "register entries' HOME documents, and this document is nobody's home.",
        anchor="`cowork_target_architecture.md` is **demoted** to the detailed-rationale reference",
        scope="document", after=1),
    "cowork_confidence_contract.md": g(
        CLAUSE,
        "An instruction to read the document instead of the section — the delegation clause's "
        "shape, in different words: 'the class vocabulary, the squashing rules and the declared "
        "comparison frames are stated in full in X, which this contract points at rather than "
        "restates'. Same grade and same ground as the seed's. The parenthetical naming at the "
        "head of the same section records where the contract was ratified and is the excluded "
        "provenance form; (k1) makes this one govern.",
        anchor="are stated in full in `cowork_confidence_contract.md`",
        scope="document", before=1, after=1),
    "cowork_layer6_grouping_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word, SUPPLEMENTING the 'Full spec:' citation two "
        "paragraphs above rather than replacing it — so the document is named in both an "
        "admitting and an excluded form and (k1) governs.",
        anchor="The ratified contract for this layer is `cowork_layer6_grouping_design.md` (AS-BUILT, 2026-07-02",
        scope="document"),
    "cowork_voiceleading_axis_design.md": g(
        NAMED_SECTIONS,
        "The bar's second named form, word for word — it is the bar's own worked example, "
        "'Criterion + build home: X §0/§5.3', here widened on the user's direction to "
        "§0/§5.1/§5.3/§8/§9. The passage states which sections are deliberately NOT named and "
        "why, so the section list is the delegation's own and not this tool's reading of it.",
        anchor="`cowork_voiceleading_axis_design.md` §0/§5.1/§5.3/§8/§9 (AS-BUILT)",
        scope="sections", sections=["§0", "§5.1", "§5.3", "§8", "§9"], before=1, after=3),
    "cowork_bounded_context_design.md": g(
        CLAUSE,
        "The bar's second named form, word for word: 'The ONE detailed cross-layer spec for this "
        "contract is X'. Same grade and same ground as the seed's.",
        anchor="detailed cross-layer spec for this contract is **`cowork_bounded_context_design.md`**",
        scope="document", before=1, after=3),
    "cowork_evidence_inventory.md": g(
        CLAUSE,
        "A subject-is-X naming with a delegating predicate — 'The catalog of what each layer "
        "discovers is X' — the same shape as the bar's first admitted form, and it binds an "
        "obligation to the document (kept in step with the layer specifications as facts are "
        "adopted). Same grade and same ground as the seed's.",
        anchor="`cowork_evidence_inventory.md`, kept in step with these layer specifications",
        scope="document", before=1),
    "cowork_layer1_note_model_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word, in the Layer-1 section — the same wording the "
        "Layer-2/3/4/5/6 sections carry. ★ ABSENT FROM THE LIVE SEED, and the reason is not that "
        "the text lost the delegation: the seed RETIRED its grade on 2026-08-17 when the last "
        "register entry homed in this document was soft-discarded, so the document stopped being "
        "anybody's home and left the seed's population. The delegation itself stands at the text, "
        "unchanged, and the seed's retired block records the same ADMITTED grade.",
        anchor="The ratified contract for this layer is `cowork_layer1_note_model_design.md`",
        scope="document"),
    "cowork_phrase_boundary_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word, sited in the Layer-1 section because this "
        "document specifies the Layer-1.5 primitive and the canonical document carries no section "
        "of its own for L1.5 — a choice the delegating paragraph states rather than leaves to be "
        "inferred. Same grade and same ground as the seed's.",
        anchor="The ratified contract for the phrase-boundary primitive is `cowork_phrase_boundary_design.md`",
        scope="document"),
    "cowork_layer2_slicing_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word, in the Layer-2 section, SUPPLEMENTING the "
        "'See …' citation above it — so the document is named twice, once in each form, and (k1) "
        "makes the delegation govern. ★ ABSENT FROM THE LIVE SEED for the same reason as the "
        "Layer-1 note model's: the seed RETIRED its grade on 2026-08-16 when the ruled "
        "soft-discard emptied the document of register entries. The delegation stands at the text.",
        anchor="The ratified contract for this layer is `cowork_layer2_slicing_design.md`",
        scope="document"),
    "cowork_layer3_keymode_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word. Same grade and same ground as the seed's.",
        anchor="The ratified contract for this layer is `cowork_layer3_keymode_design.md`",
        scope="document"),
    "cowork_layer4_chordsymbol_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word. Same grade and same ground as the seed's.",
        anchor="The ratified contract for this layer is `cowork_layer4_chordsymbol_design.md`",
        scope="document"),
    "cowork_layer5_function_design.md": g(
        CLAUSE,
        "The bar's first named form, word for word. The 'Full spec:' line two paragraphs above is "
        "the bar's excluded example word for word, and the delegating paragraph says so itself; "
        "(k1) makes the delegation govern. Same grade and same ground as the seed's.",
        anchor="The ratified contract for this layer's function, cadence and tonicization decisions is `cowork_layer5_function_design.md`",
        scope="document"),
    "cowork_layer5_engagement_design.md": g(
        CLAUSE,
        "The bar's first named form, and it names its target's sections as well (Part 1 §1–§5, "
        "Part 2 §6–§10). Same grade and same ground as the seed's; the scope is SECTIONS because "
        "the delegation names them.",
        anchor="is `cowork_layer5_engagement_design.md` (Part 1 §1–§5, Part 2 §6–§10)",
        scope="sections",
        sections=["§1", "§2", "§3", "§4", "§5", "§6", "§7", "§8", "§9", "§10"]),
    "cowork_notation_adoption_increment.md": g(
        CLAUSE,
        "The bar's first named form: 'The ratified contract for the notation-surface adoption "
        "increment — its scope, its increments and their tracking — is X, which this section "
        "points at and does not restate'. It supplements the two provenance attributions "
        "elsewhere in the file, so (k1) governs. Same grade and same ground as the seed's.",
        anchor="`cowork_notation_adoption_increment.md`, which this section points at and does not restate.",
        scope="document", before=3),
    "docs/llm_integration.md": g(
        CLAUSE,
        "The bar's second named form of clause — 'The ONE detailed design for this section's scope "
        "is X, which this section points at and does not restate' — the same shape as the "
        "bounded-context delegation the bar admits word for word. It supplements the 'Full design "
        "document:' line above it and the two 'See X §n' citations below, so (k1) governs. Same "
        "grade and same ground as the seed's.",
        anchor="for this section's scope is `docs/llm_integration.md`",
        scope="document", before=2, after=1),
    "STATUS.md": g(
        CLAUSE,
        "A subject-is-in-X naming with a delegating predicate and a precedence rule beside it: "
        "'the authoritative, current implemented/planned state lives in STATUS.md. Where a "
        "heading's status and STATUS.md disagree, STATUS.md wins.' The canonical document's own "
        "living-document banner adds the two halves the seed's `docs/scoring_model.md` grade "
        "turns on — it makes the document a mandatory session-start read and binds an update rule "
        "to it ('Update STATUS.md as your last act when anything changes') — and §15 repeats the "
        "authority clause. Graded on the strongest of those namings. ★ ABSENT FROM THE SEED (A3: "
        "this document is nobody's home in the register), and ★ CARRIED INTO THE MEMBER LIST WITH "
        "A FINDING BESIDE IT: its subject is current implementation STATUS, not a specification of "
        "the analysis, and Ruling 6's mechanism carries no exclusion for it. The finding is "
        "reported, not acted on.",
        anchor="implemented/planned state lives in STATUS.md",
        scope="document", before=1, after=1),
    "cowork_idiom_entry_mapping.md": g(
        CLAUSE,
        "A subject-is-X naming with a naming predicate — 'the per-entry re-tag is X' — which is "
        "grammatically the bar's first admitted form (subject, copula, name) rather than the "
        "excluded LABEL-plus-name shape of 'Full spec: X.'. ★ THIS IS THE ONE NEAR-TIE IN THIS "
        "GRADING AND IT IS DECLARED RATHER THAN DEFAULTED. The competing reading: the clause is "
        "semicolon-joined to a sentence reporting what was ratified, so it can be read as an "
        "appended citation of where an artifact lives, which the bar excludes. Under that reading "
        "the document leaves the member list. The verdict taken is ADMITTED, on the form-first "
        "precedence the register applies (form first, kind second and last) and on the register's "
        "own precedent of admitting 'The catalog of what each layer discovers is X'. What turns "
        "on it: this member alone, whose subject is a per-entry data mapping rather than a "
        "specification of the analysis.",
        anchor="`cowork_idiom_entry_mapping.md` (`cowork_style_taxonomy_proposal.md:3-9`;",
        scope="document", before=2, after=1),

    # ── EXCLUDED ────────────────────────────────────────────────────────────────────────────────
    "cowork_key_chord_joint_inference_grounding.md": g(
        BARE_CITATION,
        "The only naming is 'Theory basis: X.' appended to the governing-decision banner — the "
        "bar's first excluded form, a label followed by a name."),
    "OPEN_ITEMS.md": g(
        PROVENANCE,
        "Every naming is a citation of a tracking row — 'tracked at `OPEN_ITEMS.md` OI-nnn', "
        "'(`OPEN_ITEMS.md` OI-nnn item n)' — recording where an open question or a correction is "
        "tracked. A provenance attribution, and the register's own index rather than a "
        "specification of the analysis."),
    "cc_adoption_measurement_report.md": g(
        PROVENANCE,
        "Named once, inside the adoption banner's citation list, as the adoption record."),
    "CLAUDE.md": g(
        PROVENANCE,
        "Every naming cites a standing rule, a principle or the gate block — 'CLAUDE.md gate block "
        "(A)', '`CLAUDE.md` rule (i)', '(`CLAUDE.md` #8; `DEFECT_TYPES.md` DT-2)'. A naming inside "
        "a list of citations or a parenthetical recording where a rule lives; the bar's second "
        "excluded form. ★ The plan's §5 additionally EXCLUDES this document's gate block and "
        "grading conventions by name, as measurement content belonging to the measurement-design "
        "stage."),
    "cowork_handoff.md": g(
        PROVENANCE,
        "Named once, 'per-unit provenance in STATUS.md / `cowork_handoff.md`' — a parenthetical "
        "recording where per-unit provenance is written down."),
    "cc_instruction_notation_switch.md": g(
        PROVENANCE,
        "Named once, in a parenthesis recording which dispatch performed the switch."),
    "DEFECT_TYPES.md": g(
        PROVENANCE,
        "Named once, inside a two-item citation list beside `CLAUDE.md` #8. ★ The plan's §5 "
        "additionally EXCLUDES this document by name, as a catalog of engineering and method "
        "defects carrying almost no musical knowledge."),
    "open_items/OI-176.md": g(
        PROVENANCE,
        "Named once, inside a parenthetical citation list recording where the pre-fit protocols "
        "are tracked."),
    "open_items/OI-177.md": g(
        PROVENANCE,
        "Named once, in the same parenthetical citation list as OI-176's."),
    "cowork_rulings_2026_08_11_fourteenth_stop.md": g(
        PROVENANCE,
        "Named twice, each time in a parenthesis recording where a user ruling was taken — the "
        "bar's second excluded form, word for word."),
    "docs/redesign_plan.md": g(
        BARE_CITATION,
        "Named three times as an appended design reference — 'Design reference: X Step 4 (Phase "
        "D)', 'X (\"single comprehensive pass…\")', 'adopted Phase E direction: X'. All three are "
        "labels followed by a name, and all three sit inside blocks the document itself marks "
        "SUPERSEDED."),
    "cowork_target_architecture_review.md": g(
        BARE_CITATION,
        "Named once, 'Full rationale and literature comparison: X' — a label followed by a name, "
        "inside a block the document marks SUPERSEDED."),
    "docs/architecture_joint_inference.md": g(
        NO_CONCERN,
        "Named once, as the subject of a supersession: 'The X joint-decode synthesis is superseded "
        "by this, retained only as history.' It delegates nothing; it records that a document is "
        "no longer to be built to."),
    "cowork_siloed_facts_audit.md": g(
        PROVENANCE,
        "Named once, as the evidence behind a rule — 'Why: X found 17 instances of a fact being "
        "re-derived by a consumer instead of read from its producer.' Naming a document as the "
        "evidence for a rule records where the reasoning lives; it delegates no concern."),
    "docs/extension_stripping_policy.md": g(
        BARE_CITATION,
        "Named once, 'with the design memo X' appended to a sentence stating how the rule is "
        "implemented."),
    "docs/p3_granularity_ab_3_1b.md": g(
        PROVENANCE,
        "Named once, as the committed evidence a shelving rests on, with the figures deliberately "
        "not carried across. A provenance attribution."),
    "cc_layer1_impl_report.md": g(
        BARE_CITATION,
        "Named once, in a 'See …' citation list of session reports."),
    "cc_layer1_coverage_report.md": g(
        BARE_CITATION,
        "Named once, in the same 'See …' citation list."),
    "cowork_layer2_reslice_design.md": g(
        BARE_CITATION,
        "The only naming is a parenthetical citation appended to a sentence the canonical document "
        "states in its own voice about how the slicer clips to the loaded span. It names a "
        "SECTION, which is why it is graded rather than waved past — but the bar's admitting "
        "second form is a NAMED HOME with sections, and this is a citation supporting a "
        "restatement, not a home. Same grade and same ground as the seed's."),
    "cc_layer2_impl_report.md": g(
        BARE_CITATION,
        "Named once, in a 'See …' citation list of three documents."),
    "cc_layer2_audit_dossier.md": g(
        BARE_CITATION,
        "Named once, in the same 'See …' citation list."),
    "cc_layer3_wiring_report.md": g(
        BARE_CITATION,
        "Named once, in a 'Full provenance:' citation list."),
    "docs/nct_detection_design.md": g(
        NO_CONCERN,
        "Named once, in a sentence recording that the document EXISTS — 'the non-chord-tone filter "
        "is the named lever at OI-55 and OI-68, and X exists'. It delegates nothing."),
    "cowork_l1l4_review_charter.md": g(
        PROVENANCE,
        "Named once, in a parenthesis recording where the L4-build grading was reported."),
    "cowork_phase5b_l4_build_plan.md": g(
        BARE_CITATION,
        "Named once, in a 'Full provenance:' citation list beside the Layer-4 contract and the "
        "Phase-5b commits."),
    "cowork_engage_arc_plan.md": g(
        PROVENANCE,
        "Named once, inside a sentence establishing that the Layer-5 engagement design's authority "
        "is TRANSITIVE — 'the user-ratified X (RATIFIED by the user, 2026-07-07) delegates arcs #9 "
        "and #11 to it by name'. That is a statement about a delegation the ARC PLAN writes, not a "
        "delegation this document writes TO the arc plan. Rule (j) is the ruling that keeps the "
        "two roles apart: delegating to a document and being a home are different tests with "
        "different subjects."),
    "cc_tonicization_modulation_metric_dossier.md": g(
        PROVENANCE,
        "Named once, as the record every figure of that measurement lives in and is not restated "
        "from (#17f, D-431). A provenance attribution."),
    "cowork_rulings_2026_08_09_second_stop.md": g(
        PROVENANCE,
        "Named once, in a parenthesis recording which ruling corrected a passage."),
    "docs/scoring_model.md": g(
        BARE_CITATION,
        "The only naming in this document is 'see X §\"ScoringPhase\"' appended to a parenthesis "
        "about a replaced flag — a bare appended citation. ★ THE DOCUMENT IS A MEMBER ANYWAY, by "
        "LIMB 3 of the ruling, which names it directly; this grade decides only that "
        "`ARCHITECTURE.md` does not delegate to it."),
    "docs/prompts/iteration_64_root_present_prefilter.md": g(
        BARE_CITATION,
        "Named once, 'Instruction at X.' — a label followed by a name."),
    "docs/key_path_design.md": g(
        PROVENANCE,
        "Named once, with line numbers, inside a parenthesis recording where a removal is dated "
        "and its re-targeted pins named."),
    "docs/iter90_bass_as_root_promotion_shelved.md": g(
        BARE_CITATION,
        "Named once, 'see X for characterization and Iter 91 design' appended to a sentence about "
        "where a fix belongs."),
    "_design.md": g(
        NO_CONCERN,
        "★ NOT A DOCUMENT NAMING AT ALL: this is the tail of the document-governance clause's GLOB "
        "`cowork_layer*_design.md`, which the scan sees as a filename because the glob's asterisk "
        "is not a filename character. Rule (k) settles what it confers: 'A glob pattern and a "
        "trailing ellipsis CONFER NOTHING.' It is graded rather than filtered out so that the "
        "scan's own population stays the population."),
    "STYLE_AUTHORING_GUIDE.md": g(
        NO_CONCERN,
        "Named once, as a filename inside the planned styles-directory listing in a code block. "
        "Not a naming of a repository document in prose."),
    "cowork_style_taxonomy_proposal.md": g(
        PROVENANCE,
        "Named five times, every one a parenthetical citation with line numbers recording where "
        "the taxonomy proposal, its corroborations, its admission basis and its retired genre list "
        "are written down — with one 'Full proposal + the surveyed corpora:' citation list. All "
        "excluded forms."),
    "cowork_idiom_discovery_findings.md": g(
        PROVENANCE,
        "Named once, as a parenthetical citation by document AND line recording where a "
        "measurement is written down. Same grade and same ground as the seed's."),
    "cowork_style_clustering_plan.md": g(
        PROVENANCE,
        "Named twice, both parenthetical citations recording where the committed clustering work "
        "is described — once inside a 'Full proposal + the surveyed corpora:' list."),
    "backlog_drift_reset.md": g(
        BARE_CITATION,
        "Named once, '(see X)' appended to a sentence about a future marker."),
    "backlog_invisible_split.md": g(
        BARE_CITATION,
        "Named once, 'See X.' — the bar's first excluded form, word for word."),
    "docs/quality_observations_iter76.md": g(
        BARE_CITATION,
        "Named once, 'See X for the recommended workflow.'"),
    "docs/submission_scope.md": g(
        NO_CONCERN,
        "Named once, inside a phase checklist as a document to be CREATED — 'Create submission "
        "scope document (X)'. It delegates nothing; the document is an output of a phase that has "
        "not started."),
    "docs/rfc_musescore_forum_post.md": g(
        PROVENANCE,
        "Named once, in the document's own version-history paragraph, recording where an RFC draft "
        "was written."),
    "docs/chordlist_bug_report.md": g(
        PROVENANCE,
        "Named once, in the same version-history paragraph."),
}

# ── AUTHORED — the two declared properties per member ─────────────────────────────────────────────
#   member -> dict(live: (file, anchor) | None, live_value, est: (file, anchor) | None, est_value)
# A property is UNDECLARED where no banner and no rule says it; nothing is inferred.
UND = "UNDECLARED"


def p(live_value, live_file=None, live_anchor=None,
      est_value=UND, est_file=None, est_anchor=None, remark=None):
    return {"live_or_dormant": live_value, "live_file": live_file, "live_anchor": live_anchor,
            "declared_establishment_status": est_value, "est_file": est_file,
            "est_anchor": est_anchor, "remark": remark}


PROPERTIES: dict[str, dict] = {
    "ARCHITECTURE.md": p(
        "LIVE", "ARCHITECTURE.md", "This is **THE canonical architecture doc**",
        remark="The canonical specification; its own document-governance block declares it so."),
    "docs/scoring_model.md": p(
        "DORMANT (its mechanism content)", "docs/scoring_model.md",
        "Its mechanism content describes the LEGACY",
        "DECLARED NOT ESTABLISHED", "docs/scoring_model.md",
        "they are UNFALSIFIED, NOT ESTABLISHED",
        remark="The banner declares the DOCUMENT a live mandatory reference and its MECHANISM "
               "content dormant on both production surfaces; both halves are quoted."),
    "cowork_joint_estimator_architecture.md": p(
        "LIVE", "ARCHITECTURE.md",
        "the joint estimator\n> is now the PRODUCTION inference layer on the batch/corpus surface"),
    "cowork_joint_estimator_factorization.md": p(
        "LIVE", "ARCHITECTURE.md",
        "is `cowork_joint_estimator_factorization.md`, which this section points at",
        "Values remain unfit.", "cowork_joint_estimator_factorization.md",
        "Values remain unfit.",
        remark="LIVE by the delegation's own words — it is the ratified contract for the factor "
               "structure of the production inference layer."),
    "cowork_prefit_gates.md": p(
        UND, None, None,
        'protocol ratified — pending execution', "cowork_prefit_gates.md",
        'rows read "protocol ratified — pending execution"'),
    "cowork_notation_output_contract.md": p(
        "DORMANT (as declared at the naming)", "ARCHITECTURE.md",
        "as-built, DORMANT; contract `cowork_notation_output_contract.md`",
        remark="The declaration is the delegating line's own parenthesis. It describes the "
               "A-native record as as-built and dormant at the time that line was written; the "
               "record path has since become the production notation path (the same document's "
               "record-path section). Both are quoted rather than reconciled here."),
    "cowork_stage5_fitter_design.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a SIGNING (user, 2026-07-04), which is a ratification status "
               "and not a live/dormant or establishment declaration."),
    "cowork_score_census.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares delivery of v1 and awaits user disposition of the acquisition "
               "tiers — neither a live/dormant nor an establishment declaration."),
    "cowork_progression_schema_dictionary.md": p(
        "DORMANT", "ARCHITECTURE.md",
        "Until the RECOGNITION CONSUMER is built, the function layer does not touch this vocabulary"),
    "cowork_progression_schema_design.md": p(
        "DORMANT", "ARCHITECTURE.md", "Scaffolding-first, deferred."),
    "cowork_target_architecture.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a governance demotion, not a live/dormant state of the "
               "analysis."),
    "cowork_confidence_contract.md": p(
        "LIVE (as the standard, with a declared departure)", "ARCHITECTURE.md",
        "The production notation record path departs from",
        remark="The canonical document declares the contract the standard the shipped record path "
               "is measured against, and declares the departure unresolved."),
    "cowork_layer6_grouping_design.md": p(
        "DORMANT", "cowork_layer6_grouping_design.md",
        "built dormant + oracle-validated after the extension gate passed"),
    "cowork_voiceleading_axis_design.md": p(
        "DORMANT", "cowork_voiceleading_axis_design.md",
        "The dormant\n> foundation is built, tested, and gate-proven"),
    "cowork_bounded_context_design.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a SIGNING and the L6 gate, not a live/dormant state."),
    "cowork_evidence_inventory.md": p(
        UND, None, None, UND, None, None,
        remark="The document carries no status banner."),
    "cowork_layer1_note_model_design.md": p(
        "LIVE", "ARCHITECTURE.md",
        "#### Layer 1 — the lossless note model (Built+Live)"),
    "cowork_phrase_boundary_design.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a SIGNING and a build in progress, neither of which states a "
               "live or dormant state on a production surface."),
    "cowork_layer2_slicing_design.md": p(
        "LIVE", "ARCHITECTURE.md",
        "#### Layer 2 — the deterministic change-point slicer (Built+Live — consumed by L3)"),
    "cowork_layer3_keymode_design.md": p(
        "DORMANT", "ARCHITECTURE.md",
        "#### Layer 3 — key/mode is the sequence decoder (Built+Dormant)"),
    "cowork_layer4_chordsymbol_design.md": p(
        "DORMANT", "ARCHITECTURE.md",
        "#### Layer 4 — the per-slice chord-symbol decoder (Built+Dormant — not wired)"),
    "cowork_layer5_function_design.md": p(
        "DORMANT", "ARCHITECTURE.md",
        "#### Layer 5 — the function/cadence layer (Built+Dormant — design ratified; consumed by L6)"),
    "cowork_layer5_engagement_design.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a read-only design pass, not a live or dormant state."),
    "cowork_notation_adoption_increment.md": p(
        UND, None, None, UND, None, None,
        remark="Its banner declares a user ratification, which is neither property."),
    "docs/llm_integration.md": p(
        "DORMANT (nothing built)", "docs/llm_integration.md",
        "Design phase. No code written yet."),
    "STATUS.md": p(
        "LIVE", "STATUS.md", "**Living document.**"),
    "cowork_idiom_entry_mapping.md": p(
        "DORMANT", "ARCHITECTURE.md",
        "replaced in the dormant `harmonicvocabulary` component",
        "Provisional, easy to revise.", "cowork_idiom_entry_mapping.md",
        "Provisional, easy to revise."),
}

LIMB_3 = "docs/scoring_model.md"

NAME_RE = re.compile(r"[A-Za-z0-9_./-]+\.md\b")


# ── locating, with the STOPs that keep a citation from going stale ────────────────────────────────
def read_lines(path: Path) -> list[str]:
    if not path.exists():
        raise Stop(f"a file the derivation reads is missing: {path}")
    return path.read_text(encoding="utf-8").split("\n")


def locate(lines: list[str], anchor: str, where: str) -> int:
    """Return the 1-based line number carrying `anchor`. Missing or ambiguous STOPs."""
    if "\n" in anchor:                       # an anchor spanning two lines
        head, tail = anchor.split("\n", 1)
        hits = [i for i in range(len(lines) - 1)
                if head in lines[i] and tail in lines[i + 1]]
    else:
        hits = [i for i, ln in enumerate(lines) if anchor in ln]
    if not hits:
        raise Stop(f"{where}: anchor not found — {anchor!r}")
    if len(hits) > 1:
        raise Stop(f"{where}: anchor matches {len(hits)} lines — {anchor!r}")
    return hits[0] + 1


def passage(lines: list[str], line_no: int, before: int, after: int) -> str:
    lo = max(0, line_no - 1 - before)
    hi = min(len(lines), line_no + after)
    return "\n".join(lines[lo:hi])


def heading_level(line: str) -> int | None:
    m = re.match(r"^(#{1,6})\s", line)
    return len(m.group(1)) if m else None


def region_range(lines: list[str], heading: str) -> tuple[int, int, str]:
    start = locate(lines, heading, "limb-1 region")
    lvl = heading_level(lines[start - 1])
    if lvl is None:
        raise Stop(f"limb-1 region anchor is not a heading line: {heading!r}")
    end = len(lines)
    for i in range(start, len(lines)):
        h = heading_level(lines[i])
        if h is not None and h <= lvl:
            end = i
            break
    return start, end, lines[start - 1].strip()


# ── the seed, read as a seed and never as the population ──────────────────────────────────────────
def seed_admitted_in_architecture() -> dict[str, dict]:
    sys.path.insert(0, str(ROOT / "tools" / "audit" / "decisions"))
    import gen_phase1p_delegation_bar as seed          # noqa: E402  (path set above)
    out = {}
    for doc, (form, surface, anchor, why) in seed.FORMS.items():
        if surface == "ARCHITECTURE.md" and form in seed.ADMITTING:
            out[doc] = {"form": form, "anchor": anchor, "retired": False}
    for doc, (form, surface, anchor, why) in seed.RETIRED_FORMS.items():
        if surface == "ARCHITECTURE.md" and form in seed.ADMITTING:
            out[doc] = {"form": form, "anchor": anchor, "retired": True}
    return out


def build() -> dict:
    arch = read_lines(ARCH)
    claude = read_lines(CLAUDE)

    # ── DERIVED: the candidate population — every naming of another .md document ─────────────────
    namings: dict[str, list[dict]] = {}
    for i, ln in enumerate(arch, start=1):
        for m in NAME_RE.finditer(ln):
            tok = m.group(0)
            if tok == "ARCHITECTURE.md":
                continue
            namings.setdefault(tok, []).append({"line": i, "line_text": ln.strip()})

    scanned = set(namings)
    authored = set(GRADES)
    unclassified = sorted(scanned - authored)
    if unclassified:
        raise Stop(f"scanned target(s) with no authored grade: {unclassified} — a document named "
                   f"by a later edit may not enter the population unclassified")
    stray = sorted(authored - scanned)
    if stray:
        raise Stop(f"authored grade(s) for target(s) the scan does not find: {stray}")

    # ── DERIVED: the deciding clauses, located in CLAUDE.md on every run ─────────────────────────
    clauses = {}
    for name, anchor in DECIDING_CLAUSES.items():
        ln = locate(claude, anchor, f"CLAUDE.md deciding clause {name}")
        clauses[name] = {"citation": f"CLAUDE.md:{ln}", "text": claude[ln - 1].strip()}

    # ── the grades, each with its governing naming located and quoted at HEAD ────────────────────
    graded = []
    for target in sorted(GRADES):
        spec = GRADES[target]
        form = spec["form"]
        if form not in FORMS_VOCABULARY:
            raise Stop(f"{target}: form {form!r} is outside the five-class vocabulary")
        rec = {
            "target": target,
            "form": form,
            "admitted": form in ADMITTING,
            "why_this_grade": spec["why"],
            "decided_by": ("rule_(i)_admitted" if form in ADMITTING
                           else "rule_(i)_not_admitted"),
            "namings_in_ARCHITECTURE.md": namings[target],
            "namings_counted": len(namings[target]),
        }
        if form in ADMITTING:
            if not spec["anchor"]:
                raise Stop(f"{target}: an ADMITTED grade carries no anchor")
            ln = locate(arch, spec["anchor"], f"the governing naming of {target}")
            if target not in arch[ln - 1]:
                raise Stop(f"{target}: the governing anchor sits at ARCHITECTURE.md:{ln}, which "
                           f"does not name that target")
            if spec["scope"] not in ("document", "sections"):
                raise Stop(f"{target}: scope {spec['scope']!r} is not 'document' or 'sections'")
            if spec["scope"] == "sections" and not spec["sections"]:
                raise Stop(f"{target}: a 'sections' scope names no sections")
            rec["the_governing_naming"] = {
                "citation": f"ARCHITECTURE.md:{ln}",
                "passage_verbatim": passage(arch, ln, spec["before"], spec["after"]),
            }
            rec["delegation_scope"] = spec["scope"]
            rec["delegated_sections"] = spec["sections"]
            rec["scope_decided_by"] = "rule_(h)_granularity"
            if len(namings[target]) > 1:
                rec["other_namings_do_not_undo_it"] = "rule_(k1)_the_strongest_naming_governs"
        graded.append(rec)

    admitted = [r for r in graded if r["admitted"]]

    # ── A3: the seed, reconciled BOTH WAYS ──────────────────────────────────────────────────────
    seed = seed_admitted_in_architecture()
    seed_refound, seed_missing = [], []
    for doc, s in sorted(seed.items()):
        try:
            ln = locate(arch, s["anchor"], f"the seed's anchor for {doc}")
        except Stop:
            seed_missing.append(doc)
            continue
        seed_refound.append({"document": doc, "seed_form": s["form"],
                             "retired_in_the_seed": s["retired"],
                             "re_found_at": f"ARCHITECTURE.md:{ln}"})
    if seed_missing:
        raise Stop(f"seed-admitted delegation(s) the text does not carry: {seed_missing} — the "
                   f"seed is then wrong about the tree, which is a finding bearing on the record "
                   f"and not this batch's to repair")

    seed_live = {d for d, s in seed.items() if not s["retired"]}
    text_admitted = {r["target"] for r in admitted}
    absent_from_the_seed = sorted(text_admitted - seed_live)
    misses = len(absent_from_the_seed)
    denom = len(text_admitted)

    # ── limb 1: the three regions, their line ranges DERIVED from the file's own headings ────────
    regions = []
    for label, headings in LIMB_1_REGIONS:
        parts = []
        for h in headings:
            s, e, text = region_range(arch, h)
            parts.append({"heading": text, "first_line": s, "last_line": e, "lines": e - s + 1})
        regions.append({"region": label, "sections": parts,
                        "lines_total": sum(x["lines"] for x in parts)})

    # ── the member list, DERIVED from the grades ─────────────────────────────────────────────────
    members = []

    def member(path, limb, scope, sections, note=None):
        props = PROPERTIES.get(path)
        if props is None:
            raise Stop(f"member {path} carries no authored property block")
        rec = {"member": path, "limb": limb, "delegation_scope": scope,
               "delegated_sections": sections,
               "file_exists_at_the_tree": (ROOT / path).exists()}
        for kind, val_key, file_key, anchor_key in (
                ("live_or_dormant", "live_or_dormant", "live_file", "live_anchor"),
                ("declared_establishment_status", "declared_establishment_status",
                 "est_file", "est_anchor")):
            value, f, a = props[val_key], props[file_key], props[anchor_key]
            entry = {"value": value}
            if a:
                lines = arch if f == "ARCHITECTURE.md" else read_lines(ROOT / f)
                ln = locate(lines, a, f"{path} property {kind}")
                entry["quote"] = lines[ln - 1].strip()
                entry["at"] = f"{f}:{ln}"
            else:
                entry["quote"] = None
                entry["at"] = None
            rec[kind] = entry
        if props["remark"]:
            rec["remark"] = props["remark"]
        if note:
            rec["note"] = note
        return rec

    members.append(member("ARCHITECTURE.md", "limb 1 — the canonical specification",
                          "sections", [r["region"] for r in regions],
                          note="The three regions the ruling names; their line ranges are above."))
    for r in admitted:
        members.append(member(r["target"], "limb 2 — an admitted delegation target",
                              r["delegation_scope"], r["delegated_sections"]))
    if LIMB_3 not in {m["member"] for m in members}:
        members.append(member(LIMB_3, "limb 3 — the ruled pilot subject", "document", None,
                              note="Named directly by Ruling 6's third limb. `ARCHITECTURE.md` "
                                   "does not delegate to it: its only naming there is a bare "
                                   "appended citation."))

    members_with_no_file = [m["member"] for m in members if not m["file_exists_at_the_tree"]]

    return {
        "what_this_is": (
            "THE SPECIFICATION DOCUMENT SET, derived from `ARCHITECTURE.md`'s admitted delegations "
            "under Ruling 6 of `cowork_rulings_2026_08_21_successor_plan_sitting.md`. It derives "
            "no specification, admits no fact, and takes no view on whether any member's content "
            "is right."),
        "dispatch": "cc_instruction_successor_plan_landing_and_step_zero.md",
        "ruling": (
            "Ruling 6 (Alternative A): \"Three limbs, as plan §5 states them: `ARCHITECTURE.md` "
            "(the analysis layers' sections, the joint estimator's standing-rules section, "
            "document governance); every document `ARCHITECTURE.md` delegates to in a form the "
            "delegation-form rule admits (`CLAUDE.md` decisions-register rule (i)), each "
            "delegating line quoted; and `docs/scoring_model.md`. The decisions register's home "
            "population is NOT the source. Whether `ARCHITECTURE.md`'s delegations are complete "
            "is recorded as a finding, not assumed. Three properties travel with every member: "
            "its pollution distribution (Ruling 7), LIVE or DORMANT, and its declared "
            "establishment status.\""),
        "generator": "tools/audit/gen_specification_document_set.py",
        "reproduce": ("python tools/audit/gen_specification_document_set.py --check   "
                      "# re-derives and exits 1 on any drift"),
        "what_is_DERIVED": [
            "the candidate population — every naming of another .md document in ARCHITECTURE.md, "
            "scanned from the file, with the line and the line's own text",
            "the member list, from the authored grades",
            "the three limb-1 regions' line ranges, from the file's own headings",
            "every count",
            "the both-ways reconciliation against the delegation seed and its miss rate",
            "whether each member's file exists at the tree",
            "every quoted passage and every quoted property, read from the file at HEAD",
        ],
        "what_is_AUTHORED": [
            "the grade per named target under CLAUDE.md rule (i), with (h) and (k)/(k1)",
            "for an ADMITTED target, the anchor of the naming that GOVERNS, and the scope",
            "the two declared properties per member, each as an anchor into the declaring file",
            "the three limb-1 regions' heading list",
        ],
        "the_form_vocabulary": {
            "admitted": sorted(ADMITTING),
            "excluded": sorted(FORMS_VOCABULARY - ADMITTING),
            "★_four_of_the_five_are_the_bar's_own": (
                "explicit-delegation-clause, named-home-with-sections, bare-appended-citation and "
                "provenance-attribution are `CLAUDE.md` rule (i)'s own four forms, quoted below. "
                "naming-that-delegates-no-concern is THIS TOOL'S OWN residue class, declared as "
                "such: a naming that is neither a citation nor a delegation — a filename inside a "
                "directory listing, a document named as superseded, a document named as one to be "
                "created. It admits nothing, so it can only narrow the set, never widen it."),
        },
        "the_deciding_clauses_located_in_CLAUDE.md": clauses,
        "counted": {
            "targets_named_in_ARCHITECTURE.md": len(namings),
            "namings_scanned": sum(len(v) for v in namings.values()),
            "targets_by_form": dict(sorted(Counter(r["form"] for r in graded).items())),
            "targets_ADMITTED": len(admitted),
            "members_total": len(members),
            "members_by_limb": dict(sorted(Counter(m["limb"] for m in members).items())),
            "members_by_delegation_scope": dict(
                sorted(Counter(m["delegation_scope"] for m in members).items())),
            "members_with_no_file": len(members_with_no_file),
            "members_by_live_or_dormant": dict(
                sorted(Counter(m["live_or_dormant"]["value"] for m in members).items())),
            "members_by_declared_establishment_status": dict(
                sorted(Counter(m["declared_establishment_status"]["value"]
                               for m in members).items())),
        },
        "the_limb_1_regions": regions,
        "the_grades": graded,
        "the_seed_reconciliation": {
            "what_the_seed_is": (
                "`tools/audit/decisions/gen_phase1p_delegation_bar.py`'s FORMS and RETIRED_FORMS "
                "tables. They were produced to answer WHERE DOES A REGISTER ENTRY LIVE, over the "
                "entries' home documents — not to enumerate every delegation `ARCHITECTURE.md` "
                "writes. Read here as a SEED and never as the population (the dispatch's "
                "assumption A3)."),
            "seed_admitted_delegations_sited_in_ARCHITECTURE.md": seed_refound,
            "every_one_re_found_at_the_text": True,
            "text_found_admitted_delegations_absent_from_the_live_seed": absent_from_the_seed,
            "miss_rate_against_the_seed": {
                "misses": misses,
                "of_admitted_targets": denom,
                "rate": round(misses / denom, 4) if denom else None,
                "★_what_a_miss_means_here": (
                    "A miss is a delegation THIS derivation finds at the text that the seed's LIVE "
                    "table does not carry. It is not evidence that the seed is wrong: the seed's "
                    "population is the register's home documents, so a delegation to a document "
                    "that is nobody's home is outside what the seed ever looked at, and a "
                    "delegation whose target was emptied by a re-homing or a soft-discard was "
                    "RETIRED out of the seed's live table by design. Both causes are named per "
                    "document in `the_grades`. The rate is published because a derivation's "
                    "measured miss rate against the record is part of its name (D-661)."),
            },
        },
        "the_document_set": members,
        "the_members_with_no_file": members_with_no_file,
        "★_the_findings_this_derivation_records_rather_than_acts_on": [
            "WHETHER `ARCHITECTURE.md`'S DELEGATIONS ARE COMPLETE IS NOT ASSERTED, and the ruling "
            "asks for it as a finding. What this derivation establishes is what the canonical "
            "document DOES delegate, graded naming by naming. It cannot see a specification the "
            "canonical document never names — and one class of such a document is visible from "
            "inside the derivation itself: the document-governance clause reaches its per-layer "
            "and per-component design documents through a GLOB and a trailing ELLIPSIS, both of "
            "which rule (k) makes confer nothing, so any design document that is not separately "
            "named by filename is outside the set although the clause plainly means to include "
            "it. Every layer specification in this set is in it by a separate delegation the user "
            "wrote, not by that clause.",
            "THE SET CONTAINS A STATUS SURFACE. `STATUS.md` is a member by the ruled mechanism: "
            "`ARCHITECTURE.md` makes it a mandatory session-start read, binds an update rule to "
            "it, and gives it precedence over its own §5 headings on current state. Its subject "
            "is current implementation status, not a specification of the analysis, and the "
            "plan's §5 exclusion list does not reach it. Reported, not acted on.",
            "THE SET CONTAINS A DATA MAPPING. `cowork_idiom_entry_mapping.md` is a member on the "
            "ONE near-tie in this grading, which is declared at its own grade with both readings "
            "and the consequence of each.",
            "TWO MEMBERS ARE ABSENT FROM THE SEED'S LIVE TABLE BECAUSE THE SEED RETIRED THEM, NOT "
            "BECAUSE THE TEXT LOST THEM — `cowork_layer1_note_model_design.md` and "
            "`cowork_layer2_slicing_design.md`. Both delegations stand at the text word for word. "
            "The cause is that every register entry homed in each was retired by a ruled "
            "soft-discard, which emptied the document out of the seed's home population.",
            "THE `LIVE OR DORMANT` PROPERTY IS UNDECLARED FOR SEVERAL MEMBERS AND IS NOT "
            "INFERRED. Ruling 6's own words are that it is quoted or UNDECLARED; a banner "
            "declaring a SIGNING, a RATIFICATION or a DELIVERY is neither of the two properties "
            "and is recorded as such in the member's remark.",
        ],
        "what_this_does_NOT_do": (
            "It edits no document. It restores nothing, reverts nothing and corrects nothing. It "
            "closes no open-items row and writes no decisions-register entry. It derives no "
            "specification statement, admits no fact into any ledger, builds no frame, and "
            "authorizes no pilot act."),
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: specification_document_set.json does not re-derive")
            return 1
        print("the specification document set re-derives")
    else:
        OUT.write_text(text, encoding="utf-8", newline="")
        print(f"wrote {OUT.relative_to(ROOT)}")
    c = art["counted"]
    print(f"  targets named {c['targets_named_in_ARCHITECTURE.md']}; "
          f"namings {c['namings_scanned']}; admitted {c['targets_ADMITTED']}")
    print(f"  members {c['members_total']}; with no file {c['members_with_no_file']}")
    r = art["the_seed_reconciliation"]["miss_rate_against_the_seed"]
    print(f"  seed misses {r['misses']} of {r['of_admitted_targets']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as e:
        print(f"STOP: {e}")
        sys.exit(2)
