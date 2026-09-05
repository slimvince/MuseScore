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

AND, SINCE 2026-08-31, PER-SUBJECT EXTRAS AFTER THEM (user, Ruling 16 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` -- his words, verbatim: "extend
generator").  Ruling 14 first put such an addition OUTSIDE this tool and ruled its own overturn
condition; it fired, decisively because `check_all` compares the DIRECTORY LISTING against the
generated set, so a file written into a pack directory from outside makes that pack permanently
STALE.  The extension is ADDITIVE AND PER-SUBJECT: the ruled six stay in every pack, unchanged
and in their ruled order -- which `build_subject` now STOPs on rather than promising -- and a
subject may carry EXTRAS after them.  An extra is quoted from named PARTS and may carry two
authored filters, `removals` (a passage by anchor text) and `cuts` (a section by what its heading
contains), each VERIFIED IN BOTH DIRECTIONS on every render: what was removed is absent, and
re-inserting exactly what was removed reproduces the source byte for byte.  Neither marks its
omission in place -- the verification is that the rendered member equals its source with exactly
those spans deleted, and a mark is an addition -- so what was cut is disclosed to the session in
the read-me instead.  `EXTRAS` carries an entry for EVERY subject and an empty list is authored,
never left absent.

AND, SINCE 2026-08-31, A SPENT SUBJECT IS FROZEN RATHER THAN RE-RENDERED (user, Ruling 17(a) of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`).  A subject whose deriving session HAS
RUN is SPENT: its pack is no longer an input to be kept current, it is the RECORD OF WHAT THAT
SESSION WAS GIVEN.  D-646 is the ruled shape -- *a generated record that must outlive its own
writer is frozen at an established snapshot, and the freeze is enforced by a hash STOP* -- and
`FROZEN` below is that snapshot: per subject, one digest per file of its pack directory.

  WHY A FREEZE AND NOT A REFRESH, recorded here so a later reader meets the ground rather than
  the mechanism alone.  ★ WHAT FOLLOWS IS THE GROUND OF THE TWO FREEZES TAKEN 2026-08-31, and it
  is scoped to them: each subject's own ground is in its own entry (#6), and `l0-l1`, frozen
  2026-09-04, was NOT stale when it was frozen.  Members (2) and (4) of the two packs frozen that
  day no longer re-render, because
  `CLAUDE.md` and `cowork_audit_protocol.md` have GROWN since those packs were rendered.  The
  drift is ADDITION-ONLY, and the first lines a re-render would add are the P-1
  ordinary-session-start-read clause and the P-2 standing dispatch clause, BOTH RATIFIED
  2026-08-29 -- after both packs were rendered and after both their sessions ran.  Re-rendering
  would therefore make those packs claim their sessions read rules that did not yet exist, which
  is a falsification of the record of two completed derivations (#12).

  THE DIGEST IS THE GIT BLOB HASH OF THE FILE'S OWN BYTES, and that is the point of choosing it:
  `git hash-object <file>` reproduces it from OUTSIDE this tool, so the freeze is checkable
  without trusting the generator that declares it (#19).  It was established at the objects when
  the table was filled that the filtered and unfiltered hashes agree for every one of these
  files, so the recorded digest is the hash of the bytes on disk and not of a normalized form.

  WHAT THE FREEZE DOES.  `write_all` writes NOTHING into a frozen subject's directory.
  `check_all` verifies that subject against its RECORDED DIGESTS instead of against a re-render,
  in both directions -- every recorded file present, every present file recorded, every digest
  equal -- and any mismatch is a STOP rather than a drift line, because a moved frozen file is
  not staleness to be regenerated away.  The manifest CONTINUES TO CARRY both subjects' entries.

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
     opening;
  9. a subject with no authored `EXTRAS` entry STOPS it -- an empty list is authored so that a
     missing one cannot read as an empty one;
 10. an EXTRA's removal anchor not found exactly once, or not sitting inside its own delimiter
     pair, STOPS it; an EXTRA's cut heading not found exactly once, or not terminated by a
     further heading at its own level, STOPS it; two of a part's filters overlapping STOPS it;
     and EITHER DIRECTION of the extras' verification failing STOPS it -- filtered text still
     present, or re-inserting what was removed not reproducing the source;
 11. the ruled six not intact, in their ruled order, at the head of a subject's rendered members
     STOPS it;
 12. a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one of whose
     files does not carry its recorded digest, STOPS it -- in both directions, so neither an
     added file nor a removed one passes; a FROZEN entry naming a subject this tool does not
     build STOPS it; and a freeze record missing its finding, its date or its reason STOPS it,
     on the same demand every other authored input here answers.

THE FOUR RESIDUALS THE EXTENSION CAUSED ARE REPAIRED (user, Ruling 17(c) of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`).  When the extras dimension landed,
`the_rulings_it_executes`, `the_STOPS`, `what_is_AUTHORED` and `the_pack_files_in_order` still
described the PRE-EXTENSION tool -- the last naming the ruled six and the read-me and no
subject's extras -- and the read-me's stop-and-record clause still read *"including one of these
six"*.  They were left standing then, and deliberately: the dispatch that ordered the extension
made it a STOP for the manifest to change by anything other than the addition of the new subject,
and every one of those fields is global.  Ruling 17(c) RELAXES that bar for this purpose and for
no other, and the four are now repaired: `the_pack_files_in_order` is DERIVED PER SUBJECT from
the members actually rendered for it, the three descriptive fields state this tool's actual
state, and the read-me's count is derived.  THE STOP-AND-RECORD CLAUSE'S RULE IS UNCHANGED and
the boundary clause is untouched -- only the count moved.

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
import hashlib
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

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — the FROZEN table: a SPENT subject, pinned at the blobs its pack actually carries.
#
# THE RULING THIS EXISTS FOR (user, 2026-08-31, Ruling 17(a) of
# `cowork_rulings_2026_08_31_decision_surface_sitting.md`), quoted verbatim:
#
#     The two existing packs are not re-rendered.  They are frozen, and `--check` ranges over
#     live subjects. … `harmony-boundary` and `scoring-model` are pinned at their current blobs
#     as SPENT, with that hash STOP; nothing is re-rendered and nothing is lost, and `l0-l1` can
#     go green on its own.
#
# WHAT MAKES A SUBJECT SPENT, stated so the table is not read as a convenience: its deriving
# session HAS RUN, so its pack is no longer an input to be kept current — it is the record of
# what that session was given, and D-646 is the ruled shape for a generated record that must
# outlive its own writer.
#
# THE GROUND FOR FREEZING RATHER THAN REFRESHING, which is a fact and not a preference: members
# (2) and (4) of both packs no longer re-render because `CLAUDE.md` and `cowork_audit_protocol.md`
# have GROWN, and the first lines a re-render would add are the P-1 and P-2 clauses RATIFIED
# 2026-08-29 — after both packs were rendered and after both their sessions ran.  A re-render
# would make those packs claim their sessions read rules that did not yet exist (#12).
#
# THE DIGEST IS THE GIT BLOB HASH OF THE FILE'S OWN BYTES.  `git hash-object <file>` reproduces
# every value below from outside this tool, so the freeze does not rest on this generator's own
# word (#19).  Each digest was taken at the object on 2026-08-31, and it was established in the
# same act that `git hash-object` and `git hash-object --no-filters` agree on every one of these
# files — so the recorded value is the hash of the bytes on disk, not of a normalized form.
# ══════════════════════════════════════════════════════════════════════════════════════════════
FROZEN: dict[str, dict] = {
    "harmony-boundary": {
        "finding": ("Its deriving session has run.  `--check` reports members (2) and (4) STALE "
                    "because `CLAUDE.md` and `cowork_audit_protocol.md` have grown since this "
                    "pack was rendered, and the drift is addition-only."),
        "date": "2026-08-31",
        "reason": ("Re-rendering would add to this pack the P-1 and P-2 clauses ratified "
                   "2026-08-29 — after this pack was rendered and after its session ran — and so "
                   "would make the pack claim its session read rules that did not yet exist "
                   "(#12).  Frozen at the blobs it carries, under D-646, with the hash STOP."),
        "digests": {
            "00_READ_THIS_FIRST.md": "ae9edbb2cef09eb94f1156713f1dc22e9d71b402",
            "01_the_phase_definitions.md": "518b1e50d60af2b4e2ddcd8978623832eb071899",
            "02_the_guiding_principles_and_the_conventions.md":
                "5d1fd0365379ba90ae817a5a1c5e9446348f0744",
            "03_the_writing_standards.md": "518048459da6a865285a0f7c66c5d8f8045f0fc2",
            "04_the_dispatch_protocol.md": "48a68197394ead0dbe0266b5f91bf3c885fc93ef",
            "05_the_ratified_design_intent.md": "dbcd948d20fffaec8eb45e84ee7620b33fec5ea8",
            "06_the_defect_type_catalog.md": "1dec7621dc48d89242cacaf79b3048cd965d6a19",
        },
    },
    "scoring-model": {
        "finding": ("Its deriving session has run.  `--check` reports members (2) and (4) STALE "
                    "for the same two grown sources, and the drift is addition-only here too."),
        "date": "2026-08-31",
        "reason": ("The same ground, and it is the same two ratified clauses: a re-render would "
                   "put rules dated after this session into the pack that session was given "
                   "(#12).  Frozen at the blobs it carries, under D-646, with the hash STOP."),
        "digests": {
            "00_READ_THIS_FIRST.md": "5068c69314655a6b258196e7b30886c8350a083c",
            "01_the_phase_definitions.md": "518b1e50d60af2b4e2ddcd8978623832eb071899",
            "02_the_guiding_principles_and_the_conventions.md":
                "cf718c5678b07e89924b2e39d53982074069fa9c",
            "03_the_writing_standards.md": "518048459da6a865285a0f7c66c5d8f8045f0fc2",
            "04_the_dispatch_protocol.md": "48a68197394ead0dbe0266b5f91bf3c885fc93ef",
            "05_the_ratified_design_intent.md": "60563ab26e5c5c8827e32645b12eceaeb355933b",
            "06_the_defect_type_catalog.md": "1dec7621dc48d89242cacaf79b3048cd965d6a19",
        },
    },
    "l0-l1": {
        "finding": ("Its deriving session has RUN: the detail-specification phase's first "
                    "derivation was delivered 2026-09-02 and is "
                    "`cowork_blind_derivation_l0_l1_2026_08_31.md` (the sitting record, §3al). "
                    "Unlike the two subjects frozen on 2026-08-31, this pack was NOT stale when "
                    "it was frozen — `--check` PASSED at the tip's own guard run — so the "
                    "digests recorded here are both what the sources render today and what its "
                    "session was given."),
        "date": "2026-09-04",
        "reason": ("A spent subject's pack is the record of what its session was given rather "
                   "than an input to be kept current (Ruling 17(a); D-646). Left live it would "
                   "re-render on the first growth of `CLAUDE.md` or `cowork_audit_protocol.md` — "
                   "the addition-only drift that made the other two packs stale — and would then "
                   "either turn `--check` red or, if refreshed, back-date into a completed "
                   "derivation's record rules that did not exist when its session ran (#12). "
                   "Frozen at the blobs it carries, with the hash STOP."),
        "digests": {
            "00_READ_THIS_FIRST.md": "7e7339cf3250ac87337317ca109cf9645dd31b8d",
            "01_the_phase_definitions.md": "518b1e50d60af2b4e2ddcd8978623832eb071899",
            "02_the_guiding_principles_and_the_conventions.md":
                "00ffb0bede471f15d70de6cb7435a617b09caa58",
            "03_the_writing_standards.md": "518048459da6a865285a0f7c66c5d8f8045f0fc2",
            "04_the_dispatch_protocol.md": "02107d1ab37af197821edf3ca98ccf6f7ae5c0d3",
            "05_the_ratified_design_intent.md": "60563ab26e5c5c8827e32645b12eceaeb355933b",
            "06_the_defect_type_catalog.md": "1dec7621dc48d89242cacaf79b3048cd965d6a19",
            "07_the_charter_the_layers_and_the_decisions.md":
                "a0513707886414a1c193a884e3f5f15ffd3f12f5",
            "08_the_five_research_extracts.md": "54d0892b022107a8bd4cedc9e4bba54679a1ed41",
            "09_the_empirical_findings_ledger.md": "2bf845db798e91382236387e7f35fabf48b2ec07",
        },
    },
    # `l0-l1` IS FROZEN ABOVE, ITS DERIVING SESSION HAVING RUN ON 2026-09-02; its own ground is
    # in its own entry and is not restated here (#6).
    # ★ SUPERSEDED 2026-09-04, THE FORMER WORDING PRESERVED IN PLACE (#12): "`l0-l1` IS ABSENT
    # DELIBERATELY, and its absence is what makes it LIVE: its deriving session has not run, so
    # its pack is still an input and must stay current with its sources."  True when written, and
    # made false by that session's run.
}

# The header row of `DEFECT_TYPES.md`'s catalog table, matched exactly once.  Amendment (a3)
# admits its first two columns — `ID` and `type (plain)` — and excludes the other three.
DEFECT_TABLE_HEADER = "| ID | type (plain) | founding instance | detection signature | mechanical? |"
DEFECT_COLUMNS_KEPT = 2

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — the PER-SUBJECT EXTRAS, rendered AFTER the ruled six.
#
# THE RULING THIS EXISTS FOR (user, 2026-08-31, Ruling 16 of
# `cowork_rulings_2026_08_31_decision_surface_sitting.md`).  The user's words, verbatim:
#
#     extend generator
#
# and the shape ruled with them, quoted verbatim from the same ruling:
#
#     `MEMBERS` is global and was ruled by the user on 2026-08-22.  The extension is therefore
#     ADDITIVE and PER-SUBJECT: the ruled six stay in every pack, unchanged and in their ruled
#     order, and a subject may carry EXTRAS after them.  For the two existing subjects the extras
#     list is empty, so both existing packs and the manifest must re-render BYTE-IDENTICAL.
#
# WHY THE GENERATOR RATHER THAN THE BRIEF.  Ruling 14 first put the filtered charter member
# outside this tool and ruled its own overturn condition; it fired at three findings in this
# file, the decisive one being that `check_all` compares the DIRECTORY LISTING against the
# generated set — so a file written into a pack directory from outside makes that pack
# permanently STALE.  Extras are members, inside the pack's own integrity check.
#
# EVERY SUBJECT CARRIES AN ENTRY HERE, and an EMPTY list is AUTHORED rather than left absent, so
# that the emptiness is visible where a reader looks for a subject's extras — the shape the
# `scoring-model` verdict table already uses.  A subject absent from this table STOPS the tool.
#
# AN EXTRA IS RENDERED FROM PARTS.  Each part names ONE source file, the spans of it that are
# taken (the same four span kinds the ruled members use, by ANCHOR TEXT and never by line
# number), and two AUTHORED FILTERS over what those spans returned:
#
#   removals  a passage addressed by ANCHOR TEXT, deleted from the opening of the delimiter pair
#             it sits inside to that pair's close.  The anchor must match EXACTLY ONCE in the
#             part's own text, whitespace-normalized so an anchor may span a line break, or the
#             tool STOPS.
#   cuts      a section addressed by a string its HEADING contains, deleted from that heading up
#             to the next heading at the same level.  Not found exactly once, or not terminated
#             by such a heading, STOPS the tool.
#
# BOTH FILTERS ARE VERIFIED IN BOTH DIRECTIONS ON EVERY RUN, and a failure in either direction is
# a STOP: what was removed is ABSENT from what is rendered, AND re-inserting exactly what was
# removed at the offsets it came from reproduces the source byte for byte — which is what proves
# NOTHING ELSE was taken out.  Neither filter marks its omission in place: the ruling's own
# verification is that the rendered member equals its source with exactly the named spans
# deleted, and a mark is an addition.  What was cut is disclosed to the session in the read-me
# instead, which is where the design-intent member's own gaps are disclosed.
# ══════════════════════════════════════════════════════════════════════════════════════════════
EXTRAS: dict[str, list[dict]] = {
    # EMPTY BY RULING for both existing subjects, and the emptiness is the proof the extension is
    # additive: their packs and their manifest entries must re-render byte-identical.
    "harmony-boundary": [],
    "scoring-model": [],

    "l0-l1": [
        {
            "number": 7,
            "filename": "07_the_charter_the_layers_and_the_decisions.md",
            "title": "The ratified charter — the layers, their contracts, and the architecture "
                     "decisions",
            "source": "FRAMEWORK.md",
            "rendered_from": "the file itself, quoted — §5 and §9 whole, with two passages removed",
            "parts": [
                {
                    "source": "FRAMEWORK.md",
                    "spans": [
                        {"kind": "heading-to-heading",
                         "start": "## 5. Building-block view — the layers",
                         "end": "## 6. Runtime view — scenarios"},
                        {"kind": "heading-to-heading",
                         "start": "## 9. Architecture decisions",
                         "end": "## 10. Quality and testing"},
                    ],
                    # Ruling 11 Decision 1 cuts every passage describing what this project
                    # currently has.  Ruling 16 carried Ruling 14's other half unchanged and
                    # named two: DP-N's and DP-Q's stage-two parentheticals.  Ruling 17(b) then
                    # widened the filter by ONE and no more, on the sweep the extension reported
                    # — §5's second-axis provenance parenthetical.  The filter is exactly these
                    # three; widening it further is the user's act, not this tool's.
                    #
                    # NOT REMOVED, and the exclusions are recorded because an excluded candidate
                    # is evidence about the filter (Ruling 17(b)): DP-N's two disagreeing
                    # analyses and DP-Q's three exemplar analyses DESCRIBE CORPUS MATERIAL rather
                    # than what this project's system does, so they do not breach
                    # implementation-blindness, and both are load-bearing EVIDENCE for their
                    # design points; and the two references to the ledger are MOOT, the pack
                    # carrying that document whole as member (9).
                    "removals": [
                        {"anchor": "This is adopted from this project's material",
                         "opens_with": "*(",
                         "closes_with": ")*",
                         "why": ("§5's second-axis parenthetical.  Ruling 17(b) of "
                                 "`cowork_rulings_2026_08_31_decision_surface_sitting.md`: pure "
                                 "provenance — it tells the reader that this project's own "
                                 "material holds the decision — the same shape as the two "
                                 "anchors Ruling 16 carried, and its removal costs the deriving "
                                 "session nothing.")},
                        {"anchor": "Stage two established that this project's own layer "
                                   "specifications",
                         "opens_with": "*(",
                         "closes_with": ")*",
                         "why": ("DP-N.  Ruling 16 of "
                                 "`cowork_rulings_2026_08_31_decision_surface_sitting.md`, "
                                 "carrying Ruling 14's unspent half: it states what this "
                                 "project's own layer specifications do and do not say about the "
                                 "cadential six-four, which is a description of what this project "
                                 "currently has.")},
                        {"anchor": "Stage two found the same question open in this project's own "
                                   "record",
                         "opens_with": "*(",
                         "closes_with": ")*",
                         "why": ("DP-Q.  The same ruling: it states a rule this project's own "
                                 "record carries about abstention on the tonality axis, and that "
                                 "the record does not settle which governs.")},
                    ],
                    "cuts": [],
                },
            ],
        },
        {
            "number": 8,
            "filename": "08_the_five_research_extracts.md",
            "title": "Five published sources, read at the object — the L1 slice",
            "source": "reading_pass/extracts/ — the five named in "
                      "`reading_pass/candidacy_upgrades.md`'s reading-progress table",
            "rendered_from": "the five files themselves, quoted whole, each with ONE named "
                             "section cut",
            "parts": [
                {
                    "source": f"reading_pass/extracts/{stem}.md",
                    "spans": [{"kind": "whole"}],
                    "removals": [],
                    # Ruling 11 Decision 2: the extracts go in WITH their
                    # "What an L1 detail specification could adopt, adapt, or must argue against"
                    # sections CUT — this side's conclusions over the papers, which a deriving
                    # session must reach for itself.  ONE named section, and no more: the
                    # findings section each extract also carries is deliberately NOT cut.
                    "cuts": [
                        {"heading_contains": "detail specification could adopt, adapt, or must "
                                             "argue against",
                         "heading_level": "## ",
                         "why": ("Ruling 11 Decision 2 of "
                                 "`cowork_rulings_2026_08_31_decision_surface_sitting.md`: it is "
                                 "this side's conclusion about what an L1 specification should "
                                 "do with the paper, which is the deriving session's own work.")},
                    ],
                }
                for stem in (
                    "pardo-birmingham-2002-algorithms-for-chordal-analysis",
                    "temperley-sleator-1999-modeling-meter-and-harmony",
                    "bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-"
                    "detection",
                    "karystinaios-widmer-2022-cadence-detection-graph-neural-networks",
                    "sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences",
                )
            ],
        },
        {
            "number": 9,
            "filename": "09_the_empirical_findings_ledger.md",
            "title": "The admitted empirical findings",
            "source": "EMPIRICAL_FINDINGS_LEDGER.md",
            "rendered_from": "the file itself, quoted, whole and unfiltered",
            "parts": [
                # WHOLE AND UNFILTERED, by Ruling 12's correction of record: §3.4 of
                # `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` names
                # "the same independent sources and ledger as the framework phase" among this
                # phase's inputs, so the ledger enters by the phase definition's own naming and
                # not by any decision taken at that sitting.
                {"source": "EMPIRICAL_FINDINGS_LEDGER.md",
                 "spans": [{"kind": "whole"}],
                 "removals": [],
                 "cuts": []},
            ],
        },
    ],
}

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

    # ── THE FIRST DERIVING SUBJECT OF THE DETAIL-SPECIFICATION PHASE — an EMPTY withheld family ─
    # Ruling 10 of `cowork_rulings_2026_08_31_decision_surface_sitting.md` made L0+L1 that
    # phase's first deriving subject.  The EMPTY family is ordered by Task 4 of
    # `cc_instruction_l0l1_boot_pack_2026_08_31.md`, quoted verbatim:
    #
    #     Add `l0-l1` with an EMPTY withheld family, on the `scoring-model` precedent Task 1
    #     established.
    #
    # ★ WHAT THE RECORD DOES AND DOES NOT SAY, WRITTEN HERE SO IT IS NOT LATER READ AS MORE THAN
    # IT IS.  For `scoring-model` a ruling states in its own words that the unit is not held out
    # and has no oracle.  NO RULING OF 2026-08-31 SAYS THAT OF `l0-l1`.  What the record carries
    # is the dispatch's order above and the precedent it rests on, and that is what is stated
    # here — the ground is DECLARED, not established (#24), and inventing a ruling to fill it
    # would be the defence-written-afterwards that the never-work-from-memory rule forbids.
    "l0-l1": {
        "the_subject_in_plain_words":
            "L0, the input contract — what a notated record must supply, what may be assumed of "
            "it, and what happens when a real score does not supply it — and L1, which finds the "
            "moments at which a harmony may begin and publishes what the notation says at each, "
            "deciding nothing about the music.",
        "the_oracle_this_family_protects": (
            "NONE IS NAMED.  No withheld identities, no withheld documents, no withheld passages: "
            "Task 4 of `cc_instruction_l0l1_boot_pack_2026_08_31.md` orders the family empty on "
            "the `scoring-model` precedent, and the standing leak check does the whole of the "
            "cutting over the two generated members.  What is NOT claimed, because no ruling of "
            "2026-08-31 states it: that this unit is not held out against an oracle.  The record "
            "carries the order and the precedent, and no more."),
        "withheld_documents": {},
        "withheld_passages": [],
        # NO `the_identity_the_ruling_names`: none is named, the family being empty.
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

# ── L2's ruled keyword list — FORTY-TWO TERMS ─────────────────────────────────────────────────
# Ruling 86, §3co of `cowork_rulings_2026_08_31_decision_surface_sitting.md`, in its own words:
# "The pilot's eighteen, unchanged" plus "the twenty-four added for the other three charter
# limbs", and "the six bare words `mode`, `root`, `quality`, `figure`, `applied` and `passing`
# are EXCLUDED" — they must not appear below.
#
# THE EIGHTEEN ARE TAKEN FROM `KEYWORDS` RATHER THAN RETYPED (#6): the ruling says unchanged, and
# a second copy of them would be a second place to change.  `KEYWORDS` ITSELF IS NOT WIDENED —
# `harmony-boundary` reads it, that subject is FROZEN and its verdict table is authored for the
# candidate set the eighteen produce, so widening the shared tuple would derive candidates with
# no verdict and `build_subject` would STOP.
L2_KEYWORDS = KEYWORDS + (
    # the tonality at each moment
    "tonality", "tonic", "local key", "key area", "modulation", "tonicization",
    # which sounding notes belong to the harmony and which elaborate it
    "chord tone", "non-chord", "chord-tone assignment", "elaboration relation",
    "passing tone", "passing note", "neighbour", "neighbor", "suspension", "anticipation",
    "ornament",
    # what chord is read over each span
    "scale degree", "roman numeral", "inversion", "applied chord", "chord quality",
    "figured bass",
    # the charter's own word for what L2 must publish beside its answer
    "rival",
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
    # EMPTY on the same ground and in the same shape: the withheld family is empty for this
    # subject, so no candidate has to be derived and no verdict has to be authored.  The
    # empty-criterion branch of `criterion_block` recognizes the STATE and not the subject name,
    # so this subject renders truthfully without a line of that function being touched.
    "l0-l1": {
        "groups": (),
        "home_documents": (),
        "architecture_spans": (),
        "keywords": (),
        "always": (),
    },
    # ── L2, the next deriving subject under Ruling 10 ─────────────────────────────────────────
    # DORMANT BY DESIGN, AND THE DORMANCY IS DECLARED WITH ITS CONSUMER NAMED (the
    # fact-publication corollary: a fact consumed by no one is declared dormancy or waste).
    # NOTHING REACHES THIS ENTRY TODAY: `build()` iterates `WITHHELD`, and no `l2` withheld
    # family is authored, because L2's family is ruled list by list at Cowork decision surfaces
    # (Ruling 81, §3cj) and no list exists yet.  Its consumer is `build_subject("l2", ...)`, which
    # runs when that family lands — a separate act, not this one.
    #
    # EVERY TERM IS RULED, each cited to the section that ruled it in
    # `cowork_rulings_2026_08_31_decision_surface_sitting.md`:
    #   groups              Ruling 82, §3ck — A, C, D, E, F and G, "the six register groups the
    #                       charter's four limbs and their vocabulary reach".
    #   keywords            Ruling 86, §3co — the forty-two of `L2_KEYWORDS` above.
    #   home_documents      Ruling 87, §3cp — the thirteen documents holding a design-intent entry
    #                       the group and keyword terms do not already reach — PLUS
    #                       `ARCHITECTURE.md`, added by Ruling 88, §3cq: fourteen in all.
    #                       `cowork_layer5_engagement_design.md` is STRUCK by Ruling 89, §3cr,
    #                       its naming refuted at the object, and MUST NOT appear here.
    #   architecture_spans  Ruling 88, §3cq — EMPTY.  The file is named as a document, so no
    #                       passage is named and no anchor is authored.
    #   always              NO RULING OF THAT RECORD NAMES AN IDENTITY FOR THIS SUBJECT, so the
    #                       term is empty.  Said here rather than left to be read off an empty
    #                       tuple, which would not distinguish "none named" from "not yet filled".
    #
    # WHAT THIS TABLE PICKS, and it is the one check that it was written as ruled: over the 244
    # DESIGN-INTENT entries of `tools/audit/rulings_sort_classification.json`'s 411, the group
    # term alone picks 130, the keyword list adds 47 beyond it, and the home-document list adds
    # the remaining 67.  130 + 47 + 67 = 244, and the criterion picks 244 of 244.
    #
    # THE BOUND THAT SURVIVES THAT (#24, D-661): the population is the sort artifact's 411, NOT
    # the decisions register's 477.  Sixty-six register entries are outside it and no term of this
    # criterion can reach them.  Complete is complete relative to that membership and nothing
    # wider.
    "l2": {
        "groups": ("A", "C", "D", "E", "F", "G"),
        "home_documents": (
            "ARCHITECTURE.md",
            "CLAUDE.md",
            "cowork_architecture_review_2026_07.md",
            "cowork_census_full_needs_audit.md",
            "cowork_engage_arc_plan.md",
            "cowork_layer6_grouping_design.md",
            "cowork_notation_output_contract.md",
            "cowork_phrase_boundary_design.md",
            "cowork_progression_schema_design.md",
            "cowork_progression_schema_dictionary.md",
            "cowork_score_census.md",
            "cowork_voiceleading_axis_design.md",
            "docs/llm_integration.md",
            "docs/scoring_model.md",
        ),
        "architecture_spans": (),
        "keywords": L2_KEYWORDS,
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

    # The first deriving subject of the detail-specification phase, in the same state and for the
    # same reason: an empty criterion returns no candidate, so there is nothing to grade.
    "l0-l1": {},

    # ── L2, the next deriving subject under Ruling 10 — PROPOSALS, NOT A WITHHELD FAMILY ─────────
    # Ruling 81 (§3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`): every candidate
    # carries an authored verdict with its finding, its date and its reason; the lists go to the
    # user one per turn; NO identity is withheld that he has not ruled.  So this table is a set of
    # proposals.  `WITHHELD` carries no `l2` entry, `build()` iterates `WITHHELD`, and therefore
    # NOTHING READS THIS TABLE TODAY: it is dormant by design, its consumer the `build_subject("l2")`
    # run that happens when the user has ruled the lists and the family is authored — a separate act.
    #
    # THE TEST, from the pilot's Task 1(d) with L2's four-limbed charter question in place of the
    # pilot's one-limbed one (`FRAMEWORK.md` §5, the L2 block): IN — a deriving session that read
    # this entry would know, in whole or in part, what the ruled answer is to "over this music, what
    # is the tonality at each moment, where does each harmony give way to the next, which sounding
    # notes belong to the harmony and which elaborate it, and what chord is read over each span?";
    # OUT — the entry bears on another unit, and the reason says which; UNPLACED — the entry's own
    # text does not settle it, and the reason says what was read.  DEFAULT NOTHING.
    #
    # THE DATE.  Ruling 81 requires each verdict to carry its date.  The renderer stamps every
    # verdict with the module constant `DATE` (2026-08-22, the pilot's authoring date), which is
    # false for this table and is recorded as OWED at the batch that builds L2's pack — see
    # `cc_instruction_l2_verdict_pass_2026_09_05.md`.  Until the mechanism carries a per-subject
    # date, the authoring date of each group block is stated in that block's own heading comment.
    #
    # ORDER: the register groups the ruled group term names first (A, C, D, E, F, G), then the
    # twelve groups reached only by the keyword or home-document terms (B, H, I, J, K, L, M, N, Q,
    # S, T, U); inside a group, ascending entry number.  A group block is either COMPLETE — every
    # candidate of that group graded — or ABSENT; there is no partly written group (D-671, D-672).
    "l2": {

        # ── group A — The estimator architecture — the joint estimator — 27 candidates — authored 2026-09-05 ──
        "D-001": (VERDICT_IN,
                  "Its verbatim rules key, mode and chord inferred by ONE probabilistic decode over "
                  "`(tonic, mode, chord)` with segmentation as a modeled semi-Markov variable; its "
                  "plain says that single pass 'also decides where one chord ends and the next "
                  "begins'.",
                  "It states the ruled answer to all four limbs at once — the tonality, the "
                  "boundary, and the chord are decided together in one decode."),
        "D-002": (VERDICT_OUT,
                  "Its verbatim compiles the committed artifacts and the selected weight vector "
                  "VERBATIM into a generated source pair rather than reading them from disk.",
                  "It bears on how fitted artifacts are delivered into the binary — build and "
                  "provenance — and says nothing about what tonality, boundary, tone status or "
                  "chord is read."),
        "D-003": (VERDICT_IN,
                  "Its verbatim rules inference PRESET-INDEPENDENT, presets being presentation "
                  "concerns; its plain says the preset 'changes nothing about what the estimator "
                  "concludes'.",
                  "It rules out the style preset as evidence in the reading itself, which is part "
                  "of the ruled answer to what decides the tonality and the chord."),
        "D-005": (VERDICT_IN,
                  "Its verbatim names the joint estimator 'the PRODUCTION inference layer on the "
                  "batch/corpus surface'; its plain says the graded reading comes from it and not "
                  "from the older chord-by-chord pipeline.",
                  "It tells a session that the reading is produced by a joint estimator rather than "
                  "by a staged chord-by-chord path, which is the shape of the ruled answer."),
        "D-095": (VERDICT_OUT,
                  "Its verbatim records the migration state CLOSED on both surfaces and the legacy "
                  "`region::analyzeRegions` → `analyzeSection` path compiled and dormant, awaiting "
                  "deletion at the retirement map.",
                  "It bears on the declared migration state and the retirement of the legacy path — "
                  "governance under #23 — not on any of the four limbs."),
        "D-096": (VERDICT_IN,
                  "Its verbatim rules that factor FORMS come from theory and factor VALUES are fit "
                  "ONCE against ground truth and never tuned per case.",
                  "The charter assigns the score's terms and their fitting to this layer's detail "
                  "specification, and this states the ruled shape of both."),
        "D-114": (VERDICT_IN,
                  "Its verbatim rules that on the key axis the decoder commits its "
                  "maximum-a-posteriori path and NEVER abstains, naming a key for every committed "
                  "segment.",
                  "It states the ruled answer to the tonality limb's commitment behaviour: a "
                  "tonality is named at every moment, with no abstention."),
        "D-270": (VERDICT_IN,
                  "Its verbatim fixes the held-out protocol — five-fold cross-validation grouped by "
                  "ground-truth analysis file, everything fitted inside the training folds only, "
                  "the held-out fold touched exactly once.",
                  "The charter names 'how any weight is fitted' as part of this layer's detail "
                  "specification, and this states the ruled fitting and evaluation protocol."),

        "D-271": (VERDICT_IN,
                  "Its verbatim fixes the capacity budget — a cell keeps its own estimate only at or "
                  "above a stated training count, otherwise pooling to a declared parent under "
                  "smoothing, with free parameters bounded against the training tokens.",
                  "Same ground as D-270: the charter assigns the fitting of this layer's values to "
                  "its detail specification, and this states the ruled capacity rule."),
        "D-283": (VERDICT_IN,
                  "Its verbatim rejects a learned key detector in favour of structural levers; its "
                  "plain states that the later ratifications govern — the joint estimator infers "
                  "the key inside a theory-declared generative form whose factor values are fitted "
                  "once, its cadence factor carrying the structural insight.",
                  "The plain restates the current ruled answer to the tonality limb, so a session "
                  "reading the entry would have it however the verbatim is read."),
        "D-285": (VERDICT_IN,
                  "Its verbatim rules embellishment chord-first — segmentation then a "
                  "non-chord-tone post-process — never a union re-derive or a widened vocabulary; "
                  "its plain says the ratified factorization's emission carries exactly that shape.",
                  "It states the ruled answer to the third limb: which sounding notes belong to the "
                  "harmony is decided against the committed chord, not by widening the chord."),
        "D-376": (VERDICT_IN,
                  "Its verbatim weighs a single joint-state decoder against a bounded coupling over "
                  "two existing decoders and chooses the coupling; its plain says the option "
                  "rejected there 'is the shape the production engine now has'.",
                  "It names both candidate shapes for deciding the tonality and the chord together "
                  "and says which one the production reading has."),
        "D-449": (VERDICT_IN,
                  "Its verbatim fixes factor granularity — the bass factor per event, the "
                  "missing-tone penalty per event of segment length, the emission per tone, and the "
                  "transition, entry and key-change factors per boundary.",
                  "It states the ruled counting of every term the four limbs are decided by, and "
                  "names the length bias that fixing it removes from the boundary decision."),
        "D-450": (VERDICT_IN,
                  "Its verbatim rules that the key-signature and declared-mode prior conditions the "
                  "INITIAL key state only, re-entering only at a notated signature change, and "
                  "REJECTS a persistent pull toward the signature at every step.",
                  "It states the ruled answer to what the written signature contributes to the "
                  "tonality at each moment, and what it may not contribute."),
        "D-451": (VERDICT_OUT,
                  "Its verbatim rules that every table value a desk simulation uses is PROVISIONAL, "
                  "declared before use, and that none may survive into a fit.",
                  "It bears on the desk-simulation procedure under the Premise Gate (#17c) — how a "
                  "mechanism is traced by hand — not on what the traced mechanism decides."),
        "D-452": (VERDICT_OUT,
                  "Its verbatim rules that every desk-simulation trace runs the generative product "
                  "with every weight at one, so the trace tests the structure and the tables rather "
                  "than the weighting.",
                  "Same subject as D-451: it bears on how a trace is run, not on what tonality, "
                  "boundary, tone status or chord is read."),
        "D-453": (VERDICT_IN,
                  "Its verbatim is a verdict — 'the ratified factorization passes nine of ten "
                  "traces as specified; no finding requires re-ratifying the STRUCTURE (variables, "
                  "factors, decode)' — and states no variable, factor or decode rule.",
                  "Ruled IN 2026-09-05 from UNPLACED (Ruling 3 of "
                  "`cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`): its plain names the "
                  "counting granularity as the one thing sharpened and the variables, factors and "
                  "decode as ratified, so a session reading it learns that a ratified factorization "
                  "exists and which of its points was open; the pilot's family graded the same text "
                  "IN and that ruling stands, and the same text cannot settle the superset question "
                  "less than it settled the subset."),
        "D-524": (VERDICT_IN,
                  "Its verbatim rules the joint state's mode axis {major, minor} with the composite "
                  "minor, puts modal and chromatic colour in the pitch-emission factor rather than "
                  "the state, excludes the dominant-family exotic scales, and requires the "
                  "un-rounded reading published.",
                  "It states the ruled vocabulary of the tonality limb and where everything outside "
                  "that vocabulary is modelled instead."),
        "D-525": (VERDICT_IN,
                  "Its verbatim fixes the staged fit — factor tables counted generatively from "
                  "ground truth and frozen, a small combination-weight vector fit discriminatively, "
                  "with all-weights-equal-one as the mandatory ablation arm that must be beaten.",
                  "It states the ruled construction of the score over candidate readings, which the "
                  "charter assigns to this layer's detail specification."),
        "D-526": (VERDICT_IN,
                  "Its verbatim rules the joint state's chord axis SCALE-DEGREE-VALUED — a Roman "
                  "numeral of degree, quality and inversion relative to the state's own tonic and "
                  "mode — with the chord symbol a DERIVED fact published once.",
                  "It states the ruled answer to the fourth limb: what a chord read over a span "
                  "actually is, and what is merely derived from it."),
        "D-527": (VERDICT_IN,
                  "Its verbatim rules that NO live non-chord-tone cleaning stage exists — each tone "
                  "is emitted by category inside the one decode on chord-independent melodic and "
                  "metric covariates, and ornament labels are derived AFTER the decode.",
                  "It states the ruled answer to the third limb: chord identity and tone status are "
                  "settled together, and no elaboration verdict is committed early."),
        "D-528": (VERDICT_IN,
                  "Its verbatim rules the key-signature and declared-mode prior a weak, fitted, "
                  "transposition-invariant SOFT prior with no conditional gate and no threshold "
                  "anywhere, and formally retires the hard declared-mode penalty.",
                  "It states the ruled strength and form of the written signature's contribution to "
                  "the tonality at each moment."),
        "D-532": (VERDICT_IN,
                  "Its verbatim adds one pooling level to the chord-transition table grouping a "
                  "secondary dominant's continuations by their RELATION to the target — resolves "
                  "versus moves elsewhere — restoring the distinction from counts.",
                  "It states a ruled term of the model that decides what chord is read over each "
                  "span and how one span's chord conditions the next."),
        "D-533": (VERDICT_IN,
                  "Its verbatim rules that a continuation too rare to hold its own probability is "
                  "scored by dividing the row's leftover in PROPORTION to each chord's overall "
                  "frequency — never evenly and never as impossible.",
                  "It states the ruled back-off inside the transition model that decides what chord "
                  "is read over each span."),
        "D-534": (VERDICT_IN,
                  "Its verbatim rules the penalty for a chord tone that never sounds COUNTED per "
                  "chord factor — root, third, fifth, seventh — from every humanly labelled chord "
                  "segment, replacing one blanket value.",
                  "It states a ruled term of the emission that decides both which notes a candidate "
                  "chord expects and what chord is read over a span."),
        "D-535": (VERDICT_OUT,
                  "Its verbatim reports that across three passages the real counted values overturn "
                  "no desk-simulation verdict, that margins moved by 1.5–3.5 in both directions, "
                  "and that one margin expectation was plainly wrong.",
                  "Ruled OUT 2026-09-05 from UNPLACED (Ruling 3 of the same record): it bears on the "
                  "checking stage's own outcome — a confirmation that the real counted tables "
                  "overturned no desk-simulation verdict — reporting no value and no rule; what it "
                  "discloses about the tables, that they are counted from data and checked, D-525 "
                  "(withheld) states in full."),
        "D-565": (VERDICT_IN,
                  "Its verbatim rules that exact score ties are real and are broken by a declared "
                  "TOTAL order on paths — fewer segments first, then the earliest boundary-tick "
                  "sequence, then the canonical class-key order — with no epsilon.",
                  "Its first two keys decide where the boundaries fall when two readings score "
                  "equally, which is the ruled answer to the second limb at exactly the hardest "
                  "case."),

        # ── group C — Cross-cutting analysis contracts — 43 candidates — authored 2026-09-05 ──
        "D-022": (VERDICT_IN,
                  "Its verbatim rules the analysis works 'at the finest grain where harmony is "
                  "well-defined' and makes everything coarser a derived view; its plain names that "
                  "grain 'the smallest stretch over which the sounding harmony does not change'.",
                  "It states where a boundary falls — at a change in the sounding harmony — which "
                  "is the second limb in terms."),
        "D-023": (VERDICT_IN,
                  "Its verbatim names the atomic analysis unit 'the constant-sonority slice (L2), "
                  "never the metric beat'; its plain defines it as 'a stretch during which exactly "
                  "the same notes are sounding'.",
                  "It states the boundary rule itself: a boundary is where the sounding set "
                  "changes."),
        "D-024": (VERDICT_IN,
                  "Its verbatim rules L1 (notes) and L2 (slicing) 'style-agnostic and lossless — "
                  "they carry facts, never style', with style-specificity confined to the judgment "
                  "layers' calibration.",
                  "It rules that where one stretch ends is a fact read from the notes and never a "
                  "style-calibrated judgment, which is part of what evidence may decide a "
                  "boundary."),
        "D-025": (VERDICT_IN,
                  "Its verbatim rules the architecture FORWARD-ONLY; its plain says a confident "
                  "earlier answer could be overturned only by re-running that stretch forwards, and "
                  "that 'the one genuinely tangled key-versus-chord case got a narrow, gated "
                  "exception'.",
                  "It states how the tonality and the chord decisions relate and how either may be "
                  "revised, which bears on the first and fourth limbs."),
        "D-026": (VERDICT_IN,
                  "Its verbatim records that a subsequent investigation 'measured the full joint "
                  "cross-layer search INERT'; its plain says the effort was redirected into better "
                  "evidence flowing forwards.",
                  "It is a measured ruling on whether the reading is produced by one global joint "
                  "search, which bears on all four limbs at once."),
        "D-027": (VERDICT_IN,
                  "Its verbatim rules that each layer 'emits ranked candidates + a confidence, "
                  "never a forced point estimate'.",
                  "The charter has this layer publish the rivals with their mass, and this states "
                  "the ruled requirement that they be published at all."),
        "D-028": (VERDICT_OUT,
                  "Its verbatim bans the unqualified word 'region' as ambiguous and requires every "
                  "layer to name the span it operates on.",
                  "It bears on the span-naming vocabulary — which word names which stretch — and "
                  "states no rule about where any boundary falls."),
        "D-029": (VERDICT_OUT,
                  "Its verbatim rules preferring what can be verified against ground truth and, "
                  "where sound theory cannot be verified, building it with an alternative-confidence "
                  "path and an 'empirically-unvalidated' mark.",
                  "It bears on the verifiability contract governing what may be built and how it is "
                  "marked, not on what tonality, boundary, tone status or chord is read."),
        "D-030": (VERDICT_OUT,
                  "Its verbatim states the three binding scale requirements — cost scales with the "
                  "working span, re-analysis is incremental over the dirty span, the working span is "
                  "extensible.",
                  "It bears on the bounded-context contract's cost and incrementality requirements, "
                  "not on what is read from the music it loads."),
        "D-031": (VERDICT_OUT,
                  "Its verbatim states that whole-score analysis is the degenerate case, selection "
                  "equalling score.",
                  "It bears on the bounded-context contract's scope — how much music is analysed — "
                  "and settles none of the four limbs."),
        "D-032": (VERDICT_OUT,
                  "Its verbatim requires every confidence crossing a layer boundary to be in [0,1], "
                  "class-declared, and named to its decision.",
                  "It bears on the cross-layer confidence contract's FORM requirements, which "
                  "constrain how a value is published rather than what reading it belongs to."),
        "D-033": (VERDICT_IN,
                  "Its verbatim rules that each layer owns one evidence-source-by-question "
                  "contribution and that 'within its scope uses *all* the information L1 carries "
                  "losslessly (notated spelling, metric weight, voice)'.",
                  "It states what evidence this layer may bring to bear on every one of the four "
                  "limbs — all of the note model's information, not a narrowed subset."),
        "D-034": (VERDICT_OUT,
                  "Its verbatim admits a new layer or axis only when it clears three co-equal "
                  "gates, all required.",
                  "It bears on the criterion for admitting a new layer or axis to the architecture, "
                  "not on what any existing layer decides."),
        "D-035": (VERDICT_OUT,
                  "Its verbatim rules every cost-driving choice an explicit setting rather than a "
                  "hardcoded constant, and every optional expensive refinement a separable stage.",
                  "It bears on the effort control and the governance of cost, not on the reading."),
        "D-099": (VERDICT_IN,
                  "Its verbatim rules that 'a ruled-out reading is carried, not dropped' — published "
                  "on the output surface at low confidence unless the elimination is recomputable.",
                  "The charter has this layer publish the rivals with their mass including "
                  "boundary-differing rivals, and this states the ruled rule for carrying the "
                  "ruled-out ones."),
        "D-100": (VERDICT_OUT,
                  "Its verbatim rules every derived analytical fact published exactly once on the "
                  "producing layer's output surface, consumers reading and never re-deriving.",
                  "It bears on the fact-publication contract — where a fact lives and who may "
                  "re-derive it — not on what the fact says about the music."),
        "D-260": (VERDICT_OUT,
                  "Its verbatim states the invariant that the analysis output covers exactly the "
                  "selection and everything outside it is evidence, never a result.",
                  "It bears on the bounded-context contract's output scope, not on what is read "
                  "inside that scope."),
        "D-261": (VERDICT_OUT,
                  "Its verbatim rules that a layer never guesses how much context it needs and "
                  "stops on convergence — its in-selection output ceasing to change with further "
                  "context.",
                  "It bears on the bounded-context contract's extension and stopping rule, not on "
                  "what tonality, boundary, tone status or chord is read."),
        "D-262": (VERDICT_OUT,
                  "Its verbatim rules the extension increment set by the requesting layer in its "
                  "own inference scale, an efficiency knob only because convergence fixes the "
                  "result.",
                  "Same subject as D-261: it bears on the bounded-context contract's mechanics."),
        "D-264": (VERDICT_OUT,
                  "Its verbatim states the equivalence invariant — the result after any sequence of "
                  "extensions must equal a single fresh run over the final loaded span.",
                  "It bears on the bounded-context contract's correctness guard, not on what the "
                  "run reads."),
        "D-265": (VERDICT_OUT,
                  "Its verbatim rules the extension request a data-supply call DOWN to the note "
                  "layer, with inference then flowing forward and never backward.",
                  "It bears on the bounded-context contract and the forward-only control flow, not "
                  "on any of the four limbs."),
        "D-267": (VERDICT_OUT,
                  "Its verbatim declares exactly two admissible confidence classes — a decision "
                  "margin and a calibrated probability — and forbids claiming the second until a "
                  "reliability map is fitted.",
                  "It bears on the confidence contract's class vocabulary, not on what reading a "
                  "confidence belongs to."),
        "D-268": (VERDICT_OUT,
                  "Its verbatim states five rules of use — a confidence attaches to a named "
                  "decision, is bounded and class-declared at a layer boundary, is compared only "
                  "within one class and frame, keeps its identity, and abstention means below the "
                  "declared bar.",
                  "It bears on the confidence contract's rules of use; naming key-of-slice and "
                  "chord-of-slice as decisions does not state what either decides."),
        "D-278": (VERDICT_IN,
                  "Its verbatim records the joint key-and-chord step SHELVED, measured not to pay, "
                  "with the cause stated — 'the carried alternative keys are diatonic-collection "
                  "siblings so the chord is almost always key-stable'.",
                  "It is a measured verdict on coupling the tonality and the chord decisions, which "
                  "is directly about how the first and fourth limbs relate."),
        "D-282": (VERDICT_OUT,
                  "Its verbatim rules the oracle-and-tier measurement standing and forbids grading "
                  "on the bare bass-is-root proxy, which rewards a wrong root that happens to be "
                  "the bass.",
                  "It bears on how the analysis is graded — the measurement unit — not on what the "
                  "analysis reads."),
        "D-286": (VERDICT_OUT,
                  "Its verbatim records a measured A/B in which a bounded-window analysis beat a "
                  "whole-score interactive one against the published annotations, the whole-score "
                  "variant SHELVED and the bounded window adopted.",
                  "It bears on the analysis extent — how much music one reading is taken over — "
                  "which is the effort question and not one of the four limbs."),
        "D-288": (VERDICT_IN,
                  "Its verbatim forbids retrying a widened search and gives the reason: 'the wrong "
                  "reading is the highest-scoring one', so 'only changing how readings are scored, "
                  "or cutting the music differently, can move it'.",
                  "It names the two levers that decide the reading — the score and the "
                  "segmentation — and rules out the third, which is part of the answer's shape."),
        "D-289": (VERDICT_IN,
                  "Its verbatim records the meta-principle that 'precision lives in emission + "
                  "functional labeling, NOT search/path'.",
                  "It states a ruled steer about what determines the reading — the evidence each "
                  "candidate is judged on rather than the search over candidates."),
        "D-293": (VERDICT_IN,
                  "Its verbatim rules values fitted per IDIOM — one fit event per body of "
                  "repertoire sharing a practice — and never adjusted to make a named preset come "
                  "out right.",
                  "The charter assigns the fitting of this layer's values to its detail "
                  "specification, and this states the ruled unit of that fit."),
        "D-313": (VERDICT_OUT,
                  "Its verbatim rules calibration maps monotone or deferred, a non-monotone "
                  "empirical curve being an upstream finding rather than a mapping target.",
                  "It bears on the confidence-calibration contract — turning an internal number "
                  "into a probability — not on what reading that number belongs to."),
        "D-339": (VERDICT_IN,
                  "Its verbatim rules that a confident earlier inference is overturned by decisive "
                  "later evidence through ONE confidence-weighted forward-recompute mechanism, "
                  "naming the modulation recompute and the fine-grain chord override as instances.",
                  "Both named instances overturn a committed tonality or a committed chord, so the "
                  "rule states how the first and fourth limbs are finally settled."),
        "D-466": (VERDICT_IN,
                  "Its verbatim rules forward-only 'a strong *default*, not dogma', a sanctioned "
                  "backward edge admissible only as a deliberate, surfaced, measured, documented "
                  "exception.",
                  "It states the ruled condition under which this layer's reading may be revised "
                  "backwards, which bears on how every one of the four limbs is settled."),
        "D-474": (VERDICT_OUT,
                  "Its verbatim establishes a FACT-of-absence: no published study reports per-axis "
                  "inter-annotator agreement for Roman-numeral or key annotation of "
                  "Baroque/classical symbolic music.",
                  "It bears on the ground-truth ceiling (#21) and on what may be claimed about any "
                  "residual, not on what the analysis reads."),
        "D-475": (VERDICT_OUT,
                  "Its verbatim declares the BCMH chorale annotations unestablished as an "
                  "instrument — one annotator, annotations sitting on a homorhythmic reduction, "
                  "reached through a machine translation.",
                  "It bears on one corpus's establishment status under #19, not on any of the four "
                  "limbs."),
        "D-497": (VERDICT_OUT,
                  "Its verbatim requires the empirically-unvalidated mark applied to the Jazz preset "
                  "constants and to the idioms no gate-grade ground truth has calibrated, with the "
                  "validation path named beside each.",
                  "It bears on the marking and validation of style constants, not on what tonality, "
                  "boundary, tone status or chord is read."),
        "D-500": (VERDICT_OUT,
                  "Its verbatim records the user's ratification of CORPUS EXPANSION — gate-grade "
                  "jazz ground truth, chromatic material of the Wagner class, and more non-Bach, "
                  "non-Baroque annotated music.",
                  "It bears on the material the analysis is measured against, not on the reading "
                  "itself."),
        "D-521": (VERDICT_IN,
                  "Its verbatim states the general law by which an abstract circle becomes acyclic "
                  "in the concrete — the score already contains one side, a key-agnostic form of "
                  "the evidence exists, the dependency is on a coarser stable fact, or the ratified "
                  "forward-override covers the rare remainder.",
                  "Its own plain names the circle as key, chord, cadence and non-chord tones "
                  "needing one another, so it states how the mutual dependency of the first, third "
                  "and fourth limbs is resolved."),
        "D-522": (VERDICT_OUT,
                  "Its verbatim makes 'show me why' a late-bound DISPLAY consumer of facts that "
                  "already exist rather than a new analysis, the gap being publication.",
                  "It bears on the explainability display surface, not on what the analysis "
                  "decides."),
        "D-531": (VERDICT_IN,
                  "Its verbatim records the standing verdict that the hand-built analysis is "
                  "CONFIRMED and the learned replacement NOT triggered, retained as an explicit "
                  "fallback re-opening 'for any slice later established as a genuine ceiling'.",
                  "It states the ruled answer to what kind of thing scores a candidate reading, "
                  "which the charter assigns to this layer's detail specification."),
        "D-576": (VERDICT_OUT,
                  "Its verbatim states that a chord's root and bass are largely key-independent, so "
                  "the root-agreement percentage barely moves when the tonality is misread while "
                  "quality, Roman numeral and some inversions are corrupted.",
                  "It bears on how a published measurement figure must be read, not on what the "
                  "analysis reads from the music."),
        "D-600": (VERDICT_IN,
                  "Its verbatim records that two post-scoring passes change the chord quality the "
                  "scorer committed and keep no record of what they replaced, and rules the "
                  "violation TOLERATED until the gate-dissolution step.",
                  "It states that the committed chord's quality is overwritten downstream, which is "
                  "a ruled fact about what chord is read over a span."),
        "D-601": (VERDICT_OUT,
                  "Its verbatim hard-gates the fitting of a conversion constant between two "
                  "differently-scaled confidences behind a premise ledger and a desk simulation.",
                  "It bears on the confidence contract's comparison frames and on the Premise Gate, "
                  "not on any of the four limbs."),
        "D-656": (VERDICT_OUT,
                  "Its verbatim forbids amending the crediting rule so that a tonicization label "
                  "counts as agreeing with the annotator's modulated numeral, only a diagnostic "
                  "partial-sub-split being defensible.",
                  "It is the MEASUREMENT half of its decision and bears on the grading convention; "
                  "the build half it names is homed elsewhere and is not in this text."),

        # ── group D — Layer 1 — the note model — 2 candidates — authored 2026-09-05 ──
        "D-569": (VERDICT_OUT,
                  "Its verbatim confines the collection layer to collecting every sounding note, "
                  "annotated and lossless, and forbids it to filter, weight, select a bass, or make "
                  "'any harmonic/segmentation/key decision'.",
                  "It bears on the note-model unit — what the collection layer does and does not "
                  "do — and its only mention of the tonal reading is to exclude it from that "
                  "layer."),
        "D-625": (VERDICT_OUT,
                  "Its verbatim rules spelling presence tested with the validity predicate and "
                  "never with a non-negative test, because the flat side of the line of fifths is "
                  "negative.",
                  "It bears on the note model's spelling representation and its presence test, not "
                  "on what tonality, boundary, tone status or chord is read."),

        # ── group E — Layer 2 — the slicer — 1 candidate — authored 2026-09-05 ──
        "D-605": (VERDICT_IN,
                  "Its verbatim rules that a local-key hypothesis derives from KEY-AGNOSTIC signals "
                  "only and NEVER from the key-area grouping, and states its own scope: 'what it "
                  "constrains is *what evidence a modulation decision may read*, which binds any "
                  "such decision on any arm'.",
                  "It states what evidence a change-of-tonality decision may read, which is the "
                  "first limb — the pilot graded it OUT because its one-limbed question was the "
                  "chord boundary alone, and that reason does not reach the four-limbed question."),

        # ── group F — Layer 3 — key and mode — 24 candidates — authored 2026-09-05 ──
        "D-057": (VERDICT_IN,
                  "Its verbatim IS the priority-of-evidence table's strongest row — 'Strongest | "
                  "Actual sounding notes | what is literally happening now'; its plain ranks the "
                  "sounding notes above the surrounding bars, the signature and its mode tag.",
                  "It states the ruled ranking of the evidence that decides the tonality at each "
                  "moment, which is the first limb; it is also the pilot's own first withheld "
                  "identity."),
        "D-306": (VERDICT_IN,
                  "Its verbatim rules that the key layer's backward re-reading facility 'stays "
                  "SWITCHED OFF in the shipped configuration', built with `enabled = false` as the "
                  "shipped default.",
                  "It states whether the tonality reading may return to an earlier stretch once "
                  "later evidence arrives, which is part of the ruled answer to the first limb."),
        "D-323": (VERDICT_IN,
                  "Its verbatim forbids reintroducing `keyTonicPc + scale` for a membership test — "
                  "a membership question reads the key signature's own collection, while a "
                  "scale-DEGREE question legitimately uses the tonic.",
                  "It states how 'does this pitch belong to the key' is answered, which is a term "
                  "of the tonality decision and of the chord read against it."),
        "D-343": (VERDICT_IN,
                  "Its verbatim gives the key/mode layer the candidate space and the note-evidence "
                  "model outright, with the residual the notes cannot decide handed forward as "
                  "ranked alternatives and SELECTED later, never re-scored.",
                  "It states where the tonality is inferred from the notes, what the candidate "
                  "space is, and how the undecidable residual is settled — the first limb in "
                  "full."),
        "D-344": (VERDICT_IN,
                  "Its verbatim rules that any scale outside the twenty-one recognized modes — "
                  "pentatonic, blues, whole-tone, octatonic, non-Western — is reported as the "
                  "best-fitting recognized mode and never as the unrecognized scale.",
                  "It states what tonality is emitted for music the vocabulary does not contain, "
                  "which is the first limb's answer at its edge."),
        "D-345": (VERDICT_IN,
                  "Its verbatim makes the key/mode layer the first place the style preset is used, "
                  "as a deliberately weak per-mode prior the note evidence overrides.",
                  "It states what the preset contributes to the tonality at each moment and how "
                  "strongly, which is part of the first limb's ruled answer."),
        "D-347": (VERDICT_IN,
                  "Its verbatim fixes the change cost as cheap-to-stay plus a term growing with key "
                  "distance plus a large relative-pair penalty, rejecting a single flat margin.",
                  "It states what decides where one tonality gives way to the next, which is the "
                  "first limb's own segmentation."),
        "D-348": (VERDICT_IN,
                  "Its verbatim measures tonal distance as circle-of-fifths (key-signature) "
                  "distance, not semitone distance and not differing scale tones, and states that "
                  "there is NO duration threshold for brief-versus-sustained at all.",
                  "It states the metric inside the tonality change cost and denies the duration "
                  "rule a reader would expect, both part of the first limb's answer."),
        "D-349": (VERDICT_IN,
                  "Its verbatim defines the confidence as how much better the winning sequence is "
                  "than the best different-key sequence at that stretch, explicitly not the gap "
                  "between the top two candidates there.",
                  "It states that the tonality decision is over whole readings rather than one "
                  "moment, and what the published confidence on it measures."),
        "D-351": (VERDICT_IN,
                  "Its verbatim adopts a dedicated best-sequence decoder for key/mode and records "
                  "reusing the existing chord decoder as considered and rejected.",
                  "It states how the run of tonalities is searched and that the chord decoder is "
                  "not what searches it, which bears on the first limb and on its relation to the "
                  "fourth."),
        "D-352": (VERDICT_OUT,
                  "Its verbatim states the grading bar's partition — unambiguous where the "
                  "annotation gives one local key with no alternative and the analyses agree, "
                  "genuinely ambiguous otherwise — and what the bar is on each side.",
                  "It bears on how the key/mode layer is GRADED against the published annotations, "
                  "not on what tonality it reads."),
        "D-353": (VERDICT_OUT,
                  "Its verbatim keeps two quality goals apart — accuracy on the resolvable cases, "
                  "and calibration of the uncertainty mark on the genuinely ambiguous ones — the "
                  "second graded in its own right.",
                  "Same subject as D-352: it bears on the measurement of the key/mode layer rather "
                  "than on the reading."),
        "D-494": (VERDICT_IN,
                  "Its verbatim requires key-confirmation channels that do NOT require a cadence — "
                  "sustained dominant emphasis and recognized transposition sequences — plus an "
                  "enharmonic-identity rule for key spans, because on resolution-denying music the "
                  "cadence-confirmed gate almost never fires.",
                  "It states what may confirm a change of tonality, which is the first limb's own "
                  "admission rule."),
        "D-571": (VERDICT_IN,
                  "Its verbatim reduces the declared-mode influence to a small additive hint whose "
                  "smallness IS the gate — it can only flip the winner where the raw note-based gap "
                  "is already narrow, so no separate confidence test is added.",
                  "It states the strength and the firing condition of the declared mode's "
                  "contribution to the tonality at each moment."),
        "D-572": (VERDICT_IN,
                  "Its verbatim records the hard post-hoc declared-mode promotion — which moved the "
                  "best declared-compatible result to the front REGARDLESS of the candidate-score "
                  "gap — REMOVED OUTRIGHT rather than kept in a gated form.",
                  "It states what the declared mode may no longer do to the tonality decision, "
                  "which is exclusion evidence about the first limb's ruled answer."),
        "D-575": (VERDICT_IN,
                  "Its verbatim handles the Baroque partial-signature convention by DETECTING it — "
                  "the flattened sixth degree pervasive and dominating its natural form — and "
                  "reinterpreting the written signature one step, never by widening the candidate "
                  "family for every score.",
                  "It states how a whole class of notation is turned into a tonality reading, which "
                  "is the first limb."),
        "D-587": (VERDICT_OUT,
                  "Its verbatim rules that a preset presents as a familiar genre-era label plus "
                  "exemplars the user knows, never as an idiom name, genre names being LABELS over "
                  "mixtures rather than axes.",
                  "It bears on how a preset is presented to the user and on the style taxonomy's "
                  "structure, not on what tonality, boundary, tone status or chord is read."),
        "D-588": (VERDICT_OUT,
                  "Its verbatim gives preset coverage three tiers with no bare guessing — measured, "
                  "editorially declared with a stated theory rationale, or self-correcting by "
                  "detection.",
                  "It bears on the style system's coverage and validation tiers, not on the "
                  "reading."),
        "D-589": (VERDICT_OUT,
                  "Its verbatim makes every idiom mixture selectable and the discovered cloud the "
                  "EVIDENCE MAP rather than the boundary, each chosen point carrying its evidence "
                  "status.",
                  "It bears on the style system's user configuration and on what may be claimed "
                  "about a chosen mixture, not on any of the four limbs."),
        "D-590": (VERDICT_OUT,
                  "Its verbatim makes the score's own user-defined properties the PRIMARY home of "
                  "that score's idiom mixture, a user-set mixture never silently overwritten by "
                  "re-detection.",
                  "It bears on where a per-piece style setting is stored and how it is refreshed, "
                  "not on the reading."),
        "D-591": (VERDICT_OUT,
                  "Its verbatim splits the licence constraint — the per-idiom ANCHORS are shipped "
                  "fitted parameters and reached by it, the mixture weights are free user "
                  "configuration and are not.",
                  "It bears on licensing and on which half of the style system the fitting-pool "
                  "constraint reaches, not on what is read from the music."),
        "D-598": (VERDICT_OUT,
                  "Its verbatim makes the taxonomy and the per-style weights ONE data-derived "
                  "object and VALIDATION a separate third job the clustering does not deliver.",
                  "It bears on the style taxonomy's derivation and validation, not on any of the "
                  "four limbs."),
        "D-616": (VERDICT_IN,
                  "Its verbatim rules that a global tonic anchor enters key scoring at "
                  "RESOLVER/SECTION scope and never as one more local term inside the window "
                  "scorer, because a local term strong enough to win the relative-pair near-ties "
                  "also overrides the correct reading where the mode is present.",
                  "It states where section-scoped evidence about the tonality may be applied and "
                  "where it may not, which is the first limb."),
        "D-622": (VERDICT_IN,
                  "Its verbatim records the reach-back convergence PROXY measured FALSE and "
                  "dropped: the as-built tracks the leading-edge key itself and stops when that "
                  "stops changing, one settled indication not anchoring the leading edge.",
                  "It states what quantity the tonality reading watches when it reads backwards and "
                  "when it stops, which is part of the first limb's ruled answer."),

        # ── group G — Layer 4 — chord identity — 33 candidates — authored 2026-09-05 ──
        "D-207": (VERDICT_IN,
                  "Its verbatim defines the pedal-point class VOICE-INDEPENDENTLY — a tone "
                  "sustained or continuously restruck against changing harmony in any voice, "
                  "sub-labeled bass, internal or inverted.",
                  "It states which sounding notes are read as standing outside the moving harmony, "
                  "which is the third limb."),
        "D-280": (VERDICT_IN,
                  "Its verbatim rules that a gate or scoring rule reads STRUCTURED FIELDS ONLY — "
                  "never a chord-symbol string, never a Roman numeral — because signals derived "
                  "from either are lossy and entangled with the formatter.",
                  "It states what evidence chord classification may and may not take as input, "
                  "which is part of the fourth limb's ruled answer."),
        "D-284": (VERDICT_IN,
                  "Its verbatim records selection and competition SATURATED — stop adding "
                  "re-ranking heuristics and gates — with the residual named as candidate "
                  "generation, key quality, or floor.",
                  "It states where the chord reading's remaining error lives and which lever is "
                  "exhausted, which bears on the first and fourth limbs."),
        "D-317": (VERDICT_IN,
                  "Its verbatim closes the backward-walk boundary change — counting notes that stop "
                  "exactly where a stretch begins as belonging to that stretch — and gives the "
                  "measured reason at the boundary itself, that those notes are OTHER chord tones "
                  "and the root attacks later.",
                  "It rules on how a note's release relates to a boundary and to chord membership, "
                  "which is the second and third limbs together."),
        "D-318": (VERDICT_IN,
                  "Its verbatim closes a short-region external merger — measured, its trigger never "
                  "fires because the same-root merge inside the first pass has already combined "
                  "those stretches.",
                  "It rules on whether short neighbouring stretches may be merged after the fact, "
                  "which is the second limb."),
        "D-319": (VERDICT_IN,
                  "Its verbatim closes every tone-aggregation approach to the arpeggio root "
                  "failure: pooling an arpeggio's notes and re-reading the chord from the pool was "
                  "measured worse, the wrong pitch sounding longer than the right one.",
                  "It rules on whether a chord may be read from notes pooled across a stretch, "
                  "which is the second and fourth limbs together."),
        "D-320": (VERDICT_IN,
                  "Its verbatim reverts the absent-root guard entirely and states the premise false "
                  "corpus-wide — 'an absent root means a wrong reading' is contradicted by readings "
                  "the published human analysis itself makes with an absent root.",
                  "It rules on what chord may be read over a span whose root does not sound, which "
                  "is the fourth limb."),
        "D-321": (VERDICT_IN,
                  "Its verbatim rules winner selection by exact double comparison with no epsilon "
                  "anywhere, exact ties broken by template index then root pitch class.",
                  "It states how the chord read over a span is chosen among scored candidates, "
                  "which is the fourth limb."),
        "D-322": (VERDICT_OUT,
                  "Its verbatim requires a full corpus A/B on both presets before any change to "
                  "optimization flags or to the order of the scoring arithmetic is trusted.",
                  "It bears on the verification obligation attached to a build-level change, not on "
                  "what tonality, boundary, tone status or chord is read."),
        "D-324": (VERDICT_OUT,
                  "Its verbatim rules retirement of a post-scoring rule GLOBAL — a rule live on any "
                  "one carrier is retained for all.",
                  "It bears on how the correction-rule population may change, not on what any rule "
                  "decides about the music."),
        "D-325": (VERDICT_IN,
                  "Its verbatim rules that a correction able to change a committed chord's root, "
                  "quality or bass is retired or folded into the scoring BEFORE the search is "
                  "widened past it, because such a rule feeds the backward-looking evidence.",
                  "It states that a later rule can change which chord was committed and what must "
                  "happen before the search widens, which bears on the fourth limb."),
        "D-326": (VERDICT_IN,
                  "Its verbatim rules that the chord-path search emits the WHOLE PATH with every "
                  "stretch's alternatives and its margins, not the committed reading alone, because "
                  "the layer above consumes the alternatives.",
                  "The charter has this layer publish the rivals with their mass, and this states "
                  "the ruled content of that publication."),
        "D-327": (VERDICT_IN,
                  "Its verbatim rules the root-continuity guard reading the RECONSTRUCTED inversion "
                  "credit rather than testing directly whether the candidate's third is sounding — "
                  "the two agreeing everywhere except on diminished chords.",
                  "It states a term inside the decision of what chord is read over a span, and what "
                  "sounding evidence stands behind it."),
        "D-329": (VERDICT_IN,
                  "Its verbatim makes COMPLETENESS the priority — every tertian chord the slice's "
                  "pitches could spell is listed before any is chosen, because 'a chord never "
                  "listed can never be chosen'; its plain records the principle transferred to the "
                  "live joint estimator as its admission premise.",
                  "The charter puts the rule admitting a candidate to the search inside this "
                  "layer's specification, and this states it."),
        "D-330": (VERDICT_IN,
                  "Its verbatim is 'the authoritative statement of this prohibition' — never a "
                  "pooled recompute; membership is judged per slice against the prevailing chord, "
                  "because pooling over-reads and treats every passing note as a chord tone.",
                  "It states how a note's membership of the harmony is decided and over what "
                  "stretch, which is the third limb."),
        "D-331": (VERDICT_IN,
                  "Its verbatim carries the ranked alternatives and the confidence on EVERY "
                  "decision — commit and inherit included, filled before the trichotomy and never "
                  "pruned — so the layer above overrides by selecting among them.",
                  "It states the ruled completeness of the rivals this layer publishes."),
        "D-380": (VERDICT_IN,
                  "Its verbatim makes DISTINCT ROOTS the carry's meaningful axis and requires every "
                  "above-threshold distinct root carried at graded confidence with ruled-out roots "
                  "kept at low confidence, a third distinct root clearing threshold on about a "
                  "quarter of slices.",
                  "It states what the rivals published for each span are and on what axis they "
                  "differ."),
        "D-381": (VERDICT_IN,
                  "Its verbatim requires the carry to cap on DISTINCT ROOTS with each root's "
                  "variant depth bounded, rather than on a flat voicing list which gives no "
                  "structural guarantee that a third root survives.",
                  "It states the ruled shape of the rivals this layer publishes, which the charter "
                  "assigns to it."),
        "D-385": (VERDICT_IN,
                  "Its verbatim homes pedal-point detection as a reader over the chord layer's "
                  "carry emitting an additive pedal ANNOTATION on a carried reading, never a "
                  "mutation of the winner; its plain states the pedaled note may be in any voice.",
                  "It states how a sustained note read as standing outside the harmony is recorded "
                  "and that the chord reading is not replaced by it — the third and fourth limbs."),
        "D-386": (VERDICT_IN,
                  "Its verbatim states that the pedal reader consumes the carry's own distinct-root "
                  "margin and adds no further scan, and that 'the ≥2nd distinct root's carried "
                  "confidence *is* the pedal confirmation signal'.",
                  "It names the evidence that confirms a note is read as a pedal rather than a "
                  "chord tone, which is the third limb."),
        "D-423": (VERDICT_OUT,
                  "Its verbatim states three prohibitions holding through every stage — no new "
                  "gates, no threshold widening, no gating of the root-continuity bonus — and makes "
                  "the per-gate retirement stage the only sanctioned channel of change.",
                  "It bears on how the post-scoring gate population may change, not on what those "
                  "gates decide about the music."),
        "D-463": (VERDICT_IN,
                  "Its verbatim records that several signals looking backward or forward in time "
                  "are computed inside the part of the scorer meant to judge one moment, and that "
                  "Gate R's test uses a score component as a stand-in for 'this candidate has a "
                  "sounding third'.",
                  "It states what evidence actually stands behind a term that decides the chord "
                  "read over a span, which is the fourth limb."),
        "D-464": (VERDICT_OUT,
                  "Its verbatim forbids adding any further progression-level signal to the "
                  "single-step look-around structure and plans the migration of four such fields to "
                  "the progression-level structure.",
                  "It bears on where a signal is stored — a structure boundary and its migration — "
                  "not on what any signal decides."),
        "D-465": (VERDICT_IN,
                  "Its verbatim gives three tests for a proposed gate, naming the scorer's "
                  "bass-as-root pull as the bias two thirds of the gates were correcting, a "
                  "structural pitch-class condition as likely sound, and a three-step cascade as a "
                  "signal that the real problem is missing functional context.",
                  "It states the diagnosed failure structure of the chord reading and which kind of "
                  "evidence resolves it, which bears on the fourth limb."),
        "D-467": (VERDICT_IN,
                  "Its verbatim forbids a rebuilt or re-tuned chord scoring from relying on the "
                  "held-note repetition bonus the faithful note model removed — a tie-held note "
                  "counted more than once had been pushing a handful of ambiguous sonorities toward "
                  "the correct root.",
                  "It states a constraint on what evidence may carry the chord reading, and names "
                  "an artifact that must not."),
        "D-501": (VERDICT_IN,
                  "Its verbatim rules a written chord symbol readable ONLY as a comparison or "
                  "ground-truth label — production paths must not read symbols as input to analysis "
                  "at all, since a symbol is user content and may be wrong.",
                  "It states what the chord read over a span may not be derived from, which is part "
                  "of the fourth limb's ruled answer."),
        "D-510": (VERDICT_IN,
                  "Its verbatim rules the correct carry the one that KEEPS the distinct alternative "
                  "reading, the append idiom having been measured to inject a near-copy of the "
                  "winner and displace the genuinely different partner.",
                  "It states what the rivals this layer publishes must contain, which the charter "
                  "assigns to it."),
        "D-511": (VERDICT_IN,
                  "Its verbatim rules ONE promotion primitive with a present-first dedup guard, the "
                  "append branch firing only when the target is genuinely absent so no duplicate "
                  "can enter the carry.",
                  "It states how the published rivals are kept free of a duplicate of the winner, "
                  "which is a rule about the carry's content."),
        "D-512": (VERDICT_OUT,
                  "Its verbatim makes byte-for-byte reproduction of the carry the retirement "
                  "condition for a separate rule, and records that winner-only inertness was not "
                  "enough because the carry changed on a named subset.",
                  "It bears on the retirement condition for a rule and on the verification standard "
                  "(#15) — inertness on the full output surface — not on what is read."),
        "D-536": (VERDICT_IN,
                  "Its verbatim rules the bass and the chord chosen TOGETHER as one (bass, root, "
                  "template) triple, replacing a pipeline that committed the bass first, because a "
                  "passing note that is the absolute lowest pitch was winning bass selection and "
                  "flipping the root.",
                  "It states how the chord read over a span is decided and what it is decided "
                  "jointly with, which is the fourth limb."),
        "D-537": (VERDICT_IN,
                  "Its verbatim fires the completeness bonus ONLY for a root-position reading whose "
                  "three triad tones are all above the presence threshold, so a genuine slash chord "
                  "neither gains it nor is beaten by a rival that gains it wrongly.",
                  "It states a term deciding what chord is read over a span, with its structural "
                  "entry condition."),
        "D-538": (VERDICT_OUT,
                  "Its verbatim orders a multi-signal scoring change landed one signal at a time, "
                  "the corpus check re-run after each step and no step allowed to increase the "
                  "error count.",
                  "It bears on the landing and validation procedure for a change, not on what the "
                  "changed scoring decides."),
        "D-580": (VERDICT_IN,
                  "Its verbatim separates two purely-local VERTICAL refinements that must survive "
                  "the dissolution from the ten gates that 'read context from beyond their own "
                  "stretch and are compensation by construction'.",
                  "It states which corrections refine the reading from the notes of one stretch and "
                  "which exist only because the decision before them could not see enough, which "
                  "bears on the second and fourth limbs."),

        # ── group B — The notation output surface and the record path — 4 candidates — authored 2026-09-05 ──
        "D-010": (VERDICT_IN,
                  "Its verbatim flips `useJointNotationRecord`'s default to ON; its plain states "
                  "that the harmony seen inside the program 'is produced by the joint estimator', "
                  "the old path compiled but reachable only by turning the new one off.",
                  "It names which mechanism produces the reading on the in-app surface — one joint "
                  "estimator rather than a staged path — which is the shape of the ruled answer, on "
                  "the same ground as D-005."),
        "D-275": (VERDICT_OUT,
                  "Its verbatim requires every published record to carry its instrument provenance "
                  "— the embedded table set's source-artifact hashes, the selected weight-vector "
                  "identity, the decoder's version — so a provenance-less analysis cannot exist.",
                  "It bears on the notation record's provenance requirement, which says which "
                  "fitted values produced an analysis rather than what that analysis reads."),
        "D-276": (VERDICT_IN,
                  "Its verbatim publishes modal colour as un-rounded per-degree counts of every "
                  "chromatic inflection actually observed, and rules that 'no 21-value mode label "
                  "is inferred or published anywhere', the two-mode key plus this table dominating "
                  "the retired labels.",
                  "It states what the tonality reading emits and what it may not emit, which is the "
                  "first limb's ruled answer at its output."),
        "D-425": (VERDICT_IN,
                  "Its verbatim rules that the uncertainty surface's contract IS the full "
                  "posterior, the local-slice form being the first delivered step and a strict "
                  "subset of it, with the completion a named rowed step rather than an indefinite "
                  "upgrade.",
                  "The charter has this layer publish the rivals with their mass, and this states "
                  "that the ruled content of that publication is the whole distribution over "
                  "readings."),

        # ── group H — Layer 5 and Layer 6 — function, cadence, grouping — 47 candidates — authored 2026-09-05 ──
        "D-291": (VERDICT_IN,
                  "Its verbatim leaves the applied-chord labeller deliberately unwired and names "
                  "'THE REAL LEVER IS AT THE KEY LAYER'; its plain says the annotator has changed "
                  "key and labelling the chord against the old one hides that.",
                  "It states that the class of error is a tonality error and that the lever is the "
                  "key reading, which is a steer about the first limb."),
        "D-335": (VERDICT_IN,
                  "Its verbatim rules the Roman numeral the complete, precise analysis and the "
                  "tonic/subdominant/dominant summary a derived read-out that is lossy to store as "
                  "a primary output.",
                  "The chord this layer reads over a span IS a Roman numeral under D-526, so this "
                  "states what form the fourth limb's answer takes and what is merely derived from "
                  "it."),
        "D-336": (VERDICT_IN,
                  "Its verbatim rules cadence detection key-agnostic and voting FOR the key rather "
                  "than reading a resolved one, the prior key-dependent detector rejected as "
                  "circular.",
                  "It states that cadence evidence votes for the tonality and may not read one, "
                  "which is what evidence the first limb may use."),
        "D-337": (VERDICT_IN,
                  "Its verbatim rules tonicization the default and modulation requiring cadence "
                  "confirmation plus persistence expressed as a change-cost, rejecting a "
                  "fixed-duration rule and rejecting resolution in the key layer.",
                  "It states when the tonality changes and when instead an applied chord is "
                  "written, which is the first limb and the fourth together."),
        "D-338": (VERDICT_IN,
                  "Its verbatim rules that the layer SELECTS among the chord layer's carried "
                  "readings and never re-derives, re-scoring the slice from the notes being "
                  "rejected as the lower layer's job.",
                  "It states how a chord left open over a span is finally settled, and that it is "
                  "settled by selection among carried rivals rather than by re-reading the notes."),
        "D-341": (VERDICT_IN,
                  "Its verbatim completes the licensed root-motion set by theory — adding the "
                  "ascending fifth, the descending second and the diatonic diminished fifth — and "
                  "calls it algorithmic completion per theory, not tuning.",
                  "It states the content of the chord-succession evidence a reading is judged "
                  "against, which is a term of the fourth limb."),
        "D-382": (VERDICT_IN,
                  "Its verbatim rules selection by JOINT CONSISTENCY across key, root, inversion "
                  "and bass rather than by maximizing any single score, reasoning over the graded "
                  "distinct-root distribution including the exclusion tail.",
                  "It states how the tonality and the chord are chosen together over the carried "
                  "rivals, which is the first and fourth limbs at once."),
        "D-383": (VERDICT_IN,
                  "Its verbatim re-orders the resolver so that bass and inversion, spelling and "
                  "key-consistency are the primary channels and a licensed progression is only the "
                  "tie-break among mutually-consistent readings.",
                  "It ranks the evidence that decides the chord over a span and demotes one channel "
                  "explicitly, which is the fourth limb's ruled answer in part."),
        "D-384": (VERDICT_IN,
                  "Its verbatim rules that re-ranking the key under chord evidence is a DISTINCT "
                  "step and not the function layer's selection, which 'reasons within a *fixed* "
                  "region key'.",
                  "It states where the coupling of the tonality and the chord lives and where it "
                  "does not, which is directly about the first and fourth limbs' relation."),
        "D-387": (VERDICT_IN,
                  "Its verbatim unifies the contradiction into one structured open mark carrying "
                  "its kind, and rules that in the contradiction case 'the reading stays the L4 "
                  "commit' with the contradiction carried as calibrated uncertainty.",
                  "It states that the committed chord over a span survives a functional "
                  "contradiction and how that disagreement is published, which is the fourth limb."),
        "D-388": (VERDICT_OUT,
                  "Its verbatim adopts motion-type-led features for texture, the interval-profile "
                  "view being measured weaker and partly a chordal-density artifact.",
                  "It bears on the voice-leading dimension's texture classification, a different "
                  "axis from the tonal reading."),
        "D-389": (VERDICT_OUT,
                  "Its verbatim keeps a notated voice (a fact) and an inferred stream (a judgment) "
                  "as separate types, never conflated.",
                  "It bears on the voice-leading dimension's two-tier voice model."),
        "D-390": (VERDICT_OUT,
                  "Its verbatim classifies texture at whole-selection granularity in the first "
                  "version, a per-span claim being assumption-based until a named measurement runs.",
                  "It bears on the voice-leading dimension's texture classification scope."),
        "D-391": (VERDICT_IN,
                  "Its verbatim licenses harmonic layers to consume voice-leading FACTS freely — "
                  "naming 'the future L4 non-chord-tone filter' — because facts depend on no "
                  "harmonic inference, with the converse read admissible only where the combined "
                  "graph stays acyclic.",
                  "It states what evidence a chord-tone decision may take from the other axis, "
                  "which bears on the third limb."),
        "D-392": (VERDICT_OUT,
                  "Its verbatim makes the later voice-leading components claims with owners rather "
                  "than builds, each clearing its own design and footing first.",
                  "It bears on the voice-leading dimension's build gating."),
        "D-393": (VERDICT_OUT,
                  "Its verbatim requires the texture stage to publish the committed class plus the "
                  "full ranked list of all class fits with their weights.",
                  "It bears on the voice-leading dimension's own output contract; the "
                  "carried-alternatives discipline it cites is stated for this layer elsewhere."),
        "D-394": (VERDICT_OUT,
                  "Its verbatim makes reduction of a chord-bearing voice to one line a declared, "
                  "uniform, per-query parameter, the first version providing top-note only.",
                  "It bears on the voice-leading dimension's line extraction."),
        "D-395": (VERDICT_OUT,
                  "Its verbatim names three floors governing abstention — evidential, margin and "
                  "fit — the fit floor letting a span resembling no reference class abstain.",
                  "It bears on the voice-leading dimension's texture abstention."),
        "D-396": (VERDICT_OUT,
                  "Its verbatim declares the axis covering notated music only, its style coordinate "
                  "UNDEFINED rather than zero for sources that carry no voices.",
                  "It bears on the voice-leading dimension's coverage declaration."),
        "D-397": (VERDICT_OUT,
                  "Its verbatim assigns four previously ownerless analysis objects — the stock "
                  "patterns, the melodic phrase, chord voicing, part-writing advice — to the "
                  "voice-leading axis as CLAIMS rather than as work started.",
                  "It bears on ownership assignment across the voice-leading dimension."),
        "D-398": (VERDICT_OUT,
                  "Its verbatim rules 'interval preserved' semitone-exact, so a same-direction move "
                  "whose semitone interval changes counts as similar rather than parallel motion.",
                  "It bears on the voice-leading dimension's motion-type definition."),
        "D-400": (VERDICT_OUT,
                  "Its verbatim admits a PER-VOICE span kind to the typology because melodic "
                  "phrases run concurrently and out of step across voices and tile only within one "
                  "voice.",
                  "It bears on the span typology's admission of a phrase span kind, not on where "
                  "one harmony gives way to the next."),
        "D-419": (VERDICT_OUT,
                  "Its verbatim states that until the recognition consumer is built the function "
                  "layer makes NO use of the progression catalog — the connection absent, not "
                  "partial.",
                  "It bears on the declared dormancy of the link between the function layer and the "
                  "harmonic vocabulary."),
        "D-454": (VERDICT_OUT,
                  "Its verbatim gives the grouping layer NO detection of its own — it assembles the "
                  "punctuation-span segmentation, the key-area grouping and the cadence alignment "
                  "and hosts read-through carries.",
                  "It bears on the grouping layer's scope, and states in terms that the material it "
                  "assembles was decided elsewhere."),
        "D-455": (VERDICT_OUT,
                  "Its verbatim aligns cadences to punctuation-spans asymmetrically and surfaces an "
                  "off-boundary cadence as internal rather than snapping it to the nearest "
                  "boundary.",
                  "It bears on cadence-to-grouping alignment in the grouping layer, whose spans are "
                  "a different kind from the harmonic span."),
        "D-456": (VERDICT_OUT,
                  "Its verbatim keeps sections, periods and sentences out of the grouping layer's "
                  "core for PROPORTIONALITY and states explicitly that they are not disqualified "
                  "for lacking an oracle.",
                  "It bears on the grouping layer's scope and on the verifiability contract's "
                  "application to it."),
        "D-457": (VERDICT_OUT,
                  "Its verbatim marks a group whose edge is the selection edge "
                  "`clipped-by-selection-edge`, and tags an unclosed edge span with an "
                  "`extension-cue` the grouping layer only surfaces.",
                  "It bears on the grouping layer's edge handling and on who acts on a "
                  "bounded-context extension cue."),
        "D-459": (VERDICT_OUT,
                  "Its verbatim makes the key-area confidence a Class-M boundary confidence under "
                  "the cross-layer contract whose input is the declared key confidence rather than "
                  "the grading diagnostics' sigmoid.",
                  "It bears on the grouping layer's published confidence and on the confidence "
                  "contract, not on what tonality is read."),
        "D-460": (VERDICT_OUT,
                  "Its verbatim reports a punctuation-span fully resolved when and only when no "
                  "unit in it carries an open mark — 'no confidence threshold is involved' — the "
                  "grouping layer never resolving one.",
                  "It bears on how the grouping layer reports an earlier layer's residual, and says "
                  "in terms that it resolves nothing."),
        "D-461": (VERDICT_OUT,
                  "Its verbatim makes the grouping layer a deliberate EXPLAINABILITY layer rather "
                  "than an accuracy requirement, competitive systems reaching Roman-numeral "
                  "accuracy with no explicit grouping layer at all.",
                  "It bears on the grouping layer's proportionality and purpose."),
        "D-462": (VERDICT_OUT,
                  "Its verbatim scopes cadence validation to LOCATION against the annotated oracle, "
                  "cadence TYPE being harmony-dependent and only partially attributable and never a "
                  "clean gate.",
                  "It bears on how cadence detection is validated — a measurement scoping — not on "
                  "what the analysis reads."),
        "D-472": (VERDICT_OUT,
                  "Its verbatim groups key areas by a smoothing pass and lets a disagreeing region "
                  "keep its own key reading while being grouped into the enclosing area; it states "
                  "of itself that it 'is a grouping rule and not a second key analysis — it reads "
                  "the key fields the earlier layers already published rather than re-deciding "
                  "them'.",
                  "The entry settles its own subject as grouping over an already-published key "
                  "sequence, so it bears on the key-area grouping rather than on the tonality "
                  "decision."),
        "D-476": (VERDICT_OUT,
                  "Its verbatim owns the phrase-boundary primitive at the notation-derived view "
                  "layer, rejecting the note model and rejecting the function layer that consumes "
                  "phrase boundaries.",
                  "It bears on the ownership of the phrase-boundary primitive, a different span "
                  "kind from the harmonic span."),
        "D-477": (VERDICT_OUT,
                  "Its verbatim reads a phrase boundary from the written surface alone — never from "
                  "a resolved key, a chord reading or a cadence — accepting that boundaries marked "
                  "only harmonically are missed and recovered downstream.",
                  "It bears on the phrase-boundary primitive's evidence; the boundary it governs is "
                  "the phrase's, not the harmony's."),
        "D-478": (VERDICT_OUT,
                  "Its verbatim makes a phrase boundary a peak in a continuous strength profile "
                  "rather than the OR of a few binary signals.",
                  "It bears on the phrase-boundary primitive's model."),
        "D-479": (VERDICT_OUT,
                  "Its verbatim runs the boundary cues per eligible voice and aggregates them by "
                  "voice-coincidence, publishing both the per-voice and the texture boundaries.",
                  "It bears on the phrase-boundary primitive's computation and output."),
        "D-480": (VERDICT_OUT,
                  "Its verbatim states the phrase-boundary primitive is NOT an accuracy "
                  "requirement, a competitive reference engine doing no phrase segmentation at all, "
                  "and orders it built right but kept proportionate.",
                  "It bears on the phrase-boundary primitive's proportionality."),
        "D-481": (VERDICT_OUT,
                  "Its verbatim emits every notated marker as a boundary unconditionally, only the "
                  "surface-cue strength being peak-picked.",
                  "It bears on the phrase-boundary primitive's picking rule."),
        "D-482": (VERDICT_OUT,
                  "Its verbatim retires two hand-synchronised copies of the fermata scan into one "
                  "owned primitive, byte-identically.",
                  "It bears on a code unification inside the phrase-boundary primitive."),
        "D-484": (VERDICT_OUT,
                  "Its verbatim makes the phrase-boundary primitive a derived view that inherits "
                  "the loaded span and requests no extension of its own, publishing a per-profile "
                  "max-normalised confidence that participates in no override frame.",
                  "It bears on the phrase-boundary primitive's context behaviour and published "
                  "confidence."),
        "D-485": (VERDICT_OUT,
                  "Its verbatim requires every picked boundary to carry which cue or marker fired "
                  "and at what scope, and records the picked set SCOPE-BLIND today and the "
                  "requirement not built.",
                  "It bears on the phrase-boundary primitive's provenance requirement."),
        "D-490": (VERDICT_IN,
                  "Its verbatim records the fine-grain function override FALSIFIED — the harm rate "
                  "is flat against the contradiction value and RISES with the incumbent's "
                  "confidence, so no threshold separates the cases it fixes from those it breaks.",
                  "The override overturns a committed chord, so a measured verdict that it cannot "
                  "be made net-positive is directly about what chord is read over a span."),
        "D-491": (VERDICT_IN,
                  "Its verbatim records the vertically-fair repair REFUTED and states the cause: "
                  "'the progression contradiction does not predict which root is correct at these "
                  "moments', the earlier vertical commit being the better predictor of the "
                  "annotated root.",
                  "It states which evidence does and does not predict the correct root, which is "
                  "the fourth limb's ruled answer in part."),
        "D-492": (VERDICT_IN,
                  "Its verbatim recommends demoting the override to an ANNOTATION — leaving the "
                  "committed chord alone and recording that the progression disagrees — and marks "
                  "the recommendation explicitly NOT adopted and not implementable from that "
                  "paragraph.",
                  "Its subject is whether a committed chord over a span is overturned, and it "
                  "carries the measured position on that question."),
        "D-493": (VERDICT_IN,
                  "Its verbatim rules the principled restriction UN-COMPUTABLE because its trigger "
                  "needs a per-key chord re-decode, which 'IS the joint key-and-chord step the "
                  "record says is still owed'.",
                  "It names the genuinely coupled key-and-chord minority and what would be needed "
                  "to identify it, which is directly about the first and fourth limbs' relation."),
        "D-495": (VERDICT_OUT,
                  "Its verbatim requires a stated fallback where the phrase-boundary profile is "
                  "featureless — relax cadence admission and scale the vote weight down by the "
                  "graded strength rather than starve.",
                  "It bears on cadence admission and on the phrase-boundary profile it reads, both "
                  "outside the four limbs."),
        "D-629": (VERDICT_IN,
                  "Its verbatim rules that the resolver of carried uncertain readings IS the "
                  "function layer itself — it reads the carried alternatives and marks, assigns "
                  "function under each carried key/chord reading, and keeps the coherent one — with "
                  "no distinct gated box between the note layers and it.",
                  "It states what finally settles a tonality or chord left carried as uncertain, "
                  "which bears on the first and fourth limbs."),

        # ── group I — Module boundaries and code structure — 6 candidates — authored 2026-09-05 ──
        "D-072": (VERDICT_OUT,
                  "Its verbatim enforces the dependency order and requires any code that would "
                  "invert it to move to the notation bridge layer.",
                  "It bears on module dependency structure — what the analysis library may know "
                  "about the score format — not on what it reads from the music."),
        "D-229": (VERDICT_OUT,
                  "Its verbatim states three parts: the analysis library depends on no MuseScore "
                  "types; the bridge reads the score only through the established pattern and never "
                  "layout-derived state as analysis input; and editing MuseScore's own code is "
                  "admissible only for a blocking defect.",
                  "It bears on module boundaries, and its one analysis-facing clause names the note "
                  "model as the sanctioned reading surface rather than saying what is read from "
                  "it."),
        "D-296": (VERDICT_OUT,
                  "Its verbatim allows READING and CALLING MuseScore's engraving code from anywhere "
                  "we may edit, only EDITING the notation and engraving source being off limits.",
                  "It bears on module boundaries and on what may be edited, not on the reading."),
        "D-469": (VERDICT_OUT,
                  "Its verbatim leaves the point-in-time tick-local path OUTSIDE the unified "
                  "pipeline BY DESIGN, its semantics differing too much to force one interface "
                  "without distortion.",
                  "It bears on module boundaries — which paths are unified onto one pipeline — not "
                  "on what any of them decides."),
        "D-470": (VERDICT_OUT,
                  "Its verbatim records the temporal-context extension fields during the analysis "
                  "pass that computes them, a consumer reading what was recorded and never "
                  "re-running the chord analysis to rebuild them.",
                  "It bears on the fact-publication rule at the producing surface — record once, "
                  "read the record — not on what tonality, boundary, tone status or chord is "
                  "read."),
        "D-623": (VERDICT_OUT,
                  "Its verbatim makes a selection-aware capability a PARAMETER on the one "
                  "orchestrator rather than a second driver beside it, so one path builds, slices "
                  "and decodes.",
                  "It bears on orchestration — that one path sequences build, slice and decode — "
                  "not on what the decode decides; the pilot graded it OUT on the same ground."),

        # ── group J — Presentation and output conventions — 4 candidates — authored 2026-09-05 ──
        "D-295": (VERDICT_OUT,
                  "Its verbatim states the governing requirement of ZERO INFORMATION LOSS TO THE "
                  "END USER — every inferred object must be displayable, gradual revelation being "
                  "the intended design.",
                  "It bears on the presentation surface's obligation to be able to show what was "
                  "inferred, not on what is inferred."),
        "D-471": (VERDICT_OUT,
                  "Its verbatim fixes in advance the verdict rule for the sub-beat annotation "
                  "duration gate — kept if it reduces clutter without suppressing correct "
                  "annotations, retired if it suppresses equally many of each — and records it "
                  "undischarged at HEAD.",
                  "It bears on a display gate that hides very short chords from the annotation, not "
                  "on what chord is read over a span."),
        "D-498": (VERDICT_OUT,
                  "Its verbatim requires the product stance written for dense abstention and for "
                  "out-of-domain input — what the user sees when the system says a passage is "
                  "outside its tonal vocabulary.",
                  "It bears on the product stance at the presentation surface, not on any of the "
                  "four limbs."),
        "D-584": (VERDICT_OUT,
                  "Its verbatim makes the perfect/imperfect cadence call on the bass-derived "
                  "inversion, demoting the soprano arrival degree to a soft nudge because the "
                  "structural melody is not reliably recoverable.",
                  "It bears on how a cadence's type is decided, which is a read-off fact taken from "
                  "a settled tonal reading rather than one of the four limbs."),

        # ── group K — Documentation governance — 3 candidates — authored 2026-09-05 ──
        "D-113": (VERDICT_OUT,
                  "Its verbatim reserves any term that coincides even slightly with music theory "
                  "for its musical sense only.",
                  "It bears on the project's writing conventions, not on what the analysis reads."),
        "D-499": (VERDICT_IN,
                  "Its verbatim carries four documentation riders, one of which is to 'record the "
                  "membership tie-breaker as an idiom-calibrated constant'; its plain calls it 'the "
                  "rule that breaks a tie about whether a note belongs to the chord'.",
                  "That rider discloses that a note's membership of the chord is settled at a tie "
                  "by an idiom-calibrated constant, which is part of the third limb's answer."),
        "D-660": (VERDICT_OUT,
                  "Its verbatim rules that a research-tied name is not renamed but governed by two "
                  "tiers — explained at the introduction site, annotated at every later use — and "
                  "fixes the cleanup order with no tree-wide rename.",
                  "It bears on the terminology convention and the order of its cleanup, not on the "
                  "reading."),

        # ── group L — Licensing, contribution, and coding standards — 2 candidates — authored 2026-09-05 ──
        "D-292": (VERDICT_OUT,
                  "Its verbatim restricts the pool a ship-intended weight or table may be estimated "
                  "on to public-domain, CC0 and CC-BY sources, non-commercially or unlicensed music "
                  "being usable to validate but never to fit.",
                  "It bears on licensing — which music a shipped fitted value may be estimated on — "
                  "rather than on how the value enters the reading."),
        "D-614": (VERDICT_OUT,
                  "Its verbatim establishes that every real difficulty-grade label source is "
                  "research-only or proprietary at origin, so a commercial grading feature needs a "
                  "licence path or labels of our own.",
                  "It bears on licensing for a difficulty-grading feature, which is outside the "
                  "tonal reading entirely."),

        # ── group M — The style system and the knowledge base — 17 candidates — authored 2026-09-05 ──
        "D-131": (VERDICT_OUT,
                  "Its verbatim makes the style vocabulary ONE shared taxonomy — the five idioms "
                  "with mode and chromaticism as orthogonal cross-attributes — the same set the "
                  "harmonic vocabulary tags with, not two parallel vocabularies.",
                  "It bears on the style taxonomy's structure and its sharing between two "
                  "components, not on any of the four limbs."),
        "D-132": (VERDICT_OUT,
                  "Its verbatim states that what remains future work is the per-preset WEIGHTS "
                  "rather than the clusters, the clusters half being delivered by the ratified "
                  "five-idiom set.",
                  "It bears on the style system's remaining empirical grounding, not on the "
                  "reading."),
        "D-406": (VERDICT_OUT,
                  "Its verbatim splits ownership — this catalog owns the named progressions and "
                  "substitutions, the function layer's grammar owns which root motions are licensed "
                  "at all — the two never derived from each other, coupled only by a one-way "
                  "consistency test.",
                  "It bears on the ownership split between two knowledge stores; it states the "
                  "content of neither."),
        "D-421": (VERDICT_OUT,
                  "Its verbatim re-runs idiom discovery after every material corpus change, on "
                  "research material only, a changed cluster set being its own ratification event.",
                  "It bears on the style system's re-discovery protocol and its held-out "
                  "discipline."),
        "D-496": (VERDICT_OUT,
                  "Its verbatim makes the one-store-or-two question about the pairwise progression "
                  "grammar an OWED decision triggered at the recognition-consumer build, and says "
                  "'no section can yet state a rule here'.",
                  "It bears on an owed unification decision between two knowledge stores, and "
                  "states in terms that it fixes no rule."),
        "D-502": (VERDICT_OUT,
                  "Its verbatim names the span a recognised progression covers the "
                  "`progression-schema-span`, reserving 'sequence' and 'progression' for their own "
                  "senses.",
                  "It bears on naming and the reserved-vocabulary convention, not on where any span "
                  "falls."),
        "D-503": (VERDICT_OUT,
                  "Its verbatim makes the idiom weight vector DISCOVERED from the score and merely "
                  "SEEDED by the user's preference, in three forward-only phases.",
                  "It bears on the style system's idiom-mixture estimation, not on what tonality, "
                  "boundary, tone status or chord is read."),
        "D-504": (VERDICT_IN,
                  "Its verbatim rules a recognised harmonic sequence ALWAYS emitted as evidence of "
                  "the local key — corroborating a confirming cadence, tempering a disagreeing one, "
                  "and substituting for the cadence channel at a lower weight where none confirms "
                  "the candidate key.",
                  "It states an evidence channel that votes on the tonality and its weight relative "
                  "to the cadence, which is the first limb."),
        "D-505": (VERDICT_IN,
                  "Its verbatim requires at least two transposed statements of the SAME recognised "
                  "entry for a sequence, a single internally-sequential recognition emitting none.",
                  "It defines what counts as the sequence evidence that votes for the local key, "
                  "which is part of the first limb's evidence rule."),
        "D-506": (VERDICT_IN,
                  "Its verbatim makes progression recognition ADDITIVE — the literal Roman numeral "
                  "is never changed — rewriting it to the substituted-for function being rejected "
                  "as losing the label the ground truth scores.",
                  "The Roman numeral is this layer's own chord under D-526, so the rule that "
                  "recognition never rewrites it is about what chord is read over a span."),
        "D-507": (VERDICT_OUT,
                  "Its verbatim marks line-defined catalog entries 'chords-only' when recognised by "
                  "their chord skeleton, the mark retiring per entry when the voice-leading layer "
                  "supplies the other half.",
                  "It bears on the progression catalog's recognition and its confidence marking."),
        "D-508": (VERDICT_OUT,
                  "Its verbatim ships the catalog/grammar consistency test scoped to the measured "
                  "containment with an explicit known-gap list, tightening to a clean assertion when "
                  "the grammar amendment lands.",
                  "It bears on a consistency test between two knowledge stores, not on the "
                  "reading."),
        "D-509": (VERDICT_IN,
                  "Its verbatim rules that where the chord layer committed, a recognised "
                  "progression's prior enters the SAME contradiction frame under the same threshold "
                  "and tie rules, and may only SELECT an existing carried reading — never one built "
                  "from the notes.",
                  "It states what may change a committed chord over a span and what it may change "
                  "it to, which is the fourth limb."),
        "D-542": (VERDICT_OUT,
                  "Its verbatim orders idiom discovery DISCOVER-THEN-NAME — structure learned on a "
                  "label-free low-level encoding, theory features and genre labels applied only "
                  "afterwards as interpretation lenses.",
                  "It bears on the style-clustering study's method."),
        "D-543": (VERDICT_OUT,
                  "Its verbatim fixes the discovery encoding as key-normalised tonal-pitch-class "
                  "transitions, spelled where spelling is reliable, run as two complementary views.",
                  "It bears on the style-clustering study's encoding."),
        "D-544": (VERDICT_OUT,
                  "Its verbatim makes confound control a first-class validity gate with a mandatory "
                  "source-leakage test: if the clusters approximate the source, the study found "
                  "bookkeeping and not idiom.",
                  "It bears on the style-clustering study's validity gate."),
        "D-545": (VERDICT_OUT,
                  "Its verbatim makes one external library the uniform mechanical extractor for "
                  "idiom discovery, stopping at notes and simultaneities, our own key/chord/function "
                  "inference never touching the extraction.",
                  "It bears on the idiom-discovery study's extraction method, and excludes our own "
                  "reading from it rather than describing it."),

        # ── group N — Generation, constraints, visualization, and the LLM integration — 8 candidates — authored 2026-09-05 ──
        "D-440": (VERDICT_OUT,
                  "Its verbatim makes the language-model integration a purpose-built module tapping "
                  "existing interfaces directly rather than waiting for the plugin API redesign.",
                  "It bears on the language-model integration's build scope."),
        "D-441": (VERDICT_OUT,
                  "Its verbatim keeps analysis and modification in one conversation thread, a "
                  "follow-up instruction executing without re-analysis from the model's own "
                  "history.",
                  "It bears on the language-model integration's conversational behaviour."),
        "D-442": (VERDICT_OUT,
                  "Its verbatim feeds a validation failure back to the model as a tool-call error "
                  "rather than showing it to the user, only clean output reaching the score.",
                  "It bears on the language-model integration's error handling."),
        "D-443": (VERDICT_OUT,
                  "Its verbatim requires only tool use of a provider; a provider without it may be "
                  "used for read-only analysis but cannot drive score modification.",
                  "It bears on the language-model integration's provider abstraction."),
        "D-444": (VERDICT_OUT,
                  "Its verbatim makes the core access layer a facade over interfaces that already "
                  "exist rather than a redesign.",
                  "It bears on the language-model integration's access layer."),
        "D-445": (VERDICT_OUT,
                  "Its verbatim records that an address does not uniquely identify a note, several "
                  "notes of one chord sharing one address, so the note entity carries its own "
                  "identifier.",
                  "It bears on the language-model integration's entity addressing."),
        "D-447": (VERDICT_OUT,
                  "Its verbatim generates the model's tool definitions from the operation-set "
                  "schemas automatically, with no manual maintenance.",
                  "It bears on the language-model integration's tool generation."),
        "D-448": (VERDICT_OUT,
                  "Its verbatim curates about forty operations from observed use rather than "
                  "exposing every editing method.",
                  "It bears on the language-model integration's operation set."),

        # ── group Q — Scope and the development toolchain — 5 candidates — authored 2026-09-05 ──
        "D-365": (VERDICT_OUT,
                  "Its verbatim answers that a corpus search driven by the sum of all needs is "
                  "worth running but is step 3 of 3, the needs artifact and the re-scoring of the "
                  "existing enumeration coming first.",
                  "It bears on the corpus-search procedure, not on the reading."),
        "D-514": (VERDICT_OUT,
                  "Its verbatim makes a newly acquired annotation set whose works overlap the "
                  "regression corpus RECORD-ONLY over those works — not wired to, not compared "
                  "against, not bulk-diffed with the gate corpus without a user ruling.",
                  "It bears on corpus intake and on protecting the gate from contamination."),
        "D-516": (VERDICT_OUT,
                  "Its verbatim records two ground-truth classes ADOPTED at the first full-needs "
                  "audit — contrapuntal/imitative structure, and marked part-writing errors.",
                  "It bears on which ground-truth classes the project tracks as needed."),
        "D-613": (VERDICT_OUT,
                  "Its verbatim records implied-polyphony ground truth CONFIRMED ABSENT and closes "
                  "the search.",
                  "It bears on corpus availability for voice and stream separation; the pilot "
                  "graded it OUT on the same ground, reached only by an in-word match."),
        "D-665": (VERDICT_OUT,
                  "Its verbatim requires the intake record to say what a voice/stream label set "
                  "actually measures — labels derived from engraved notation, not from a listener's "
                  "judgment about heard lines.",
                  "It bears on the intake record for a corpus of voice labels."),

        # ── group S — The guiding principles — 12 candidates — authored 2026-09-05 ──
        "D-168": (VERDICT_OUT,
                  "Its verbatim is principle #4 whole: 'Long-term goal: maximum-precision "
                  "inference.'",
                  "It states the project's objective, against which any answer is judged; it states "
                  "no answer."),
        "D-170": (VERDICT_OUT,
                  "Its verbatim is principle #6: total unification, no duplication, one path per "
                  "concern.",
                  "It bears on code structure across the whole project, not on the reading."),
        "D-171": (VERDICT_OUT,
                  "Its verbatim is principle #7: enhance a layer only with algorithms and methods "
                  "that belong to it, the worst case forcing a layer redesign rather than a "
                  "cross-layer patch.",
                  "It bears on layer adherence as a general discipline; it says nothing about what "
                  "this layer decides."),
        "D-172": (VERDICT_OUT,
                  "Its verbatim is principle #8: no inference-problem-driven coding until the "
                  "refactoring, the architectural design and the algorithmic completion are done.",
                  "It bears on the sequencing of work, not on the reading."),
        "D-180": (VERDICT_OUT,
                  "Its verbatim is principle #17, the Premise Gate, with its six lettered "
                  "requirements from the premise ledger to the no-hand-transcribed-figures rule.",
                  "It bears on the method by which any inference-affecting design is built or "
                  "probed, not on what this one decides."),
        "D-182": (VERDICT_OUT,
                  "Its verbatim is principle #19: an unestablished instrument, corpus, gate or "
                  "recorded figure is forbidden until positively established.",
                  "It bears on the establishment of measurement, not on the reading."),
        "D-185": (VERDICT_OUT,
                  "Its verbatim is principle #22: every hard gate carries a pre-declared protocol "
                  "for the largest change it will face.",
                  "It bears on gate governance, not on the reading."),
        "D-190": (VERDICT_OUT,
                  "Its verbatim is the decision-neutrality corollary: a design is chosen from the "
                  "principles and the objective alone, reuse cost secondary, downstream impact and "
                  "user-visible change carrying no weight.",
                  "It bears on how a design is chosen, not on which design this layer has."),
        "D-201": (VERDICT_OUT,
                  "Its verbatim states that very large scores MUST be handled and are expected to "
                  "be a more common use than our corpora.",
                  "It bears on a standing scale requirement every later design is judged against, "
                  "not on any of the four limbs."),
        "D-202": (VERDICT_OUT,
                  "Its verbatim makes the effort control ONE setting with several dials behind it, "
                  "among the quantities it must bound being the time the analysis takes, and marks "
                  "it DEFERRED.",
                  "It bears on the effort control, not on what the analysis reads."),
        "D-205": (VERDICT_OUT,
                  "Its verbatim makes a HUMAN the ground truth where no formal ground truth exists, "
                  "an automated triage judge being guidance for that person and never a grader.",
                  "It bears on the ground-truth policy for unannotated repertoire."),
        "D-206": (VERDICT_OUT,
                  "Its verbatim holds the intonation section as a deliberate long-horizon hold and "
                  "a declared future CONSUMER of the analysis.",
                  "It bears on a held feature and its status as a consumer of the analysis, not on "
                  "the analysis."),

        # ── group T — Standing process rules and local patches — 1 candidate — authored 2026-09-05 ──
        "D-279": (VERDICT_OUT,
                  "Its verbatim states the Stage-3 entry gate's seven conditions before any "
                  "engagement wiring can reach production, beginning with Tier-1 defusal as a "
                  "prerequisite rather than an inventory item.",
                  "It bears on the process gate a build must clear before wiring reaches "
                  "production, not on what the wiring would decide."),

        # ── group U — The standing decision-bearing surfaces — 5 candidates — authored 2026-09-05 ──
        "D-220": (VERDICT_IN,
                  "Its verbatim requires the augmented-seventh guard to see BOTH the major third "
                  "and the augmented fifth, the third-only form having been tried and reverted.",
                  "It states the firing condition of a guard inside the chord decision, which is "
                  "part of what chord is read over a span."),
        "D-221": (VERDICT_IN,
                  "Its verbatim gates the inversion bonuses on `hasStructuralBass`, so a sparse "
                  "upper-register lowest note earns none.",
                  "It states when a lowest note counts as a structural bass and so what inversion "
                  "is read, which is part of the fourth limb."),
        "D-222": (VERDICT_IN,
                  "Its verbatim falls back to the without-`w_dim` variant when the post-bonus "
                  "winner is not diminished or half-diminished, the bonus being able to rotate the "
                  "winner across bass candidates.",
                  "It states a rule that decides which reading is committed over a span, which is "
                  "the fourth limb."),
        "D-223": (VERDICT_OUT,
                  "Its verbatim requires a gate computing against the pre-correction winner to read "
                  "the `originalWinner*` snapshots rather than the live top result.",
                  "It bears on how a gate reads its own input — an implementation rule — rather "
                  "than on what the gate decides about the music."),
        "D-224": (VERDICT_IN,
                  "Its verbatim fires joint bass-and-chord scoring only where at least one tone "
                  "came from accumulating a whole stretch, single-tick, status-bar and unit-test "
                  "paths using the legacy single-bass path.",
                  "It states when the bass and the chord are scored together and when they are not, "
                  "which is part of the fourth limb's ruled answer."),
    },
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


# ── the extras: two authored filters, each verified in BOTH directions ────────────────────────
# Counted in words up to twenty, because the read-me is prose and "The 9 files of this pack"
# would read as a defect.  Beyond twenty the digit is rendered: a pack that large is not a state
# this tool has ever been in, and a STOP there would fail a run for a cosmetic reason.
NUMBER_WORDS = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen", "twenty")


def number_word(n: int) -> str:
    return NUMBER_WORDS[n] if 0 <= n < len(NUMBER_WORDS) else str(n)


def _removal_spans(text: str, removals: list[dict], rel: str) -> list[dict]:
    """The offsets of each authored removal, located by ANCHOR TEXT and never by line number."""
    norm, idx = _normalize(text)
    spans = []
    for r in removals:
        at = _find_once(norm, r["anchor"], f"{rel}: the removal's anchor")
        origin = idx[at]
        opens, closes = r["opens_with"], r["closes_with"]
        a = text.rfind(opens, 0, origin)
        if a == -1:
            raise Stop(f"{rel}: nothing opens with {opens!r} before the anchor {r['anchor']!r}")
        if text.find(closes, a, origin) != -1:
            raise Stop(f"{rel}: the nearest {opens!r} before the anchor {r['anchor']!r} is closed "
                       f"again before the anchor is reached — the anchor is not inside it")
        c = text.find(closes, origin)
        if c == -1:
            raise Stop(f"{rel}: nothing closes with {closes!r} after the anchor {r['anchor']!r}")
        b = c + len(closes)
        spans.append({"kind": "removal", "anchor": r["anchor"],
                      "opens_with": opens, "closes_with": closes, "why": r["why"],
                      "start": a, "end": b, "the_text_removed": text[a:b],
                      "characters_removed": b - a})
    return spans


def _cut_spans(text: str, cuts: list[dict], rel: str) -> list[dict]:
    """The offsets of each authored section cut, located by what its HEADING contains."""
    lines = text.split("\n")
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln) + 1
    spans = []
    for cut in cuts:
        level, needle = cut["heading_level"], cut["heading_contains"]
        hits = [i for i, ln in enumerate(lines) if ln.startswith(level) and needle in ln]
        if len(hits) != 1:
            raise Stop(f"{rel}: {len(hits)} headings at {level!r} contain {needle!r}, not exactly "
                       f"one")
        h = hits[0]
        nxt = next((j for j in range(h + 1, len(lines)) if lines[j].startswith(level)), None)
        if nxt is None:
            raise Stop(f"{rel}: the section {lines[h]!r} is not terminated by a further {level!r} "
                       f"heading")
        a, b = starts[h], starts[nxt]
        spans.append({"kind": "cut", "heading": lines[h], "heading_contains": needle,
                      "closes_before": lines[nxt], "why": cut["why"],
                      "start": a, "end": b, "the_text_removed": text[a:b],
                      "characters_removed": b - a})
    return spans


def filter_part(text: str, part: dict, rel: str) -> tuple[str, list[dict]]:
    """Apply one part's authored filters, and VERIFY IN BOTH DIRECTIONS or STOP.

    The two directions, which are the ruling's own verification and not this tool's invention:
    what was removed is ABSENT from what is rendered, and re-inserting exactly what was removed
    at the offsets it came from reproduces the source BYTE FOR BYTE — which is what proves that
    nothing else was taken out.  Nothing is marked in place: a mark would be an addition, and the
    verification is that the rendered text equals the source with exactly these spans deleted.
    """
    spans = (_removal_spans(text, part.get("removals", []), rel)
             + _cut_spans(text, part.get("cuts", []), rel))
    spans.sort(key=lambda s: s["start"])
    for prev, nxt in zip(spans, spans[1:]):
        if nxt["start"] < prev["end"]:
            raise Stop(f"{rel}: two authored filters overlap, at {prev['start']}–{prev['end']} "
                       f"and {nxt['start']}–{nxt['end']}")

    out = text
    for s in reversed(spans):
        out = out[:s["start"]] + out[s["end"]:]

    # DIRECTION ONE — what was removed is gone.
    for s in spans:
        if s["the_text_removed"] in out:
            raise Stop(f"{rel}: a filtered passage is still present in the rendered text")
        if s["kind"] == "cut" and s["heading"] in out:
            raise Stop(f"{rel}: the cut section's heading {s['heading']!r} is still present")

    # DIRECTION TWO — nothing else was removed.
    rebuilt, cur, fpos = [], 0, 0
    for s in spans:
        keep = s["start"] - cur
        rebuilt.append(out[fpos:fpos + keep])
        fpos += keep
        rebuilt.append(s["the_text_removed"])
        cur = s["end"]
    rebuilt.append(out[fpos:])
    if "".join(rebuilt) != text:
        raise Stop(f"{rel}: re-inserting what was removed does not reproduce the source — "
                   f"something else was removed")

    for s in spans:
        s.pop("start")
        s.pop("end")
    return out, spans


def render_extra(extra: dict) -> tuple[str, dict]:
    """One extra member: its parts, each taken by anchor and filtered, joined and verified."""
    texts, part_records = [], []
    for part in extra["parts"]:
        rel = part["source"]
        bodies, span_records = [], []
        for spec in part["spans"]:
            body, srec = span_lines(rel, spec)
            span_records.append(srec)
            bodies.append("\n".join(body))
        text = "\n\n".join(bodies)
        text, filters = filter_part(text, part, rel)
        texts.append(text)
        part_records.append({
            "source": rel,
            "spans": span_records,
            "filters_applied": filters,
            "★_verified_in_both_directions": (
                "What each filter removed is ABSENT from the rendered text, AND re-inserting "
                "exactly what was removed at the offsets it came from reproduces this source "
                "byte for byte — so nothing else was taken out.  Both are STOPs, re-run on every "
                "render."),
            "characters": len(text),
        })
    return "\n\n".join(texts) + "\n", {
        "member": extra["number"],
        "file": extra["filename"],
        "title": extra["title"],
        "source": extra["source"],
        "rendered_from": extra["rendered_from"],
        "★_this_is_an_EXTRA": (
            "Rendered AFTER the ruled six under Ruling 16 of "
            "`cowork_rulings_2026_08_31_decision_surface_sitting.md`.  The ruled six are not "
            "removed, not reordered and not renamed for any subject; `MEMBERS` keeps its ruled "
            "content."),
        "parts": part_records,
        "leak_checked": False,
        "leak_not_checked_because": (
            "The leak check is ruled over members (5) and (6) — the two this tool GENERATES.  An "
            "extra is quoted, and what it may not carry is cut by its own authored filters, "
            "which are verified in both directions."),
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


_GROUP_TITLES: dict[str, str] | None = None


def group_title(group: str) -> str:
    """The decisions register's OWN title for a register group, read from the table that defines it.

    NOT a second copy of those titles (#6): `DECISIONS.md` renders its group headings from the same
    `groups` table this reads, so the register and this tool cannot drift apart.

    BEFORE 2026-09-05 this gloss was the hardcoded string "Layer 2 — the slicer".  Until the `l2`
    criterion was written, the only criterion carrying a group term named exactly one group, E, so
    the string was true of every group match the tool then made; WHY it was written as a literal is
    not established and is not asserted (#18).  The `l2` criterion names six, and for A, C, D, F and
    G that string is false.  Group E's title in the backbone is that same
    string, so the `harmony-boundary` subject's rendered manifest is byte-unchanged by this repair,
    which is what makes it a repair and not a behaviour change.  The former wording is preserved
    here rather than deleted (#12).

    An unknown group is a STOP rather than a fallback: a gloss that silently degrades to the bare
    letter would read as a title and be believed.
    """
    global _GROUP_TITLES
    if _GROUP_TITLES is None:
        _GROUP_TITLES = {g["id"]: g["title"]
                         for g in read_json(BACKBONE).get("groups", [])
                         if g.get("id") and g.get("title")}
        if not _GROUP_TITLES:
            raise Stop("the backbone carries no usable `groups` table, so no group title can be "
                       "read and the group gloss has no source")
    if group not in _GROUP_TITLES:
        raise Stop(f"register group {group!r} carries no title in the backbone's `groups` table")
    return _GROUP_TITLES[group]


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
                        "means": group_title(e.get("group"))})
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


