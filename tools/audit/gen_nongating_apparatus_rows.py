#!/usr/bin/env python3
"""Derive the NON-GATING apparatus set, and publish THE LIVE GATING ANSWER by identity.

THE RULING (user, 2026-08-03): rows whose subject is this project's own tracking and
documentation apparatus are declared NON-GATING - worked in leftover capacity, gating nothing.

★ AND THE SECOND RULING THIS FILE NOW SERVES (user, 2026-08-17, Ruling 1 of
`cowork_rulings_2026_08_17_session_start_read_sitting.md`): "A session no longer reads the whole
index at session start. It reads the derived gating answer, and opens the INDEX when it needs a
row."  The gating side is the COMPLEMENT of the non-gating verdicts over the open rows this tool
already parses, so publishing it authors no verdict; it publishes what this derivation already
computes.  It is established under #19 on every run, reconciled in BOTH directions against the
INDEX itself, and a row it cannot place HALTS the run.  The full statement of what is derived,
what would falsify it and what it does NOT do is at `the_live_gating_answer` below and is
published into the artifact at `★_the_live_gating_answer`.

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
# The canonical status vocabulary, the row split and the leading-token function live in ONE place
# (#6) — the lint that enforces them. This parser reads a row's state through them rather than
# re-implementing the test, which is what makes the lint's verdict and this parser's verdict the
# same verdict by construction (Ruling 33, 2026-08-09).
from index_status_lint import (                  # noqa: E402  (path set above)
    CANONICAL, CELLS_PER_ROW, leading_token, split_row,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent
ROOT = ROOT.parent
INDEX = ROOT / "OPEN_ITEMS.md"
OUT = ROOT / "tools" / "audit" / "nongating_apparatus_rows.json"
# D-639's SECOND application — the reach derivation over the apparatus-classed rows. Its IN set is
# what the user's Ruling 56 APPLIES here, and it is read on every run rather than transcribed.
REACH = ROOT / "tools" / "audit" / "decisions" / "true_half_reach_rows.json"
# READ FOR COMPARISON ONLY, never to reach the live answer. Its generator is frozen HISTORICAL; the
# reason and the bound are at `frozen_gating_enumeration` below.
FROZEN_INVENTORY = ROOT / "tools" / "audit" / "phase1_completion_inventory.json"

GATES = "GATES"
NON_GATING = "NON-GATING"

# The ground a gating row carries when it is gating because it is OUTSIDE the over-inclusive
# apparatus first cut. It is a distinct string so the two ways a row reaches the gating side can be
# told apart at the artifact without opening this file.
OUTSIDE_THE_CUT_GROUND = (
    "the ruled default - the row is outside the over-inclusive apparatus first cut, so the "
    "non-gating declaration does not reach it at all")

# The gate ground a row carries when it is here because D-639's reach derivation put it INSIDE the
# doc-sync half and the user's Ruling 56 applied that. It is a distinct string so the authored table
# and the derivation's artifact can be reconciled MECHANICALLY, in both directions, rather than the
# moved set being listed by hand — which is what that ruling asks for in its own words.
RULING_56_GROUND = "D-639's reach derivation, applied by the user's Ruling 56"

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
    "OI-370": (GATES, "the default - the row's own text does not settle its subject",
               "A MANDATORY SESSION-START READ CANNOT BE PERFORMED: `CLAUDE.md` names `STATUS.md` "
               "among the three files every session reads and forbids relying on memory for "
               "baselines or iteration state, and the file tools refuse the file. THE FIRST-CUT "
               "CLASSIFICATION REACHED THIS ROW and the verdict is authored for it here, which is "
               "what the tool requires; no non-gating verdict is hand-added, which is the act the "
               "record forbids. WHAT DECIDES IT IS THE DECLARATION'S OWN DEFAULT, and that is said "
               "plainly rather than argued around: the row states BOTH readings and settles "
               "neither, in its own words -- the subject is the record's own apparatus, which the "
               "declaration classes non-gating, but the consequence is that a session may not know "
               "the analysis's current state, and D-438's second half reaches a statement about "
               "the analysis or its build state -- and it ends 'Left for the derivation.' A row "
               "whose subject its own text does not settle GATES, because the declaration only "
               "ever removes a wait where the row supports removing it. The two readings pull "
               "opposite ways on the apparatus line itself: what is OWED reads as apparatus (a "
               "filing act under the file's own archive rule, or a size guard), while what the row "
               "ESTABLISHES is that a governing instruction cannot be carried out at all. NOT an "
               "establishment obligation (#19), which would override the criterion whatever the "
               "subject: the size guard's own establishment would be owed BY that check if it were "
               "ever built, which is a condition on a future act rather than an obligation "
               "standing now -- the same distinction that keeps [[OI-364]] off the exemption. "
               "★ ITS FIRST REMEDY HAS ALREADY RUN AND THE ROW SURVIVED IT: the archive rule was "
               "applied and the read failed again, which is why the row is still open and why the "
               "verdict is made on the row as it stands rather than on the remedy proposed for "
               "it. Distinct from the retired [[OI-47]], which was four SECTIONS of that file "
               "contradicting the governing documents; this is the file's accumulation against its "
               "own archive rule, and the two rows say so of each other.",
               "RESOLVED 2026-08-17 - the row's SECOND remedy ran and the read succeeded "
               "(`cc_instruction_preparation_sixth.md` Task 1, executing Ruling 4 of "
               "`cowork_rulings_2026_08_17_governing_surface_split.md`). THE VERDICT WAS CORRECT "
               "WHILE IT STOOD and is kept whole (#12); it is retired because the row closed, "
               "never because it was wrong. ★ WHAT THE CLOSING ACT SUPPLIED IS EXACTLY WHAT THE "
               "VERDICT SAID THE ROW LACKED: the verdict rests on the row settling neither "
               "reading, and the row's first remedy had already run without closing it because "
               "the archive rule never defined which entries count as superseded. The user's "
               "Ruling 4 defines it - an entry is superseded the moment a later batch's close "
               "exists - and the read was then re-attempted and succeeded, which is the row's own "
               "closing condition tested rather than assumed (#19)."),
    "OI-47": (GATES, RULING_56_GROUND,
              "★ RE-CLASSED 2026-08-11 by the user's Ruling 56 of "
              "`cowork_rulings_2026_08_11_twelfth_stop.md`, which APPLIES D-639's reach derivation "
              "over the apparatus-classed rows; the former NON-GATING verdict is preserved whole at "
              "`superseded_verdicts` (#12), and WHICH rows move is DERIVED from that derivation's "
              "own artifact and reconciled here in both directions rather than listed by hand. The "
              "derivation put this row INSIDE the doc-sync half under D-639's fallback (1A), and "
              "the ground is that four superseded status sections carry MEASURED VALUES about the "
              "analysis which the governing hard stop supersedes - so a reader of the current-state "
              "section is told the system's error counts are values no measurement now supports. "
              "The owed act is unchanged and is the row's own: annotate, do not rewrite history.",
              "RESOLVED 2026-08-11 - the BANNER half was performed at the objects "
              "(`cc_instruction_status_touch_and_oi141_premise_repin.md` Task 2), all four "
              "submission-era sections carrying a dated HISTORICAL banner and not one line below "
              "any banner edited. THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole (#12); "
              "it is retired because the row closed, never because it was wrong. ★ ITS GROUND IS "
              "WHAT THE CLOSING ACT TURNED OUT TO NEED: the verdict graded the row on the sections "
              "carrying MEASURED VALUES the governing hard stop supersedes, and the banner the act "
              "wrote is exactly a statement that those acceptance numbers and hard stops are "
              "superseded in whole - so a verdict written against the subject survived a closing "
              "act that happened in a DIFFERENT FILE from the one this row's own citations named. "
              "WHAT THE CLOSURE DOES NOT DISCHARGE: [[OI-370]], the file's accumulation against its "
              "own archive rule, which the row's own text keeps apart from this one and which "
              "carries its own verdict above; and one false-at-HEAD clause found while bannering, "
              "named at its banner and carried at [[OI-315]] rather than corrected below it."),
    "OI-282": (GATES, RULING_56_GROUND,
               "★ RE-CLASSED 2026-08-11 by the user's Ruling 56, which APPLIES D-639's reach "
               "derivation; the former NON-GATING verdict is preserved whole at "
               "`superseded_verdicts` (#12), and WHICH rows move is DERIVED from that derivation's "
               "artifact and reconciled here both ways. This is the one of the three the test "
               "decided WITHOUT reaching the fallback: it is D-639's SECOND WORKED EXAMPLE word for "
               "word - a missing supersession note on a superseded plan - and the consequence is "
               "the one that example is about, a reader sent there by two live specifications "
               "being told the categories are still to be discovered when they are discovered, "
               "ratified and compiled in. The owed act is unchanged: an annotation, not a rewrite.",
               "RESOLVED 2026-08-11 - the act the verdict's own last sentence names was performed "
               "(`cc_instruction_return_continuation_14.md` Task 3): a dated scope annotation, not "
               "a rewrite. THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole; it is retired "
               "because the row closed, never because it was wrong. Its last clause is worth one "
               "line - a verdict that names the SHAPE of the owed act as well as the class turns "
               "out to be the one a later session can act on without re-deciding anything."),
    "OI-304": (GATES, "a statement about the analysis's build state",
               "Two dated annotations assert that the owed iteration-API renames have a subject "
               "including LIVE Layer-1.5 code; D-428 was corrected against the call sites one wave "
               "later and records that every use sits on the legacy arm. What is owed is the "
               "correction of a statement about which code is live - the same D-438 clause as "
               "[[OI-303]], not a filing or a pointer.",
               "RESOLVED 2026-08-11 - a dated CORRECTION REMARK was written beside each of the two "
               "annotation blocks, naming D-428's corrected text, with neither block edited "
               "(`cc_instruction_return_continuation_14.md` Task 3). THE VERDICT WAS CORRECT WHILE "
               "IT STOOD and is kept whole; it is retired because the row closed. Its own last "
               "clause held at the act: what was owed was the correction of a statement about "
               "which code is live, and the remedy's being an annotation rather than an edit did "
               "not make it a filing act."),
    "OI-318": (GATES, RULING_56_GROUND,
               "★ RE-CLASSED 2026-08-11 by the user's Ruling 56, which APPLIES D-639's reach "
               "derivation; the former NON-GATING verdict is preserved whole at "
               "`superseded_verdicts` (#12), and WHICH rows move is DERIVED from that derivation's "
               "artifact and reconciled here both ways. The derivation reaches this row under the "
               "fallback and through its FIRST half only: the Layer-6 paragraph is not the "
               "document's account of ITSELF at all - it tells a reader what a LAYER PRODUCES, and "
               "a reader of it alone is told the grouping layer segments melodic phrases, which the "
               "ratified design exists to deny. THE SECOND HALF IS NOT RE-CLASSED WITH IT and is "
               "recorded so the row is not read as gating on both: one section number used twice is "
               "a numbering artifact and would be OUT on its own.",
               "RESOLVED 2026-08-11 - both items corrected "
               "(`cc_instruction_return_continuation_14.md` Task 3), and the verdict's own split "
               "survived the act intact: the Layer-6 paragraph now names the punctuation-span at "
               "all three of its uses, which is the half the derivation reached, and the duplicated "
               "section number was renumbered as the numbering artifact this verdict said it was. "
               "THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole. What the closure does NOT "
               "discharge: OI-229's scoped terminology pass, which is untouched - this act "
               "corrected two labels, not a class."),
    "OI-332": (GATES, "a statement about the analysis's build state",
               "★ RE-CLASSED 2026-08-07 by the user's ruling (dispatch "
               "`cc_instruction_five_rulings.md` §0a, R5); the former NON-GATING verdict is "
               "preserved whole at `superseded_verdicts` (#12), and the row that found the defect "
               "is [[OI-336]], which closes on this act. The row cut its own class from the FIRST "
               "HALF of D-438's line -- the half naming a pointer, an anchor, a label and a banner "
               "as apparatus. THE SAME SENTENCE CONTINUES: 'a correction to a statement about the "
               "analysis OR ITS BUILD STATE, or the completion of a specification, GATES' -- and "
               "that half reaches two of the three documents. `cowork_layer1_extend_design.md` "
               "carries a 'Read-only design -- no code' banner over two operations the row itself "
               "verified BUILT at the header: a banner asserting that a design has no code, over "
               "code that exists, IS a statement about the build state, and the fact that a banner "
               "is the vehicle does not change what it states. `docs/stage4c_cadence_key_design.md` "
               "carries no note that the approach it builds toward was falsified (D-290), which is "
               "a statement about the analysis. The third item, a drifted code anchor, is apparatus "
               "on both halves and carries the row neither way. The row takes the STRONGEST of its "
               "instances, as OI-334's verdict does. Recorded against the row's SUBJECT, never its "
               "remedy.",
               "RESOLVED 2026-08-11 - all three items performed across two tasks of one batch "
               "(`cc_instruction_return_continuation_14.md` Tasks 2 and 3): the falsified design "
               "re-bannered under the user's Ruling 62, the 'no code' banner corrected to AS-BUILT, "
               "and the drifted anchors RE-AIMED AT FUNCTIONS rather than re-numbered. THE VERDICT "
               "WAS CORRECT WHILE IT STOOD and is kept whole; it is retired because the row closed. "
               "★ ITS THIRD-ITEM READING IS VINDICATED IN AN UNEXPECTED WAY: it called the drifted "
               "anchor apparatus on both halves, carrying the row neither way -- and the act "
               "confirmed exactly that by treating it as a locator question, replacing the line "
               "numbers with function names rather than refreshing them, because the drift sat "
               "inside a CORRECTION of an earlier citation and re-numbering would only have reset "
               "the clock."),
    "OI-320": (GATES, "the criterion - the row's subject bears on an instrument",
               "A corpus/score inventory names the SUPERSEDED batch case-identity sets as the "
               "current acceptance gate, three times, and tells the reader the granularity-robust "
               "metric does not exist yet. That is a statement about an instrument a measurement "
               "depends on and about the analysis's build state, which D-438's line inside the "
               "documentation rows puts on the gating side; and the document is the one CLAUDE.md "
               "makes a mandatory first read for any task that touches scores, so a session is "
               "pointed at the retired gate before it reads anything else.",
               "RESOLVED 2026-08-11 - the user's Ruling 62 "
               "(`cowork_rulings_2026_08_11_fourteenth_stop.md`) supplied the filing decision the "
               "row said no session could take: this document is a LIVE GOVERNING SURFACE, so its "
               "BODY is corrected rather than re-bannered, and all four sites now POINT at the "
               "block that owns each -- the governing stop at gate block (A), the retired batch "
               "diagnostic at block (C) -- with no figure restated (D-431) and every former wording "
               "preserved at the correction (#12). THE VERDICT WAS CORRECT WHILE IT STOOD and is "
               "kept whole; it is retired because the row closed, never because it was wrong. Its "
               "own last clause is what the act turned on: the cost was that a session is pointed "
               "at the retired gate BEFORE it reads anything else, and the sentence saying the "
               "granularity-robust metric was still roadmap work was the sharpest form of that."),
    "OI-322": (GATES, "the criterion - the row's subject bears on the analysis",
               "A completed audit describes five pieces of analysis-tool code in the present tense "
               "-- with call-site line citations and three open questions -- that its own last line "
               "says were deleted. The subject is what the code does and whether a symbol may reach "
               "the analyzer, not a banner or a label: D-438's apparatus line does not reach it. "
               "(The document's FILING -- re-banner as a historical record or rewrite -- is "
               "apparatus, but it is the remedy's shape, not the row's subject.)",
               "RESOLVED 2026-08-11 - the user's Ruling 62 answered the filing question this row "
               "posed for the whole class: BRANCH ONE, a completed audit is re-bannered as a "
               "historical record and its body is never rewritten. The banner names the date, the "
               "state audited, the fate of the subject and the deleting commit; the body is "
               "untouched (#12). THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole -- and "
               "its parenthesis is worth one line, because it drew exactly the distinction the "
               "ruling then ruled on: the FILING is apparatus, the row's SUBJECT is not, and a "
               "verdict recorded against the subject survives whichever filing the user chooses. "
               "WHAT THE CLOSURE DOES NOT DISCHARGE: the row's wider half -- every completed audit "
               "in the tree -- is answered by a DERIVED enumeration whose reach is stated rather "
               "than measured and which is declared NOT SOUND against its seeds; that is a bound, "
               "not a completeness claim."),
    "OI-324": (GATES, "the criterion - the row's subject bears on what the emission reads",
               "Whether the priority-of-evidence ranking binds the production emission or only the "
               "legacy key path is a question about the evidential contract the joint emission is "
               "measured against -- OI-228 puts that very premise under load. Nothing about it is "
               "apparatus. The row's smaller second half (an unqualified predicate in the same "
               "paragraph pair) would be apparatus on its own and does not lift the row.",
               "RESOLVED 2026-08-11 - the user's Ruling 63 "
               "(`cowork_rulings_2026_08_11_fourteenth_stop.md`) ruled reading (i): the ranking is "
               "CROSS-CUTTING and binds BOTH arms, and the rule is now stated for the production "
               "arm where the emission's evidential contract lives, under the registered homing "
               "procedure D-668 (step 1 tried and declined, kind half judged before the write). The "
               "smaller second half was corrected under the same ruling's licence. THE VERDICT WAS "
               "CORRECT WHILE IT STOOD and is kept whole (#12); it is retired because the row "
               "closed, never because it was wrong -- and it is worth one line that the verdict's "
               "own reasoning is what the ruling confirmed: it graded the row on the SUBJECT being "
               "the evidential contract the emission is measured against, and the user ruled "
               "exactly that question rather than the wording one. WHAT THE CLOSURE DOES NOT "
               "DISCHARGE: OI-228, the departure this premise measures the code against, which "
               "remains a conformance gap DECLARED and whose remedy belongs to the ONE design over "
               "the struck-versus-sounding family at its #8-correct stage."),
    "OI-369": (GATES, "the criterion - D-438's own line puts the completion of a specification on "
                      "the gating side, and the default on doubt is to keep the wait",
               "The phase-1 finish line's last homing item counts one register entry and names, as "
               "the act that closes it, a write the user's own ruling forbids: the entry is "
               "SUPERSEDED, and a supersession is register business with no specification home "
               "owed. THE FIRST-CUT CLASSIFICATION REACHED THIS ROW and the verdict is authored "
               "for it here, which is what the tool requires; no non-gating verdict is hand-added, "
               "which is the act the record forbids. IT IS NOT SETTLED BY THE APPARATUS "
               "CRITERION, and that is said plainly rather than argued around: the surface is a "
               "derived completion map, which reads as this project's own tracking. What decides "
               "it is D-438's line INSIDE the documentation rows, which puts the completion of a "
               "specification on the gating side because the phase-1 rule makes specifications "
               "COMPLETE and TRUE the thing that precedes everything else -- and what is owed here "
               "is not a pointer, an anchor, a label, a banner or a section boundary, but the "
               "question of whether one specification-completion obligation is owed at all. The "
               "declaration's own default carries the remainder: a row whose subject its own text "
               "does not settle GATES, because the declaration only ever removes a wait where the "
               "row supports removing it. Recorded against the row's SUBJECT, never its remedy -- "
               "the two closing acts it names are a subtraction in a derivation and a correction "
               "to an authored closing act, and choosing between them is a mechanism question "
               "D-436 reserves to the user.",
               "RESOLVED 2026-08-11 - the user's Ruling 61 "
               "(`cowork_rulings_2026_08_11_fourteenth_stop.md`) ruled the FIRST of the two closing "
               "acts: the item gains the same D-642 subtraction its four sibling items apply, one "
               "machinery per concern (#6). THE VERDICT WAS CORRECT WHILE IT STOOD and is kept "
               "whole (#12); it is retired because the row closed, never because it was wrong. ★ "
               "ITS LAST SENTENCE IS THE ONE WORTH KEEPING: it recorded the verdict against the "
               "row's SUBJECT and never its remedy, on the ground that choosing between the two "
               "closing acts is a mechanism question D-436 reserves to the user -- and the user "
               "chose. A verdict written against a remedy would have had to be re-authored when the "
               "remedy was picked; one written against the subject is simply retired."),
    "OI-303": (GATES, "a statement about the analysis's build state",
               "Six comments in src/ and tools/ say the record arm is 'default OFF' and that the "
               "record section adapter has no caller. D-438's line inside the documentation rows "
               "makes a correction to a statement about the analysis or its BUILD STATE gating, "
               "and every one of the six is exactly that - they are where a reader goes to learn "
               "which analysis arm runs, and all six name the dormant one.",
               "RESOLVED 2026-08-11 - all six claims are discharged and every one was verified AT "
               "THE FILES by the closing session rather than at any record of them "
               "(`cc_instruction_return_continuation_13.md` Task 2). Five were corrected by the "
               "user's Ruling 16, the one licensed comment-only `src/` act; the sixth was corrected "
               "in two halves under Rulings 48 and 59, the second half being a SECOND block of the "
               "same file that the first correction did not reach - which is why the row survived "
               "an act that appeared to close it. THE VERDICT WAS CORRECT WHILE IT STOOD and is "
               "kept whole: what it graded was the SUBJECT, and the subject was a statement about "
               "which analysis arm runs, which is exactly what D-438's line puts on the gating "
               "side. It is retired because the row closed, never because it was wrong. WHAT THE "
               "CLOSURE DOES NOT DISCHARGE is carried forward rather than lost: the enumeration "
               "that located these six had no measured reach against the text it scans, so its "
               "empty verdict bounded nothing - that is OI-368, closed separately by a ruling that "
               "BOUNDED the pattern rather than measuring it, and its closure is explicitly not a "
               "claim that the pattern has been measured."),
    "OI-276": (GATES, "specification truth",
               "Three live-specification documents state as current what is false at HEAD, and "
               "one names as its acceptance criterion, five times, a regression gate superseded "
               "in whole. A stale criterion is not a description - it is what a future build "
               "would try to satisfy.",
               "RESOLVED 2026-08-11 - the three doc-sync acts were performed, one per document, "
               "each complete in itself (`cc_instruction_return_continuation_11.md` Task 1). The "
               "as-built banner over a dormant mechanism and the missing supersession note on a "
               "revisited shelving are D-639's first two worked examples word for word; the stale "
               "acceptance criterion is decided under the fallback and said so, and is corrected "
               "by POINTING at CLAUDE.md gate block (A) rather than by restating any criterion "
               "(#6, D-431). Its two AS-BUILT-RECORD sites were QUALIFIED rather than rewritten, "
               "because what that 2026-07-03 build was proven against is TRUE as a record and "
               "false only if read as the gate a later change reproduces. Every former wording is "
               "preserved in place (#12). The verdict was correct while it stood and is kept "
               "whole; it is retired because the row closed, never because it was wrong. WHAT THE "
               "CLOSURE DOES NOT DISCHARGE is carried on the row rather than lost: whether a "
               "sweep for this class rides the remaining unread LIVE-SPEC reads or runs as its "
               "own pass is a SCOPING CALL the row reserves to the user, and the three edits "
               "close three instances rather than the class.",
    ),
    "OI-298": (NON_GATING, "user",
               "A binding rule POINTS at an enumeration the user has not ratified. What is owed "
               "is a pointer and a ratification status - the user's own apparatus examples - and "
               "the six subjects the clause itself names bind on the clause's own authority "
               "either way, so nothing about the analysis or its inputs turns on the ruling. It "
               "is deliberately NOT read as specification completion: no specification is "
               "incomplete or false here, and the clause was left unchanged precisely so that "
               "remains true.",
               "LEFT THE OPEN POPULATION 2026-08-11 - and the reason is worth reading, because "
               "the row's own text had recorded its closure since 2026-08-03 while its status "
               "cell opened with an open-state token, so every derivation over the index counted "
               "it OPEN. That is OI-367's finding, and the user's Ruling 53 of "
               "`cowork_rulings_2026_08_11_eleventh_stop.md` corrected the opening token PER THE "
               "CELL'S OWN WORDS under the both-ways discipline, the named row the only permitted "
               "mover. The verdict was correct while it stood and is kept whole; it is retired "
               "because the row left the cut, never because it was wrong - and NOT because the "
               "row resolved on 2026-08-11: it resolved on 2026-08-03 and said so, and what "
               "changed here is that the index now reads what the cell already said. WHAT THE "
               "CORRECTION DOES NOT DISCHARGE is carried forward rather than lost: the family's "
               "enumerating pattern still owes a measured miss rate over the openings the index "
               "actually uses (D-436's detection-rate condition, D-661's completeness rule), and "
               "that gap is recorded on OI-367's own row on the ruling's direction rather than "
               "opened as a new one.",
    ),
    "OI-230": (NON_GATING, "user",
               "The writing-standards conformance question, and the user has already DEFERRED it "
               "to a discussion. Its subject is how this project's documents are written.",
               "RESOLVED 2026-08-09 - the deferral ended and all three of the row's questions were "
               "ruled at the fifth STOP (`cowork_rulings_2026_08_09_fifth_stop.md`): the "
               "fourteen-section structure is KIND-SCOPED with its kind list enumerated in "
               "`cowork_design_doc_template.md` and a STOP on an unlisted kind (Ruling 28); "
               "documents are IN the conformance enumeration for a named MECHANICAL subset "
               "(Ruling 29) while the deep half is ruled KNOWLEDGE and that limb closes "
               "(Ruling 32); and the terminology cleanup is scoped -- no tree-wide rename, scanner "
               "first, then ruled batches, research-tied names governed by a two-tier rule "
               "(Rulings 30 and 31). The verdict was correct while it stood and is kept whole; it "
               "is retired because the row closed, never because it was wrong. WHAT THE CLOSURE "
               "DOES NOT DISCHARGE is carried forward rather than lost: the owed mechanical check "
               "is OI-364, and the cleanup itself stays open at OI-229 with its ruled scope on it.",
    ),
    "OI-358": (GATES, "two independent grounds - D-438's line, and the clause that overrides the "
                      "criterion (an establishment obligation, #19, always gates)",
               "Five consecutive register entries quote a DIFFERENT rule than their own title, "
               "restatement and defense describe; one quotes a section heading. THE FIRST-CUT "
               "CLASSIFICATION IS RIGHT ABOUT THE SUBJECT -- this is the decisions register's own "
               "content -- and is not disputed. TWO THINGS DECIDE IT ANYWAY, either sufficient. "
               "(1) D-438's line inside the documentation rows puts a correction to a statement "
               "about the analysis on the gating side, and what is owed here is not a pointer, an "
               "anchor, a label, a banner, a filing decision or a section boundary: five entries "
               "STATE ONE RULE'S IDENTITY OVER ANOTHER RULE'S WORDS, so a reader of the register "
               "learns the wrong rule about the scorer. (2) Independently an establishment "
               "obligation: the register's own verbatim check and the disposition verifier BOTH "
               "PASS over the corrupted pairs, because once the verbatim is the text at the "
               "drifted line the two agree with each other permanently -- so two green verdicts do "
               "not bound what they appear to bound, which is the shape #19 refuses. Recorded "
               "against the row's SUBJECT, never its remedy -- and the remedy is deliberately "
               "open, since whether a corrupted verbatim is re-taken from the correct bullet or "
               "the wrong quote is preserved beside it (#12) is a filing judgment about the "
               "register's own unit.",
               "RESOLVED 2026-08-09 - the user ruled the filing judgment the row reserved "
               "(Ruling 24 of `cowork_rulings_2026_08_09_fourth_stop.md`): the five quotes are "
               "RE-TAKEN from the bullets their titles and defenses describe, with the former "
               "quote and former anchor preserved in each entry's provenance (#12) and one quote "
               "in the load-bearing field (#6). The verdict was correct while it stood and is kept "
               "whole; it is retired because the row closed, never because it was wrong. ITS "
               "SECOND GROUND IS NOT DISCHARGED BY THAT CLOSURE and does not disappear with this "
               "retirement: both checks are still satisfied by a corrupted pair, and that "
               "obligation is carried forward at OI-360 with its own verdict above.",
    ),
    "OI-354": (GATES, "the clause that overrides the criterion - an establishment obligation (#19) "
                      "always gates, whatever its subject, including one whose subject is this "
                      "project's own tracking apparatus",
               "The legacy-mark verification's authored verdict table no longer covers the derived "
               "legacy-marked set, and OI-289's status of record is a completed VERIFICATION over "
               "that set. So a verification recorded as established describes a population smaller "
               "than the one it names. THE FIRST-CUT CLASSIFICATION IS RIGHT ABOUT THE SUBJECT and "
               "is not disputed: the subject is the decisions register's own verification "
               "apparatus, it bears on no analysis, no analysis input and no measurement tool any "
               "measurement of the analysis depends on, and the documentation criterion alone would "
               "put it outside the gate. WHAT DECIDES IT IS THE OTHER CLAUSE, stated once in "
               "`CLAUDE.md`'s own non-gating declaration and not discretionary there: an "
               "establishment obligation always gates, whatever its subject, and the declaration "
               "names an obligation whose subject is the open-items register itself as covered. "
               "This is one -- #19 exists because a thing merely unfalsified is not established, "
               "and this claim was unfalsified only because the tool that would have falsified it "
               "was stopping earlier on an unrelated drifted citation. Backgrounding it is how it "
               "never happens, which the declaration gives as its own reason for the clause. "
               "Recorded against the row's SUBJECT, never its remedy -- and the remedy is "
               "deliberately open, since who may author the owed per-entry verdicts is exactly what "
               "the row leaves to the user.",
               "RESOLVED 2026-08-09 - the user ruled the question the row reserved (Ruling 18 of "
               "`cowork_rulings_2026_08_09_third_stop.md` settled WHOSE act the establishment is; "
               "Ruling 23 of `cowork_rulings_2026_08_09_fourth_stop.md` ratified the reviewed "
               "verdict set and ordered it applied). The verdict was correct while it stood and is "
               "kept whole (#12); it is retired because the row closed, never because it was wrong "
               "- and its own ground held to the end, since what discharged the row was the "
               "establishment it named, performed by one session and cleared by another act on the "
               "user's ruling, which is the separation D-655 records."),
    "OI-300": (GATES, "an establishment obligation (#19) - the exemption, not the criterion",
               "Its whole subject is a mechanism's MEASURED false-deny and detection rates over "
               "two shapes its corpora do not contain. Classified GATES on the exemption alone, "
               "and the exemption is what makes the classification easy: an establishment "
               "obligation always gates whatever its subject, because backgrounding one is how "
               "it never happens. The apparatus test is not reached and is not applied.",
               "RESOLVED 2026-08-08 - the owed establishment run was performed and all five "
               "shapes are answered by the ONE design the user ruled that day "
               "(`cowork_ruling_guard_family_2026_08_08.md`), corpus first. The verdict was "
               "correct while it stood and is kept whole (#12); it is retired because the row "
               "closed, never because it was wrong - and its own ground held to the end, since "
               "what discharged the row was the establishment run it named."),
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
    "OI-331": (GATES, "the criterion - the row's subject bears on the analysis's inputs",
               "A LIVE, user-ratified register entry names a convergence proxy the build MEASURED "
               "FALSE and dropped, and the entry carries no annotation. The subject is a binding "
               "contract rule about HOW MUCH MUSIC THE ANALYSIS READS before it commits to a key "
               "-- the analysis's own input scope, which is the strongest form D-438's test has. "
               "A session applying the rule as written would build a stop condition already "
               "measured not to work. Nothing about it is apparatus: what is owed is not a "
               "pointer, an anchor or a filing choice but the correction of a rule, which "
               "D-438's line inside the documentation rows puts on the gating side in terms.",
               "RESOLVED 2026-08-07 (ruling R3) - the user struck the proxy clause and its worked "
               "example from the signed contract document, which now states the current behaviour "
               "in its own voice and records the struck clause as tried and closed with D-622 "
               "named as superseding it; D-261's headline rule, its home and its ratified status "
               "are unchanged and its verbatim is re-taken from the edited home with the former "
               "verbatim preserved (#12). The verdict was correct while it stood and is kept whole; "
               "it is retired because the row closed, never because it was wrong."),
    "OI-353": (GATES, "the criterion - a statement about the analysis's BUILD STATE, which D-438's "
                      "line inside the documentation rows puts on the gating side",
               "Six comments in `src/` describe the production notation record path as DEFAULT OFF "
               "while the configuration sets its default to true and says so in the comment beside "
               "the call. WHAT IS OWED decides it, and what is owed is not a pointer, an anchor, a "
               "label, a banner, a filing decision or a section boundary: it is the CORRECTION OF "
               "A STATEMENT ABOUT WHICH ANALYSIS ARM RUNS, and D-438's own line names a correction "
               "to a statement about the analysis or its build state on the gating side in those "
               "words. Which arm ships is the strongest form that statement has -- these are the "
               "comments a session reads when the never-work-from-memory rule sends it to the code "
               "for exactly that question, and they answer it wrongly in six places. It is the "
               "same class as OI-304, whose verdict is GATES on the same clause, and the same "
               "class as the resolved OI-232 one surface over -- that row found the identical "
               "staleness in ARCHITECTURE.md and closed on the document half only, leaving the "
               "code half nobody had looked at. NOT an establishment obligation (#19): no rate, "
               "instrument or measurement is affected, and no comment is executable -- the "
               "behaviour is what the configuration says. Recorded against the row's SUBJECT, "
               "never its remedy; the remedy is a `src/` edit no wave under the phase-1 freeze may "
               "make.",
               "RESOLVED 2026-08-09 (`cc_instruction_return_continuation_8.md` Task 4) on the "
               "user's Ruling 16 of 2026-08-09, BOTH halves in the ruling's own order. The SWEEP "
               "ran first and enumerated the family by derivation -- every `src/` comment block "
               "making a dormancy, no-consumer or flag-default claim AND naming the joint module "
               "or the notation record, graded against two configuration facts re-read at the code "
               "on every run (tools/audit/arm_comment_sweep.json). It CONFIRMED the ruling's own "
               "prediction that this row's six sites are the found members and not the family: the "
               "largest false group declares the JOINT MODULE'S OWN dormancy, which this row never "
               "named. Then ONE comment-only commit corrected every FALSE-AT-HEAD block, its diff "
               "verified comment-only mechanically; ten blocks whose falsity needs the CALL GRAPH "
               "rather than a file-level fact are HELD, not edited, by the ruling's own clause. "
               "The verdict above was correct while it stood and is kept whole (#12); it is "
               "retired because the row closed, never because it was wrong."),
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
    "OI-150": (GATES, "an instrument a measurement depends on",
               "The recorded test baselines are stale and the notation line hides four xfails. A "
               "baseline is what a regression is measured against.",
               "RESOLVED 2026-08-13 - both halves performed at the objects "
               "(`cc_instruction_oi150_baselines.md` Tasks 1 and 2): the two suites were BUILT and "
               "RUN at HEAD, both `BUILD_AND_TEST.md` baselines were written from those runs and "
               "from nothing else, and the notation line now names all four xfails by test name "
               "with the standing do-not-re-bless instruction and a pointer to their one home. THE "
               "VERDICT WAS CORRECT WHILE IT STOOD and is kept whole (#12); it is retired because "
               "the row closed, never because it was wrong. ★ ITS GROUND IS WHAT THE CLOSING ACT "
               "TURNED OUT TO NEED: the verdict graded the row on an INSTRUMENT rather than on "
               "filing, and the act that closed it was accordingly a MEASUREMENT and not a wording "
               "change - the earlier wave that touched the file and declined to re-stamp declined "
               "for exactly that reason, having run no suite. WHAT THE CLOSURE DOES NOT DISCHARGE: "
               "[[OI-148]], the four xfails themselves, still failing by design and still owned by "
               "the key-layer build - naming them in a baseline line neither fixes nor re-blesses "
               "them."),
    "OI-315": (GATES, "a statement about the analysis's build state",
               "The canonical specification describes a key-layer behaviour in the present tense "
               "that the code removed on 2026-06-14, and register entry D-058 carries it LIVE. "
               "D-438's line inside the documentation rows makes a correction to a statement about "
               "the analysis or its BUILD STATE gating, and this is one with a live register entry "
               "riding on it -- the same clause as OI-303 and OI-304, one surface further in.",
               "RESOLVED 2026-08-13 - both halves closed "
               "(`cc_instruction_oi315_class_licence.md`, Tasks 1-3): the specification and the "
               "register entry on 2026-08-04, the design document and the two dated reports at "
               "commit d9f674e0ec, the one `src/` comment this row names at commit 65f2f2b86f "
               "under the user's FIRST `src/` licence, and the remaining `src/` comments of the "
               "same class at commit 7b802ec4a5 under the SECOND. THE VERDICT WAS CORRECT WHILE IT "
               "STOOD and is kept whole (#12); it is retired because the row closed, never because "
               "it was wrong. * ITS GROUND IS WHAT THE CLOSING ACTS TURNED OUT TO NEED: the "
               "verdict graded the row on a statement about the analysis's BUILD STATE, and every "
               "closing act was exactly a correction of such a statement - including the last one, "
               "which corrected a PRODUCTION HEADER's parameter comment that no account of this "
               "row had named, the earlier ones having confined the `src/` residue to the test "
               "file. WHAT THE CLOSURE DOES NOT DISCHARGE: the `KeyResolveDump::candidates` "
               "comment's 'empty on fallback' half, reported at the row as a finding about a "
               "different subject and deliberately not corrected under a licence that does not "
               "reach it."),
    "OI-45": (GATES, "specification completeness",
              "Half of it is stale anchors, which would be apparatus - but the other half is a "
              "scoring constant with no entry in the scoring specification at all, and phase 1 "
              "requires specifications COMPLETE, not only true. The whole row gates with its "
              "gating half.",
              "RESOLVED 2026-08-14 - both halves closed in one pass over "
              "`docs/scoring_model.md` (`cc_instruction_scoring_model_pass.md` Task 2, commit "
              "b366d44947). THE VERDICT WAS CORRECT WHILE IT STOOD and is kept whole (#12); it is "
              "retired because the row closed, never because it was wrong. * ITS GROUND IS WHERE "
              "THE VERDICT AND THE ROW PARTED COMPANY, AND THE VERDICT WAS THE MORE ACCURATE OF "
              "THE TWO: it gated the row on specification COMPLETENESS, on the ground that a "
              "scoring constant had no entry at all - and read at the document, the entry EXISTS. "
              "What was actually wrong was WHERE the entry said the bonus fires (the "
              "bias-correction block, not the enharmonic-flip block or the G-family region), "
              "which is specification TRUTH rather than completeness. So the row gated on a half "
              "that was already met and was closed by correcting a different defect at the same "
              "place; the anchor half, which the verdict rightly called apparatus, was closed "
              "beside it. * AND THE ANCHOR HALF WAS WRONG ABOUT ITS OWN SECTIONS: the raw "
              "line-number anchors stood in the overview, the matrix section, the terms section, "
              "the joint-scoring section AND the inversion-correction section - not the two the "
              "row names, whose gate section carried none at all, its location column having "
              "already been converted to named code regions (the document does not date that "
              "conversion, so its ordering against the row is NOT established and is not claimed). "
              "Enumerating at the document rather than from the row's list is what found "
              "both, and is why the dispatch required it."),
    "OI-183": (GATES, "specification completeness",
               "Twelve of thirty-two override-registered scoring constants have no by-name "
               "mention in the scoring specification. Incompleteness of a specification, the "
               "same ground as OI-45.",
               "RESOLVED 2026-08-14 - the twelve get a by-name table in the terms section, each "
               "with the site it acts at and, where the specification already describes its "
               "effect without naming it, the cell or prose that covers it - the row's own stated "
               "alternative, taken as an equal outcome (`cc_instruction_scoring_model_pass.md` "
               "Task 2, commit b366d44947). THE VERDICT WAS CORRECT WHILE IT STOOD and is kept "
               "whole (#12); it is retired because the row closed, never because it was wrong. * "
               "ITS GROUND WAS EXACTLY RIGHT AND THE CLOSING ACT NEEDED NOTHING ELSE: the verdict "
               "graded the row on specification completeness, and completing the specification is "
               "the whole of what was done. * WHAT THE CLOSURE CORRECTS IN THE ROW'S OWN "
               "ACCOUNT, and therefore in this verdict's opening sentence, which took its "
               "population figure from it: the TWELVE reproduce exactly at HEAD, but the "
               "POPULATION does not - the scorer's translation unit registers one fewer name than "
               "the row gives it, and the progression constants registered through the same "
               "registry from the function layer are excluded from the row's population "
               "altogether, though the specification already names every one of them so none is "
               "a gap. The outcome is unchanged; the count is not the row's."),
}

# Verdicts a USER RULING has RE-CLASSED. Distinct from RETIRED_VERDICTS in both directions: there
# the row CLOSED and left the population, here the row stays open and stays a first-cut candidate
# while the answer changes. The live verdict is in V; the verdict that stood before it is kept whole
# here (#12) with the ruling that replaced it, because a verdict overwritten in place is a reasoning
# the next session re-derives -- the same ground the retired table gives for itself.
SUPERSEDED_VERDICTS = {
    "OI-47": (NON_GATING, "user",
              "The subject is four superseded sections of STATUS.md, a tracking surface, and the "
              "owed act is explicitly the BANNER half - marking them historical. The triage half, "
              "which was the part that touched what is true of the analysis, is discharged.",
              "RE-CLASSED GATES 2026-08-11 by the user's Ruling 56 of "
              "`cowork_rulings_2026_08_11_twelfth_stop.md`, which APPLIES D-639's reach derivation. "
              "The verdict is kept whole because it was right about the OWED ACT and the derivation "
              "asks a different question: not what is owed, but whether the document's account "
              "changes how its analysis content is read. What the derivation found is that those "
              "sections carry MEASURED VALUES about the analysis that the governing hard stop "
              "supersedes, so a reader of the current-state section is told the system's error "
              "counts are values no measurement now supports."),
    "OI-282": (NON_GATING, "user",
               "A PLAN document still presents as future work a half delivered and ratified the "
               "next day. The falsehood is real but it sits in a tracking surface: the analysis "
               "fact it concerns - the five-idiom set - is correctly recorded in the canonical "
               "document and in the register, so no specification of the analysis is wrong.",
               "RE-CLASSED GATES 2026-08-11 by the user's Ruling 56, applying D-639's reach "
               "derivation, which decided this row by the ruling's SECOND WORKED EXAMPLE word for "
               "word - a missing supersession note on a superseded plan. The verdict is kept whole "
               "because its reading of where the falsehood SITS is unchanged; what it did not ask "
               "is whether the document's account of itself changes how its analysis content is "
               "read, and the derivation's answer is that a reader sent there by two live "
               "specifications is told the categories are still to be discovered when they are "
               "discovered, ratified and compiled in."),
    "OI-318": (NON_GATING, "user",
               "Two LABELS in the canonical document: the Layer-6 section still calls the grouping "
               "unit a 'phrase' after the ratified rename reserved that word, and one section "
               "number is used twice. D-438's line names a label and an anchor as apparatus, and "
               "item (1) is already sequenced as its own scoped terminology work item under "
               "OI-229. Neither states anything false about what the analysis does.",
               "RE-CLASSED GATES 2026-08-11 by the user's Ruling 56, applying D-639's reach "
               "derivation, whose fallback (1A) reaches this row through its FIRST half. The "
               "verdict is kept whole because its reading of item (2) stands - a section number "
               "used twice is a numbering artifact and would be OUT on its own. What it read as a "
               "label, the derivation reads as a statement: the paragraph tells a reader what a "
               "LAYER PRODUCES, and a reader of it alone is told the grouping layer segments "
               "melodic phrases, which the ratified design exists to deny."),
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
               "obligation, so the starred clause does not reach it either.",
               "RE-CLASSED GATES 2026-08-07 by the user's ruling (dispatch "
               "`cc_instruction_five_rulings.md` §0a, R5), on the ground [[OI-336]] recorded: this "
               "verdict was cut from the FIRST HALF of D-438's line and the same sentence continues "
               "past it. The verdict was not wrong about what it read -- a banner and an anchor ARE "
               "named as apparatus -- and it is kept whole for that reason; what it did not read is "
               "the clause that decides two of the three documents."),
}

V = {
    # ------------------------------------------------------------------ NON-GATING
    "OI-46": (NON_GATING, "user",
              "What is owed is 'annotate the tables' - a consistency banner inside the "
              "structural-integrity audit, a tracking document. Nothing about the analysis is "
              "stated falsely by the tables; two records disagree about a stage's build status."),
    # OI-47's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
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
    "OI-364": (NON_GATING, "user",
               "The owed MECHANICAL half of the writing-standards conformance check, created when "
               "the user's Rulings 28/29/32 split that question: status-banner presence, "
               "terms-table presence on a new specification, and section structure judged against "
               "the enumerated kind list. All three read a DOCUMENT'S OWN STRUCTURE, so what is "
               "owed is a check over how this project's documents are written - the same subject "
               "the retired OI-230 verdict names, one construct out. CLASSIFIED WITH OI-297 AND "
               "APART FROM OI-292, and the difference is stated so the pair does not read as "
               "inconsistent: OI-292 gates because two of its members are MEASUREMENT rules and a "
               "third guards the local patches to MuseScore's own code, while every member of this "
               "row is a documentation-structure check that no measurement of the analysis "
               "depends on. AND IT IS NOT AN ESTABLISHMENT OBLIGATION, which would override the "
               "criterion whatever the subject: nothing here is a published rate or a trusted "
               "instrument awaiting establishment - the establishment #19 requires would be owed "
               "BY the check if it were ever built, which is a condition on a future act rather "
               "than an obligation standing now. The distinction is the same one that puts OI-359 "
               "on the gating side: there the missing mechanism enforces a MEASUREMENT convention, "
               "which is an instrument a measurement of the analysis depends on."),
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
    # OI-282's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
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
    # OI-298's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the row's opening token was
    # corrected under Ruling 53 and it left the open population.
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
    "OI-321": (GATES, "a statement about the analysis's build state",
               "A design document states three things as current that are false at HEAD, one of "
               "them a refactoring phase it calls DEFERRED which the code says was EXECUTED. "
               "D-438's line inside the documentation rows makes a correction to a statement about "
               "the analysis or its BUILD STATE gating, and a phase's execution status is that "
               "statement in its strongest form. THE ROW REACHED THIS CUT FOR THE FIRST TIME ON "
               "2026-08-09: it had SEVEN cells, its layer/gate column written twice, so the ONE "
               "index parser skipped it silently and it was in no population at all (OI-362). The "
               "user's Ruling 33 made a malformed row a STOP and the row was repaired in the same "
               "act, which is what put it here. Its own text already carried this verdict in "
               "words; authoring it for a row the cut DID reach is what the tool requires."),
    "OI-302": (GATES, "the default - the row's own scope does not settle it",
               "Half (a) IS apparatus: whether the decisions register gains a field for a mark "
               "whose subject is dormant while its prohibition is live. The other halves are not. "
               "Whether D-423's three prohibitions bind the LIVE design is a ruling about what the "
               "family design may do, and D-055's half is a factual question about production code "
               "(a preference registered unconditionally whose consumer is the legacy scorer). A "
               "row that is not wholly apparatus, or whose subject its own text does not settle, "
               "GATES by the declaration's own default - the declaration only ever removes a wait "
               "where the row supports removing it."),
    # OI-303's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
    # OI-304's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
    # OI-300's verdict moved to RETIRED_VERDICTS on 2026-08-08 when the row closed.
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
    # OI-318's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
    # ---------------------------------------------------------------------- GATES
    # OI-315's verdict moved to RETIRED_VERDICTS on 2026-08-13 when the row closed.
    # OI-45's verdict moved to RETIRED_VERDICTS on 2026-08-14 when the row closed.
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
    "OI-154": (GATES, "the default - out of the declared class",
               "Explainability as an end-user feature is a product requirement, not this "
               "project's tracking or documentation apparatus, so the declaration does not reach "
               "it and the default applies. Recorded honestly: the row's own status is 'held' "
               "pending an unrelated publication wave, so nothing turns on the verdict today."),
    # OI-183's verdict moved to RETIRED_VERDICTS on 2026-08-14 when the row closed.
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
    # OI-276's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the three doc-sync acts
    # landed and the row closed.
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
    # OI-320's and OI-322's verdicts moved to RETIRED_VERDICTS on 2026-08-11, when the user's
    # Ruling 62 closed both rows.
    # OI-324's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the user's Ruling 63 closed
    # the row.
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
    # Two rows, and they fell on opposite sides -- which was the criterion doing its job rather
    # than a close call. Both verdicts are made against the row's SUBJECT, never its remedy.
    # OI-331's verdict moved to RETIRED_VERDICTS on 2026-08-07, when the user ruled the row (R3)
    # and it closed. OI-332's was RE-CLASSED on the same day (R5) and its former verdict is kept
    # at SUPERSEDED_VERDICTS -- the two tables are different acts and are deliberately separate.
    # ---------------------------------------------------------------------- GATES
    # OI-332's verdict moved to RETIRED_VERDICTS on 2026-08-11 when the row closed.
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
    # ---- rowed 2026-08-07 by the owner-rulings homing wave --------------------------- NON-GATING
    "OI-346": (NON_GATING, "user",
               "The empirically-unvalidated mark is specified but not applied: the Jazz preset "
               "constants and the ground-truth-less idioms carry no mark and name no validating "
               "corpus. WHAT IS OWED decides it, and what is owed is a MARK on a value together "
               "with the name of the corpus that would validate it -- a LABEL, which D-438's line "
               "names on the apparatus side in that word. It states nothing false about the "
               "analysis: no constant moves, no measurement moves, and the fact the mark would "
               "declare -- that those values rest on no gate-grade ground truth -- is already "
               "stated in the specification, in the rule this wave homed at ARCHITECTURE.md 6 and "
               "in that rule's own sentence that the mark is NOT applied at HEAD. The row's own "
               "text settles its subject, so the default does not reach it. "
               "THE ESTABLISHMENT QUESTION (#19) WAS PUT RATHER THAN ASSUMED, and it is the one "
               "clause that would flip this: an establishment obligation always gates whatever its "
               "subject. This row is NOT one. Establishing the jazz values is the separate "
               "obligation [[OI-7]] carries -- acquire a jazz ground-truth corpus or de-scope the "
               "claims -- and that row GATES the Stage-3 entry gate in its own right. This row is "
               "the honest DECLARATION of that non-establishment, which is the opposite act: it "
               "asks for the absence of evidence to be visible where a reader meets the values, "
               "not for the evidence to be produced. Recorded against the row's SUBJECT, never its "
               "remedy."),
    "OI-347": (NON_GATING, "user",
               "The two Layer-1.5 primitives are sited in different sections of the canonical "
               "architecture document, and only one of the two sitings states its reason. WHAT IS "
               "OWED decides it, and what is owed is a FILING DECISION and a SECTION BOUNDARY -- "
               "where a specification paragraph should sit -- which D-438's line names on the "
               "apparatus side in those words. Nothing false about the analysis is stated by the "
               "present arrangement: the rule at issue is PUBLISHED, once, at the Layer-4 section, "
               "with 5.14 pointing at it, and this wave's own STOP check established that no "
               "section specifies the primitive twice, so there is no contradiction to correct and "
               "no specification left incomplete by it. It bears on no analysis, no analysis input "
               "and no instrument any measurement depends on -- the primitive's behaviour is "
               "untouched either way. It carries no establishment obligation (#19): nothing here is "
               "an instrument trusted without being established. Recorded against the row's "
               "SUBJECT, never its remedy -- and the remedy is deliberately open, since re-siting "
               "the spelling primitive and completing Layer 1's derived-views list are both "
               "available and neither is proposed."),
    # OI-353's verdict moved to RETIRED_VERDICTS on 2026-08-09 when the row closed under Ruling 16.
    "OI-359": (GATES, "the criterion - the subject is an instrument a measurement of the analysis "
                      "depends on",
               "The per-corpus half of a ratified measurement convention has no mechanism, and the "
               "split that does exist is by PRESET, which answers a different question. THE "
               "FIRST-CUT CLASSIFICATION REACHED THIS ROW and the verdict is authored for it here, "
               "which is what the tool requires; no non-gating verdict is hand-added, which is the "
               "act the record forbids. It GATES on the criterion itself rather than on the "
               "exemption: the subject is the ENFORCEMENT of a rule about how a measurement of the "
               "analysis is reported, so it bears on an instrument every published figure depends "
               "on, and D-438's test is answered YES directly. What is owed is not a pointer, an "
               "anchor, a label, a banner, a filing decision or a section boundary -- it is a "
               "mechanism for a convention whose own stated reason is that a single aggregate can "
               "hide which corpus moved (#9, #24). Recorded against the row's SUBJECT, never its "
               "remedy: the remedy is a mechanism build the user's own ruling deliberately did not "
               "start, and it joins the D-436 backlog."),
    "OI-360": (GATES, "the clause that overrides the criterion - an establishment obligation "
                      "(#19) always gates, whatever its subject",
               "Two checks over the decisions register's own data are BOTH satisfied by a "
               "corrupted pair -- once an entry's quote IS the text at its drifted line, the two "
               "agree with each other permanently -- so their green verdicts do not bound what "
               "they appear to bound. That is the shape #19 refuses: a thing trusted because "
               "nothing contradicted it, where what would contradict it cannot. THE FIRST-CUT "
               "CLASSIFICATION IS RIGHT ABOUT THE SUBJECT and is not disputed -- this is the "
               "decisions register's own verification apparatus, and the documentation criterion "
               "alone would put it outside the gate. What decides it is the clause `CLAUDE.md`'s "
               "non-gating declaration states and does not leave discretionary. The obligation is "
               "not discharged by the repair that closed OI-358: repairing five entries removes "
               "five instances and leaves the class unguarded, and the one candidate signal has "
               "now been MEASURED and does not separate. Recorded against the row's SUBJECT, "
               "never its remedy -- a second candidate signal is a mechanism design D-436 "
               "reserves to the user, and this row proposes none."),
    # OI-369's verdict moved to RETIRED_VERDICTS on 2026-08-11, when the user's Ruling 61 closed
    # the row.
    # ---- rowed 2026-08-11, graded 2026-08-11 (`cc_instruction_apply_the_bearing_cut.md` Task 2) --
    # The dispatch's assumption A6 forbids assuming either of these is apparatus and requires both
    # to go through the cut like any other row, taking whatever verdict it gives them. Both come
    # out GATES, on DIFFERENT grounds, which is the criterion doing its job rather than a close
    # call. Each verdict is made against the row's SUBJECT, never its remedy.
    # OI-370's verdict moved to RETIRED_VERDICTS on 2026-08-17, when the user's Ruling 4 of
    # `cowork_rulings_2026_08_17_governing_surface_split.md` supplied the boundary the row's first
    # remedy lacked and the mandatory read succeeded, closing the row.
    "OI-371": (GATES, "a statement about the analysis's build state",
               "A set of comment blocks was graded HELD pending a call-graph answer, that answer "
               "is now established, and the row that recorded the hold is RESOLVED -- so a "
               "false-at-HEAD statement about WHICH DECODER SHIPS has no live tracking. WHAT IS "
               "OWED decides it, and what is owed is not a pointer, an anchor, a label, a banner, "
               "a filing decision or a section boundary: it is the CORRECTION OF A STATEMENT ABOUT "
               "WHICH ANALYSIS ARM RUNS, which D-438's own line inside the documentation rows "
               "names on the gating side in those words. It is the class the retired [[OI-303]], "
               "[[OI-304]] and [[OI-353]] verdicts all carry, one artifact further in: there the "
               "false claims stood in the comments, and here what is ALSO wrong is the sweep's own "
               "verdict, which reads `undecided` rather than `owed` and therefore brings nothing "
               "back. The row's own text reaches the same reading and is not the reason for it -- "
               "the reading is made at D-438's line. NOT an establishment obligation (#19): no "
               "rate, measurement tool or measured value is affected, and no comment is executable "
               "-- the behaviour is what the configuration says, which is the same ground the "
               "OI-353 verdict gave. Recorded against the row's SUBJECT, never its remedy: the "
               "re-grade must run through `gen_arm_comment_sweep.py` rather than around it, and "
               "the correcting act needs its own authorization, exactly as [[OI-368]]'s act (a) "
               "records for the neighbouring site."),
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
    """THE ONE INDEX PARSER (#6) — every derivation over the open-items register reads rows here.

    ★ CHANGED 2026-08-09 by the user's Ruling 33 (`cowork_rulings_2026_08_09_fifth_stop.md`), which
    remedies ONE family of three defects at once rather than per symptom:

      * a status cell MENTIONING another row's resolved mark made this row read as resolved
        (OI-356) — impossible now, because only the cell's own opening token decides it;
      * a resolution spelled IN WORDS read as open (OI-361) — impossible now, because a resolved
        cell must open with the mark;
      * a row that did not split was skipped SILENTLY, present in no population at all (OI-362) —
        now a STOP.

    THE FORMER RULE, PRESERVED (#12): a row was OPEN when the resolved mark did not occur ANYWHERE
    in its status cell, and a row that did not yield six cells was `continue`d without a report.
    """
    rows, malformed, noncanonical = [], [], []
    for lineno, ln in enumerate(INDEX.read_text(encoding="utf-8").splitlines(), 1):
        if not ln.startswith("| OI-"):
            continue
        cells = split_row(ln)
        if len(cells) != CELLS_PER_ROW:
            malformed.append(f"line {lineno}: {len(cells)} cells "
                             f"({cells[0] if cells else '?'})")
            continue
        tok = leading_token(cells[4])
        if tok is None:
            noncanonical.append(f"{cells[0]} (line {lineno}): {cells[4][:80]}")
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
            "open": CANONICAL[tok] == "open",
        })
    if malformed or noncanonical:
        raise SystemExit(
            "STOP: the open-items INDEX does not parse (Ruling 33 of 2026-08-09 — a row that does "
            "not split, or a status cell whose opening is not canonical, is a STOP and never a "
            "silent skip).\n  malformed rows: " + "; ".join(malformed) +
            "\n  non-canonical status openings: " + "; ".join(noncanonical) +
            "\n  The vocabulary and the lint are at tools/audit/index_status_lint.py.")
    return rows


def reach_rows_inside() -> list:
    """The rows D-639's reach derivation put INSIDE the doc-sync half, read at its own artifact.

    A MISSING artifact is a STOP rather than an empty set. An item whose closing act names one
    derivation must not quietly omit it and read as though the derivation had found nothing — which
    would silently un-do the user's Ruling 56 on the next regeneration.
    """
    if not REACH.exists():
        raise SystemExit(
            f"STOP: {REACH.relative_to(ROOT)} is absent. The user's Ruling 56 applies THAT "
            "derivation's IN set, so without it this tool cannot say which rows were moved — and "
            "treating an absent artifact as an empty set would silently reverse a user ruling.")
    art = json.loads(REACH.read_text(encoding="utf-8"))
    try:
        return list(art["rows_inside_the_doc_sync_half"])
    except KeyError as exc:                                        # pragma: no cover - a STOP
        raise SystemExit(
            "STOP: the reach derivation's artifact does not carry "
            f"`rows_inside_the_doc_sync_half` ({exc}), which is the field Ruling 56 applies.")


def frozen_gating_enumeration() -> tuple[list | None, str]:
    """The FROZEN phase-1 enumeration of gating rows, read for COMPARISON only.

    ★ THE LIVE ANSWER DOES NOT DEPEND ON THIS AND MUST NOT. `the_live_gating_answer` is computed
    entirely from the INDEX as it stands and from the verdicts in this file; this read exists so
    the difference between the live answer and the frozen record can be PUBLISHED as evidence for
    the phase's retrospective. An absent frozen artifact therefore does not halt the derivation —
    it is reported as unreadable, in terms, so it can never be mistaken for "no difference".
    """
    if not FROZEN_INVENTORY.exists():
        return None, (f"{FROZEN_INVENTORY.relative_to(ROOT).as_posix()} is absent, so the "
                      "comparison could NOT be taken. This is not a statement that the two agree.")
    art = json.loads(FROZEN_INVENTORY.read_text(encoding="utf-8"))
    try:
        return list(art["the_gating_split"]["gates"]["ids"]), ""
    except KeyError as exc:
        return None, (f"{FROZEN_INVENTORY.relative_to(ROOT).as_posix()} carries no "
                      f"`the_gating_split.gates.ids` ({exc}), so the comparison could NOT be "
                      "taken. This is not a statement that the two agree.")


def the_live_gating_answer(open_rows: list, items: list, ng_ids: list) -> dict:
    """★ THE LIVE GATING ANSWER, PUBLISHED BY IDENTITY — Ruling 1 of the session-start-read sitting.

    WHAT THIS IS AND WHY IT IS A PUBLICATION RATHER THAN A JUDGMENT. Rule (b) of the open-items
    register is *a stage may not open while a register item gating it is open*, so a session needs
    to know WHICH ROWS GATE. This derivation already determines that for every open row, and until
    2026-08-17 it published only one side of it: the NON-GATING identities, plus a count and a
    per-ground listing of the GATES verdicts INSIDE its own over-inclusive first cut. The gating
    side as a whole was never enumerated.

    It needs no new verdict. The first cut is deliberately OVER-INCLUSIVE — the module docstring
    says so and the tool STOPs unless every candidate in it carries an authored verdict — so an
    open row OUTSIDE the cut is not an apparatus candidate at all, and THE RULED DEFAULT already
    answers it: *a row that is not apparatus, or whose subject the row does not settle, GATES.*
    The gating set is therefore the COMPLEMENT of the non-gating verdicts over the open rows this
    tool already parses, and publishing it is publishing what the derivation computes.

    ★ WHAT WOULD FALSIFY IT, recorded with it so a later session can challenge the derivation
    rather than rediscover the question:
      * an open row placed in NEITHER side, or in BOTH — the partition is asserted in both
        directions on every run and a row it cannot place HALTS the run;
      * a gating identity that is not an OPEN row of `OPEN_ITEMS.md` — asserted against the parsed
        population itself, not against a copy of it;
      * a gating row carrying no ground — asserted per row;
      * the ruled default ceasing to be *GATES* for a row outside the apparatus cut, which would
        make the complement the wrong operation. That is a USER RULING and not a drift: it would
        be visible at `THE_DEFAULT` above, which is quoted into the artifact on every run.

    ★ WHAT IT DOES NOT DO. It does not make this artifact a second home for status: the INDEX
    remains the authoritative status surface (#6), and this is a route to ONE question the INDEX
    answers. It closes no row, flips none, and creates none. It does not reach an establishment
    obligation (#19), which always gates.
    """
    open_ids = sorted(r["id"] for r in open_rows)
    ng_set = set(ng_ids)
    cut_ground = {i["id"]: i.get("gate_ground") for i in items if i["verdict"] == GATES}
    in_cut = {i["id"] for i in items}

    gating, unplaceable = [], []
    for rid in open_ids:
        if rid in ng_set:
            continue
        if rid in in_cut:
            ground = cut_ground.get(rid)
            how = "the authored verdict at the row, inside the apparatus first cut"
            if not ground:
                unplaceable.append(rid)
                continue
        else:
            ground = OUTSIDE_THE_CUT_GROUND
            how = "the ruled default, the row being outside the over-inclusive apparatus first cut"
        gating.append({"id": rid, "gate_ground": ground, "how_it_was_placed": how})

    gating_ids = [g["id"] for g in gating]
    # ── the #19 establishment: reconciled in BOTH directions against the INDEX itself ────────────
    if unplaceable:
        raise SystemExit(
            "STOP: open row(s) the gating derivation cannot place: " + ", ".join(unplaceable)
            + ". A row the derivation cannot place halts the run rather than being defaulted "
              "silently — the gating answer is only established while every open row is accounted "
              "for.")
    both = sorted(set(gating_ids) & ng_set)
    if both:
        raise SystemExit("STOP: open row(s) on BOTH sides of the gating split: "
                         + ", ".join(both) + ". A row gates or it does not.")
    neither = sorted(set(open_ids) - set(gating_ids) - ng_set)
    if neither:
        raise SystemExit("STOP: open row(s) on NEITHER side of the gating split: "
                         + ", ".join(neither) + ". Every open row is accounted for or nothing is "
                         "written.")
    not_open = sorted(set(gating_ids) - set(open_ids))
    if not_open:
        raise SystemExit("STOP: gating identity/identities that are not open rows of the INDEX: "
                         + ", ".join(not_open))
    groundless = sorted(g["id"] for g in gating if not g["gate_ground"])
    if groundless:
        raise SystemExit("STOP: gating row(s) carrying no ground: " + ", ".join(groundless))

    frozen, why_not = frozen_gating_enumeration()
    comparison = {
        "what_this_is": (
            "THE MEASUREMENT OF WHAT THE OSSIFICATION HAS BEEN HIDING, and it is EVIDENCE FOR THE "
            "PHASE'S RETROSPECTIVE — never an act. No row is flipped, created or discarded by it, "
            "and the frozen artifact's own population is left exactly as it stands."),
        "the_frozen_record": FROZEN_INVENTORY.relative_to(ROOT).as_posix()
                             + " → the_gating_split.gates.ids",
        "why_it_is_frozen": (
            "its generator `tools/audit/gen_phase1_completion_inventory.py` carries the verdict "
            "`records-a-point-in-time-measurement` in the committed guard classification and "
            "stands HISTORICAL, because its subject is the three-phase structure the six phases "
            "superseded. It is a historical record and not a live answer."),
        "★_the_two_populations_are_different_BY_CONSTRUCTION_and_that_is_the_finding": (
            "the frozen split is applied over `the wide cut` — an authored keyword selection of "
            "open rows, whose own over-inclusion that artifact declares unmeasured — while this "
            "derivation's population is EVERY OPEN ROW of the INDEX as it stands. So the "
            "difference below is not drift between two answers to one question: it is the gap "
            "between a frozen answer over a narrow authored cut and the live answer over the "
            "whole open register."),
    }
    if frozen is None:
        comparison["the_comparison_could_not_be_taken"] = why_not
    else:
        frozen_set, live_set = set(frozen), set(gating_ids)
        comparison["frozen_gating_rows"] = len(frozen)
        comparison["live_gating_rows"] = len(gating_ids)
        comparison["in_the_frozen_record_and_still_gating_live"] = sorted(frozen_set & live_set)
        comparison["in_the_frozen_record_but_NOT_gating_live"] = sorted(frozen_set - live_set)
        comparison["gating_live_but_NOT_in_the_frozen_record"] = sorted(live_set - frozen_set)
        comparison["★_what_each_difference_side_means"] = (
            "A row in the frozen record but not gating live has either RESOLVED since the freeze "
            "or been re-classed NON-GATING by a verdict in this file — read its side at the INDEX "
            "and at the items above, never from this list alone. A row gating live but absent "
            "from the frozen record is one the frozen wide cut never selected, or one opened "
            "since the freeze. NEITHER side is acted on here.")

    return {
        "what_this_is": (
            "THE LIVE GATING ANSWER: which OPEN rows of `OPEN_ITEMS.md` a stage waits on, derived "
            "at the INDEX as it stands today and published BY IDENTITY. This is the artifact a "
            "session reads at session start under rule (a) of the open-items register section of "
            "`CLAUDE.md`; it opens the INDEX when it needs a row."),
        "the_ruling_that_ordered_it": (
            "Ruling 1 of `cowork_rulings_2026_08_17_session_start_read_sitting.md`: \"A session no "
            "longer reads the whole index at session start. It reads the derived gating answer, "
            "and opens the INDEX when it needs a row.\" The ruling's own #19 precondition is that "
            "the artifact must be POSITIVELY ESTABLISHED before anything relies on it."),
        "the_question_it_answers": (
            "Rule (b) of the open-items register: a stage may not open while a register item "
            "gating it is open. A count does not answer that question; identities do."),
        "★_how_it_is_derived_and_why_it_is_a_publication_and_not_a_judgment": (
            "The gating set is the COMPLEMENT of this file's non-gating verdicts over the open "
            "rows this tool already parses. No new verdict is authored: the apparatus first cut is "
            "deliberately OVER-INCLUSIVE and every candidate in it must carry an authored verdict "
            "or the tool STOPs, so an open row outside the cut is not an apparatus candidate and "
            "THE RULED DEFAULT already gates it. Nothing is imported from any frozen artifact to "
            "reach this answer."),
        "★_the_establishment_under_#19_taken_POSITIVELY_on_every_run": {
            "reconciled_in_both_directions_against_the_INDEX_itself": [
                "every gating identity is an OPEN row of the parsed INDEX population",
                "every open row is accounted for as gating or non-gating — none in both, none in "
                "neither",
                "every gating row carries a ground",
            ],
            "a_row_the_derivation_cannot_place_HALTS_the_run": True,
            "what_would_falsify_it": [
                "an open row placed in neither side, or in both",
                "a gating identity that is not an open row of the INDEX",
                "a gating row carrying no ground",
                "the ruled default ceasing to be GATES for a row outside the apparatus cut, which "
                "would make the complement the wrong operation — a USER RULING, visible at "
                "`the_default` in this artifact, and not a drift",
            ],
            "what_it_does_NOT_establish": (
                "That any individual GATES verdict is right — a verdict about a row's subject is "
                "authored and is challengeable at the row. What is established is that the "
                "partition is complete, that every identity is a live open row, and that every "
                "gating row carries a ground."),
        },
        "the_default_that_places_every_row_outside_the_apparatus_cut": THE_DEFAULT,
        "gating_rows": len(gating_ids),
        "non_gating_rows": len(ng_ids),
        "open_rows": len(open_ids),
        "gating_ids": gating_ids,
        "gating_rows_by_how_they_were_placed": {
            "the_authored_verdict_inside_the_apparatus_first_cut":
                sorted(g["id"] for g in gating
                       if g["how_it_was_placed"].startswith("the authored verdict")),
            "the_ruled_default_outside_the_apparatus_first_cut":
                sorted(g["id"] for g in gating
                       if g["how_it_was_placed"].startswith("the ruled default")),
        },
        "the_gating_rows": gating,
        "★_the_frozen_enumeration_measured_against_this_one": comparison,
        "★_what_this_answer_does_NOT_do": [
            "It does not change rule (a)'s authority: the INDEX remains the AUTHORITATIVE STATUS "
            "SURFACE, and this is a route to one question it answers, never a second home for "
            "status (#6).",
            "It flips no row, creates none and discards none.",
            "It does not reach an establishment obligation (#19), which always gates.",
            "It says nothing about a row's SIZE or its owner — that is "
            "`tools/audit/gating_row_sizing.json`, whose own population comes from the frozen "
            "record and is deliberately left exactly as it stands.",
        ],
    }


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
    # A SUPERSEDED verdict must name a row that still carries a LIVE verdict here, and that live
    # verdict must actually differ from it -- otherwise the table is either a graveyard for rows
    # that left (which is what RETIRED_VERDICTS is for) or a duplicate of a verdict nothing
    # replaced, which is the drift both stops above exist to prevent.
    #
    # ★ A CLOSED ROW IS THE THIRD CASE, and it is admitted rather than stopped on (added 2026-08-11,
    # `cc_instruction_return_continuation_14.md` Task 3). A row that was RE-CLASSED and has since
    # CLOSED has no live verdict here by construction -- its verdict is in RETIRED_VERDICTS -- and
    # its superseded verdict must still be kept whole (#12), because deleting it would destroy the
    # record that the re-class happened at all. The two failures this STOP was written against are
    # untouched: a superseded verdict for a row that never left, and one for a row that left
    # WITHOUT its live verdict being retired.
    orphan_superseded = [i for i in SUPERSEDED_VERDICTS
                         if i not in V and i not in RETIRED_VERDICTS]
    if orphan_superseded:
        raise SystemExit("STOP: superseded verdicts for rows with no live verdict here: "
                         + ", ".join(sorted(orphan_superseded))
                         + ". A row that left the population belongs in RETIRED_VERDICTS.")
    unchanged_superseded = [i for i, s in SUPERSEDED_VERDICTS.items()
                            if i in V and V[i][0] == s[0]]
    if unchanged_superseded:
        raise SystemExit("STOP: superseded verdict(s) whose live verdict carries the same class: "
                         + ", ".join(sorted(unchanged_superseded))
                         + ". Nothing was re-classed, so nothing was superseded.")

    # ── the user's Ruling 56: WHICH rows the reach derivation moved is DERIVED, not listed ──────
    reach_in = reach_rows_inside()
    # A row the derivation moved and that has since CLOSED is counted here through its RETIRED
    # record: the ruling was applied to it, and its closure is not an un-application. Without this
    # the reconciliation would fire on every row Ruling 56 moved that a later act then closed --
    # reporting the ruling as un-applied when what happened is that the work was done.
    moved_here = sorted([i for i, v in V.items() if v[1] == RULING_56_GROUND]
                        + [i for i, v in RETIRED_VERDICTS.items()
                           if v[1] == RULING_56_GROUND and i in reach_in])
    if moved_here != sorted(reach_in):
        raise SystemExit(
            "STOP: the rows re-classed here under the user's Ruling 56 and the rows D-639's reach "
            "derivation puts INSIDE the doc-sync half disagree.\n"
            f"  re-classed here but not IN the derivation: "
            f"{[i for i in moved_here if i not in reach_in]}\n"
            f"  IN the derivation but not re-classed here: "
            f"{[i for i in reach_in if i not in moved_here]}\n"
            "  Ruling 56 applies the derivation's own artifact and forbids a hand-listed set, so "
            "the two must agree in both directions or nothing is written.")
    not_superseded = [i for i in moved_here if i not in SUPERSEDED_VERDICTS]
    if not_superseded:
        raise SystemExit(
            "STOP: a row re-classed under Ruling 56 carries no superseded verdict: "
            + ", ".join(not_superseded)
            + ". A re-class replaces an answer, and the answer it replaced is kept whole (#12).")

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
    # A row a LATER USER RULING re-classed is a third case, and it is kept apart for the same
    # reason the closed one is: the assumption was graded against the verdict that stood when it
    # was made, and a ruling that changed the answer did not make the original reading wrong.
    # Folding it into `refuted` would report a mistake where what happened is a decision.
    a3_reclassed = [i for i in a3_ids if i not in a3_closed and i in SUPERSEDED_VERDICTS]
    a3_live = [i for i in a3_ids if i not in a3_closed and i not in a3_reclassed]
    a3_confirmed = [i for i in a3_live if i in ng_ids]
    a3_refuted = [i for i in a3_live if i not in ng_ids]
    a3_missed = [i for i in ng_ids if i not in a3_ids]

    live_answer = the_live_gating_answer(open_rows, items, ng_ids)

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
        "★_the_ruling_56_application": {
            "the_ruling": (
                "User, 2026-08-11, Ruling 56 of `cowork_rulings_2026_08_11_twelfth_stop.md`: the "
                "rows D-639's reach derivation put INSIDE the doc-sync half join the gating "
                "TRUE-half item — derived from the derivation's own artifact, never hand-listed."
            ),
            "what_it_completes": (
                "The FIRST application of D-639's test reported the same consequence for one "
                "document and declined to apply it, on the ground that a non-gating verdict is "
                "DERIVED from a cut and never hand-added — and the user then ruled it separately, "
                "re-classing that row GATES. This ruling is that reserved answer, given for the "
                "SECOND application and for its whole IN set at once."
            ),
            "how_the_moved_set_is_derived": (
                "Read on every run from `tools/audit/decisions/true_half_reach_rows.json` → "
                "`rows_inside_the_doc_sync_half`, and reconciled BOTH WAYS against the rows this "
                "table carries with the Ruling-56 gate ground. A disagreement in either direction "
                "is a STOP, and a MISSING artifact is a STOP rather than an empty set — treating "
                "it as empty would silently reverse a user ruling on the next regeneration."
            ),
            "rows_moved": sorted(i for i, v in V.items() if v[1] == RULING_56_GROUND),
            "rows_moved_that_have_since_CLOSED": sorted(
                i for i, v in RETIRED_VERDICTS.items()
                if v[1] == RULING_56_GROUND and i in reach_in),
            "why_the_two_lists_are_apart": (
                "The first is what a consumer of this artifact must still subtract from the "
                "pre-ruling cut; the second is rows the ruling moved and a later act then CLOSED, "
                "which are no longer in any live population and must not be subtracted from one. "
                "Keeping them together would make a consumer's cut disagree with the derived row "
                "set — the failure the reconciliation STOPs on — and dropping the second list "
                "entirely would lose the record that the ruling reached those rows at all (#12)."
            ),
            "what_did_NOT_move_with_them": (
                "Nothing about D-438 or its criterion, which is unchanged and still decides every "
                "other row here; and no row the derivation put OUT. Each moved row's FORMER verdict "
                "is preserved whole at `superseded_verdicts` (#12) with the reason it was right "
                "about the question it answered — the two tests have different subjects, which "
                "D-639 states in terms."
            ),
        },
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
        "★_the_live_gating_answer": live_answer,
        "items": items,
        "superseded_verdicts": {
            "what_this_is": (
                "Verdicts a USER RULING has RE-CLASSED. The row is still open and still a first-cut "
                "candidate, so its live verdict is in the items above; what is kept here is the "
                "verdict that stood before it, whole, with the ruling that replaced it (#12). "
                "Distinct from `retired_verdicts` in both directions: there the row CLOSED and left "
                "the population, here the row stayed and the answer changed. Two STOPs guard it - a "
                "superseded verdict naming a row with no live verdict, and a superseded verdict "
                "whose live verdict carries the same class, each stop the tool."
            ),
            "entries": {
                rid: {"former_verdict": v, "former_class_basis_or_ground": g,
                      "former_reason": reason, "re_classed": ruling}
                for rid, (v, g, reason, ruling) in sorted(SUPERSEDED_VERDICTS.items())
            },
        },
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
            reclassed_by_a_later_ruling=a3_reclassed,
            reclassed_note=(
                "A row a LATER USER RULING re-classed is the third case and is kept apart for the "
                "same reason the closed one is. A3 was graded against the verdict that stood when "
                "it was made; a ruling that changed the answer did not make the original reading "
                "wrong, and folding such a row into `refuted` would report a mistake where what "
                "happened is a decision. Each one's former verdict is whole at "
                "`superseded_verdicts` with the ruling that replaced it."
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
