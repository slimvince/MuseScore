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
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()

ROOT = Path(__file__).resolve().parent.parent.parent
IN_SPLIT = ROOT / "tools" / "audit" / "period_stratum_split.json"
OUT_JSON = ROOT / "tools" / "audit" / "july_screen.json"
OUT_REPORT = ROOT / "tools" / "audit" / "july_screen_report.md"

CODE_INFLUENCED = "POSITIVELY CODE-INFLUENCED"
RATIFIED = "RATIFIED-ACT EDIT"
RESTRUCTURING = "RESTRUCTURING-SHAPED"
UNDETERMINED = "UNDETERMINED"
CLASSES = (CODE_INFLUENCED, RATIFIED, RESTRUCTURING, UNDETERMINED)

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


# ── DERIVED ──────────────────────────────────────────────────────────────────────────────────────
_HDR = re.compile(r"^@@ (-\S+ \+\S+) @@")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding="utf-8", errors="replace").stdout


class Stop(Exception):
    """A demand of the screen is unmet. Never a warning."""


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
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