def render_what_was_cut(withheld_entries: int, passages: list[dict],
                        extras_filtered: list[dict]) -> str:
    """The read-me's what-was-cut section, DERIVED from what was actually withheld.

    ★ EXTENDED 2026-08-31 TO THE EXTRAS, AND THE REASON IS THE ONE THE FUNCTION ALREADY CARRIES.
    An extra member may be filtered by its own authored removals and cuts.  Before this, a
    subject with no withheld family but a filtered extra would have told its session that
    *nothing has been withheld from this pack* while three of its nine members had material
    deleted out of them silently — the same falsity, in the same section, that the licensed
    accommodation below was written to remove.  The extras' filtering is therefore DERIVED into
    this section from the counts, exactly as the other two kinds are, and NOT switched on a
    subject name.  A subject whose extras are empty renders BYTE-IDENTICALLY to before.

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

    held_out = bool(kinds)
    for x in extras_filtered:
        bits = []
        if x["removals"]:
            bits.append(f"{number_word(x['removals'])} passage"
                        f"{'' if x['removals'] == 1 else 's'}")
        if x["cuts"]:
            bits.append(f"{number_word(x['cuts'])} whole section"
                        f"{'' if x['cuts'] == 1 else 's'}")
        if bits:
            kinds.append(f"{' and '.join(bits)} taken out of `{x['filename']}` — deleted where "
                         f"they stood,\n  with no mark, so you cannot tell from that file where "
                         f"one was")

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

    lead = f"{number_word(len(kinds)).capitalize()} kind{'' if len(kinds) == 1 else 's'}:"
    bullets = "\n".join("* " + k + (";" if i < len(kinds) - 1 else ".")
                        for i, k in enumerate(kinds))
    # The opening sentence names WHY, and the why is not the same in the two states.  Where a
    # family is withheld, the pack is cut so that what is derived can be compared against an
    # answer the session has not read.  Where nothing is held out and only an extra is filtered,
    # there is no such answer, and saying there is would be false.  DERIVED from what was
    # actually withheld, not switched on a subject name.
    opening = ("Material has been withheld from this pack **for this subject**, so that what you "
               "derive can be\ncompared against a ruled answer you have not read."
               if held_out else
               "Material has been removed from this pack **for this subject**, so that what it "
               "carries states\nwhat the analysis SHOULD do and never what this project already "
               "has. Nothing is held back\nfrom you as an answer to be compared against; what is "
               "gone is this side's own conclusions and\nits account of what exists.")
    return f"""{head}

