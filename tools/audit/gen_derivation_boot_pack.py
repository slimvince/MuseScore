#!/usr/bin/env python3
"""THE DERIVATION BOOT PACK — the curated boot list, CUT for one subject and RENDERED WHOLE.

THE RULING THIS EXISTS FOR (user, 2026-08-22, amendment (a1) of Ruling 1 of
`cowork_rulings_2026_08_22_boot_list_sitting.md`), quoted verbatim:

    A per-session WITHHELD LIST, generated, never hand-cut.  A dispatch for a session that runs
    the held-out test (Ruling 4 of 2026-08-21) names the withheld register identities as an
    AUTHORED INPUT carrying finding, date and reason -- the same shape as an authored exclusion
    (D-677; the `STATUS.md` exclusion of `gen_specification_document_set.py`).  A generator cuts
    member (5) to the `DESIGN-INTENT` class LESS those identities, derives and adds every entry of
    the class that quotes or cross-references the withheld oracle's home lines, STOPs on a named
    identity that is not in the class, and publishes the cut artifact; the session boots from that
    artifact and never from the whole sort.

and, on the second withheld input (user, 2026-08-22, Ruling 1 of
`cowork_rulings_2026_08_22_member_two_leak_sitting.md`):

    For the harmony-boundary subject, the generator's authored `WITHHELD` table carries, beside the
    withheld register identities and the withheld document, a WITHHELD PASSAGE: the
    founding-instance sentence of the never-work-from-memory rule in `CLAUDE.md`'s Conventions
    span, LOCATED BY ITS OWN TEXT AND NEVER BY LINE NUMBER, with finding, date (2026-08-22) and
    reason -- the D-677 shape.

WHAT THE PACK IS.  A deriving session is an implementation-blind session: it writes what the
analysis SHOULD do for one unit without reading what the code or the specifications say it DOES.
The curated boot list (ruled 2026-08-22: six members, eight exclusions, three amendments) is the
implementation-free read list such a session boots from.  This tool RENDERS that list into a
self-contained directory, `tools/audit/derivation_boot_pack/<subject>/`, with the withheld family
for that subject cut out of it, and publishes the manifest of what it did.

WHAT IS AUTHORED AND WHAT IS DERIVED, stated because the difference is the whole value:

  AUTHORED -- the six ruled MEMBERS and the spans that make them up, EACH BY ANCHOR TEXT AND NEVER
              BY LINE NUMBER, IMPORTED from the ruled draft
              (`cowork_curated_boot_list_draft_2026_08_19.md` §2, ruled 2026-08-22) rather than
              re-decided here; and the `WITHHELD` table per subject -- the register identities, the
              documents and the passages withheld, each carrying its finding, its date and its
              reason (the D-677 shape: an INPUT to the derivation, never a hand edit to its output,
              so `--check` re-renders the pack with the withholding applied); and one verdict --
              IN, OUT or UNPLACED -- per derived candidate, each with its finding, date and reason.
  DERIVED  -- the CANDIDATE LIST for the subject, from the sort artifact and the decisions
              register's data file, with the matching criterion recorded per candidate; the
              CROSS-REFERENCE ADDITIONS to the withheld set; the CUT of the `DESIGN-INTENT` class;
              the LEAK check over the two members whose text is generated rather than quoted; every
              rendered file, byte for byte; and every count.

THE SIX MEMBERS, as ruled:
  (1) `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` -- the phase
      definitions section, whole.
  (2) `CLAUDE.md` -- TWO spans only: the guiding principles through the delegation pointer, and the
      conventions through the self-check.
  (3) `cowork_design_doc_template.md` -- whole.
  (4) `cowork_audit_protocol.md` -- the dispatch-protocol section, to the end of the file.
  (5) the `DESIGN-INTENT` class of `tools/audit/rulings_sort_classification.json`, CUT to the
      admitted identities and rendered with FOUR fields only -- `id`, `title`, `verbatim`, `plain`.
      The register's `home`, `rationale`, `status_source` and `patterns` are NOT rendered: each
      names a place or a fact in the implementation's own documents.
  (6) `DEFECT_TYPES.md` -- the catalog table's `ID` and `type (plain)` columns only, header row
      included (amendment (a3); the founding-instance and detection-signature columns are
      implementation descriptions and are excluded).

THE LEAK CHECK, AND ITS SCOPE, STATED HERE BECAUSE A SCOPE THAT IS NOT STATED READS AS TOTAL.  It
runs over MEMBERS (5) AND (6) ONLY -- the two members this tool GENERATES rather than quotes.  An
entry whose rendered fields carry a withheld identity string, the withheld document's name, a
`docs/` or `src/` path, or the string `ARCHITECTURE.md` is NOT rendered into the pack: it is listed
in the manifest under `LEAKS` with the field and the string that matched, and it goes to the user in
the reading file beside the withheld family.  A LEAK IN MEMBERS (1)-(4) IS NOT CHECKED, and that is
deliberate rather than an omission: those members are ruled WHOLE, and member (2)'s Conventions span
names `ARCHITECTURE.md` in the never-work-from-memory rule BY DESIGN -- a string check over them
would strike the rule that tells a deriving session where a primary source lives.  What member (2)
carries that a string check could not have caught is handled by the authored withheld PASSAGE
instead, which is the second ruling above.

THE STOPS, so this cannot silently stop being a derivation:
  1. an ANCHOR that is not found EXACTLY ONCE in its file STOPS the tool -- so no span is ever cut
     from a coordinate that has drifted, and no member is rendered from a file that has moved under
     its own heading;
  2. an authored withheld IDENTITY that is not in the `DESIGN-INTENT` class STOPS it -- the
     ruling's own condition, made mechanical;
  3. an authored withheld identity, document or passage MISSING its finding, its date or its
     reason STOPS it -- amended #10's own demand of a withholding record, in the shape
     `gen_specification_document_set.AUTHORED_EXCLUSIONS` already uses;
  4. a derived CANDIDATE with no authored verdict STOPS it, and a verdict naming an entry the
     derivation does not return as a candidate STOPS it -- the two directions together, so a
     candidate cannot be graded by silence and a verdict cannot outlive its subject;
  5. a verdict outside the closed three-value vocabulary STOPS it, and so does a verdict whose
     distribution does not account for the candidate population;
  6. an authored withheld IDENTITY that is not among the candidates STOPS it -- the family is a
     subset of what the criterion returns, so an identity nobody derived cannot be withheld by
     assertion;
  7. a member's file that the tree does not carry STOPS it;
  8. a withheld PASSAGE whose opening or closing anchor is not found exactly once inside the
     bullet the ruling scopes it to STOPS it, and so does a closing anchor that precedes its
     opening.

WHAT THIS DOES NOT ASSERT.
  * That the CANDIDATE CRITERION is complete.  Its reach is that of a pattern match over the
    register's own text and it is UNMEASURED (#19, D-673); the bound is stated on the artifact at
    `★_the_bound_on_the_candidate_criterion` and an empty match is evidence of nothing.  No
    analysis decision consumes this enumeration -- the user does -- which is the test D-673 fixes.
  * That any verdict is right.  Every verdict is AUTHORED and CLEARS NOTHING (D-655): the family is
    delivered as a reading file and the user rules it before any session boots from the pack.
  * That member (2) carries no other leak.  The ruling that added the withheld passage says in its
    own words that the span was searched for the oracle's own phrases and not for every paraphrase.
  * That the cross-reference additions are transitive.  They are derived ONE PASS from the AUTHORED
    identities, not from the additions themselves, and the artifact says so.

AND IT BOOTS NO SESSION.  Rendering the pack is not opening it.

Run:
    python tools/audit/gen_derivation_boot_pack.py                        # render every subject
    python tools/audit/gen_derivation_boot_pack.py --subject harmony-boundary
    python tools/audit/gen_derivation_boot_pack.py --check                # re-render, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "derivation_boot_pack.json")
PACK_ROOT = os.path.join(HERE, "derivation_boot_pack")

SORT = os.path.join(HERE, "rulings_sort_classification.json")
BACKBONE = os.path.join(HERE, "decisions", "backbone_decisions.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout


class Stop(Exception):
    """An anchor drifted, an authored input is incomplete, or a population cannot be placed."""


# ── the closed vocabulary of a verdict ────────────────────────────────────────────────────────
# Named with the `VERDICT_` prefix rather than bare: a bare `OUT` collides with this file's own
# artifact-path constant above, which every sibling generator also names `OUT`.
VERDICT_IN, VERDICT_OUT, VERDICT_UNPLACED = "IN", "OUT", "UNPLACED"
VERDICTS_VOCABULARY = (VERDICT_IN, VERDICT_OUT, VERDICT_UNPLACED)

DATE = "2026-08-22"

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — the six ruled members, each span named by its own anchor text.
#
# IMPORTED from the ruled draft `cowork_curated_boot_list_draft_2026_08_19.md` §2 (ruled by the
# user on 2026-08-22, Ruling 1 of `cowork_rulings_2026_08_22_boot_list_sitting.md`) and NOT
# re-decided here.  Every anchor is a line of the file it names, matched EXACTLY ONCE or the tool
# STOPS.  `kind` says how the span is taken:
#   heading-to-heading   from the line carrying `start` up to (not including) the line carrying `end`
#   heading-to-paragraph from the line carrying `start` up to the end of the paragraph opened by
#                        the line carrying `end` (a paragraph ends at the next blank line)
#   heading-to-eof       from the line carrying `start` to the end of the file
#   whole                the whole file
# ══════════════════════════════════════════════════════════════════════════════════════════════
MEMBERS = [
    {
        "number": 1,
        "filename": "01_the_phase_definitions.md",
        "title": "The six phases and the standing constraints over every one of them",
        "source": "ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md",
        "rendered_from": "the file itself, quoted",
        "spans": [
            {"kind": "heading-to-heading",
             "start": "## 3. DECISION 1 — the proposed phase definitions",
             "end": "## 4. DECISION 2"},
        ],
    },
    {
        "number": 2,
        "filename": "02_the_guiding_principles_and_the_conventions.md",
        "title": "The guiding principles and the conventions",
        "source": "CLAUDE.md",
        "rendered_from": "the file itself, quoted — TWO spans only",
        "spans": [
            {"kind": "heading-to-paragraph",
             "start": "## Guiding principles",
             "end": "**Delegation pointer"},
            {"kind": "heading-to-eof",
             "start": "## Conventions"},
        ],
    },
    {
        "number": 3,
        "filename": "03_the_writing_standards.md",
        "title": "The writing standards every derived specification is written to",
        "source": "cowork_design_doc_template.md",
        "rendered_from": "the file itself, quoted, whole",
        "spans": [{"kind": "whole"}],
    },
    {
        "number": 4,
        "filename": "04_the_dispatch_protocol.md",
        "title": "The dispatch protocol a deriving session is dispatched under",
        "source": "cowork_audit_protocol.md",
        "rendered_from": "the file itself, quoted",
        "spans": [
            {"kind": "heading-to-eof",
             "start": "## The dispatch protocol these audits are commissioned and run under"},
        ],
    },
    {
        "number": 5,
        "filename": "05_the_ratified_design_intent.md",
        "title": "The ratified design intent, CUT for this subject",
        "source": "tools/audit/rulings_sort_classification.json + "
                  "tools/audit/decisions/backbone_decisions.json",
        "rendered_from": "GENERATED — the DESIGN-INTENT class less the withheld family, four "
                         "fields per entry",
        "spans": [],
    },
    {
        "number": 6,
        "filename": "06_the_defect_type_catalog.md",
        "title": "The defect-type catalog — type and definition only",
        "source": "DEFECT_TYPES.md",
        "rendered_from": "GENERATED — two columns of the catalog table",
        "spans": [],
    },
]

READ_ME = "00_READ_THIS_FIRST.md"

# The header row of `DEFECT_TYPES.md`'s catalog table, matched exactly once.  Amendment (a3)
# admits its first two columns — `ID` and `type (plain)` — and excludes the other three.
DEFECT_TABLE_HEADER = "| ID | type (plain) | founding instance | detection signature | mechanical? |"
DEFECT_COLUMNS_KEPT = 2

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — the WITHHELD table, per subject.  Each identity, document and passage carries its
# finding, its date and its reason; one lacking any of the three STOPS the tool (amended #10's own
# demand of a withholding record, in the shape `gen_specification_document_set.AUTHORED_EXCLUSIONS`
# already uses).
#
# `identities` is filled from the AUTHORED verdicts below: every candidate graded IN is withheld.
# What is written here by hand is the ruling's own first identity and its documents and passages.
# ══════════════════════════════════════════════════════════════════════════════════════════════
WITHHELD: dict[str, dict] = {
    "harmony-boundary": {
        "the_subject_in_plain_words":
            "How the analysis should decide where one chord ends and the next begins, and what "
            "evidence decides it.",
        "the_oracle_this_family_protects": (
            "Ruling 4(c) of `cowork_rulings_2026_08_21_successor_plan_sitting.md`: the "
            "evidence-ranking ruling of 2026-08-11 (`ARCHITECTURE.md`, the span opening "
            "\"THE RANKING, and it binds THIS ARM\"), with Claude Code's five recorded corpus "
            "traces of the ratified factorization as the oracle's second arm."),
        "withheld_documents": {
            "cowork_joint_estimator_factorization.md": {
                "finding": ("Ruling 1(a1) of `cowork_rulings_2026_08_22_boot_list_sitting.md` "
                            "records the ten-factor model as ORACLE material for the pilot "
                            "(Ruling 4's second arm), not a boot member."),
                "date": DATE,
                "reason": ("It is the oracle's second arm. A deriving session that read it would "
                           "be reading the answer it is being tested on, and the test that "
                           "positively establishes the method (#19) would be void."),
            },
        },
        "withheld_passages": [
            {
                "file": "CLAUDE.md",
                "member": 2,
                "scope_anchor": "**NEVER WORK FROM MEMORY INSTEAD OF DOCUMENTED FACTS",
                "opens": "**Founding instance:** on 2026-07-28 Cowork reasoned",
                "closes": "which is the general case, not the exception.",
                "finding": ("Ruling 1 of "
                            "`cowork_rulings_2026_08_22_member_two_leak_sitting.md`, widened by "
                            "Ruling 5 of "
                            "`cowork_rulings_2026_08_22_withheld_family_sitting.md`: the "
                            "founding-instance clause of the never-work-from-memory rule states "
                            "both halves of the held-out test's withheld answer for this "
                            "subject, and its remainder tells a deriving session that a "
                            "documented decision on the subject exists and is contradicted by "
                            "the implementation."),
                "date": DATE,
                "reason": ("The narrower cut left a residue that discloses the existence of the "
                           "ruled answer and the implementation's disagreement with it; one "
                           "authored passage with wider anchors removes the clause whole, and "
                           "the statement of the rule itself, above it, stays in the pack."),
            },
            {
                "file": "CLAUDE.md",
                "member": 2,
                "scope_anchor": "**EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME",
                "opens": "Founding instances of the gap:",
                "closes": "each recorded with no derivation.",
                "finding": ("Ruling 1 of "
                            "`cowork_rulings_2026_08_23_member_two_second_leak_sitting.md`: the "
                            "sentence names, from its own words, a boundary-membership "
                            "convention — a tick at a boundary belongs to the segment it "
                            "starts — adjacent to the oracle's ranking of actual sounding notes "
                            "and to withheld D-317's subject, and names the decode segment cap's "
                            "value beside it; it stands in member (2), rendered whole, outside "
                            "the ruled leak-check scope and outside both passages previously "
                            "ruled."),
                "date": "2026-08-23",
                "reason": ("The disclosure is content, not existence — a deriving session learns "
                           "the convention from its name alone; withholding it as an authored "
                           "passage is the mechanism twice ruled for this shape, and the "
                           "bullet's principle stays whole above the cut."),
            },
        ],
        # The identity the ruling names in terms; every other IN verdict below joins it.
        "the_identity_the_ruling_names": "D-057",
    },

    # ── THE SIZING SUBJECT — an EMPTY withheld family by ruling ────────────────────────────────
    # Ruling 1 of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`, quoted verbatim:
    #
    #     a second subject, `scoring-model`: no withheld identities, no withheld documents, no
    #     withheld passages … The standing leak check does the whole of the cutting … The leak
    #     list goes to the user as a reading file in the shape List Four took. Members (1)-(4) and
    #     (6) render whole; member (2) carries NO withheld passage for this subject.
    #
    # THE FAMILY IS EMPTY BECAUSE THIS UNIT IS NOT HELD OUT AND HAS NO ORACLE — not because a
    # search came back empty. There is therefore no candidate criterion either: nothing is
    # withheld, so nothing needs deriving as a candidate and no verdict is authored.
    "scoring-model": {
        "the_subject_in_plain_words":
            "The unit whose specification `docs/scoring_model.md` carries — derived here from the "
            "domain and from the ruled design intent, without that document being opened.",
        "the_oracle_this_family_protects": (
            "NONE. This unit is not held out and has no oracle. Ruling 1 of "
            "`cowork_rulings_2026_08_24_sizing_pilot_sitting.md` rules the withheld family EMPTY "
            "for this subject — no withheld identities, no withheld documents, no withheld "
            "passages — and leaves the whole of the cutting to the standing leak check. The "
            "declined alternatives are recorded at that ruling: withholding in the held-out shape "
            "would starve the derivation of ruled intent no test needs and size a handicapped "
            "method, and reusing the harmony-boundary pack would carry another oracle's cuts."),
        "withheld_documents": {},
        "withheld_passages": [],
        # NO `the_identity_the_ruling_names`: the ruling names none, the family being empty.
    },

    # THE `framework` SUBJECT IS ABSENT DELIBERATELY, not by oversight: its deriving session is
    # not implementation-blind, so no pack is rendered for it and nothing is withheld
    # (`cowork_rulings_2026_08_28_informed_framework_sitting.md`).
}

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — the candidate criterion for each subject, as the dispatch fixes it.
# ══════════════════════════════════════════════════════════════════════════════════════════════
KEYWORDS = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)

CRITERION = {
    "harmony-boundary": {
        "groups": ("E",),
        "home_documents": ("cowork_joint_estimator_factorization.md",
                           "cowork_factorization_desk_simulation.md"),
        "architecture_spans": (
            {"name": "the evidence-ranking ruling of 2026-08-11",
             "kind": "paragraph", "anchor": "THE RANKING, and it binds THIS ARM"},
            {"name": "§5.2's priority-of-evidence table",
             "kind": "table", "anchor": "| Strongest | Actual sounding notes |"},
        ),
        "keywords": KEYWORDS,
        "always": ("D-057",),
    },
    # EMPTY BY RULING, and the emptiness is a statement about the SUBJECT rather than a search
    # result: nothing is withheld for `scoring-model`, so no candidate has to be derived and no
    # verdict has to be authored. Every term is empty, which is the shape the tool's own STOPs
    # already accept — an empty criterion returns no candidate, an empty verdict table grades
    # none, and the distribution accounts for the population exactly.
    "scoring-model": {
        "groups": (),
        "home_documents": (),
        "architecture_spans": (),
        "keywords": (),
        "always": (),
    },
}

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — one verdict per derived candidate: IN, OUT or UNPLACED, each with its finding, its
# date and its reason.  Filled by `cc_instruction_pilot_preparation_withheld_family.md` Task 1(d).
#
#   IN       a deriving session that read this entry would know, in whole or in part, what the
#            ruled answer to *where one chord ends and the next begins, and what evidence decides
#            it* is.
#   OUT      the entry bears on another unit, and reading it tells the session nothing about that
#            answer.  The reason says what it bears on instead.
#   UNPLACED the entry's own text does not settle it.  The reason says what was read.
#
# DEFAULT NOTHING: a verdict that cannot be defended in one sentence at the entry's own verbatim is
# UNPLACED.
# ══════════════════════════════════════════════════════════════════════════════════════════════
VERDICTS: dict[str, dict[str, tuple[str, str, str]]] = {
    "harmony-boundary": {

        # ── IN ────────────────────────────────────────────────────────────────────────────────
        "D-001": (VERDICT_IN,
                  "Its verbatim names segmentation a MODELED (semi-Markov) VARIABLE of the one "
                  "joint decode, and its plain restatement says that single pass 'also decides "
                  "where one chord ends and the next begins'.",
                  "It states how a boundary is decided — jointly, inside the decode, as a modeled "
                  "variable — which is the ruled answer's own first half."),
        "D-022": (VERDICT_IN,
                  "Its verbatim rules that the analysis works 'at the finest grain where harmony "
                  "is well-defined' and makes everything coarser a derived view; its plain names "
                  "that grain 'the smallest stretch over which the sounding harmony does not "
                  "change'.",
                  "It states where a boundary falls — at a change in the sounding harmony — in "
                  "terms."),
        "D-023": (VERDICT_IN,
                  "Its verbatim names the atomic unit 'the constant-sonority slice (L2), never "
                  "the metric beat'; its plain defines it as 'a stretch during which exactly the "
                  "same notes are sounding'.",
                  "It states the boundary rule itself: a boundary is where the sounding set "
                  "changes."),
        "D-024": (VERDICT_IN,
                  "Its verbatim names L2 as 'slicing' and rules L1 and L2 'style-agnostic and "
                  "lossless — they carry facts, never style', with style-specificity confined to "
                  "the judgment layers' calibration.",
                  "It tells a deriving session that where one stretch ends is a fact read from "
                  "the notes and never a style-calibrated judgment, which is part of what "
                  "evidence may decide a boundary."),
        "D-057": (VERDICT_IN,
                  "Amendment (a1) names it as the first withheld identity, and its verbatim IS "
                  "the priority-of-evidence table's strongest row — 'Actual sounding notes | what "
                  "is literally happening now'.",
                  "It is the legacy statement of the withheld oracle's own ranking, so a session "
                  "reading it would read the answer it is being tested on."),
        "D-317": (VERDICT_IN,
                  "Its verbatim closes the backward-walk boundary change — counting notes that "
                  "STOP exactly where a stretch begins as belonging to that stretch — and gives "
                  "the measured reason at the boundary itself, that those notes are other chord "
                  "tones and the root attacks later.",
                  "It rules on how a note's RELEASE relates to a boundary, which is the ruled "
                  "answer's own subject."),
        "D-318": (VERDICT_IN,
                  "Its verbatim closes a short-region external merger because 'the same-root "
                  "merge already inside the first pass has combined those stretches before any "
                  "external pass could see them'.",
                  "It discloses a merge rule that decides where one stretch ends and the next "
                  "begins."),
        "D-383": (VERDICT_IN,
                  "Its verbatim ranks the evidence channels — 'bass/inversion + spelling + "
                  "key-consistency are the primary channels and progression is the tie-break' — "
                  "and re-orders the built resolver so the vertical channels decide. (It reaches "
                  "the candidate list only through an in-word match of `slice` inside "
                  "`isLicensedProgression`, published at its own context field.)",
                  "It states that vertical evidence outranks progression — temporal-context — "
                  "evidence, which is the same subordination the withheld oracle's ranking "
                  "makes."),
        "D-449": (VERDICT_IN,
                  "Its verbatim fixes factor granularity per factor — the bass judged per event "
                  "against the segment's chord, the missing-tone penalty normalized per event of "
                  "segment length, the transition, entry and key-change factors per boundary — "
                  "and names the semi-Markov length bias whose bookkeeping 'alone decided merge "
                  "against split, against the ground truth'.",
                  "It states the machinery that decides where a segment's edges fall and what is "
                  "weighed at a boundary."),
        "D-450": (VERDICT_IN,
                  "Its verbatim rules that the key-signature and declared-mode prior conditions "
                  "the INITIAL key state only, rejects a persistent pull toward the signature, "
                  "and says the initial-state form 'pays the tax once and lets the music govern "
                  "thereafter'.",
                  "It states the notated signature's subordination to the sounding evidence, "
                  "which is the withheld oracle's own ranking between those two evidence "
                  "classes."),
        "D-453": (VERDICT_IN,
                  "Its verbatim is the desk simulation's verdict on the ratified factorization — "
                  "nine of ten traces pass and no finding reopens the structure — and its plain "
                  "names the tenth as the trace that exposed 'how finely each term is counted'.",
                  "It is the ratified factorization's own trace verdict and points at the "
                  "granularity finding that decides merge against split."),
        "D-491": (VERDICT_IN,
                  "Its verbatim states, measured across bands of the vertical gap, that 'the "
                  "earlier layer's vertical commit is a better predictor of the annotated root "
                  "than the progression re-pick, even where the alternative is its vertical "
                  "equal'.",
                  "It is a measured statement that sounding-note evidence outranks progression — "
                  "temporal-context — evidence, which is the withheld oracle's ranking."),
        "D-545": (VERDICT_IN,
                  "Its verbatim describes the mechanical extraction as 'reading notes and cutting "
                  "them into simultaneities' and calls the project's own equivalent 'our own "
                  "cleaner slicer'.",
                  "It tells a deriving session that a slice IS a simultaneity — the "
                  "sounding-set-constant stretch the ruled answer names."),
        "D-565": (VERDICT_IN,
                  "Its verbatim breaks exact ties by 'fewer segments first; then the earliest "
                  "boundary-tick sequence (lexicographic)', and records the ties as real at eight "
                  "corpus pieces — 'equal-score segmentations differing by one boundary on "
                  "repeated-chord runs'; its home is the factorization document, the oracle's "
                  "second arm.",
                  "It is a rule that decides which of two segmentations is committed — where a "
                  "boundary falls — and it is homed in the oracle's own document."),
        "D-569": (VERDICT_IN,
                  "Ruling 3 of `cowork_rulings_2026_08_22_withheld_family_sitting.md`, ruled by "
                  "the user over an UNPLACED verdict: its verbatim supplies the vocabulary of "
                  "the withheld passage — 'every sounding note in a region', 'eligible for "
                  "harmonic analysis', onset and offset as the note's own edges — without "
                  "stating the rule.",
                  "A deriving session that read it would have the oracle's own terms, and the "
                  "comparison could not distinguish recovery from recall."),
        "D-575": (VERDICT_IN,
                  "Its verbatim rules that the Baroque partial signature is handled by DETECTING "
                  "'the flattened sixth degree pervasive across the sounding weight and "
                  "dominating its natural form' and reinterpreting the written signature one step "
                  "accordingly.",
                  "It states the sounding weight overruling the notated key signature, which is "
                  "the withheld oracle's own ranking between those two evidence classes."),

        # ── UNPLACED — NONE.  The three entries this table carried UNPLACED were ruled by the
        #    user on 2026-08-22, Ruling 3 of
        #    `cowork_rulings_2026_08_22_withheld_family_sitting.md`: D-569 IN, D-457 and D-526
        #    OUT.  Each now stands in its own class here, carrying what was read as its finding
        #    (#12).  The value stays in the vocabulary above because DEFAULT NOTHING governs
        #    every later candidate exactly as before. ──────────────────────────────────────────

        # ── OUT — what each bears on instead ──────────────────────────────────────────────────
        "D-032": (VERDICT_OUT,
                  "Its verbatim is the cross-layer confidence contract: every confidence crossing "
                  "a layer boundary is bounded, class-declared and named to its decision.",
                  "Its 'boundary' is a LAYER boundary; it bears on the confidence contract "
                  "between stages and states neither where a chord's boundary falls nor which "
                  "evidence outranks which."),
        "D-114": (VERDICT_OUT,
                  "Its verbatim rules that on the key axis the decoder commits its "
                  "maximum-a-posteriori path and never abstains, so the abstention counter reads "
                  "zero.",
                  "It bears on the key axis's commitment and the abstain counter; 'segment' "
                  "appears only as the unit a key is named for."),
        "D-207": (VERDICT_OUT,
                  "Its verbatim defines the pedal-point class voice-independently — a tone "
                  "sustained or continuously restruck against changing harmony in any voice, "
                  "sub-labeled bass, internal or inverted.",
                  "It bears on the ornament vocabulary's pedal-point class and which voices it "
                  "reaches."),
        "D-224": (VERDICT_OUT,
                  "Its verbatim gates the legacy joint bass-and-chord scoring on regional "
                  "accumulation — it fires only where a tone carries an onset at the region start "
                  "or distinct metric positions.",
                  "It bears on when the dormant vertical scorer's joint path switches on, not on "
                  "where a region's edges fall."),
        "D-262": (VERDICT_OUT,
                  "Its verbatim rules that the extension increment is chosen by the REQUESTING "
                  "layer at its own natural inference scale and is an efficiency knob only.",
                  "It bears on the bounded-context extension protocol; 'harmony/slice scale' "
                  "appears only as an example of the increment one layer would choose."),
        "D-264": (VERDICT_OUT,
                  "Its verbatim states the equivalence invariant — the result after any sequence "
                  "of extensions must equal a single fresh run over the final loaded span.",
                  "It bears on the bounded-context extension's correctness guard; slices appear "
                  "only as the unit the forward cascade decays over."),
        "D-268": (VERDICT_OUT,
                  "Its verbatim is the confidence contract's five rules of use — a confidence "
                  "attaches to a named decision, is bounded and class-declared at a layer "
                  "boundary, is compared only within one class and frame, keeps its identity, and "
                  "abstention means low confidence in the declared class.",
                  "It bears on the cross-layer confidence contract; 'chord-of-slice' and "
                  "'boundary-strength' appear only as names of decisions a confidence may attach "
                  "to."),
        "D-276": (VERDICT_OUT,
                  "Its verbatim publishes, per key run and scale degree, the sounding duration "
                  "and onset count of every chromatic inflection observed, and rules that no mode "
                  "label is inferred or published anywhere.",
                  "It bears on what the record publishes about modal colour."),
        "D-280": (VERDICT_OUT,
                  "Its verbatim rules that a gate or scoring rule reads structured fields only — "
                  "never a chord-symbol string and never a Roman numeral.",
                  "It bears on the inference/presentation boundary, which is the 'boundary' its "
                  "text names."),
        "D-285": (VERDICT_OUT,
                  "Its verbatim is one line: embellishment is chord-first — segmentation plus a "
                  "non-chord-tone post-process — never a union re-derive or a richer vocabulary.",
                  "It bears on how ornamental tones are handled; it names a segmentation step "
                  "without saying where its boundaries fall or what puts them there."),
        "D-313": (VERDICT_OUT,
                  "Its verbatim rules that a calibration map is monotone or deferred, a "
                  "non-monotone empirical curve being an upstream finding rather than a mapping "
                  "target.",
                  "It bears on confidence calibration; 'combinedBoundary' appears only as the "
                  "name of the curve that was measured."),
        "D-320": (VERDICT_OUT,
                  "Its verbatim reverts the absent-root guard outright and records the measured "
                  "refutation of its premise — an absent root does not mean a wrong reading, "
                  "corpus-wide.",
                  "It bears on chord identity — whether a candidate whose root does not sound may "
                  "win — not on where a boundary falls or which evidence outranks which."),
        "D-327": (VERDICT_OUT,
                  "Its verbatim rules that the root-continuity guard reads the pipeline's "
                  "reconstructed inversion credit rather than a literal sounding-third test.",
                  "It bears on one gate of the dormant vertical scorer and on what that gate's "
                  "test reads."),
        "D-329": (VERDICT_OUT,
                  "Its verbatim rules candidate admission — from a stretch's pitches generate "
                  "every tertian chord they could spell, completeness being the priority because "
                  "a chord never listed can never be chosen.",
                  "It bears on candidate admission for a stretch already cut, not on where the "
                  "cut falls."),
        "D-330": (VERDICT_OUT,
                  "Its verbatim forbids a pooled recompute — membership is judged per slice "
                  "against the prevailing chord, and several slices' pitches are never pooled "
                  "into one bag.",
                  "It bears on non-chord-tone membership and on the prohibition of pooling; it "
                  "presupposes slices without stating where their edges fall."),
        "D-337": (VERDICT_OUT,
                  "Its verbatim makes tonicization the default and requires cadence confirmation "
                  "plus persistence for a modulation, expressed as a change-cost.",
                  "It bears on where one KEY gives way to the next, which is a different unit "
                  "from the chord boundary."),
        "D-338": (VERDICT_OUT,
                  "Its verbatim rules that the function layer selects among the chord layer's "
                  "carried readings and never re-derives a chord from the notes.",
                  "It bears on the function layer's selection discipline."),
        "D-339": (VERDICT_OUT,
                  "Its verbatim states the one confidence-weighted forward-recompute mechanism by "
                  "which decisive later evidence may overturn a confident earlier inference.",
                  "It bears on the architecture-wide override mechanism; 'grain' appears only "
                  "inside 'fine-grain chord override', one named instance of it."),
        "D-341": (VERDICT_OUT,
                  "Its verbatim completes the licensed root-motion set by theory — the ascending "
                  "fifth, the descending second and the diatonic diminished fifth. It reaches the "
                  "candidate list only through an in-word match of `slice` inside "
                  "`isLicensedProgression`, published at its own context field.",
                  "It bears on which root motions count as functional progressions."),
        "D-343": (VERDICT_OUT,
                  "Its verbatim gives the key/mode layer the candidate space and the "
                  "note-evidence model outright and hands the residual forward to be SELECTED "
                  "among its carried alternatives.",
                  "It bears on which layer owns key/mode inference; its 'evidence boundary' is "
                  "the line between two layers."),
        "D-348": (VERDICT_OUT,
                  "Its verbatim measures tonal distance in the change cost as circle-of-fifths "
                  "distance and rules that there is no duration threshold for "
                  "brief-versus-sustained.",
                  "It bears on the key-change cost; slices appear only as the unit an excursion's "
                  "length is felt over."),
        "D-349": (VERDICT_OUT,
                  "Its verbatim defines key/mode confidence as how much better the winning "
                  "sequence is than the best different-key sequence at that stretch.",
                  "It bears on how the key confidence is computed."),
        "D-353": (VERDICT_OUT,
                  "Its verbatim keeps two quality goals apart — accuracy on the resolvable cases, "
                  "and calibration of the uncertain mark.",
                  "It bears on how the key/mode layer is graded."),
        "D-376": (VERDICT_OUT,
                  "Its verbatim chooses a bounded coupling over the two existing decoders and "
                  "rejects the unified single-state alternative, on three named constraints.",
                  "It bears on the shape of the key-and-chord coupling, since shelved; it names "
                  "no segmentation and no evidence ranking."),
        "D-380": (VERDICT_OUT,
                  "Its verbatim rules that the carry's meaningful axis is DISTINCT ROOTS and that "
                  "every above-threshold root is carried at its graded confidence.",
                  "It bears on what the chord layer hands forward; slices appear only as the "
                  "population a measured share is taken over."),
        "D-382": (VERDICT_OUT,
                  "Its verbatim rules that selection is by JOINT CONSISTENCY across key, root, "
                  "inversion and bass rather than by maximizing any one candidate score.",
                  "It bears on the function layer's selection objective."),
        "D-386": (VERDICT_OUT,
                  "Its verbatim rules that the pedal reader adds no fourth hand-rolled scan and "
                  "consumes the carry's own distinct-root margin.",
                  "It bears on where the pedal reader takes its confirmation margin from."),
        "D-387": (VERDICT_OUT,
                  "Its verbatim unifies the function-context contradiction onto the ONE open "
                  "mark, enriched with its reason, rather than a second parallel flag.",
                  "It bears on how a contradiction between the function context and a committed "
                  "chord is surfaced."),
        "D-392": (VERDICT_OUT,
                  "Its verbatim keeps the later voice-leading components as claims with owners, "
                  "each clearing its own design and evidence before an instruction exists.",
                  "It bears on the voice-leading dimension's build sequencing; 'phrase "
                  "segmentation' appears only as one named component."),
        "D-394": (VERDICT_OUT,
                  "Its verbatim makes reduction of a chordal voice to one line a declared, "
                  "uniform, per-query parameter, with top-note the one rule the first version "
                  "offers.",
                  "It bears on the voice-leading dimension's reduction rule."),
        "D-400": (VERDICT_OUT,
                  "Its verbatim admits a PER-VOICE span kind to the typology, because melodic "
                  "phrases overlap across voices by construction and tile only within one voice.",
                  "It bears on the span typology and the phrase span's tiling law; the tiling "
                  "remark is the contrast the new kind is admitted against."),
        "D-425": (VERDICT_OUT,
                  "Its verbatim rules that the uncertainty surface's contract IS the full "
                  "posterior, with the narrower local form the first delivered step.",
                  "It bears on what the analysis publishes about its own uncertainty."),
        "D-454": (VERDICT_OUT,
                  "Its verbatim rules that the grouping layer defines no detection of its own and "
                  "assembles what earlier layers decided.",
                  "It bears on the grouping layer's scope."),
        "D-455": (VERDICT_OUT,
                  "Its verbatim rules that a cadence away from a grouping boundary is surfaced as "
                  "internal, never snapped to the nearest boundary and never discarded.",
                  "It bears on cadence alignment to punctuation spans — a different span kind."),
        "D-457": (VERDICT_OUT,
                  "Read: its verbatim's subject is the grouping layer's edge marking — "
                  "'clipped-by-selection-edge' on a group or key area truncated by the selection "
                  "edge, and an 'extension-cue' tag where a span reaches the edge with no closing "
                  "boundary and no cadence — and it cites, in a parenthesis, 'L2's "
                  "artificial-clip-boundary distinction'.",
                  "The grouping layer's marking of a group or key area truncated by the selection "
                  "edge; it discloses that the slicer distinguishes an artificial clip boundary "
                  "from a musical one — the existence of a distinction, not its rule (Ruling 3 of "
                  "the withheld-family sitting)."),
        "D-459": (VERDICT_OUT,
                  "Its verbatim declares the key-area confidence a Class-M boundary confidence "
                  "whose input is the declared key confidence rather than the grading "
                  "diagnostics' sigmoid.",
                  "It bears on the grouping layer's published key-area confidence."),
        "D-463": (VERDICT_OUT,
                  "Its verbatim leaves the temporal signals sitting inside the vertical scorer "
                  "where they are and requires the gate that depends on one to move with them.",
                  "It bears on a known structural debt in the dormant vertical scorer and on that "
                  "gate's coupling; it ranks no evidence class against another and locates no "
                  "boundary."),
        "D-464": (VERDICT_OUT,
                  "Its verbatim bars any further progression-level signal from the single-step "
                  "look-around structure.",
                  "It bears on which structure carries progression-level signals."),
        "D-474": (VERDICT_OUT,
                  "Its verbatim records the FACT-of-absence: no published study reports per-axis "
                  "inter-annotator agreement for this repertoire.",
                  "It bears on the ground-truth ceiling; it reaches the candidate list only "
                  "through an in-word match of `release` inside 'released'."),
        "D-476": (VERDICT_OUT,
                  "Its verbatim gives the phrase-boundary primitive to the notation-derived view "
                  "layer and rejects the note model and the function layer as owners.",
                  "It bears on the PHRASE boundary — a different span kind — and on its owner."),
        "D-477": (VERDICT_OUT,
                  "Its verbatim rules phrase boundaries read from the written surface alone, "
                  "never from a resolved key, chord or cadence, and accepts the boundaries this "
                  "misses.",
                  "It bears on the phrase-boundary primitive's inputs — a different span kind, "
                  "and its exclusion of harmonic evidence is the opposite question."),
        "D-478": (VERDICT_OUT,
                  "Its verbatim makes a phrase boundary a peak in a continuous strength profile "
                  "rather than the OR of a few binary signals.",
                  "It bears on the phrase-boundary model."),
        "D-479": (VERDICT_OUT,
                  "Its verbatim runs the boundary cues per eligible voice and aggregates them by "
                  "voice-coincidence, publishing both the per-voice and the texture boundaries.",
                  "It bears on the phrase-boundary primitive's scope."),
        "D-480": (VERDICT_OUT,
                  "Its verbatim rules the phrase-boundary primitive not an accuracy requirement "
                  "and requires it built right but kept proportionate.",
                  "It bears on the phrase-boundary primitive's proportionality."),
        "D-481": (VERDICT_OUT,
                  "Its verbatim emits the notated markers as boundaries unconditionally and "
                  "peak-picks only the surface-cue strength.",
                  "It bears on the phrase-boundary picking rule."),
        "D-484": (VERDICT_OUT,
                  "Its verbatim makes the phrase-boundary primitive a derived view that inherits "
                  "the loaded span, requests no extension of its own, and publishes a per-profile "
                  "max-normalised confidence.",
                  "It bears on the phrase-boundary primitive's context obligation and confidence "
                  "class."),
        "D-485": (VERDICT_OUT,
                  "Its verbatim requires every picked boundary to carry which cue fired and at "
                  "what scope, and records the picked set as scope-blind today.",
                  "It bears on the phrase-boundary primitive's owed provenance."),
        "D-490": (VERDICT_OUT,
                  "Its verbatim falsifies the fine-grain function override: the harm rate is "
                  "unrelated to both quantities its trigger is built from.",
                  "It bears on that override's viability; 'grain' appears only inside "
                  "'fine-grain'."),
        "D-495": (VERDICT_OUT,
                  "Its verbatim requires a stated fallback where the phrase-boundary profile is "
                  "featureless — relax cadence admission and scale the vote weight down rather "
                  "than starve.",
                  "It bears on cadence admission against the phrase-boundary profile."),
        "D-526": (VERDICT_OUT,
                  "Read: its verbatim's subject is the joint state's chord axis being "
                  "scale-degree-valued, and among the tonic/degree coupling terms it says "
                  "dissolve by construction it names 'the segmenter's head-gap tonic prior — the "
                  "gap map's group 1'.",
                  "The chord axis's representation as a scale degree; it names a segmenter prior "
                  "at the head of a gap in order to say it dissolves — the existence of a prior, "
                  "not a rule (Ruling 3 of the withheld-family sitting)."),
        "D-527": (VERDICT_OUT,
                  "Its verbatim rules that no live non-chord-tone cleaning stage exists — each "
                  "tone is emitted by category inside the one decode, conditioned on "
                  "chord-independent melodic and metric covariates, with ornament labels derived "
                  "after it.",
                  "It bears on the emission factor and on ornament labelling; it ranks no "
                  "evidence class and locates no boundary."),
        "D-531": (VERDICT_OUT,
                  "Its verbatim confirms the hand-built analysis and does not trigger the learned "
                  "replacement, retaining it behind the interface as an explicit fallback.",
                  "It bears on whether the scorer is replaced by a trained model."),
        "D-534": (VERDICT_OUT,
                  "Its verbatim counts the missing-tone penalty PER CHORD FACTOR from the "
                  "labelled corpus rather than carrying one invented blanket value.",
                  "It bears on the missing-tone penalty's values; 'segment' appears as the ground "
                  "truth's own labelled unit."),
        "D-536": (VERDICT_OUT,
                  "Its verbatim makes the winner a (bass, root, template) triple, replacing the "
                  "order in which the bass was committed before any chord was scored.",
                  "It bears on the dormant vertical scorer's internal ordering."),
        "D-584": (VERDICT_OUT,
                  "Its verbatim decides the perfect/imperfect cadence call on the bass-derived "
                  "inversion and demotes the soprano arrival degree to a soft optional nudge.",
                  "It bears on cadence typing and on why the structural melody is unavailable to "
                  "this layer."),
        "D-589": (VERDICT_OUT,
                  "Its verbatim makes every idiom mixture selectable and the discovered cloud the "
                  "EVIDENCE MAP rather than the boundary, each chosen point carrying its evidence "
                  "status.",
                  "It bears on the style system; its 'boundary' is the edge of the measured idiom "
                  "cloud."),
        "D-605": (VERDICT_OUT,
                  "Its verbatim rules that a local-key hypothesis derives from key-agnostic "
                  "signals ONLY and never from the key-area grouping, on a stated circularity "
                  "ground.",
                  "It reaches the candidate list as the sole group-E entry, but its subject is "
                  "what evidence a MODULATION decision may read — the key axis's circularity "
                  "guard — and not the chord boundary."),
        "D-613": (VERDICT_OUT,
                  "Its verbatim records implied-polyphony ground truth CONFIRMED ABSENT and "
                  "closes the search.",
                  "It bears on corpus availability for voice and stream separation; it reaches "
                  "the candidate list only through an in-word match of `release` inside "
                  "'released'."),
        "D-623": (VERDICT_OUT,
                  "Its verbatim makes a selection-aware capability a PARAMETER on the one "
                  "orchestrator rather than a second driver beside it.",
                  "It bears on orchestration — that one path builds, slices and decodes — not on "
                  "where a slice's edges fall."),
    },

    # The sizing subject's criterion is empty by ruling, so the derivation returns no candidate and
    # there is nothing to grade. The empty table is authored rather than left absent so that the
    # emptiness is visible here, where a reader looks for a subject's verdicts.
    "scoring-model": {},
}


# ── file helpers ──────────────────────────────────────────────────────────────────────────────
def read_text(rel: str) -> str:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise Stop(f"member source {rel} is not in the tree")
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def read_json(path: str):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def locate(lines: list[str], anchor: str, what: str) -> int:
    """The 0-based index of the ONE line carrying `anchor`. Not exactly one is a STOP."""
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    if len(hits) != 1:
        raise Stop(f"{what}: the anchor {anchor!r} matches {len(hits)} lines, not exactly one")
    return hits[0]


def span_lines(rel: str, spec: dict) -> tuple[list[str], dict]:
    """One authored span of one file, taken by anchor. Returns the lines and its own record."""
    text = read_text(rel)
    lines = text.split("\n")
    kind = spec["kind"]
    if kind == "whole":
        body, rec = lines, {"kind": kind, "taken": "the whole file"}
    elif kind == "heading-to-heading":
        a = locate(lines, spec["start"], f"{rel}: the span's opening")
        b = locate(lines, spec["end"], f"{rel}: the span's closing")
        if b <= a:
            raise Stop(f"{rel}: the closing anchor precedes the opening one")
        body = lines[a:b]
        rec = {"kind": kind, "opens_at": spec["start"], "closes_before": spec["end"]}
    elif kind == "heading-to-paragraph":
        a = locate(lines, spec["start"], f"{rel}: the span's opening")
        p = locate(lines, spec["end"], f"{rel}: the closing paragraph's opening")
        if p < a:
            raise Stop(f"{rel}: the closing paragraph precedes the opening anchor")
        end = p
        while end + 1 < len(lines) and lines[end + 1].strip():
            end += 1
        body = lines[a:end + 1]
        rec = {"kind": kind, "opens_at": spec["start"],
               "closes_at_the_end_of_the_paragraph_opening": spec["end"]}
    elif kind == "heading-to-eof":
        a = locate(lines, spec["start"], f"{rel}: the span's opening")
        body = lines[a:]
        rec = {"kind": kind, "opens_at": spec["start"], "closes_at": "the end of the file"}
    else:
        raise Stop(f"{rel}: span kind {kind!r} is not one this tool renders")
    while body and not body[-1].strip():
        body.pop()
    rec["lines_rendered"] = len(body)
    return body, rec


# ── the withheld passage: located by its own text, never by line number ───────────────────────
_WS = re.compile(r"\s+")


def _normalize(text: str) -> tuple[str, list[int]]:
    """Collapse whitespace runs to one space, keeping a map back to original offsets."""
    out, idx, i, n = [], [], 0, len(text)
    while i < n:
        ch = text[i]
        if ch.isspace():
            j = i
            while j < n and text[j].isspace():
                j += 1
            out.append(" ")
            idx.append(i)
            i = j
        else:
            out.append(ch)
            idx.append(i)
            i += 1
    idx.append(n)
    return "".join(out), idx


def _find_once(hay_norm: str, needle: str, what: str) -> int:
    needle = _WS.sub(" ", needle).strip()
    hits, at = [], hay_norm.find(needle)
    while at != -1:
        hits.append(at)
        at = hay_norm.find(needle, at + 1)
    if len(hits) != 1:
        raise Stop(f"{what}: the anchor {needle!r} matches {len(hits)} places, not exactly one")
    return hits[0]


def withhold_passage(text: str, passage: dict, marker: str) -> tuple[str, dict]:
    """Cut ONE authored passage out of a rendered span, marking the omission in place."""
    lines = text.split("\n")
    s = locate(lines, passage["scope_anchor"], "the withheld passage's scope")
    e = s + 1
    while e < len(lines) and not lines[e].startswith("- "):
        e += 1
    scope = "\n".join(lines[s:e])
    scope_start = sum(len(ln) + 1 for ln in lines[:s])

    norm, idx = _normalize(scope)
    o = _find_once(norm, passage["opens"], "the withheld passage's opening")
    c = _find_once(norm, passage["closes"], "the withheld passage's closing")
    if c < o:
        raise Stop("the withheld passage's closing anchor precedes its opening")
    close_end = c + len(_WS.sub(" ", passage["closes"]).strip())
    a_orig, b_orig = idx[o], idx[close_end] if close_end < len(idx) else len(scope)

    cut = scope[a_orig:b_orig]
    new_scope = scope[:a_orig] + "\n\n  " + marker + "\n\n  " + scope[b_orig:].lstrip()
    out = text[:scope_start] + new_scope + text[scope_start + len(scope):]
    return out, {
        "file": passage["file"],
        "member": passage["member"],
        "scope_anchor": passage["scope_anchor"],
        "opens": passage["opens"],
        "closes": passage["closes"],
        "the_text_matched": cut,
        "characters_omitted": len(cut),
        "marked_in_place_with": marker,
        "finding": passage["finding"],
        "date": passage["date"],
        "reason": passage["reason"],
    }


# ── the candidate derivation ──────────────────────────────────────────────────────────────────
HOME_LINES = re.compile(r"^([^\s:]+\.md):(\d+)(?:-(\d+))?")


def architecture_spans(spec) -> list[dict]:
    """The `ARCHITECTURE.md` line ranges the criterion names, LOCATED BY TEXT on every run."""
    lines = read_text("ARCHITECTURE.md").split("\n")
    found = []
    for s in spec:
        a = locate(lines, s["anchor"], f"ARCHITECTURE.md: {s['name']}")
        if s["kind"] == "paragraph":
            b = a
            while b + 1 < len(lines) and lines[b + 1].strip():
                b += 1
        elif s["kind"] == "table":
            b = a
            while b + 1 < len(lines) and lines[b + 1].startswith("|"):
                b += 1
            while a - 1 >= 0 and lines[a - 1].startswith("|"):
                a -= 1
        else:
            raise Stop(f"{s['name']}: span kind {s['kind']!r} is not one this tool locates")
        found.append({"name": s["name"], "located_by": s["anchor"],
                      "first_line": a + 1, "last_line": b + 1})
    return found


def haystack(entry: dict, backbone: dict, fields: tuple[str, ...]) -> dict:
    out = {}
    for f in fields:
        v = backbone.get(f) if f in backbone else entry.get(f)
        if isinstance(v, list):
            v = " ".join(str(x) for x in v)
        out[f] = v or ""
    return out


def candidates(subject: str, design_intent: list[dict], backbone: dict) -> list[dict]:
    spec = CRITERION[subject]
    arch = architecture_spans(spec["architecture_spans"])
    found = []
    for e in design_intent:
        eid = e["id"]
        bb = backbone.get(eid, {})
        why = []
        if e.get("group") in spec["groups"]:
            why.append({"criterion": "group", "matched": e.get("group"),
                        "means": "Layer 2 — the slicer"})
        home = (e.get("home") or "")
        for doc in spec["home_documents"]:
            if home.startswith(doc):
                why.append({"criterion": "home-document", "matched": doc, "means": home})
        m = HOME_LINES.match(home)
        if m and m.group(1) == "ARCHITECTURE.md":
            lo = int(m.group(2))
            hi = int(m.group(3)) if m.group(3) else lo
            for s in arch:
                if lo <= s["last_line"] and hi >= s["first_line"]:
                    why.append({"criterion": "home-inside-an-oracle-span",
                                "matched": s["name"], "means": home})
        fields = haystack(e, bb, ("title", "verbatim", "plain", "patterns"))
        for field, value in fields.items():
            low = value.lower()
            for kw in spec["keywords"]:
                at = low.find(kw)
                if at != -1:
                    # The matched text in its own context, so a reader can see WHY the pattern
                    # fired rather than taking this tool's word for it — a keyword can match
                    # inside a longer word, and a match a reader cannot see is a match nobody
                    # can challenge.
                    lo, hi = max(0, at - 45), min(len(value), at + len(kw) + 45)
                    why.append({"criterion": "keyword", "matched": kw,
                                "means": f"in `{field}`",
                                "in_context": ("…" if lo else "") + value[lo:hi].replace("\n", " ")
                                             + ("…" if hi < len(value) else "")})
        if eid in spec["always"]:
            why.append({"criterion": "named-by-the-ruling", "matched": eid,
                        "means": "amendment (a1) names it as the first withheld identity"})
        if why:
            found.append({
                "id": eid,
                "group": e.get("group"),
                "title": e.get("title"),
                # The entry's OWN words, carried beside the verdict so that every verdict is
                # checkable at the text it was made from rather than at this tool's account of it.
                # This is the MANIFEST, not the pack: the pack directory is what a deriving session
                # opens, and its read-me forbids opening anything outside it.
                "verbatim": bb.get("verbatim", ""),
                "plain": bb.get("plain", ""),
                "matched_by": why,
            })
    found.sort(key=lambda r: (int(r["id"].split("-")[1]), r["id"]))
    return found


def criterion_is_empty(spec: dict) -> bool:
    """True where the authored criterion carries NO term at all.

    DERIVED FROM THE AUTHORED ENTRY AND NEVER SWITCHED ON A SUBJECT NAME, which is the condition
    the licence for this rendering states in terms.  A subject whose withheld family is empty by
    ruling authors no criterion — every term of its entry is empty — so this test recognizes the
    state rather than recognizing the subject, and a later subject in the same state renders the
    same way without a line being touched.
    """
    return not any(spec[term] for term in
                   ("groups", "home_documents", "architecture_spans", "keywords", "always"))


def criterion_block(subject: str) -> tuple[str, dict]:
    """The manifest's bound paragraph and its candidate-criterion block, for one subject.

    LICENSED by Ruling 2(a) of `cowork_rulings_2026_08_24_sizing_leak_list_sitting.md`, quoted
    verbatim: *"the manifest's candidate-criterion block renders truthfully for a subject whose
    criterion is EMPTY BY RULING -- stating that no search was run because the ruling empties the
    family, rather than describing a pattern match that never ran; derived from the authored
    entry, not switched on a subject name, with the harmony-boundary subject block required to
    re-render BYTE-UNCHANGED as the proof"*.

    Before it, both were written for a criterion that runs a pattern match over the register's own
    text: a subject with no criterion at all published five conditional bullets describing that
    match, and a bound paragraph disclaiming ITS unmeasured reach -- so a generated artifact read
    as though a search had been run and returned nothing.  The disclaimer belongs to the non-empty
    case alone, which is where it is now rendered.

    The NON-EMPTY branch is byte-for-byte what this tool published before the correction.
    """
    spec = CRITERION[subject]
    spans = architecture_spans(spec["architecture_spans"])
    terms = {
        "the_oracle_spans_located_by_text_on_every_run": spans,
        "the_keywords": list(spec["keywords"]),
        "the_groups": list(spec["groups"]),
        "the_home_documents": list(spec["home_documents"]),
        "named_by_the_ruling": list(spec["always"]),
    }
    if criterion_is_empty(spec):
        return (
            "NO CANDIDATE SEARCH WAS RUN FOR THIS SUBJECT, and no criterion is authored for it. "
            "Its withheld family is EMPTY BY RULING — no withheld identities, no withheld "
            "documents, no withheld passages — so there is nothing for a candidate search to "
            "find. The empty candidate list and the empty verdict table below are a CONSEQUENCE "
            "OF THAT RULING and NOT the result of a pattern match that returned nothing.",
            {
                "★_there_is_no_criterion_here_and_nothing_was_searched": (
                    "Every term below is empty because none was authored, the withheld family "
                    "being empty by ruling. Read no reach and no coverage into them: this tool "
                    "made no attempt to find a candidate for this subject, so their emptiness "
                    "says nothing about what the record holds on it."),
                **terms,
            },
        )
    return (
        "The candidate criterion is a PATTERN MATCH over the rulings sort and the decisions "
        "register's own text. ITS REACH IS UNMEASURED (#19): an entry that bears on this "
        "subject in words none of the criterion's terms carry would not appear here, and an "
        "empty match would be evidence of nothing. The bound is stated rather than a "
        "detection measurement being owed, under D-673, and the test that clause fixes is "
        "met: NO ANALYSIS DECISION CONSUMES THIS ENUMERATION — the user rules it at the "
        "reading file this dispatch delivers.",
        {
            "a candidate is every DESIGN-INTENT entry meeting ANY of": [
                "its `group` is E — Layer 2, the slicer",
                "its `home` document is one of the withheld-document candidates",
                "its `home` is `ARCHITECTURE.md` at a line inside one of the oracle spans below",
                "any of `title`, `verbatim`, `plain`, `patterns` contains one of the keywords",
                "it is an identity the ruling names",
            ],
            **terms,
        },
    )


def cross_reference_additions(authored: set[str], docs: set[str],
                              design_intent: list[dict], backbone: dict) -> list[dict]:
    """Every DESIGN-INTENT entry that quotes or cross-references a withheld identity or document."""
    adds = []
    for e in design_intent:
        eid = e["id"]
        if eid in authored:
            continue
        bb = backbone.get(eid, {})
        fields = haystack(e, bb, ("title", "verbatim", "plain", "rationale", "status_source"))
        hits = []
        for field, value in fields.items():
            for other in sorted(authored):
                if other in value:
                    hits.append({"field": field, "matched": other})
            for doc in sorted(docs):
                if doc in value:
                    hits.append({"field": field, "matched": doc})
        if hits:
            adds.append({"id": eid, "title": e.get("title"), "derived_because": hits})
    adds.sort(key=lambda r: (int(r["id"].split("-")[1]), r["id"]))
    return adds


# ── the leak check, scoped to members (5) and (6) ─────────────────────────────────────────────
PATH_LIKE = re.compile(r"\b(?:docs|src)/[A-Za-z0-9_./+-]+")


def leak_strings(withheld_ids: set[str], docs: set[str]) -> list[tuple[str, str]]:
    out = [("withheld-identity", i) for i in sorted(withheld_ids)]
    out += [("withheld-document", d) for d in sorted(docs)]
    out.append(("the-implementation's-own-specification", "ARCHITECTURE.md"))
    return out


def leaks_in(fields: dict, strings: list[tuple[str, str]]) -> list[dict]:
    hits = []
    for field, value in fields.items():
        if not value:
            continue
        for kind, s in strings:
            if s in value:
                hits.append({"field": field, "kind": kind, "matched": s})
        for m in PATH_LIKE.finditer(value):
            hits.append({"field": field, "kind": "a-docs-or-src-path", "matched": m.group(0)})
    return hits


# ── rendering ─────────────────────────────────────────────────────────────────────────────────
def fence_for(text: str) -> str:
    n = 3
    while ("`" * n) in text:
        n += 1
    return "`" * n


def render_design_intent(subject: str, admitted: list[dict]) -> str:
    out = [
        "# The ratified design intent — the entries this pack admits for this subject",
        "",
        "This file is GENERATED. It carries the entries of the `DESIGN-INTENT` class of the "
        "rulings sort — the decisions the record sorts as ruled design intent rather than as "
        "management of the implementation — LESS the family withheld for this subject.",
        "",
        "Four fields per entry and no others: the identifier, the title, the decision in the "
        "words it was decided in, and its plain restatement. Where a decision is recorded, what "
        "defends it, what its status came from and the words a search finds it by are all "
        "deliberately absent: each of those names a place or a fact in the implementation's own "
        "documents, which this pack does not carry.",
        "",
        "Entries are in identifier order. An identifier missing from the run is not an error and "
        "is not a gap in the record: it is either outside this class or withheld for this "
        "subject, and this pack does not say which.",
        "",
        "---",
        "",
    ]
    for e in admitted:
        out.append(f"## {e['id']} — {e['title']}")
        out.append("")
        out.append("**As decided, in the words it was decided in:**")
        out.append("")
        v = e["verbatim"] or ""
        f = fence_for(v)
        out += [f, v, f, ""]
        out.append(f"**In plain words:** {e['plain']}")
        out += ["", "---", ""]
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out) + "\n"


def render_defect_types(rows: list[list[str]], header: list[str]) -> str:
    out = [
        "# The defect types — the named shapes of reasoning error",
        "",
        "This file is GENERATED. It carries the catalog's TYPE and DEFINITION columns and nothing "
        "else: the founding-instance and detection-signature columns are descriptions of this "
        "project's implementation and are excluded from this pack by the ruling that admits the "
        "catalog.",
        "",
        "These are the shapes a derivation must not walk into. They are named here so that a "
        "session can check its own work against them by name.",
        "",
        "| " + " | ".join(header) + " |",
        "|" + "|".join(["---"] * len(header)) + "|",
    ]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def render_what_was_cut(withheld_entries: int, passages: list[dict]) -> str:
    """The read-me's what-was-cut section, DERIVED from what was actually withheld.

    LICENSED ACCOMMODATION (ii) of §4(1) of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`,
    quoted verbatim: *"the read-me's what-was-cut section renders truthfully for a subject with no
    withheld entries and no withheld passages"*.  Before it, the two-kinds lead-in and the
    entries bullet were HARDCODED, so a subject withholding nothing would have told its session
    that material had been withheld from it and that there were `0 passages` — the zero-passage
    bound the record declared twice.

    IT IS DERIVED FROM THE COUNTS AND NOT SWITCHED ON A SUBJECT NAME, so it is true at any future
    subject; and the two-kinds state re-renders BYTE-IDENTICALLY, which is what shows the
    rendering derived rather than duplicated (#6).
    """
    member_two = MEMBERS[1]["filename"]
    kinds: list[str] = []
    if withheld_entries:
        kinds.append("entries of the design-intent file that were not rendered — you will see "
                     "identifier gaps, and\n  those gaps are **not** evidence of anything")
    n = len(passages)
    if n == 1:
        kinds.append(f"one passage inside `{member_two}`, marked in place where it was removed")
    elif n > 1:
        kinds.append(f"{n} passages inside `{member_two}`, each marked in place where it was "
                     f"removed")

    head = "## What has been cut out of this pack, and why you are told"
    tail = ("**Do not try to reconstruct any of it, and do not treat a gap as a hint.** Derive the "
            "unit from the\ndomain and from what this pack does carry.")

    if not kinds:
        return f"""{head}

**Nothing has been withheld from this pack for this subject.** No register entry and no passage
was held back: this unit is not held out against a ruled answer you have not read.

What the design-intent file does not carry is the entries a standing check removed for a
different reason — an entry whose own rendered words name a path into this project's own
implementation documents. You will see identifier gaps where that happened, and those gaps are
**not** evidence of anything.

{tail}"""

    lead = "One kind:" if len(kinds) == 1 else "Two kinds:"
    bullets = "\n".join("* " + k + (";" if i < len(kinds) - 1 else ".")
                        for i, k in enumerate(kinds))
    return f"""{head}

Material has been withheld from this pack **for this subject**, so that what you derive can be
compared against a ruled answer you have not read. {lead}

{bullets}

{tail}"""


def render_read_me(subject: str, subject_words: str, passages: list[dict],
                   withheld_entries: int) -> str:
    names = [READ_ME] + [m["filename"] for m in MEMBERS]
    listing = "\n".join(
        [f"{i + 1}. `{m['filename']}` — {m['title']}" for i, m in enumerate(MEMBERS)])
    what_was_cut = render_what_was_cut(withheld_entries, passages)
    return f"""# READ THIS FIRST — the whole of what this session opens

You are an **implementation-blind deriving session**. Your work is to write what the analysis
**should** do for one unit, from the domain and from the ruled design intent — **not** to describe
what any existing code or specification says it currently **does**.

**The unit for this session is: {subject_words}**

## The six files of this pack, in order

{listing}

Read them in that order. Together with this file they are **the whole of your read within this
repository**, apart from the brief that dispatched you and what the boundary below admits.

## The boundary, stated once and binding

**This directory replaces the ordinary session-start read for you.** `cowork_handoff.md`,
`STATUS.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `docs/scoring_model.md`, the open-items register
and its derived gating answer, and every `cc_*` and `cowork_*` file outside this directory — the
brief that dispatched you excepted — are **NOT opened**. No branch rule is taken. What you may
read beyond this directory — your brief, score and analysis files your brief stages to you by
name, and published research — is stated by your brief, and by nothing in this directory.

