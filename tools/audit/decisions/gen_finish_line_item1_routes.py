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

# The edit surface a homing dispatch authorizes. An entry whose owning specification lies outside
# it is classified but NOT executed -- stated so that a small executed set is read as a scope bound
# rather than as a judgment that the remaining entries have no owner.
#
# ★ WIDENED 2026-08-07 (user's ruling, dispatch `cc_instruction_five_rulings.md` §0a R1, recorded
# in `cowork_audit_protocol.md`): a HOMING dispatch may also touch `docs/scoring_model.md`,
# `CLAUDE.md` and `BUILD_AND_TEST.md`, SCOPED TO HOMING ACTS ALONE.  The former value, preserved
# (#12): EXECUTABLE_OWNER_PREFIX = "ARCHITECTURE.md" -- the standing autonomous-operation
# authorization and nothing else.
EXECUTABLE_OWNER_PREFIXES = ("ARCHITECTURE.md", "CLAUDE.md", "docs/scoring_model.md",
                             "BUILD_AND_TEST.md")

# ★ THE OWNER-DETERMINACY VERDICT FOR THE LICENSING CLASS, AUTHORED 2026-08-07, AND WHY IT IS A
# SEPARATE FIELD RATHER THAN A REWRITE OF THE `unambiguous` COLUMN.
#
# `OPEN_ITEMS.md` OI-342 measured that the `unambiguous` column below carries the answer to a
# DIFFERENT question for the rows whose recorded reason names only the edit surface -- those rows
# name a determinate site and then say it was out of reach -- and that row declines to re-author
# another wave's judgment table, on the ground that re-authoring is not a reading act.  So the
# column is left exactly as it stands and this verdict is recorded beside it.
#
# It is the discharge of the homing dispatch's own assumption A1 ("every licensing-class entry's
# recorded owner names a DETERMINATE section of its file"), taken per entry against the RECORD's
# own reading rather than a fresh judgment: OI-342 enumerates the three members of that class whose
# owner is genuinely soft INDEPENDENT of the surface -- D-539 ("the principles"), D-538 ("the
# project's standing rules") and D-281 (two candidate homes, in two different files) -- and states
# that every other member names a determinate site.  A1 is therefore REFUTED FOR THOSE THREE, which
# the dispatch names as a result rather than a failure: they are not homed, they stay in item 1,
# and they return to the user with the owner question.  Nothing here guesses a section.
A1_OWNER_IS_DETERMINATE = {
    "D-451", "D-452", "D-473", "D-486", "D-564", "D-582", "D-602", "D-603",
}

# ★ THE THREE OWNER RULINGS OF 2026-08-07, AND WHY THEY ARE A TABLE OF THEIR OWN.
#
# The A1 verdict above RETURNED three entries to the user with the owner question, which is what
# it was for.  The user answered all three on the same date (dispatch
# `cc_instruction_three_owner_rulings.md` §0a, rulings R1-R3).  The answers are recorded here
# rather than folded into the set above, because the two record different acts: that set records
# what a session could NOT settle, this one records what the user did settle.  Widening the first
# would erase the refusal that produced the question.
#
# Two of the three are HOMED and leave item 1.  The third, D-538, is ratified and ruled SUPERSEDED
# in the same act, which discharges it by a different route entirely -- its route below becomes
# NO HOME EXISTS and its disposition is DERIVED in `gen_r1_superseded_reach.py`, never authored
# here.  So it is deliberately absent from this table.
#
# WHY `EXECUTABLE_OWNER_PREFIXES` IS NOT WIDENED FOR D-539.  Its ruled home,
# `cowork_engage_arc_plan.md`, is a ratified contract document outside every standing licence, and
# the user's ruling is the authorization for THAT ONE EDIT rather than for a standing surface.
# Writing the file into the prefix table would convert a one-edit authorization into a licence,
# which is the act rule (g) reserves to the user.  The ruling therefore admits the entry directly.
OWNER_RULED_2026_08_07 = {
    "D-281": "BUILD_AND_TEST.md (re-homed 2026-08-07 on the user's ruling R1 — no longer in item 1)",
    "D-539": "cowork_engage_arc_plan.md (re-homed 2026-08-07 on the user's ruling R3 — no longer in "
             "item 1)",
}

# ★ THE FORTY-EIGHT OWNER RULINGS OF 2026-08-07 (the homing wave), AND WHY THEY ARE A THIRD TABLE.
#
# The two tables above record, in order, what a session could NOT settle (the A1 verdict) and what
# the user settled for the three entries that verdict returned.  This table records a LATER and
# LARGER act by the same user on the same date: the ruling record `cowork_owner_rulings_2026_08_07.md`
# rules the owner for the whole remaining population of item 1's re-home class -- the forty
# owner-not-determinate entries and the eight no-blocker entries -- entry by entry, on four decision
# surfaces.  It is kept separate for the same reason the second table is: merging it into the A1
# verdict would erase the refusal that produced the question, and merging it into the three-ruling
# table would date two different rulings to one act.
#
# EACH VALUE IS THE DESTINATION FILE the ruling names.  The destinations themselves are not
# re-authored here: they are the ruling record's own table, read whole (D-643), and the homing act
# that carried them out wrote each decision into the named section with its defense.
#
# ★ D-472 IS ABSENT FROM THIS TABLE AND SITS IN THE 2026-08-08 ONE BELOW.  The 2026-08-07 ruling
# routed it to the Layer-6 section and made the LEGACY mark conditional on an arm check at the code
# (the homing dispatch's assumption A5); the check came back MIXED, so it was HELD and returned to
# the user, which is why it never entered this table.  The user then ruled it on 2026-08-08 and it
# was homed in the ruled form, so its record is the next table, not this one.  FORMER TEXT OF THIS
# BLOCK, PRESERVED (#12) -- true when it was written, and superseded by the later ruling rather than
# wrong: "★ D-472 IS DELIBERATELY ABSENT, AND ITS ABSENCE IS A RESULT RATHER THAN AN OMISSION.  The
# ruling routes it to the Layer-6 section and makes the LEGACY mark conditional on an arm check at
# the code (the homing dispatch's assumption A5).  The check came back MIXED -- the grouping rule the
# entry specifies is SHARED and reached on the production record arm, while the stabilization pass
# its own text names as the precondition is legacy-arm-only -- and a mixed arm is the dispatch's
# stated outcome for holding an entry and returning it to the user.  So it was NOT homed, it stays
# in item 1, and its route row below records the ruling and the hold together."
OWNER_RULED_2026_08_07_HOMING = {
    # the joint-estimator section (created by the same act, by converting the standing-rules block)
    "D-449": "ARCHITECTURE.md", "D-450": "ARCHITECTURE.md",
    "D-532": "ARCHITECTURE.md", "D-533": "ARCHITECTURE.md", "D-534": "ARCHITECTURE.md",
    # the ARCHITECTURE.md section groups
    "D-280": "ARCHITECTURE.md", "D-501": "ARCHITECTURE.md",
    "D-419": "ARCHITECTURE.md", "D-496": "ARCHITECTURE.md",
    "D-421": "ARCHITECTURE.md", "D-542": "ARCHITECTURE.md", "D-543": "ARCHITECTURE.md",
    "D-544": "ARCHITECTURE.md", "D-545": "ARCHITECTURE.md",
    "D-464": "ARCHITECTURE.md", "D-470": "ARCHITECTURE.md",
    "D-469": "ARCHITECTURE.md", "D-471": "ARCHITECTURE.md",
    "D-531": "ARCHITECTURE.md", "D-497": "ARCHITECTURE.md",
    "D-326": "ARCHITECTURE.md", "D-625": "ARCHITECTURE.md",
    "D-494": "ARCHITECTURE.md", "D-495": "ARCHITECTURE.md",
    "D-605": "ARCHITECTURE.md", "D-616": "ARCHITECTURE.md", "D-622": "ARCHITECTURE.md",
    # the scoring-surface rule
    "D-325": "docs/scoring_model.md", "D-327": "docs/scoring_model.md",
    "D-328": "docs/scoring_model.md", "D-423": "docs/scoring_model.md",
    "D-463": "docs/scoring_model.md", "D-465": "docs/scoring_model.md",
    "D-490": "docs/scoring_model.md", "D-491": "docs/scoring_model.md",
    "D-492": "docs/scoring_model.md", "D-493": "docs/scoring_model.md",
    "D-510": "docs/scoring_model.md", "D-511": "docs/scoring_model.md",
    "D-512": "docs/scoring_model.md", "D-536": "docs/scoring_model.md",
    "D-537": "docs/scoring_model.md", "D-580": "docs/scoring_model.md",
    # the gate block and the principle
    "D-604": "CLAUDE.md", "D-606": "CLAUDE.md", "D-474": "CLAUDE.md",
    # the arc plan, under the same one-edit authorization the D-539 ruling carried
    "D-568": "cowork_engage_arc_plan.md",
}