{opening} {lead}

{bullets}

{tail}"""


def render_read_me(subject: str, subject_words: str, passages: list[dict],
                   withheld_entries: int, members: list[dict],
                   extras_filtered: list[dict]) -> str:
    # DERIVED from the member count for THIS subject, which is the prose defect the per-subject
    # extras dimension itself causes and must therefore fix (Ruling 16, 2026-08-31): the heading
    # read "The six files of this pack, in order" and built its list from the global `MEMBERS`,
    # so a pack carrying extras would have stated six over a directory of ten.  A subject with no
    # extras renders BYTE-IDENTICALLY to before.
    #
    # THE STOP-AND-RECORD CLAUSE'S COUNT IS DERIVED THE SAME WAY (Ruling 17(c), 2026-08-31).  It
    # read "in any file, including one of these six", which would have stated six over nine in
    # the FIRST thing a blind session reads.  ONLY THE COUNT MOVED: the rule the clause states is
    # unchanged, and the boundary clause above it is untouched.
    listing = "\n".join(
        [f"{i + 1}. `{m['filename']}` — {m['title']}" for i, m in enumerate(members)])
    what_was_cut = render_what_was_cut(withheld_entries, passages, extras_filtered)
    return f"""# READ THIS FIRST — the whole of what this session opens