**If you nonetheless meet a statement about how THIS project's analysis currently works — in any
file, including one of these six — STOP READING THAT FILE AT THAT POINT and record WHERE you were
and HOW MUCH you had seen.** That record is part of your output. It is not a failure; an unrecorded
one is.

{what_was_cut}

## What your output is

A specification of the unit named above, in the six-field form the writing standards and the phase
definitions in this pack describe, plus your source declaration — which files you actually
consulted — and any stop-and-record notes from the clause above.
"""


# ── the build ─────────────────────────────────────────────────────────────────────────────────
def build_subject(subject: str, sort_entries: list[dict], backbone: dict) -> tuple[dict, dict]:
    """Returns (the subject's manifest record, {relative filename: rendered text})."""
    if subject not in WITHHELD:
        raise Stop(f"no authored WITHHELD table for subject {subject!r}")
    if subject not in CRITERION:
        raise Stop(f"no authored candidate criterion for subject {subject!r}")
    authored = WITHHELD[subject]
    design_intent = [e for e in sort_entries if e.get("proposed_class") == "DESIGN-INTENT"]
    di_ids = {e["id"] for e in design_intent}

    # ── the candidates ────────────────────────────────────────────────────────────────────────
    cands = candidates(subject, design_intent, backbone)
    cand_ids = [c["id"] for c in cands]

    # ── STOP 4/5: every candidate carries exactly one verdict, and no verdict outlives one ────
    graded = VERDICTS.get(subject, {})
    missing = [c for c in cand_ids if c not in graded]
    if missing:
        rows = "\n".join(
            f"    {c['id']:<7} {c['title']}\n"
            f"            VERBATIM: {c['verbatim']}\n"
            f"            PLAIN:    {c['plain']}\n"
            f"            matched by: "
            + "; ".join(f"{w['criterion']}={w['matched']} ({w['means']})"
                        + (f" <<{w['in_context']}>>" if w.get("in_context") else "")
                        for w in c["matched_by"])
            for c in cands if c["id"] in missing)
        raise Stop(f"{len(missing)} derived candidate(s) carry no authored verdict — a candidate "
                   f"cannot be graded by silence:\n{rows}")
    orphan = sorted(set(graded) - set(cand_ids))
    if orphan:
        raise Stop(f"verdict(s) for entries the derivation does not return as candidates: {orphan}")
    bad = sorted({v[0] for v in graded.values()} - set(VERDICTS_VOCABULARY))
    if bad:
        raise Stop(f"verdict(s) outside the closed three-value vocabulary: {bad}")
    for cid, v in sorted(graded.items()):
        if len(v) != 3 or not all(str(x).strip() for x in v):
            raise Stop(f"the verdict for {cid} lacks its verdict, its finding or its reason")

    verdict_rows = []
    for c in cands:
        vd, finding, reason = graded[c["id"]]
        verdict_rows.append({**c, "verdict": vd, "finding": finding,
                            "date": DATE, "reason": reason})
    counted = {v: sum(1 for r in verdict_rows if r["verdict"] == v)
               for v in VERDICTS_VOCABULARY}
    if sum(counted.values()) != len(cands):
        raise Stop(f"the verdicts ({sum(counted.values())}) do not account for the candidate "
                   f"population ({len(cands)})")

    # ── the authored withheld identities: every IN verdict, plus the ruling's own ─────────────
    authored_ids = {r["id"] for r in verdict_rows if r["verdict"] == VERDICT_IN}
    named = authored.get("the_identity_the_ruling_names")
    if named and named not in authored_ids:
        raise Stop(f"amendment (a1) names {named} as a withheld identity for this subject and the "
                   f"authored verdicts do not carry it IN")
    # STOP 2 and STOP 6.
    outside = sorted(authored_ids - di_ids)
    if outside:
        raise Stop(f"withheld identity/identities not in the DESIGN-INTENT class: {outside}")
    not_a_candidate = sorted(authored_ids - set(cand_ids))
    if not_a_candidate:
        raise Stop(f"withheld identity/identities nobody derived as a candidate: {not_a_candidate}")

    # ── STOP 3: every authored withholding record carries its three fields ────────────────────
    for doc, rec in sorted(authored.get("withheld_documents", {}).items()):
        for f in ("finding", "date", "reason"):
            if not rec.get(f):
                raise Stop(f"the withholding of {doc} lacks its {f} and does not reach the "
                           f"derivation (amended #10)")
    for p in authored.get("withheld_passages", []):
        for f in ("finding", "date", "reason", "opens", "closes", "scope_anchor", "file"):
            if not p.get(f):
                raise Stop(f"a withheld passage of {p.get('file')} lacks its {f}")

    docs = set(authored.get("withheld_documents", {}))

    # ── the derived cross-reference additions ────────────────────────────────────────────────
    adds = cross_reference_additions(authored_ids, docs, design_intent, backbone)
    withheld_ids = authored_ids | {a["id"] for a in adds}

    # ── member (5): the cut, then the leak check ─────────────────────────────────────────────
    strings = leak_strings(withheld_ids, docs)
    admitted, leaks = [], []
    for e in design_intent:
        eid = e["id"]
        if eid in withheld_ids:
            continue
        bb = backbone.get(eid)
        if bb is None:
            raise Stop(f"{eid} is in the DESIGN-INTENT class and not in the register's data file")
        rendered = {"id": eid, "title": bb.get("title", ""),
                    "verbatim": bb.get("verbatim", ""), "plain": bb.get("plain", "")}
        hit = leaks_in(rendered, strings)
        if hit:
            leaks.append({"member": 5, "id": eid, "title": rendered["title"], "matched": hit})
        else:
            admitted.append(rendered)
    admitted.sort(key=lambda r: (int(r["id"].split("-")[1]), r["id"]))

    # ── member (6): the two admitted columns, then the same leak check ───────────────────────
    dt_lines = read_text("DEFECT_TYPES.md").split("\n")
    h = locate(dt_lines, DEFECT_TABLE_HEADER, "DEFECT_TYPES.md: the catalog table's header")
    header = [c.strip() for c in dt_lines[h].strip().strip("|").split("|")][:DEFECT_COLUMNS_KEPT]
    dt_rows, i = [], h + 2
    while i < len(dt_lines) and dt_lines[i].startswith("|"):
        cells = [c.strip() for c in dt_lines[i].strip().strip("|").split("|")]
        row = cells[:DEFECT_COLUMNS_KEPT]
        fields = {header[k]: row[k] for k in range(len(row))}
        hit = leaks_in(fields, strings)
        if hit:
            leaks.append({"member": 6, "id": row[0], "title": row[1] if len(row) > 1 else "",
                          "matched": hit})
        else:
            dt_rows.append(row)
        i += 1
    if not dt_rows:
        raise Stop("DEFECT_TYPES.md: the catalog table rendered no rows")

    # ── render every member ──────────────────────────────────────────────────────────────────
    files: dict[str, str] = {}
    member_records = []
    passages_applied = []
    for m in MEMBERS:
        rec = {"member": m["number"], "file": m["filename"], "title": m["title"],
               "source": m["source"], "rendered_from": m["rendered_from"]}
        if m["number"] == 5:
            text = render_design_intent(subject, admitted)
            rec["entries_rendered"] = len(admitted)
            rec["leak_checked"] = True
        elif m["number"] == 6:
            text = render_defect_types(dt_rows, header)
            rec["rows_rendered"] = len(dt_rows)
            rec["columns_kept"] = header
            rec["leak_checked"] = True
        else:
            parts, spans = [], []
            for spec in m["spans"]:
                body, srec = span_lines(m["source"], spec)
                spans.append(srec)
                parts.append("\n".join(body))
            text = "\n\n".join(parts) + "\n"
            rec["spans"] = spans
            rec["leak_checked"] = False
            rec["leak_not_checked_because"] = (
                "members (1)-(4) are ruled WHOLE; the leak check is scoped to the two members this "
                "tool GENERATES. What member (2) carries is handled by the authored withheld "
                "passage instead.")
            for p in authored.get("withheld_passages", []):
                if p["member"] == m["number"]:
                    text, prec = withhold_passage(
                        text, p, "[A PASSAGE IS WITHHELD FROM THIS PACK FOR THIS SUBJECT.]")
                    passages_applied.append(prec)
        files[m["filename"]] = text
        rec["characters"] = len(text)
        member_records.append(rec)

    want_passages = len(authored.get("withheld_passages", []))
    if len(passages_applied) != want_passages:
        raise Stop(f"{want_passages} withheld passage(s) authored, {len(passages_applied)} applied")

    files[READ_ME] = render_read_me(subject, authored["the_subject_in_plain_words"],
                                    passages_applied, len(withheld_ids))

    criterion_bound, criterion_terms = criterion_block(subject)

    record = {
        "subject": subject,
        "the_subject_in_plain_words": authored["the_subject_in_plain_words"],
        "the_oracle_this_family_protects": authored["the_oracle_this_family_protects"],
        "the_directory": f"tools/audit/derivation_boot_pack/{subject}",
        "★_the_bound_on_the_candidate_criterion": criterion_bound,
        "the_candidate_criterion": criterion_terms,
        "counted": {
            "design_intent_class": len(design_intent),
            "candidates": len(cands),
            "verdicts": counted,
            "withheld_identities_authored": len(authored_ids),
            "withheld_identities_derived": len(adds),
            "withheld_identities_total": len(withheld_ids),
            "withheld_documents": len(docs),
            "withheld_passages": len(passages_applied),
            "leaks": len(leaks),
            "design_intent_entries_rendered": len(admitted),
            "defect_type_rows_rendered": len(dt_rows),
            "files_in_the_pack": len(files),
        },
        "THE_WITHHELD_FAMILY": {
            "★_what_this_is": (
                "AUTHORED, and it CLEARS NOTHING (D-655). A session may author an establishment; "
                "its verdicts are delivered as a ratification-surface reading file and the user "
                "rules them. No session boots from this pack before that ruling."),
            "identities": [
                {"id": r["id"], "title": r["title"], "finding": r["finding"],
                 "date": r["date"], "reason": r["reason"]}
                for r in verdict_rows if r["verdict"] == VERDICT_IN],
            "documents": authored.get("withheld_documents", {}),
            "passages": passages_applied,
            "derived_cross_reference_additions": {
                "★_what_these_are": (
                    "Entries of the DESIGN-INTENT class whose own text QUOTES OR "
                    "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
                    "the withheld set by the derivation rather than by hand. The fields searched "
                    "include `rationale` and `status_source`, which the pack does not render — a "
                    "cross-reference in either is still a route to the withheld material."),
                "★_the_bound": (
                    "ONE PASS, from the AUTHORED identities only. It is NOT transitive: an entry "
                    "that cross-references one of these additions rather than an authored "
                    "identity is not itself added."),
                "additions": adds,
            },
        },
        "THE_CANDIDATES_AND_THEIR_VERDICTS": verdict_rows,
        "LEAKS": {
            "★_what_this_is": (
                "An entry of member (5) or a row of member (6) whose RENDERED fields carry a "
                "withheld identity string, a withheld document's name, a `docs/` or `src/` path, "
                "or the string `ARCHITECTURE.md`. It is NOT rendered into the pack and is listed "
                "here instead."),
            "★_the_scope, stated because a scope that is not stated reads as total": (
                "Members (5) and (6) ONLY — the two this tool GENERATES. Members (1)-(4) are ruled "
                "WHOLE and are not string-checked; member (2)'s Conventions span names "
                "`ARCHITECTURE.md` in the never-work-from-memory rule BY DESIGN."),
            "entries": leaks,
        },
        "the_members_as_rendered": member_records,
    }
    return record, files


def build() -> tuple[dict, dict[str, dict[str, str]]]:
    sort = read_json(SORT)
    if "entries" not in sort:
        raise Stop("the rulings sort artifact carries no `entries`")
    bb_data = read_json(BACKBONE)
    backbone = {d["id"]: d for d in bb_data.get("decisions", [])}
    for r in bb_data.get("retired_entries", {}).get("entries", []):
        e = r.get("the_entry", {})
        if e.get("id") and e["id"] not in backbone:
            backbone[e["id"]] = e

    subjects, packs = {}, {}
    for subject in sorted(WITHHELD):
        rec, files = build_subject(subject, sort["entries"], backbone)
        subjects[subject] = rec
        packs[subject] = files

    manifest = {
        "what_this_is": (
            "THE DERIVATION BOOT PACK. The curated boot list an implementation-blind deriving "
            "session opens at boot, RENDERED into a self-contained directory per subject with the "
            "family withheld for that subject cut out of it. The session opens that directory and "
            "nothing else."),
        "generator": "tools/audit/gen_derivation_boot_pack.py",
        "the_rulings_it_executes": [
            "Ruling 1 and amendments (a1) and (a3) of "
            "`cowork_rulings_2026_08_22_boot_list_sitting.md` — the standing boot list, the "
            "per-session withheld list generated rather than hand-cut, and the defect catalog "
            "admitted at two columns.",
            "Ruling 1 of `cowork_rulings_2026_08_22_pilot_order_sitting.md` — the held-out test "
            "runs first, and this generator is built with the pilot's opening.",
            "Ruling 1 of `cowork_rulings_2026_08_22_member_two_leak_sitting.md` — the "
            "founding-instance passage of the never-work-from-memory rule is withheld from "
            "member (2) as an authored input in the D-677 shape.",
            "Ruling 4(c) of `cowork_rulings_2026_08_21_successor_plan_sitting.md` — the held-out "
            "test and its oracle.",
            "Ruling 1 of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md` — the second "
            "subject, `scoring-model`, rendered with an EMPTY withheld family, the standing leak "
            "check doing the whole of the cutting.",
        ],
        "★_it_boots_no_session": (
            "Rendering the pack is not opening it. Nothing here derives a specification "
            "statement, opens an oracle, or takes a pilot act."),
        "★_the_verdicts_clear_nothing": (
            "The withheld family is AUTHORED. Under D-655 a session may perform an owed "
            "establishment and author its verdicts, and those verdicts CLEAR NO GUARD when they "
            "are written: they are delivered as a ratification-surface reading file, and the user "
            "rules them before any session boots from this pack."),
        "what_is_AUTHORED": [
            "the six ruled members and their spans, each by ANCHOR TEXT and never by line number, "
            "imported from the ruled draft rather than re-decided",
            "the WITHHELD table per subject — identities, documents and passages, each with its "
            "finding, its date and its reason (the D-677 shape)",
            "the candidate criterion the dispatch fixes",
            "one verdict per derived candidate — IN, OUT or UNPLACED — with its finding, its date "
            "and its reason",
        ],
        "what_is_DERIVED": [
            "the candidate list, with the matching criterion recorded per candidate",
            "the `ARCHITECTURE.md` oracle spans, located by their own text on every run",
            "the cross-reference additions to the withheld set",
            "the cut of the DESIGN-INTENT class and the leak check over it",
            "every rendered file, byte for byte, and every count",
        ],
        "the_STOPS": [
            "an anchor not found exactly once in its file",
            "an authored withheld identity outside the DESIGN-INTENT class",
            "an authored withheld identity, document or passage missing its finding, date or "
            "reason",
            "a derived candidate with no authored verdict, and a verdict for an entry the "
            "derivation does not return as a candidate",
            "a verdict outside the closed three-value vocabulary, or a distribution that does not "
            "account for the candidate population",
            "an authored withheld identity that is not among the derived candidates",
            "a member's source file the tree does not carry",
            "a withheld passage whose opening or closing anchor is not found exactly once inside "
            "its ruled scope, or whose closing precedes its opening",
        ],
        "the_pack_files_in_order": [READ_ME] + [m["filename"] for m in MEMBERS],
        "subjects": subjects,
    }
    return manifest, packs


def pack_dir(subject: str) -> str:
    return os.path.join(PACK_ROOT, subject)


def write_all(manifest: dict, packs: dict, only: str | None) -> None:
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    for subject, files in sorted(packs.items()):
        if only and subject != only:
            continue
        d = pack_dir(subject)
        os.makedirs(d, exist_ok=True)
        for name, text in sorted(files.items()):
            with open(os.path.join(d, name), "w", encoding="utf-8", newline="") as fh:
                fh.write(text)


def check_all(manifest: dict, packs: dict) -> int:
    drift = []
    want = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    if have != want:
        drift.append("derivation_boot_pack.json does not re-derive")
    for subject, files in sorted(packs.items()):
        d = pack_dir(subject)
        if not os.path.isdir(d):
            drift.append(f"{subject}: the pack directory is missing")
            continue
        on_disk = sorted(n for n in os.listdir(d) if os.path.isfile(os.path.join(d, n)))
        if on_disk != sorted(files):
            drift.append(f"{subject}: the directory holds {on_disk}, not {sorted(files)}")
        for name, text in sorted(files.items()):
            p = os.path.join(d, name)
            got = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
            if got != text:
                drift.append(f"{subject}/{name} does not re-render")
    if drift:
        print("STALE: the derivation boot pack does not re-derive")
        for d in drift:
            print(f"  - {d}")
        return 1
    print("the derivation boot pack re-derives")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="render the derivation boot pack")
    ap.add_argument("--subject", help="render only this subject's directory")
    ap.add_argument("--check", action="store_true", help="re-render and compare, exit 1 on drift")
    args = ap.parse_args(argv)

    manifest, packs = build()
    if args.subject and args.subject not in packs:
        raise Stop(f"no authored subject {args.subject!r}")

    if args.check:
        return check_all(manifest, packs)

    write_all(manifest, packs, args.subject)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    for subject, rec in sorted(manifest["subjects"].items()):
        c = rec["counted"]
        print(f"  {subject}: design-intent {c['design_intent_class']} · "
              f"candidates {c['candidates']} · "
              f"IN {c['verdicts']['IN']} / OUT {c['verdicts']['OUT']} / "
              f"UNPLACED {c['verdicts']['UNPLACED']}")
        print(f"    withheld {c['withheld_identities_total']} "
              f"({c['withheld_identities_authored']} authored + "
              f"{c['withheld_identities_derived']} derived) · "
              f"documents {c['withheld_documents']} · passages {c['withheld_passages']} · "
              f"leaks {c['leaks']}")
        print(f"    rendered: {c['design_intent_entries_rendered']} design-intent entries, "
              f"{c['defect_type_rows_rendered']} defect-type rows, "
              f"{c['files_in_the_pack']} files")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