# ★ THE 2026-08-08 RULING — ONE ENTRY, AND A FOURTH TABLE FOR THE SAME REASON THE THIRD IS SEPARATE.
#
# D-472 was HELD by the 2026-08-07 homing wave because the arm check its own ruling ordered came back
# MIXED.  The user then ruled it on 2026-08-08 (Option A, recorded in the dated 2026-08-08 amendment
# to `cowork_owner_rulings_2026_08_07.md` and applied by `cc_instruction_document_routes_and_d472.md`):
# it is homed at the Layer-6 section in a form that shows BOTH ENDS OF THE SPLIT -- the grouping rule
# specified as LIVE on the production record arm, and the Pass-4 stabilization its own text names as
# the precondition beside it marked ⚠ LEGACY, each carrying its citation (#12) -- and the conformance
# question is rowed as `OPEN_ITEMS.md` OI-349, which GATES.
#
# WHY IT IS NOT MERGED INTO THE 2026-08-07 TABLE.  For the reason that table gives for not merging
# into the two above it: merging would date two different rulings to one act, and it would erase the
# HOLD, which is the thing that produced the second ruling.  The hold is a result, not a gap.
#
# WHY THE TABLE IS ADDED HERE RATHER THAN THE ENTRY BEING QUIETLY DROPPED.  Without it this generator
# STOPS -- "authored routes for entries item 1 does not carry" -- because the homing removed D-472
# from item 1's population while the table still expected it there.  That STOP is the guard working:
# it refuses to run while an authored route and the register disagree, and what it wants is the act
# recorded, not the route deleted.
RULED_2026_08_08 = {
    "D-472": "ARCHITECTURE.md",
}

# ★ THE SEVENTH RETURN CONTINUATION'S RE-HOMINGS, 2026-08-09 — a FIFTH table, for the same reason the
# fourth is separate from the third: one table per act, so no wave's date stands for another's.
#
# `cc_instruction_return_continuation_7.md` Task 1, under the user's Ruling 38 (the homing default).
# Two AUDIT-METHOD entries whose owning specification was determinate from their own records and whose
# home document was named in no user-ratified surface: D-581, the four-verdict rubric an
# information-loss sweep classifies every site under, with its no-guessing fourth verdict; and D-583,
# the condition a `keep, deferred` disposition holds under — that the thing kept stays characterized
# exactly, and is re-adjudicated the moment its form changes.  Both are written into P2 of
# `cowork_audit_protocol.md`, the section that already states this project's closed-verdict-set rule,
# in that section's own voice with their defenses; both take class `process`, which is what a method
# rule is and which leaves the home population by construction rather than by a delegation.  The
# catalogue's own text is untouched (#12) -- what stays there is the U2 INSTANCE and the sweep's
# findings, which are findings rather than rules.
REHOMED_2026_08_09_SEVENTH_RETURN = {
    "D-581": "cowork_audit_protocol.md",
    "D-583": "cowork_audit_protocol.md",
}

# The SIXTH per-act table, one per wave as the five before it are.  These five left item 1 under
# the user's RULING 40 (`cowork_rulings_2026_08_09_eighth_stop.md`), STEP 2 of its three-step
# procedure: the rule was written into the census section that owns it, in that section's own
# voice, under the census-edit licence the ruling grants -- and the entry's home and verbatim then
# moved there.  They need this table for the same reason the two above do: Ruling 38's conversion
# of an authored NEEDS A DELEGATION into a RE-HOME is applied at ROW BUILD while ROUTES keeps the
# authored judgment (#12), so the executed-check reading the authored tuple alone would report a
# performed act as never having happened.
REHOMED_2026_08_09_EIGHTH_RETURN = {
    "D-513": ("cowork_score_census.md", "§3, the inclusion criteria"),
    "D-514": ("cowork_score_census.md", "§4, the overlap-hazard accounting rule"),
    "D-500": ("cowork_score_census.md", "§5, the decision-tier block"),
    "D-422": ("cowork_score_census.md", "§5, at Tier J"),
    "D-614": ("cowork_score_census.md", "§8c, beside the Stage-5 fitting-pool licence constraint"),
}