You are an **implementation-blind deriving session**. Your work is to write what the analysis
**should** do for one unit, from the domain and from the ruled design intent — **not** to describe
what any existing code or specification says it currently **does**.

**The unit for this session is: {subject_words}**

## The {number_word(len(members))} files of this pack, in order

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
file, including one of these {number_word(len(members))} — STOP READING THAT FILE AT THAT POINT and record WHERE you were
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
    if subject not in EXTRAS:
        raise Stop(f"no authored EXTRAS list for subject {subject!r} — an empty list is authored, "
                   f"never left absent, so that a missing one cannot read as an empty one")
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

    # ── the EXTRAS, rendered AFTER the ruled six ─────────────────────────────────────────────
    extras = EXTRAS[subject]
    extras_filtered = []
    for x in extras:
        text, rec = render_extra(x)
        files[x["filename"]] = text
        rec["characters"] = len(text)
        member_records.append(rec)
        extras_filtered.append({
            "filename": x["filename"],
            "removals": sum(len(p.get("removals", [])) for p in x["parts"]),
            "cuts": sum(len(p.get("cuts", [])) for p in x["parts"]),
        })

    # ── STOP: the ruled six are not removed, not reordered and not renamed, for any subject ───
    # The user ruled `MEMBERS` on 2026-08-22 and Ruling 16 rules the extension ADDITIVE.  Making
    # that mechanical rather than a promise is what stops a later edit from quietly moving one.
    ruled = [(m["number"], m["filename"]) for m in MEMBERS]
    rendered_six = [(r["member"], r["file"]) for r in member_records[:len(MEMBERS)]]
    if rendered_six != ruled:
        raise Stop(f"the ruled six are not intact and in their ruled order: rendered "
                   f"{rendered_six}, ruled {ruled}")

    files[READ_ME] = render_read_me(subject, authored["the_subject_in_plain_words"],
                                    passages_applied, len(withheld_ids),
                                    MEMBERS + extras, extras_filtered)

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

    # STOP 12's first limb: a freeze naming a subject this tool does not build would pin a
    # directory nothing here accounts for, and its digests would never be checked.
    orphan_freeze = sorted(set(FROZEN) - set(WITHHELD))
    if orphan_freeze:
        raise Stop(f"FROZEN names subject(s) this tool does not build: {orphan_freeze}")

    subjects, packs = {}, {}
    for subject in sorted(WITHHELD):
        rec, files = build_subject(subject, sort["entries"], backbone)
        if subject in FROZEN:
            rec["★_FROZEN"] = frozen_block(subject)
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
            "Ruling 1 of `cowork_rulings_2026_08_23_member_two_second_leak_sitting.md` — the "
            "second withheld passage of member (2), the defense-at-its-home bullet's "
            "founding-instances sentence, withheld for the harmony-boundary subject.",
            "Ruling 2(a) of `cowork_rulings_2026_08_24_sizing_leak_list_sitting.md` — the "
            "manifest's candidate-criterion block renders truthfully for a subject whose "
            "criterion is EMPTY BY RULING, derived from the authored entry and never switched on "
            "a subject name.",
            "Ruling 16 of `cowork_rulings_2026_08_31_decision_surface_sitting.md` — the "
            "PER-SUBJECT EXTRAS dimension, ADDITIVE: the ruled six stay in every pack, unchanged "
            "and in their ruled order, and a subject may carry extras after them.",
            "Rulings 11 (Decisions 1 and 2) and 12 of "
            "`cowork_rulings_2026_08_31_decision_surface_sitting.md` — what the `l0-l1` subject's "
            "three extras carry: the charter's §5 and §9 leak-filtered, the five reading-pass "
            "extracts with one named section cut from each, and the empirical findings ledger "
            "whole by the phase definition's own naming.",
            "Ruling 17 of `cowork_rulings_2026_08_31_decision_surface_sitting.md` — (a) the two "
            "SPENT subjects frozen at their established blobs with a hash STOP (D-646) rather "
            "than re-rendered; (b) the filter widened by ONE named candidate and no more; (c) "
            "the four residuals repaired, the bar that forbade it relaxed for this purpose "
            "alone; (d) the what-was-cut section's derivation from the counts ratified.",
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
            "the EXTRAS a subject carries after the ruled six — each one's parts, the spans taken "
            "from each part by ANCHOR TEXT and never by line number, and its two filters "
            "(`removals` by anchor text, `cuts` by what a heading contains), each carrying its "
            "own reason; an EMPTY list is authored for a subject with none, never left absent",
            "the FROZEN table — the per-file blob digests at which a SPENT subject's pack is "
            "pinned, with its finding, its date and its reason (the D-677 shape again), so that "
            "the freeze is enforced by a hash STOP rather than trusted",
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
            "a subject with no authored EXTRAS entry — an empty list is authored so that a "
            "missing one cannot read as an empty one",
            "an EXTRA's removal anchor not found exactly once or not sitting inside its own "
            "delimiter pair; an EXTRA's cut heading not found exactly once or not terminated by "
            "a further heading at its own level; two of a part's filters overlapping; and EITHER "
            "DIRECTION of the extras' verification failing — filtered text still present, or "
            "re-inserting what was removed not reproducing the source",
            "the ruled six not intact, in their ruled order, at the head of a subject's rendered "
            "members",
            "a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one "
            "of whose files does not carry its recorded blob digest — checked in both "
            "directions; a FROZEN entry naming a subject this tool does not build; and a freeze "
            "record missing its finding, its date or its reason",
        ],
        # DERIVED PER SUBJECT (Ruling 17(c)), from the members actually rendered for it, so this
        # field can no longer name six files over a directory of ten.  It is derived from the
        # member records already built rather than from a second walk of `MEMBERS` and `EXTRAS`,
        # so there is ONE derivation of a pack's file list and not two (#6).
        "the_pack_files_in_order": {
            subject: [READ_ME] + [r["file"] for r in rec["the_members_as_rendered"]]
            for subject, rec in sorted(subjects.items())
        },
        "subjects": subjects,
    }
    return manifest, packs


