#!/usr/bin/env python3
"""THE RULING SURFACE FOR THE ARTIFACT INVENTORY — one section per class, every verdict PROPOSED.

Dispatch: `cc_instruction_artifact_inventory.md`, Task 2 (Cowork, 2026-08-15), executing §2.10 of
`cowork_rulings_2026_08_15_method_directions.md`: *"per class: role per phase, mining verdict
(including antipattern mining), retirement-candidate flag ... Verdicts are PROPOSED by the tool's
surface and RULED by the user."*

WHY IT IS GENERATED RATHER THAN WRITTEN.  Every count, every member list and every split on this
surface comes from `tools/audit/artifact_inventory.json` or from a scan this file performs — none
is typed by hand (#17f, D-431).  What is authored is the PROPOSAL per class, and it is marked as
authored on its face, so a reader can see exactly where the judgment starts.

WHAT IS DERIVED AND WHAT IS AUTHORED:

  DERIVED  — the class list, every count, every total in bytes and every member list, imported
             whole from the inventory artifact; and THE CITATION SCAN, which reads the governing
             record and reports, per file, whether the record names it anywhere.
  AUTHORED — the PROPOSAL per class: its role, its mining verdict, its retirement-candidate flag
             and the reason for each; which classes are presented as QUESTIONS rather than
             proposals; and, for the four mixed classes, which proposal attaches to each side of
             the derived citation split.

THE CITATION SCAN, and why it is the load-bearing derived signal.  The user's §2.11 says of the
writing side's own design documents that they are *"NOT direct witnesses — their value is measured
by what the curation acts extract (fact-based, not presumed)"*.  A file the governing record never
names is not thereby worthless, but it is a different object from one the record leans on, and the
difference is a FACT rather than an impression.  So the four classes where specifications, reports,
plans and one-off diagnostics interleave are split by that fact and proposed per side.

  WHAT THE SCAN DOES NOT ESTABLISH, stated before its first use: a citation is evidence that
  something reads the file, NOT that the file is correct, current, or worth keeping; and an absent
  citation is evidence of nothing being pointed at it from the governing record, NOT that nothing
  anywhere depends on it. The scan reads the governing documents and the two registers' detail
  files; a reference from a source outside that set is invisible to it and the surface says so.

THE STOPS:
  1. a class in the inventory with NO authored proposal is a STOP — the whole point of the surface
     is that the user rules on every class, and a class that quietly reached no section would be
     ruled on by omission;
  2. a proposal naming a class the inventory does not carry is a STOP — in either direction, so
     the two files cannot drift apart (#6);
  3. a role or mining verdict outside the closed vocabulary the dispatch names is a STOP;
  4. a proposal with no reason is a STOP.

WHAT THIS DOES NOT DO.  It moves, renames, retires, archives and deletes nothing — every
retirement on this surface is a CANDIDATE FLAG awaiting the user, and retirement itself is
archive-with-record under #12: nothing is destroyed. It rules nothing, ratifies nothing, and
performs no mining.

Usage:
  python tools/audit/gen_artifact_inventory_surface.py            # write the surface
  python tools/audit/gen_artifact_inventory_surface.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
INVENTORY = ROOT / "tools" / "audit" / "artifact_inventory.json"
OUT = ROOT / "ratification_surfaces" / "cowork_artifact_inventory_ruling_surface.md"


class Stop(Exception):
    """A demand of the surface is unmet. Never a warning, never a class left unproposed."""


# ── the closed vocabularies, taken from the dispatch's own words ─────────────────────────────────
ROLES = (
    "clean-room admissible",
    "airlock input",
    "mining witness",
    "audit material",
    "regression pin",
    "operational apparatus",
    "outside every phase's inputs",
)
MINING = (
    "mine directly",
    "mine via the airlock",
    "mine via the airlock for antipatterns",
    "not worth mining",
)

PROPOSAL = "PROPOSAL"
QUESTION = "QUESTION"
SPLIT = "SPLIT"      # the class carries no single verdict; the proposals sit one per side below

# ── AUTHORED — the governing record the citation scan reads ──────────────────────────────────────
GOVERNING_DOCUMENTS = ("CLAUDE.md", "ARCHITECTURE.md", "BUILD_AND_TEST.md", "DECISIONS.md",
                       "OPEN_ITEMS.md", "STATUS.md", "DEFECT_TYPES.md")
GOVERNING_DIRECTORIES = ("decisions", "open_items")

# ── AUTHORED — the four classes descended into, and why each is mixed ────────────────────────────
# Prediction P2 named `docs/`, `tools/` and the repository-root prose surfaces as the places where
# per-item descent would be needed.  These are those places.  Each is split by the DERIVED citation
# scan and proposed per side; no member is proposed on individually, which is what the dispatch
# means by bulk rules carrying their counts.
MIXED_CLASSES = {
    "documentation-directory-prose":
        "One directory holds layer specifications, design documents, reconstructions of what a "
        "mechanism was, policies, and dated findings from single iterations. They cannot share a "
        "verdict: a specification is a witness the derivation must read against, and a dated "
        "finding about one iteration is at most airlock material.",
    "measurement-and-analysis-tools":
        "One directory holds the pinned measurement tools the hard stop and the corpus commands "
        "depend on, and a long tail of single-iteration diagnostics written to answer one question "
        "and never run again. Retiring the first kind would break a gate; keeping the second kind "
        "in every phase's inputs is the noise the inventory exists to remove.",
    "writing-side-design-documents":
        "One naming convention covers ratified contract documents that governing surfaces delegate "
        "to, and exploratory drafts that were superseded the week they were written. The user's "
        "own direction is that these are NOT direct witnesses and that their value is measured "
        "rather than presumed.",
    "reports-from-the-coding-side":
        "One naming convention covers measurement reports the gate block cites as provenance and "
        "one-off diagnostic write-ups. The first kind is evidence for the empirical findings "
        "ledger; the second is at most an antipattern source.",
}

# ── AUTHORED — the proposal per class ────────────────────────────────────────────────────────────
# Shape: class -> (presentation, role, mining verdict, retirement-candidate flag, reason).
# For a class in MIXED_CLASSES the entry is a pair of proposals, one per side of the citation
# split, under the keys `cited` and `uncited`.

P = dict  # readability only


PROPOSALS: dict[str, dict] = {

    # ---- our own analysis --------------------------------------------------------------------
    "our-analysis-source": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="The clean room's whole content is that the derivation NEVER looks at the "
               "implementation — the user's own words. This class IS the implementation. It is "
               "not a mining source either: a fact read out of the code is exactly the kind of "
               "influence eighteenth-stop Ruling 5 says is invisible in the text afterwards. It "
               "becomes the SUBJECT of the audit once the derived specifications exist, which is "
               "a role it holds in a later phase and not an input to any earlier one."),

    "our-analysis-tests-and-fixtures": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="§2.11 of the method-directions record sends the classification of the tests and "
               "the catalogs here rather than deciding it. The QUESTION, stated at the width the "
               "record leaves it: a test asserts what the code SHOULD do, so it reads like design "
               "intent — but it was written beside the code and passes because the code passes it, "
               "so it may be the mirror rather than the world. And the two "
               "`chordanalyzer_catalog*.musicxml` files are ground truth this project authored, "
               "which gate block (A)'s own convention bars from ever being a standard of "
               "correctness. Three sub-questions the user may want to answer separately: are the "
               "tests clean-room admissible, airlock input, or outside every phase; do the "
               "catalogs differ from the tests in that answer; and does a failing test become "
               "audit material of a different kind from a passing one."),

    "our-pipeline-snapshot-goldens": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="Named explicitly in §2.11 as decided here. These pin the current output of the "
               "P1/P2/P3/P4 path piece by piece. They are self-annotation in the exact sense gate "
               "block (A) bars from being a standard of correctness — they hold behaviour against "
               "change and say nothing about whether the behaviour is right. The QUESTION is "
               "whether that makes them a regression pin the phases keep and never read as "
               "evidence, or material the derivation must be walled off from entirely."),

    "our-pipeline-snapshot-test-harness": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="The suite that reads those goldens, sent here with them by §2.11. Its corpus "
               "description states which pieces are pinned and why, which is closer to design "
               "intent than the goldens themselves are."),

    "our-measurement-tool-test-material": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="§2.11 sends the classification of tests here without distinguishing which tests. "
               "These check the measurement tools rather than the analysis — the cross-language "
               "constant checks and the parser fixtures — so the answer may differ from the answer "
               "for the analysis tests, and the surface does not assume it does not."),

    # ---- code we did not write -----------------------------------------------------------------
    "third-party-vendored-code": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="Vendored libraries with their own upstream history, carried so the application "
               "builds. Nothing in them bears on harmonic analysis, and they are not ours to "
               "retire. This is one of the three subjects prediction P1 named as ONE class with "
               "one verdict, and it is."),

    "upstream-application-source": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="MuseScore's own application code. It is the implementation for the same reason "
               "our analysis source is, and the fork's recorded edits inside it are enumerated by "
               "their own mechanisms (`tools/audit/local_patches_check.py` and the arm comment "
               "sweep) rather than by any phase reading this class. ★ ONE CAVEAT THE USER SHOULD "
               "SEE BEFORE RULING: this class carries our fork-local edits mixed in with upstream "
               "code, and no signature separates them — so `outside every phase's inputs` is a "
               "verdict about the class, not a claim that nothing in it matters."),

    "upstream-application-resources": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="Templates, translations, sounds, styles, icons and type faces shipped with the "
               "application. Largest class by bytes and empty of anything the derivation reads."),

    "upstream-application-tests": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="MuseScore's integration suite and its visual regression material. Distinct from "
               "the tests question above, which is about OUR tests: nothing here tests harmonic "
               "analysis."),

    "build-and-continuous-integration-configuration": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="How the fork is built and checked. The second of P1's three named subjects, and "
               "one class with one verdict as predicted."),

    "repository-metadata-and-legal-notices": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="The repository's own configuration and its notices. ★ ONE MEMBER IS NOT INERT AND "
               "IS FLAGGED RATHER THAN BURIED: `.gitignore` carries the rule `/cc_*.md`, which "
               "ignores the entire dispatch-and-report family — see the finding published with the "
               "untracked appendix below."),

    # ---- the governing record ------------------------------------------------------------------
    "governing-documents": P(
        presentation=PROPOSAL, role="clean-room admissible",
        mining="mine directly", retirement_candidate=False,
        reason="The seven documents a session is instructed to read. They carry the principles, "
               "the ruled conventions and the standing constraints the derivation is conducted "
               "under — the world rather than the mirror. ★ TWO QUALIFICATIONS THE USER ALREADY "
               "RULED AND THIS SURFACE DOES NOT RE-OPEN: `CLAUDE.md` is explicitly replaceable for "
               "a deriving session's curated boot (§2.2), and D-231's truth half plus the phase "
               "structure inside it are superseded and not yet rewritten. So `clean-room "
               "admissible` is proposed for the CLASS, and which text a deriving session actually "
               "boots from is the separate curated-boot ruling the record already lists as owed."),

    "governing-documents-superseded-halves": P(
        presentation=PROPOSAL, role="mining witness",
        mining="mine via the airlock", retirement_candidate=False,
        reason="`STATUS_ARCHIVE.md` and `cowork_handoff_archive.md` — reference-only by their own "
               "banners and outside the session-start reads. They hold the earlier statements of "
               "things the live documents now state differently, which is exactly what a mining "
               "map wants; and their being superseded is why the airlock rather than a direct "
               "read. NOT a retirement candidate: they are already out of every mandatory read, so "
               "retirement would buy nothing and #12 argues against moving them."),

    "the-open-items-register-detail-files": P(
        presentation=PROPOSAL, role="audit material",
        mining="mine via the airlock", retirement_candidate=False,
        reason="One detail file per row, carrying narrative and provenance and never a status. "
               "They are the record of what was found and not yet resolved, so they are the "
               "natural feed for the audit's question list — and Ruling 13's marking of rows "
               "affected by the pollution reads this population when it runs. Via the airlock "
               "because a row's narrative frequently describes the implementation, which is the "
               "quarantine case rather than a design input."),

    "the-decisions-register-group-files": P(
        presentation=PROPOSAL, role="mining witness",
        mining="mine via the airlock", retirement_candidate=False,
        reason="The rendered entries carrying each decision's verbatim text, restatement, reason "
               "and provenance. They are the single densest source of ratified design intent in "
               "the repository. Via the airlock and not directly, for the reason eighteenth-stop "
               "Ruling 8 gives in terms: the decisions register was harvested from sources "
               "including "
               "production code comments, so it contains observations of what the code does "
               "recorded as though decided — and the filtering ruling that separates the two has "
               "not run. ★ NOT A RETIREMENT CANDIDATE even partly: the filter is soft-discard, "
               "explicitly not destruction."),

    "ratification-surfaces": P(
        presentation=PROPOSAL, role="clean-room admissible",
        mining="mine directly", retirement_candidate=False,
        reason="The reading surfaces rulings were taken on. Each states the alternatives, their "
               "costs and the recommendation — so it carries not only what was decided but what "
               "was declined and why, which is the constrained-optimum shape the ledger corollary "
               "to #17 asks for. Directly admissible: a decision surface argues from principles "
               "toward a choice, which is design intent by construction."),

    # ---- the writing side's record ---------------------------------------------------------------
    "writing-side-ruling-records": P(
        presentation=PROPOSAL, role="clean-room admissible",
        mining="mine directly", retirement_candidate=False,
        reason="The user's own rulings, several quoted verbatim, each dated and carrying its "
               "ground. §2.5 names the ratified design-intent rulings as the seed of the framework "
               "phase, and this class is where they live on disk. The highest-value class on this "
               "surface per byte, and the one whose loss would be least recoverable."),

    "writing-side-session-records": P(
        presentation=PROPOSAL, role="audit material",
        mining="mine via the airlock", retirement_candidate=False,
        reason="`cowork_handoff.md`, `cowork_away_returns.md` and the writing side's own "
               "dispatches. They are the running account of what was done, in what order, and what "
               "was believed at the time — the raw material for process antipatterns under §2.4's "
               "second kind, and the place a claim's date can be checked. Via the airlock: they "
               "describe acts on the implementation constantly."),

    "writing-side-scratch-directories": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=True,
        reason="Dated scratch kept beside two sessions' work. ★ RETIREMENT CANDIDATE, and the "
               "reminder on this surface's own face applies: retirement is archive-with-record and "
               "destroys nothing (#12). The ground is that scratch is by definition the working "
               "residue of an act whose output landed elsewhere; if any member turns out to carry "
               "something the landed output does not, that is a finding and the flag is wrong for "
               "that member. The user rules."),

    # ---- the coding side's record ------------------------------------------------------------------
    "dispatches-to-the-coding-side": P(
        presentation=PROPOSAL, role="audit material",
        mining="mine via the airlock for antipatterns", retirement_candidate=False,
        reason="One dispatch per CC session, each carrying its predictions registered before the "
               "work ran (#17b), its premise ledger, its stop rules and its explicit list of what "
               "is deliberately not done. That is the richest available source of PROCESS "
               "antipatterns, which §2.4 sends into the phase definitions' constraints and stop "
               "rules rather than into the findings ledger. ★ AND A SECOND USE THE USER MAY WANT "
               "TO RULE ON SEPARATELY: a dispatch states what a session was ASKED to do, so it is "
               "the independent side of any question about whether a session did something it was "
               "not asked to — which is the eighteenth stop's own diagnosis."),

    # ---- the documentation directory -----------------------------------------------------------------
    "llm-triage-prompts": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=True,
        reason="Prompt text for a triage mechanism. ★ RETIREMENT CANDIDATE on the ground that no "
               "governing document the citation scan reads names any member, and the largest "
               "single file count in `docs/` is spent on them. Archive-with-record, nothing "
               "destroyed. The user rules, and a reader who knows of a live consumer should say "
               "so — an absent citation is evidence about the governing record, not about the "
               "world."),

    "documentation-directory-superseded": P(
        presentation=PROPOSAL, role="mining witness",
        mining="mine via the airlock", retirement_candidate=False,
        reason="Documents already moved to `docs/old_docs/` by an earlier act. Being superseded is "
               "what makes them worth reading in a derivation-first repair: they hold the earlier "
               "statement of something the live text now states differently, and the difference is "
               "the signal. Already out of the way, so retirement would move nothing."),

    "published-research-papers": P(
        presentation=PROPOSAL, role="clean-room admissible",
        mining="mine directly", retirement_candidate=False,
        reason="Published research is the world, not the mirror — the first thing §2.2 admits by "
               "name. ★ AND A FINDING RATHER THAN A PROPOSAL: this class holds two files. "
               "Principles #1 and #2 make published research the basis of every design decision, "
               "and the theory-grounding corollary requires that a source be FETCHED AND READ "
               "before an equation is carried out of it. Two papers on disk is a small holding "
               "against that demand, and whether the remainder of the literature this project "
               "rests on "
               "is reachable at all is a question the framework phase will meet immediately."),

    "generated-api-documentation-assets": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="Static assets for generated API documentation. Machine output about the "
               "application's plugin surface, unrelated to harmonic analysis."),

    # ---- the four MIXED classes: no class-level verdict, proposals per side of the split ---------
    "documentation-directory-prose": P(
        presentation=SPLIT, role=None, mining=None, retirement_candidate=None,
        reason=MIXED_CLASSES["documentation-directory-prose"]),
    "measurement-and-analysis-tools": P(
        presentation=SPLIT, role=None, mining=None, retirement_candidate=None,
        reason=MIXED_CLASSES["measurement-and-analysis-tools"]),
    "writing-side-design-documents": P(
        presentation=SPLIT, role=None, mining=None, retirement_candidate=None,
        reason=MIXED_CLASSES["writing-side-design-documents"]),
    "reports-from-the-coding-side": P(
        presentation=SPLIT, role=None, mining=None, retirement_candidate=None,
        reason=MIXED_CLASSES["reports-from-the-coding-side"]),

    # ---- the audit apparatus -------------------------------------------------------------------------
    "audit-apparatus-generators": P(
        presentation=PROPOSAL, role="operational apparatus",
        mining="not worth mining", retirement_candidate=False,
        reason="The generators that derive this project's own records — the guard set, the "
               "registers' checks, the enumerations, and this surface. They are how a claim is "
               "kept derived rather than remembered, so they run THROUGH every phase rather than "
               "feeding into one. Not mined: they are our own machinery, and a fact read out of "
               "them is a fact about us. ★ THE USER MAY WANT A SEPARATE RULING ON THEIR UPKEEP "
               "COST: this class and its artifacts are the apparatus whose defect stream the "
               "2026-08-11 lapse ruling was written to stop, and nothing here proposes reviving "
               "it."),

    "audit-apparatus-artifacts": P(
        presentation=PROPOSAL, role="operational apparatus",
        mining="mine via the airlock", retirement_candidate=False,
        reason="What those generators wrote: enumerations, screens, splits, dispositions and "
               "guard state. Operational, and mineable through the airlock for one specific "
               "reason — several of them are ENUMERATIONS OF EVIDENCE (the candidate pass, the "
               "July screen, the period split), which is precisely what §2.7 says survives the "
               "restructuring phase with a changed job as the MINING MAP."),

    # ---- measurement, corpora and fitted material ---------------------------------------------------------
    "the-hard-stop-reference": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="Named explicitly in §2.11 as decided here. `tools/robust_stop/` is the committed "
               "reference the block-(A) regression stop diffs every candidate against, plus its "
               "dated snapshots. The QUESTION has two halves and they may take different answers. "
               "(a) As a GATE it is operational apparatus that must keep working — nothing in the "
               "derivation touches it, and the dispatch forbids touching it. (b) As EVIDENCE it is "
               "a measured record of our own system's behaviour, which §2.4 routes through the "
               "airlock with the admission test *does the fact survive the implementation being "
               "thrown away?* — and a per-run enumeration of which runs fail may not survive that "
               "test while the aggregate durations do. The user rules on both halves."),

    "joint-estimator-tables-and-fit-records": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="The estimator's committed tables, its adoption record and the per-fit ledgers. "
               "Presented as a QUESTION and not a proposal because it sits exactly on the open "
               "ruling §2.11 names — whether the measurement layer's own specifications are in the "
               "derivation's scope — and because the two halves pull opposite ways. The FIT "
               "LEDGERS record what was tried and what it scored, which is empirical-findings-"
               "ledger material of the first order including its negative results (#12's finding "
               "by exclusion). The TABLES are fitted parameters of the current implementation, "
               "which is the mirror. Splitting them is available and is not proposed here."),

    "calibration-maps-and-their-snapshots": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="Fitted maps and their pre-change snapshots, on the same open ruling as the "
               "estimator tables above and presented the same way for the same reason."),

    "notation-seam-artifacts": P(
        presentation=PROPOSAL, role="airlock input",
        mining="mine via the airlock", retirement_candidate=False,
        reason="The classified evidence and golden reconciliation from the notation switch. Their "
               "content is a measured comparison of two arms of our own implementation, so the "
               "admission test applies in full: what survives the implementation being thrown away "
               "is which DISTINCTIONS turned out to matter at the notation seam, not the "
               "per-surface diffs."),

    "musical-score-collections-held-for-research": P(
        presentation=PROPOSAL, role="clean-room admissible",
        mining="mine directly", retirement_candidate=False,
        reason="Acquired musical scores and their annotations. §2.2 admits ground-truth corpora "
               "and their annotator conventions by name — they are the world. ★ ONE STANDING RULE "
               "IS RESTATED RATHER THAN RE-DECIDED: a newly acquired corpus enters as research "
               "material and does not become part of the pass/fail check by arriving; promoting "
               "any of it into the gate is a separate deliberate re-baseline. Nothing here "
               "proposes such a promotion."),

    "corpus-and-parameter-registries": P(
        presentation=QUESTION, role=None, mining=None, retirement_candidate=None,
        reason="Named explicitly in §2.11 as decided here. The registries state what is held, "
               "where it came from and what it may be used for — which reads as convention rather "
               "than implementation — while `param_manifest.json` and the baseline JSON state what "
               "the current implementation's parameters and outputs ARE, which is the mirror. The "
               "class is mixed in KIND rather than in citation, so the surface does not split it "
               "by the scan and asks instead."),

    "measurement-outputs-recorded-beside-the-tools": P(
        presentation=PROPOSAL, role="airlock input",
        mining="mine via the airlock", retirement_candidate=True,
        reason="Recorded outputs and characterisations sitting loose in `tools/`, most named for "
               "the single iteration that produced them. Airlock input because a characterisation "
               "of which cases failed and why is a finding that can outlive the code that "
               "produced it. ★ RETIREMENT CANDIDATE for the members the citation scan finds "
               "unnamed by the governing record — archive-with-record, nothing destroyed — once "
               "whatever they carry has been through the airlock, and not before."),

    "probe-outputs-and-their-snapshots": P(
        presentation=PROPOSAL, role="airlock input",
        mining="mine via the airlock", retirement_candidate=False,
        reason="Dated probe outputs kept beside their generator, including pre-change snapshots "
               "taken under the standing snapshot-before-re-baseline rule. They are measurements "
               "of our own system and go through the airlock for that reason; not retirement "
               "candidates, because a snapshot's whole job is to still be there when someone asks "
               "what the value was before."),

    "upstream-developer-tooling": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="MuseScore's own developer utilities and the chord diagram converter. Not ours and "
               "not about harmonic analysis."),

    # ---- other workspaces ------------------------------------------------------------------------------
    "idiom-discovery-workspace": P(
        presentation=PROPOSAL, role="airlock input",
        mining="mine via the airlock for antipatterns", retirement_candidate=True,
        reason="A workspace of one-file scripts building and characterising idiom profiles. Its "
               "findings document is a `cowork_` file elsewhere; what sits here is the machinery "
               "that produced them. Airlock for antipatterns because an exploration that did not "
               "become a design is the clearest available statement of an approach tried and not "
               "adopted, which §2.4 says rules out the TRIED IMPLEMENTATION rather than always the "
               "approach. ★ RETIREMENT CANDIDATE once mined — archive-with-record. The user "
               "rules."),

    "ai-assistant-design-notes": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=True,
        reason="Design notes for a separate assistant feature whose source, by the project's own "
               "record, lives outside this repository. ★ RETIREMENT CANDIDATE on the ground that "
               "it belongs to a different product surface entirely — archive-with-record. If any "
               "of it bears on harmonic analysis the flag is wrong and the user should say so."),

    "demonstration-and-sandbox-material": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=False,
        reason="Demonstration musical scores shipped with the application and two small build "
               "sandboxes. Upstream material."),

    # ---- the repository root ---------------------------------------------------------------------------------
    "root-level-project-prose-outside-the-naming-conventions": P(
        presentation=PROPOSAL, role="mining witness",
        mining="mine via the airlock", retirement_candidate=False,
        reason="Three project documents at the repository root carrying none of the naming "
               "conventions — a deduplication plan, a build-error triage prompt and a findings "
               "document. ★ WHAT IS WORTH THE USER'S ATTENTION HERE IS NOT THE VERDICT BUT THE "
               "CLASS EXISTING AT ALL: three files that no convention reaches are three files a "
               "convention-driven sweep will miss, and the derivation-first repair is exactly such "
               "a sweep. Naming them is the point of the class."),

    "stray-working-files-committed-to-the-repository-root": P(
        presentation=PROPOSAL, role="outside every phase's inputs",
        mining="not worth mining", retirement_candidate=True,
        reason="Dumped analysis output, diagnostic text, logs, an exported musical score, an audio "
               "file, application settings written by a run, and the unpacked members of a musical "
               "score container together with a CTest temporary directory — all committed to the "
               "repository root at some point and never removed. ★ RETIREMENT CANDIDATE as a "
               "class: archive-with-record under #12, nothing destroyed. ★ AND ONE MEMBER IS "
               "FLAGGED SEPARATELY BECAUSE IT IS NOT SCRATCH: `Compatibility`, `META-INF/` and "
               "`Thumbnails/` are the unpacked members of a MuseScore container, which means a "
               "musical score was extracted into the repository root and committed. That is worth "
               "the user seeing before anything is archived, because it says how the class arose."),
}

# ── AUTHORED — the proposal per side of the citation split, for the four mixed classes ───────────
SPLIT_PROPOSALS: dict[str, dict] = {
    "documentation-directory-prose": {
        "cited": P(presentation=PROPOSAL, role="mining witness", mining="mine via the airlock",
                   retirement_candidate=False,
                   reason="Named somewhere in the governing record, so something points at it. "
                          "These are the specifications and policies the derivation must derive "
                          "AGAINST — read after the derived statement is written, never before "
                          "(§2.2's derive-before-compare), and every implementation description "
                          "found in them quarantined as an audit question rather than absorbed."),
        "uncited": P(presentation=PROPOSAL, role="airlock input",
                     mining="mine via the airlock for antipatterns", retirement_candidate=True,
                     reason="Named nowhere in the governing record. Mostly dated characterisations "
                            "of one iteration's behaviour and reconstructions of what a mechanism "
                            "was. ★ RETIREMENT CANDIDATE once mined — archive-with-record, nothing "
                            "destroyed — and mined for antipatterns first, because a document "
                            "recording why an iteration went wrong is the cheapest antipattern "
                            "source in the repository."),
    },
    "measurement-and-analysis-tools": {
        "cited": P(presentation=PROPOSAL, role="operational apparatus",
                   mining="not worth mining", retirement_candidate=False,
                   reason="Named in the governing record — the pinned measurement tools, the "
                          "corpus commands and the graders the hard stop and the standing "
                          "conventions depend on. They must keep working through every phase. Not "
                          "mined: a tool is machinery, and its behaviour is a fact about our "
                          "implementation."),
        "uncited": P(presentation=PROPOSAL, role="airlock input",
                     mining="mine via the airlock for antipatterns", retirement_candidate=True,
                     reason="Named nowhere in the governing record — the single-iteration "
                            "diagnostics, sweeps, enumerations and one-question probes. ★ "
                            "RETIREMENT CANDIDATE, archive-with-record. ★ AND A WARNING THE USER "
                            "SHOULD WEIGH BEFORE RULING: absence from the governing record is not "
                            "absence of a caller. A tool imported by another tool, or named only "
                            "in a report, is invisible to the scan. A retirement act should check "
                            "callers at the objects first, which is a named later act and is not "
                            "started."),
    },
    "writing-side-design-documents": {
        "cited": P(presentation=PROPOSAL, role="mining witness", mining="mine via the airlock",
                   retirement_candidate=False,
                   reason="Named in the governing record — this is where the ratified contract "
                          "documents live, the ones `ARCHITECTURE.md` delegates concerns to under "
                          "rules (g) through (m). ★ THE USER'S OWN §2.11 QUALIFICATION IS THE "
                          "REASON THIS IS NOT `clean-room admissible`: `cowork_*` design documents "
                          "are NOT direct witnesses, and their value is measured by what the "
                          "curation acts extract rather than presumed. Being cited raises the "
                          "prior; it does not settle it."),
        "uncited": P(presentation=PROPOSAL, role="airlock input", mining="mine via the airlock",
                     retirement_candidate=False,
                     reason="Named nowhere in the governing record — drafts, explorations, audits "
                            "and dossiers that no live surface points at. ★ NOT FLAGGED FOR "
                            "RETIREMENT, and the asymmetry with the `docs/` class above is "
                            "deliberate: §2.7 keeps the candidate artifacts and the screen as the "
                            "MINING MAP, and this class is the population that map was built over. "
                            "Retiring it before the mining runs would retire the thing being "
                            "mined."),
    },
    "reports-from-the-coding-side": {
        "cited": P(presentation=PROPOSAL, role="airlock input", mining="mine via the airlock",
                   retirement_candidate=False,
                   reason="Named in the governing record — the measurement reports gate block (A) "
                          "and the standing conventions cite as provenance for figures still in "
                          "force. Airlock and not direct: every one of them is a measurement of "
                          "OUR system, so the admission test applies — does the fact survive the "
                          "implementation being thrown away? Some do (a corpus's annotator "
                          "convention, a refuted premise); some do not (a per-preset agreement "
                          "percentage)."),
        "uncited": P(presentation=PROPOSAL, role="airlock input",
                     mining="mine via the airlock for antipatterns", retirement_candidate=True,
                     reason="Named nowhere in the governing record — diagnostic write-ups and "
                            "closed investigations. ★ RETIREMENT CANDIDATE once mined, "
                            "archive-with-record. These are the richest DESIGN-antipattern source "
                            "in the repository under §2.4's first kind: a report that says an "
                            "approach was tried and measured worse, with its failure diagnosis or "
                            "an explicit *cause undiagnosed*."),
    },
}


def load_inventory() -> dict:
    if not INVENTORY.exists():
        raise Stop(f"the inventory artifact is missing: {INVENTORY} — run "
                   f"`python tools/audit/gen_artifact_inventory.py` first")
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def governing_text() -> tuple[str, list[str]]:
    """The governing record, read once. Returns the joined text and the files it came from."""
    chunks, sources = [], []
    for name in GOVERNING_DOCUMENTS:
        path = ROOT / name
        if not path.exists():
            raise Stop(f"a governing document named for the citation scan is missing: {name}")
        chunks.append(path.read_text(encoding="utf-8", errors="replace"))
        sources.append(name)
    for directory in GOVERNING_DIRECTORIES:
        base = ROOT / directory
        if not base.is_dir():
            raise Stop(f"a governing directory named for the citation scan is missing: {directory}")
        for path in sorted(base.rglob("*.md")):
            chunks.append(path.read_text(encoding="utf-8", errors="replace"))
        sources.append(f"{directory}/**/*.md")
    return "\n".join(chunks), sources


def cited_names(text: str) -> set[str]:
    """Every file name the governing record mentions, taken as bare tokens.

    Deliberately crude and deliberately GENEROUS: it collects anything shaped like a file name and
    asks only whether a candidate's base name is among them.  A generous scan errs toward calling a
    file CITED, which errs away from flagging it for retirement — the safe direction for a proposal
    the user has not yet ruled on.
    """
    return set(re.findall(r"[A-Za-z0-9_.\-]+\.[A-Za-z0-9]+", text))


def verify_vocabulary(where: str, entry: dict) -> None:
    if entry["presentation"] in (QUESTION, SPLIT):
        if entry["role"] is not None or entry["mining"] is not None:
            raise Stop(f"{where}: a {entry['presentation']} carries no proposed role or mining "
                       f"verdict at the class level")
    else:
        if entry["role"] not in ROLES:
            raise Stop(f"{where}: role {entry['role']!r} is outside the closed vocabulary {ROLES}")
        if entry["mining"] not in MINING:
            raise Stop(f"{where}: mining verdict {entry['mining']!r} is outside the closed "
                       f"vocabulary {MINING}")
        if entry["retirement_candidate"] not in (True, False):
            raise Stop(f"{where}: the retirement-candidate flag must be true or false")
    if not entry.get("reason", "").strip():
        raise Stop(f"{where}: a proposal with no reason is not a proposal")


def build() -> tuple[str, dict]:
    inv = load_inventory()
    classes = {c["class"]: c for c in inv["the_classes"]}

    missing = [name for name in classes if name not in PROPOSALS]
    if missing:
        raise Stop(f"these classes reached no section of the surface: {missing}. A class the user "
                   f"never sees is a class ruled on by omission.")
    unknown = [name for name in PROPOSALS if name not in classes]
    if unknown:
        raise Stop(f"these proposals name a class the inventory does not carry: {unknown}")
    for name, entry in PROPOSALS.items():
        verify_vocabulary(f"class {name}", entry)
    for name, sides in SPLIT_PROPOSALS.items():
        if name not in MIXED_CLASSES:
            raise Stop(f"a split proposal names {name}, which is not declared mixed")
        for side, entry in sides.items():
            verify_vocabulary(f"class {name}, {side} side", entry)
    for name in MIXED_CLASSES:
        if name not in SPLIT_PROPOSALS:
            raise Stop(f"class {name} is declared mixed but carries no split proposals")
        if name not in classes:
            raise Stop(f"class {name} is declared mixed but the inventory does not carry it")
        if not classes[name].get("every_member"):
            raise Stop(f"class {name} is declared mixed but the inventory publishes no members "
                       f"for it — the split cannot be taken")

    text, sources = governing_text()
    names = cited_names(text)

    splits = {}
    for name in MIXED_CLASSES:
        cited, uncited = [], []
        for member in classes[name]["every_member"]:
            base = posixpath.basename(member["path"])
            (cited if base in names else uncited).append(member["path"])
        splits[name] = {"cited": sorted(cited), "uncited": sorted(uncited)}

    # the retirement-candidate roll-up, DERIVED from the authored flags
    flagged_whole = [n for n, e in PROPOSALS.items() if e["retirement_candidate"] is True]
    flagged_partly = [n for n, sides in SPLIT_PROPOSALS.items()
                      if any(s["retirement_candidate"] for s in sides.values())]
    questions = [n for n, e in PROPOSALS.items() if e["presentation"] == QUESTION]

    data = {
        "inventory_commit": inv["derived_at_commit"],
        "classes": classes,
        "splits": splits,
        "citation_sources": sources,
        "flagged_whole": flagged_whole,
        "flagged_partly": flagged_partly,
        "questions": questions,
    }
    return render(inv, data), data


def _fmt_bytes(n: int) -> str:
    return f"{n // 1024:,} KiB" if n >= 1024 else f"{n} bytes"


def _proposal_lines(entry: dict) -> list[str]:
    out = []
    if entry["presentation"] == SPLIT:
        out.append("**NO SINGLE VERDICT IS PROPOSED FOR THIS CLASS — it is mixed, and the "
                   "proposals sit one per side of the split immediately below.**")
        out.append("")
        out.append(f"**Why — AUTHORED:** {entry['reason']}")
        return out
    if entry["presentation"] == QUESTION:
        out.append("**PRESENTED AS A QUESTION, NOT A PROPOSAL.** No role, no mining verdict and no "
                   "retirement flag is proposed for this class.")
        out.append("")
        out.append(f"**The question — AUTHORED:** {entry['reason']}")
        return out
    flag = ("**YES — a candidate, awaiting the user's ruling**" if entry["retirement_candidate"]
            else "no")
    out.append(f"- **PROPOSED role (AUTHORED):** {entry['role']}")
    out.append(f"- **PROPOSED mining verdict (AUTHORED):** {entry['mining']}")
    out.append(f"- **Retirement candidate (AUTHORED):** {flag}")
    out.append("")
    out.append(f"**Reason — AUTHORED:** {entry['reason']}")
    return out


def render(inv: dict, data: dict) -> str:
    L: list[str] = []
    add = L.append
    classes = data["classes"]
    pop = inv["the_population"]

    add("# The artifact inventory — the ruling surface: a role, a mining verdict and a "
        "retirement flag PROPOSED for every class")
    add("")
    add("> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED, AND NOTHING HERE "
        "HAS BEEN DONE.** Every role, mining verdict and retirement flag below is **AUTHORED by "
        "the coding side and marked as such**; every count, every member list and every split is "
        "**DERIVED** from `tools/audit/artifact_inventory.json` or from the citation scan this "
        "surface performs. Generated by `tools/audit/gen_artifact_inventory_surface.py`; do not "
        "hand-edit — change the generator and regenerate.")
    add(">")
    add("> **★ RETIREMENT DESTROYS NOTHING.** Every retirement flag on this surface means "
        "**archive-with-record, out of every phase's inputs** — #12 governs, and the user's own "
        "§2.10 says so in terms. No file has been moved, renamed, archived or deleted by the "
        "dispatch that produced this surface, and none will be until the user rules.")
    add(">")
    add("> **★ THE ONE THING TO READ BEFORE THE CLASSES**, because it changes what the inventory "
        "means: a large body of this project's dispatches and reports is **not in git at all** — "
        "see *The untracked appendix* at the end. It is a finding, not a proposal.")
    add(">")
    add(f"> *Dispatch: `cc_instruction_artifact_inventory.md`, Task 2. Derived from the tracked "
        f"tree at `{data['inventory_commit'][:10]}`.*")
    add("")

    add("## 0. What this surface is asking for")
    add("")
    add("The user directed that the artifact inventory come **before the phases are drafted** — "
        "understand what artifacts exist and decide how they should be used, then draft the "
        "phases citing ruled classes. This surface is the second half of that: the walk is done "
        "and published; what is owed now is a ruling per class.")
    add("")
    add("Three things are proposed per class, in the vocabulary the direction names:")
    add("")
    add("- **Role** — one of: " + ", ".join(f"*{r}*" for r in ROLES) + ".")
    add("- **Mining verdict** — one of: " + ", ".join(f"*{m}*" for m in MINING) + ".")
    add("- **Retirement candidate** — a flag with its ground. Archive-with-record, never "
        "destruction.")
    add("")
    add("**Where the record already leaves a ruling open, the class is presented as a QUESTION "
        "rather than a proposal.** §2.11 of `cowork_rulings_2026_08_15_method_directions.md` "
        "sends the classification of the tests, the goldens, the catalogs, `tools/robust_stop/` "
        "and the registries here, and leaves the scope of the measurement layer's own "
        "specifications open. Proposing a verdict on those would be answering the user's own open "
        "question on their behalf.")
    add("")
    add(f"**{len(data['questions'])} classes are presented as QUESTIONS; "
        f"{len(classes) - len(data['questions'])} carry proposals.**")
    add("")

    add("## 1. The population, and what the classification does and does not establish")
    add("")
    add(f"- **{pop['entries_in_the_tree']:,} tracked entries** at "
        f"`{data['inventory_commit'][:10]}`, **{pop['classified']:,} classified**, "
        f"**{pop['unclassified']} unclassified**, in "
        f"**{pop['classes_in_the_signature_table']} classes**, "
        f"{_fmt_bytes(pop['total_bytes'])} in total.")
    add("- The signature is **path and extension only**. No file's content was read to class it.")
    add("- The unclassified bucket being empty is a **STOP that did not fire**, not a remainder — "
        "and the last rule in the table is deliberately bounded so that the STOP *can* fire.")
    add("")
    add("**★ WHAT AN EMPTY BUCKET DOES NOT ESTABLISH**, in the inventory's own words: it shows "
        "every file matched *some* rule and nothing about whether it matched the *right* one. A "
        "file sitting in a directory whose name misdescribes it is classed by the misdescription. "
        "A reading of a sample of members per class against its stated signature would settle the "
        "other half; that act is named and not started (#19).")
    add("")

    add("## 2. The citation scan — the one DERIVED signal the mixed classes are split by")
    add("")
    add("Four classes interleave material that cannot share a verdict. They are split by a fact "
        "rather than an impression: **does the governing record name this file anywhere?**")
    add("")
    add("- **What is scanned:** " + ", ".join(f"`{s}`" for s in data["citation_sources"]) + ".")
    add("- **How:** every token shaped like a file name is collected from that text, and a "
        "candidate is *cited* if its base name is among them. The scan is deliberately crude and "
        "**generous** — erring toward *cited* errs away from flagging something for retirement, "
        "which is the safe direction for a proposal nobody has ruled on yet.")
    add("")
    add("**★ WHAT THE SCAN DOES NOT ESTABLISH.** A citation shows something points at the file, "
        "**not** that the file is correct, current or worth keeping. An absent citation shows the "
        "governing record does not name it, **not** that nothing depends on it — a tool imported "
        "by another tool, or a document cited only from a report, is invisible here. **No "
        "retirement should be executed on this signal alone.**")
    add("")

    add("## 3. The classes")
    add("")
    for block in inv["the_classes"]:
        name = block["class"]
        entry = PROPOSALS[name]
        marker = "❓" if entry["presentation"] == QUESTION else ""
        add(f"### {block['order_in_the_signature_table'] + 1}. `{name}` {marker}".rstrip())
        add("")
        add(f"**{block['files']:,} files, {_fmt_bytes(block['total_bytes'])}.** "
            f"*Signature (AUTHORED):* {block['signature']}")
        add("")
        add("*Example members (DERIVED):* " +
            ", ".join(f"`{p}`" for p in block["example_paths"]))
        add("")
        for line in _proposal_lines(entry):
            add(line)
        add("")
        if name in MIXED_CLASSES:
            split = data["splits"][name]
            add(f"#### Descent — this class is MIXED, and is split by the citation scan")
            add("")
            add(f"*Why it is mixed (AUTHORED):* {MIXED_CLASSES[name]}")
            add("")
            for side, label in (("cited", "NAMED in the governing record"),
                                ("uncited", "NAMED NOWHERE in the governing record")):
                members = split[side]
                sub = SPLIT_PROPOSALS[name][side]
                add(f"**{label} — {len(members):,} of {block['files']:,} files.**")
                add("")
                for line in _proposal_lines(sub):
                    add(line)
                add("")
                if members:
                    add("<details><summary>The members (DERIVED)</summary>")
                    add("")
                    for path in members:
                        add(f"- `{path}`")
                    add("")
                    add("</details>")
                    add("")
        add("---")
        add("")

    add("## 4. The retirement candidates, gathered")
    add("")
    add("**Every one is a CANDIDATE awaiting the user's ruling, and retirement is "
        "archive-with-record: nothing is destroyed (#12).**")
    add("")
    add("**Flagged as a whole class:**")
    add("")
    for name in data["flagged_whole"]:
        block = classes[name]
        add(f"- `{name}` — {block['files']:,} files, {_fmt_bytes(block['total_bytes'])}")
    add("")
    add("**Flagged partly — the uncited side of a mixed class only:**")
    add("")
    for name in data["flagged_partly"]:
        block = classes[name]
        sides = [s for s, e in SPLIT_PROPOSALS[name].items() if e["retirement_candidate"]]
        counted = sum(len(data["splits"][name][s]) for s in sides)
        add(f"- `{name}` — {counted:,} of {block['files']:,} files "
            f"({', '.join(sides)} side)")
    add("")
    add("**★ THE STANDING WARNING ON ALL OF THEM:** the uncited side is derived from a scan that "
        "sees only the governing record. Before any retirement is executed, callers and "
        "references should be checked at the objects. That act is named here and is not started.")
    add("")

    add("## 5. The questions, gathered")
    add("")
    add("These classes carry no proposal. Each sits on a ruling the record already leaves open.")
    add("")
    for name in data["questions"]:
        block = classes[name]
        add(f"- **`{name}`** — {block['files']:,} files, {_fmt_bytes(block['total_bytes'])}")
    add("")

    add("## 6. The untracked appendix — and the finding inside it")
    add("")
    ap = inv["appendix_untracked_and_ignored_paths_NOT_classified"]
    add("Assumption A2 of the dispatch: the population is the **tracked** tree, and an untracked "
        "file is either scratch or an un-landed record — both for the user to see, not for a tool "
        "to grade. So these are listed, never classified.")
    add("")
    add(f"- **{ap['untracked_candidate_records']['count']:,}** untracked, not ignored, outside "
        f"any scratch directory")
    add(f"- **{ap['untracked_inside_a_scratch_directory']['count']:,}** untracked inside a scratch "
        f"directory")
    add(f"- **{ap['ignored_files_at_the_repository_root']['count']:,}** **ignored** files at the "
        f"repository root")
    add(f"- **{ap['ignored_directories_collapsed']['count']:,}** ignored directories, listed "
        f"collapsed (build output, dependency trees, editor state)")
    add("")
    add("### ★ THE FINDING: the dispatch-and-report family is ignored by `.gitignore`, and most "
        "of it has never been committed")
    add("")
    add("`.gitignore` carries the rule `/cc_*.md`. That rule covers **every** dispatch written to "
        "the coding side and **every** report written back. The tracked tree nonetheless carries "
        f"{classes['dispatches-to-the-coding-side']['files']} dispatches and "
        f"{classes['reports-from-the-coding-side']['files']} reports — added with an explicit "
        "override at some point — while "
        f"**{ap['ignored_files_at_the_repository_root']['count']:,} more sit on disk, ignored, "
        "outside git.**")
    add("")
    add("**Why this is not a housekeeping remark.** Documents in that ignored set are cited as "
        "provenance by the governing record itself — including by gate block (A) of `CLAUDE.md` "
        "and by rulings of the eighteenth stop. A fresh clone of this repository does not contain "
        "them. They are therefore **not available to any phase that reads only what git carries**, "
        "and the handover-safety the method-directions record requires does not currently extend "
        "to them.")
    add("")
    add("**What this surface does about it: nothing.** It is stated, not fixed. Landing them is a "
        "commit that names its own act, and it is the user's to order.")
    add("")

    add("## 7. What was deliberately not done")
    add("")
    add("- **No file moved, renamed, retired, archived or deleted.** Every retirement above is a "
        "flag.")
    add("- **No mining performed.** The register filter, the rulings sort and the findings ledger "
        "are later acts that consume the *ruled* inventory.")
    add("- **No phase defined, no specification derived, no repair** — the eighteenth stop's §3 "
        "stands whole.")
    add("- **No open-items row marked, flipped or discarded; no decisions-register entry "
        "written.** OI-179 stays OPEN and GATES.")
    add("- **The re-opened period question is untouched** — it is the user's ruling, listed in "
        "`cowork_rulings_2026_08_15_method_directions.md` §3.")
    add("")
    add("*Generated by `tools/audit/gen_artifact_inventory_surface.py` from "
        "`tools/audit/artifact_inventory.json`. Reproduce: "
        "`python tools/audit/gen_artifact_inventory_surface.py --check`.*")
    add("")
    return "\n".join(L)


def main(argv: list[str]) -> int:
    text, data = build()
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: surface missing:", OUT)
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed surface:", OUT)
            return 1
        print("OK: the ruling surface re-derives from the inventory artifact.")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8", newline="")
    print("wrote", OUT)
    print(f"  {len(data['classes'])} classes: {len(data['questions'])} questions, "
          f"{len(data['classes']) - len(data['questions'])} proposals")
    print(f"  retirement candidates: {len(data['flagged_whole'])} whole classes, "
          f"{len(data['flagged_partly'])} partly")
    for name, split in data["splits"].items():
        print(f"  split {name}: {len(split['cited'])} cited / {len(split['uncited'])} uncited")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