# ★ THE 2026-08-09 RULING — THE HOMING FORK IS RESOLVED FOR THE WHOLE REMAINING POPULATION.
#
# `cowork_rulings_2026_08_09_sixth_stop.md`, Ruling 38 (user).  Its words: "For every remaining
# register entry in the finish-line items whose home document is named in NO user-ratified surface,
# or only in a form the delegation bar excludes: the closing act is RE-HOMING into the owning
# layer's specification — rule (e)'s own preference, and what makes C4 true without the register.
# NO DOCUMENT IS EXCEPTED at ruling time.  A later exception — a document the user wants kept as a
# contract home by delegation — is a NEW USER RULING naming the document, taken BEFORE its entries
# are re-homed, never after."  Its excluded alternative, recorded: delegation as the default — it
# grows the contract-home class, requires the user's writing per document (rule (g)), and runs
# against both concrete declinations already on the record.
#
# WHAT IT MOVES HERE, AND WHAT IT DOES NOT.  The fork the ruling resolves is DELEGATION versus
# RE-HOME, which is what its own excluded alternative names.  So every OPEN row whose authored
# route is NEEDS A DELEGATION now closes by a RE-HOME, and the authored route is preserved beside
# it (#12) rather than overwritten — the authored judgment is still the record of what a session
# read off the document, and the ruling is what decided the act.
#
# THE `NO HOME EXISTS` CLASS IS DELIBERATELY NOT MOVED, and the reason is stated so the boundary is
# not read as an oversight.  Those rows do not record a choice between a delegation and a re-home:
# they record that NEITHER applies — the entry's live content is carried by a homed successor, so
# writing it into a specification would put a second copy of a homed rule (#6), or there is no
# decision content to write at all.  Ruling 38 settles which of two available routes is the
# default; it does not create a route where the record says there is none, and it says nothing
# about #6.  That class is dispositioned under D-642 in `gen_r1_superseded_reach.py`, which is
# where it was already dispositioned before this ruling and where it stays (#6).
RULING_38 = (
    "User, 2026-08-09, Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`: re-homing into the "
    "owning layer's specification is the DEFAULT closing route for every remaining entry of the "
    "no-ratified-surface and bar-excluded classes, and NO DOCUMENT IS EXCEPTED. A later exception "
    "is a new user ruling naming the document, taken BEFORE its entries are re-homed."
)

# ── RULING 39, THE FIRST EXCEPTION TAKEN UNDER RULING 38's OWN MECHANISM ──────────────────────
#
# THE RULING.  User, 2026-08-09, Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md`, taken
# after a three-option decision surface: `cowork_score_census.md` is KEPT as the owning surface for
# the corpus decisions whose recorded owner it already is, the user approved the wording of a
# DOCUMENT-LEVEL delegation into `ARCHITECTURE.md` verbatim, and the rows below were to close by
# CLASSIFICATION rather than by a re-home, with zero text movement.
#
# WHAT WAS PERFORMED.  `cc_instruction_return_continuation_7.md` Task 0 wrote the approved wording
# into `ARCHITECTURE.md` beside the §8c naming, moved this document's FORMS grade to the
# explicit-delegation form (the strongest naming governs, rule (k1)), moved its authored
# `delegation_scope` from `sections` to `document`, and re-ran the classification.
#
# WHAT THE MEASUREMENT SAID, AND IT REFUTES THE PREDICTED CLOSE.  Not one of these rows moved, and
# the cause is a fact about where they are homed rather than anything about the delegation.  A
# register entry's class is decided by ITS OWN HOME DOCUMENT.  These entries name
# `cowork_score_census.md` as their OWNING SPECIFICATION -- the surface that ought to state their
# rules -- but every one of them is HOMED in a different document, and each of those documents is
# named in none of the three user-ratified surfaces, so clause (a) excludes them before any
# delegation is reached.  A delegation to the census cannot reach an entry that does not sit in the
# census.  The delegation write moved no entry at all: every entry actually homed in the census
# already sat in a reached, rule-stating section and was already `contract-home`.
#
# SO THE TWO HALVES OF THE RULING COME APART, AND CHOOSING BETWEEN THEM IS THE USER'S.  The ruling's
# ACT (the census is the owner; the delegation is written) is performed and stands.  The ruling's
# PREDICTED OUTCOME (these rows close by classification, with zero text movement) is unreachable as
# stated.  Two routes remain and each is one act: move each entry's HOME to the census section that
# already states its rule, if one does -- a pointer move, and the only route that is literally zero
# text movement; or perform the re-home Ruling 38 makes the default, writing each rule into the
# census section that owns it, which is text movement the exception was taken to avoid.  A session
# may not pick between a ruling's act and its stated outcome, so these rows are HELD INDIVIDUALLY
# with both routes named, and the refutation is reported at `cowork_away_returns.md` §1.12.
RULING_39 = (
    "User, 2026-08-09, Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md`: "
    "`cowork_score_census.md` is KEPT as the owning surface for the corpus decisions whose recorded "
    "owner it already is — the first exception taken under Ruling 38's own exception mechanism, in "
    "the form that mechanism requires. The user approved the wording of a DOCUMENT-LEVEL delegation "
    "into `ARCHITECTURE.md` verbatim; rule (h)'s granularity then does the filtering, so the "
    "census's rule-stating sections are homes and its findings tables are not."
)

RULING_39_MEASURED = (
    "HELD — the ruling's ACT is performed and its PREDICTED OUTCOME is refuted by measurement. The "
    "delegation was written verbatim into `ARCHITECTURE.md`, this document's FORMS grade moved to "
    "the explicit-delegation form and its authored delegation scope to `document`; the "
    "classification was then re-run and THIS ROW DID NOT MOVE. The cause is where the entry is "
    "homed, not the delegation: a register entry's class is decided by its own HOME DOCUMENT, this "
    "entry names the census as its OWNING SPECIFICATION but is homed in a different document, and "
    "that document is named in no user-ratified surface — so clause (a) excludes it before any "
    "delegation is reached. Two routes remain, each one act, and choosing between a ruling's act "
    "and its stated outcome is the user's: (1) move this entry's HOME into the census section that "
    "already states its rule, if one does — a pointer move, and the only route that is literally "
    "zero text movement; or (2) perform the re-home Ruling 38 makes the default, writing the rule "
    "into the census section that owns it, which is the text movement this exception was taken to "
    "avoid. Reported at `cowork_away_returns.md` §1.12."
)