def pack_dir(subject: str) -> str:
    return os.path.join(PACK_ROOT, subject)


# ── the freeze: enforced by a hash STOP, never by a convention (D-646) ────────────────────────
def blob_sha1(path: str) -> str:
    """The GIT BLOB hash of a file's own bytes — the form `git hash-object` reproduces.

    Chosen over a bare content hash for one reason: an independent tool can confirm the freeze
    without trusting this generator's own arithmetic (#19).
    """
    data = open(path, "rb").read()
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(data))
    h.update(data)
    return h.hexdigest()


def verify_frozen(subject: str) -> dict:
    """A frozen subject, checked against its RECORDED DIGESTS and never against a re-render.

    BOTH DIRECTIONS, because one alone would pass a defect: every recorded file is present and
    carries its digest, AND the directory holds no file the freeze does not record.  Any failure
    is a STOP rather than a drift line — a frozen file that has moved is not staleness to be
    regenerated away, it is the record of a completed derivation having been altered.
    """
    rec = FROZEN[subject]
    for f in ("finding", "date", "reason"):
        if not rec.get(f):
            raise Stop(f"the freeze of {subject!r} lacks its {f} and does not reach the "
                       f"derivation (amended #10, the shape every authored input here answers)")
    d = pack_dir(subject)
    if not os.path.isdir(d):
        raise Stop(f"{subject} is FROZEN and its pack directory is missing")
    on_disk = sorted(n for n in os.listdir(d) if os.path.isfile(os.path.join(d, n)))
    recorded = sorted(rec["digests"])
    if on_disk != recorded:
        raise Stop(f"{subject} is FROZEN: the directory holds {on_disk}, and the freeze records "
                   f"{recorded}")
    checked = {}
    for name in recorded:
        got = blob_sha1(os.path.join(d, name))
        want = rec["digests"][name]
        if got != want:
            raise Stop(f"{subject}/{name} is FROZEN at blob {want} and now hashes {got} — the "
                       f"record of a completed derivation has been altered")
        checked[name] = got
    return checked


