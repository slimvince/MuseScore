#!/usr/bin/env python3
"""THE JULY SCREEN — every out-of-period specification-bearing flagged hunk read one at a time.

Dispatch: `cc_instruction_period_checks.md`, Task 2 (Cowork, 2026-08-15), executing the second
ruling of `cowork_rulings_2026_08_15_period_start.md`.

WHAT IT IS FOR.  The restructuring period was ruled to open EXCLUSIVE at `b006dc15b5`.  The
decision surface that ruling was taken on records the risk of that choice in its own words: if a
code-influenced specification correction happened before the ruled start and outside a ratified
act, it falls outside the period and its destroyed signal is lost silently.  The screen reads the
population where such a change could sit — the specification-bearing documentation changes OUTSIDE
the ruled period — and reports what it finds.  **The falsification rule is the user's and is
LIVE:** a positively code-influenced correction re-opens the period question, and the re-opening is
the user's act on this report, never this tool's.

WHAT THE SCREEN JUDGES, in the ruling's own words (Ruling 5 of the eighteenth stop): *"whether any
fact in the code influenced the change.  Influence is invisible in the text: a narrowed rule reads
exactly like a rule that was always narrow."*  So the screen finds POSITIVE evidence of influence
and nothing else; a clear verdict is bounded by that invisibility, which is what the UNDETERMINED
class is for.

WHAT IS DERIVED AND WHAT IS AUTHORED:

  DERIVED  — the population, imported whole from `tools/audit/period_stratum_split.json` and never
             re-listed (#6); each hunk's text, retrieved from the git object by explicit hash; the
             removed/added line counts of what was retrieved, cross-checked against what the
             population records; every count in the artifact and the report.
  AUTHORED — the verdict per hunk, its ground, its citations and its reported shape.  A verdict
             about a documentation change cannot be computed, and this file is where that judgment
             lives, one entry per hunk, each naming what it was made from.

THE FOUR CLASSES ARE THE DISPATCH'S, AND THE ORDER THEY ARE APPLIED IN IS DECLARED HERE, because
the dispatch fixes the classes and not the order, and the order decides cases:

  1. POSITIVELY-CODE-INFLUENCED — the change WITHDRAWS, NARROWS, QUALIFIES or REPLACES something
     the documentation already stated, and the source of that replacement is a fact read in
     implementation code THIS COMMIT DID NOT WRITE; or the change's own account states that a
     documentation statement was corrected against the implementation.  **Applied FIRST**, so that
     a ratified act cannot launder a correction made under it.
  2. RATIFIED-ACT-EDIT — the change writes, re-stamps or records what a NAMED user act ruled,
     ratified or directed, including the same-commit documentation half of a ratified change to the
     code.  Every such verdict names the act AND where its ratification is recorded, or it is not
     admitted (assumption A3).
  3. RESTRUCTURING-SHAPED — relocation, split, re-heading or growth whose source is not a fact read
     in implementation code the commit did not write.
  4. UNDETERMINED — NOT CLEARED.  The dispatch's own gloss for this class is *not cleared*, and it
     is used here in that sense: a fact in the implementation is the source of the change but the
     change adds material rather than replacing a standing statement, or no ground supports any of
     the three classes above.  It is reported whole and never argued down.

WHY THE UNDETERMINED CLASS IS LARGE AND WHY THAT IS NOT A HEDGE.  The pre-period population
contains documentation written in the same commit as the code it describes — the standing
same-commit sync rules (#10, and the scoring-model sync rule) require exactly that.  Such a change
is influenced by facts in the code by construction, and it destroys no discrepancy, because the
documentation and the implementation moved together in one authored act.  It is not cleared, and it
is not a correction; so it is reported in the not-cleared class with its shape named, rather than
being waved through as restructuring or counted as a falsification.

THE DECLARED THIRD VALUE OF THE POLLUTION INPUT (Ruling 2(b), 2026-08-22).  A member of the
coverage gap -- one with no changed passage in the candidate enumeration at all -- has no measured
pollution distribution and must not be read as clean.  Its per-document pollution input is
therefore recorded as a DECLARED THIRD VALUE: "NOT EDITED IN THE RESTRUCTURING PERIOD; last
authored before it, at <commit, date>".  It is DERIVED, never typed -- the period's own bounds are
read from `tools/audit/doc_change_candidates.json` -> `range`, and the authoring commit and its
date from `git log` at those bounds.  ITS OWN STOP: a commit strictly inside the period that
touches the file contradicts the coverage-gap reason the enumeration gives for itself, and the two
readings disagreeing STOPS the tool rather than declaring anything; so does a gap member the
enumeration DOES carry (enumerated, every changed passage PURE), for which Ruling 2(b) declares
nothing.

THE STOPS, so this cannot silently stop being a screen:
  1. a population member with no authored verdict STOPS the tool — the population is imported, so a
     hunk entering it cannot be graded silently or quietly dropped;
  2. a verdict naming a hunk the population does not carry STOPS it, which is the same demand in
     the other direction;
  3. a verdict outside the four-class vocabulary, or a reported shape outside the declared one,
     STOPS it;
  4. a RATIFIED-ACT-EDIT verdict that does not name the act AND where its ratification is recorded
     STOPS it (assumption A3's own condition, made mechanical);
  5. a verdict with no ground STOPS it.

WHAT THIS DOES NOT DO.  It edits no screened document.  It restores nothing, reverts nothing and
corrects nothing.  It closes no open-items row and writes no decisions-register entry.  It does not
re-open
the period question — it reports what would, and the act is the user's.

Usage:
  python tools/audit/gen_july_screen.py            # write the artifact and the report
  python tools/audit/gen_july_screen.py --check    # re-derive both, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import hashlib
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()

ROOT = Path(__file__).resolve().parent.parent.parent
IN_SPLIT = ROOT / "tools" / "audit" / "period_stratum_split.json"
IN_MAIN = ROOT / "tools" / "audit" / "doc_change_candidates.json"
OUT_JSON = ROOT / "tools" / "audit" / "july_screen.json"
OUT_REPORT = ROOT / "tools" / "audit" / "july_screen_report.md"

CODE_INFLUENCED = "POSITIVELY CODE-INFLUENCED"
RATIFIED = "RATIFIED-ACT EDIT"
RESTRUCTURING = "RESTRUCTURING-SHAPED"
UNDETERMINED = "UNDETERMINED"
CLASSES = (CODE_INFLUENCED, RATIFIED, RESTRUCTURING, UNDETERMINED)

# ── THE WIDENED POPULATION (added 2026-08-21 by
#    `cc_instruction_successor_plan_landing_and_step_zero.md` Task 3, executing Ruling 7) ──────────
#
# THE METHOD IS INHERITED WHOLE AND UNCHANGED.  The four classes above, the ORDER they are applied
# in, the six reported shapes and the five STOPs are Ruling 7's own clause — "its method untouched" —
# and nothing below amends any of them.  What is added is a SECOND POPULATION and a SECOND AUTHORED
# BLOCK for it; the existing sixty-eight verdicts are neither re-read nor re-graded, and a widened
# hunk that is ALREADY in the existing screen population INHERITS that verdict rather than receiving
# a new one.
#
# TWO FURTHER VALUES, DECLARED AS ADDITIONS RATHER THAN SMUGGLED INTO THE VOCABULARY:
#
#   NOT YET READ            the ONE declared exception to the STOP that a population member with no
#                           authored verdict halts the tool.  A widened member nobody has read is
#                           admitted to the artifact, counted in its own class, and reported as
#                           unread — never silently absent, and NEVER counted as UNDETERMINED.  It
#                           is the DEFAULT for an unauthored member and may not be authored, so a
#                           member cannot be marked unread as a judgment.
#   OUTSIDE NAMED SECTIONS  a hunk of a member whose delegation names SECTIONS, falling outside
#                           them.  It is RECORDED and NOT GRADED, so the four classes never apply to
#                           text the ruled document set does not reach.  It is authored, with its
#                           ground, exactly as any other verdict.
WIDENED_KEY = "★_the_widened_screen_population"
NOT_YET_READ = "NOT YET READ"
OUTSIDE_SECTIONS = "OUTSIDE NAMED SECTIONS"
WIDENED_VOCABULARY = CLASSES + (NOT_YET_READ, OUTSIDE_SECTIONS)

# ── AUTHORED — the DECLARED THIRD VALUE of the pollution input (Ruling 2(b), 2026-08-22) ────
NOT_EDITED_IN_PERIOD = "NOT EDITED IN THE RESTRUCTURING PERIOD"
THIRD_VALUE_RULING = (
    "Ruling 2(b) of `cowork_rulings_2026_08_22_step_zero_return_sitting.md`: \"ONLY the "
    "pollution input of Ruling 12 is affected. For each of the nine, the July screen's "
    "per-document value is recorded as a DECLARED THIRD VALUE — 'NOT EDITED IN THE "
    "RESTRUCTURING PERIOD; last authored before it, at <commit, date>' — derived by the "
    "generator from the candidate enumeration and from git, never hand-typed (#17f, D-431). "
    "It is distinct from a measured distribution and from 'clean': the screen measures "
    "corrections made toward the code DURING the period and has never measured "
    "authoring-time influence for any member; the fact-gate tests that, per statement, for "
    "every source.\"")

# AUTHORED — the reported shapes.  A shape is never a verdict; it is what a reader needs in order to
# see WHICH KIND of change sits behind a verdict, and it is the device the candidate pass used for
# its look-alike signals.
SHAPES = {
    "measured-value-re-stamp":
        "The change re-stamps measured values into gate block (A) at a ratified re-baseline. The "
        "values describe what a measurement of the system produced; they are not a statement of "
        "design intent, and every superseded column is preserved in place (#12).",
    "same-commit-code-documentation":
        "The change documents code the SAME commit introduces, under the standing same-commit sync "
        "rules. Influenced by facts in the code by construction; destroys no discrepancy, because "
        "documentation and implementation moved together in one act.",
    "describes-pre-existing-implementation-behaviour":
        "The change ADDS a description of how the implementation already behaves, read at the code "
        "or measured on it. Nothing standing is withdrawn — in the instances here the behaviour is "
        "named as a DEFECT — but the source is the implementation, so the hunk is not cleared.",
    "governing-decision-record":
        "The change records a user ruling, ratification or direction in the governing document.",
    "document-relocation-or-re-heading":
        "The change moves, splits, re-heads or re-points documentation; no fact from the "
        "implementation is its source.",
    "new-document-content":
        "The change creates a document or a section of one, with no fact from the implementation as "
        "its source.",
}

# ── AUTHORED — the verdict per hunk ──────────────────────────────────────────────────────────────
#
# Keyed by (commit, file, hunk header) — the identity the population publishes.  Every entry was
# made by reading that hunk's own removed and added text at the git object, together with the
# commit's own account (its subject and body), and nothing else.  `act` and `ratification_at` are
# required for a RATIFIED-ACT-EDIT and are the assumption-A3 condition made mechanical.
V: dict[tuple[str, str, str], dict] = {}


def v(commit, path, header, verdict, ground, shape, act=None, ratification_at=None, remark=None):
    V[(commit, path, header)] = {"verdict": verdict, "ground": ground, "shape": shape,
                                 "act": act, "ratification_at": ratification_at, "remark": remark}


# --- 2026-07-11 · the open-items register stratum -------------------------------------------------
v("6b4ca1752b6f857027da1b9ddff4ea9fd3081814", "CLAUDE.md", "-44 +44,3", RATIFIED,
  "The hunk rewrites principle #17(c) to put the control-flow question first, and the added text "
  "carries its own attribution — \"control flow — ratified sharpening 2026-07-10, the EG-2 desk-sim "
  "lesson\". The commit's account opens \"User ratified the #17(c) sharpening\". No fact about the "
  "implementation appears in the change or in the account.",
  "governing-decision-record",
  act="the #17(c) control-flow-first sharpening of the Premise Gate",
  ratification_at="the added text itself; the commit's own account; and CLAUDE.md's #17 provenance "
                  "paragraph at HEAD, which records #17–19 as ratified by the user on 2026-07-10")

v("2454658f077a2ba5efd43600b409b309ebfdd486", "CLAUDE.md", "-63,0 +64,6", RATIFIED,
  "The hunk adds the fact-publication corollary, whose own first line reads \"(ratified by the "
  "user, 2026-07-10)\". The commit's account opens \"User ratified: (1) the fact-publication "
  "corollary\". Its evidence citations are to two Cowork documents, not to the code.",
  "governing-decision-record",
  act="the fact-publication corollary to #6/#7/#12",
  ratification_at="the added text itself, and the same corollary at CLAUDE.md at HEAD")

v("7123c7cb5512b011811edb4b4c87bb1d8c94e877", "CLAUDE.md", "-74 +74", RESTRUCTURING,
  "One pointer, `COWORK_HANDOFF.md` → `cowork_handoff.md`, following the tracked rename of that "
  "documentation file in the SAME commit. The source is a documentation file's own name; nothing "
  "about the implementation appears in the change or in the account.",
  "document-relocation-or-re-heading")

v("239408faadf40e2d46c428397522ca3d688dbe5d", "CLAUDE.md", "-554,0 +555,15", RATIFIED,
  "The hunk adds two conventions, each carrying its own attribution — \"(User-directed, repeatedly; "
  "recorded 2026-07-11.)\" and \"(user-directed, 2026-07-11)\". Neither mentions the implementation.",
  "governing-decision-record",
  act="the no-self-invented-labels convention and the standing self-check after every coding exercise",
  ratification_at="the added text itself, and both rules at CLAUDE.md at HEAD")

# --- 2026-07-12 · the OI-142/OI-143 key-grading re-baseline ---------------------------------------
for hdr in ("-177,11 +177,18", "-213,4 +220,12"):
    v("d9b52ba9696ae51f1504c902c04825c538313754", "CLAUDE.md", hdr, RATIFIED,
      "Gate block (A) is re-stamped with the values the OI-142/OI-143 re-baseline measured. The "
      "commit's subject carries \"(user-ratified 2026-07-12)\" and the added text repeats it. The "
      "superseded column is preserved in place with its snapshot directory named (#12). What the "
      "re-baseline changed is the GRADING — the transposition offsets applied to the ground truth "
      "and the key column split in two — not a statement about what the implementation does.",
      "measured-value-re-stamp",
      act="the OI-142/OI-143 key-grading re-baseline",
      ratification_at="the commit subject and the added text; the same re-baseline is recorded in "
                      "gate block (A)'s superseded-column lineage at CLAUDE.md at HEAD")

v("fe985ab04757dc9eb214ed12664001fa5156238e", "CLAUDE.md", "-68,0 +69,9", RATIFIED,
  "The hunk adds the amendment whose own opening is \"*Amendment (user, 2026-07-12, at the "
  "evidence-inventory discussion):*\" and which quotes the user's rationale. The commit's account "
  "names it \"the user's 2026-07-12 amendment to the fact-publication corollary\".",
  "governing-decision-record",
  act="the user's amendment for EVIDENCE-class facts (publish broadly without a named consumer)",
  ratification_at="the added text itself, and the same amendment at CLAUDE.md at HEAD")

# --- 2026-07-13 · the OI-132 mode-grading consolidation -------------------------------------------
for hdr in ("-194 +194", "-196,8 +196,22", "-230,7 +244,12"):
    v("800f1a12bf136ebc80b84d05427570a9be0a7a5b", "CLAUDE.md", hdr, RATIFIED,
      "The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. "
      "The commit's account carries both dates in terms — \"Ruling: the user, 2026-07-12 … "
      "Ratified: the user, 2026-07-13\" — and the added text repeats \"user-ratified 2026-07-13\". "
      "The superseded columns are preserved with their snapshot directory named (#12). The "
      "consolidation changed how an emitted mode is GRADED, not what the implementation does.",
      "measured-value-re-stamp",
      act="the OI-132 parent-collection mode-grading consolidation",
      ratification_at="the commit's own account; and the same convention at CLAUDE.md at HEAD, "
                      "among the four grading conventions the robust unit is measured under")

# --- 2026-07-14 · the OI-168 measurement build ----------------------------------------------------
v("153d45e78c5162c17844c7a488f9e9901b524141", "ARCHITECTURE.md", "-609,0 +610,4", UNDETERMINED,
  "Four lines are added to the source-tree listing for `keycollectionprobe.h/.cpp`, files this "
  "commit itself creates. The commit's account names the act — \"Doc-sync in the same commit (#10) "
  "… ARCHITECTURE.md lists the new TU\". So a fact in the code is the source, and the code is this "
  "commit's own; nothing standing is withdrawn and no user act is cited. NOT CLEARED.",
  "same-commit-code-documentation")

v("153d45e78c5162c17844c7a488f9e9901b524141", "docs/scoring_model.md", "-262,0 +263,23", UNDETERMINED,
  "A new §4 block is added describing the membership predicate's COMMITTED FORM — the "
  "mode-transposed set, the 19-of-21 equality, the two modes it is wrong for — and stating in terms "
  "that \"both terms score against the wrong collection\". The behaviour described is pre-existing: "
  "the commit's own account says the unified predicate's \"committed branch is the same test as "
  "before\". So the source is a reading of implementation code this commit did not write. It is an "
  "ADDITION — nothing standing is withdrawn, and the discrepancy is NAMED as a defect rather than "
  "removed — so it is not a correction; it is also not cleared. This is the largest instance of the "
  "shape in the whole screened population and it is reported as one.",
  "describes-pre-existing-implementation-behaviour",
  remark="Ruling 4 of the eighteenth stop is what keeps this in view: an addition can make a correct "
       "specification wrong without removing a word. Whether a specification that states what the "
       "code does — even while calling it a defect — pre-empts the comparison a later audit would "
       "have made is not establishable from the text, which is why the verdict is NOT CLEARED "
       "rather than either clear class.")

v("153d45e78c5162c17844c7a488f9e9901b524141", "docs/scoring_model.md", "-556 +579", CODE_INFLUENCED,
  "A STANDING table entry is REPLACED. It read \"Awarded when root is a scale member of the current "
  "key.\"; it now reads that the bonus is awarded on membership in the current key's collection, "
  "names the code-level predicate the term shares with its sibling, and carries \"including its "
  "OI-168 defect on `Altered` / `AlteredDomBB7`\". The source of the replacement is a reading of "
  "implementation code THIS COMMIT DID NOT WRITE — the commit's own account states the doc-sync "
  "\"documents the shared predicate and the defect\", and states that the predicate's committed "
  "branch is the same test as before. That is a standing documentation statement altered against "
  "the implementation, which is this class.",
  "describes-pre-existing-implementation-behaviour",
  remark="THE COUNTER-CONSIDERATION, recorded because the user's act rests on this hunk: the "
       "replacement does not ERASE the discrepancy — it names the defect, points at the §4 block "
       "that measures it, and the same commit builds a default-OFF measurement of it. The "
       "substance of the first clause may also be unchanged, since \"scale member of the current "
       "key\" and \"member of the current key's collection\" are arguably the same claim in "
       "different words. What fires the class is the test as the dispatch states it — the change, "
       "and its commit's own account, show a documentation statement altered against the "
       "implementation — not a judgment that evidence was destroyed here.")

# --- 2026-07-14 · the OI-168 fix ------------------------------------------------------------------
for hdr in ("-186 +186", "-190,8 +190,32", "-244 +268,4"):
    v("10235d5547865c899fb088423fcf3a151fa9520e", "CLAUDE.md", hdr, RATIFIED,
      "Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "
      "\"The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork "
      "2026-07-13, user-ratified)\", and the added text carries \"dispatch user-ratified "
      "2026-07-13\". The superseded reference is preserved with its snapshot directory named (#12).",
      "measured-value-re-stamp",
      act="the OI-168 signature-mask correctness fix and its re-baseline",
      ratification_at="the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose "
                      "OI-168 re-baseline block records the same ratification")

for hdr in ("-263,22 +263,34", "-579 +591"):
    v("10235d5547865c899fb088423fcf3a151fa9520e", "docs/scoring_model.md", hdr, RATIFIED,
      "The §4 block and the table entry are rewritten to describe the behaviour THIS COMMIT "
      "INTRODUCES — the two terms now test the key signature's own collection — and the form they "
      "replaced is kept beside them as \"the defect it replaced\". The commit's account names the "
      "act and its ratification, and names the standing rule that requires the documentation to "
      "move in the same commit. Documentation and implementation moved together under one ratified "
      "act, so no standing statement was aligned to unchanged behaviour.",
      "same-commit-code-documentation",
      act="the OI-168 signature-mask correctness fix",
      ratification_at="the commit's own account (\"cc_instruction_oi168_fix.md, Cowork 2026-07-13, "
                      "user-ratified\"); and gate block (A) at CLAUDE.md at HEAD")

# --- 2026-07-16 · the OI-170 measurement build ----------------------------------------------------
v("b3d6c0f03a18a72d87341ad89220a81e090039ba", "docs/scoring_model.md", "-297,0 +298,25", UNDETERMINED,
  "A block is added recording what a default-OFF A/B measured at three PRE-EXISTING sites — that "
  "zero committed chords move, that one published flag moves on nine files, and what a future fix "
  "may and may not do. The source is a measurement of implementation code this commit did not "
  "write. Nothing standing is withdrawn and no user act is cited. NOT CLEARED.",
  "describes-pre-existing-implementation-behaviour")

# --- 2026-07-17/18 · the joint-estimator governing decision and principles #20–#24 -----------------
v("06d4318bd1f322d055d04622681587c44a01bffb", "ARCHITECTURE.md", "-2,0 +3,8", RATIFIED,
  "The governing-decision banner is added, its own first words \"★★ GOVERNING DECISION "
  "(user-ratified 2026-07-17): the key/mode/chord estimator is JOINT\". The commit's account lists "
  "it among the 2026-07-17 joint-architecture decision documents.",
  "governing-decision-record",
  act="the joint key/mode/chord estimator as the target architecture",
  ratification_at="the added banner itself, which is still at the top of ARCHITECTURE.md at HEAD")

v("06d4318bd1f322d055d04622681587c44a01bffb", "CLAUDE.md", "-56,0 +57,27", RATIFIED,
  "Principles #20–#24 and the constrained-optimum ledger corollary are added. The commit's account "
  "names them \"(user-ratified 2026-07-18)\".",
  "governing-decision-record",
  act="principles #20–#24 and the constrained-optimum ledger corollary",
  ratification_at="CLAUDE.md's #17–#24 provenance paragraph, which records the 2026-07-18 "
                  "ratification at the joint-estimator plan review and stands at HEAD")

v("06d4318bd1f322d055d04622681587c44a01bffb", "CLAUDE.md", "-82 +109,4", RATIFIED,
  "The provenance paragraph is extended to record who ratified #20–#24 and when. It is the "
  "citation half of the same act.",
  "governing-decision-record",
  act="principles #20–#24 and the constrained-optimum ledger corollary",
  ratification_at="the extended provenance paragraph itself, at CLAUDE.md at HEAD")

# --- 2026-07-18 · the STATUS/handoff doc split ----------------------------------------------------
for hdr, what in (("-168 +168,2", "the session-start read's description of the now-lean STATUS.md"),
                  ("-170 +171,3", "the pointer to the two reference-only archives")):
    v("51d4f6dcf34121a2598750c41b808c2f895ae674", "CLAUDE.md", hdr, RESTRUCTURING,
      f"The doc-split commit updates {what}. Its account is \"Pure documentation hygiene per the "
      "dispatch … the history moves verbatim to reference-only archives. No code, no build, no "
      "golden, no corpus, no register change\", and it reports a byte-level reconciliation of the "
      "partition. No fact from the implementation is its source.",
      "document-relocation-or-re-heading")

# --- 2026-07-19 · the research library ------------------------------------------------------------
v("4f2c5ddfdb0ecd2e4363982b0dc722dd9e7e52e0", "docs/research_papers/BIBLIOGRAPHY.md", "-0,0 +1,99",
  RESTRUCTURING,
  "A new document: one row per published source, with its link, whether a local copy exists and its "
  "redistribution tier. Its subject is the published literature and this fork's handling of it; no "
  "fact from the implementation is its source.",
  "new-document-content")

v("4f2c5ddfdb0ecd2e4363982b0dc722dd9e7e52e0", "docs/research_papers/README.md", "-0,0 +1,27",
  RESTRUCTURING,
  "A new document indexing the locally held copies and what each settled in the theory grounding, "
  "plus the statement that the binaries live only in a private repository. Its subject is the "
  "literature and file handling; no fact from the implementation is its source.",
  "new-document-content")

# --- 2026-07-25 · the L1 fact-surface extension ---------------------------------------------------
v("1e35415ee06b77e001aeea3b947369a2016573b3", "ARCHITECTURE.md", "-768 +768", UNDETERMINED,
  "The standing note-model row is extended to describe the additive `notatedNotes()` surface this "
  "commit itself adds. The commit's account names the act — \"ARCHITECTURE.md L1 note-model row "
  "synced (#10 / OI-146)\". A sanction is named (OI-180) but no user act and no place of "
  "ratification is citable from the change or its account, so the RATIFIED-ACT class is not "
  "admitted (assumption A3). Nothing standing is withdrawn. NOT CLEARED.",
  "same-commit-code-documentation")

# --- 2026-07-26 · the OI-178 adoption -------------------------------------------------------------
v("205dd0843aff3e41e3da3ff7e8e6e4147b320d74", "ARCHITECTURE.md", "-10,0 +11,25", RATIFIED,
  "The as-built banner for the adoption is added, its own first words \"★★ AS-BUILT (the OI-178 "
  "adoption, user-ratified 2026-07-26, option 1 — STAGED SCOPE)\". The commit's subject and account "
  "carry the same.",
  "governing-decision-record",
  act="the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)",
  ratification_at="the added banner; and gate block (A) at CLAUDE.md at HEAD, which records the "
                  "adoption as user-ratified 2026-07-26 with its measurement provenance")

for hdr in ("-219 +219,3", "-228,7 +230,28", "-300,8 +323,13"):
    v("205dd0843aff3e41e3da3ff7e8e6e4147b320d74", "CLAUDE.md", hdr, RATIFIED,
      "Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence "
      "statement, the staged-scope declaration, and the superseded columns preserved with their "
      "snapshot named (#12). The commit subject and the added text both carry \"user-ratified "
      "2026-07-26, option 1\".",
      "measured-value-re-stamp",
      act="the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)",
      ratification_at="the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified "
                      "baselines still record this adoption and its measurement provenance")

# --- 2026-07-26 · the decision-neutrality corollary ------------------------------------------------
v("00c0df81c5682fbda0515a81cea0c3c541e8ee23", "CLAUDE.md", "-105,0 +106,14", RATIFIED,
  "The decision-neutrality corollary is added, its own opening \"(corollary to #4/#6/#19; "
  "user-ratified 2026-07-26)\". The commit's subject is a ratification record.",
  "governing-decision-record",
  act="the decision-neutrality corollary",
  ratification_at="the added text, and the same corollary at CLAUDE.md at HEAD, whose provenance "
                  "names the notation-layer adoption increment's decision surface")

v("00c0df81c5682fbda0515a81cea0c3c541e8ee23", "CLAUDE.md", "-112 +126,3", RATIFIED,
  "The provenance paragraph is extended to record the corollary's ratification and where its "
  "analysis lives. It is the citation half of the same act.",
  "governing-decision-record",
  act="the decision-neutrality corollary",
  ratification_at="the extended provenance paragraph itself, at CLAUDE.md at HEAD")

# --- 2026-07-26 · Decision D1, the embedded tables ------------------------------------------------
for hdr in ("-18,3 +18,14", "-24 +35,2"):
    v("83fbb9e66156d2c0fc4ad6b2f98cad4ed46e4146", "ARCHITECTURE.md", hdr, RATIFIED,
      "The as-built banner is amended to record the embedded table/weight delivery THIS COMMIT "
      "introduces, and the changed sentences describe the new delivery rather than the old one. The "
      "commit's subject is \"Decision D1 EXECUTED\" and its account cites \"ratified Decision D1, "
      "cowork_notation_adoption_increment.md §5\".",
      "same-commit-code-documentation",
      act="ratified Decision D1 — the fitted tables and the selected weight vector embedded as "
          "provenance-stamped generated source",
      ratification_at="`cowork_notation_adoption_increment.md` §5, the decision surface CLAUDE.md's "
                      "decision-neutrality corollary records as user-ratified 2026-07-26")

# --- 2026-07-26/27 · the seams units, documented as built -----------------------------------------
v("56439ebad7f5010013cec41eab834d39189f52f6", "ARCHITECTURE.md", "-44,0 +45,22", UNDETERMINED,
  "An as-built block is added for the posterior slice this commit itself implements, with its "
  "establishment and its parity result. The commit's account names the act — \"Doc sync (#10): "
  "ARCHITECTURE.md joint-estimator as-built\". A contract section and a dispatch are cited; no user "
  "act is, so the RATIFIED-ACT class is not admitted (assumption A3). NOT CLEARED.",
  "same-commit-code-documentation")

v("e336bd034837cfc4e81cf1c5bb4b00d611c283b4", "ARCHITECTURE.md", "-66,0 +67,27", UNDETERMINED,
  "An as-built block is added for the notation record §3.1–§3.6 delivered across this commit and "
  "its predecessors, with its establishment. The commit's account names a ratified decision (C1) "
  "for ONE PORTION of what the block describes — the modal reading — and no user act for the "
  "remainder, so "
  "the RATIFIED-ACT class is not admitted for the hunk as a whole (assumption A3). NOT CLEARED.",
  "same-commit-code-documentation")

v("6e71b3ceff61dcdf9c79cfb722111fa95e79e0c8", "ARCHITECTURE.md", "-90,3 +90,8", UNDETERMINED,
  "A standing establishment sentence is extended with the C++/Python spelling parity this commit's "
  "own Task 1 established on 13,063 committed segments, and the consumer clause is re-pointed at "
  "the producer this commit adds. Nothing standing is withdrawn — a measured establishment is "
  "inserted — but the source is a measurement of the implementation. NOT CLEARED.",
  "describes-pre-existing-implementation-behaviour")

v("6e71b3ceff61dcdf9c79cfb722111fa95e79e0c8", "ARCHITECTURE.md", "-93,0 +99,22", UNDETERMINED,
  "An as-built block is added for the record producer and the two seam views this commit "
  "implements. The commit's account names the act — \"Doc sync (#10)\". No user act is cited. "
  "NOT CLEARED.",
  "same-commit-code-documentation")

# --- 2026-07-27 · the open-items register split ---------------------------------------------------
for hdr in ("-133 +133", "-135,6 +135,12", "-142,2 +148,3"):
    v("1e32b5e92e2594d3a8d1752fcea051dab16f60a7", "CLAUDE.md", hdr, RATIFIED,
      "The open-items register section is rewritten for the index-plus-detail split, and the "
      "changed text carries \"split into index + detail files, user-ratified 2026-07-26\" and "
      "\"user-ratified option 1\". The commit subject carries the same. The rules (a)–(e) are "
      "re-worded for the split; no fact from the implementation is the source.",
      "governing-decision-record",
      act="the open-items register's split into a lean index plus one detail file per item",
      ratification_at="the changed text itself, and the same section at CLAUDE.md at HEAD")

v("b2c71fb6e3b29d1ae1b7595a6875199389604b75", "ARCHITECTURE.md", "-123,0 +124,22", UNDETERMINED,
  "An as-built block is added for the notation consumer re-plumb and the permanently guarded "
  "inference/presentation boundary this commit implements. Ratified rules are cited inside it "
  "(Decision D2, the contract amendment) but no user act is named for this change, so the "
  "RATIFIED-ACT class is not admitted (assumption A3). NOT CLEARED.",
  "same-commit-code-documentation")

v("599eebd45eb5a050e1901ef9111a7b5890716817", "ARCHITECTURE.md", "-145,0 +146,25", UNDETERMINED,
  "An as-built block is added for the implode and tuning span-seam consumers and the exposure-bucket "
  "unification this commit implements, including the two constants' declared sites. The commit's "
  "account names the act — \"ARCHITECTURE.md gains the implode/tuning record-path + exposure-bucket "
  "as-built block\". No user act is cited. NOT CLEARED.",
  "same-commit-code-documentation")

v("903125a5dc79b9ac80865f82b79fa15cd604bdc5", "ARCHITECTURE.md", "-170,0 +171,27", UNDETERMINED,
  "An as-built block is added for the note-seam re-plumb this commit implements, down to which "
  "fields the record-arm builder fills and which it leaves at defaults. The commit's account names "
  "the act — \"Doc sync (#10)\". No user act is cited. NOT CLEARED.",
  "same-commit-code-documentation")

v("89412b48b27e2cfe70254e5a2199d6c3c681958c", "ARCHITECTURE.md", "-107 +107,7", UNDETERMINED,
  "A standing sentence about the producer is extended with the OI-204 input-scoping parameter and "
  "what it does at the fact adapter. Nothing standing is withdrawn; the source is the implementation. "
  "The commit's account names the act — \"Doc sync: ARCHITECTURE.md (the OI-204 input-scoping "
  "parameter + the dual-arm instrument as-built)\". NOT CLEARED.",
  "same-commit-code-documentation")

v("89412b48b27e2cfe70254e5a2199d6c3c681958c", "ARCHITECTURE.md", "-197,0 +204,21", UNDETERMINED,
  "An as-built block is added for the dual-arm classified-comparison tool this commit delivers, "
  "with the classes it assigns and what it measured. No user act is cited. NOT CLEARED.",
  "same-commit-code-documentation")

# --- 2026-07-27 · the P7 consolidation ------------------------------------------------------------
_P7 = ("4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17", "ARCHITECTURE.md")
for hdr, what in (
    ("-100,2 +100,11", "the consolidated section header replaces the first per-unit heading, and the "
                       "framing text restates the dual-arm posture the five blocks already carried"),
    ("-121,2 +130,3", "a consumer sentence is re-pointed from a later dispatch to the subsections "
                      "below it"),
    ("-130,3 +140,2", "a per-unit heading becomes numbered subsection (2)"),
    ("-152,2 +161,2", "a per-unit heading becomes numbered subsection (3)"),
    ("-177,2 +186,2", "a per-unit heading becomes numbered subsection (4)"),
    ("-199,4 +208", "a forward-looking sentence about what remains before the switch is trimmed to "
                    "one line, its substance carried into the new subsection (6)"),
    ("-204,2 +210,2", "a per-unit heading becomes numbered subsection (5)"),
):
    v(*_P7, hdr, RESTRUCTURING,
      f"One step of the P7 consolidation: {what}. The commit's account states the act and its own "
      "no-loss claim — \"the five accumulated per-unit record-path blocks consolidated into ONE "
      "coherent as-built section (nothing historical removed)\". No fact newly read in the "
      "implementation is the source of the change.",
      "document-relocation-or-re-heading")

v(*_P7, "-223,0 +230,13", UNDETERMINED,
  "A new subsection (6) is added stating the dual path's current state — the flag OFF everywhere, "
  "the partition closed out and completeness-verified, the three suites green — and what the switch "
  "would do. The state it reports is read off a verification of the code performed in the same "
  "commit. Nothing standing is withdrawn. NOT CLEARED.",
  "describes-pre-existing-implementation-behaviour")

# --- 2026-07-27 · the notation switch -------------------------------------------------------------
for path, hdr in (("ARCHITECTURE.md", "-100,8 +100,9"),
                  ("ARCHITECTURE.md", "-231,12 +232,18"),
                  ("CLAUDE.md", "-269,4 +269,16")):
    v("2a81af273ee9b9339736f6e03b0fc96b55bc5005", path, hdr, RATIFIED,
      "The dormant-posture text is replaced by the switched posture: the record path is the "
      "production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. "
      "The commit's subject carries \"(user-ratified 2026-07-27)\" and every changed passage repeats "
      "it. The replaced statements were made false by the ratified act itself, not by a reading of "
      "the code.",
      "governing-decision-record",
      act="THE NOTATION SWITCH — the record path made the production in-app notation analysis",
      ratification_at="the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED "
                      "SCOPE block records the switch as user-ratified 2026-07-27")

# --- 2026-07-28 · the score inventory --------------------------------------------------------------
v("5135764ed7f8d7b992ed5f1c3b4c2fecab7f5d35", "docs/score_inventory.md", "-234 +234,18", UNDETERMINED,
  "A subfolder of large scores is added to the inventory with measured counts, the licence read "
  "from each file's own metadata, and a closing statement that the joint decoder returns an EMPTY "
  "analysis on 13 of the 23. That last clause is a measured fact about the implementation's "
  "behaviour. Nothing standing is withdrawn and no user act is cited. NOT CLEARED.",
  "describes-pre-existing-implementation-behaviour")

# --- 2026-07-28 · the never-work-from-memory and writing conventions --------------------------------
v("8c8e57eab9c031bb126f2521f378382e8fead1e6", "CLAUDE.md", "-720,0 +721,19", RATIFIED,
  "The never-work-from-memory convention is added, its own opening \"(user-directed, 2026-07-28; "
  "binds Cowork and CC equally)\". Its founding instance names a specification and the position it "
  "states; the rule itself is the user's.",
  "governing-decision-record",
  act="the never-work-from-memory convention",
  ratification_at="the added text, and the same convention at CLAUDE.md at HEAD")

v("8c8e57eab9c031bb126f2521f378382e8fead1e6", "CLAUDE.md", "-724,0 +744,51", RATIFIED,
  "The writing-standards pointer and the music-theory reserved-word convention with its "
  "disambiguation rule are added, each carrying \"(user-directed, 2026-07-28)\" or an earlier dated "
  "user attribution. No fact from the implementation is the source.",
  "governing-decision-record",
  act="the writing-standards pointer and the music-theory reserved-word / disambiguation convention",
  ratification_at="the added text, and both conventions at CLAUDE.md at HEAD")

# --- 2026-08-01 · the defense-at-its-home convention -----------------------------------------------
v("80ad92f9d3dae1d0d51a696e402734215529ac24", "CLAUDE.md", "-795,0 +796,14", RATIFIED,
  "The every-design-decision-carries-its-defense convention is added, its own opening "
  "\"(user-directed, 2026-08-01, at the decisions-register ratification review)\". The commit's "
  "account records it as a riding Cowork edit of that date.",
  "governing-decision-record",
  act="the convention that every design decision carries its defense at its home",
  ratification_at="the added text, and the same convention at CLAUDE.md at HEAD")

# --- 2026-08-01 · the decisions register ratified and made the living surface ----------------------
v("a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4", "ARCHITECTURE.md", "-721,0 +722,12", RATIFIED,
  "A scoping annotation is added, its own opening \"★ Scoping annotation (user ruling, 2026-08-02, "
  "at the OI-234 decision-conflict adjudication — reading 3)\". It scopes a standing finding to "
  "what it tested and states what it does not bear on; the ground given is the adjudication, not a "
  "reading of the code.",
  "governing-decision-record",
  act="the OI-234 decision-conflict adjudication, reading 3",
  ratification_at="the added annotation itself, at ARCHITECTURE.md at HEAD")

v("a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4", "ARCHITECTURE.md", "-956,0 +969,27", RATIFIED,
  "The MuseScore-Dependency Rule is added, its own heading carrying \"(user-ratified 2026-08-02, at "
  "the OI-241 adjudication)\", and its closing paragraph states the derivation from the "
  "already-ratified scoped forms.",
  "governing-decision-record",
  act="the MuseScore-Dependency Rule",
  ratification_at="the added section heading itself, at ARCHITECTURE.md at HEAD")

for hdr, what in (("-151,0 +152,15", "the decisions-register section with its rules (a)–(e)"),
                  ("-189 +204", "the session-start read count, two files becoming three"),
                  ("-192,0 +208,2", "the decisions-register INDEX added to the session-start reads")):
    v("a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4", "CLAUDE.md", hdr, RATIFIED,
      f"The change adds {what}. The section's own heading carries \"(shape user-ratified "
      "2026-07-28; content + living surface 2026-08-02)\", and the commit's account records the "
      "decisions register's 228 entries as user-ratified and the living surface as landing in "
      "this commit.",
      "governing-decision-record",
      act="the decisions register ratified and made the living surface (its session-start read)",
      ratification_at="the section heading itself at CLAUDE.md at HEAD, and the ratification "
                      "recorded in the decisions register's INDEX preamble")

# --- 2026-08-02 · D-231 itself, the commit the period opens at ------------------------------------
v("b006dc15b5f696f2fc86ad72b97fae58d2119cd7", "CLAUDE.md", "-826,0 +827,19", RATIFIED,
  "The three-phase sequencing rule is added, its own opening \"(user-directed, 2026-08-02; sharpens "
  "#8 …)\". This is the boundary commit itself — the act the ruled period opens exclusive at — and "
  "the hunk that writes the instruction whose truth half the eighteenth stop's diagnosis names.",
  "governing-decision-record",
  act="D-231, the three-phase sequencing rule (specification completion, issue-exhaustion, one fix plan)",
  ratification_at="the added text, and the same rule at CLAUDE.md Conventions at HEAD")


# ══ END OF THE EXISTING AUTHORED BLOCK — every verdict above is one of the original sixty-eight and
#    is neither re-read nor re-graded by the widening.  Its digest is published in the artifact at
#    `the_existing_verdicts_digest`, which is what makes "byte-unchanged" a measurement rather than a
#    claim. ═════════════════════════════════════════════════════════════════════════════════════════


# ── AUTHORED — the verdict per NEW widened hunk ──────────────────────────────────────────────────
#
# Keyed by (commit, file, hunk header), the identity the widened population publishes.  Every entry
# is made by reading that hunk's own removed and added text at the git object, together with the
# commit's own account, and nothing else — the inherited method, applied to a wider population.
#
# The four classes are applied in the DECLARED ORDER: POSITIVELY CODE-INFLUENCED first, so that a
# ratified act cannot launder a correction made under it.
W: dict[tuple[str, str, str], dict] = {}


def w(commit, path, header, verdict, ground, shape=None, act=None, ratification_at=None,
      remark=None):
    W[(commit, path, header)] = {"verdict": verdict, "ground": ground, "shape": shape,
                                 "act": act, "ratification_at": ratification_at, "remark": remark}


# ★ ONE NOTE ON THE SHAPE VOCABULARY, RECORDED ONCE HERE RATHER THAN AT EVERY VERDICT.  The six
# shapes are the original screen's and are inherited unchanged.  The gloss of
# `describes-pre-existing-implementation-behaviour` ends "Nothing standing is withdrawn — in the
# instances here the behaviour is named as a DEFECT" — a description of the instances the ORIGINAL
# screen met, not a condition of the shape: that screen's own single POSITIVELY CODE-INFLUENCED
# verdict carries this shape.  In the widened population the dominant kind is a documentation
# statement CORRECTED against the implementation, which withdraws something standing.  It is
# reported under this same shape, because inventing a seventh would amend a method Ruling 7 fixes as
# untouched, and the withdrawal is stated in each verdict's own ground.

# ── 2026-08-02 · the phase-1 HOMING acts (D-231's first half) ─────────────────────────────────────
_HOMING = "f833a2d2a9f4fd389da913fb17b9ff3b558012ec"
_HOMING_GROUND = (
    "The commit's own account is \"phase 1 Task 1 — the homing acts (20 decisions written into "
    "their owning specifications)\", and it states what it is: every register entry whose home was "
    "a documentation gap or a tracking surface is written into the specification that owns it, "
    "\"in that specification's own voice, with its defense and its ratifying date\". The hunk adds "
    "text that carries its own ratification date. No fact about the implementation is the source "
    "of the addition, and nothing the documentation already stated is withdrawn or narrowed by it.")

w(_HOMING, "ARCHITECTURE.md", "-250,0 +251,45", RATIFIED,
  _HOMING_GROUND + " Here the added block is the joint estimator's standing rules, and each rule "
  "carries its own ratifying date inside the added text — \"Ratified by the user 2026-07-17\", "
  "\"Protocols ratified 2026-07-19\", the OI-178 adoption \"user-ratified 2026-07-26\". The block "
  "also NAMES an unresolved tension (the key axis against §5.7a) and leaves it unsettled, which is "
  "a homing act recording a decision rather than taking one.",
  "governing-decision-record",
  act="the D-231 phase-1 homing of the joint estimator's four standing rules into their owning "
      "specification",
  ratification_at="each rule's own ratifying date inside the added text; and D-231 itself at "
                  "`CLAUDE.md` Conventions at HEAD")

w(_HOMING, "ARCHITECTURE.md", "-843,0 +889,60", RATIFIED,
  _HOMING_GROUND + " Here the added text is §2.15's three cross-cutting contracts and the new "
  "§2.16, and every one carries its own attribution — \"Ratified by the user 2026-07-02\", "
  "\"ratified by the user 2026-07-06\", \"Ratified by the user 2026-07-10 and amended 2026-07-12\", "
  "and \"Two requirements the user stated on 2026-07-28\".",
  "governing-decision-record",
  act="the D-231 phase-1 homing of the cross-layer confidence contract, the negative-evidence rule, "
      "the fact-publication corollary and the two standing design requirements",
  ratification_at="each contract's own attribution inside the added text; and the same rules at "
                  "`CLAUDE.md` at HEAD")

w(_HOMING, "ARCHITECTURE.md", "-3654 +3759,6", RATIFIED,
  _HOMING_GROUND + " Here the hunk QUALIFIES §5.12's Status line by recording that the two-pass "
  "pedal detector is superseded as a DESIGN by the voice-independent class, \"user-ratified "
  "2026-07-26\". ★ The first class was tested and does not fire: the qualification's ground — that "
  "the two-pass detector can only see the lowest voice — is stated by §5.12's own text, which "
  "specifies the detector on the lowest-pitched tone, so it is available from the documentation "
  "and is not a fact read in implementation code this commit did not write.",
  "governing-decision-record",
  act="the voice-independent pedal-point ruling of the notation-adoption increment",
  ratification_at="the added text's own \"user-ratified 2026-07-26\"; and §7.4 at HEAD, which "
                  "states the ratifying surface as `cowork_notation_adoption_increment.md` §7 + §10")

w(_HOMING, "ARCHITECTURE.md", "-4230,0 +4341,13", RATIFIED,
  _HOMING_GROUND + " Here the added block is §7.4's voice-independent pedal-point class (D-207), "
  "\"user-ratified 2026-07-26\". ★ The first class was tested and does not fire, and the call is "
  "recorded because it is close: the added text DOES cite implementation code this commit did not "
  "write (`chordpostpasses.cpp:275`) and DOES supersede a standing pair of published facts. What "
  "decides it is that the code citation is offered as the DESIGN reason the legacy mechanism is "
  "inadequate, not as a fact against which a documentation statement was found false — the "
  "supersession's source is the user's ratification, which the text names.",
  "governing-decision-record",
  act="the voice-independent pedal-point class of the ornament vocabulary (D-207)",
  ratification_at="the added text's own \"user-ratified 2026-07-26\" and its naming of the "
                  "ratifying surface `cowork_notation_adoption_increment.md` §7 + §10")

w(_HOMING, "ARCHITECTURE.md", "-4655,0 +4779,11", RATIFIED,
  _HOMING_GROUND + " Here the added block is §11's HELD status and the declaration that intonation "
  "is a named future CONSUMER of the analysis, \"user-decided 2026-07-13\", quoting the user's own "
  "stated dependency.",
  "governing-decision-record",
  act="the user's decision of 2026-07-13 that intonation is held and is a declared future consumer "
      "of the analysis (D-206)",
  ratification_at="the added text's own \"user-decided 2026-07-13\"; the row it names, "
                  "`OPEN_ITEMS.md` OI-62")

w(_HOMING, "ARCHITECTURE.md", "-6239,0 +6374,11", RATIFIED,
  _HOMING_GROUND + " Here the added block is §16's rule that a HUMAN acts as ground truth where "
  "none is published, \"user-decided 2026-07-13\", with the language-model judge admitted as "
  "triage and explicitly never as a grader.",
  "governing-decision-record",
  act="the user's decision of 2026-07-13 that a human is ground truth where none is published "
      "(D-205)",
  ratification_at="the added text's own \"user-decided 2026-07-13\"; the rows it names, "
                  "`OPEN_ITEMS.md` OI-38 and OI-56")

# ── 2026-08-02 · the phase-1 TRUTH-SYNC (D-231's second half) ─────────────────────────────────────
# ★ THIS COMMIT IS THE ONE THE FIRST CLASS IS WRITTEN FOR, AND ITS OWN ACCOUNT SAYS SO.  The class's
# second limb admits a hunk where "the change's own account states that a documentation statement
# was corrected against the implementation".  This commit's account states exactly that, in terms:
# "a specification cannot be the compliance standard while it misdescribes the code, so every
# statement the named open-items rows establish as false at HEAD is corrected".  Each hunk below is
# nonetheless graded on ITS OWN text, and three of the thirty-nine do NOT fire the first class.
_SYNC = "ab336f43b5e5610077488117a8a3a1ea32cec440"
_SYNC_ACCOUNT = (
    "The commit's own account is \"phase 1 Task 2 — the truth-sync (every named false "
    "specification statement corrected at HEAD)\", and it states the correction's direction in "
    "terms: \"a specification cannot be the compliance standard while it misdescribes the code, so "
    "every statement the named open-items rows establish as false at HEAD is corrected\". That is "
    "the first class's second limb, word for word.")


def _sync(header, subject, cites, extra=""):
    w(_SYNC, "ARCHITECTURE.md", header, CODE_INFLUENCED,
      _SYNC_ACCOUNT + f" This hunk {subject} The correction's own text cites {cites}, which this "
      "commit did not write." + (" " + extra if extra else ""),
      "describes-pre-existing-implementation-behaviour")


_sync("-39,4 +39,9",
      "REPLACES the STAGED-SCOPE clause, which said the in-app notation layer stays on the legacy "
      "pipeline, with the statement that the switch closed the migration on both surfaces; its own "
      "parenthesis says the replaced sentence \"the switch made false\".",
      "the flag default at `composingconfiguration.cpp:178`")
_sync("-138,2 +143,4",
      "REPLACES the layer-sections scope note, which had the two surfaces the wrong way round; its "
      "own parenthesis says the replaced sentence said \"the legacy pipeline was still live on the "
      "notation path\".",
      "the notation switch and the resulting dormant-compiled state of both surfaces")
_sync("-1236 +1257,13",
      "REPLACES Layer 3's build-state tag `Built+Live` with `Built+Dormant` and adds the "
      "verification; its own heading is \"Build-state correction\" and it says the tag \"the two "
      "adoptions made false\".",
      "all four production call sites — `notationcomposingbridge.cpp:324-328` and `:1509-1513`, "
      "`notationimplodebridge.cpp:1434-1441`, `notationtuningbridge.cpp:794` — and the flag default "
      "at `composingconfiguration.cpp:178`")
_sync("-1290 +1323,10",
      "REPLACES Layer 4's heading clause \"engages with L5\", which \"no longer describes anything "
      "scheduled\", and records that the plan was overtaken without any ruling naming it.",
      "the state of the production inference layer on both surfaces since the two adoptions",
      "The source is what the implementation became, established at the adoptions rather than at a "
      "ruling — the hunk's own words are \"a supersession in fact, not by decision\".")
_sync("-1362,4 +1404,8",
      "REPLACES the voice-leading layer's description \"not built\"; its own parenthesis says the "
      "entry \"said 'not built', contradicting §2.15 in the same document\".",
      "the built-and-dormant state of the axis-2 foundation (VL-A/VL-B/VL-C)")
for _h, _what in (
        ("-1622,0 +1669,3", "ADDS the note recording that the documented bit order was wrong"),
        ("-1628,2 +1677,2", "SWAPS the documented bits 4 and 5 of the Extension mask"),
        ("-1633,2 +1682,2", "SWAPS the documented bits 9 and 10 of the Extension mask"),
        ("-1638,2 +1687,2", "SWAPS the documented bits 14 and 15 of the Extension mask")):
    _sync(_h, _what + ", correcting the listing against the header it claims to reproduce.",
          "`chordanalyzer.h:213-230`",
          "The added note states the consequence itself: \"a reader deriving a mask from this "
          "listing would be wrong\".")
_sync("-1641,0 +1691,2",
      "ADDS the note recording that four fields were missing from the documented field list.",
      "the `ChordIdentity` definition the listing claims to reproduce")
for _h, _what in (
        ("-1647,0 +1699", "`naturalFifthPresent`"),
        ("-1648,0 +1701", "`tiePriority`"),
        ("-1649,0 +1703,3", "`isPedalPoint` and `pedalBassPc`")):
    _sync(_h, f"ADDS {_what} to the documented field list, re-syncing it with the struct.",
          "the `ChordIdentity` definition in the code")
_sync("-1643 +1694",
      "REPLACES the documented meaning of `score` — \"Raw confidence. Higher is better. Not "
      "normalized.\" becomes \"Raw template-match score. Higher is better. Ranking only.\"",
      "what the field actually is in the scorer",
      "A documented statement about what a published value MEANS, corrected against the code that "
      "produces it.")
_sync("-1685 +1741,4",
      "REPLACES the documented default of `bassNoteRootBonus`, 0.65 with 0.70.",
      "the code default at `analysis/types/analysistypes.h:196`")
_sync("-1718 +1777",
      "REPLACES the gates' documented home and drops Gate K from the list of live calibrated "
      "thresholds.",
      "`postscoringgates.cpp`, where the two surviving margin constants are declared")
_sync("-1726,0 +1786,9",
      "ADDS the two corrections in full — the gates' home, and Gate K's retirement, which made "
      "listing it \"as a live calibrated threshold false\".",
      "`postscoringgates.cpp:46`, `:47`, `:49` and `:523`",
      "It also records that the same retired threshold is still listed in `CLAUDE.md` and that "
      "correcting a governing document was outside the pass's scope — an owed correction named "
      "rather than taken.")
_sync("-1769 +1837,2",
      "REPLACES §4.1b's restatement of the same constant, 0.65 with 0.70.",
      "the same code default, cited as OI-107(a)")
_sync("-1787,4 +1856,20",
      "MARKS §4.1b's safety constraint superseded and states the constraint that actually survives, "
      "\"read off the code\", noting that it differs between the two predicates.",
      "`chordanalyzer.cpp:855-870` and `:829-853`",
      "Its closing sentence states the direction of the correction exactly: \"No code change is "
      "owed — the code is the later behaviour and is correct; what was owed was saying so here.\"")
_sync("-2239 +2324,7",
      "REPLACES the backlog item's status with PARTLY DONE and states which half was done.",
      "`analysis/chord/chordsymbolformatter.cpp` and the absence of a `chordsymbolformatter.h`")
_sync("-2818 +2909,6",
      "REPLACES §4.3's single \"File:\" line, which \"predated refactor-1\".",
      "the split between the declaring header and the implementing translation unit")
_sync("-2867,3 +2963,6",
      "REPLACES the Roman-numeral scope paragraph, which said extensions beyond the 7th are \"not "
      "yet emitted\".",
      "`chordsymbolformatter.cpp:590-616`")
for _h, _what in (
        ("-3032 +3131,3", "REPLACES AnalysisUtils' documented path, which omitted the `chord/` "
                          "component"),
        ("-3034 +3135,2", "REPLACES the one-line description of what the leaf is"),
        ("-3039,0 +3142,5", "ADDS the three functions the listing was missing")):
    _sync(_h, _what + ".", "the header as it stands at `analysis/chord/analysisutils.h`")
_sync("-3753,3 +3860,10",
      "REPLACES §5.11's assertion that the augmented-sixth labels are \"Gated to Standard and "
      "Baroque presets only\", which \"the code defers exactly\".",
      "`chordsymbolformatter.cpp:882-883`")
for _h, _what in (
        ("-3838,2 +3952,13", "REPLACES §5.13's claim that there is \"no path-selection flag\", "
                             "which was \"false at HEAD\""),
        ("-3842,0 +3968,3", "ADDS the sentence declaring what each row of the rebuilt table means "
                            "at HEAD"),
        ("-3845,7 +3973,27", "REPLACES the whole entry-point table, every row rebuilt against what "
                             "runs")):
    _sync(_h, _what + ".",
          "`notationcomposingbridge.cpp:728-738`, `:703`, `:621`, `:1385`, "
          "`notationimplodebridge.cpp:1409-1431`, `notationtuningbridge.cpp:794` and the flag "
          "default at `composingconfiguration.cpp:178`")
_sync("-4677,0 +4826,8",
      "ADDS the premise correction to §10.0, recording that its prerequisite and \"the whole "
      "premise above are false at HEAD\".",
      "the production annotation path, which \"never calls `greedyExpandSegmentation()`\"")
_sync("-5591,4 +5747,13",
      "REPLACES §11.5's status and its account of what the implode action runs.",
      "`notationimplodebridge.cpp:1409-1431` and `:1434-1441`, and the declared-versus-defined "
      "split at `notationcomposingbridge.h:161` / `notationharmonicrhythmbridge.cpp:69`")
_sync("-5998,3 +6163,22",
      "REPLACES §12.1a's two clauses — \"analysis cost is negligible (well under 1ms)\" and "
      "\"suppressing the display does not require skipping the analysis\" — both of which the "
      "correction states are \"false on the production path\".",
      "the note-seam funnel's whole-score decode and the measurement at "
      "`tools/joint_estimator/noteseam_latency.json`")
for _h, _what in (
        ("-6008,2 +6192,4", "REPLACES §12.1b's claim that two actions are registered"),
        ("-6016,3 +6202,22", "ADDS the seven further actions, each with its registration site, and "
                             "records the right-click chord anchor with \"derivation not "
                             "recorded\"")):
    _sync(_h, _what + ".",
          "`notationuiactions.cpp:1402`–`:1432`, `notationcontextmenumodel.cpp:174` and `:210-214`, "
          "and `notationactioncontroller.cpp:387`")

# ── the three hunks of the truth-sync commit where the FIRST CLASS DOES NOT FIRE ──────────────────
w(_SYNC, "ARCHITECTURE.md", "-819 +826,4", RATIFIED,
  _SYNC_ACCOUNT + " ★ BUT THIS HUNK IS NOT A CORRECTION AGAINST THE IMPLEMENTATION. It replaces "
  "the parenthetical \"ratification-gated\" with \"RATIFIED by the user 2026-07-02\" — a statement "
  "about a RULING, corrected against the ruling record, with no fact from the code in its source. "
  "The first class was applied first and does not fire; the second does, and the hunk records what "
  "a named user act ratified.",
  "governing-decision-record",
  act="the user's ratification of review amendment A-1, the cross-layer confidence and calibration "
      "contract, on 2026-07-02",
  ratification_at="`cowork_confidence_contract.md`'s own banner, \"Status: RATIFIED (user, "
                  "2026-07-02)\"; and the corrected parenthesis itself at `ARCHITECTURE.md` at HEAD")

w(_SYNC, "ARCHITECTURE.md", "-821 +831,2", RESTRUCTURING,
  _SYNC_ACCOUNT + " ★ BUT THIS HUNK CARRIES NONE OF THAT. It appends one sentence re-pointing the "
  "reader to where the contract's own rule and defense are stated, in the list below. No standing "
  "statement is withdrawn, no code fact is its source, and no user act is recorded — it is a "
  "pointer added inside the document.",
  "document-relocation-or-re-heading")

w(_SYNC, "ARCHITECTURE.md", "-823,2 +834,12", RESTRUCTURING,
  _SYNC_ACCOUNT + " ★ BUT THIS HUNK CORRECTS THE DOCUMENT'S ACCOUNT OF ITSELF, NOT OF THE CODE. It "
  "withdraws the claim that the span-typology rename was \"propagated through every layer spec\" "
  "and states what it actually covered — established by reading THIS document, which still uses "
  "the banned bare word in four headings the correction names. Its source is the document's own "
  "text; nothing from the implementation appears in it. The shape is reported as a re-heading "
  "because the subject of both the original claim and the correction is a renaming programme; it "
  "is the nearest of the six inherited shapes and no seventh is invented.",
  "document-relocation-or-re-heading")

w(_SYNC, "ARCHITECTURE.md", "-6307 +6512", RESTRUCTURING,
  _SYNC_ACCOUNT + " ★ BUT THIS HUNK IS A HEADING RE-MARK whose source is the project's own work "
  "history, not the code: `*(next)*` becomes `*(not started; NOT the next thing)*`. No fact read "
  "in implementation code is its source.",
  "document-relocation-or-re-heading")

w("19fbe9e2714f3f5d65db753e4d999e57e7f15649", "ARCHITECTURE.md", "-1333,0 +1334,11",
  CODE_INFLUENCED,
  "The commit's own account is \"phase 1d Task 0 — the two riding acts (OI-265 truth-sync, "
  "OI-266's six rules homed)\", and this hunk is the truth-sync half. It adds a scope note to "
  "Layer 4 which states in terms that the section \"carries one sentence about what runs — that "
  "production chord analysis still runs the legacy `analyzeChord` + post-scoring gates (§4.1) — "
  "which was true when written and is **false at HEAD**\". That is a documentation statement "
  "found false against the implementation, and the correction cites the flag default at "
  "`composingconfiguration.cpp:178`, which this commit did not write.",
  "describes-pre-existing-implementation-behaviour")

# ── 2026-08-02 · the phase-1i POINTER pass ────────────────────────────────────────────────────────
_PTR = "ebda0889f2f6c6076df4a0041008733b8d2296d8"
_PTR_GROUND = (
    "The commit's own account is \"phase 1i task 3 — the pointer pass (6 lines, pointer class "
    "only)\", and it states its own bound: \"Every ARCHITECTURE.md insertion is the ratified "
    "POINTER class — a one-line delegation pointer or a one-line tried-and-closed pointer. No "
    "content was copied and no ruling was made; the whole diff is 12 added lines and nothing "
    "else.\" The first class was applied first and does not fire: nothing standing is withdrawn "
    "and no fact from the implementation is the source. What the hunk records is the fifth home "
    "case, which the added line itself dates.")

for _h, _which in (
        ("-281,0 +282,2", "the delegation pointer to the fitting event's own design contract"),
        ("-293,0 +296,2", "the tried-and-closed pointer on the search"),
        ("-1270,0 +1275,4", "Layer 3's delegation pointer and its tried-and-closed line"),
        ("-1333,0 +1342,4", "Layer 4's delegation pointer and its tried-and-closed line")):
    w(_PTR, "ARCHITECTURE.md", _h, RATIFIED,
      _PTR_GROUND + f" Here the added line is {_which}.",
      "governing-decision-record",
      act="the fifth home case — a ratified contract document the owning `ARCHITECTURE.md` section "
          "points at is a proper home — and the pointer pass performed under it",
      ratification_at="the added line's own \"(the fifth home case, user-ratified 2026-08-02)\"; "
                      "and the same rule at `CLAUDE.md`'s decisions-register section, rule (g), at "
                      "HEAD")

# ── 2026-08-02 · the phase-1j HOMING half ─────────────────────────────────────────────────────────
_HOME_J = "88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27"
_HOME_J_GROUND = (
    "The commit's own account is \"phase 1j task 1 — the OI-272 HOMING half (16 rules written into "
    "their owning specifications)\". The hunk writes a rule the decisions register already held "
    "into the specification that owns it, in that specification's own voice and with its defense. "
    "The first class was applied first and does not fire: nothing the documentation already stated "
    "is withdrawn or narrowed, and no fact read in implementation code this commit did not write "
    "is the source of the addition.")


def _homej(header, what, extra=""):
    w(_HOME_J, "ARCHITECTURE.md", header, RATIFIED,
      _HOME_J_GROUND + f" Here the rule written in is {what}." + (" " + extra if extra else ""),
      "governing-decision-record",
      act="the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning "
          "specification",
      ratification_at="D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; "
                      "and, where the homed rule's own ratification is recorded, the date the "
                      "added text carries")


w(_HOME_J, "ARCHITECTURE.md", "-258,2 +258,3", RESTRUCTURING,
  _HOME_J_GROUND[:0] + "The commit is the phase-1j homing half, and this hunk is its heading "
  "half: the standing-rules heading is re-worded from \"Four rules\" to \"Six rules\" and its "
  "subject list extended, to keep the heading in step with the two rules the SAME commit adds "
  "below. Nothing outside the document is its source — not a fact read in implementation code, "
  "and not a ruling; the source is the commit's own addition. It is a re-heading.",
  "document-relocation-or-re-heading")
_homej("-305,0 +307,24",
       "rules (e) and (f) of the joint estimator's standing rules — the shipped-value licence pool "
       "and the per-idiom fit",
       "The added text carries its own dates: \"Ratified by the user 2026-07-04 … reaffirmed as "
       "written by the user 2026-08-02\", and for (f) \"Ratified by the user; the record does not "
       "date the mandate\" — the gap stated rather than filled.")
_homej("-937,0 +963,9",
       "the boundary of the no-information-loss rule — never COMPUTING a possibility is not loss, "
       "only DISCARDING a computed one is",
       "The added text records its own provenance honestly: \"Decided 2026-07-07; the record does "
       "not name the ratifier.\"")
_homej("-948,0 +983,10",
       "the rule that the analysis always emits its fullest reading and that simplifying is a "
       "comparison-side act only",
       "The added text states \"the record states neither a date nor a ratifier for the rule "
       "itself\", so the homing records a gap rather than inventing an attribution.")
_homej("-1117,0 +1162,10",
       "clause 4 of the MuseScore-dependency rule — reading and calling MuseScore's engraving code "
       "is allowed; only editing it is off limits",
       "The added text names the act: \"a user correction, 2026-06-14, of an over-statement that "
       "had conflated the two\".")
_homej("-1278,0 +1333,9",
       "the rule that Layer 3's backward re-reading facility stays switched off in the shipped "
       "configuration",
       "The added text names the act and its date: \"Decided by the user 2026-07-02.\"")
_homej("-1345,0 +1409,8",
       "the deferral of non-chord-tone detection, with the shape it is constrained to in advance",
       "The added text states \"**derivation not recorded**\" and \"The record states neither a "
       "date nor a ratifier\" — the gap written down rather than filled.")
_homej("-1411,0 +1483,2",
       "Layer 5's delegation pointer to the engagement contract, with its TRANSITIVE authority "
       "stated",
       "The added line carries \"(the fifth home case, user-ratified 2026-08-02)\" and names the "
       "user-ratified surface the authority passes through.")
_homej("-2561,0 +2635,10",
       "the rule that the annotation ban is decided by WHAT AN ANNOTATION SAYS rather than by how "
       "the score stores it",
       "The added text states \"**derivation not recorded**\" and that the record names neither a "
       "date nor a ratifier.")
_homej("-2565,0 +2649,13",
       "the standing consequence that jazz accuracy is not measurable on the corpora held, and "
       "that no jazz-specific scoring work is planned on them",
       "The added text names the measurement it rests on — the bass-injection experiment — and "
       "records \"Decided 2026-04-08; the record does not name the ratifier.\"")
_homej("-6169,0 +6266,8",
       "§12's governing requirement of zero information loss to the end user",
       "The added text records \"Ratified by the user; the record does not date it.\"")

w(_SYNC, "ARCHITECTURE.md", "-6313,0 +6519,6", RESTRUCTURING,
  _SYNC_ACCOUNT + " ★ BUT THIS HUNK'S SOURCE IS THE PROJECT'S OWN WORK HISTORY, not the code: it "
  "adds the correction paragraph for the heading above, whose ground is that \"no session since "
  "2026-04 has treated [Phase 3] as the next thing\". It leaves when the phase becomes next OPEN "
  "and settles nothing.",
  "new-document-content")


# ══ THE PASS CONTINUED, 2026-08-22 (`cc_instruction_step_zero_exclusion_and_pass_continuation.md`
#    Task 2, under Ruling 1 of `cowork_rulings_2026_08_22_dispatch_order_sitting.md`).  The remainder
#    was DERIVED fresh from the artifact's own `NOT YET READ` set after the `STATUS.md` exclusion,
#    never carried from any report's account of it, and is worked in the artifact's own order — by
#    document, then by commit, then by changed passage.  The method is the inherited one and no
#    other: each passage retrieved from the git object by explicit hash, read at its own removed and
#    added text together with its commit's own account, and the four classes applied in the DECLARED
#    ORDER with POSITIVELY CODE-INFLUENCED first. ════════════════════════════════════════════════

# ── 2026-08-03 · the phase-1j self-check correction ───────────────────────────────────────────────
w("3fbece9c1a6570df394839f4b87e9094e44eeb94", "ARCHITECTURE.md", "-970 +970", UNDETERMINED,
  "The hunk REPLACES one word of a standing statement in §2.15 — the shelved joint step's measured "
  "fire rate, stated as a percentage \"of slices\", becomes a percentage \"of cases\". ★ The first "
  "class was applied first and does NOT fire: the commit's own account names the source, and it is "
  "the record rather than the code — \"the shelved joint step's measured fire-rate is stated over "
  "regions, and the homed §2.15 text called the same quantity a percentage of slices. Corrected to "
  "'cases', which is what the source claim supports without asserting a unit.\" No fact read in "
  "implementation code is its source, and the account does not say the statement was corrected "
  "against the implementation. ★ Nor does the second class fire — no user act is named, the "
  "correction being the standing self-check's own product — and the third does not, because the "
  "hunk replaces a standing statement rather than relocating, splitting, re-heading or growing "
  "text. NOT CLEARED: the statement it corrects is about MEASURED behaviour of the system, and the "
  "screen cannot clear a correction of such a statement as restructuring.",
  "describes-pre-existing-implementation-behaviour")

# ── 2026-08-03 · phase 1k — the five 2026-08-03 rulings applied ───────────────────────────────────
_K1 = "7454abe5db4e169fcbdc43440c018b1add4db31b"
_K1_ACCOUNT = (
    "The commit's own account is \"phase 1k tasks 1-4 — the five 2026-08-03 rulings APPLIED\", and "
    "it states its own scope: \"Documentation and register work only: no src/ change, no golden "
    "refresh, no tools/corpus/ or tools/robust_stop/ movement, no behavior change, no fix, no "
    "design.\" The ruling this hunk carries is R3, which the account states as \"ARCHITECTURE.md "
    "§6.7 restated over the five idioms\".")

w(_K1, "ARCHITECTURE.md", "-4505,2 +4505,4", RATIFIED,
  _K1_ACCOUNT + " Here the hunk REPLACES §6.5's terminology note, whose examples named the retired "
  "genre families, with the five idioms — and the replacement carries its own dated attribution "
  "inside the added text: \"(Corrected 2026-08-03 with the §6.7 restatement — this note previously "
  "gave the retired genre families 'Baroque, swing, bebop' as its examples.)\" ★ The first class "
  "was applied first and does not fire: a standing statement IS replaced, but its source is the "
  "§6.7 restatement the same ruling orders, and no fact read in implementation code is cited "
  "anywhere in the added text.",
  "governing-decision-record",
  act="the user's ruling R3 of 2026-08-03 — the §6.7 taxonomy restatement over the five idioms — "
      "carried into §6.5 in the same act so the restatement does not leave the terminology note "
      "contradicting the section it cites",
  ratification_at="the added text's own \"(Corrected 2026-08-03 with the §6.7 restatement …)\"; the "
                  "commit's own account naming the surface the rulings were taken at, "
                  "`cowork_pending_ratifications_next_session.md`, and the dispatch that applied "
                  "them, `cc_instruction_phase1k_apply_rulings.md`")

w(_K1, "ARCHITECTURE.md", "-4528,9 +4530,51", RATIFIED,
  _K1_ACCOUNT + " Here the hunk REPLACES §6.7's genre taxonomy with the five idioms and their two "
  "orthogonal cross-attributes, and every load-bearing clause carries its own attribution inside "
  "the added text — \"Ratified by the user 2026-06-30 and ENCODED\" — with the discovery study's "
  "own figures as the defense and the superseded genre list preserved beneath it as historical "
  "context (#12). ★ The first class was applied first and does not fire, and the call is recorded "
  "because it is close: the added text DOES state something about the code — that the placeholder "
  "`{Baroque, Jazz, Default}` StyleTag is retired and replaced in the dormant `harmonicvocabulary` "
  "component by `enum class Idiom` + `IdiomSet`. What decides it is that every citation offered for "
  "that statement is a record document (`cowork_style_taxonomy_proposal.md`, "
  "`cowork_progression_schema_dictionary.md`) and none is implementation code; the encoding is "
  "recorded as part of what the 2026-06-30 ratification settled, not as a fact against which a "
  "documentation statement was found false.",
  "governing-decision-record",
  act="the user's ratification of the five-idiom taxonomy on 2026-06-30, applied to "
      "`ARCHITECTURE.md` §6.7 by the user's ruling R3 of 2026-08-03",
  ratification_at="the added text's own \"Ratified by the user 2026-06-30 and ENCODED\"; and the "
                  "commit's own account of R3, taken at "
                  "`cowork_pending_ratifications_next_session.md`")

# ── 2026-08-03 · phase 1m — the D-416 disposition ─────────────────────────────────────────────────
w("1b8ecaf685295024cdeafee067332ca38b26be04", "ARCHITECTURE.md", "-270,0 +271,2", RATIFIED,
  "The hunk ADDS one paragraph beside the joint estimator's standing rule (a), and the added text "
  "declares what it is in its own opening words: \"Pointer, not a seventh rule (added 2026-08-03 on "
  "the user's D-416 ruling; register entry D-429)\". It records that the 2026-06-14 mandate to "
  "dissolve the legacy post-hoc gate-correction layer carries a principle binding on this "
  "estimator, and states in terms that the mandate is NOT treated as discharged. ★ The first class "
  "was applied first and does not fire: nothing standing is withdrawn, and no fact read in "
  "implementation code appears in the added text. The commit's account DOES report a dispatch "
  "premise refuted at the code — that the gate layer is unreachable on the live notation arm — but "
  "that refutation is recorded in the register entry and in the row it names, not in this hunk.",
  "governing-decision-record",
  act="the user's D-416 ruling of 2026-08-03 (the fourth ruling set of that date), which split the "
      "two-deferred-refactors mandate into its three components and transferred component (2)'s "
      "principle to the phase-3 family design",
  ratification_at="the added text's own \"added 2026-08-03 on the user's D-416 ruling\"; the "
                  "dispatch the commit names, "
                  "`cc_instruction_phase1m_dispositions_and_measurements.md`; and register entry "
                  "D-429")

# ── 2026-08-03 · phase 1r — the six delegations the USER wrote (the OI-293 write list) ────────────
_R1 = "1642c48e7f8c41f02a9ed14129ab2b9c6291b814"
_R1_ACCOUNT = (
    "The commit's own account opens \"The user wrote all six delegations the phase-1q write list "
    "asked for (OI-293). This commit records them and re-runs every downstream act against them.\" "
    "Each of this commit's `ARCHITECTURE.md` hunks carries that attribution inside its own added "
    "text. ★ The first class was applied first and does not fire on any of them: no fact read in "
    "implementation code is cited in any added passage, and where a standing statement IS replaced "
    "the source is the user's own direction.")


def _wl(header, what):
    w(_R1, "ARCHITECTURE.md", header, RATIFIED, _R1_ACCOUNT + " " + what,
      "governing-decision-record",
      act="the six delegations the user wrote into `ARCHITECTURE.md` on 2026-08-03 — the OI-293 "
          "write list, which the phase-1q classification pass asked for and only the user may write "
          "(decisions-register rule (g))",
      ratification_at="each hunk's own \"written 2026-08-03 on the user's direction, the OI-293 "
                      "write list\" / \"widened 2026-08-03 on the user's direction (the OI-293 "
                      "write list)\"; `OPEN_ITEMS.md` OI-293; and the commit's own account, which "
                      "lists the seven write-list edits as verified present and unaltered")


_wl("-50,0 +51,6",
    "Here the hunk ADDS the delegation pointer for the pre-fit protocols, naming "
    "`cowork_prefit_gates.md` (USER-RATIFIED 2026-07-19) and D-270…D-274, with its own parenthesis "
    "recording why the weaker naming above it does not delegate under rule (i).")
_wl("-74 +80,2",
    "Here the hunk REPLACES the notation-record contract's section list, §3.1–§3.4 becoming "
    "§2–§3.4, with the user's direction and the reason inside the added text: \"the provenance rule "
    "that §3.1's own text depends on is in §2\".")
_wl("-902 +909,5",
    "Here the hunk REPLACES the voice-leading contract's section list, §0/§5.3 becoming "
    "§0/§5.1/§5.3/§8/§9, and states which sections are deliberately NOT named and why — \"they are "
    "ratification asks, not rule-stating sections\", which is the register's own kind half.")
_wl("-1484,0 +1496,2",
    "Here the hunk ADDS the delegation pointer for the function layer, naming "
    "`cowork_layer5_function_design.md` (SIGNED, user, 2026-06-26) and D-335…D-342, with its own "
    "parenthesis recording that the \"Full spec:\" line above is a citation and not a delegation — "
    "\"this paragraph is the delegation the record relied on and never had\".")

# ── 2026-08-04 · phase 1z — §5.2 stops asserting a mechanism the code removed ─────────────────────
_KEY = "c7d44b010e630c4a28bbb5d9faf8420aa39c7fc1"
_KEY_ACCOUNT = (
    "The commit's own subject states the direction of the correction in terms: \"the specification "
    "stops asserting a mechanism the code removed\". Its Task 3 account says §5.2 \"now states what "
    "the key opening actually does at HEAD (note-based, each clause read at the code, pins named), "
    "with the removal recorded as a tried-and-closed line\", and the added text says it again: "
    "\"The paragraph this replaces specified a piece-start shortcut in the present tense. The code "
    "removed that short-circuit in Stage 4b-i on 2026-06-14 and this document went on asserting "
    "it.\" That is the first class's second limb, word for word, and the class is applied FIRST.")


def _key(header, what, cites):
    w(_KEY, "ARCHITECTURE.md", header, CODE_INFLUENCED,
      _KEY_ACCOUNT + f" This hunk {what} The correction's own text cites {cites}, which this commit "
      "did not write.",
      "describes-pre-existing-implementation-behaviour")


_key("-3510,8 +3510,34",
     "REPLACES the piece-start-shortcut paragraph outright — the exception is gone and the opening "
     "is stated as note-based — and adds the scoping sentence saying which path §5.2 describes at "
     "all.",
     "`notationcomposingbridgehelpers.cpp:140`, `keyresolver.cpp:255`, `:286-289`, `:303-326`, "
     "`:340` and `:358-367`, the flag default at `composingconfiguration.cpp:178`, and the two "
     "regression pins at `regionanalysis_tests.cpp:122` and `:144`")
_key("-3536,4 +3562,4",
     "REPLACES the fallback list's count and drops the removed shortcut from it — \"the list read "
     "'two' and named the removed piece-start shortcut as the first of them\".",
     "the surviving fallback's own guard, `results.empty() || distinctPitchClasses(ctx) < 3`")
_key("-3541 +3567,4",
     "REPLACES the surviving fallback's description, adding the confidence it actually returns, the "
     "code coordinate and the pin, and the statement that it fires at any tick and is not a "
     "piece-start rule.",
     "`keyresolver.cpp:328-332` and the pin at `regionanalysis_tests.cpp:164`")
_key("-3544 +3573",
     "REPLACES the closing back-reference, \"these two fallback paths\" becoming \"that one "
     "fallback path\".",
     "the same single surviving fallback")

# ── 2026-08-04 · the six-wave backlog — the OI-327 write list and the census delegation ───────────
_BL = "e10479a09f39c46419a62ada58e584a826f275ca"
_BL_ACCOUNT = (
    "The commit's own account states what it is and what it is not: \"Committed on the user's "
    "ruling R1 of 2026-08-04 … This commit adds nothing to any of the six waves and changes nothing "
    "in them. It is the authorization each of them was owed and none of them received.\" Every "
    "`ARCHITECTURE.md` hunk of it carries its own attribution to a user act inside the added text. "
    "★ The first class was applied first and does not fire on any of them: each ADDS a delegation "
    "pointer, none withdraws a standing statement, and no fact read in implementation code is cited "
    "in any added passage.")


def _bl(header, what, act, ratification_at):
    w(_BL, "ARCHITECTURE.md", header, RATIFIED, _BL_ACCOUNT + " " + what,
      "governing-decision-record", act=act, ratification_at=ratification_at)


_bl("-331,0 +332,15",
    "Here the hunk WIDENS the census pointer to the sections holding that document's own standing "
    "rules, and states what the widening settles and what it does not — the delegation half alone, "
    "with the kind half left to be judged per section at the classification pass.",
    "the user's census-delegation ruling of 2026-08-04, written under the fifth home case "
    "(decisions-register rule (g), user-ratified 2026-08-02)",
    "the added text's own \"written 2026-08-04 on the user's ruling; the fifth home case, rule (g), "
    "user-ratified 2026-08-02\"; and the commit's own account of the census-delegation wave, "
    "`cc_instruction_census_delegation_and_commit.md`")
_bl("-1241,0 +1257,4",
    "Here the hunk ADDS two delegation pointers — the Layer-1 note model's contract and the "
    "Layer-1.5 phrase-boundary primitive's — the second with its siting reasoned in its own "
    "parenthesis, including why it is not sited at the consuming Layer-6 section.",
    "the OI-327 write list — the delegations the user wrote into `ARCHITECTURE.md` on 2026-08-04",
    "each pointer's own \"written 2026-08-04 on the user's direction, the OI-327 write list\"; "
    "`OPEN_ITEMS.md` OI-327; and the commit's own account of read wave 5, which records three "
    "delegations written and two withheld")
_bl("-1327,0 +1347,2",
    "Here the hunk ADDS the Layer-2 slicer's delegation pointer, with its own parenthesis recording "
    "that the \"See …\" line above is a citation of three documents and not a delegation under rule "
    "(i).",
    "the OI-327 write list — the delegations the user wrote into `ARCHITECTURE.md` on 2026-08-04",
    "the pointer's own \"written 2026-08-04 on the user's direction, the OI-327 write list\"; "
    "`OPEN_ITEMS.md` OI-327")
_bl("-1508,0 +1530,2",
    "Here the hunk ADDS the Layer-6 delegation pointer together with the user's answer to the "
    "question it had been withheld over — why a contract home is coherent for a layer that may not "
    "be built — and states in terms that D-266 is untouched and that the pointer authorizes no "
    "build, no wiring and no change to what the analysis computes.",
    "the OI-327 write list, together with the user's 2026-08-04 answer on the withheld Layer-6 "
    "clause",
    "the pointer's own \"written 2026-08-04 on the user's direction, the OI-327 write list\" and "
    "its own \"the question this clause was withheld over on 2026-08-04 and which the user has now "
    "answered\"; `OPEN_ITEMS.md` OI-327")

# ── 2026-08-07 · three phase-1 waves committed on the user's instruction ──────────────────────────
_TW = "bd3a608fecf82c446f959432b13e0a5944093cd2"
_TW_ACCOUNT = (
    "The commit's own subject is \"commit three phase-1 waves on the user's instruction\", and its "
    "body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a "
    "RE-HOMING act under D-231's criterion C1 — a register decision written into the specification "
    "that owns it — and each added block names the register entry it carries and says it was "
    "\"re-homed into this specification 2026-08-04\".")

w(_TW, "ARCHITECTURE.md", "-1289,0 +1290,24", RATIFIED,
  _TW_ACCOUNT + " Here the added blocks carry D-628, the change-point as the finest meaningful "
  "extension step, and D-607, the absence of any validated deterministic rule set for polyphonic "
  "phrase-boundary detection. ★ The first class was applied first and does not fire: both ADD "
  "material and withdraw nothing, and neither ground is a fact read in implementation code — "
  "D-628's is what a Layer-2 slice IS as this same document specifies it, and D-607's is a stated "
  "fact of absence established by a literature survey.",
  "governing-decision-record",
  act="the D-231 phase-1 re-homing of two register decisions into the specification that owns them, "
      "performed under the user's instruction of 2026-08-04 and criterion C1 as re-issued that day",
  ratification_at="each added block's own \"re-homed into this specification 2026-08-04\"; the "
                  "commit's own \"on the user's instruction\"; D-231's phase-1 clause at "
                  "`CLAUDE.md` Conventions (user-directed 2026-08-02); and the C1 ruling the commit "
                  "names, `cc_instruction_c1_ruling_and_item1c.md` (register entry D-642)")

w(_TW, "ARCHITECTURE.md", "-1375,0 +1400,30", RATIFIED,
  _TW_ACCOUNT + " Here the added blocks carry D-624, D-635 and D-623. ★ The first class was applied "
  "first and does NOT fire, and the call is recorded because it is close: two of the three rest on "
  "what the implementation currently does — D-635's claim that the requirement is MASKED rests on "
  "\"the note model still loads the whole score anyway\", and D-623's on the capability having been "
  "built as an option on the existing driver and being off by default. What decides it is the "
  "distinction the inherited method already draws at a homing act: all three ADD material and none "
  "withdraws a standing documentation statement, and each implementation fact is stated as the "
  "DECISION'S OWN CONTENT — what the design chose and what state it left — not as a fact against "
  "which a documentation statement was found false.",
  "governing-decision-record",
  act="the D-231 phase-1 re-homing of three bounded-context and orchestration decisions into the "
      "specification that owns them, performed under the user's instruction of 2026-08-04",
  ratification_at="each added block's own \"re-homed into this specification 2026-08-04\"; the "
                  "commit's own \"on the user's instruction\"; and D-231's phase-1 clause at "
                  "`CLAUDE.md` Conventions (user-directed 2026-08-02)")

w(_TW, "ARCHITECTURE.md", "-1505,0 +1560,22", CODE_INFLUENCED,
  _TW_ACCOUNT + " ★ BUT THE FIRST CLASS FIRES HERE, and it is applied first exactly so that a "
  "ratified act cannot launder a correction made under it. The added block's own heading is \"Two "
  "premises this decoder carries were MEASURED, and both came back against it\", and it QUALIFIES "
  "what this section specifies: the symmetric-root spelling pin's entry premise is stated FALSE and "
  "the mechanism effectively unreachable (D-608), and the abstention rate is stated to ride on a "
  "never-fitted seed constant (D-609). The source is named in the added text itself — \"measured at "
  "the probe and traced at the code\" for the first, \"established at the code — the constant is a "
  "seed in the decoder's own header, and the control flow was traced\" for the second — and this "
  "commit wrote none of that code.",
  "describes-pre-existing-implementation-behaviour")

w(_TW, "ARCHITECTURE.md", "-1520,0 +1597,31", RATIFIED,
  _TW_ACCOUNT + " Here the added block carries D-584, D-585 and D-586, three standing constraints "
  "on this layer's methods. ★ The first class was applied first and does not fire, and the call is "
  "recorded because it is close: D-586's text DOES name our own legacy component — \"the legacy "
  "component carrying the name compares candidate chords instead\". What decides it is that the "
  "constraint's stated ground is a literature survey (\"established by survey — every published "
  "autonomous Roman-numeral system the catalog names …\"), the naming of our own component being an "
  "explanatory corollary rather than the source; and that nothing standing in the documentation is "
  "withdrawn — the closing sentence EXPLAINS why the layer's output is already specified as the "
  "Roman numeral rather than replacing that specification.",
  "governing-decision-record",
  act="the D-231 phase-1 re-homing of three method constraints into the specification that owns "
      "them, performed under the user's instruction of 2026-08-04; the three decisions are recorded "
      "as user-ratified on that date",
  ratification_at="the added block's own \"re-homed into this specification 2026-08-04\"; the "
                  "commit's own \"on the user's instruction\"; and D-231's phase-1 clause at "
                  "`CLAUDE.md` Conventions (user-directed 2026-08-02)")

w(_TW, "ARCHITECTURE.md", "-3565,0 +3673,11", RATIFIED,
  _TW_ACCOUNT + " Here the added block records D-572 — the hard post-hoc declared-mode promotion — "
  "as a tried-and-closed line beside the §5.2 correction the preceding commit made, which is the "
  "form the commit's own body names: \"ruling R2 recorded (D-644) and applied to D-572 at "
  "ARCHITECTURE.md §5.2\". ★ The first class was applied first and does NOT fire: the hunk ADDS the "
  "closed line and withdraws nothing — the standing statement it belongs to had already been "
  "replaced by the preceding commit, which is graded on its own hunks above — and it cites no code "
  "coordinate. ★ ONE THING THE SCREEN CANNOT ESTABLISH IS RECORDED RATHER THAN RESOLVED: the added "
  "text attributes the removal's defense to \"the defense recorded with the change\" without naming "
  "WHERE that record is, so whether the wording came from the code beside the removal or from the "
  "change's own written record is not decidable at this hunk's text. It does not move the verdict, "
  "because the ACT this hunk performs is the ruled one and is named.",
  "governing-decision-record",
  act="ruling R2 of 2026-08-04 — where a superseded decision's content is a REMOVAL, the "
      "specification states the current behaviour and records the removal as a tried-and-closed "
      "line — applied here to D-572",
  ratification_at="the dispatch the commit's own body names, "
                  "`cc_instruction_guard_fix_and_item1d.md` (\"ruling R2 recorded (D-644) and "
                  "applied to D-572 at ARCHITECTURE.md §5.2\"); and the rule's home at "
                  "`cowork_audit_protocol.md`, register entry D-644")


# ── 2026-08-08 · five waves committed as one — the owner-rulings homings ──────────────────────────
_OW = "d1891db1588d73fbf41789c9139006d269a1c766"
_OW_ACCOUNT = (
    "The commit carries five waves and names each with the dispatch that ran it; the wave whose "
    "acts these hunks are is `cc_instruction_owner_rulings_homing.md` — \"the forty-eight owner "
    "rulings homed; the joint estimator gains a section a decision can be sited inside\". Every "
    "`ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added "
    "blocks say so in their own words — \"re-homed into this specification 2026-08-07 on the user's "
    "ruling\". The commit's own scope line is \"No src/ change, no goldens, no tools/corpus/ or "
    "tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no "
    "design.\"")
_OW_ACT = ("the user's owner rulings of 2026-08-07, homed into the specifications that own them "
           "under D-231's phase-1 criterion C1")
_OW_RAT = ("each added block's own \"re-homed into this specification 2026-08-07 on the user's "
           "ruling\"; the ruling record the commit lands beside them, "
           "`cowork_owner_rulings_2026_08_07.md`; the dispatch "
           "`cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` "
           "Conventions (user-directed 2026-08-02)")


def _ow(header, verdict, what, shape, act=None, rat=None):
    w(_OW, "ARCHITECTURE.md", header, verdict, _OW_ACCOUNT + " " + what, shape,
      act=(act if verdict == RATIFIED else None),
      ratification_at=(rat if verdict == RATIFIED else None))


_ow("-264,0 +265,2", RESTRUCTURING,
    "Here the hunk adds a HEADING and nothing else — \"## The joint estimator — the standing rules "
    "of the production inference layer\" — which is the commit's own \"the joint estimator gains a "
    "section a decision can be sited inside\". ★ The first class was applied first and does not "
    "fire: no statement of any kind is made, so nothing can be withdrawn and no source is cited. "
    "The second does not fire either — a heading records no ruling's content — and the third does, "
    "this being a re-heading whose source is not a fact read in implementation code.",
    "document-relocation-or-re-heading")

_ow("-355,0 +358,76", RATIFIED,
    "Here the hunk adds the decode's five counted quantities — factor granularity, the "
    "key-signature and declared-mode prior's scope, the secondary-dominant pooling level, the "
    "leftover back-off and the per-factor missing-tone penalty — and the document-governance "
    "heading beneath them. ★ The first class was applied first and does not fire: every block ADDS "
    "and withdraws nothing, and each ground named in the added text is a desk simulation, a count "
    "over the ground-truth corpus or the published back-off construction — not a fact read in "
    "implementation code. The counting is over the annotated corpus, which is ground truth and not "
    "our own output.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-533,0 +612,17", RATIFIED,
    "Here the hunk adds the standing verdict that the hand-built analysis is CONFIRMED and the "
    "learned replacement NOT triggered, retained as an explicit fallback with a concrete trigger. "
    "★ The first class was applied first and does NOT fire, and the call is recorded because it is "
    "close: the verdict's whole ground is a MEASUREMENT of what this implementation produces — "
    "\"the error mass decomposes into causes reachable within it\", \"the corrected metric showed "
    "the residual had been inflated by already-correct artifacts and by mis-attributed cases\". "
    "What decides it is that the block ADDS and withdraws nothing, and that the measurement is the "
    "DECISION'S OWN SUBJECT — the choice between a hand-built and a learned scorer was sized by "
    "measuring, which is the decision — not a fact against which a documentation statement was "
    "found false.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-1207,0 +1303,28", RATIFIED,
    "Here the hunk adds the two boundary invariants that keep the rendered form from crossing back "
    "into the analysis — structured fields only, and a written chord symbol readable only as a "
    "comparison or ground-truth label — and states in its own text why they are sited at the "
    "boundary's own section rather than copied (#6). ★ The first class was applied first and does "
    "not fire: both invariants ADD, both defenses are stated as the rules' own reasoning, and "
    "neither cites a fact read in implementation code.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-1481,0 +1605,55", RATIFIED,
    "Here the hunk adds four standing rules of the key/mode layer — what a local-key hypothesis may "
    "read, at what scope a global tonic anchor enters, the refuted reach-back proxy, and the owed "
    "enharmonic-identity rule for key spans. ★ The first class was applied first and does NOT fire, "
    "and the call is recorded because it is close: the second rule's ⚠ LEGACY mark is justified by "
    "a REACHABILITY CHECK AT THE CODE this commit did not write — \"the window scorer this rule "
    "excludes (`KeyModeAnalyzer::analyzeKeyMode`) is reached only through the legacy resolver and "
    "this layer's dormant sequence decoder, and the resolver is retired from the production region "
    "path\" — and the added text says in terms that the mark \"follows a check at the code, not the "
    "decision's age\". What decides it is that all four ADD and none withdraws a standing "
    "documentation statement: the code check SCOPES a rule arriving here for the first time, rather "
    "than refuting a statement this document already carried.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-1581,0 +1760,27", RATIFIED,
    "Here the hunk adds the chord search's output-surface contract and the shared spelling "
    "primitive's presence test. ★ The first class was applied first and does NOT fire, and the call "
    "is recorded because it is close: the presence-test rule's own defense is \"established at the "
    "source rather than asserted\" — the source being the shared line-of-fifths primitive, whose "
    "sign convention and whose `tpcIsValid()` predicate this commit did not write — and it carries "
    "an honest bound read at the same place, that the predicate cannot tell a real flattest "
    "spelling from a default-initialised field. What decides it is that both rules ADD and neither "
    "withdraws a standing documentation statement: the primitive's sign convention is cited as the "
    "REASON FOR THE RULE, not as a fact that found an existing statement false.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-1627,0 +1833,25", RATIFIED,
    "Here the hunk adds the two ratified obligations the function layer owes — a stated fallback "
    "for a featureless phrase-boundary profile, and key-confirmation channels that do not require a "
    "cadence — and marks both DESIGN-ONLY in its own words, \"work this layer is required to "
    "specify, not mechanisms it has\". ★ The first class was applied first and does not fire: both "
    "ADD, both grounds are the architecture review's own stress simulation on resolution-denying "
    "music, and no fact read in implementation code is cited.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-3787,0 +4018,25", RATIFIED,
    "Here the hunk adds two standing rules on the temporal-context structure — what may enter it, "
    "and that its extension fields are recorded by the producing pass and never rebuilt by a "
    "consumer. ★ The first class was applied first and does NOT fire, and the call is recorded "
    "because it is close: the first rule's finding is stated about the CODE and not about the "
    "record — \"Four fields describing the previous winner's competition outcome were added to it "
    "that belong to the planned progression-level structure instead\", the finding being that "
    "\"one had been growing into the other with no migration plan written down\". What decides it "
    "is that both rules ADD and neither withdraws a standing documentation statement, and that the "
    "code fact is what the rule is ABOUT — a prohibition on adding more of the same — rather than "
    "a fact that found an existing statement false.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-4304,0 +4560,7", RESTRUCTURING,
    "Here the hunk adds a POINTER and nothing else — that why the tick-local path is a separate "
    "module at all is decided at §11.5 and stated once there (#6). ★ The first class was applied "
    "first and does not fire: no statement about the system is made or withdrawn here, the "
    "paragraph only re-points the reader. The second does not fire — a pointer records no ruling's "
    "content — and the third does.",
    "document-relocation-or-re-heading")

_ow("-4330,0 +4593,7", RESTRUCTURING,
    "Here the hunk adds a POINTER — that how a spelling's presence is tested belongs to the "
    "Layer-4 section that specifies the shared primitive, and is stated once there (#6). ★ The "
    "first class was applied first and does not fire, and the call is recorded because the pointer "
    "repeats the rule's one-clause reason (\"the flat side of the line of fifths is negative\"). "
    "What decides it is that the paragraph withdraws nothing and states no fact of its own: it "
    "re-points, which is the third class exactly. The rule it points at is graded at its own hunk "
    "above.",
    "document-relocation-or-re-heading")

_ow("-4712,0 +4982,18", RATIFIED,
    "Here the hunk adds the rule that every uncalibrated style constant and idiom carries the "
    "empirically-unvalidated mark with its validation path named beside it, and closes by stating "
    "in terms what it does NOT claim — that the mark is applied at HEAD; it is not, and applying it "
    "is owed work tracked in the open-items register. ★ The first class was applied first and does "
    "not fire: the block ADDS, and its ground is the architecture review's own finding about where "
    "the mark is ABSENT FROM THE SPECIFICATION, which is a fact about the record and not one read "
    "in implementation code.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-4766,0 +5054,68", RATIFIED,
    "Here the hunk adds the five rules of the method that produces and re-produces the idiom "
    "taxonomy — discover-then-name, the key-normalised tonal-pitch-class encoding, confound control "
    "as a validity gate, the external mechanical extractor, and re-discovery riding every corpus "
    "wave. ★ The first class was applied first and does not fire: the block ADDS, and every ground "
    "is methodological or prior art. Where our own tooling is named — the slicer not used for "
    "extraction, the analyzer deliberately kept out of it — it is named as the study's own DESIGN "
    "CHOICE and its stated reason, not as a fact against which a documentation statement was found "
    "false.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-4789,0 +5145,25", RATIFIED,
    "Here the hunk adds the harmonic vocabulary's declared dormancy — the function layer does not "
    "touch it until the recognition consumer is built, and the connection is absent rather than "
    "partial — and states the one open structural question with the trigger that decides it. ★ The "
    "first class was applied first and does not fire: the block ADDS, and both grounds are the "
    "ratified build order and the component's own contract, with no fact read in implementation "
    "code cited.",
    "governing-decision-record", _OW_ACT, _OW_RAT)

_ow("-6405,0 +6786,35", RATIFIED,
    "Here the hunk adds this pipeline's own scope statement — the point-in-time path left outside "
    "it by design — and the pre-declared keep-or-drop rule for the sub-beat annotation duration "
    "gate, with both branches fixed in advance and the gate recorded undischarged at HEAD. ★ The "
    "first class was applied first and does not fire: the block ADDS and withdraws nothing, its "
    "scope half restates a decision's own stated reason (point-in-time semantics differ too much to "
    "force one interface), and its gate half is a protocol written BEFORE the measurement it "
    "governs — the pre-declared-protocol discipline, which is the opposite of a correction made "
    "against a result.",
    "governing-decision-record", _OW_ACT, _OW_RAT)


# ── 2026-08-08 · the hold is over — the away batch's Task 0 and the document-routes wave ──────────
_HO = "82ebfd68d9f7760396aab2b792ea3a1dce02a9e5"
_HO_ACCOUNT = (
    "The commit's own account is \"Task 0 of the away batch (`cc_instruction_away_execution.md`), "
    "applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)\", and it "
    "states its own scope: \"No `src/` change, no golden, no `tools/corpus/` or "
    "`tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no "
    "design.\" Every `ARCHITECTURE.md` hunk of it says in its own added text either \"re-homed into "
    "this specification 2026-08-08 on the user's ruling\" or \"this delegation written 2026-08-08 "
    "on the user's ruling\".")
_HO_ACT = ("the user's rulings of 2026-08-08, under which the owed decisions were homed into the "
           "specifications that own them and four delegations were written, D-231's phase-1 "
           "criterion C1 being the standing obligation they discharge")
_HO_RAT = ("each added block's own \"re-homed into this specification 2026-08-08 on the user's "
           "ruling\" / \"this delegation written 2026-08-08 on the user's ruling\"; the ruling "
           "record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 "
           "clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)")


def _ho(header, verdict, what, shape):
    w(_HO, "ARCHITECTURE.md", header, verdict, _HO_ACCOUNT + " " + what, shape,
      act=(_HO_ACT if verdict == RATIFIED else None),
      ratification_at=(_HO_RAT if verdict == RATIFIED else None))


_ho("-272,0 +273,7", RATIFIED,
    "Here the hunk adds the delegation pointer for the estimator's factor structure, naming "
    "`cowork_joint_estimator_factorization.md` and saying what the six rules beneath it govern by "
    "contrast. ★ The first class was applied first and does not fire: the pointer ADDS, withdraws "
    "nothing, and cites no fact read in implementation code.",
    "governing-decision-record")

_ho("-431,0 +439,50", RATIFIED,
    "Here the hunk adds the hard/soft line the evidence classification rests on, and where the "
    "hand-built-versus-learned choice lives — four statements carried forward out of a superseded "
    "architecture proposal, with the added text stating in terms that nothing of the superseded "
    "proposal's SHAPE is carried. ★ The first class was applied first and does NOT fire, and the "
    "call is recorded because it is close: three of the four rest on MEASUREMENTS — the notated "
    "signature measured to pin the wrong home key, and three reading-shaped producers each measured "
    "to pin wrong. What decides it is that the block ADDS and withdraws nothing, that the signature "
    "finding's own scope clause says it is \"a property of the written music and its human "
    "analyses, not of any one of our pipelines\", and that the producers' measurements are carried "
    "with an explicit ⚠ LEGACY SCOPE saying they are of those producers and not claims about the "
    "estimator this section specifies.",
    "governing-decision-record")

_ho("-1436,0 +1494,12", RATIFIED,
    "Here the hunk adds the rule that voice slots and stem direction are structural notational "
    "metadata and may therefore be read by this layer. ★ The first class was applied first and does "
    "not fire: the block ADDS, and its whole defense is the line the chord-symbol prohibition "
    "already draws — what the score IS versus what a user has CLAIMED about it — applied to a new "
    "pair of fields, with no fact read in implementation code cited.",
    "governing-decision-record")

_ho("-1495,0 +1565,31", RATIFIED,
    "Here the hunk adds what may be asserted across an extension and what a slice carries — the "
    "loaded-edge boundary being artificial so that the edge slice GROWS, with an "
    "old-slices-stay-byte-identical assertion recorded FALSE and prohibited as a test, and the "
    "slice kept minimal. ★ The first class was applied first and does not fire: the block ADDS, and "
    "the false assertion it prohibits is corrected against a COUNTEREXAMPLE THE DESIGN STATES IN "
    "FULL — a single eligible note spanning the loaded start — not against a fact read in "
    "implementation code. Its one implementation statement, that the minimal form was taken at the "
    "build, records the decision's outcome rather than sourcing it.",
    "governing-decision-record")

_ho("-1659,0 +1760,18", RATIFIED,
    "Here the hunk adds the Baroque partial-signature handling — detect the convention and "
    "reinterpret the signature one step, never widen the candidate family for every score. ★ The "
    "first class was applied first and does NOT fire, and the call is recorded because it is close: "
    "the block carries a ⚠ LEGACY / SUPERSEDED IN FACT qualification whose ground is an ARM CHECK "
    "AT THE CODE — \"the correction is applied inside the legacy resolver, which the production arm "
    "no longer runs; no ruling superseded it, a later build replaced what it governs\". What "
    "decides it is that the rule and its qualification arrive TOGETHER in one addition: no standing "
    "statement of this document is withdrawn, and the block explicitly declines to assert anything "
    "about the arm that runs — \"Whether the joint estimator handles the convention AT ALL is NOT "
    "settled by this entry and is not asserted here.\"",
    "governing-decision-record")

_ho("-1674,0 +1793,13", RATIFIED,
    "Here the hunk adds the constraint that a rebuilt or re-tuned chord scoring must not lean on "
    "the held-note repetition bonus the faithful note model removed. ★ The first class was applied "
    "first and does NOT fire, and the call is recorded because it is close: the constraint's ground "
    "is a MEASUREMENT taken when the removal surfaced — \"removing the inflation moved a small "
    "number of cases the wrong way while the key axis stayed flat\". What decides it is that the "
    "block ADDS and withdraws nothing, and that the added text refuses the very assertion a "
    "correction would make: \"Whether those cases have since recovered is NOT stated here and was "
    "not checked — the constraint binds regardless.\"",
    "governing-decision-record")

_ho("-1799,0 +1931,18", RATIFIED,
    "Here the hunk adds that the resolver of carried uncertain readings is this layer itself and "
    "that there is no distinct gated box between the note layers and it. ★ The first class was "
    "applied first and does not fire: the block ADDS, and its defense is \"derived from the "
    "layer-identity test and then confirmed by measurement\" — a derivation from the layer contract "
    "with a corpus measurement as corroboration, and the three admission tests for a new component "
    "applied to it. No standing documentation statement is withdrawn; the added text reads the "
    "'gated step' language elsewhere as describing this layer's own gated entry.",
    "governing-decision-record")

_ho("-1868,0 +2018,26", RATIFIED,
    "Here the hunk adds the key-area grouping rule — a smoothing pass over stabilized regions, with "
    "a disagreeing region keeping its own key while being grouped — together with a marked block "
    "that splits the decision across the two arms. ★ The first class was applied first and does "
    "NOT fire, and this is the closest call in the commit: the marked block IS an arm check at the "
    "code, citing `sectionrecordadapter.cpp:360` and `sectionanalyzer.cpp:750`, and it reports that "
    "the rule is live on the record arm while the stabilization pass it names as a PRECONDITION has "
    "its only call site inside the legacy arm. What decides it is that the rule and the split "
    "arrive together in one addition, so nothing this document already stated is withdrawn — and "
    "that the block takes NO verdict: it states the question as OPEN, says in terms that it bears "
    "on the analysis, and points it at the open-items register. ★ Recorded so a reader meets it: "
    "this is a code-read fact reaching a specification, and it is cleared here only because it "
    "withdraws nothing and adjudicates nothing.",
    "governing-decision-record")

_ho("-5121,0 +5297,100", RATIFIED,
    "Here the hunk adds what the taxonomy and its weights are as an object, three findings about "
    "the second axis the discovery study found, and the whole of §6.8 — the user-facing preset "
    "layer's naming, coverage tiers, mixture contract and licence split, marked RECORDED and "
    "DEFERRED product work. ★ The first class was applied first and does not fire: the block ADDS, "
    "and its grounds are the discovery study's own measurements over external corpora and the "
    "standing principles, none of them a fact read in implementation code. Its one implementation "
    "remark — that custom properties survive the native format while the MusicXML round-trip is "
    "only partial — is recorded as an open check the feature must make, not as a source.",
    "governing-decision-record")

_ho("-6493,0 +6769,8", RATIFIED,
    "Here the hunk adds the delegation pointer for the notation-surface adoption increment, with "
    "its own sentence separating what stays in that contract from what this section states. ★ The "
    "first class was applied first and does not fire: the pointer ADDS, withdraws nothing and cites "
    "no fact read in implementation code.",
    "governing-decision-record")

_ho("-7527,0 +7811,6", RATIFIED,
    "Here the hunk adds the delegation pointer for the language-model integration's detailed "
    "design. ★ The first class was applied first and does not fire, on the same ground as the "
    "pointer above: it ADDS, withdraws nothing and cites no fact read in implementation code.",
    "governing-decision-record")


# ── 2026-08-08 · nine archive-only decisions moved into the specifications that own them ──────────
_AR = "dfbf3ab824f0717d83cf3cce8e332c69f1074328"
_AR_ACCOUNT = (
    "The commit's own account is \"Task 2 of the away batch (`cc_instruction_away_execution.md`). "
    "D-601's homing is the one edit Ruling 2 of `cowork_rulings_2026_08_08_pre_away.md` "
    "authorizes\", and it states what the act was FOR: entries that \"lived ONLY in a "
    "session-handoff archive\" or were \"already NAMED in an `ARCHITECTURE.md` 'Tried and closed' "
    "line without the section saying what they were, so a reader met an identifier and could not "
    "learn the rule\". Both `ARCHITECTURE.md` hunks say so in their own added text: \"re-homed into "
    "this specification 2026-08-08\". The commit's scope line is \"No `src/` change, no golden, no "
    "corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no "
    "fix to inference, no design.\"")
_AR_ACT = ("the away batch's Task 2 under the user's rulings of 2026-08-08, re-homing "
           "archive-only decisions into the specifications that own them — D-231's phase-1 "
           "criterion C1 being the standing obligation discharged")
_AR_RAT = ("each added block's own \"re-homed into this specification 2026-08-08\"; the ruling "
           "record the batch applies, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 "
           "clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)")

w(_AR, "ARCHITECTURE.md", "-316,0 +317,14", RATIFIED,
  _AR_ACCOUNT + " Here the hunk adds what D-288 IS — do not retry widening the search to consider "
  "more candidate readings in parallel — behind a naming the section already carried. ★ The first "
  "class was applied first and does NOT fire, and the call is recorded because it is close: the "
  "rule's ground is a MEASUREMENT of this system's own behaviour, \"the wrong reading is the "
  "highest-scoring one\", cross-checked against independent earlier measurements. What decides it "
  "is that the block ADDS the content behind an existing identifier and withdraws nothing, and that "
  "the measurement is the SHELVING'S OWN SUBJECT rather than a fact against which a documentation "
  "statement was found false.",
  "governing-decision-record", act=_AR_ACT, ratification_at=_AR_RAT)

w(_AR, "ARCHITECTURE.md", "-1613,0 +1628,25", RATIFIED,
  _AR_ACCOUNT + " Here the hunk adds what the key layer's two named dead ends ARE — the ranked "
  "key-candidate carry, and deciding the key from key-agnostic cadences one at a time — each with "
  "its stated re-open condition or its stated scope. ★ The first class was applied first and does "
  "NOT fire, on the same ground as the hunk above: both rules ADD content behind namings the "
  "section already carried, both grounds are measurements of legacy mechanisms that are the "
  "shelvings' own subjects, and one of them is explicitly re-read for the joint estimator — \"that "
  "design carries a full posterior by construction, so the concern this shelving withdrew is met by "
  "a different design rather than by reviving this one\".",
  "governing-decision-record", act=_AR_ACT, ratification_at=_AR_RAT)

# ── 2026-08-09 · the ten rulings of 2026-08-09 applied through Task 3 ─────────────────────────────
_R9 = "935efcf99349bf414196e81613f07b9cfae99f43"
_R9_ACCOUNT = (
    "The commit's own account is \"the ten rulings of 2026-08-09 applied through Task 3\", "
    "applying `cowork_rulings_2026_08_09_return.md` read whole, and it states its scope: \"No src/ "
    "change, no golden, no corpus of scores, no tools/robust_stop/ movement, no behaviour change to "
    "the analysis, no fix to inference, no design.\" Both `ARCHITECTURE.md` hunks carry their own "
    "attribution — \"written into this section 2026-08-09 on the user's ruling\".")

w(_R9, "ARCHITECTURE.md", "-1212,0 +1213,30", RATIFIED,
  _R9_ACCOUNT + " Here the hunk homes D-286 — whole-score interactive analysis SHELVED WITH "
  "EVIDENCE against a bounded window — into §2.16, with a marked block stating that the "
  "implementation at HEAD contradicts the shelving. ★ The first class was applied first and does "
  "NOT fire, and this is a close call recorded in full: the marked block IS a statement read at the "
  "implementation — \"The record producer takes no tick range: every record-arm seam analyzes the "
  "whole score and narrows to the requested span afterward\" — and it is offered against the very "
  "decision being homed. What decides it is that the shelving and the contradiction arrive TOGETHER "
  "in one addition, so nothing this document already stated is withdrawn, and that the block takes "
  "NO verdict — it says in terms \"This section does not decide which of the two is right\" and "
  "points the conformance question at its own rows. That is the ruled form for homing a decision "
  "the implementation contradicts, applied rather than improvised.",
  "governing-decision-record",
  act="the user's Ruling 5 of 2026-08-09 — where the implementation contradicts the decision being "
      "homed, the shelving is written in AS a shelving, the contradiction stated beside it and the "
      "questions pointed at their rows, with no verdict taken",
  ratification_at="the added block's own \"written into this section 2026-08-09 on the user's "
                  "ruling\"; the ruling record the commit names, "
                  "`cowork_rulings_2026_08_09_return.md`; and the rule's home at "
                  "`cowork_audit_protocol.md`, register entry D-649")

w(_R9, "ARCHITECTURE.md", "-2045,0 +2076,28", RATIFIED,
  _R9_ACCOUNT + " Here the hunk homes the BUILD half of D-291 — the tonicization labeller is "
  "deliberately left unwired and the real lever is a local-modulation detector at the key layer — "
  "with its measurement half explicitly left where it belongs (#6). ★ The first class was applied "
  "first and does NOT fire: the block ADDS and withdraws nothing, and its ground is a measurement "
  "of the GRADING COMPARISON against the human annotations — that the comparison scores by root and "
  "quality and therefore MASKS the key error — which is a fact about the measurement apparatus and "
  "the ground truth, not a fact read in implementation code that found a documentation statement "
  "false.",
  "governing-decision-record",
  act="the user's Ruling 11 of 2026-08-09, splitting D-291 and homing its build half at the "
      "Layer-5 function section with its defense",
  ratification_at="the added block's own \"written into this section 2026-08-09 on the user's "
                  "ruling\"; `cowork_rulings_2026_08_09_return.md`; and the measurement half's own "
                  "home in `CLAUDE.md` gate block (A), which the block points at rather than "
                  "restating")

# ── 2026-08-09 · the specification now describes the arm that ships ───────────────────────────────
w("4aab2ec297444a4a85d7b0197cf07e66fe9d5354", "ARCHITECTURE.md", "-2115,25 +2115,48",
  CODE_INFLUENCED,
  "The commit's own subject states the direction of the change in terms: \"the specification now "
  "describes the arm that ships\". ★ THE FIRST CLASS FIRES, on both of its limbs. The hunk REPLACES "
  "a standing statement of this document — the heading's \"OVER STABILIZED REGIONS\" and the whole "
  "OPEN QUESTION block beneath it, both of which this same population carries as an earlier hunk — "
  "with a corrected account of what supplies the smoothed key sequence on each arm. And the "
  "correction's source is named as a read at the code: \"after the read-only probe the open-items "
  "register had reserved to the user established the answer at the code\". Its own why-clause is "
  "the first class's second limb word for word — \"the former text named the legacy step as THE "
  "precondition, so it described an arm that does not ship; the record arm meets the requirement by "
  "other means, and a specification that says otherwise cannot be the compliance standard (#10)\". "
  "The corrected text carries the behavioural non-equivalence between the two arms visibly and "
  "calls it UNMEASURED, and the former wording stands preserved in place (#12).",
  "describes-pre-existing-implementation-behaviour")

# ── 2026-08-09 · the homing default executed for three entries ────────────────────────────────────
_HD = "9fe7f4561f750de4403b9bf9cfe812e474a1a5b3"
_HD_ACCOUNT = (
    "The commit's own account is \"Dispatch `cc_instruction_return_continuation_6.md` Task 1, on "
    "the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`: re-homing into the owning "
    "layer's specification is the DEFAULT closing route for the finish line's homing items\", and "
    "both `ARCHITECTURE.md` hunks carry their own attribution — \"user-ratified 2026-07-03; written "
    "here 2026-08-09\". Its scope line names no `src/` change, no golden, no corpus of scores and "
    "no behaviour change to the analysis.")
_HD_ACT = ("the user's Ruling 38 of 2026-08-09, making re-homing into the owning layer's "
           "specification the default closing route, executed here for two entries the user "
           "ratified on 2026-07-03")
_HD_RAT = ("each added block's own \"user-ratified 2026-07-03; written here 2026-08-09\"; the "
           "ruling record the commit names, `cowork_rulings_2026_08_09_sixth_stop.md`; and the "
           "rule's home at `CLAUDE.md`, decisions-register rule (l)")

w(_HD, "ARCHITECTURE.md", "-1094,0 +1095,14", RATIFIED,
  _HD_ACCOUNT + " Here the hunk adds the per-voice span kind to the span typology, with what the "
  "record deliberately does NOT assert stated beside it — that consecutive phrases within one voice "
  "tile that voice exactly. ★ The first class was applied first and does not fire: the block ADDS a "
  "member to the typology, withdraws nothing, and its ground is contrapuntal writing itself — "
  "phrases running concurrently and out of step across voices — with no fact read in implementation "
  "code cited.",
  "governing-decision-record", act=_HD_ACT, ratification_at=_HD_RAT)

w(_HD, "ARCHITECTURE.md", "-1124 +1138,17", RATIFIED,
  _HD_ACCOUNT + " Here the hunk assigns four ownerless analysis objects to the voice-leading axis, "
  "each written in AS A CLAIM discharged only at that component's own ratified design. ★ The first "
  "class was applied first and does NOT fire, and the call is recorded because it is close: one "
  "ground is a check at our own built catalogue — \"the built chord catalogue already records "
  "exactly that with a voice-leading-defined flag on the entries concerned, checked at the "
  "catalogue rather than assumed\". What decides it is that the hunk's one replaced line is a SPLIT "
  "made to insert the block, not a withdrawal, and that the catalogue check is offered as the "
  "REASON an object belongs to the axis rather than as a fact that found a documentation statement "
  "false.",
  "governing-decision-record", act=_HD_ACT, ratification_at=_HD_RAT)

# ── 2026-08-10 · Ruling 39's delegation written verbatim ──────────────────────────────────────────
w("2fae57d21219e834a24a2e8cf391ae47cf66f63d", "ARCHITECTURE.md", "-369,0 +370,6", RATIFIED,
  "The commit's own account is \"Ruling 39's delegation is written verbatim\", performed on the "
  "user's Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md`, and it records that the wording "
  "is \"the user's own, approved verbatim\" and that the clause \"and nothing else\" was written. "
  "★ The first class was applied first and does not fire: the hunk ADDS a delegation clause beside "
  "an existing naming, withdraws nothing, and cites no fact read in implementation code. ★ The "
  "commit's own body reports that the ruling's PREDICTED OUTCOME was refuted by measurement; that "
  "refutation is about which register entries the delegation reaches and is recorded on the rows, "
  "not in this hunk's text.",
  "governing-decision-record",
  act="the user's Ruling 39 of 2026-08-09 — the exception to the Ruling 38 re-homing default, "
      "naming `cowork_score_census.md` as a document-level delegation whose reach is judged per "
      "section",
  ratification_at="the added text's own \"user-ratified 2026-08-09; the Ruling 39 exception to the "
                  "Ruling 38 re-homing default\"; and the ruling record the commit names, "
                  "`cowork_rulings_2026_08_09_seventh_stop.md`")


# ── 2026-08-11 · the first commissioning sitting's five rulings ───────────────────────────────────
_C5 = "a74c821f891415f42d5aa4f864901ae100c72697"
_C5_ACCOUNT = (
    "The commit's own account is \"Rulings 60–64 of `cowork_rulings_2026_08_11_fourteenth_stop.md`, "
    "read whole (D-643), applied under `cc_instruction_return_continuation_14.md` Task 0\", and all "
    "three `ARCHITECTURE.md` hunks are Ruling 63's — the priority-of-evidence rule homed for the "
    "production arm, the phase-1z scoping note annotated rather than re-worded, and one unqualified "
    "predicate corrected. Its scope line names no `src/` change, no golden, no corpus of scores and "
    "no behaviour change to the analysis.")
_C5_ACT = ("the user's Ruling 63 of 2026-08-11 — the priority-of-evidence rule homed for the "
           "production arm under D-668, the scoping note annotated rather than re-worded (#12), and "
           "the unqualified \"no exception\" corrected to \"no PIECE-START exception\"")
_C5_RAT = ("each added block's own citation of the ruling — \"Ruled by the user, 2026-08-11 "
           "(`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 63, closing `OPEN_ITEMS.md` "
           "OI-324)\" — and that ruling record itself")

w(_C5, "ARCHITECTURE.md", "-384,0 +385,42", RATIFIED,
  _C5_ACCOUNT + " Here the hunk adds the evidential priority the emission is scored under, ruled "
  "ARM-INDEPENDENT, and states why: a premise a live open item puts under load had been stated only "
  "inside a section whose own scoping sentence disclaims describing the shipped analysis. ★ The "
  "first class was applied first and does NOT fire, and the call is recorded because it is close: "
  "the block NAMES a conformance gap in the implementation — \"the pitch and bass emissions reading "
  "the STRUCK set where the design says sounding\". What decides it is that the block ADDS a rule "
  "and withdraws nothing, that its two grounds are the user's own recorded position of 2026-07-28 "
  "and the Layer-2 slice-identity specification, and that the gap is named in the "
  "WHAT-THIS-DOES-NOT-DO clause as DECLARED AND NOT FIXED, with the remedy left to the one design "
  "over the whole family at its #8-correct stage.",
  "governing-decision-record", act=_C5_ACT, ratification_at=_C5_RAT)

w(_C5, "ARCHITECTURE.md", "-4210,0 +4253,18", RATIFIED,
  _C5_ACCOUNT + " Here the hunk adds an ANNOTATION beside the phase-1z scoping note saying what "
  "that note does and does not scope — the MECHANISM, not the evidential ranking — with the note "
  "itself preserved exactly as written (#12) and the excluded reading recorded. ★ The first class "
  "was applied first and does not fire: nothing is withdrawn, the annotation is explicitly chosen "
  "OVER a re-wording, and no fact read in implementation code is its source.",
  "governing-decision-record", act=_C5_ACT, ratification_at=_C5_RAT)

w(_C5, "ARCHITECTURE.md", "-4245 +4305,6", RATIFIED,
  _C5_ACCOUNT + " Here the hunk REPLACES one sentence — \"the priority of evidence, which now has "
  "no exception\" becomes \"which now has no PIECE-START exception\" — with the correction's reason "
  "in its own parenthesis. ★ The first class was applied first and does NOT fire, although a "
  "standing statement IS replaced: the correction's source is stated in the added text and it is "
  "the DOCUMENT'S OWN INCONSISTENCY — a predicate that \"named no argument — no exception TO "
  "WHAT — and which read plainly as contradicting the 'all but one narrow fallback case' sentence "
  "below it\". No fact read in implementation code is cited, and the added text says which "
  "neighbouring sentence establishes the intended reading.",
  "governing-decision-record", act=_C5_ACT, ratification_at=_C5_RAT)

# ── 2026-08-11 · OI-346's marks applied, the idiom half held ──────────────────────────────────────
_MK = "11af13a5729a3b06cb49c3dbfdc76f3509a7ba58"
_MK_ACCOUNT = (
    "The commit's own account is \"OI-346's marks reached at last as a dedicated task — the Jazz "
    "half applied with its establishment, the idiom half HELD because #19 forbids a verdict in "
    "either direction\", executing `cc_instruction_return_continuation_14.md` Task 1. It is the "
    "APPLICATION half of D-497, RATIFIED AMENDMENT A-7, and its scope line names no `src/` change, "
    "no golden, no corpus of scores, no constant moved and no behaviour change to the analysis.")
_MK_ACT = ("the application of D-497 — RATIFIED AMENDMENT A-7, user-ratified 2026-08-04, that every "
           "uncalibrated style constant carries the empirically-unvalidated mark with its "
           "validation path named — tracked at `OPEN_ITEMS.md` OI-346")
_MK_RAT = ("each added block's own \"the §6.6 rule applied, 2026-08-11 (`OPEN_ITEMS.md` OI-346, the "
           "application half of D-497)\"; §6.6 itself, which states the rule and its maintenance; "
           "and D-497's own ratification at the 2026-07 architecture review")

w(_MK, "ARCHITECTURE.md", "-2619,0 +2620,15", RATIFIED,
  _MK_ACCOUNT + " Here the hunk adds the mark on the Jazz chord-scoring constants, with the "
  "validation path named and the one thing a reader could mistake for validation named too — the "
  "Jazz regression check runs the Jazz preset over the Bach chorale corpus, which is not jazz "
  "ground truth. ★ The first class was applied first and does NOT fire, and the call is recorded "
  "because it is close: the block cites the implementation to say WHICH values are marked — the "
  "extension threshold against the default \"the header declares\", and the reduced inversion "
  "bonuses \"set in `tools/batch_analyze.cpp`\" — code this commit did not write. What decides it "
  "is that the block ADDS a mark and withdraws no statement: the citations IDENTIFY the constants "
  "the ratified rule reaches, and the establishment offered is the record's own (§4.1c and the "
  "corpus census), not a fact found in the code.",
  "governing-decision-record", act=_MK_ACT, ratification_at=_MK_RAT)

w(_MK, "ARCHITECTURE.md", "-4172 +4187", RATIFIED,
  _MK_ACCOUNT + " Here the hunk REPLACES the Jazz row of the preset table to carry the "
  "empirically-unvalidated mark and its validation path. ★ The first class was applied first and "
  "does NOT fire although a standing row IS replaced: the six values themselves are unchanged, what "
  "is added is the mark the ratified rule requires, and the source of the change is that rule "
  "rather than a fact read in implementation code.",
  "governing-decision-record", act=_MK_ACT, ratification_at=_MK_RAT)

w(_MK, "ARCHITECTURE.md", "-4176,0 +4192,15", RATIFIED,
  _MK_ACCOUNT + " Here the hunk adds what the mark on that row means and what it does NOT say — "
  "not that the six values are wrong, and not that anything about the analysis moves. ★ The first "
  "class was applied first and does NOT fire, and the call is recorded because the establishment "
  "offered is a MEASUREMENT — §4.1c's recorded consequence that jazz accuracy is not measurable on "
  "the corpora held, measured by the bass-injection experiment. What decides it is that the "
  "measurement is about the CORPORA HELD rather than about our code, that the block ADDS and "
  "withdraws nothing, and that it is offered as the ratified rule's own establishment requirement.",
  "governing-decision-record", act=_MK_ACT, ratification_at=_MK_RAT)

w(_MK, "ARCHITECTURE.md", "-5391,4 +5421,20", RATIFIED,
  _MK_ACCOUNT + " Here the hunk REPLACES §6.6's closing clause — which said the mark was not "
  "applied at HEAD — with how far the application has got, and records the idiom half as HELD "
  "rather than guessed, because #19 forbids a verdict in either direction where no surface maps the "
  "five idiom names onto a per-idiom ground-truth verdict. The former wording stands preserved "
  "(#12). ★ The first class was applied first and does NOT fire although a standing statement IS "
  "replaced: what made it false is THIS COMMIT'S OWN documentation act, not a fact read in "
  "implementation code.",
  "governing-decision-record", act=_MK_ACT, ratification_at=_MK_RAT)

# ── 2026-08-11 · the session-small drain — OI-318's two label defects ─────────────────────────────
_DR = "bf48b1f834afe7b0b71da7473b373e37549e99ea"
_DR_ACCOUNT = (
    "The commit's own account is \"the session-small drain — four gating rows closed\", executing "
    "`cc_instruction_return_continuation_14.md` Task 3, and the three `ARCHITECTURE.md` hunks are "
    "OI-318's two label defects. Its scope line names no `src/` change, no golden, no corpus of "
    "scores and no behaviour change to the analysis.")
_DR_ACT = ("the ratified terminology rename of 2026-07-01, which reserves the bare word for the "
           "accepted melodic phrase alone, applied here to the two places this document breached "
           "it — tracked at `OPEN_ITEMS.md` OI-318 item (1)")
_DR_RAT = ("each added block's own naming of \"the ratified 2026-07-01 rename\" and of the "
           "delegated design's terminology section, which the correction cites as the thing the "
           "breach contradicted")

w(_DR, "ARCHITECTURE.md", "-1111 +1111,11", RATIFIED,
  _DR_ACCOUNT + " Here the hunk records that the document's own account of how far the rename "
  "reached was ONE INSTANCE SHORT, and states what that shows about the enumeration — it was built "
  "by looking for one banned word, so a second banned word was outside what it could find, and its "
  "count is not a bound on how many exist. ★ The first class was applied first and does not fire: "
  "the correction's source is a READ OF THIS DOCUMENT — a second reserved word standing in its own "
  "Layer-6 paragraph — and no fact read in implementation code is cited.",
  "governing-decision-record", act=_DR_ACT, ratification_at=_DR_RAT)

w(_DR, "ARCHITECTURE.md", "-2184,3 +2194,8", RATIFIED,
  _DR_ACCOUNT + " Here the hunk REPLACES the Layer-6 paragraph's three uses of the reserved word "
  "with the punctuation-span, with the former wording preserved in place (#12) and the reason "
  "stated — the paragraph told a reader that the grouping layer segments melodic phrases, \"the one "
  "thing the delegated design's terminology section exists to deny\". ★ The first class was applied "
  "first and does NOT fire although a standing statement IS replaced: the source is the ratified "
  "rename and the delegated design's own terminology section, not a fact read in implementation "
  "code.",
  "governing-decision-record", act=_DR_ACT, ratification_at=_DR_RAT)

w(_DR, "ARCHITECTURE.md", "-8153 +8168,7", RESTRUCTURING,
  _DR_ACCOUNT + " Here the hunk RENUMBERS a section heading: two sections carried the same number, "
  "and neighbouring text cites into that run by number, so a citation did not resolve. ★ The first "
  "class was applied first and does not fire — no statement about the system is made or withdrawn, "
  "and the added parenthesis says in terms that the change \"changes no content and leaves nothing "
  "below it renumbered\". The second does not fire either: the act cites a standing documentation "
  "rule about this document's section numbers rather than recording what any user act ruled. The "
  "third does, this being a re-heading exactly.",
  "document-relocation-or-re-heading")


# ══ THE PASS MOVES OFF `ARCHITECTURE.md`, IN THE ARTIFACT'S OWN ORDER ═════════════════════════════

# ── `cowork_bounded_context_design.md` ────────────────────────────────────────────────────────────
w("d1eadc076cfb7c3923d3742ce74f3b75de4e57b4", "cowork_bounded_context_design.md", "-225 +225,8",
  RATIFIED,
  "The commit's own subject is \"D-278 and D-266 RULED (user 2026-08-02)\", and the added block "
  "opens with its own attribution — \"Dated annotation (user ruling, 2026-08-02, at the D-266 "
  "ratification)\". It records that the Layer-6 gate STANDS and transfers, while the acceptance list "
  "above it is DEPRECATED. ★ The first class was applied first and does NOT fire although a standing "
  "statement IS deprecated: the ground given is the RECORD'S OWN supersession — the list \"names "
  "layers, seams and a corpus gate of the superseded legacy stack (the 53/24/53 batch stop was "
  "itself superseded 2026-07-06)\" — and no fact read in implementation code is cited.",
  "governing-decision-record",
  act="the user's ruling of 2026-08-02 at the D-266 ratification — the Layer-6 gate stands and "
      "transfers to the architecture that ships, its acceptance list deprecated and to be restated "
      "as part of the phase-3 plan",
  ratification_at="the added block's own \"(user ruling, 2026-08-02, at the D-266 ratification)\" "
                  "and its closing \"Register entry D-266 carries this ruling\"; and the commit's "
                  "own subject")

_BC = "d1891db1588d73fbf41789c9139006d269a1c766"
_BC_ACCOUNT = (
    "The three hunks of this commit in this document are ONE correction made in three places, and "
    "the correction's evidence is stated at the first of them: the convergence item's "
    "domain-proxy clause is STRUCK, its former wording preserved verbatim (#12), because \"the one "
    "time it was exercised, measurement disproved it\" and because the as-built does the direct "
    "thing instead — \"the as-built consequence is verified in the production source at the "
    "reach-back loop's own convergence note\", with `regionanalyzer.cpp` named as where the code "
    "states it in its own words. ★ THE FIRST CLASS FIRES ON ALL THREE: each REPLACES a standing "
    "statement of this document, and the source of the replacement is a fact read in implementation "
    "code this commit did not write, together with the measurement that disproved the struck "
    "clause.")

w(_BC, "cowork_bounded_context_design.md", "-65,5 +65,26", CODE_INFLUENCED,
  _BC_ACCOUNT + " This hunk is the strike itself: the licence to substitute a cheaper domain proxy "
  "is withdrawn and replaced by the direct criterion the as-built implements, with the struck "
  "clause quoted in full and the reason the strike reaches the general clause rather than only its "
  "worked example stated with it.",
  "describes-pre-existing-implementation-behaviour")
w(_BC, "cowork_bounded_context_design.md", "-138 +159,5", CODE_INFLUENCED,
  _BC_ACCOUNT + " This hunk carries the same correction into §5's extension-request line — the stop "
  "condition formerly read \"the prevailing key before the selection is in view\", which the added "
  "text names as \"the proxy, not the criterion\" — and states why it is corrected here rather than "
  "left standing: \"a reader reaching §5 first would build the stop condition the strike exists to "
  "remove\".",
  "describes-pre-existing-implementation-behaviour")
w(_BC, "cowork_bounded_context_design.md", "-249,2 +274,4", CODE_INFLUENCED,
  _BC_ACCOUNT + " This hunk carries the same correction into the layer-by-layer summary bullet, "
  "with its own \"Same correction and same ruling as the §5 bullet\" and the former wording "
  "preserved (#12).",
  "describes-pre-existing-implementation-behaviour")

# ── `cowork_confidence_contract.md` ───────────────────────────────────────────────────────────────
w("dfbf3ab824f0717d83cf3cce8e332c69f1074328", "cowork_confidence_contract.md", "-86,0 +87,13",
  RATIFIED,
  "The commit's own account is the away batch's Task 2 — \"nine archive-only decisions moved into "
  "the specifications that own them, D-601's hold ended\" — and this is that one authorized edit. "
  "The added block carries its own attribution: \"user-ratified 2026-07-10; re-homed into this "
  "section 2026-08-08 under a one-edit authorization for this act alone\". ★ The first class was "
  "applied first and does NOT fire, and the call is recorded because the block's defense is a "
  "MEASUREMENT — \"the one calibration attempted so far failed, and it failed non-monotonically\". "
  "What decides it is that the block ADDS a gate and withdraws nothing, and that the failed "
  "calibration is offered as evidence about the PREMISE the gate is placed on rather than as a fact "
  "against which a documentation statement was found false.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-10 that the commensurability premise must itself pass a "
      "premise ledger and a desk simulation before any conversion constant is fitted, re-homed "
      "2026-08-08 under the away batch's Ruling 2",
  ratification_at="the added block's own \"user-ratified 2026-07-10; re-homed into this section "
                  "2026-08-08 under a one-edit authorization for this act alone\"; and the ruling "
                  "record the batch applies, `cowork_rulings_2026_08_08_pre_away.md`")

# ── `cowork_layer3_keymode_design.md` ─────────────────────────────────────────────────────────────
w("f3c7f1afe24668f38b182755e58745f3a4db4aad", "cowork_layer3_keymode_design.md", "-4 +4,17",
  CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES. The hunk QUALIFIES a standing statement of this document — its own "
  "as-built banner — and says so in its heading: \"THE AS-BUILT CLAUSE IMMEDIATELY BELOW IS FALSE "
  "AT HEAD AND ITS FORMER WORDING IS PRESERVED IN PLACE (#12)\". The source is the state of the "
  "implementation this commit did not write: \"all four of this decoder's production call sites sit "
  "in the flag's false branch\", with the joint estimator named as the production key path on both "
  "surfaces. The correction's own closing sentence names the obligation it discharges — the "
  "doc-sync half's first worked example, an as-built banner over a dormant mechanism — and states "
  "that the design content is untouched and nothing in it is withdrawn.",
  "describes-pre-existing-implementation-behaviour")

# ── `cowork_layer6_grouping_design.md` ────────────────────────────────────────────────────────────
w("640d587ab9549904110453b1cbcd362c348de784", "cowork_layer6_grouping_design.md", "-233,0 +234,10",
  RATIFIED,
  "The commit's own subject is \"the homing remainder, opened — D-458 re-homed into the section "
  "that owns its rule, with step 1 checked first and declined\", which is the fixed-order homing "
  "procedure applied. ★ The first class was applied first and does not fire: the block ADDS the "
  "codetta refinement's canonical reading, withdraws nothing, and its defense is the flat/total "
  "partition law this layer is defined by — no fact read in implementation code is cited. ★ ONE "
  "THING IS STATED SO A READER IS NOT MISLED: the decision's own ratifier is COWORK (\"ruled at "
  "ratification, Cowork, 2026-07-02\"), not the user; what carries the user's authority is the "
  "HOMING, under the re-homing default the user ruled on 2026-08-09.",
  "governing-decision-record",
  act="the user's Ruling 38 of 2026-08-09 making re-homing into the owning specification the "
      "default closing route, executed here for D-458",
  ratification_at="the added block's own \"(Homed here 2026-08-11 from the document's own status "
                  "banner, where the ruling was recorded; the banner text is untouched (#12) and "
                  "this section is where the rule now lives.)\"; the ruling's home at `CLAUDE.md`, "
                  "decisions-register rule (l); and `cowork_rulings_2026_08_09_sixth_stop.md`")

# ── `cowork_stage5_fitter_design.md` ──────────────────────────────────────────────────────────────
w("1b8ecaf685295024cdeafee067332ca38b26be04", "cowork_stage5_fitter_design.md", "-108,0 +109,11",
  CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES. The added block's own heading is \"CORRECTION OF STATE\", and what it "
  "corrects is a standing statement of this document: the scope-out line calls the "
  "`chordanalyzer.cpp` file split \"parked by ratified R9\", and the block records that the act "
  "\"was already DELIVERED when this design was written\". The source is the state of the "
  "implementation this commit did not write — \"The split was committed as `41f7c65f63` on "
  "2026-06-17, seventeen days before this design of 2026-07-04\", which the same wave's own account "
  "records as verified at the object. The sentence itself is preserved unedited (#12) and the "
  "scope-out is unaffected in substance, which is why the correction is an annotation rather than "
  "an edit.",
  "describes-pre-existing-implementation-behaviour")

w("bf48b1f834afe7b0b71da7473b373e37549e99ea", "cowork_stage5_fitter_design.md", "-118,0 +119,11",
  CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES. The added remark records that clause (i) of the annotation above "
  "\"ASSERTS THE OPPOSITE OF WHAT D-428 NOW RECORDS\", and the source of the refutation is a check "
  "at the code this commit did not write: D-428 \"was corrected later the same day — at phase 1n, "
  "against the premise AND AT THE CALL SITES — and now records that every use sits on the legacy "
  "arm, so deleting that path discharges them\". The annotation block itself is deliberately left "
  "as written, \"the record of what was believed when it was written\" (#12), which is why the "
  "correction rides beside it; the commit's own account names this as the second of the two "
  "surfaces the earlier correction never reached.",
  "describes-pre-existing-implementation-behaviour")

# ── `cowork_voiceleading_axis_design.md` — a SECTION-SCOPED member (§0, §5.1, §5.3, §8, §9) ───────
w("9fe7f4561f750de4403b9bf9cfe812e474a1a5b3", "cowork_voiceleading_axis_design.md", "-95,2 +95,12",
  CODE_INFLUENCED,
  "INSIDE the delegated sections: the hunk sits in §0's accepted-music-theory subsection, and rule "
  "(h) reaches a named section's subsections. ★ THE FIRST CLASS FIRES. The hunk REPLACES a standing "
  "statement of this document — the bullet formerly closed \"whether 'interval preserved' is "
  "counted in semitones or in diatonic generic size is an implementation declaration owed at build\" "
  "— and the added text states that this \"was true when written and is FALSE at HEAD\". The source "
  "is the implementation: the convention \"was read off the exploratory study's own motion "
  "classifier at source and reproduced exactly in the production classification, which is "
  "oracle-tested against it\". The commit's own account calls it in terms \"a doc-sync correction "
  "(C3)\".",
  "describes-pre-existing-implementation-behaviour")

_VL = "f3c7f1afe24668f38b182755e58745f3a4db4aad"
_VL_OUTSIDE = (
    "OUTSIDE THE DELEGATED SECTIONS, so it is RECORDED and NOT GRADED. This member's delegation "
    "names §0, §5.1, §5.3, §8 and §9; the section boundaries were derived from the document's own "
    "headings at this commit's own blob and the hunk's post-image line range placed against them. ")

w(_VL, "cowork_voiceleading_axis_design.md", "-6 +6,4", OUTSIDE_SECTIONS,
  _VL_OUTSIDE + "This hunk sits at the head of the document, ABOVE §0 — in the status banner — so "
  "no named section reaches it and the four classes are not applied to it.")
w(_VL, "cowork_voiceleading_axis_design.md", "-77,2 +80,12", RATIFIED,
  "INSIDE the delegated sections: the hunk sits in §0's own preamble, between that heading and its "
  "first subsection. The hunk REPLACES the corpus-gate term's definition — the batch case-identity "
  "sets give way to the robust unit, with the former wording preserved (#12) and the reason stated: "
  "the stale sentence \"is not a description of the past, it is an ACCEPTANCE CRITERION a future "
  "build would try to satisfy\". ★ The first class was applied first and does NOT fire although a "
  "standing statement IS replaced: the source is the RECORD'S OWN supersession — the batch stop "
  "\"SUPERSEDED IN WHOLE at R10-b on 2026-07-06\" — and no fact read in implementation code is "
  "cited.",
  "governing-decision-record",
  act="the R10-b ratification of 2026-07-06, at which the robust-unit stop superseded the batch "
      "case-identity gate in whole, applied here as a doc-sync correction of a stale acceptance "
      "criterion",
  ratification_at="the added text's own naming of `CLAUDE.md` gate block (A) as the one authority "
                  "and of block (C) as retaining the superseded gate historically; and gate block "
                  "(A)'s own \"Ratified at R10-b (2026-07-06)\"")
w(_VL, "cowork_voiceleading_axis_design.md", "-219,2 +232,5", OUTSIDE_SECTIONS,
  _VL_OUTSIDE + "This hunk sits in §2, Constraints, which the delegation does not name.")
w(_VL, "cowork_voiceleading_axis_design.md", "-571,3 +587,7", OUTSIDE_SECTIONS,
  _VL_OUTSIDE + "This hunk sits in §10, Quality & testing, which the delegation does not name.")

# ── `cowork_phrase_boundary_design.md` ────────────────────────────────────────────────────────────
_PB = "f007bc473b03643f31e33fde661d2182381d3139"
_PB_ACCOUNT = (
    "The commit's own subject is \"two entries re-homed inside their own specification\", performed "
    "under the re-homing default the user ruled on 2026-08-09. ★ The first class was applied first "
    "and does not fire on either hunk: both ADD and neither withdraws a standing statement of this "
    "document.")
_PB_ACT = ("the user's Ruling 38 of 2026-08-09 making re-homing into the owning specification the "
           "default closing route, executed here for two of this primitive's own entries")
_PB_RAT = ("the ruling's home at `CLAUDE.md`, decisions-register rule (l), and the ruling record "
           "`cowork_rulings_2026_08_09_sixth_stop.md`; and the commit's own subject, which names "
           "the act")

w(_PB, "cowork_phrase_boundary_design.md", "-82,0 +83,12", RATIFIED,
  _PB_ACCOUNT + " This hunk adds that the primitive is a DERIVED VIEW inheriting the loaded span "
  "and requesting no extension of its own, and that its published boundary strength is a "
  "per-profile max-normalised confidence participating in no override frame. Both defenses are "
  "structural — a second extension policy beside its consumers' would be a #6 violation, and a "
  "quantity not comparable across scores may not overrule one that is — with no fact read in "
  "implementation code cited.",
  "governing-decision-record", act=_PB_ACT, ratification_at=_PB_RAT)
w(_PB, "cowork_phrase_boundary_design.md", "-192,0 +205,15", RATIFIED,
  _PB_ACCOUNT + " This hunk adds the requirement that every picked boundary carries which cue fired "
  "and at what scope. ★ The call is recorded because it is close: the block names a DEFECT in what "
  "is built — \"The picked set is SCOPE-BLIND today\", a per-voice marker spiked onto the texture "
  "profile so a consumer cannot tell a local breath from a global barline. What decides it is that "
  "the block ADDS a requirement and withdraws nothing, and that it states in terms that it is NOT "
  "BUILT and changes nothing on the gate repertoire.",
  "governing-decision-record", act=_PB_ACT, ratification_at=_PB_RAT)

# ── `cowork_layer5_function_design.md` ────────────────────────────────────────────────────────────
_LF = "92371a01b8737976d44d0c9aaece36c6284c8f4e"
_LF_ACCOUNT = (
    "The commit's own subject is \"phase 1s — … and D-341 moved to the section it amends\", and the "
    "moved text carries its own attribution: \"Homed here 2026-08-03 on the user's ruling, "
    "`OPEN_ITEMS.md` OI-295 … moved unchanged, never rewritten, #12. Register entry D-341.\" The "
    "move's own reason is stated with it: the rule had been recorded in §15, \"a section that "
    "records findings\", while §5.0 is where the layer states the rule it amends (#7).")
_LF_ACT = ("the user's ruling of 2026-08-03 at `OPEN_ITEMS.md` OI-295, moving the grammar-completion "
           "amendment from the findings-recording open-items section into §5.0, the section it "
           "amends — register entry D-341")
_LF_RAT = ("the moved text's own \"Homed here 2026-08-03 on the user's ruling, `OPEN_ITEMS.md` "
           "OI-295\" and the §15 stub's \"Ruled by the user 2026-08-03\"; and the amendment's own "
           "\"RATIFIED by the user 2026-07-03\", which the move carries unchanged")

w(_LF, "cowork_layer5_function_design.md", "-203 +203,2", RATIFIED,
  _LF_ACCOUNT + " This hunk REPLACES the amendment's label line, the §15 cross-reference giving way "
  "to the amendment's own name together with how it was found and when the user ratified it. ★ The "
  "first class was applied first and does not fire: no fact read in implementation code is its "
  "source, and the spec-ahead-of-code state it names is carried forward unchanged.",
  "governing-decision-record", act=_LF_ACT, ratification_at=_LF_RAT)
w(_LF, "cowork_layer5_function_design.md", "-208 +209,2", RATIFIED,
  _LF_ACCOUNT + " This hunk adds the characterization the move carries with the rule — that the "
  "three added root motions are \"algorithmic completion per theory, NOT tuning\". ★ The first "
  "class was applied first and does not fire: the ground is theory, the added words are moved "
  "unchanged from §15, and nothing standing is withdrawn.",
  "governing-decision-record", act=_LF_ACT, ratification_at=_LF_RAT)
w(_LF, "cowork_layer5_function_design.md", "-211 +213,8", RATIFIED,
  _LF_ACCOUNT + " This hunk adds the amendment's EVIDENCE and the homing note. ★ The first class "
  "was applied first and does NOT fire, and the call is recorded because the evidence is pinned in "
  "the code — \"the 6-entry/11-motion failure table, measured, enumerated and pinned in the "
  "consumer's consistency test (`EXPECT_EQ(failing.size(), 11u)`)\". What decides it is that the "
  "text is MOVED UNCHANGED from §15 of this same document, so nothing is corrected against the "
  "implementation here: the pin is the amendment's own recorded evidence travelling with it.",
  "governing-decision-record", act=_LF_ACT, ratification_at=_LF_RAT)
w(_LF, "cowork_layer5_function_design.md", "-226 +235", RESTRUCTURING,
  _LF_ACCOUNT + " This hunk RE-POINTS one cross-reference — \"the ruled grammar gaps of §15-12\" "
  "becomes \"the ruled grammar gaps of the amendment above\" — and nothing else. ★ The first class "
  "was applied first and does not fire: no statement about the system changes. The second does not "
  "fire AT THIS HUNK'S OWN TEXT: the added words name no act, the ruling being recorded at the two "
  "hunks that carry the move. The third does, this being a re-pointing forced by a relocation.",
  "document-relocation-or-re-heading")
w(_LF, "cowork_layer5_function_design.md", "-888,12 +897,8", RATIFIED,
  _LF_ACCOUNT + " This hunk REPLACES §15's item 12 with the record that the rule MOVED, keeping the "
  "entry only \"so the tracking history and the cross-references to 'item 12' still resolve\" and "
  "deliberately not restating the rule (#6). ★ The first class was applied first and does not fire: "
  "what is withdrawn is a DUPLICATE of text that moved within the same document, and the source is "
  "the user's ruling the added text names.",
  "document-relocation-or-re-heading", act=_LF_ACT, ratification_at=_LF_RAT)


# ── `cowork_evidence_inventory.md` ────────────────────────────────────────────────────────────────
#
# ★ ONE LINE OF THE INHERITED METHOD IS EXERCISED HERE FOR THE FIRST TIME IN THIS DOCUMENT AND IS
# STATED ONCE RATHER THAN AT EVERY VERDICT.  The second class asks whether the change records WHAT A
# NAMED USER ACT RULED, RATIFIED OR DIRECTED — the CONTENT being what the act settled.  A user
# direction to PERFORM a survey is not that: the act is directed, and what the survey then finds is
# its own.  So a homing act, whose content is a decision the register already holds, is a
# ratified-act edit; a catalog of what our own layers publish, silo, trap and leave dormant, made at
# the user's direction, is not — its content is read off this system.
w("fe985ab04757dc9eb214ed12664001fa5156238e", "cowork_evidence_inventory.md", "-0,0 +1,216",
  UNDETERMINED,
  "The hunk CREATES this document whole. ★ The first class was applied first and does NOT fire: "
  "nothing existed here to withdraw, narrow, qualify or replace. ★ The second does not fire either, "
  "on the line stated above the block: the user's direction, quoted in the document's own preamble, "
  "is to \"enumerate ALL the hints/clues each layer discovers that should be passed forward\" — a "
  "directed ACT whose findings are the document's content, not a decision whose content the user "
  "settled. ★ Nor the third: growth qualifies only where its source is not a fact read in "
  "implementation code, and here the source IS that, by construction. The catalog's own status "
  "vocabulary is a vocabulary of implementation states — PUBLISHED on a layer's output surface "
  "today, SILOED or TRAPPED, DORMANT because built and gated off — and its stated sources are \"the "
  "five certified audits (which dispositioned every published/siloed/trapped fact), the siloed-facts "
  "sweep, the diagnosis, the mechanism report\". NOT CLEARED, on the not-cleared class's own first "
  "branch, and reported whole.",
  "describes-pre-existing-implementation-behaviour")

w("3966502265254dbfe721a3607b1b3c50116e030d", "cowork_evidence_inventory.md", "-32 +32,8",
  UNDETERMINED,
  "The hunk REPLACES the rests-and-silences bullet with a fuller entry. ★ The first class was "
  "applied first and does NOT fire: the standing statement is not withdrawn — it survives inside "
  "the longer bullet — so what happened is elaboration rather than replacement. ★ BUT IT IS NOT "
  "CLEARED. The added substance is read off the implementation: the dormant phrase-boundary view "
  "\"is already a silence-based phrase-end detector, gated off, with 'sufficiently long' a hand-set "
  "240-tick threshold (one of the OI-87 unfit constants)\". A fact in the implementation is the "
  "source while the change adds material.",
  "describes-pre-existing-implementation-behaviour")

w("0bc49b4b48fe5b23413a82f71c906fcf3038f91d", "cowork_evidence_inventory.md", "-205,0 +206,9",
  RATIFIED,
  "The hunk adds §8b, naming the intonation feature a declared future consumer of the published "
  "analysis facts. ★ The first class was applied first and does not fire: the block ADDS and "
  "withdraws nothing, and no fact read in implementation code is cited. ★ The second fires, and the "
  "distinction stated above the block is what admits it: the CONTENT here is what the user named — "
  "the section's own heading is \"A declared future consumer, NAMED BY THE USER (2026-07-13)\" — "
  "rather than the findings of a directed survey.",
  "governing-decision-record",
  act="the user's decision of 2026-07-13 that the intonation feature is a declared future consumer "
      "of the analysis facts, held long-horizon",
  ratification_at="the added section's own heading, \"A declared future consumer, named by the user "
                  "(2026-07-13)\", and the register row it names, `OPEN_ITEMS.md` OI-62")

_EX = "0922e2bfdcd72563b05f8754e7c1e67eb0136718"
w(_EX, "cowork_evidence_inventory.md", "-206 +206", RESTRUCTURING,
  "The hunk changes ONE heading from the singular to the plural — \"A declared future consumer\" "
  "becomes \"Declared future consumers\" — because a second one is added below it in the same "
  "commit. ★ The first class was applied first and does not fire: no statement about the system is "
  "made or withdrawn. The second does not fire at this hunk's own text, which records no act. The "
  "third does, this being a re-heading exactly.",
  "document-relocation-or-re-heading")

w(_EX, "cowork_evidence_inventory.md", "-214,0 +215,11", RATIFIED,
  "The hunk adds the second declared future consumer — explainability, \"the end user may want to "
  "know HOW a mode, chord, or function was inferred\", attributed in its own opening to \"(user, "
  "2026-07-13)\". ★ The first class was applied first and does NOT fire, and the call is recorded "
  "because it is close: the block names what exists in the implementation today — \"the "
  "chord-diagnosis replay, the dormant function machinery's structured open marks and ambiguity "
  "kinds, the ranked-candidates-plus-margins confidence contract\". What decides it is that the "
  "block ADDS and withdraws nothing, and that those internals are named as WHY the feature is a "
  "late-bound display consumer rather than a new analysis — the reason for the user's own "
  "characterization, not a fact that found a documentation statement false.",
  "governing-decision-record",
  act="the user's naming of explainability, on 2026-07-13, as a declared future consumer of facts "
      "that already exist rather than as a new analysis",
  ratification_at="the added block's own \"(user, 2026-07-13)\" and the heading above it, which the "
                  "same commit pluralizes to carry this second consumer")

w("e02bbebf887274edd119bf72cd0f6aa1763f34dc", "cowork_evidence_inventory.md", "-225,0 +226,24",
  UNDETERMINED,
  "The hunk adds §8c, filing OPEN the question whether the key layer should consume an external "
  "local key as an unvalidated second opinion, and stating where the question comes from. ★ The "
  "first class was applied first and does NOT fire: the block ADDS and withdraws nothing here. "
  "★ BUT IT IS NOT CLEARED, and the shape says which kind of not-cleared it is. This is the "
  "documentation half of a code change made in the SAME commit — the commit is a `fix(tools)` whose "
  "subject is \"remove the music21 corroborator's dead local-key block; the evidence question stays "
  "open\" — so the block is influenced by facts in the code by construction: the named class \"does "
  "not exist in music21 9.9.1\", \"the constructor always raised, the exception was swallowed, and "
  "every committed region was produced at the global key\". It destroys no discrepancy, because "
  "documentation and implementation moved together in one authored act, and it is reported in the "
  "not-cleared class rather than waved through.",
  "same-commit-code-documentation")


# ══ THE PASS CONTINUED A SECOND TIME, 2026-08-22 (`cc_instruction_pass_continuation_second.md`
#    Task 1, under Ruling 1 of `cowork_rulings_2026_08_22_dispatch_order_sitting.md`).  The remainder
#    was DERIVED FRESH from this artifact's own unread default, in the artifact's own order — by
#    document, then by commit, then by changed passage — and never from the previous batch's account
#    of it.  The inherited method and no other: the four classes in their DECLARED ORDER, POSITIVELY
#    CODE-INFLUENCED applied FIRST, so that a ratified act cannot launder a correction made under it.
#    No verdict already in this block is re-read or re-graded. ══════════════════════════════════════

# ── `cowork_joint_estimator_architecture.md` ──────────────────────────────────────────────────────
w("06d4318bd1f322d055d04622681587c44a01bffb", "cowork_joint_estimator_architecture.md",
  "-0,0 +1,139", RATIFIED,
  "The hunk is the whole document as it first enters git. Its title is \"Ratified architecture — the "
  "key/mode/chord estimator is JOINT (option A)\", its opening line is \"**Decision (user-ratified "
  "2026-07-14).**\", its §6 is \"Recorded at the user's request after the ratification\", and its §7 "
  "is \"Plan amendments (Cowork, 2026-07-18, user-directed)\", each amendment carrying its own "
  "register row. The commit's own subject is \"docs: ratify principles #20-#24 + joint-estimator "
  "plan amendments (OI-176...OI-181), user-ratified 2026-07-18\", and its body names this file's "
  "\"section 5 amendment, section 6 recorded assessment, section 7 plan amendments\" among the "
  "ratified edits it commits. ★ The first class was applied first and does NOT fire although the "
  "document SUPERSEDES the incremental key-layer framing of `cowork_key_layer_design_opening.md`: "
  "the source of that supersession is the user's ratification of 2026-07-14 on the grounding review "
  "and the published literature the text cites, not a fact read in implementation code this commit "
  "did not write. The findings about our own system it names — OI-175's ad-hoc iteration, the "
  "OI-168/OI-170 collection-membership form — are register rows the record already holds, cited as "
  "the reason the in-flight items become parts of A; neither the added text nor the account states a "
  "documentation statement corrected against the implementation.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-14 that key, mode and chord are inferred by ONE joint "
      "estimate, together with the 2026-07-18 recorded assessment and the six user-directed plan "
      "amendments (OI-176…OI-181)",
  ratification_at="the document's own title and its opening \"Decision (user-ratified 2026-07-14)\", "
                  "its §6 and §7 attributions and its closing provenance paragraph; the commit's own "
                  "subject and body; and register entry D-001 at `ARCHITECTURE.md`")

w("910a998e9b5c52383e6accb2460007178070352a", "cowork_joint_estimator_architecture.md",
  "-71 +71,120", RATIFIED,
  "The hunk REPLACES §5's standing list of undecided questions with a decided/remaining split and "
  "adds §5a, five design decisions each carrying \"(user-ratified 2026-07-19)\" in its own opening, "
  "under a starred line recording the factorization specification as user-ratified the same day. The "
  "commit's own account states it: \"five design decisions plus the factorization specification were "
  "user-ratified 2026-07-19\". ★ The first class was applied first and does NOT fire, and the call "
  "is recorded because it is close: the added text DOES name implementation code this commit did not "
  "write — `buildChordResult`'s degree, Gate G-E's degree condition, `applyTonicPriorToSparseChord`, "
  "the segmenter's head-gap tonic prior, the four inequivalent `diatonicToKey` definitions, and the "
  "−7 declared-mode wall. What decides it is that every one of those is named as a CONSEQUENCE of "
  "the ratified design — terms that \"dissolve by construction\", a defect class \"never rebuilt\", "
  "a wall \"formally retired\" — rather than as a fact against which a documentation statement was "
  "found false; the replacement's source is the ratification the added text names five times.",
  "governing-decision-record",
  act="the five joint-estimator design decisions the user ratified on 2026-07-19 — the two-mode "
      "axis with modal colour in the emission, the staged fitting, the scale-degree-valued chord "
      "state, the emission-internal non-chord-tone handling, and the weak soft signature and "
      "declared-mode prior",
  ratification_at="each decision's own \"(user-ratified 2026-07-19)\" inside the added text; the "
                  "commit's own account; and register entries D-524…D-528, whose home is this "
                  "document's §5a")

# ── `cowork_joint_estimator_factorization.md` ─────────────────────────────────────────────────────
w("910a998e9b5c52383e6accb2460007178070352a", "cowork_joint_estimator_factorization.md",
  "-0,0 +1,173", RATIFIED,
  "The hunk is the whole specification as it first enters git. Its title ends \"(★ USER-RATIFIED "
  "2026-07-19)\" and its opening line is \"**Ratified by the user 2026-07-19**\", naming section by "
  "section what is ratified; its standing paragraph adds that ratifying the document ratifies the "
  "structure and the premise ledger while all VALUES remain unfit. The commit's own account states "
  "\"The factorization specification (cowork_joint_estimator_factorization.md) is ratified the same "
  "day\". ★ The first class was applied first and does NOT fire: the document is created here and "
  "withdraws nothing the documentation stated, and the facts about our own system it cites — the "
  "OI-168 signature-mask form for the collection question, the event partition already used as the "
  "analyzer's slice unit — are named as the derived FORM of a factor, from the published theory the "
  "text cites, not as facts against which a documentation statement was found false.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-19 of the factorization specification — the variable "
      "structure, the score form, the ten-factor roster, the premise ledger P1–P8, the decode plan "
      "and the desk-simulation forms and case list",
  ratification_at="the document's own title and opening line; the commit's own account; and register "
                  "entry D-565, whose home is this document's §5")

_DSIM = "31b3dba6cabf87bac0dad2a0c0b95ef3d6fe30fd"
_DSIM_ACCOUNT = (
    "The commit's own subject is \"docs: the factorization desk simulation — run, ratified; "
    "granularity amendment; prior settled initial-only; OI-181 closed\"; its body states that the "
    "desk simulation \"is RUN and USER-RATIFIED\", that the one under-determination it found was "
    "\"AMENDED with ratification\", that the prior question was \"Also settled with ratification\", "
    "and it closes \"All content user-ratified 2026-07-19 in the Cowork session\". ★ The first class "
    "was applied first at every hunk of this commit and fires at none: a desk simulation under "
    "#17(c) traces the mechanism by hand through the INTENDED architecture, at identity weights and "
    "at table values the record declares provisional, so its facts come from the specification and "
    "from the corpus data rather than from implementation code — and neither the added text nor the "
    "account states a documentation statement corrected against the implementation.")
_DSIM_RUN_ACT = ("the user's ratification of 2026-07-19 of the factorization desk simulation and its "
                 "findings")
_DSIM_RUN_RAT = ("the added text's own \"user-ratified (2026-07-19, same day — "
                 "`cowork_factorization_desk_simulation.md`)\"; the commit's own account; and "
                 "register entry D-453, whose home is `cowork_factorization_desk_simulation.md` §7")
_DSIM_GRAN_ACT = ("the factor-granularity amendment the user ratified on 2026-07-19 at the desk "
                  "simulation")
_DSIM_GRAN_RAT = ("the added block's own \"(amendment, user-ratified 2026-07-19 at the desk "
                  "simulation — `cowork_factorization_desk_simulation.md` §4.1, the "
                  "`bwv10.7@36000` length-bias finding)\"; the commit's own account; and register "
                  "entry D-449")
_DSIM_PRIOR_ACT = ("the user's ratification of 2026-07-19, at the desk simulation's §4.2 S3 and C5 "
                   "traces, that the signature and declared-mode prior conditions the INITIAL key "
                   "state only")
_DSIM_PRIOR_RAT = ("the added text's own \"SETTLED (user-ratified 2026-07-19 at the desk simulation, "
                   "its §4.2 — the S3/C5 traces)\"; the commit's own account; and register entry "
                   "D-450")

w(_DSIM, "cowork_joint_estimator_factorization.md", "-5,2 +5,5", RATIFIED,
  _DSIM_ACCOUNT + " This hunk replaces the header's forward-looking next-stage sentence with the "
  "record that the §6 desk simulation has RUN, that its findings are user-ratified the same day, "
  "that nine of ten traces pass as specified, and that the two amendments it produced are "
  "incorporated below with dated marks.",
  "governing-decision-record", act=_DSIM_RUN_ACT, ratification_at=_DSIM_RUN_RAT)

w(_DSIM, "cowork_joint_estimator_factorization.md", "-58,0 +62,11", RATIFIED,
  _DSIM_ACCOUNT + " This hunk adds the factor-granularity rule to §2 — the pitch and spelling "
  "emissions per tone, the bass factor per event, the missing-template-tone penalty normalized per "
  "event of segment length, the transition, entry and boundary factors per boundary or event — with "
  "the finding that forced it named in its own opening. Nothing standing is withdrawn: the "
  "specification had been silent on granularity, which the amendment itself calls under-specified.",
  "governing-decision-record", act=_DSIM_GRAN_ACT, ratification_at=_DSIM_GRAN_RAT)

w(_DSIM, "cowork_joint_estimator_factorization.md", "-77 +91,2", RATIFIED,
  _DSIM_ACCOUNT + " This hunk carries the same ratified amendment into factor 3's own description: "
  "the bass and inversion factor gains \"**Evaluated per event within the segment (the 2026-07-19 "
  "granularity amendment, §2).**\" It QUALIFIES a standing statement, and the source of the "
  "qualification is the amendment §2 now carries.",
  "governing-decision-record", act=_DSIM_GRAN_ACT, ratification_at=_DSIM_GRAN_RAT)

w(_DSIM, "cowork_joint_estimator_factorization.md", "-112,2 +127,6", RATIFIED,
  _DSIM_ACCOUNT + " This hunk REPLACES factor 10's open clause — \"the persistent-pull variant is a "
  "desk-simulation question\" — with the settlement: the prior conditions the initial key state "
  "only, re-entering at a notated mid-piece signature change, and the persistent-pull variant is "
  "rejected. ★ The near-miss is recorded because the rejection's stated ground names a measured "
  "defect of our own system, that persistent pull would softly re-introduce the OI-174 "
  "signature-pull bias. What decides it is that the row is offered as the DESIGN reason the rejected "
  "variant is undesirable — beside a theory ground, that it is a linearly growing tax with no theory "
  "basis — and not as a fact against which a documentation statement was found false.",
  "governing-decision-record", act=_DSIM_PRIOR_ACT, ratification_at=_DSIM_PRIOR_RAT)

w(_DSIM, "cowork_joint_estimator_factorization.md", "-142,0 +162,5", RATIFIED,
  _DSIM_ACCOUNT + " This hunk adds the marked block above §6 — \"STAGE RUN AND RATIFIED "
  "(2026-07-19)\" — recording that the simulation was executed on paper as specified, its outcome, "
  "the one specification under-determination found and amended, the settled prior question, and that "
  "OI-181 is discharged. It adds and withdraws nothing.",
  "governing-decision-record", act=_DSIM_RUN_ACT, ratification_at=_DSIM_RUN_RAT)

w(_DSIM, "cowork_joint_estimator_factorization.md", "-169,2 +193,2", RATIFIED,
  _DSIM_ACCOUNT + " This hunk WITHDRAWS one item — the persistent-versus-initial signature prior — "
  "from the standing list of questions left open at ratification, and records in a parenthetical "
  "that the desk simulation settled it as forecast, pointing the reader at §3.10. The withdrawal's "
  "source is the settlement the §3.10 hunk of this same commit records, ratified the same day.",
  "governing-decision-record", act=_DSIM_PRIOR_ACT, ratification_at=_DSIM_PRIOR_RAT)

w("73c84b92d3fd3ba1a678ab90236bb40d99a97926", "cowork_joint_estimator_factorization.md",
  "-148,0 +149,7", RATIFIED,
  "The hunk adds the below-threshold scoring rule — where a fitted table row stores a pooled "
  "leftover for continuations below the count-reliability threshold, a specific such continuation is "
  "scored as that leftover apportioned in proportion to the outcome class's overall frequency in the "
  "mode, \"never by even division and never as zero\" — carrying its own attribution "
  "\"(user-ratified 2026-07-19 at the fitted-table probe, `cowork_sensitive_cell_probe.md` finding "
  "2, option 2a)\". The commit's own subject names the ratified probe findings it lands. ★ The first "
  "class was applied first and does NOT fire: the block ADDS a rule and withdraws nothing, and its "
  "evidence is a probe over tables counted from the ground truth — the applied contexts that had "
  "collapsed to the mode unigram — not a fact read in implementation code this commit did not write.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-19, at the fitted-table probe, of the below-threshold "
      "back-off scoring rule (finding 2, option 2a)",
  ratification_at="the added block's own attribution; the commit's own subject; and register entry "
                  "D-533")

w("869e75e0a0cdeff78922b7d8f496d14d2f103f3c", "cowork_joint_estimator_factorization.md",
  "-148,0 +149,10", RATIFIED,
  "The hunk adds the exact-score tie-break — fewer segments first, then the earliest boundary-tick "
  "sequence, then the canonical class-key order of the state sequence, \"No epsilon, no platform "
  "dependence\" — carrying its own \"(user-ratified 2026-07-20 at the C++ module build's parity "
  "finding)\". The commit's own account names it \"§5 TIE-BREAK "
  "(cowork_joint_estimator_factorization.md §5, user-ratified 2026-07-20)\". ★ The first class was "
  "applied first and does NOT fire, and the call is recorded because it is the closest of this "
  "document's: the rule's OCCASION is a fact established by RUNNING a decoder — equal-score "
  "segmentations proven at corpus pieces, and a cross-language summation drift that flips "
  "tie-adjacent boundary decisions — and the pre-existing probe decoder is code this commit did not "
  "write. What decides it is that the block ADDS a rule where the specification carried no tie "
  "policy at all, so nothing standing is withdrawn, narrowed or qualified; and that the rule's "
  "source is the user's ratification of 2026-07-20, dated five days before this commit, which both "
  "the added text and the account name — the measured facts being the reason a tie policy is owed "
  "rather than a fact against which a documentation statement was found false.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-20 of the declared TOTAL ORDER on paths that resolves "
      "exact score ties identically in every decoder of this specification",
  ratification_at="the added block's own \"(user-ratified 2026-07-20 at the C++ module build's "
                  "parity finding)\"; the commit's own account; and register entry D-565, whose home "
                  "is this document's §5")

# ── `cowork_notation_adoption_increment.md` ───────────────────────────────────────────────────────
w("00c0df81c5682fbda0515a81cea0c3c541e8ee23", "cowork_notation_adoption_increment.md",
  "-0,0 +1,482", RATIFIED,
  "The hunk CREATES this decision surface whole. Its title ends \"(★ USER-RATIFIED 2026-07-26)\", "
  "its opening block is \"★ RATIFIED BY THE USER 2026-07-26, as asked in §9\" and names each "
  "ratified item — the §2 principles amendment and the five recommendations A2, B-full, C1, D1 and "
  "E — and its author line reads \"Cowork, 2026-07-26, at the user's direction\". The commit's own "
  "subject is \"ratification record: notation-layer adoption increment decision surface + the "
  "decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194\". ★ The first "
  "class was applied first and does NOT fire: the document is created here, so nothing existed to "
  "withdraw, narrow, qualify or replace, and neither the added text nor the account states a "
  "documentation statement corrected against the implementation. ★ THE SECOND CLASS WAS TESTED "
  "AGAINST THE LINE THIS BLOCK ALREADY CARRIES — a catalog made at the user's direction, whose "
  "content is read off this system, is NOT a ratified-act edit — and it FIRES here for the reason "
  "that line turns on: the user's act was a RATIFICATION of five named recommendations and a "
  "principles amendment, whose content the user settled, and the document is that ratification's "
  "record. Its §1, \"The verified current state (all read at source this session)\", IS a read of "
  "implementation code this commit did not write; it is the surface's evidence base, one section of "
  "nine, and it withdraws nothing.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-26 of the notation-layer adoption increment's decision "
      "surface — the §2 principles amendment (the decision-neutrality corollary) and all five "
      "recommendations, A2, B-full, C1, D1 and E",
  ratification_at="the document's own title and its opening \"★ RATIFIED BY THE USER 2026-07-26, as "
                  "asked in §9\", and its §9 rulings section; the commit's own subject; and register "
                  "entries D-424, D-425 and D-426, whose home is this document")

w("5f3362f35992371c522ef1649f94598c97ac124a", "cowork_notation_adoption_increment.md",
  "-481,2 +481,36", CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES, on its SECOND limb, in the added text's own word. The hunk adds §10 and "
  "states that the consumption audit's scope check \"corrected this document's §1 three ways, now "
  "record\", then gives the three: there is a SECOND notation entry point, the single-note surface, "
  "consumed by `notationinteraction.cpp:8311` and `notationcontextmenumodel.cpp:194`, where §1 had "
  "said the in-app analysis enters through ONE function; the function-labeling layer is DORMANT, "
  "with the live section reads named as `sectionanalyzer.cpp` and `sectioncadencedetection.cpp`; "
  "and accessibility consumes only the pre-formatted annotation string. Every one of those is a "
  "fact read in implementation code this commit did not write, and the change's own account states "
  "that a documentation statement was corrected against it. ★ The hunk ALSO records the P1 "
  "pedal-point ruling, \"user-ratified 2026-07-26, with the user's voice-independence sharpening\" "
  "— and that is exactly why the declared order puts the first class first: a ratified act in the "
  "same passage does not launder a correction made under it, so the correction governs the verdict "
  "and the ratification is reported here rather than in the class it would otherwise reach.",
  "describes-pre-existing-implementation-behaviour")

# ── `cowork_notation_output_contract.md` ──────────────────────────────────────────────────────────
_NOC_IN = (
    "INSIDE the delegated sections. This member's delegation names §2, §3.1, §3.2, §3.3 and §3.4; "
    "the section boundaries were derived from the document's own headings at this commit's own blob "
    "and the hunk's post-image line range placed against them. ")

w("5f3362f35992371c522ef1649f94598c97ac124a", "cowork_notation_output_contract.md",
  "-0,0 +1,220", RATIFIED,
  _NOC_IN + "The hunk CREATES the contract whole, so its range covers all five named sections. Its "
  "title ends \"(★ USER-RATIFIED 2026-07-26)\" and its opening line is \"★ RATIFIED BY THE USER "
  "2026-07-26, as asked in §8 — as specified, no amendments.\"; its author line reads \"Cowork, "
  "2026-07-26, at the user's 'go' after the P1 pedal ruling\". The commit's own subject names the "
  "contract as one of the two ratifications it records. ★ The first class was applied first and "
  "does NOT fire, and the call is recorded because the document names live implementation seams — "
  "\"today `analyzeHarmonicRhythm` → `HarmonicRegion` vector\", \"today "
  "`analyzeNoteHarmonicContext[Details]`\" — and takes the consumption audit as its exhaustiveness "
  "basis. What decides it is that the document is created here, so nothing standing is withdrawn, "
  "and that those names appear as the seams the contract must serve rather than as facts against "
  "which a documentation statement was found false. ★ The second class fires and the catalog line "
  "does not bar it: what the user settled here is a SPECIFICATION of what the record shall publish, "
  "ratified as specified, not the findings of a directed survey.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-26, as specified and with no amendments, of the notation "
      "output-surface contract — the A-native record the in-app notation path reads",
  ratification_at="the document's own title and its opening \"★ RATIFIED BY THE USER 2026-07-26, as "
                  "asked in §8 — as specified, no amendments\"; the commit's own subject; and "
                  "register entries D-275 and D-276, whose homes are this document's §2 and §3.4")

w("04fb57ab083d35fb19943c7c11e702d29d29ce51", "cowork_notation_output_contract.md",
  "-92,5 +92,17", RATIFIED,
  _NOC_IN + "The hunk sits inside §3.3, the uncertainty surface. It REPLACES the established "
  "slice's two bullets — the runner-up key with its gap, and the top-N alternative chord classes — "
  "with the full scoreable candidate lists on both axes, and adds the amendment block that "
  "supersedes the former wording in terms. ★ The first class was applied first and does NOT fire, "
  "and the call is recorded because it is close: a standing statement IS superseded, and the block "
  "names the delivered build — \"(commits `9849134f40`/`56439ebad7` — shared label tables + "
  "per-segment full score lists, bit-identical C++ parity)\" — as \"this amendment's form\", which "
  "can be read as reconciling the contract to what was built. What decides it is the ground the "
  "block itself gives for the supersession: a breadth \"N\" or a gap-window width \"would be a "
  "hand-set value with no basis, #1/#19\", and nothing computed may be discarded at the boundary "
  "(#12) — a principled ground, ratified by the user, with the delivered form named as coinciding "
  "with the amendment rather than as a fact that found the contract false.",
  "governing-decision-record",
  act="the user's ratification of option 1 on 2026-07-26, at the posterior-slice delivery — both "
      "axes publish the FULL scoreable candidate lists, with no truncation constant anywhere in the "
      "publication",
  ratification_at="the added block's own \"★ Amendment (user-ratified option 1, 2026-07-26, at the "
                  "posterior-slice delivery)\"; the commit's own subject; and register entry D-006 "
                  "at `ARCHITECTURE.md`")

w("58ac88079be79bfbf6e0f084dc621cf8e457a2a5", "cowork_notation_output_contract.md",
  "-97,0 +98,10", RATIFIED,
  _NOC_IN + "The hunk sits inside §3.3 and ADDS the presentation-derivations amendment: the "
  "record's chord-symbol string is the GRADING form only, while the display chord symbol and the "
  "Nashville number are presentation-layer derivations from published facts, each rendered by one "
  "shared formatter and never published on the record, with a permanent dependency-direction guard "
  "both ways. ★ The first class was applied first and does NOT fire, and the call is recorded "
  "because the commit that carries it WRITES the display carriage it describes and the block's "
  "\"verified fully derivable\" clause rests on a read of the existing formatter. What decides it "
  "is that the amendment carries its own \"(user-ratified 2026-07-26, at the P3a findings)\" and "
  "its own \"user directive at the D2 ruling\", both dated before this commit, and that the "
  "verification is offered as the evidence FOR the ratified boundary rather than as a fact against "
  "which a documentation statement was found false; the commit's account names the amendment as a "
  "riding Cowork edit and states \"NO inference change\".",
  "governing-decision-record",
  act="the user's ratification of 2026-07-26 at the P3a findings that display renderings are "
      "PRESENTATION derivations, with the permanent dependency-direction guard the user directed at "
      "the D2 ruling",
  ratification_at="the added block's own \"★ Amendment (user-ratified 2026-07-26, at the P3a "
                  "findings — display renderings are PRESENTATION derivations)\" and its closing "
                  "\"user directive at the D2 ruling\"; and the commit's own account, which names "
                  "the amendment among its riding Cowork edits and cites this contract's §3.3")

# ── `cowork_prefit_gates.md` ──────────────────────────────────────────────────────────────────────
w("61a8ed750f4ca5ea2465558d69bb1f80045e21cf", "cowork_prefit_gates.md", "-0,0 +1,181", RATIFIED,
  "The hunk CREATES the four pre-fit gates whole. The title ends \"★ USER-RATIFIED 2026-07-19\", the "
  "opening line is \"**Ratified by the user 2026-07-19, as asked:** the four protocols including the "
  "[prov-ratify] constants\", and the standing paragraph adds that ratifying the document ratifies "
  "the four protocols and that changing a protocol constant thereafter is a #22 amendment and not a "
  "tuning act. The commit's own subject is \"docs: the four pre-fit gates ratified — OI-176 CV "
  "protocol, OI-177 capacity budget, OI-178 adoption protocol, OI-180 dual-path sanction\", and its "
  "closing line is \"all content user-ratified 2026-07-19 in the Cowork session\". ★ The first class "
  "was applied first and does NOT fire: the document is created here, so nothing existed to "
  "withdraw, and what it names of our own system — the robust unit's grading substrate, the corpus's "
  "326 pieces resolving to 324 analysis files, the BCMH overlap — are properties of the CORPUS and "
  "of the measurement chain cited to `docs/score_inventory.md`, not facts read in implementation "
  "code, and neither the added text nor the account states a documentation statement corrected "
  "against the implementation.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-19 of the four pre-fit gates — the held-out evaluation "
      "protocol, the capacity budget, the robust-stop architecture-adoption protocol and the "
      "dual-path sanction with its retirement map — including the four constants the document marks "
      "provisional-until-ratified",
  ratification_at="the document's own title and its opening \"Ratified by the user 2026-07-19, as "
                  "asked\"; the commit's own subject and its closing line; and register entries "
                  "D-270, D-271, D-272, D-273 and D-274, whose home is this document")

w("aef4540c0d01676ac4bad326aa78ea141fc91c23", "cowork_prefit_gates.md", "-76,2 +76,6", RATIFIED,
  "The hunk REPLACES the capacity budget's standing cap on the combination-weight vector — \"≤ 12 "
  "weights (one per factor plus the declared-mode strength)\" — with \"≤ 14 weights\", and preserves "
  "the original wording in place (#12) inside its own amendment note. The commit's own account "
  "states \"Both user rulings executed: R1 = W1 … and R2 = C1 (the capacity cap amended <=12 -> "
  "<=14; the weight vector enumerated at 13)\". ★ The first class was applied first and does NOT "
  "fire, and the call is recorded because a standing statement IS replaced in a commit that writes "
  "the fitting instrument. What decides it is the ground the note itself gives: \"the ratified "
  "factorization gives the four cadence features their own fitted weights, putting the enumerated "
  "vector at 12–13\" — a count taken from the ratified SPECIFICATION's factor roster, not a fact "
  "read in implementation code — and the amendment is dated to a user ratification that precedes "
  "this commit.",
  "governing-decision-record",
  act="the user's ruling R2 = C1 of 2026-07-19 at the weight-fit dispatch, amending the capacity "
      "budget's cap on the combination-weight vector from twelve weights to fourteen by the lawful "
      "#22 protocol-amendment path",
  ratification_at="the added note's own \"(Amended ≤ 12 → ≤ 14 by user ratification 2026-07-19 at "
                  "the weight-fit dispatch …)\"; the commit's own account naming R2 = C1; and "
                  "register entry D-271, whose home is this document's capacity-budget section")

w("869e75e0a0cdeff78922b7d8f496d14d2f103f3c", "cowork_prefit_gates.md", "-147,0 +148,9", RATIFIED,
  "The hunk ADDS a parenthetical amendment to the OI-180 dual-path sanction's terms: the sanctioned "
  "touchable set ALSO includes additive extension of the L1/L1.5 fact surface — publishing the "
  "missing notated-note facts once, on the fact layer's own output surface — under two proofs per "
  "commit, byte-identity for every existing consumer and full test coverage of the new published "
  "paths, with the estimator consuming published facts and never re-reading the raw score. ★ The "
  "first class was applied first and does NOT fire, and the call is recorded because it is close: "
  "the amendment's stated ground IS a fact about pre-existing implementation — \"the published note "
  "model is tie-resolved and lossy for A's needs\" — read at a fact layer this commit did not write. "
  "What decides it is that the fact is offered as the DESIGN reason the sanctioned set must widen, "
  "beside a principled one (a module-private raw score walk \"would be the raw-source-outside-the-"
  "fact-layer defect class the certification audits condemned\"), and not as a fact against which a "
  "documentation statement was found false; the widening's source is the user's ratification the "
  "added text names.",
  "governing-decision-record",
  act="the user's ratification of 2026-07-20, at the module build's input-parity finding, widening "
      "the OI-180 sanctioned touchable set to include additive extension of the fact layer's own "
      "published surface under two per-commit proofs",
  ratification_at="the added block's own \"(Amended by user ratification 2026-07-20, at the module "
                  "build's input-parity finding …)\"; the commit's own account, which names "
                  "`cowork_prefit_gates.md` among its riding doc edits; and register entry D-274, "
                  "whose home is this document's dual-path and retirement-map section")

_ADOPT = "d615152c513f8cee20ab4cd42a8454fcb0c76106"
_ADOPT_ACCOUNT = (
    "The two hunks of this commit in this document are ONE amendment made in two places, and the "
    "amendment's own note carries its evidence and preserves the original wording in place (#12). "
    "The commit's own account is the OI-178 adoption MEASUREMENT — \"MEASUREMENT ONLY — no "
    "production wiring, no golden refresh, no `tools/robust_stop/` re-baseline, no adoption "
    "commit\" — taken under \"user ruling ★R=A1\", and it names `cowork_prefit_gates.md` (the ★R=A1 "
    "amendment) among its riding doc edits. ★ The first class was applied first at both hunks and "
    "fires at neither, and the call is recorded because it is close: a standing PASS CONDITION is "
    "replaced, and the note's evidence is a MEASUREMENT of our own decoder at the probe and "
    "cross-validation stage, taken on code this commit did not write. What decides it is that the "
    "condition was not a description of the implementation that the implementation falsified — it "
    "was a bar the note shows to be \"impossible by construction for a correct "
    "modulation-follower\", a structural argument about what the column can measure — and that the "
    "amendment was ratified by the user BEFORE the measurement it governs ran, which is #22's own "
    "lawful moment and the opposite of a gate amended under the pressure of a live diff.")
_ADOPT_ACT = ("the user's ruling ★R=A1 of 2026-07-20, taken before the adoption measurement ran, "
              "amending the OI-178 pass condition: key-agree against the LOCAL key must exceed the "
              "baseline beyond the confidence interval, the key-HOME column is TRACKED with a "
              "mandatory decomposition against the computed ground-truth self-agreement ceiling, and "
              "a modulation-rate guard is added")
_ADOPT_RAT = ("the added note's own \"(Amended by user ratification 2026-07-20, BEFORE the adoption "
              "measurement ran (#22's lawful moment) …)\"; the commit's own account, which names the "
              "user ruling ★R=A1 and the amendment among its riding doc edits; and register entry "
              "D-273, whose home is this document's robust-stop adoption-protocol section")

w(_ADOPT, "cowork_prefit_gates.md", "-117 +117", RATIFIED,
  _ADOPT_ACCOUNT + " This hunk is the condition line itself: \"key-agree (local AND home)\" becomes "
  "\"key-agree vs the LOCAL key\".",
  "governing-decision-record", act=_ADOPT_ACT, ratification_at=_ADOPT_RAT)

w(_ADOPT, "cowork_prefit_gates.md", "-119 +119,11", RATIFIED,
  _ADOPT_ACCOUNT + " This hunk carries the rest of the same amendment: the new modulation-rate "
  "guard, the key-HOME column made TRACKED with its mandatory explained decomposition against the "
  "computed ceiling, and the amendment note with the original condition quoted whole.",
  "governing-decision-record", act=_ADOPT_ACT, ratification_at=_ADOPT_RAT)

# ── `cowork_score_census.md` ──────────────────────────────────────────────────────────────────────
_CEN40 = "5a004f78ac2aeb80f78594c2abf9421ec898b07a"
_CEN40_ACCOUNT = (
    "The commit's own subject is \"Ruling 40 executed over all nine — five close into the census's "
    "own rule-stating sections, four are held at the findings-table STOP, and step 1 closed "
    "nothing\", and its body names the authority: the user's Ruling 40 of "
    "`cowork_rulings_2026_08_09_eighth_stop.md`, whose three-step procedure it executes, with the "
    "kind half judged per section before any write. Each hunk is a HOMING ACT — a decision the "
    "decisions register already holds, written into the census section that owns it, in that "
    "section's own voice, with the former home and verbatim preserved (#12). ★ The first class was "
    "applied first at every hunk of this commit and fires at none: each ADDS a rule and withdraws "
    "nothing the census stated, and every ground the added text gives is about CORPORA, LICENCES or "
    "this project's own tracking surface — never a fact read in implementation code, and the account "
    "states no documentation statement corrected against the implementation. ★ The second class "
    "fires under the calibration this block already carries: a homing act performed under a named "
    "user ruling, whose content is a decision the register holds, IS a ratified-act edit.")

w(_CEN40, "cowork_score_census.md", "-71,0 +72,9", RATIFIED,
  _CEN40_ACCOUNT + " This hunk homes the rule into §3: a registry `content` summary is enumeration "
  "provenance, and whether an annotation layer is actually present is a measurement made per slice "
  "at the files. Its defense is two of this census's own claims falsified by measurement over the "
  "sources themselves.",
  "governing-decision-record",
  act="the user's Ruling 40 of 2026-08-09, executed as the homing of register entry D-513 into the "
      "census section that owns it",
  ratification_at="the commit's own account, which names Ruling 40 of "
                  "`cowork_rulings_2026_08_09_eighth_stop.md` as its authority; and register entry "
                  "D-513, whose home is this document's §3")

w(_CEN40, "cowork_score_census.md", "-78,0 +88,10", RATIFIED,
  _CEN40_ACCOUNT + " This hunk homes the rule into §4: a newly acquired annotation set whose works "
  "OVERLAP the regression corpus is record-only — not wired to, not compared against, not "
  "bulk-diffed with the gate corpus over those works — and any such use is a user ruling. Its "
  "defense is the dedupe rule with time added, stated in the section's own terms.",
  "governing-decision-record",
  act="the user's Ruling 40 of 2026-08-09, executed as the homing of register entry D-514 into the "
      "census section that owns it",
  ratification_at="the commit's own account, which names Ruling 40 as its authority; and register "
                  "entry D-514, whose home is this document's §4")

w(_CEN40, "cowork_score_census.md", "-92,0 +112,18", RATIFIED,
  _CEN40_ACCOUNT + " This hunk homes TWO entries into §5 in one changed passage: the ratified corpus "
  "expansion stated as the scope the tiers implement, with research-tier-on-entry beside it; and, at "
  "Tier J, the deferral of the jazz fit to the jazz-ground-truth conversion. Both carry their own "
  "ratifying attributions inside the added text — the 2026-07-02 architecture review for the first, "
  "and the tier's own path for the second — and both are entries the register already held.",
  "governing-decision-record",
  act="the user's Ruling 40 of 2026-08-09, executed as the homing of register entries D-500 and "
      "D-422 into the census section that owns them",
  ratification_at="the commit's own account, which names Ruling 40 as its authority; the added "
                  "text's own naming of the 2026-07-02 architecture review as the ratifying event "
                  "for the expansion; and register entries D-500 and D-422, whose home is this "
                  "document's §5")

w(_CEN40, "cowork_score_census.md", "-254,0 +292,11", RATIFIED,
  _CEN40_ACCOUNT + " This hunk homes the difficulty-grade licence rule into §8c, stated APART from "
  "the fitting-pool bullets above it and saying why: those restrict the pool a shipped fitted VALUE "
  "may be estimated on, this restricts a shipped FEATURE whose labels are somebody else's property.",
  "governing-decision-record",
  act="the user's Ruling 40 of 2026-08-09, executed as the homing of register entry D-614 into the "
      "census section that owns it",
  ratification_at="the commit's own account, which names Ruling 40 as its authority; and register "
                  "entry D-614, whose home is this document's §8c")

_CEN9 = "5f32da30266ffdd787a4fac828f22b89b41edd39"
_CEN9_ACCOUNT = (
    "The commit's own subject is \"the census item closes — the four entries Ruling 40's step 3 held "
    "are closed by FOUR DIFFERENT ACTS\", and its body names the authority: the user's Rulings 44–48 "
    "of `cowork_rulings_2026_08_09_ninth_stop.md`, read whole (D-643), with the kind half judged per "
    "section before each of its two writes and the needs-vector table untouched in either "
    "direction. ★ The first class was applied first at both hunks and fires at neither: each ADDS a "
    "rule, withdraws nothing the census stated, and takes its ground from this project's own "
    "tracking mechanisms and from principle #21 — no fact read in implementation code, and no "
    "account of a documentation statement corrected against the implementation.")

w(_CEN9, "cowork_score_census.md", "-241,0 +242,15", RATIFIED,
  _CEN9_ACCOUNT + " This hunk writes the rule that a ground-truth class with a named consumer gets "
  "its OWN row in the needs vector and never a remark under a neighbouring row, with its own "
  "\"(user-ruled 2026-08-09)\" and the reason stated in the section's own terms — the audit and the "
  "union search both operate on columns, so a need written inside a neighbour's cell is invisible to "
  "both. Its closing clause records what is NOT implied, so the rule is not read wider than it was "
  "made.",
  "governing-decision-record",
  act="the user's Ruling 45 of 2026-08-09, which MADE the general rule the previous batch's hold "
      "said a session may not compose, written here into the census section that owns it",
  ratification_at="the added block's own \"(user-ruled 2026-08-09)\"; the commit's own account, "
                  "which names Rulings 44–48 of `cowork_rulings_2026_08_09_ninth_stop.md`; and "
                  "register entry D-515, whose home is this document's §8c")

w(_CEN9, "cowork_score_census.md", "-312,0 +328,10", RATIFIED,
  _CEN9_ACCOUNT + " This hunk adds the intake rule's fourth consequence: what a voice or stream "
  "label set actually MEASURES is said at intake — the labels obtainable today are derived from "
  "engraved notation rather than from a listener's judgment about heard lines, and the acceptance "
  "of that substitution for keyboard music is itself recorded rather than left unsaid. Its defense "
  "is principle #21 applied at the intake point.",
  "governing-decision-record",
  act="the user's Ruling 48 of 2026-08-09, written here into the census section that owns it as the "
      "intake rule's fourth consequence",
  ratification_at="the added block's own \"(user-ruled 2026-08-09)\"; the commit's own account, "
                  "which names Rulings 44–48 of `cowork_rulings_2026_08_09_ninth_stop.md`; and "
                  "register entry D-665, whose home is this document's §8c")

# ── `docs/scoring_model.md` ───────────────────────────────────────────────────────────────────────
w("7454abe5db4e169fcbdc43440c018b1add4db31b", "docs/scoring_model.md", "-2,0 +3,11", RATIFIED,
  "The hunk ADDS the status banner at the head of the document, and the banner carries its own "
  "attribution: \"*Banner ratified by the user, 2026-08-03 — drafted at phase 1j, presented at "
  "`cowork_pending_ratifications_next_session.md` §1, applied at phase 1k.*\" The commit's own "
  "account states R1 in terms — \"the four status banners RATIFIED as drafted and written verbatim "
  "at the head of each document\". ★ The first class was applied first and does NOT fire, and the "
  "call is recorded because the banner asserts something about the implementation: \"Its mechanism "
  "content describes the LEGACY vertical scorer, which is dormant on both production surfaces since "
  "2026-07-26/27\". What decides it is that the dormancy is a fact the governing record already "
  "publishes — the staged-scope clause of `CLAUDE.md` gate block (A) — rather than a fresh reading "
  "of implementation code; that the banner ADDS and expressly declines to correct the body, saying "
  "so in its own last sentence; and that its source is the user's ratification of the drafted "
  "banner.",
  "governing-decision-record",
  act="the user's ruling R1 of 2026-08-03, ratifying the four status banners as drafted and writing "
      "each verbatim at the head of its document",
  ratification_at="the banner's own italic attribution; the commit's own account of R1; and the "
                  "presentation surface the banner names, "
                  "`ratification_surfaces/cowork_pending_ratifications_next_session.md` §1")

w("1c9124f88ef07d5c2787ed717d1290f3eb1a440e", "docs/scoring_model.md", "-9 +9", RESTRUCTURING,
  "One pointer inside the banner is re-aimed — `cowork_pending_ratifications_next_session.md` "
  "becomes `ratification_surfaces/cowork_pending_ratifications_next_session.md` — following the "
  "directory this commit creates and the ten files it moves into it by `git mv`. ★ The first class "
  "was applied first and does not fire: no statement about the system is made or withdrawn, and the "
  "source is a documentation file's own new path. The second does not fire at this hunk's own text, "
  "which records no act. The third does, this being a re-pointing exactly — the same shape as the "
  "existing screen's `COWORK_HANDOFF.md` verdict.",
  "document-relocation-or-re-heading")

_SMH = "d1891db1588d73fbf41789c9139006d269a1c766"
_SMH_ACCOUNT = (
    "The commit carries five waves as one, and this document's hunks belong to the licensed-homing "
    "wave (`cc_instruction_licensed_homing_and_oi344.md`, named in the commit's own manifest). Each "
    "hunk is a HOMING ACT — a decision the decisions register already holds, written into the "
    "section of this specification that owns it, in that section's own voice, carrying its own "
    "\"re-homed into this specification 2026-08-07 on the user's ruling\" — performed under the "
    "licence the user ruled on 2026-08-07 widening a homing dispatch's edit surface to this file "
    "(register entry D-645). ★ The first class was applied first at every hunk of this commit in "
    "this document and fires at none: each ADDS a block, none withdraws a standing statement — the "
    "originally designed mechanism text is expressly \"retained above for the record\" where one "
    "exists — and the implementation facts each block cites are the DEFENSE of a decision the "
    "register already holds, not facts against which a documentation statement was found false. "
    "Neither the added text nor the account states any such correction.")
_SMH_RAT = ("each block's own \"re-homed into this specification 2026-08-07 on the user's ruling\"; "
            "the commit's own account, which names the licensed-homing wave; and the homing licence "
            "itself, register entry D-645")

w(_SMH, "docs/scoring_model.md", "-424,0 +425,14", RATIFIED,
  _SMH_ACCOUNT + " This hunk homes the Gate R decision into §4: the reconstructed-credit read is the "
  "ratified form of the guard and the originally designed literal sounding-third test is not what "
  "shipped, with the equivalence and the one exception — Diminished — stated as the defense and the "
  "former mechanism text kept above it.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the homing of register entry D-327 into "
      "the section of this specification that owns it",
  ratification_at=_SMH_RAT + "; and register entry D-327, whose home is this document")

w(_SMH, "docs/scoring_model.md", "-481,0 +496,12", RATIFIED,
  _SMH_ACCOUNT + " This hunk homes the completeness-bonus guard: the bonus fires only for a "
  "root-position reading whose three triad tones are all present, so a genuine slash chord neither "
  "gains it nor is beaten by a rival that gains it wrongly. Its defense is the measured failure of "
  "the previous unconditional version, and it is named as an early instance of the standing rule "
  "that a correction gets a structural entry condition rather than a widened threshold.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the homing of register entry D-537 into "
      "the section of this specification that owns it",
  ratification_at=_SMH_RAT + "; and register entry D-537, whose home is this document")

w(_SMH, "docs/scoring_model.md", "-711,0 +738,15", RATIFIED,
  _SMH_ACCOUNT + " This hunk homes the joint bass-and-chord decision into §5: the winner is the best "
  "(bass, root, template) triple, not a bass committed first and chords scored against it, with "
  "both defects that forced it diagnosed to the same cause and the accepted cost stated.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the homing of register entry D-536 into "
      "the section of this specification that owns it",
  ratification_at=_SMH_RAT + "; and register entry D-536, whose home is this document")

w(_SMH, "docs/scoring_model.md", "-720,0 +762,7", RATIFIED,
  _SMH_ACCOUNT + " This hunk adds a POINTER rather than a rule — what a gate may read is fixed at "
  "the inference/presentation boundary and published once at `ARCHITECTURE.md` §3.3, so the line "
  "points at it and expressly does not restate it (#6). ★ The third class was also tested and "
  "declined: the hunk is not a relocation, split, re-heading or growth of this document's own text "
  "but the recording, under the same homing ruling, of where a binding rule lives.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the pointer this specification owes to "
      "register entry D-280's home",
  ratification_at=_SMH_RAT + "; and register entry D-280, whose home is `ARCHITECTURE.md` §3.3")

w(_SMH, "docs/scoring_model.md", "-778,0 +827,35", RATIFIED,
  _SMH_ACCOUNT + " This hunk homes the three decisions the promotion primitive rests on: which carry "
  "is correct is decided on the carry's PURPOSE and not on which code was at HEAD; one promotion "
  "primitive with a present-first dedup guard; and the retirement condition for the separate rule is "
  "byte-for-byte reproduction of its carry, not the winner-inertness that preceded it.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the homing of register entries D-510, "
      "D-511 and D-512 into the section of this specification that owns them",
  ratification_at=_SMH_RAT + "; and register entries D-510, D-511 and D-512, whose home is this "
                             "document")

w(_SMH, "docs/scoring_model.md", "-981,0 +1065,121", RATIFIED,
  _SMH_ACCOUNT + " This hunk homes six standing constraints and dead ends into §8, and beneath them "
  "the four findings about the fine-grain function override, kept together as one evidence record "
  "about one mechanism. ★ The near-miss is recorded because this block carries a REACHABILITY "
  "reading taken at the code — the override is \"not reachable on any production surface, and not "
  "on the plain legacy batch path either\", surviving behind a return-early diagnostic flag and the "
  "test suites. What decides it is that the reading QUALIFIES the LEGACY mark on newly homed "
  "material and withdraws nothing this document stated, and that each homed finding's own content "
  "is a decision the register already holds.",
  "governing-decision-record",
  act="the user's homing ruling of 2026-08-07, executed as the homing of register entries D-325, "
      "D-328, D-423, D-463, D-465 and D-580, and of the four fine-grain-override findings D-490, "
      "D-491, D-492 and D-493, into the section of this specification that owns them",
  ratification_at=_SMH_RAT + "; and register entries D-325, D-328, D-423, D-463, D-465, D-580, "
                             "D-490, D-491, D-492 and D-493, whose home is this document")

w("82ebfd68d9f7760396aab2b792ea3a1dce02a9e5", "docs/scoring_model.md", "-1185,0 +1186,103",
  RATIFIED,
  "The hunk homes FOUR blocks into §8, each carrying its own \"Re-homed into this section 2026-08-08 "
  "on the user's ruling\": the bass-as-root promotion shelving with the cascade it exposed; the "
  "quality-overwrite information-loss acceptance, tolerated until the gate-dissolution step and kept "
  "visible on its row; four measured dead ends of the segmentation-and-root path; and the "
  "retroactively void validation basis of every hand-set scoring magnitude on this surface. The "
  "commit's own account is the away batch's Task 0 under the user's Ruling 1 of "
  "`cowork_rulings_2026_08_08_pre_away.md`. ★ The first class was applied first and does NOT fire: "
  "every block ADDS, none withdraws a standing statement of this document, and each states in its "
  "own words what it does NOT assert about the arm that ships — whether the joint estimator's "
  "modelled segmentation shows the same coupling, whether the acceptance still has a subject at "
  "HEAD, whether the fitted tables inherit the same standing — so the measured evidence they carry "
  "is the DEFENSE of decisions the register holds rather than a fact against which a documentation "
  "statement was found false.",
  "governing-decision-record",
  act="the homing of four archive-held decisions into the section of this specification that owns "
      "them, performed 2026-08-08 under the user's homing licence",
  ratification_at="each block's own \"Re-homed into this section 2026-08-08 on the user's ruling\"; "
                  "the commit's own account, which names Ruling 1 of "
                  "`cowork_rulings_2026_08_08_pre_away.md`; the homing licence, register entry "
                  "D-645; and register entries D-600, D-317, D-318, D-319 and D-320, whose home is "
                  "this document")

w("dfbf3ab824f0717d83cf3cce8e332c69f1074328", "docs/scoring_model.md", "-1272,0 +1273,40",
  RATIFIED,
  "The hunk homes four archive-only dead ends into §8 — no negative-margin guard; do not retry "
  "reading a minor chord as a diminished one on the same root; do not retry reading a root-position "
  "major chord as the first inversion of a minor one; do not attempt any further local scoring fix "
  "for inversions — under \"Re-homed into this section 2026-08-08\", with every ⚠ LEGACY mark "
  "intact. The commit's own account is the away batch's Task 2, \"nine archive-only decisions moved "
  "into the specifications that own them\", and it records that three of these four carried in their "
  "own provenance the statement that this section did not mention them, checked and not assumed. "
  "★ The first class was applied first and does NOT fire: each block ADDS, none withdraws a standing "
  "statement, and the measured evidence each carries is the DEFENSE of a decision the register "
  "already holds — with the counts expressly left where they were measured (D-431).",
  "governing-decision-record",
  act="the homing of four archive-only chord-scoring dead ends into the section of this "
      "specification that owns them, performed 2026-08-08 under the user's homing licence",
  ratification_at="each block's own \"Re-homed into this section 2026-08-08\"; the commit's own "
                  "account of the away batch's Task 2; the homing licence, register entry D-645; "
                  "and register entries D-299, D-300, D-301 and D-302, whose home is this document")

_SMP = "b366d44947f687245146b955475561bdb2218738"
_SMP_LOCATOR = (
    "★ THE FIRST CLASS FIRES. This is one of the eight raw line-number anchors the commit re-aimed "
    "AT THE CODE: a standing statement of this document about WHERE something is, REPLACED, and the "
    "source of the replacement is a reading of implementation code this commit did not write. The "
    "commit's own account states it in terms — \"OI-45, re-aimed at the code (D-307 — cite by "
    "function or section, never by raw line)\" — which is the class's second limb as well as its "
    "first. ★ THE COUNTER-CONSIDERATION IS RECORDED ONCE HERE AND APPLIES TO EVERY LOCATOR HUNK OF "
    "THIS COMMIT: every former wording is preserved verbatim in the same commit's \"Code locators\" "
    "note (#12), so nothing the document stated is lost; and D-639's own worked examples place a "
    "stale anchor OUTSIDE the doc-sync half phase 1 owes. What fires the class is the test as this "
    "tool states it, not a judgment that a discrepancy signal was destroyed here. ")

w(_SMP, "docs/scoring_model.md", "-11,2 +11,9", RESTRUCTURING,
  "The hunk re-points the status banner's closing sentence at the §1 scoping sentence the SAME "
  "commit adds, and the sentence it supersedes stands verbatim inside the new text — \"The former "
  "wording of the sentence this replaces, preserved (#12), was: …\" — so nothing this document "
  "stated is withdrawn. It also narrows the open row it names to its second half, a "
  "governing-document question expressly left to the user. ★ The first class was applied first and "
  "does NOT fire: the source of the change is this commit's own documentation act, not a fact read "
  "in implementation code. ★ The second does not fire at this hunk's own text, which records no user "
  "act and expressly reserves the remaining question to the user. ★ The third does: the hunk grows "
  "the banner and re-points it, with the former wording standing in place.",
  "document-relocation-or-re-heading")

w(_SMP, "docs/scoring_model.md", "-38,0 +46,24", CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES, on its SECOND limb. The hunk adds the \"Code locators\" note, whose own "
  "heading states that EVERY raw line-number anchor in this document was re-aimed to a named code "
  "region, and whose table gives the eight former wordings beside what each is now named as. It "
  "states that FOUR of the eight had drifted across a FILE boundary and that one was \"wrong as well "
  "as the line\" — so the change's own account states, in terms, that documentation statements were "
  "corrected against the implementation, read at code this commit did not write. ★ The "
  "counter-consideration is recorded: every former wording is preserved verbatim in this very note "
  "(#12), and the note itself declares that \"no term, value, guard, gate or template is added, "
  "changed or removed by it\".",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-42,0 +74,21", UNDETERMINED,
  "The hunk adds the §1 SCOPING SENTENCE: the scorer described below is dormant on both production "
  "surfaces, the body's present tense is the tense of its specification rather than a statement "
  "about what runs, and §8's constraints bind regardless of that dormancy. ★ The first class was "
  "applied first and does NOT fire: the body is untouched, no standing statement is withdrawn or "
  "narrowed, and the dormancy is cited to the record's own adoption decisions — the batch surface at "
  "D-005 and the notation surface at D-010 — rather than to a fresh reading of code. ★ The second "
  "does not fire: the act is the session's, performed under a dispatch to discharge an open row, and "
  "the added text expressly reserves the remaining half of that row to the user; no user act's "
  "CONTENT is what the change records. ★ The third does not fire: growth qualifies only where its "
  "source is not a fact about the implementation, and here the source IS one — that this scorer no "
  "longer produces a committed chord. ★ NOT CLEARED, on the not-cleared class's own first branch: a "
  "fact in the implementation is the source and the change adds material rather than replacing a "
  "standing statement. Reported whole.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-134 +186,2", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §2's tie-break sentence stops naming \"the comparator at ~L2412\" and names "
  "the winning-bass comparator in `applyHarmonicFunction` (`harmonicfunctionlayer.cpp`).",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-155 +208", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §3's three score matrices stop being \"declared at ~L2014–L2016\" and are "
  "named as declared in `analyzeChord` (`chordanalyzer.cpp`).",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-607 +660", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §4's scoring loop stops being \"the `(rootPc, tplIdx)` loop at "
  "chordanalyzer.cpp:~L2026\" and is named as that loop in `analyzeChord` (`chordanalyzer.cpp`).",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-624,5 +677,19", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here the correction is substantive rather than a coordinate: §4 had the "
  "`ScoringPhase` enum and the `ChordAnalyzerPreferences` field both in `chordanalyzer.h`, and both "
  "live in `analysis/types/analysistypes.h`; the `ScoringSnapshot` forward declaration the sentence "
  "placed beside the enum stayed behind in `chordanalyzer.h`; and the include-chain reason is "
  "restated one link longer. The commit's account names this among \"two items found at the document "
  "that no row names, both corrected\". The former wording is preserved verbatim in the added note "
  "(#12), together with what the correction does NOT touch.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-676 +743", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §4's `maxTotalInversionContextBonus` note stops citing the "
  "`ChordAnalyzerPreferences` declaration at `chordanalyzer.h:411` and cites "
  "`analysis/types/analysistypes.h` — the commit's account calling it \"wrong file as well as wrong "
  "line\".",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-688,0 +756,37", UNDETERMINED,
  "The hunk adds a §4 table naming twelve registered scoring constants that had no by-name mention "
  "anywhere in this document, each with the site it acts at and, where the document already "
  "describes its effect without naming it, the cell or prose that covers it. ★ The first class was "
  "applied first and does NOT fire: the table ADDS and withdraws nothing — the added text says in "
  "terms that several of these \"were never a substantive gap, only an ungreppable one\" — and no "
  "account states a documentation statement corrected against the implementation. ★ The second does "
  "not fire: no user act's content is recorded. ★ The third does not fire: the growth's source IS a "
  "fact read in implementation code this commit did not write — each row names the function the "
  "constant acts at and what it does there, read at `chordanalyzer.cpp` and its neighbours. ★ NOT "
  "CLEARED, on the not-cleared class's own first branch. Recorded with it: no VALUE is transcribed "
  "into the table, deliberately, which is the same staleness class the locator re-aim of this commit "
  "exists against.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-719 +823,2", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §5's `hasStructuralBass` stops being cited at \"~L1935\" and is named as "
  "computed in `analyzeChord` (`chordanalyzer.cpp`).",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-928,8 +1033,13", CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES, and this is the commit's substantive correction rather than a locator. "
  "§6's `kHalfDimFirstInversionBonus` entry said the bonus is \"additive bonus inside the "
  "enharmonic-flip block\", fired from the `preferMinorOverMajorAdd6` path in the Gate-A / G-family "
  "region, on a HalfDiminished FIRST-INVERSION alternative. The replacement says it sits in the "
  "BIAS-CORRECTION block, after the winner's bass-root deduction and before the bias re-sort, on an "
  "alternative whose third, fifth OR seventh is the winner's bass, and that the `BiasCorrection` "
  "rule owns it because `paramoverride.h`'s enum says so. Every element of that replacement is read "
  "in implementation code this commit did not write, and the commit's own account states the "
  "correction in terms — the open row said the entry was \"missing from §6 entirely\", and \"at HEAD "
  "THE ENTRY EXISTS — what was wrong was WHERE it said the bonus fires\". ★ Recorded with it: the "
  "former wording is preserved verbatim in the companion note (#12), and the value is unchanged.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-937,0 +1048,17", CODE_INFLUENCED,
  "★ THE FIRST CLASS FIRES, on its SECOND limb, in the added text's own words: \"Location corrected "
  "2026-08-14 … at the code\". The hunk is the companion note to the correction immediately above "
  "it — it quotes the former wording whole (#12), states what in it is false at HEAD, and names "
  "what the correction does NOT touch: the value, checked at the constant and unchanged, and the "
  "provenance, preset gating and dissolution-target status, which are carried over and were not "
  "re-verified. ★ Recorded with it, because the note itself declares it: one naming observation — "
  "the constant's name says *first inversion* while the code admits the third, fifth or seventh in "
  "the bass — is stated and expressly NOT acted on.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-960 +1087,2", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §7's reference to \"The 'bias correction' entry above (~L2867)\" is named as "
  "the bias-correction block of `applyPostScoringGates` (`postscoringgates.cpp`) — one of the three "
  "§7 anchors the commit's account records as having drifted across a file boundary when refactor #1 "
  "moved them out of `chordanalyzer.cpp`.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-974 +1102", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §7's \"At ~L2647–L2651, before the sort can run\" becomes \"In that same "
  "block's outer guard, before the sort can run\" — the second of the three §7 anchors that had "
  "drifted across a file boundary.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-984 +1112", CODE_INFLUENCED,
  _SMP_LOCATOR + "Here §7's \"Gate G-E (~L2910) reads\" becomes \"Gate G-E (`postscoringgates.cpp`) "
  "reads\" — the third of the three §7 anchors that had drifted across a file boundary.",
  "describes-pre-existing-implementation-behaviour")

w(_SMP, "docs/scoring_model.md", "-1585 +1713,28", RESTRUCTURING,
  "The hunk re-stamps the document's footer, which read \"Last updated: 2026-06-12 — Stage 3.1\" "
  "while the body already carried everything the new stamp enumerates, and keeps the old stamp "
  "beneath it as \"*Prior: 2026-06-12 …*\", so nothing is withdrawn (#12). ★ The first class was "
  "applied first and does NOT fire: the source of the re-stamp is THIS DOCUMENT'S OWN BODY — the "
  "added text says so, dating each act \"as the body dates them\" — and not a fact read in "
  "implementation code. ★ The second does not fire: the stamp NAMES user-ratified acts among the "
  "ones the body carries, but it records the document's own edit history rather than the content of "
  "any decision, so no user act's content is what the change records. ★ The third does: the footer "
  "grows and is re-stamped with its predecessor standing in place.",
  "document-relocation-or-re-heading")


# ── DERIVED ──────────────────────────────────────────────────────────────────────────────────────
_HDR = re.compile(r"^@@ (-\S+ \+\S+) @@")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding="utf-8", errors="replace").stdout


class Stop(Exception):
    """A demand of the screen is unmet. Never a warning."""


def last_authored_before_the_period(path: str, start_exclusive: str, end: str) -> dict:
    """Ruling 2(b)'s third value, derived from git and from nothing typed: the commit that last
    touched `path` at or before the period's end, with the check — a STOP, not a warning — that
    no commit strictly inside the period touched it (which is what the candidate enumeration's
    own coverage-gap reason asserts, re-measured here at the objects rather than inherited)."""
    inside = git("log", "--format=%H", f"{start_exclusive}..{end}", "--", path).split()
    if inside:
        raise Stop(f"{path}: the coverage gap says no period commit touched it, but git "
                   f"names {len(inside)} — the two readings disagree and nothing is declared")
    last = git("log", "-1", "--format=%H %cs", end, "--", path).strip()
    if not last:
        raise Stop(f"{path}: no commit at or before {end} touches it — nothing to declare")
    commit, date = last.split()
    return {"value": NOT_EDITED_IN_PERIOD,
            "last_authored_before_it_at": {"commit": commit, "date": date},
            "declared_text": f"{NOT_EDITED_IN_PERIOD}; last authored before it, at {commit[:10]}, {date}",
            "★_what_it_is_not": ("Not a measured distribution and not 'clean' — the screen has "
                                 "never measured authoring-time influence for any member.")}


def existing_verdicts_digest() -> str:
    """sha256 over the canonical JSON of the EXISTING authored block. Published so that
    'the existing sixty-eight verdicts are byte-unchanged' is a measurement, not a claim."""
    canon = json.dumps(
        sorted(([list(k), v] for k, v in V.items()), key=lambda x: x[0]),
        ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def retrieve(commit: str, path: str) -> dict:
    """Every hunk of one file in one commit, keyed by its -U0 header. A git OBJECT query by
    explicit hash — the retrieval assumption A2 declares, performed rather than asserted."""
    text = git("show", commit, "--no-color", "--format=", "-U0", "--", path)
    out: dict[str, dict] = {}
    cur = None
    for line in text.split("\n"):
        m = _HDR.match(line)
        if m:
            cur = {"removed": [], "added": []}
            out[m.group(1)] = cur
            continue
        if cur is None:
            continue
        if line.startswith("-") and not line.startswith("---"):
            cur["removed"].append(line[1:])
        elif line.startswith("+") and not line.startswith("+++"):
            cur["added"].append(line[1:])
    return out


def build() -> dict:
    split = json.loads(IN_SPLIT.read_text(encoding="utf-8"))
    population = split["the_screen_population_for_task_2"]["hunks"]

    # STOPs 1 and 2 — the population and the authored verdicts must agree in BOTH directions.
    pop_ids = {(h["commit"], h["file"], h["hunk_header"]) for h in population}
    ungraded = sorted(pop_ids - set(V))
    if ungraded:
        raise Stop(f"population member(s) with no authored verdict: {ungraded[:5]}")
    stray = sorted(set(V) - pop_ids)
    if stray:
        raise Stop(f"verdict(s) naming a hunk the population does not carry: {stray[:5]}")

    # STOPs 3, 4 and 5 — the vocabulary, assumption A3's own condition, and the ground.
    for ident, rec in V.items():
        if rec["verdict"] not in CLASSES:
            raise Stop(f"verdict outside the four-class vocabulary at {ident}: {rec['verdict']}")
        if rec["shape"] not in SHAPES:
            raise Stop(f"reported shape outside the declared vocabulary at {ident}: {rec['shape']}")
        if not rec["ground"]:
            raise Stop(f"verdict with no ground at {ident}")
        if rec["verdict"] == RATIFIED and not (rec["act"] and rec["ratification_at"]):
            raise Stop(f"RATIFIED-ACT-EDIT with no act or no place of ratification at {ident} "
                       f"(assumption A3)")

    cache: dict[tuple[str, str], dict] = {}
    rows = []
    for h in population:
        ident = (h["commit"], h["file"], h["hunk_header"])
        rec = V[ident]
        pair = (h["commit"], h["file"])
        if pair not in cache:
            cache[pair] = retrieve(*pair)
        got = cache[pair].get(h["hunk_header"])
        resolved = got is not None
        counts = [len(got["removed"]), len(got["added"])] if resolved else None
        row = {
            "commit": h["commit"],
            "date": h["date"],
            "stratum": h["stratum"],
            "commit_subject": h["commit_subject"],
            "file": h["file"],
            "hunk_header": h["hunk_header"],
            "role": h["role"],
            "change_shape_from_the_population": h["change_shape"],
            "added_by_the_ruled_cut": h["added_by_the_ruled_cut"],
            "verdict": rec["verdict"],
            "reported_shape": rec["shape"],
            "ground": rec["ground"],
            "the_act": rec["act"],
            "where_its_ratification_is_recorded": rec["ratification_at"],
            "remark": rec["remark"],
            "A2_retrieval": {
                "retrieved": resolved,
                "command": h["retrieve"],
                "lines_removed_added_as_retrieved": counts,
                "agrees_with_the_population_record": (counts == h["lines_removed_added"]
                                                      if resolved else False),
            },
        }
        if rec["verdict"] == CODE_INFLUENCED and resolved:
            row["the_text"] = {"removed": got["removed"], "added": got["added"]}
        rows.append(row)

    # ── THE WIDENED SCREEN (Task 3, Ruling 7) ────────────────────────────────────────────────────
    widened_block = split.get(WIDENED_KEY)
    if widened_block is None:
        raise Stop(f"the split artifact carries no `{WIDENED_KEY}` — the widening's population is "
                   f"imported, never re-derived here (#6)")
    widened_pop = widened_block["hunks"]
    new_ids = {(h["commit"], h["file"], h["hunk_header"]) for h in widened_pop if h["is_NEW"]}

    # STOP — a widened verdict naming a hunk the NEW population does not carry.
    stray_w = sorted(set(W) - new_ids)
    if stray_w:
        raise Stop(f"widened verdict(s) naming a hunk the NEW population does not carry: "
                   f"{stray_w[:5]}")

    # STOPs — the vocabulary, the shape, the ground, and assumption A3's own condition, inherited.
    for ident, rec in W.items():
        if rec["verdict"] not in WIDENED_VOCABULARY:
            raise Stop(f"widened verdict outside the declared vocabulary at {ident}: "
                       f"{rec['verdict']}")
        if rec["verdict"] == NOT_YET_READ:
            raise Stop(f"{NOT_YET_READ} is the DEFAULT for an unauthored member and is never "
                       f"authored — a member cannot be marked unread as a judgment: {ident}")
        if rec["verdict"] == OUTSIDE_SECTIONS:
            if rec["shape"] is not None:
                raise Stop(f"{OUTSIDE_SECTIONS} is recorded and NOT graded, so it carries no "
                           f"reported shape: {ident}")
        elif rec["shape"] not in SHAPES:
            raise Stop(f"widened reported shape outside the declared vocabulary at {ident}: "
                       f"{rec['shape']}")
        if not rec["ground"]:
            raise Stop(f"widened verdict with no ground at {ident}")
        if rec["verdict"] == RATIFIED and not (rec["act"] and rec["ratification_at"]):
            raise Stop(f"widened RATIFIED-ACT-EDIT with no act or no place of ratification at "
                       f"{ident} (assumption A3)")

    wrows = []
    for h in widened_pop:
        ident = (h["commit"], h["file"], h["hunk_header"])
        if h["already_screened"]:
            rec = V[ident]
            source = ("the existing screen's own verdict, INHERITED UNCHANGED — the widening "
                      "re-reads and re-grades none of the original sixty-eight")
        elif ident in W:
            rec = W[ident]
            source = "authored for the widened population by the inherited method"
        else:
            rec = {"verdict": NOT_YET_READ, "ground": None, "shape": None,
                   "act": None, "ratification_at": None, "remark": None}
            source = ("the declared exception: admitted UNREAD, counted in its own class and "
                      "reported as unread — never silently absent and never counted as "
                      f"{UNDETERMINED}")
        pair = (h["commit"], h["file"])
        if pair not in cache:
            cache[pair] = retrieve(*pair)
        got = cache[pair].get(h["hunk_header"])
        resolved = got is not None
        counts = [len(got["removed"]), len(got["added"])] if resolved else None
        wrows.append({
            "commit": h["commit"],
            "date": h["date"],
            "stratum": h["stratum"],
            "commit_subject": h["commit_subject"],
            "file": h["file"],
            "hunk_header": h["hunk_header"],
            "role": h["role"],
            "member_limb": h["member_limb"],
            "member_delegation_scope": h["member_delegation_scope"],
            "member_delegated_sections": h["member_delegated_sections"],
            "in_period_under_the_ruling": h["in_period_under_the_ruling"],
            "already_screened": h["already_screened"],
            "is_NEW": h["is_NEW"],
            "change_shape_from_the_population": h["change_shape"],
            "verdict": rec["verdict"],
            "reported_shape": rec["shape"],
            "ground": rec["ground"],
            "the_act": rec["act"],
            "where_its_ratification_is_recorded": rec["ratification_at"],
            "remark": rec["remark"],
            "where_this_verdict_comes_from": source,
            "A2_retrieval": {
                "retrieved": resolved,
                "command": h["retrieve"],
                "lines_removed_added_as_retrieved": counts,
                "agrees_with_the_population_record": (counts == h["lines_removed_added"]
                                                      if resolved else False),
            },
        })

    # the per-document POLLUTION DISTRIBUTION, derived
    per_doc: dict[str, Counter] = {}
    for r in wrows:
        per_doc.setdefault(r["file"], Counter())[r["verdict"]] += 1
    gap_by_member = {g["member"]: g for g in
                     widened_block["the_coverage_gap"]["members"]}
    # the period's own bounds, read from the candidate enumeration's artifact and never typed
    rng = json.loads(IN_MAIN.read_text(encoding="utf-8"))["range"]
    distribution = []
    for path in sorted(set(per_doc) | set(gap_by_member)):
        c = per_doc.get(path, Counter())
        gapm = gap_by_member.get(path)
        if gapm is None:
            pollution_input = {"value": "MEASURED", "see": "by_class"}
        elif gapm["hunks_in_the_candidate_enumeration"] == 0:
            pollution_input = last_authored_before_the_period(
                path, rng["start_commit_EXCLUSIVE"], rng["end_commit"])
        else:
            raise Stop(f"{path}: a coverage-gap member the enumeration DOES carry (enumerated, "
                       f"every hunk PURE). Ruling 2(b)'s declared third value is ruled for the "
                       f"no-commit case only, and this batch declares nothing for the other")
        distribution.append({
            "member": path,
            "hunks": sum(c.values()),
            "by_class": {k: c.get(k, 0) for k in WIDENED_VOCABULARY if c.get(k, 0)},
            "read": sum(c.get(k, 0) for k in CLASSES),
            NOT_YET_READ: c.get(NOT_YET_READ, 0),
            OUTSIDE_SECTIONS: c.get(OUTSIDE_SECTIONS, 0),
            "in_the_coverage_gap": path in gap_by_member,
            "the_coverage_gap_reason": (
                gap_by_member[path]["the_reason_the_enumeration_gives_for_itself"]
                if path in gap_by_member else None),
            "pollution_input": pollution_input,
        })

    # THE RULED FAILURE SIGNAL, evaluated at the artifact and not at an impression
    wread = [r for r in wrows if r["verdict"] in CLASSES]
    wundet = [r for r in wread if r["verdict"] == UNDETERMINED]
    wunread = [r for r in wrows if r["verdict"] == NOT_YET_READ]
    if not wread:
        signal = "NOT YET EVALUABLE"
        signal_why = ("No widened member carries a verdict in the four inherited classes, so the "
                      "majority test has no population to run over. This is not the signal "
                      "failing to fire; it is the test not yet having an input.")
    elif wunread:
        signal = "INCONCLUSIVE-AT-THIS-COVERAGE"
        signal_why = ("The widened population is not yet read whole, so a majority over the read "
                      "members cannot be reported as the ruled signal firing. The read share is "
                      "published beside the majority, and the ruling's own words are that a "
                      "majority reached only because few members were read is reported this way "
                      "rather than as the signal firing.")
    elif len(wundet) * 2 > len(wread):
        signal = "FIRES"
        signal_why = ("Over the widened population's READ members, UNDETERMINED is the majority, "
                      "and every widened member has been read. That is the ruled failure signal.")
    else:
        signal = "DOES NOT FIRE"
        signal_why = ("Over the widened population's READ members, UNDETERMINED is not the "
                      "majority, and every widened member has been read.")

    by_verdict = Counter(r["verdict"] for r in rows)
    by_shape = Counter(r["reported_shape"] for r in rows)
    unresolved = [{"commit": r["commit"], "file": r["file"], "hunk_header": r["hunk_header"]}
                  for r in rows if not r["A2_retrieval"]["retrieved"]]
    disagreeing = [{"commit": r["commit"], "file": r["file"], "hunk_header": r["hunk_header"]}
                   for r in rows if r["A2_retrieval"]["retrieved"]
                   and not r["A2_retrieval"]["agrees_with_the_population_record"]]
    fired = [r for r in rows if r["verdict"] == CODE_INFLUENCED]

    return {
        "what_this_is": (
            "THE JULY SCREEN. Every out-of-period specification-bearing flagged hunk, read one at a "
            "time at its own text and its commit's own account, and classified into exactly one of "
            "the dispatch's four classes with its ground. It edits no screened document, restores "
            "nothing and corrects nothing."),
        "dispatch": "cc_instruction_period_checks.md",
        "generator": "tools/audit/gen_july_screen.py",
        "population_from": "tools/audit/period_stratum_split.json → the_screen_population_for_task_2",
        "reproduce": ("python tools/audit/gen_july_screen.py --check   # re-derives the artifact and "
                      "the report and exits 1 on any drift"),
        "★_the_inherited_establishment_caveat": split["★_the_inherited_establishment_caveat"],
        "★_the_falsification_rule_and_what_fired": {
            "the_rule_as_ruled": (
                "From `cowork_rulings_2026_08_15_period_start.md`: \"if any shows a code-influenced "
                "correction, the period question RE-OPENS\", and the re-opening \"is the user's act "
                "on the screen's report\"."),
            "hunks_positively_code_influenced": len(fired),
            "the_rule_fires": bool(fired),
            "what_that_does_and_does_not_mean": (
                "It means the screen found positive evidence of the shape the rule names, and that "
                "the period question is now the user's to re-open or to leave settled. It does NOT "
                "mean the period ruling is wrong, and this tool takes no view on that. Nothing is "
                "repaired, reverted or restored by this finding."),
        },
        "the_classes_and_the_order_they_are_applied_in": {
            CODE_INFLUENCED: (
                "The change WITHDRAWS, NARROWS, QUALIFIES or REPLACES something the documentation "
                "already stated, and the source of the replacement is a fact read in implementation "
                "code THIS COMMIT DID NOT WRITE; or the change's own account states that a "
                "documentation statement was corrected against the implementation. APPLIED FIRST, "
                "so a ratified act cannot launder a correction made under it."),
            RATIFIED: (
                "The change writes, re-stamps or records what a NAMED user act ruled, ratified or "
                "directed — including the same-commit documentation half of a ratified change to "
                "the code. The act AND where its ratification is recorded are both cited, or the "
                "class is not admitted (assumption A3)."),
            RESTRUCTURING: (
                "Relocation, split, re-heading or growth whose source is not a fact read in "
                "implementation code the commit did not write."),
            UNDETERMINED: (
                "NOT CLEARED — the dispatch's own gloss. A fact in the implementation is the source "
                "but the change adds material rather than replacing a standing statement, or no "
                "ground supports any class above. Reported whole, never argued down."),
        },
        "★_what_the_screen_cannot_settle": (
            "Ruling 5 of the eighteenth stop states that influence is INVISIBLE IN THE TEXT — a "
            "narrowed rule reads exactly like a rule that was always narrow. So this screen finds "
            "POSITIVE evidence of influence and nothing else, and a clear verdict here is bounded "
            "by that. A clean class is not a certificate that the change was uninfluenced; the "
            "not-cleared class exists for exactly this reason and is published whole."),
        "P2_the_registered_prediction_graded": {
            "taken_at": ("`cc_instruction_period_checks.md` §0a, prediction P2, registered before "
                         "anything ran. Moderate confidence, no authority."),
            "limb_1_the_large_majority_classify_RATIFIED_ACT_or_RESTRUCTURING_SHAPED": {
                "hunks_in_those_two_classes": by_verdict[RATIFIED] + by_verdict[RESTRUCTURING],
                "of_hunks_screened": len(rows),
                "share": round((by_verdict[RATIFIED] + by_verdict[RESTRUCTURING]) / len(rows), 4),
                "★_why_this_limb_is_published_rather_than_scored": (
                    "The prediction says *large majority* and fixes no threshold, so the share is "
                    "published and the reading is left to the reader rather than computed against "
                    "a number nobody registered."),
            },
            "limb_2_ZERO_classify_POSITIVELY_CODE_INFLUENCED": {
                "predicted": 0,
                "derived": len(fired),
                "held": not fired,
                "★_the_refutation_condition_as_registered": (
                    "\"one hunk whose change, or whose commit's own account, states or shows "
                    "correction against the implementation\" — which is the condition this screen "
                    "applies as its first class."),
            },
            "★_the_prediction_is_not_reconciled_towards": (
                "Nothing in the verdicts was adjusted to make a limb hold. A prediction is graded "
                "and never used as an input (#17b)."),
        },
        "counted": {
            "hunks_screened": len(rows),
            "by_verdict": dict(sorted(by_verdict.items())),
            "by_reported_shape": dict(sorted(by_shape.items())),
            "by_stratum": dict(sorted(Counter(r["stratum"] for r in rows).items())),
            "by_file": dict(sorted(Counter(r["file"] for r in rows).items())),
            "distinct_commits": len({r["commit"] for r in rows}),
        },
        "A2_the_retrieval_assumption_checked_per_hunk": {
            "how": ("Every hunk's text was retrieved from the git object by explicit hash — "
                    "`git show <commit> --no-color -U0 -- <path>` — and its recorded header looked "
                    "for among the headers that came back. Performed on every run, not asserted."),
            "hunks_that_did_not_resolve": unresolved,
            "hunks_whose_retrieved_line_counts_disagree_with_the_population_record": disagreeing,
            "★_what_a_disagreement_would_mean": (
                "The coordinates would not identify the same change the population enumerated. It "
                "is reported per hunk rather than halting the screen, which is what the dispatch's "
                "assumption A2 asks for."),
        },
        "the_reported_shapes": SHAPES,
        "★_the_widened_screen": {
            "what_it_is_honestly": (
                "An AUTHORED VERDICT PER HUNK over a DERIVED population — the FLAG hunks of the "
                "candidate enumeration whose file is a member of the ruled specification document "
                "set. It finds POSITIVE EVIDENCE OF INFLUENCE ONLY, and it is bounded by the "
                "invisibility the original screen declares of itself: influence is invisible in "
                "the text, because a narrowed rule reads exactly like a rule that was always "
                "narrow. SO A CLEAN CLASS IS NOT A CERTIFICATE that a change was uninfluenced. "
                "That text is INHERITED from the screen this widens and is not re-argued here."),
            "ruling": widened_block["ruling"],
            "★_a_POSITIVELY_CODE_INFLUENCED_hunk_HERE_is_not_the_period_questions_falsification": (
                "The falsification rule at the head of this artifact belongs to the ORIGINAL "
                "screen and to its population, which is OUT-OF-PERIOD by construction: a "
                "code-influenced correction found THERE would mean the ruled period start is in "
                "the wrong place, and it re-opens that question. THIS population is deliberately "
                "wider — every stratum, in-period and out-of-period alike — because Ruling 7 asks "
                "it to MEASURE the pollution rather than to test the period. So an IN-PERIOD "
                "positively-code-influenced hunk here is the measurement's own subject and is "
                "EXPECTED: the period is defined as the programme under which the truth-sync "
                "happened. It is not a falsification of anything, and it must not be read as one. "
                "Each hunk records whether it is in period, so the two readings never have to be "
                "guessed apart."),
            "★_the_method_is_inherited_whole": (
                "The four classes, the ORDER they are applied in, the six reported shapes and the "
                "five STOPs are the existing screen's and are unchanged — \"its method untouched\" "
                "is Ruling 7's own clause. What is added is a SECOND POPULATION, a SECOND AUTHORED "
                "BLOCK for it, and two declared values: NOT YET READ, the one declared exception "
                "to the no-verdict STOP, and OUTSIDE NAMED SECTIONS, for a hunk of a "
                "section-scoped member falling outside the sections its delegation names."),
            "★_the_existing_sixty_eight_are_not_re_read_or_re_graded": (
                "A widened hunk that is ALREADY in the existing screen population inherits that "
                "hunk's existing verdict verbatim; no verdict of the original sixty-eight is "
                "re-authored, and the `verdicts` array above is byte-unchanged by this widening."),
            "the_existing_verdicts_digest": {
                "value": existing_verdicts_digest(),
                "over": ("sha256 of the canonical JSON of the existing authored block — every "
                         "verdict, ground, shape, act, place-of-ratification and remark of the "
                         "original sixty-eight, sorted by hunk identity."),
                "★_how_to_use_it": (
                    "Compare it across the runs of this batch. An identical value is a "
                    "measurement that the existing authored block did not move; a different one "
                    "means a verdict of the original sixty-eight changed, which the widening may "
                    "not do."),
            },
            "counted": {
                "hunks_in_the_widened_population": len(wrows),
                "already_screened_and_inherited": sum(1 for r in wrows if r["already_screened"]),
                "NEW": sum(1 for r in wrows if r["is_NEW"]),
                "read": len(wread),
                "unread": len(wunread),
                "by_verdict": dict(sorted(Counter(r["verdict"] for r in wrows).items())),
                "by_reported_shape": dict(sorted(
                    Counter(r["reported_shape"] for r in wrows
                            if r["reported_shape"]).items())),
                "by_document": dict(sorted(Counter(r["file"] for r in wrows).items())),
                "distinct_commits": len({r["commit"] for r in wrows}),
            },
            "★_the_ruled_failure_signal": {
                "the_rule_as_ruled": (
                    "Ruling 7, with the plan's §4: \"if most passages land UNDETERMINED the "
                    "premise is not measurable, and that is a STOP to the user, not a licence to "
                    "proceed.\" It is not a licence to argue the class down either."),
                "verdict": signal,
                "why": signal_why,
                "read_members": len(wread),
                "of_the_widened_population": len(wrows),
                "read_share": (round(len(wread) / len(wrows), 4) if wrows else None),
                "UNDETERMINED_among_the_read": len(wundet),
                "UNDETERMINED_share_of_the_read": (round(len(wundet) / len(wread), 4)
                                                   if wread else None),
            },
            "the_per_document_pollution_distribution": distribution,
            "★_the_declared_third_value": THIRD_VALUE_RULING,
            "the_coverage_gap_beside_it": widened_block["the_coverage_gap"],
            "the_hunks": wrows,
        },
        "what_this_does_NOT_do": (
            "No screened document is edited. Nothing is restored, reverted, reconciled or "
            "corrected. No open-items row is marked, flipped or discarded; no decisions-register "
            "entry is written. No fix, design or measurement of the analysis is authorized or performed. The "
            "period question is not re-opened here — the report says what would re-open it, and the "
            "act is the user's."),
        "verdicts": rows,
    }


def render_report(art: dict) -> str:
    rows = art["verdicts"]
    c = art["counted"]
    f = art["★_the_falsification_rule_and_what_fired"]
    fired = [r for r in rows if r["verdict"] == CODE_INFLUENCED]

    L: list[str] = []
    L.append("# The July screen — the out-of-period specification-bearing flagged hunks, read one "
             "at a time")
    L.append("")
    L.append("> **GENERATED FILE — do not hand-edit.** Written by "
             "`tools/audit/gen_july_screen.py`; re-derive with `--check`. Every verdict below is "
             "AUTHORED and every count is DERIVED. The screen edits no document it reads.")
    L.append("")
    if fired:
        L.append("## ★ THE FALSIFICATION RULE FIRES — the period question is RE-OPENED FOR THE USER")
        L.append("")
        L.append(f"**{len(fired)} of {c['hunks_screened']} screened hunks classify "
                 f"{CODE_INFLUENCED}.** The ruled falsification rule is: *\"if any shows a "
                 "code-influenced correction, the period question RE-OPENS\"* — and the re-opening "
                 "is the user's act on this report, not this screen's.")
        L.append("")
        L.append("**What that does and does not mean.** " + f["what_that_does_and_does_not_mean"])
        L.append("")
    else:
        L.append("## The falsification rule does NOT fire")
        L.append("")
        L.append("No screened hunk classifies " + CODE_INFLUENCED + ". Read that verdict beside "
                 "what the screen cannot settle, immediately below.")
        L.append("")
    L.append("## What the screen cannot settle, stated before the result")
    L.append("")
    L.append(art["★_what_the_screen_cannot_settle"])
    L.append("")
    L.append("## The population")
    L.append("")
    L.append(f"- **{c['hunks_screened']} hunks**, across **{c['distinct_commits']} commits** and "
             f"**{len(c['by_file'])} documents**.")
    L.append("- By stratum: " + ", ".join(f"{k} {n}" for k, n in c["by_stratum"].items()) + ".")
    L.append("- By document: " + ", ".join(f"`{k}` {n}" for k, n in c["by_file"].items()) + ".")
    L.append("- The population is imported whole from `tools/audit/period_stratum_split.json` and "
             "never re-listed here (#6); a member entering or leaving it halts the generator "
             "rather than being graded silently or quietly dropped.")
    L.append("")
    L.append("## The verdicts")
    L.append("")
    L.append("| class | hunks |")
    L.append("|---|---|")
    for k, n in c["by_verdict"].items():
        L.append(f"| {k} | {n} |")
    L.append("")
    L.append("**The classes, and the order they are applied in** (the order is declared because it "
             "decides cases, and the first class is applied FIRST so that a ratified act cannot "
             "launder a correction made under it):")
    L.append("")
    for k in CLASSES:
        L.append(f"- **{k}** — {art['the_classes_and_the_order_they_are_applied_in'][k]}")
    L.append("")
    L.append("## The reported shapes — what kind of change sits behind each verdict")
    L.append("")
    L.append("A shape is never a verdict. It is what lets a reader see the KIND of change without "
             "the class name standing in for it.")
    L.append("")
    L.append("| shape | hunks | what it is |")
    L.append("|---|---|---|")
    for k, n in c["by_reported_shape"].items():
        L.append(f"| `{k}` | {n} | {art['the_reported_shapes'][k]} |")
    L.append("")
    if fired:
        L.append("## The hunks that fire the rule, quoted whole")
        L.append("")
        for r in fired:
            L.append(f"### `{r['file']}` @ `{r['hunk_header']}` — {r['commit'][:10]}, "
                     f"{r['date'][:10]}")
            L.append("")
            L.append(f"*Commit subject:* {r['commit_subject']}")
            L.append("")
            L.append(f"**Ground.** {r['ground']}")
            L.append("")
            if r.get("remark"):
                L.append(f"**{r['remark']}**")
                L.append("")
            L.append("**Removed:**")
            L.append("")
            L.append("```")
            L.extend(r["the_text"]["removed"])
            L.append("```")
            L.append("")
            L.append("**Added:**")
            L.append("")
            L.append("```")
            L.extend(r["the_text"]["added"])
            L.append("```")
            L.append("")
            L.append(f"*Retrieve it yourself:* `{r['A2_retrieval']['command']}`")
            L.append("")
    L.append("## The registered prediction P2, graded")
    L.append("")
    p2 = art["P2_the_registered_prediction_graded"]
    l1 = p2["limb_1_the_large_majority_classify_RATIFIED_ACT_or_RESTRUCTURING_SHAPED"]
    l2 = p2["limb_2_ZERO_classify_POSITIVELY_CODE_INFLUENCED"]
    L.append(f"- **Limb 1 — the large majority classify {RATIFIED} or {RESTRUCTURING}:** "
             f"{l1['hunks_in_those_two_classes']} of {l1['of_hunks_screened']} "
             f"({l1['share']}). " + l1["★_why_this_limb_is_published_rather_than_scored"])
    L.append(f"- **Limb 2 — ZERO classify {CODE_INFLUENCED}:** predicted {l2['predicted']}, "
             f"derived {l2['derived']} — **{'HELD' if l2['held'] else 'REFUTED'}**. "
             + l2["★_the_refutation_condition_as_registered"])
    L.append("")
    L.append(p2["★_the_prediction_is_not_reconciled_towards"])
    L.append("")
    L.append("## Assumption A2 — the retrieval, checked per hunk rather than asserted")
    L.append("")
    a2 = art["A2_the_retrieval_assumption_checked_per_hunk"]
    L.append(a2["how"])
    L.append("")
    L.append(f"- Hunks that did not resolve: **{len(a2['hunks_that_did_not_resolve'])}**.")
    L.append("- Hunks whose retrieved line counts disagree with the population's own record: "
             f"**{len(a2['hunks_whose_retrieved_line_counts_disagree_with_the_population_record'])}**.")
    L.append("")
    L.append("## Every hunk, with its verdict and its ground")
    L.append("")
    for r in rows:
        L.append(f"### {r['date'][:10]} · `{r['file']}` @ `{r['hunk_header']}` · "
                 f"{r['commit'][:10]}")
        L.append("")
        L.append(f"- **Verdict:** {r['verdict']} · shape `{r['reported_shape']}`"
                 + ("  ·  *added by the ruled cut*" if r["added_by_the_ruled_cut"] else ""))
        L.append(f"- **Commit subject:** {r['commit_subject']}")
        L.append(f"- **Ground.** {r['ground']}")
        if r["the_act"]:
            L.append(f"- **The act:** {r['the_act']}")
            L.append(f"- **Where its ratification is recorded:** "
                     f"{r['where_its_ratification_is_recorded']}")
        if r.get("remark"):
            L.append(f"- **Remark.** {r['remark']}")
        L.append(f"- *Retrieve:* `{r['A2_retrieval']['command']}`")
        L.append("")
    # ── the widened screen ───────────────────────────────────────────────────────────────────────
    W_ART = art["★_the_widened_screen"]
    wc = W_ART["counted"]
    sig = W_ART["★_the_ruled_failure_signal"]
    L.append("---")
    L.append("")
    L.append("# The WIDENED screen — the same method, over the ruled specification document set")
    L.append("")
    L.append("> **The population is widened by MEMBERSHIP, not by role.** Its enumeration lives at "
             "`tools/audit/period_stratum_split.json` → `★_the_widened_screen_population` and is "
             "imported whole here, never re-listed (#6).")
    L.append("")
    L.append("**What this is, honestly.** " + W_ART["what_it_is_honestly"])
    L.append("")
    L.append("**The method is inherited whole.** " + W_ART["★_the_method_is_inherited_whole"])
    L.append("")
    L.append("**A code-influenced hunk HERE is not the period question's falsification.** "
             + W_ART["★_a_POSITIVELY_CODE_INFLUENCED_hunk_HERE_is_not_the_period_questions_"
                     "falsification"])
    L.append("")
    L.append("**The existing sixty-eight are not re-read or re-graded.** "
             + W_ART["★_the_existing_sixty_eight_are_not_re_read_or_re_graded"]
             + " Digest of the existing authored block: `"
             + W_ART["the_existing_verdicts_digest"]["value"] + "`. "
             + W_ART["the_existing_verdicts_digest"]["★_how_to_use_it"])
    L.append("")
    L.append("## ★ The ruled failure signal — " + sig["verdict"])
    L.append("")
    L.append("*The rule as ruled.* " + sig["the_rule_as_ruled"])
    L.append("")
    L.append(sig["why"])
    L.append("")
    L.append(f"- Read members: **{sig['read_members']}** of **{sig['of_the_widened_population']}** "
             f"(read share {sig['read_share']}).")
    L.append(f"- {UNDETERMINED} among the read: **{sig['UNDETERMINED_among_the_read']}** "
             f"(share of the read {sig['UNDETERMINED_share_of_the_read']}).")
    L.append("")
    L.append("## The widened population")
    L.append("")
    L.append(f"- **{wc['hunks_in_the_widened_population']} hunks** across "
             f"**{wc['distinct_commits']} commits** and **{len(wc['by_document'])} documents** — "
             f"**{wc['already_screened_and_inherited']}** already screened and inherited, "
             f"**{wc['NEW']}** new.")
    L.append("- By verdict: " + ", ".join(f"{k} {n}" for k, n in wc["by_verdict"].items()) + ".")
    L.append("")
    L.append("## The per-document pollution distribution")
    L.append("")
    L.append("| member | hunks | read | " + " | ".join(CLASSES) + f" | {NOT_YET_READ} | "
             f"{OUTSIDE_SECTIONS} | coverage gap | pollution input |")
    L.append("|---|---|---|" + "---|" * (len(CLASSES) + 4))
    for d in art["★_the_widened_screen"]["the_per_document_pollution_distribution"]:
        cells = [str(d["by_class"].get(k, 0)) for k in CLASSES]
        pi = d["pollution_input"]
        L.append(f"| `{d['member']}` | {d['hunks']} | {d['read']} | " + " | ".join(cells)
                 + f" | {d[NOT_YET_READ]} | {d[OUTSIDE_SECTIONS]} | "
                 + ("**yes**" if d["in_the_coverage_gap"] else "—") + " | "
                 + pi.get("declared_text", pi["value"]) + " |")
    L.append("")
    gapb = W_ART["the_coverage_gap_beside_it"]
    L.append("## The coverage gap — the members the screen cannot see at all")
    L.append("")
    L.append(gapb["★_what_this_is"])
    L.append("")
    L.append("**The declared third value of the pollution input, as ruled.** "
             + W_ART["★_the_declared_third_value"])
    L.append("")
    L.append(f"**{gapb['members_with_no_flagged_hunk']} of {gapb['of_the_members']} members "
             f"carry no flagged hunk in the candidate enumeration.**")
    L.append("")
    for g in gapb["members"]:
        L.append(f"- `{g['member']}` — {g['the_reason_the_enumeration_gives_for_itself']}")
    L.append("")
    unread_rows = [r for r in W_ART["the_hunks"] if r["verdict"] == NOT_YET_READ]
    if unread_rows:
        L.append("## What remains UNREAD, per document")
        L.append("")
        L.append("Recorded so that a continuing session derives the remainder fresh rather than "
                 "carrying it from this session's account of it. The order below is the "
                 "artifact's own — by document, then by commit, then by hunk.")
        L.append("")
        by_doc: dict[str, int] = {}
        for r in unread_rows:
            by_doc[r["file"]] = by_doc.get(r["file"], 0) + 1
        for k, n in sorted(by_doc.items()):
            L.append(f"- `{k}` — **{n}** unread")
        L.append("")
    graded_w = [r for r in W_ART["the_hunks"] if r["is_NEW"] and r["verdict"] != NOT_YET_READ]
    if graded_w:
        L.append("## Every NEW hunk read so far, with its verdict and its ground")
        L.append("")
        for r in graded_w:
            L.append(f"### {r['date'][:10]} · `{r['file']}` @ `{r['hunk_header']}` · "
                     f"{r['commit'][:10]}")
            L.append("")
            L.append(f"- **Verdict:** {r['verdict']}"
                     + (f" · shape `{r['reported_shape']}`" if r["reported_shape"] else ""))
            L.append(f"- **Commit subject:** {r['commit_subject']}")
            L.append(f"- **Ground.** {r['ground']}")
            if r["the_act"]:
                L.append(f"- **The act:** {r['the_act']}")
                L.append(f"- **Where its ratification is recorded:** "
                         f"{r['where_its_ratification_is_recorded']}")
            if r.get("remark"):
                L.append(f"- **Remark.** {r['remark']}")
            L.append(f"- *Retrieve:* `{r['A2_retrieval']['command']}`")
            L.append("")
    L.append("## What this screen does not do")
    L.append("")
    L.append(art["what_this_does_NOT_do"])
    L.append("")
    L.append("## The inherited establishment caveat (#19)")
    L.append("")
    L.append(art["★_the_inherited_establishment_caveat"])
    L.append("")
    return "\n".join(L)


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    report = render_report(art)
    if "--check" in argv:
        bad = False
        if not OUT_JSON.exists() or OUT_JSON.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT_JSON)
            bad = True
        if not OUT_REPORT.exists() or OUT_REPORT.read_text(encoding="utf-8") != report:
            print("FAIL: re-derivation differs from the committed artifact:", OUT_REPORT)
            bad = True
        if bad:
            return 1
        print("OK: the July screen re-derives byte-identically.")
        return 0
    OUT_JSON.write_text(text, encoding="utf-8", newline="")
    OUT_REPORT.write_text(report, encoding="utf-8", newline="")
    print("wrote", OUT_JSON)
    print("wrote", OUT_REPORT)
    c = art["counted"]
    print(f"  screened {c['hunks_screened']} hunks over {c['distinct_commits']} commits")
    for k, n in c["by_verdict"].items():
        print(f"    {k}: {n}")
    f = art["★_the_falsification_rule_and_what_fired"]
    print(f"  the falsification rule fires: {f['the_rule_fires']} "
          f"({f['hunks_positively_code_influenced']} positively code-influenced)")
    a2 = art["A2_the_retrieval_assumption_checked_per_hunk"]
    print(f"  A2: {len(a2['hunks_that_did_not_resolve'])} unresolved, "
          f"{len(a2['hunks_whose_retrieved_line_counts_disagree_with_the_population_record'])} "
          f"count disagreements")
    wa = art["★_the_widened_screen"]
    wc, sg = wa["counted"], wa["★_the_ruled_failure_signal"]
    print(f"  THE WIDENED SCREEN: {wc['hunks_in_the_widened_population']} hunks — "
          f"{wc['already_screened_and_inherited']} inherited, {wc['NEW']} new; "
          f"read {wc['read']}, unread {wc['unread']}")
    for k, n in wc["by_verdict"].items():
        print(f"    {k}: {n}")
    print(f"  THE RULED FAILURE SIGNAL: {sg['verdict']} "
          f"(read share {sg['read_share']}, UNDETERMINED share of the read "
          f"{sg['UNDETERMINED_share_of_the_read']})")
    print(f"  existing-verdicts digest: {wa['the_existing_verdicts_digest']['value'][:16]}…")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