# ── RULING 40, THE PROCEDURE THAT REPLACES RULING 39's UNREACHABLE OUTCOME ────────────────────
#
# THE RULING.  User, 2026-08-09, Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md`, taken
# after the refutation above was put to them.  Ruling 39's ACT stands -- the census is the ruled
# owner and the delegation is written -- and its unreachable OUTCOME is replaced by a THREE-STEP
# PROCEDURE, executed per entry, in order, with a STOP at each boundary:
#
#   (1) where a census RULE-STATING section ALREADY STATES the entry's rule, ROUTE 1 -- the entry's
#       HOME field moves to that section, the verbatim re-taken from the census's own text, the
#       former fields preserved (#12).  Zero text movement, which is what the exception was for.
#   (2) else, where the OWNING census section STATES RULES, ROUTE 2 -- the rule is written there in
#       the section's own voice, under a census-edit licence THIS ruling grants, scoped to
#       rule-stating sections and to these entries only.
#   (3) where the owning section is a FINDINGS TABLE, the entry is HELD with its row named.  Adding
#       a rule-stating block to a findings table is a DOCUMENT-STRUCTURE act reserved to the user.
#
# The kind half is judged PER SECTION before any step-2 write, and nothing is admitted by stretch.
# An entry fitting none of the three steps is a STOP, not a judgment.  Excluded alternative,
# recorded at the ruling: nine individual rulings, which buys no fidelity over the guarded
# procedure.
RULING_40 = (
    "User, 2026-08-09, Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md`: Ruling 39's ACT "
    "stands and its unreachable predicted OUTCOME is replaced by a THREE-STEP PROCEDURE executed "
    "per entry, in order — (1) where a census RULE-STATING section already states this entry's "
    "rule, move the entry's HOME field there, verbatim re-taken from the census's own text and "
    "former fields preserved (#12), which is zero text movement; (2) else, where the OWNING census "
    "section STATES RULES, write the rule there in the section's own voice under the census-edit "
    "licence this ruling grants, scoped to rule-stating sections and to these entries only; (3) "
    "where the owning section is a FINDINGS TABLE, HOLD the entry with its row named, because "
    "adding a rule-stating block to a findings table is a document-structure act reserved to the "
    "user. The kind half is judged PER SECTION before any step-2 write; nothing is admitted by "
    "stretch; an entry fitting none of the three steps is a STOP."
)

# The per-entry OUTCOME of that procedure, authored as it is executed.  It is a table rather than a
# derived value because which step an entry takes is a READING of the census -- does a rule-stating
# section already state this rule, and is the owning section a findings table -- and a reading is
# authored.  The population is NOT listed here: membership stays derived from the authored owner
# string above, so an entry that has no verdict yet says so rather than being silently absent.
RULING_40_STEPS: dict[str, str] = {
    # ── EXECUTED 2026-08-09, cc_instruction_return_continuation_8.md Task 1 ───────────────────
    # The census was read WHOLE before the first verdict, and the KIND HALF was judged per
    # section before any write.  The rule-stating sections used: §3 (inclusion criteria -- "A
    # source enters the registry only with all five fields decided"), §4 (the overlap-hazard
    # ACCOUNTING RULE, so named in its own heading), §5 (the decision-tier block, named as
    # rule-stating in the user's own approved Ruling 39 delegation wording), and §8c's Stage-5
    # fitting-pool licence constraint (rule (h)'s founding case, named in that same wording).
    # The FINDINGS surfaces, which admit nothing: §1's container table, §2, §7, and §8c's
    # needs-vector table.
    "D-513": ("STEP 2 — WRITTEN. No census rule-stating section already stated this rule, so "
              "step 1 did not apply. The OWNING section is §3 (inclusion criteria), which "
              "STATES RULES, so the rule was written there in §3's own voice under this "
              "ruling's census-edit licence: a registry `content` summary is enumeration "
              "PROVENANCE and presence of a layer is a MEASUREMENT made per slice. The entry's "
              "home and verbatim now point there; the former home and the former verbatim are "
              "preserved in its provenance (#12), and the audit that recorded the lesson is "
              "untouched."),
    "D-514": ("STEP 2 — WRITTEN. Step 1 was checked and did not apply: §4 states the dedupe "
              "rule and cites the same contamination lesson, but it does NOT state the "
              "record-only status or the user-ruling requirement, which are this entry's rule. "
              "§4 STATES RULES — its own heading calls it the accounting rule — so the rule "
              "was written there, read forward in time from the dedupe rule it extends. The "
              "acquired set's identity, licence and counts were deliberately NOT carried: they "
              "grade the instance and stay where they were measured (D-431)."),
    "D-500": ("STEP 2 — WRITTEN. Step 1 was checked and did not apply: §5's Tier G lists the "
              "chromatic material and its Tier J cites this very ratification BY DATE, but "
              "neither STATES the ratification as the scope rule the tiers implement. §5 "
              "STATES RULES — the user's own approved Ruling 39 delegation wording names 'the "
              "decision-tier block' as one of the census's rule-stating sections — so the "
              "ratification was written there with its defense and, beside it, the "
              "research-tier-on-entry clause, so that a reader cannot take the widening for a "
              "gate movement."),
    "D-422": ("STEP 2 — WRITTEN, at §5's Tier J, the tier that owns the jazz ground-truth path "
              "this deferral waits on. Step 1 did not apply: no census section stated the "
              "deferral. The home text states the MECHANISM that makes it a corpus fact — the "
              "held jazz material is melody-and-chord-symbol transcription with the bass and "
              "the voicings absent — and carries no measured value from the experiment that "
              "established it (D-431). The roadmap's own record of the signing is untouched."),
    "D-614": ("STEP 2 — WRITTEN, beside §8c's Stage-5 fitting-pool licence constraint. ★ STEP 1 "
              "WAS CLOSE AND IS RECORDED AS CHECKED-AND-DECLINED: that constraint's last bullet "
              "already says the difficulty case 'carries its own harder version of this caveat', "
              "which states the FACT and not the CONSEQUENCE this entry records — that a "
              "commercial grading feature needs a licence path or labels of our own. A pointer "
              "move onto a sentence that does not state the rule would be admitting it by "
              "stretch, which this ruling forbids. The block STATES RULES — it is rule (h)'s "
              "founding case and is named in the approved Ruling 39 delegation wording — so the "
              "rule was written beside it, kept explicitly apart from the shipped-fitted-value "
              "prohibition it is neighbours with."),
    "D-515": ("STEP 3 — HELD. The owning census element is the §8c NEEDS-VECTOR TABLE, whose N20 "
              "row is what this decision creates and which already carries its adoption. A "
              "needs-vector row is a per-need STATE entry, so the table records findings and "
              "admits no rule. The generalizable half — that a ground-truth class gets its own "
              "row rather than a remark under a neighbour — is NOT written, because the record "
              "states the decision for this one need and authoring the general form would be "
              "composing a rule the record never made. Adding a rule-stating block to a findings "
              "table is the document-structure act this ruling reserves to the user."),
    "D-516": ("STEP 3 — HELD, for the same reason as D-515 and more plainly: this entry records "
              "an ADOPTION EVENT — two ground-truth classes admitted to the needs vector — and "
              "not a rule. Its content is the vector's MEMBERSHIP, the vector is the §8c findings "
              "table, and both adopted rows already carry their adoption there. There is no rule "
              "to write into a rule-stating section, and restating the table's own rows in one "
              "would breach #6."),
    "D-475": ("STEP 3 — HELD. This is a per-corpus ESTABLISHMENT verdict (#19) about one held "
              "annotation set, and the census carries no section for it at all: the set is named "
              "nowhere in the document, and its natural census element is the §8c needs-vector "
              "row for dual-annotator material — a findings table. Writing a verdict about one "
              "corpus into a rule-stating section would be the mirror of the error step 3 "
              "prevents: a finding placed where rules are stated. The row is named and the entry "
              "is left for the user."),
    "D-613": ("STEP 3 — HELD, and the reason is a SPLIT that is not a session's to make. The "
              "entry has two halves: a fact-of-absence (implied-polyphony ground truth is "
              "confirmed absent — do not re-search) and a RULE (what the surviving voice labels "
              "actually measure must be said at intake). The finding half's census element is "
              "the §8c needs-vector row that already carries it — a findings table — while the "
              "rule half would fit §8c's intake-rule block, which does state rules. Splitting "
              "one entry into two is a decision about the decisions register's own unit, which "
              "the user settled by ruling once already, at D-291/D-656, and it is not taken "
              "here."),
}