def frozen_block(subject: str) -> dict:
    """What the manifest says about a frozen subject, so its member records cannot mislead.

    The member records below a frozen subject are built from the CURRENT sources, because this
    tool builds every subject the same way and the ruling keeps both subjects' entries.  For a
    frozen subject those records therefore describe what the sources WOULD render and not what
    the directory holds — so the difference is stated here rather than left for a reader to walk
    into, and the DIGESTS are named as the authority over the counts.
    """
    rec = FROZEN[subject]
    return {
        "★_this_subject_is_FROZEN_and_is_NOT_re-rendered": (
            "Its deriving session has RUN, so this pack is the record of what that session was "
            "given rather than an input to be kept current. Under D-646 it is pinned at the "
            "digests below and the freeze is enforced by a hash STOP at `--check`, in both "
            "directions. `write_all` writes nothing into its directory."),
        "★_so_read_the_member_records_below_with_this_in_mind": (
            "They are built from the sources AS THEY STAND TODAY, because every subject is built "
            "the same way and the ruling keeps this subject's entry. Where a member's sources "
            "have grown since the pack was rendered, the record's counts describe what WOULD be "
            "rendered and NOT what the frozen directory holds. THE DIGESTS ARE THE AUTHORITY ON "
            "WHAT THE DIRECTORY HOLDS."),
        "finding": rec["finding"],
        "date": rec["date"],
        "reason": rec["reason"],
        "the_digests": rec["digests"],
        "the_digest_form": (
            "The git blob hash of each file's own bytes — `git hash-object <file>` reproduces "
            "every value, so the freeze can be confirmed without trusting this generator (#19)."),
    }


