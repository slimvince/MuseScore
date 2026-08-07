#!/usr/bin/env python3
"""Derive the NON-GATING apparatus set: open register rows that gate no stage.

THE RULING (user, 2026-08-03): rows whose subject is this project's own tracking and
documentation apparatus are declared NON-GATING - worked in leftover capacity, gating nothing.

THE CRITERION, as ruled: does the row's subject bear on the analysis, its inputs, or an
instrument a measurement depends on?  IF YES IT GATES.

THE EXEMPTION, as ruled: an establishment obligation (#19) ALWAYS gates, whatever its subject.
Backgrounding an establishment obligation is how it never happens.

HOW THE SET IS DERIVED, and what is authored:
  DERIVED  - the row population (parsed from OPEN_ITEMS.md), which rows are OPEN, and a
             deliberately OVER-INCLUSIVE first cut on each row's own subject column. Over-
             inclusion is safe: an over-included row that is not apparatus simply gets a GATES
             verdict from the default.
  AUTHORED - the per-row verdict and its reason, read at the row itself. The tool REFUSES to
             run if any first-cut candidate has no authored verdict, and refuses an authored
             verdict for a row that is not in the population or is not open - so the authored
             table cannot silently drift away from the register.

Usage:
  python tools/audit/gen_nongating_apparatus_rows.py           # write the artifact
  python tools/audit/gen_nongating_apparatus_rows.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent
ROOT = ROOT.parent
INDEX = ROOT / "OPEN_ITEMS.md"
OUT = ROOT / "tools" / "audit" / "nongating_apparatus_rows.json"

GATES = "GATES"
NON_GATING = "NON-GATING"

THE_RULING = (
    "Rows whose subject is this project's own tracking and documentation apparatus are declared "
    "NON-GATING - worked in leftover capacity, gating nothing (user, 2026-08-03)."
)
THE_CRITERION = (
    "Does the row's subject bear on the analysis, its inputs, or an instrument a measurement "
    "depends on? If yes it gates."
)
THE_EXEMPTION = (
    "An establishment obligation (#19) ALWAYS gates, whatever its subject - backgrounding an "
    "establishment obligation is how it never happens."
)
THE_DEFAULT = (
    "A row that is not apparatus, or whose subject the row does not settle, GATES. The "
    "declaration only ever removes a wait where the row's own text supports removing it."
)

# The line this derivation draws inside the documentation rows, stated once so every verdict
# below can be checked against it rather than against taste:
THE_LINE = (
    "A documentation row is APPARATUS when what is owed is a pointer, an anchor, a label, a "
    "banner, a filing decision or a section boundary - something that states nothing false about "
    "the analysis. A documentation row GATES when what is owed is a correction to a statement "
    "about the analysis or its build state, or the completion of a specification - because "
    "phase 1's own text makes specifications COMPLETE and TRUE the thing that must precede "
    "everything else."
)

# --------------------------------------------------------------------------------------
# The first cut: a deliberately over-inclusive match on the row's own subject column.
# --------------------------------------------------------------------------------------
FIRST_CUT_VOCAB = [
    "doc-sync", "docs /", "doc", "process", "housekeeping", "audit tooling", "harness",
    "substrate hygiene", "decisions register", "documentation gap", "repository organization",
    "registry", "tests /", "convention", "ARCHITECTURE doc", "planning", "held /",
]

# --------------------------------------------------------------------------------------
# The authored verdicts. Every first-cut candidate must appear here, with a reason.
#   class_basis is recorded ONLY on NON-GATING rows, and names WHICH ground admitted the row:
#     "user"      - tracking/documentation apparatus, the user's own phrase
#     "widening"  - process apparatus; a WIDENING of the user's phrase, stated as a judgment
#     "row-says"  - the row's own recorded status already says it gates nothing
#   gate_ground is recorded ONLY on GATES rows.
# --------------------------------------------------------------------------------------
# Verdicts for rows that have since CLOSED. The tool stops on a live verdict naming a row the
# INDEX no longer carries open -- correctly, since that is how a stale declaration survives an
# unnoticed resolution. But deleting the reasoning would lose it (#12), so a closed row's
# verdict moves here: preserved, carried into the artifact as history, and never counted.
RETIRED_VERDICTS = {
    "OI-340": (GATES, "the criterion - D-438's line puts specification completion on the gating side",
               "Whether criterion C1 reaches SUPERSEDED register entries is unruled: the per-kind "
               "scheme said to settle it does not carry that kind, and read at its own text it "
               "routes those entries the OPPOSITE way -- into the owning specification, the very "
               "act the ruling exists to forbid. WHAT IS OWED decides it, and what is owed here is "
               "not a pointer, an anchor, a label, a banner or a filing choice: it is WHICH "
               "DECISIONS PHASE 1 MUST WRITE INTO A SPECIFICATION. D-438's line names that side "
               "explicitly -- 'the completion of a specification GATES, because the phase-1 rule in "
               "Conventions makes specifications COMPLETE and TRUE the thing that precedes "
               "everything else.' The reach is not one entry: item 1's whole NO-HOME class has no "
               "closing act until it is ruled, so the finish line cannot report that item as "
               "dischargeable. Recorded against the row's SUBJECT, never its remedy.",
               "RESOLVED 2026-08-04 - the user ruled the question the row put (D-642), on the "
               "basis the row itself named. The verdict was correct while it stood and is kept "
               "whole (#12); it is retired because the row closed, never because it was wrong."),
    "OI-287": (NON_GATING, "user",
               "Where the ratification surfaces and the dispatches are filed, and how cited "
               "paths are re-aimed when they move. Repository organization; the files are "
               "committed and durable already.",
               "RESOLVED 2026-08-03 (phase 1u, Task 4) - the directory `ratification_surfaces/` "
               "created, ten files moved, every citation re-aimed per citation."),
    "OI-289": (GATES, "#19 establishment obligation",
               "Gates on the exemption, and independently on the criterion: the marked set "
               "includes D-329, complete candidate listing, which is the family design's ratified "
               "admission premise and whose marking already failed once.",
               "VERIFIED 2026-08-03 (phase 1w) - the whole marked set re-verified against the "
               "live-reachability test, 0 marks established wrong and 0 corrected, the convention "
               "not in question. Its residues opened as OI-302 (which gates), OI-303 and OI-304."),
    "OI-334": (GATES, "an establishment obligation (#19) - the exemption, not the criterion",
               "The decisions register's own published account of itself is false at HEAD in "
               "three places. The verdict is made PER INSTANCE and the row takes the strongest. "
               "The instance that decides it is the published unresolved-residual figure: its "
               "subject is the coverage measurement the OI-207 audit reports against -- the same "
               "ground OI-333 gates on -- and a figure the same generated file's own computed "
               "table contradicts is independently an establishment matter (#19), which D-438's "
               "starred clause makes gating whatever its subject. The scope statement that the "
               "per-layer design documents were not read in full is a claim about how completely "
               "the register enumerates the record, which its own text does not settle, so the "
               "declaration's own default reaches it. The third instance -- a section field the "
               "read-wave entries do not carry -- reads as apparatus on its own and does not "
               "carry the row; it is rowed as an instance rather than promoted.",
               "RESOLVED 2026-08-04 (ruling R3) - all three statements are true at HEAD, closed "
               "by three different acts: the scope sentence corrected in prose, the residual "
               "figure made COMPUTED (a template the register generator fills, an unfilled "
               "placeholder stopping it), and the home-granularity claim made true by RUNNING "
               "the apply mode under ruling R2 after the phase-1q record was snapshotted and the "
               "snapshot established. Both former wordings preserved verbatim (#12)."),
    "OI-337": (GATES, "the criterion",
               "The uncommitted backlog is six waves rather than the three ruling R4 names, and the "
               "waves cannot be committed separately. The first cut proposes it because its subject "
               "column reads as documentation apparatus -- committing is filing, and filing is what "
               "D-438's line names as apparatus. WHAT IS OWED decides it, and what is owed here is "
               "not a pointer or a label: it is that a set of INSTRUMENTS exists only in a working "
               "tree. The uncommitted set includes the guard tools, the yield generators and the "
               "derivations this arc's conclusions rest on, and an instrument that exists only in a "
               "working tree cannot support a reproducibility claim (#16) -- which is a measurement "
               "matter, not a filing one. The starred clause reaches it independently: preserving "
               "an instrument so a recorded measurement can be reproduced is an establishment "
               "obligation (#19), and D-438 makes one gate whatever its subject. Recorded against "
               "the row's SUBJECT, never its remedy, as every verdict here is.",
               "RESOLVED 2026-08-04 (ruling R1) - disposition (a) taken: one provenance-stamped "
               "commit covering all six waves, `e10479a09f`, with the six-wave figure re-derived "
               "before the act rather than carried from the row, the non-wave paths deliberately "
               "not swept in, and every guard re-run explicitly at the committed tree because a "
               "plumbing commit bypasses hooks. The gating verdict is what it was: the instruments "
               "are now committed, which is the reproducibility exposure discharged rather than "
               "re-classified."),
}

V = {
    # ------------------------------------------------------------------ NON-GATING
    "OI-46": (NON_GATING, "user",
              "What is owed is 'annotate the tables' - a consistency banner inside the "
              "structural-integrity audit, a tracking document. Nothing about the analysis is "
              "stated falsely by the tables; two records disagree about a stage's build status."),
    "OI-47": (NON_GATING, "user",
              "The subject is four superseded sections of STATUS.md, a tracking surface, and the "
              "owed act is explicitly the BANNER half - marking them historical. The triage half, "
              "which was the part that touched what is true of the analysis, is discharged."),
    "OI-48": (NON_GATING, "user",
              "A dangling reference to a memory file from two documents; the row states in terms "
              "that nothing is lost and that the code substance rides OI-61. What is owed is "
              "re-pointing a citation."),
    "OI-49": (NON_GATING, "user",
              "Two records disagree about whether one decision is closed. What is owed is "
              "reconciling the records; neither statement is about how the analysis behaves."),
    "OI-50": (NON_GATING, "user",
              "The same shape as OI-49 one document over - 'annotate the arc plan' where two "
              "records describe one question's disposition differently."),
    "OI-58": (NON_GATING, "row-says",
              "Admitted on the row's own recorded status, not on the apparatus class: it says "
              "'none gates any stage' in terms, and names the three owners. The declaration "
              "records what the register already holds."),
    "OI-85": (NON_GATING, "user",
              "A session-harness convention owed after a git-state incident: a plumbing commit "
              "ends with an index refresh and a disk-versus-HEAD verify. The subject is how this "
              "project handles its own repository, not what the analysis reads."),
    "OI-99": (NON_GATING, "user",
              "Two production comments cite a document that does not exist. A dangling POINTER: "
              "nothing false is stated about the analysis, and the owed act is to re-point or "
              "drop the citation."),
    "OI-205": (NON_GATING, "user",
               "Half (b), the only open half, is a RESTRUCTURE of two documents that have grown "
               "too large - a filing and rendering question that states nothing false. Carried "
               "with it, because the row states it and the declaration must not hide it: the "
               "row's own recorded timing puts the restructure BEFORE the OI-198/199/200 reviews "
               "consume the document, which is a sequencing constraint on phase 2's conduct and "
               "not a gate on the family design."),
    "OI-219": (NON_GATING, "widening",
               "A WIDENING, stated so the user can correct it: the subject is this project's own "
               "methodology record, which is process apparatus rather than tracking or "
               "documentation apparatus. It is admitted because the row itself settles the "
               "bearing test - it records that the measurements stand and that what was lost was "
               "the guard against motivated interpretation, so no instrument is in doubt. The row "
               "is record-only and asks for no work."),
    "OI-229": (NON_GATING, "user",
               "The convention is already LIVE for new writing; what remains open is a tree-wide "
               "rename that the user has ruled is not done unilaterally. A rename changes no "
               "rule, no reading and no behaviour - it changes which word carries which sense."),
    "OI-230": (NON_GATING, "user",
               "The writing-standards conformance question, and the user has already DEFERRED it "
               "to a discussion. Its subject is how this project's documents are written."),
    "OI-233": (NON_GATING, "user",
               "Classified WITH OI-229 deliberately, because they are one subject and judging "
               "them apart would make the verdict turn on which document a reader opened. The "
               "FALSE EXECUTION CLAIM - the part that stated something untrue - is already "
               "corrected; what stays owed is the vocabulary pass over the canonical document, "
               "sequenced against OI-229 by the row's own text."),
    "OI-280": (NON_GATING, "user",
               "One label, 'D5', naming two unrelated rulings from two private numbering series. "
               "A LABEL defect: both decisions' content is ratified and unaffected, and the owed "
               "act is to name each label's series or drop the private labels."),
    "OI-281": (NON_GATING, "user",
               "Whether a delegation pointer confers contract-home status - a question about how "
               "the decisions register classifies homes. It moves no decision's content and no "
               "statement about the analysis."),
    "OI-282": (NON_GATING, "user",
               "A PLAN document still presents as future work a half delivered and ratified the "
               "next day. The falsehood is real but it sits in a tracking surface: the analysis "
               "fact it concerns - the five-idiom set - is correctly recorded in the canonical "
               "document and in the register, so no specification of the analysis is wrong."),
    # OI-287's verdict moved to RETIRED_VERDICTS on 2026-08-03 when the row closed.
    "OI-290": (NON_GATING, "user",
               "A section of a corpus document mixes rules and findings, which the home "
               "criterion then classifies as one block. A SECTION-BOUNDARY defect in how the "
               "register homes entries; the eleven entries themselves stand."),
    "OI-297": (NON_GATING, "user",
               "A check over DISPATCHES AND REPORTS truncates its console output; the JSON "
               "artifact every citation actually uses is written first and is complete, so no "
               "recorded figure is affected and no measurement of the analysis depends on it. "
               "Classified apart from OI-292 deliberately, and the difference is stated so the "
               "pair does not read as inconsistent: OI-292 gates because two of its members are "
               "measurement rules and a third guards the local patches to MuseScore's own code, "
               "while this row's whole subject is one tool's stdout rendering over documents."),
    "OI-296": (NON_GATING, "user",
               "A sweep for ratified rules recorded in tracking sections rather than in the "
               "section they amend. Where a rule is FILED, not what it says."),
    "OI-298": (NON_GATING, "user",
               "A binding rule POINTS at an enumeration the user has not ratified. What is owed "
               "is a pointer and a ratification status - the user's own apparatus examples - and "
               "the six subjects the clause itself names bind on the clause's own authority "
               "either way, so nothing about the analysis or its inputs turns on the ruling. It "
               "is deliberately NOT read as specification completion: no specification is "
               "incomplete or false here, and the clause was left unchanged precisely so that "
               "remains true."),
    "OI-301": (NON_GATING, "user",
               "A tracking-surface check's REPORTING behaviour: a historical mode overwrites the "
               "frozen split-reconciliation artifact with a failing report. Apparatus by the "
               "user's own line - what is owed is that a check stop destroying a filing record. "
               "Classified with [[OI-297]] and apart from OI-292 on the same ground the OI-297 "
               "verdict states: no measurement of the analysis depends on it, and the register's "
               "health is separately established by the LIVING mode, which passes. Its fix's "
               "establishment run gates on its own account under the exemption."),
    "OI-299": (NON_GATING, "user",
               "The SHAPE of the open-items index: whether a row carries its narrative or points "
               "at it. Tracking apparatus in the user's own words, and the register's own status "
               "of record is not what changes. Its establishment run is named on the row and "
               "gates on its own account under the exemption below - the row's apparatus half "
               "does not carry the obligation with it."),
    # OI-305 and OI-306 (rowed 2026-08-03, phase 1w) are NOT first-cut candidates -- the
    # over-inclusive vocabulary does not reach their subject columns -- so no verdict is authored
    # for them here. The tool refuses one for a non-candidate, correctly: a hand-added verdict for a
    # row the cut never proposed would be the hand-listing CLAUDE.md forbids. Both therefore carry
    # the default, which is that they GATE.
    # ---------------------------------------------------------------------- GATES
    "OI-302": (GATES, "the default - the row's own scope does not settle it",
               "Half (a) IS apparatus: whether the decisions register gains a field for a mark "
               "whose subject is dormant while its prohibition is live. The other halves are not. "
               "Whether D-423's three prohibitions bind the LIVE design is a ruling about what the "
               "family design may do, and D-055's half is a factual question about production code "
               "(a preference registered unconditionally whose consumer is the legacy scorer). A "
               "row that is not wholly apparatus, or whose subject its own text does not settle, "
               "GATES by the declaration's own default - the declaration only ever removes a wait "
               "where the row supports removing it."),
    "OI-303": (GATES, "a statement about the analysis's build state",
               "Six comments in src/ and tools/ say the record arm is 'default OFF' and that the "
               "record section adapter has no caller. D-438's line inside the documentation rows "
               "makes a correction to a statement about the analysis or its BUILD STATE gating, "
               "and every one of the six is exactly that - they are where a reader goes to learn "
               "which analysis arm runs, and all six name the dormant one."),
    "OI-304": (GATES, "a statement about the analysis's build state",
               "Two dated annotations assert that the owed iteration-API renames have a subject "
               "including LIVE Layer-1.5 code; D-428 was corrected against the call sites one wave "
               "later and records that every use sits on the legacy arm. What is owed is the "
               "correction of a statement about which code is live - the same D-438 clause as "
               "[[OI-303]], not a filing or a pointer."),
    "OI-300": (GATES, "an establishment obligation (#19) - the exemption, not the criterion",
               "Its whole subject is a mechanism's MEASURED false-deny and detection rates over "
               "two shapes its corpora do not contain. Classified GATES on the exemption alone, "
               "and the exemption is what makes the classification easy: an establishment "
               "obligation always gates whatever its subject, because backgrounding one is how "
               "it never happens. The apparatus test is not reached and is not applied."),
    # OI-316 and OI-319 (rowed 2026-08-04, READ WAVE 1) are NOT first-cut candidates -- the
    # over-inclusive vocabulary does not reach their subject columns -- so no verdict is authored
    # for them here, on the OI-305/OI-306 precedent four rows above. Both therefore carry the
    # default, which is that they GATE. OI-319 reads as apparatus (a section-pointer field) and
    # its own text says so; that is not enough, and the row records why.
    "OI-317": (NON_GATING, "user",
               "A document's STATUS BANNER says the file is uncommitted and under a commit hold; "
               "it is committed. D-438's line inside the documentation rows names a banner as "
               "apparatus in terms. The substantive half of the same document's staleness -- what "
               "it says about the piece-start shortcut -- is a separate row, OI-315, which gates."),
    "OI-318": (NON_GATING, "user",
               "Two LABELS in the canonical document: the Layer-6 section still calls the grouping "
               "unit a 'phrase' after the ratified rename reserved that word, and one section "
               "number is used twice. D-438's line names a label and an anchor as apparatus, and "
               "item (1) is already sequenced as its own scoped terminology work item under "
               "OI-229. Neither states anything false about what the analysis does."),
    # ---------------------------------------------------------------------- GATES
    "OI-315": (GATES, "a statement about the analysis's build state",
               "The canonical specification describes a key-layer behaviour in the present tense "
               "that the code removed on 2026-06-14, and register entry D-058 carries it LIVE. "
               "D-438's line inside the documentation rows makes a correction to a statement about "
               "the analysis or its BUILD STATE gating, and this is one with a live register entry "
               "riding on it -- the same clause as OI-303 and OI-304, one surface further in."),
    "OI-45": (GATES, "specification completeness",
              "Half of it is stale anchors, which would be apparatus - but the other half is a "
              "scoring constant with no entry in the scoring specification at all, and phase 1 "
              "requires specifications COMPLETE, not only true. The whole row gates with its "
              "gating half."),
    "OI-57": (GATES, "the analysis's inputs",
              "The extra-scores registry is stale and unvalidated against what is on disk, and "
              "the row states the registry must be accurate and mechanically validated before "
              "any of those scores is used. A corpus register is an input to every measurement "
              "taken on it (#9)."),
    "OI-63": (GATES, "the analysis",
              "The mode prior is an analysis quantity; single-sourcing it is a #6 act inside the "
              "analysis, not in the paperwork."),
    "OI-95": (GATES, "an instrument a measurement depends on",
              "A duplicate disposition generator and line-stale audit inventories. The "
              "disposition generators are the instruments the audit passes run through, and "
              "phase 2's remaining partitions are audit passes."),
    "OI-105": (GATES, "specification truth",
               "Two FALSE STATEMENTS, not pointers: a predicate's name says semitone where it "
               "answers true for a whole tone, and a manifest note says the decoder is not called "
               "by batch_analyze. Both describe the analysis wrongly."),
    "OI-107": (GATES, "specification truth",
               "Stale scoring values, a wrong bit order and pre-refactor gate descriptions in the "
               "canonical document - statements about the analysis that are false at HEAD, with "
               "part still owed after the phase-1 truth-sync."),
    "OI-121": (GATES, "specification truth",
               "The Layer-5 design document future-tenses a grammar completion that has landed. "
               "A false statement about what is built, which is exactly phase 1's subject."),
    "OI-146": (GATES, "the analysis",
               "The evidence inventory is the live catalog of what each layer discovers, and the "
               "layer specifications update from it as facts are adopted. Its subject is analysis "
               "facts, not the paperwork about them."),
    "OI-150": (GATES, "an instrument a measurement depends on",
               "The recorded test baselines are stale and the notation line hides four xfails. A "
               "baseline is what a regression is measured against."),
    "OI-154": (GATES, "the default - out of the declared class",
               "Explainability as an end-user feature is a product requirement, not this "
               "project's tracking or documentation apparatus, so the declaration does not reach "
               "it and the default applies. Recorded honestly: the row's own status is 'held' "
               "pending an unrelated publication wave, so nothing turns on the verdict today."),
    "OI-183": (GATES, "specification completeness",
               "Twelve of thirty-two override-registered scoring constants have no by-name "
               "mention in the scoring specification. Incompleteness of a specification, the "
               "same ground as OI-45."),
    "OI-207": (GATES, "the analysis",
               "The decision-conformance audit searches the implementation for opposition to "
               "recorded decisions; its residual second pass is a phase-2 discovery channel and "
               "is classified GATING in the phase-3 gate partition. The two verdicts must agree "
               "and do."),
    "OI-220": (GATES, "specification truth",
               "Six or more joint-module headers say the module is dormant with no production "
               "consumer while it IS the production notation analysis. The same class as the "
               "scoring document's stale present tense, inside the analysis's own headers."),
    "OI-222": (GATES, "an instrument a measurement depends on",
               "The blinding of an audit pass was defeated at the source, so that pass's "
               "knowledge-free-discovery claim is compromised. #19 treats a search as a "
               "measurement tool, and phase 2's bounded trust statement is arithmetic over "
               "exactly these detection-power claims."),
    "OI-223": (GATES, "an instrument a measurement depends on",
               "The committed per-layer audit inventories are commit-stale, so a session that "
               "reads them instead of regenerating measures a build that no longer exists. "
               "Phase 2's remaining partitions are the sessions that would read them."),
    "OI-239": (GATES, "the analysis's inputs",
               "The joint fact adapter re-implements the Layer-2 boundary rule with three "
               "behavioural differences and no specification records that it does. The adapter IS "
               "the input surface; this is the same subject as the family rows on note "
               "eligibility and representation."),
    "OI-256": (GATES, "an instrument a measurement depends on",
               "The production interactive path's seams are largely untested and every "
               "large-score test is a disabled measurement rather than a gate. The row is also "
               "named as the input list for the record-seams audit partition, which gates."),
    "OI-259": (GATES, "the record already names it a phase-3 input",
               "Its own status reads 'phase-3 input (D-231)': every engage-era row needs one "
               "fate before the prioritized fix plan can cover the complete list."),
    "OI-267": (GATES, "the record already names it a phase-3 input",
               "Its own subject column reads 'user-directed planning / phase-3 input', and the "
               "question is whether tonicization labels are needed for maximum-precision "
               "inference - an analysis-output question."),
    "OI-274": (GATES, "specification truth",
               "REPORTED AS A DIFFERENCE from the dispatch's assumption A3, which put this row's "
               "body-tense half in the apparatus set. The document opens by stating that the "
               "legacy scorer IS the bottom-up vertical-sonority scorer and keeps that present "
               "tense throughout, while that scorer is dormant on both production surfaces - and "
               "`CLAUDE.md` directs every scoring session to read it with no other mandated read "
               "correcting it. A false statement about what runs, in a mandatory read, is the "
               "phase-1 truth class, not a banner."),
    "OI-276": (GATES, "specification truth",
               "Three live-specification documents state as current what is false at HEAD, and "
               "one names as its acceptance criterion, five times, a regression gate superseded "
               "in whole. A stale criterion is not a description - it is what a future build "
               "would try to satisfy."),
    "OI-283": (GATES, "#19 establishment obligation",
               "Gates on the exemption, and independently on the criterion: the register's "
               "coverage claim bounds which parts of the canonical document any "
               "decision-conformance finding could have come from, so an unread range could still "
               "hold a decision about the input surface."),
    # OI-289's verdict moved to RETIRED_VERDICTS on 2026-08-03 when the row was verified.
    "OI-292": (GATES, "the default - the row's scope does not settle it",
               "Most of the row is enforcement machinery for governing-document rules, which is "
               "apparatus - but two of its ten members are measurement rules (uncertainty on "
               "every reported comparison; the research-tier-on-entry rule the corpus manifest "
               "would carry) and a third guards the local patches to MuseScore's own code. Those "
               "bear on instruments and on the system, so the default applies to the row as a "
               "whole rather than splitting a row the register keeps as one."),
    # ---- rowed 2026-08-04 by READ WAVE 2 -------------------------------------------------
    # OI-321 and OI-323 are NOT first-cut candidates -- the over-inclusive vocabulary does not
    # reach their subject columns -- so no verdict is authored for them, on the OI-305/OI-306
    # precedent, and both carry the default, which is that they GATE. That is the right answer
    # for both on the criterion anyway: OI-321 is statements about the analysis's build state,
    # and OI-323 is an establishment obligation.
    "OI-320": (GATES, "the criterion - the row's subject bears on an instrument",
               "A corpus/score inventory names the SUPERSEDED batch case-identity sets as the "
               "current acceptance gate, three times, and tells the reader the granularity-robust "
               "metric does not exist yet. That is a statement about an instrument a measurement "
               "depends on and about the analysis's build state, which D-438's line inside the "
               "documentation rows puts on the gating side; and the document is the one CLAUDE.md "
               "makes a mandatory first read for any task that touches scores, so a session is "
               "pointed at the retired gate before it reads anything else."),
    "OI-322": (GATES, "the criterion - the row's subject bears on the analysis",
               "A completed audit describes five pieces of analysis-tool code in the present tense "
               "-- with call-site line citations and three open questions -- that its own last line "
               "says were deleted. The subject is what the code does and whether a symbol may reach "
               "the analyzer, not a banner or a label: D-438's apparatus line does not reach it. "
               "(The document's FILING -- re-banner as a historical record or rewrite -- is "
               "apparatus, but it is the remedy's shape, not the row's subject.)"),
    "OI-324": (GATES, "the criterion - the row's subject bears on what the emission reads",
               "Whether the priority-of-evidence ranking binds the production emission or only the "
               "legacy key path is a question about the evidential contract the joint emission is "
               "measured against -- OI-228 puts that very premise under load. Nothing about it is "
               "apparatus. The row's smaller second half (an unqualified predicate in the same "
               "paragraph pair) would be apparatus on its own and does not lift the row."),
    # ---- rowed 2026-08-04 by READ WAVE 4 -------------------------------------------------
    "OI-327": (NON_GATING, "user",
               "Five drafted delegation clauses awaiting the user's word. The subject is WHERE a "
               "decision is recorded and which surface delegates to which document -- the "
               "decisions register's own filing apparatus, which D-438's line inside the "
               "documentation rows names on the apparatus side in terms (a pointer, an anchor, a "
               "filing decision). It bears on no analysis, no input and no instrument: the "
               "decisions the five documents hold are already registered and already readable at "
               "their homes, and what the delegations would change is the CLASS the register "
               "records for those entries, not their content. It carries no establishment "
               "obligation, so the starred clause that makes those gate whatever their subject "
               "does not reach it either."),
    # ---- rowed 2026-08-04 by READ WAVE 5 -------------------------------------------------
    "OI-329": (NON_GATING, "user",
               "Two live register entries recording ONE rule at ONE home, after the wave's own "
               "widening of a principle that already had an entry. The subject is HOW MANY "
               "REGISTER ROWS record one rule -- the decisions register's own filing apparatus, "
               "which D-438's line inside the documentation rows names on the apparatus side in "
               "terms (a filing decision). It is on the apparatus side for the reason the line "
               "makes decisive -- WHAT IS OWED decides it, and what is owed here is a filing "
               "choice among three named treatments, not a correction to any statement about the "
               "analysis: the RULE, its width and its home are not in doubt, both entries quote "
               "it correctly and both verify at the cited lines, so no reader is misled about "
               "anything the analysis does. It bears on no analysis, no input and no measurement "
               "tool, and it carries no establishment obligation, so the starred clause that "
               "makes those gate whatever their subject does not reach it either."),
    # ---- rowed 2026-08-04 by READ WAVE 6 -------------------------------------------------
    # Two rows, and they fall on opposite sides -- which is the criterion doing its job rather
    # than a close call. Both verdicts are made against the row's SUBJECT, never its remedy.
    # ---------------------------------------------------------------------- GATES
    "OI-331": (GATES, "the criterion - the row's subject bears on the analysis's inputs",
               "A LIVE, user-ratified register entry names a convergence proxy the build MEASURED "
               "FALSE and dropped, and the entry carries no annotation. The subject is a binding "
               "contract rule about HOW MUCH MUSIC THE ANALYSIS READS before it commits to a key "
               "-- the analysis's own input scope, which is the strongest form D-438's test has. "
               "A session applying the rule as written would build a stop condition already "
               "measured not to work. Nothing about it is apparatus: what is owed is not a "
               "pointer, an anchor or a filing choice but the correction of a rule, which "
               "D-438's line inside the documentation rows puts on the gating side in terms."),
    # ---------------------------------------------------------------------- NON-GATING
    "OI-332": (NON_GATING, "user",
               "Three documents misdescribe their OWN state: a 'no code' status banner over a "
               "design whose two operations are built, two stale as-built code line anchors, and a "
               "design carrying no note that the approach it builds toward was later falsified. "
               "D-438's line inside the documentation rows names a BANNER and an ANCHOR as "
               "apparatus in terms, and the third item is a missing cross-reference between two "
               "documents. WHAT IS OWED decides it, and what is owed here is three pointers -- not "
               "a correction to any statement about the analysis or its build state: every "
               "substantive claim these documents make was checked and holds, and what survives "
               "the falsified approach is registered separately as D-616 and D-617. It bears on no "
               "analysis, no input and no measurement tool, and it carries no establishment "
               "obligation, so the starred clause does not reach it either."),
    # ---- rowed 2026-08-04 by the finish-line item-1b wave ---------------------------------
    # OI-340's verdict moved to RETIRED_VERDICTS on 2026-08-04 when the user ruled the question.
    # ---------------------------------------------------------------------- NON-GATING
    "OI-338": (NON_GATING, "user",
               "The phase-1 completion inventory publishes as an OPEN QUESTION one the user has "
               "since ruled (D-639), because its clause quote is derived and moved with HEAD while "
               "its criteria are an authored constant that did not -- so a check passes over a "
               "self-contradiction inside one file. WHAT IS OWED decides it, and what is owed is a "
               "correction to an AUDIT ARTIFACT's authored prose about the status of a ruling: "
               "apparatus in the plainest form D-438's line names, one document over from OI-332's "
               "banners and OI-334's scope sentence. It bears on no analysis, no analysis input and "
               "no instrument any measurement of the analysis depends on -- every population the "
               "inventory DERIVES is current and re-derives byte-identically, which is the half a "
               "measurement would rest on. It carries no establishment obligation (#19): nothing "
               "here is an instrument trusted without being established, so the starred clause that "
               "makes those gate whatever their subject does not reach it. Recorded against the "
               "row's SUBJECT, never its remedy -- and the remedy is deliberately open, since a "
               "re-wording and a structural fix are both available and neither is proposed."),
    # [[OI-333]] takes no authored verdict here and needs none: its subject column is the
    # instrument/measurement layer, which the over-inclusive first cut does not propose as an
    # apparatus candidate, so it GATES by the declaration's own default -- which is also the right
    # answer on the criterion (an instrument a measurement depends on, and independently an
    # establishment obligation). The same is true of [[OI-328]] and [[OI-330]]. Recorded here
    # because the tool STOPPED on a verdict for a non-candidate, which is how it was confirmed.
}

# The dispatch's assumption A3, recorded so the difference is reported rather than reconciled.
A3 = {
    "as_stated_in_the_dispatch": (
        "That OI-280, OI-282, OI-287 and OI-274's body-tense half are the complete apparatus-row "
        "set."
    ),
    "its_declared_source": "Cowork has read each of those rows, but not that the set is exhaustive.",
}


def parse_rows():
    rows = []
    for ln in INDEX.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("| OI-"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
        if len(cells) != 6:
            continue
        rows.append({
            "id": cells[0],
            "title": cells[1],
            # The description cell is parsed here and used by no verdict in THIS tool; it is
            # returned so that a second reader of the register does not need a second parser
            # (#6). Nothing below reads it, and no artifact of this tool carries it.
            "description_column": cells[2],
            "subject_column": cells[3],
            "status_column": cells[4],
            "open": "✅" not in cells[4],
        })
    return rows


def build():
    rows = parse_rows()
    by_id = {r["id"]: r for r in rows}
    open_rows = [r for r in rows if r["open"]]

    cut = [r for r in open_rows
           if any(v.lower() in r["subject_column"].lower() for v in FIRST_CUT_VOCAB)]
    cut_ids = [r["id"] for r in cut]

    missing = [i for i in cut_ids if i not in V and i not in RETIRED_VERDICTS]
    stray = [i for i in V if i not in cut_ids]
    # A retired verdict must name a row that is genuinely no longer an open candidate; if the
    # row reopens, the verdict must come back to V rather than sit silently in history.
    wrongly_retired = [i for i in RETIRED_VERDICTS if i in cut_ids]
    if wrongly_retired:
        raise SystemExit("STOP: retired verdicts for rows that are open first-cut candidates "
                         "again: " + ", ".join(sorted(wrongly_retired)))
    if missing:
        raise SystemExit("STOP: first-cut candidates with no authored verdict: "
                         + ", ".join(sorted(missing)))
    if stray:
        raise SystemExit("STOP: authored verdicts for rows that are not open first-cut "
                         "candidates (the register moved under the table): "
                         + ", ".join(sorted(stray)))

    items = []
    for rid in cut_ids:
        verdict, ground, reason = V[rid]
        r = by_id[rid]
        rec = {
            "id": rid,
            "title": r["title"],
            "subject_column": r["subject_column"],
            "verdict": verdict,
            "reason": reason,
        }
        if verdict == NON_GATING:
            rec["class_basis"] = {
                "user": "tracking/documentation apparatus - the user's own phrase",
                "widening": ("process apparatus - a WIDENING of the user's phrase, stated as a "
                             "judgment and the user's to correct"),
                "row-says": "the row's own recorded status already says it gates nothing",
            }[ground]
        else:
            rec["gate_ground"] = ground
        items.append(rec)

    non_gating = [i for i in items if i["verdict"] == NON_GATING]
    gates = [i for i in items if i["verdict"] == GATES]

    ng_ids = sorted(i["id"] for i in non_gating)
    a3_ids = ["OI-274", "OI-280", "OI-282", "OI-287"]
    # A row that has since CLOSED is neither a confirmation nor a refutation of the assumption:
    # it left the population rather than changing class. Counting it as refuted would report a
    # movement that never happened.
    a3_closed = [i for i in a3_ids if i in RETIRED_VERDICTS]
    a3_live = [i for i in a3_ids if i not in a3_closed]
    a3_confirmed = [i for i in a3_live if i in ng_ids]
    a3_refuted = [i for i in a3_live if i not in ng_ids]
    a3_missed = [i for i in ng_ids if i not in a3_ids]

    return {
        "purpose": (
            "The NON-GATING apparatus declaration: which OPEN register rows gate no stage and "
            "are worked in leftover capacity. It removes a wait; it authorizes no fix, no design "
            "and no inference change."
        ),
        "generated_by": "tools/audit/gen_nongating_apparatus_rows.py",
        "generated_for": "cc_instruction_phase1o_gate_partition_and_probe_rerun.md, Task 3",
        "the_ruling": THE_RULING,
        "the_criterion": THE_CRITERION,
        "the_exemption": THE_EXEMPTION,
        "the_default": THE_DEFAULT,
        "the_line_this_derivation_draws": THE_LINE,
        "what_is_authored_and_what_is_derived": {
            "derived": ("the row population and its OPEN subset, parsed from OPEN_ITEMS.md; the "
                        "over-inclusive first cut on each row's own subject column; every count"),
            "authored": "the per-row verdict and its reason, read at the row itself",
            "the_two_stops": (
                "The tool refuses to run if a first-cut candidate has no authored verdict, and "
                "refuses an authored verdict for a row that is not an open candidate - so the "
                "table cannot drift away from the register without failing loudly."
            ),
        },
        "population": {
            "rows_parsed": len(rows),
            "open_rows": len(open_rows),
            "first_cut_candidates": len(cut),
            "first_cut_vocabulary": FIRST_CUT_VOCAB,
        },
        "totals": {
            "non_gating": len(non_gating),
            "gates": len(gates),
            "non_gating_ids": ng_ids,
            "non_gating_by_class_basis": {
                b: sorted(i["id"] for i in non_gating if i["class_basis"].startswith(p))
                for b, p in (("user", "tracking/documentation"),
                             ("widening", "process apparatus"),
                             ("row-says", "the row's own recorded status"))
            },
            "gates_by_ground": {
                g: sorted(i["id"] for i in gates if i["gate_ground"] == g)
                for g in sorted({i["gate_ground"] for i in gates})
            },
        },
        "items": items,
        "retired_verdicts": {
            "what_this_is": (
                "Verdicts for rows that have since CLOSED. The tool stops on a live verdict "
                "naming a row the INDEX no longer carries open - correctly, since that is how a "
                "stale declaration survives an unnoticed resolution - and deleting the reasoning "
                "would lose it (#12), so it is preserved here. Never counted; if the row reopens, "
                "the tool stops until the verdict is moved back."
            ),
            "entries": {
                rid: {"verdict": v, "class_basis_or_ground": g, "reason": reason,
                      "closed": closed}
                for rid, (v, g, reason, closed) in sorted(RETIRED_VERDICTS.items())
            },
        },
        "assumption_A3_of_the_dispatch": dict(
            A3,
            verdict="DIFFERS in both directions - reported, not reconciled",
            confirmed=a3_confirmed,
            refuted=a3_refuted,
            closed_since_the_declaration=a3_closed,
            closed_note=(
                "A row A3 named that has since been RESOLVED is neither a confirmation nor a "
                "refutation: it left the population rather than changing class. Its verdict is "
                "kept at `retired_verdicts`."
            ),
            refuted_note=(
                "OI-274 is NOT apparatus. Its subject is a mandatory session-start read that "
                "states in the present tense that a dormant scorer is what runs; correcting a "
                "false statement about what runs is phase 1's own subject, not leftover-capacity "
                "work."
            ),
            not_in_A3_but_derived=a3_missed,
            missed_note=(
                "The rows A3 did not name are mostly the older doc-sync backlog - dangling "
                "references, contradicting records, banner acts - plus the register-machinery "
                "rows opened in the last several waves and the two terminology rows. A3 was not "
                "wrong about the four it looked at; it had not looked at the population."
            ),
        ),
        "relation_to_the_phase3_gate_partition": (
            "Different question, different population, and the two must not be read as one. "
            "`tools/audit/phase3_gate_partition.json` classifies the items of PHASE 2 against "
            "whether they could find another member of the struck-versus-sounding family; this "
            "artifact classifies OPEN REGISTER ROWS against whether their subject bears on the "
            "analysis at all. A row can be non-gating for the family design and still gate its "
            "own stage, or the reverse. Where both artifacts speak about the same object they "
            "agree by construction, because the establishment exemption is stated once and "
            "applies in both."
        ),
        "what_this_declaration_does_NOT_do": [
            "It does not close any row. A NON-GATING row stays open and stays owed.",
            "It does not reach an establishment obligation (#19), which always gates.",
            "It does not authorize any fix, design or inference change.",
            ("It does not decide phase 1's own completion: a NON-GATING row is still work phase 1 "
             "may be waiting on for its own reasons, and this artifact says only that no stage "
             "waits on it."),
        ],
    }


def main(argv):
    doc = build()
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT} does not exist")
            return 1
        if json.loads(OUT.read_text(encoding="utf-8")) == doc:
            print(f"PASS: {OUT.name} re-derives byte-identically "
                  f"({doc['totals']['non_gating']} non-gating / {doc['totals']['gates']} gates of "
                  f"{doc['population']['first_cut_candidates']} candidates over "
                  f"{doc['population']['open_rows']} open rows)")
            return 0
        print(f"FAIL: {OUT.name} differs from what the generator now produces")
        return 1
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"  open rows {doc['population']['open_rows']}, first-cut candidates "
          f"{doc['population']['first_cut_candidates']}")
    print(f"  NON-GATING {doc['totals']['non_gating']}, GATES {doc['totals']['gates']}")
    a3 = doc["assumption_A3_of_the_dispatch"]
    print(f"  A3: confirmed {a3['confirmed']}, refuted {a3['refuted']}, "
          f"not in A3 but derived {len(a3['not_in_A3_but_derived'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