def closed_row_home(entry_id: str) -> str:
    """Where an executed entry went, and in which wave -- so one hardcoded date cannot stand for
    every wave (#12)."""
    if entry_id in RULED_2026_08_08:
        return (f"{RULED_2026_08_08[entry_id]} Layer 6 (re-homed 2026-08-08 on the user's ruling "
                "of that date, with both ends of the arm split visible and the conformance "
                "question rowed at OI-349 — no longer in item 1)")
    if entry_id in REHOMED_2026_08_09_SEVENTH_RETURN:
        return (f"{REHOMED_2026_08_09_SEVENTH_RETURN[entry_id]} P2 (re-homed 2026-08-09 under the "
                "user's Ruling 38, the homing default, by the seventh return continuation; class "
                "`process` — no longer in item 1)")
    if entry_id in REHOMED_2026_08_09_EIGHTH_RETURN:
        doc, sec = REHOMED_2026_08_09_EIGHTH_RETURN[entry_id]
        return (f"{doc} {sec} (re-homed 2026-08-09 under the user's Ruling 40, STEP 2 of the "
                "three-step census procedure, by the eighth return continuation; the rule written "
                "in the section's own voice under that ruling's census-edit licence, the kind half "
                "judged before the write — no longer in item 1)")
    if entry_id in OWNER_RULED_2026_08_07_HOMING:
        return (f"{OWNER_RULED_2026_08_07_HOMING[entry_id]} (re-homed 2026-08-07 on the user's "
                "owner ruling, the homing wave — no longer in item 1)")
    if entry_id in OWNER_RULED_2026_08_07:
        return OWNER_RULED_2026_08_07[entry_id]
    if entry_id in A1_OWNER_IS_DETERMINATE:
        return "CLAUDE.md (re-homed 2026-08-07 under the homing licence — no longer in item 1)"
    return "ARCHITECTURE.md (re-homed 2026-08-04 — no longer in item 1)"

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
    "D-539": (REHOME, "cowork_engage_arc_plan.md, beside the MEASURE-BEFORE-BUILD gate", True,
              "Decompose every error slice into structural, fitted and ceiling BEFORE building. "
              "RULED 2026-08-07 (user, R3): it is an ORDER-OF-WORK rule, and the arc plan is the "
              "ratified contract for the order of work that CLAUDE.md's principles section "
              "delegates to and does not restate (#6); D-277, the method's recorded descendant, "
              "already lives there. The excluded alternative is CLAUDE.md beside the #17 funnel, "
              "which would begin restating what the governing file delegates. The ruling is itself "
              "the authorization for that one edit of a ratified contract document, and no "
              "standing edit surface is widened by it. THE FORMER OWNER AND REASON, PRESERVED "
              "(#12): 'CLAUDE.md (the standing method rules)', owner_is_unambiguous False, reason "
              "'Decompose every error slice into structural, fitted and ceiling BEFORE building. A "
              "standing method rule whose home is the principles, outside this dispatch's edit "
              "surface.'"),

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
    "D-538": (NO_HOME, None, False,
              "RULED 2026-08-07 (user, R2): the entry is ratified as correctly recorded AND its "
              "content is ruled superseded in the same act — by principle #14 (D-177) and by gate "
              "block (A)'s measured non-increase (D-115), the two successors this entry's own "
              "record already named before the ruling. Both are homed, so writing its early "
              "concrete form into a specification would put a second copy of a homed rule, which "
              "#6 forbids — and would put in-force discipline into a live specification under a "
              "LEGACY subject a reader could misapply to the live solution. Its disposition under "
              "D-642 is DERIVED at tools/audit/decisions/r1_superseded_reach.json and is not "
              "authored here. THE FORMER ROUTE, OWNER AND REASON, PRESERVED (#12): RE-HOME, "
              "'CLAUDE.md (the staging discipline for a multi-signal change)', "
              "owner_is_unambiguous False, reason 'One signal at a time with the corpus re-measured "
              "between. A landing discipline rather than a scoring rule; its home is the project's "
              "standing rules, outside this dispatch's edit surface.'"),

    # ---- docs/iteration_path1_summary.md -----------------------------------------------------
    "D-280": (REHOME, "ARCHITECTURE.md §3.3 (the inference/presentation boundary)", False,
              "Gates read structured fields only, never a chord symbol string or a Roman numeral. §3.3 "
              "states the boundary this restricts, but the entry is an INPUT restriction on scoring, which "
              "docs/scoring_model.md also governs; the owner is not determinate."),
    "D-281": (REHOME,
              "BUILD_AND_TEST.md §2, the Corpus Regression Check (the measurement procedure)", True,
              "The batch measurement tool must emit the structured fields on every alternative or a "
              "corpus measurement silently reverts. RULED 2026-08-07 (user, R1): its owner is the "
              "measurement procedure, and BUILD_AND_TEST.md is the authoritative document for the "
              "measurement tools, which is the proper layer (#7). The excluded alternative is "
              "CLAUDE.md gate block (A), which governs how the recorded numbers are READ and "
              "already delegates commands and tooling to that document, so homing the schema floor "
              "there would blur the layer and restate what is pointed at (#6); a pointer from the "
              "gate block is permitted, a copy is not. THE FORMER OWNER AND REASON, PRESERVED "
              "(#12): 'CLAUDE.md gate block (C) / BUILD_AND_TEST.md (the measurement procedure)', "
              "owner_is_unambiguous False, reason 'The batch tool must emit the structured fields "
              "on every alternative or the corpus figures silently revert. Its owner is the "
              "measurement procedure, outside this dispatch's edit surface.'"),

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
    # ★ RULED TWICE, HELD ONCE, AND HOMED ON THE SECOND RULING. The 2026-08-07 ruling routed it to
    # the Layer-6 section with §11.5 pointing and made the LEGACY mark conditional on an arm check at
    # the code; that check came back MIXED, which the homing dispatch names as the outcome that HOLDS
    # an entry. The user then ruled on 2026-08-08 (Option A) that it is homed in a form showing BOTH
    # ENDS of the split, and the conformance question is rowed rather than answered. It is therefore
    # no longer in item 1, and its membership of `RULED_2026_08_08` is what says so.
    "D-472": (REHOME, "ARCHITECTURE.md Layer 6 (the grouping layer), §11.5 pointing", False,
              "Key areas are grouped by a smoothing pass over stabilized regions. RULED 2026-08-07 "
              "(user, the owner-rulings homing wave): the owner is the Layer-6 section, which owns "
              "key-areas in the target architecture, with §11.5 pointing — and the LEGACY mark "
              "follows an arm check at the code. The arm check came back MIXED: the grouping rule "
              "is shared and runs on the production record arm; the Pass-4 stabilization the entry "
              "names as its precondition is legacy-arm-only. ★ RULED AGAIN 2026-08-08 (user, Option "
              "A) AND HOMED: the grouping rule is specified as LIVE on the production record arm "
              "and the stabilization sits beside it marked ⚠ LEGACY, each end carrying its citation "
              "— one home, both halves visible (#12) — and the conformance question, whether the "
              "record arm satisfies the stated precondition by other means or the live path groups "
              "un-stabilized regions, is ROWED as `OPEN_ITEMS.md` OI-349, which GATES. Neither "
              "answer is asserted. THE HOLD, PRESERVED (#12) — it was a result and not a gap: 'A "
              "mixed arm is the dispatch's stated outcome for holding an entry and returning it to "
              "the user, so no home text was written and the entry stays in item 1.' THE FORMER "
              "OWNER AND REASON, PRESERVED (#12): 'ARCHITECTURE.md §11.5 (Region Analysis and the "
              "Chord Track)', owner_is_unambiguous False, reason 'Key areas are grouped by a "
              "smoothing pass over stabilized regions. The key-area grouping is described both "
              "there and in the Layer-6 section, which owns key-areas in the target architecture; "
              "the owner is not determinate.'"),
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
# Follows the licensed surface rather than restating it (#6). Former value, preserved (#12):
# EXECUTABLE_OWNER_SUBSTRING = "ARCHITECTURE.md", correct while that was the whole surface.
EXECUTABLE_OWNER_PREFIXES_FOR_READING = EXECUTABLE_OWNER_PREFIXES