def write_all(manifest: dict, packs: dict, only: str | None) -> None:
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    for subject, files in sorted(packs.items()):
        if only and subject != only:
            continue
        if subject in FROZEN:
            # THE FREEZE, at the one place that could break it.  Nothing is written into a spent
            # subject's directory — not the whole pack, not one file of it.
            continue
        d = pack_dir(subject)
        os.makedirs(d, exist_ok=True)
        for name, text in sorted(files.items()):
            with open(os.path.join(d, name), "w", encoding="utf-8", newline="") as fh:
                fh.write(text)


def check_all(manifest: dict, packs: dict) -> int:
    drift: list[str] = []
    frozen_checked: dict[str, dict] = {}
    want = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    if have != want:
        drift.append("derivation_boot_pack.json does not re-derive")
    for subject, files in sorted(packs.items()):
        if subject in FROZEN:
            # VERIFIED AGAINST ITS RECORDED DIGESTS, never against a re-render: the sources have
            # grown since this pack was rendered, and re-rendering it is exactly what the ruling
            # forbids.  A mismatch raises rather than joining `drift` — see `verify_frozen`.
            frozen_checked[subject] = verify_frozen(subject)
            continue
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
    for subject, checked in sorted(frozen_checked.items()):
        print(f"  {subject}: FROZEN — {len(checked)} file(s) at their recorded blobs")
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