def _owner_judgment_reading(rows: list[dict]) -> dict:
    """Read the owner JUDGMENT rather than the column, over the open RE-HOME rows (OI-342)."""
    open_rehome = [r for r in rows if r["route"] == REHOME and not r["closed_by_this_wave"]]
    surface_only = [r for r in open_rehome if EDIT_SURFACE_PHRASE in r["reason"]]
    determinate = [r for r in open_rehome
                   if DETERMINATE_PHRASE in r["reason"]
                   and NOT_DETERMINATE_PHRASE not in r["reason"]]
    on_surface = [r for r in open_rehome
                  if (r["owning_specification"] or "").startswith(
                      EXECUTABLE_OWNER_PREFIXES_FOR_READING)]
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
                "★ CORRECTED 2026-08-07, because the widening made the former statement false. IT "
                "FORMERLY READ (#12): 'The disagreement OI-342 records is confined to rows whose "
                "owner is NOT on the editable surface, so it moves nothing this wave could "
                "execute. What it moves is what the column MEANS to a reader deciding how much of "
                "item 1 is closeable.' That was true while the surface was ARCHITECTURE.md alone. "
                "The user widened it to the three further files on 2026-08-07, SCOPED TO HOMING "
                "ACTS, and the disagreement then moved EXACTLY the rows the homing wave executed: "
                "eight entries whose column says ambiguous and whose recorded reason names a "
                "determinate CLAUDE.md site and then says it was out of reach. They were homed. "
                "The column is still untouched -- what carries the determinacy verdict is the "
                "separate A1 field, for the reason OI-342 gives."
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
    """A RE-HOME whose owner is determinate AND lies inside the licensed edit surface.

    Determinacy is read from the `unambiguous` column OR, for the licensing class, from the
    A1 verdict recorded beside it — see that table for why the column is not rewritten.

    A THIRD CASE: the user RULED the owner (2026-08-07). A ruling settles determinacy and carries
    its own authorization for the edit it names, so it admits the entry DIRECTLY rather than
    through the prefix table — see `OWNER_RULED_2026_08_07` for why that table is not widened.
    The ROUTE is still required to be a re-home: the ruling settled where the entry belongs, not
    that any route whatever discharges it, and a later wave that re-routed one of these must not
    inherit the ruling's answer to a question it no longer asks."""
    route, owner, unambig, _ = ROUTES[entry_id]
    if entry_id in REHOMED_2026_08_09_EIGHTH_RETURN:
        # A FIFTH CASE, on the same ground as the fourth immediately below: Ruling 40's STEP 2 is
        # the re-home Ruling 38 makes the default, performed under a ruling that names the target
        # SECTION. The route that governs is the RULED one, and the authored tuple still says
        # NEEDS A DELEGATION because #12 keeps it there.
        return route in (REHOME, DELEGATION)
    if entry_id in REHOMED_2026_08_09_SEVENTH_RETURN:
        # A FOURTH CASE, and it needs its own line rather than joining the three below, because
        # Ruling 38 converts an authored NEEDS A DELEGATION into a RE-HOME and that conversion is
        # applied at ROW BUILD rather than in ROUTES -- the authored judgment is preserved there
        # (#12), which is the whole point of `authored_route_before_ruling_38`. So the route that
        # GOVERNS these two is the RULED one, and reading the authored tuple alone would report an
        # act that was performed as never having happened.
        return route in (REHOME, DELEGATION)
    if (entry_id in OWNER_RULED_2026_08_07 or entry_id in OWNER_RULED_2026_08_07_HOMING
            or entry_id in RULED_2026_08_08):
        return route == REHOME
    determinate = bool(unambig) or entry_id in A1_OWNER_IS_DETERMINATE
    return bool(route == REHOME and determinate and owner
                and owner.startswith(EXECUTABLE_OWNER_PREFIXES))


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
            "home_document": closed_row_home(i),
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
            row = {
                "id": i,
                "home_document": doc,
                "route": route,
                "owning_specification": owner,
                "owner_is_unambiguous": unambig,
                "executable_under_this_dispatch": _was_executed(i),
                "closed_by_this_wave": False,
                "reason": reason,
                "authored": "the route, the owner, the unambiguity verdict and the reason",
            }
            # Ruling 38, applied to the OPEN population only. The authored route is preserved
            # beside the ruled one (#12): the authored judgment records what a session read off
            # the document, and the ruling records what decides the act.
            if route == DELEGATION:
                row["route"] = REHOME
                row["authored_route_before_ruling_38"] = DELEGATION
                row["ruled_by"] = RULING_38
            elif route == REHOME:
                row["ruled_by"] = RULING_38 + " (this row's authored route already agreed)"
            else:
                row["ruled_by"] = (
                    "NOT REACHED by Ruling 38. This row records that NEITHER route applies — the "
                    "live content is carried by a homed successor, so re-homing would put a second "
                    "copy of a homed rule (#6), or there is no decision content to write. The "
                    "ruling settles which of two available routes is the default; it creates none "
                    "where the record says there is none. Dispositioned under D-642 at "
                    "tools/audit/decisions/r1_superseded_reach.json.")
            # Ruling 39, the census exception. The membership is DERIVED from the authored owner
            # string rather than listed by hand, so a row that later gains or loses the census as
            # its owner joins or leaves this set by itself.
            if owner and "cowork_score_census.md" in owner:
                row["ruled_by_39"] = RULING_39
                row["ruling_39_outcome"] = RULING_39_MEASURED
                # Ruling 40 replaces 39's unreachable outcome with the three-step procedure. The
                # membership is the SAME derived set (the authored owner string), so a row that
                # later gains or loses the census as its owner joins or leaves this set by itself.
                row["ruled_by_40"] = RULING_40
                row["ruling_40_step_taken"] = RULING_40_STEPS.get(
                    i, "NOT YET EXECUTED — the procedure had not been run for this entry when "
                       "this artifact was generated.")
            rows.append(row)

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
        "what_a_homing_dispatch_may_execute": {
            "surface": list(EXECUTABLE_OWNER_PREFIXES),
            "why": "The standing authorization covers src/composing/, notationaccessibility.cpp and "
                   "ARCHITECTURE.md. ★ WIDENED 2026-08-07 by the user's ruling: a HOMING dispatch "
                   "may also touch docs/scoring_model.md, CLAUDE.md and BUILD_AND_TEST.md, SCOPED "
                   "TO HOMING ACTS ALONE and to no other edit of those files.",
            "the_former_statement_preserved_12": (
                "'surface': 'ARCHITECTURE.md only'; 'why': 'The standing authorization covers "
                "src/composing/, notationaccessibility.cpp and ARCHITECTURE.md. Entries whose "
                "owning specification is CLAUDE.md, docs/scoring_model.md or BUILD_AND_TEST.md are "
                "classified here and NOT executed.' True until the widening; false after it."),
            "consequence_stated_plainly": "A small executed set is a SCOPE BOUND, not a verdict that "
                                          "the remaining entries have no owner. The route column says "
                                          "which do.",
        },
        "★_assumption_A1_of_the_2026_08_07_homing_wave": {
            "the_assumption": (
                "That every licensing-class entry's recorded owner names a DETERMINATE section of "
                "its file. Checked PER ENTRY before anything was written, with a STOP for any "
                "entry it fails: that entry is not homed, it stays in item 1, and it returns to "
                "the user with the owner question rather than to a guessed section."),
            "verdict": (
                "REFUTED FOR THREE OF THE ELEVEN, which the dispatch names as a result and not a "
                "failure — the class was cut by phrase and the cut can be wrong per entry."),
            "determinate_and_homed": sorted(A1_OWNER_IS_DETERMINATE),
            "soft_owner_NOT_homed_and_returned_to_the_user": ["D-281", "D-538", "D-539"],
            "how_the_three_were_identified": (
                "Not by a fresh judgment. `OPEN_ITEMS.md` OI-342 enumerates, in its own words, the "
                "members of this class whose owner is genuinely soft INDEPENDENT of the edit "
                "surface — D-539 ('the principles'), D-538 ('the project's standing rules') and "
                "D-281 (two candidate homes, in two different files) — and states that every other "
                "member names a determinate site. Each of the three is also soft on the face of "
                "its own recorded owner string: two name no section at all, and one names two "
                "sections in two files joined by a slash."),
            "what_is_NOT_claimed": (
                "That the three have no owner, or that any corrected count is proposed for OI-342 "
                "— that row declines to propose one and nothing here proposes one either. What is "
                "claimed is only that the record does not settle WHICH section each of the three "
                "belongs in, and that a session may not settle it."),
            "★_and_the_user_RULED_ALL_THREE_on_2026_08_07": {
                "what_happened": (
                    "The refusal above did the one thing it was for: the question went to the user "
                    "and the user answered it, in three rulings on the same date (dispatch "
                    "`cc_instruction_three_owner_rulings.md` §0a). Recorded here BESIDE the verdict "
                    "rather than in place of it (#12) — the verdict is what a session could not "
                    "settle, these are what the user settled, and collapsing the two would erase "
                    "the refusal that produced the answer."),
                "R1_D_281": (
                    "HOMED in BUILD_AND_TEST.md §2, the Corpus Regression Check. The schema floor "
                    "is a contract of the measurement tools and that document is the authoritative "
                    "one for them (#7). Excluded alternative: CLAUDE.md gate block (A), which "
                    "governs how the recorded numbers are read and already delegates tooling to "
                    "that document (#6)."),
                "R2_D_538": (
                    "RATIFIED AND RULED SUPERSEDED in the same act, by principle #14 (D-177) and "
                    "gate block (A)'s measured non-increase (D-115). No specification is edited "
                    "for it, which is the ruling's point; its route below is NO HOME EXISTS and "
                    "its disposition is derived under D-642 in the R1 application. Excluded "
                    "alternative: homing it beside the gate block would put a second copy of "
                    "in-force discipline into a live specification under a LEGACY subject."),
                "R3_D_539": (
                    "HOMED in cowork_engage_arc_plan.md, beside the MEASURE-BEFORE-BUILD gate — an "
                    "order-of-work rule in the ratified contract for the order of work, where "
                    "D-277, its recorded descendant, already lives. Excluded alternative: "
                    "CLAUDE.md beside the #17 funnel, which would begin restating what the "
                    "governing file delegates. The ruling is itself the authorization for that one "
                    "edit; no standing edit surface is widened, which is why the entry is admitted "
                    "by `OWNER_RULED_2026_08_07` and not by the prefix table."),
                "what_the_rulings_did_NOT_do": (
                    "They settled the OWNER question for these three and nothing else. R1 and R3 "
                    "do not ratify their entries as correctly recorded — D-539's record still "
                    "reads NOT ratified and it stays in the ratification queue; D-281 was already "
                    "ratified on 2026-08-02, before this question arose. No fix to the analysis, "
                    "no design and no inference change is authorized by any of the three, and "
                    "nothing here proposes a corrected count for OI-342."),
            },
        },
        "★_the_2026_08_09_homing_fork_ruling": {
            "the_ruling": RULING_38,
            "recorded_by": "cc_instruction_return_continuation_6.md Task 0",
            "what_it_moves_in_this_table": (
                "Every OPEN row whose AUTHORED route was NEEDS A DELEGATION now carries route "
                "RE-HOME, with `authored_route_before_ruling_38` preserving the authored judgment "
                "beside it (#12) and `ruled_by` naming the ruling. Rows already routed RE-HOME "
                "carry `ruled_by` confirming that their authored route agreed. No reason, owner, "
                "unambiguity verdict or home document is re-authored, and no closed or discharged "
                "row is touched — those are the record of earlier waves."),
            "what_it_does_NOT_move_and_why": (
                "The NO HOME EXISTS class. Those rows do not record a choice between a delegation "
                "and a re-home; they record that NEITHER applies — the entry's live content is "
                "carried by a homed successor, so re-homing would put a second copy of a homed "
                "rule (#6), or there is no decision content to write at all. Ruling 38 settles "
                "which of two AVAILABLE routes is the default and says nothing about #6, so it "
                "creates no route where the record says there is none. That class stays "
                "dispositioned under D-642 at r1_superseded_reach.json (#6)."),
            "the_exception_list_is_EMPTY_and_that_is_the_ruled_state": (
                "No document is excepted at ruling time. A later exception — a document the user "
                "wants kept as a contract home by delegation — is a NEW USER RULING NAMING THE "
                "DOCUMENT, taken BEFORE that document's entries are re-homed and never after. A "
                "session may not except a document, and an empty list here is the ruled state "
                "rather than an unfilled field."),
            "the_excluded_alternative_recorded": (
                "Delegation as the default. It grows the contract-home class, requires the user's "
                "writing per document (rule (g)), and runs against both concrete declinations "
                "already on the record — the voice-leading delegation the user declined to widen "
                "and the structural-integrity audit for which the user ruled no delegation is "
                "drafted or written."),
        },
        "★_the_2026_08_09_census_exception_ruling_and_its_measured_outcome": {
            "the_ruling": RULING_39,
            "recorded_by": "cc_instruction_return_continuation_7.md Task 0",
            "the_act_performed": (
                "The approved wording was written VERBATIM into `ARCHITECTURE.md`, sited beside the "
                "existing §8c naming and supplementing rather than replacing it; this document's "
                "FORMS grade in `gen_phase1p_delegation_bar.py` moved to the explicit-delegation "
                "form with the former grade preserved (#12), rule (k1) governing because the "
                "document is now named in an admitting and two weaker forms; and the authored "
                "`delegation_scope` in the register data moved from `sections` to `document`, the "
                "former scope and its section list preserved (#12)."),
            "what_the_delegation_MOVED_measured_rather_than_assumed": (
                "NOTHING, in either direction. Every entry actually homed in `cowork_score_census.md` "
                "already sat in one of the seven sections the earlier section-list naming reached, "
                "and every one of those sections already carried a states-rules judgment, so all of "
                "them were `contract-home` before this act and are `contract-home` after it. The "
                "sections the widening newly reaches hold no register entry at HEAD. Established at "
                "`home_classification.json`, whose class totals and `decided_by` split are identical "
                "to the committed ones read from the git object at the commit before this act."),
            "★_the_predicted_close_is_REFUTED_and_the_rows_are_HELD": (
                "The ruling's premise is that these entries close by classification once the census "
                "is delegated to. They do not, and the cause is a checkable fact rather than a "
                "judgment: a register entry's class is decided by ITS OWN HOME DOCUMENT. These "
                "entries name the census as their OWNING SPECIFICATION — the surface that ought to "
                "state their rules — while each is HOMED in a different document, and every one of "
                "those documents is named in none of the three user-ratified surfaces, so clause (a) "
                "excludes them before any delegation is graded. A delegation to the census cannot "
                "reach an entry that does not sit in the census."),
            "the_two_routes_that_remain_and_why_neither_is_a_session's_to_pick": (
                "(1) Move each entry's HOME field into the census section that already states its "
                "rule, where one does — register-data maintenance, and the only route that is "
                "literally the zero text movement the ruling names. It has to be decided per entry, "
                "because it is only available where the census already carries the rule. (2) Perform "
                "the re-home Ruling 38 makes the default, writing each rule into the census section "
                "that owns it — which is the text movement this exception was taken to avoid, and "
                "which would land in a findings table for some of these entries, exactly the "
                "kind-half STOP the ruling arms. Choosing between a ruling's ACT and its stated "
                "OUTCOME is not a session's act, so each row is held individually with both routes "
                "named."),
            "what_is_NOT_claimed": (
                "That the ruling is wrong, or that the census is the wrong owner. The owner question "
                "is RULED and this table records it as ruled; what is refuted is only the mechanism "
                "by which the rows were expected to close."),
            "where_it_is_reported": "cowork_away_returns.md §1.12",
        },
        "★_the_2026_08_09_procedure_that_replaces_that_unreachable_outcome": {
            "the_ruling": RULING_40,
            "recorded_by": "cc_instruction_return_continuation_8.md Task 0",
            "what_it_changes_and_what_it_does_not": (
                "Ruling 39's ACT is untouched — the census is still the ruled owner and the "
                "delegation the user approved verbatim is still written. What is replaced is the "
                "predicted CLOSE, which the block above refutes by measurement. So the block above "
                "is NOT withdrawn (#12): it records why the rows did not close, and this one "
                "records what closes them instead."),
            "which_of_the_two_named_routes_it_takes": (
                "BOTH, in a fixed order, with the choice made per entry by a stated test rather "
                "than by preference. Step 1 is route (1) of the block above — the pointer move, "
                "available only where the census already carries the rule. Step 2 is route (2), "
                "the re-home Ruling 38 makes the default, and it carries a NEW census-edit licence "
                "the ruling grants, scoped to rule-stating sections and to these entries only. "
                "Step 3 is the kind-half STOP Ruling 39 armed, now given an explicit outcome: the "
                "entry is HELD with its row named rather than written by stretch."),
            "★_why_the_kind_half_is_judged_before_any_write": (
                "Register rule (h)'s two halves are applied form-first, kind-second-and-last "
                "(rule (k2)), and the kind half is DECISIVE: a well-formed delegation to a section "
                "that RECORDS FINDINGS rather than STATES RULES admits nothing. The census is a "
                "census — its findings tables are the majority of it — so a procedure that wrote "
                "first and checked afterwards would put rules into findings tables, which is the "
                "single failure this ruling's step 3 exists to prevent."),
            "the_per_entry_outcome_is_authored_and_is_on_each_row": (
                "`ruling_40_step_taken`. An entry whose procedure has not run says so rather than "
                "being absent, so a partially executed pass cannot read as a complete one."),
            "what_this_ruling_does_NOT_authorize": [
                "Any edit to a census FINDINGS TABLE, in either direction.",
                "Any census edit for an entry outside this derived set.",
                "Any fix to the analysis, any design, any inference change. Phase 1 (D-231) "
                "remains open and #8's three-clause gate stands.",
            ],
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
