#!/usr/bin/env python3
"""RULING 16's SWEEP — every `src/` comment claiming an arm, a flag default or a build state that
the notation switch made false, enumerated before anything is edited.

THE RULING (user, 2026-08-09, `cowork_rulings_2026_08_09_second_stop.md`, Ruling 16; register entry
for the bundling discipline: the standing one-fix-per-family rule).  `OPEN_ITEMS.md` OI-353 recorded
six `src/` sites saying the production record path is "default OFF".  The ruling refuses a
per-symptom fix and orders, in this order: **a read-only SWEEP first**, so the family is enumerated
against the configuration facts; **then ONE comment-only commit** over the enumerated family.  Its
own words: OI-353's six sites *"are the found members, not the family"*.  A sibling whose falsity is
**not mechanical** — one that needs a judgment about the analysis — is **HELD, not edited**.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  derived  : the two CONFIGURATION FACTS, read at the code by anchor string and never recalled —
             the flag's default value, and whether any non-test `src/` translation unit outside the
             joint module references a joint or record symbol;
             the CANDIDATE POPULATION — every comment BLOCK under `src/` that makes a dormancy,
             no-consumer or flag-default claim AND names the joint module or the notation record;
             every count, and the split of the population by verdict.
  authored : the VERDICT per candidate block — FALSE-AT-HEAD, TRUE-AT-HEAD or HELD — with the
             reason, keyed by the file and the block's own first comment line rather than by a line
             number, so the table follows its subject when the file moves.

THE STOPS, and they are the reason this is a sweep rather than a list.
  * a candidate block with NO authored verdict halts the run — the population is derived and grows
    as the tree grows, so a new sibling cannot enter silently unclassified;
  * an authored verdict naming a block the scan no longer finds halts the run — the mirror
    direction, so a verdict cannot outlive the comment it grades;
  * either configuration fact failing to resolve at its anchor halts the run — this whole
    enumeration rests on them, and a fact that cannot be located may not be assumed.

WHAT IT DOES NOT DO.  It edits nothing.  It is the read-only half of Ruling 16, and the comment-only
commit is a separate act performed against this artifact.

Usage:
  python tools/audit/gen_arm_comment_sweep.py           # write the artifact
  python tools/audit/gen_arm_comment_sweep.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(HERE, "arm_comment_sweep.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

CONFIG_FILE = os.path.join(ROOT, "src", "composing", "composingconfiguration.cpp")
DEFAULT_ANCHOR = "setDefaultValue(USE_JOINT_NOTATION_RECORD"

# A block claims something this sweep is about when it makes a STATE claim ...
STATE_CLAIM = re.compile(
    r"\bDORMANT\b|\bdormant\b|no production consumer|no src/ caller|not wired|"
    r"default-OFF|default OFF|defaults OFF", re.IGNORECASE)
# ... AND names the joint module or the notation record, which is this family's subject.
# ★ THE HYPHENATED FORMS ARE HERE BECAUSE THE FIRST RUN MISSED ONE.  `record[- ]path` and
# `record[- ]arm` are written both ways in the tree, and a space-only pattern let
# `sectionrecordadapter.cpp`'s "The record-path variant" out of the population — a FALSE block the
# phase-1w verification's own STOP then found.  Widening the derivation is the fix; narrowing one
# to quiet a STOP would be the opposite act and is never taken.
SUBJECT = re.compile(
    r"useJointNotationRecord|\bjoint\b|notation record|record[- ]arm|record[- ]path|"
    r"notation output-surface record", re.IGNORECASE)

COMMENT = re.compile(r"^\s*(///|//|#)")

FALSE_AT_HEAD, TRUE_AT_HEAD, HELD = "FALSE-AT-HEAD", "TRUE-AT-HEAD", "HELD"

# ---------------------------------------------------------------------------------------------
# AUTHORED — one verdict per candidate block, keyed by (path, the block's first comment line).
# Every FALSE-AT-HEAD verdict is mechanical: it is refuted by one of the two derived configuration
# facts below and needs no judgment about what the analysis does.
# ---------------------------------------------------------------------------------------------
VERDICTS: dict[tuple[str, str], tuple[str, str]] = {}

# The blocks the comment-only commit CORRECTED, keyed by the FORMER first comment line.  A
# corrected block either leaves the derived population (its state claim is gone) or stays in it
# with a new first line, so the orphan STOP would fire on its verdict.  Recording the correction
# here is what keeps that STOP honest: it is the difference between "this verdict's subject moved"
# and "this verdict's subject was fixed by the act this artifact records" (#12 — the former
# wording is preserved with each one, never deleted).
CORRECTED: dict[tuple[str, str], str] = {}


def _v(path: str, first_line: str, verdict: str, why: str) -> None:
    VERDICTS[(path, first_line.strip())] = (verdict, why)


def _fixed(path: str, former_first_line: str, what: str) -> None:
    CORRECTED[(path, former_first_line.strip())] = what


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def configuration_facts() -> dict:
    """The two facts every verdict is checked against, read at the code and never recalled."""
    text = read(CONFIG_FILE)
    i = text.find(DEFAULT_ANCHOR)
    if i < 0:
        raise SystemExit(
            "STOP: the flag's default-value site is not at its anchor in "
            "src/composing/composingconfiguration.cpp — this sweep rests on that fact and may "
            "not assume it.")
    line = text[text.rfind("\n", 0, i) + 1: text.find("\n", i)].strip()
    m = re.search(r"Val\(\s*(true|false)\s*\)", line)
    if not m:
        raise SystemExit(f"STOP: the default-value site does not state a boolean: {line!r}")

    # The build-state fact: does any NON-TEST src/ translation unit outside the joint module
    # reference a joint or record symbol? Derived by scanning, never asserted.
    callers = []
    for path in source_files():
        rel = path.replace("\\", "/")
        if "/tests/" in rel or "/analysis/joint/" in rel or rel.endswith("CMakeLists.txt"):
            continue
        if "/analysis/section/sectionrecordadapter" in rel:
            continue
        body = read(path)
        if re.search(r"jointnotationproducer|jointnotationrecord|analyzeSectionFromRecord",
                     body, re.IGNORECASE):
            callers.append(os.path.relpath(path, ROOT).replace("\\", "/"))

    return {
        "how_they_were_obtained": "READ AT THE CODE, located by anchor string rather than by line "
                                  "number, and re-read on every run. Neither is recalled and "
                                  "neither is quoted from a document.",
        "fact_1_the_flag_default": {
            "flag": "useJointNotationRecord",
            "site": "src/composing/composingconfiguration.cpp, at the setDefaultValue anchor",
            "the_line": line,
            "default_is_on": m.group(1) == "true",
        },
        "fact_2_the_build_state": {
            "question": "does any NON-TEST src/ translation unit outside the joint module and "
                        "outside the record adapter itself reference a joint or record symbol?",
            "answer_is_yes": bool(callers),
            "the_callers": callers,
            "why_the_exclusions": "A module referencing its own symbols proves nothing about "
                                  "whether anything CONSUMES it, and a test caller is not a "
                                  "production consumer — which is exactly the claim these "
                                  "comments make. Excluding them is what makes a YES mean what "
                                  "the comments deny.",
        },
    }


def source_files() -> list[str]:
    out = []
    for base, dirs, files in os.walk(SRC):
        dirs[:] = [d for d in dirs if d not in (".git", "build")]
        for f in files:
            if f.endswith((".h", ".hpp", ".cpp", ".cc")) or f == "CMakeLists.txt":
                out.append(os.path.join(base, f))
    return sorted(out)


def comment_blocks(path: str) -> list[dict]:
    """Runs of consecutive comment lines. A block is the unit a claim is made in — the CMake
    entries put the claim and its subject on different lines of one block, so a per-LINE scan
    would miss exactly the group the reconnaissance said is largest."""
    lines = read(path).splitlines()
    blocks, cur, start = [], [], 0
    for n, ln in enumerate(lines, 1):
        if COMMENT.match(ln):
            if not cur:
                start = n
            cur.append(ln)
        elif cur:
            blocks.append({"first_line_number": start, "lines": cur})
            cur = []
    if cur:
        blocks.append({"first_line_number": start, "lines": cur})
    return blocks


def scan() -> list[dict]:
    """The derived candidate population, with each block's own text — the reading surface an
    author needs before a verdict can be written. Exposed as `--list` because a verdict authored
    without reading the block it grades is the thing this whole sweep exists against."""
    candidates = []
    for path in source_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        for b in comment_blocks(path):
            text = "\n".join(b["lines"])
            if STATE_CLAIM.search(text) and SUBJECT.search(text):
                candidates.append({
                    "path": rel,
                    "first_line_number": b["first_line_number"],
                    "first_comment_line": b["lines"][0].strip(),
                    "block": b["lines"],
                })
    return candidates


def build() -> dict:
    facts = configuration_facts()
    candidates = []
    for path in source_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        for b in comment_blocks(path):
            text = "\n".join(b["lines"])
            if STATE_CLAIM.search(text) and SUBJECT.search(text):
                candidates.append({
                    "path": rel,
                    "first_line_number": b["first_line_number"],
                    "first_comment_line": b["lines"][0].strip(),
                    "block": b["lines"],
                })

    keys = {(c["path"], c["first_comment_line"]) for c in candidates}
    unclassified = sorted(k for k in keys if k not in VERDICTS)
    if unclassified:
        raise SystemExit(
            "STOP: candidate comment block(s) with no authored verdict — the population is "
            "derived and grows with the tree, so a new sibling may not enter unclassified:\n  "
            + "\n  ".join(f"{p}  ::  {ln}" for p, ln in unclassified))
    orphans = sorted(k for k in VERDICTS if k not in keys and k not in CORRECTED)
    if orphans:
        raise SystemExit(
            "STOP: authored verdict(s) for a comment block the scan no longer finds — a verdict "
            "may not outlive the comment it grades:\n  "
            + "\n  ".join(f"{p}  ::  {ln}" for p, ln in orphans))

    for c in candidates:
        key = (c["path"], c["first_comment_line"])
        v, why = VERDICTS[key]
        if key in CORRECTED:
            v = TRUE_AT_HEAD
            why = CORRECTED[key]
        c["verdict"], c["why"] = v, why
        c.pop("block")

    false_at_head = [c for c in candidates if c["verdict"] == FALSE_AT_HEAD]
    true_at_head = [c for c in candidates if c["verdict"] == TRUE_AT_HEAD]
    held = [c for c in candidates if c["verdict"] == HELD]

    return {
        "purpose": "Ruling 16's read-only SWEEP: the enumerated family of `src/` comments claiming "
                   "an arm, a flag default or a build state, graded against the configuration "
                   "facts. It edits nothing.",
        "generated_by": "tools/audit/gen_arm_comment_sweep.py",
        "the_ruling": "User, 2026-08-09, Ruling 16 of `cowork_rulings_2026_08_09_second_stop.md`: "
                      "OI-353 is BUNDLED — sweep first so the family is enumerated, then ONE "
                      "comment-only commit over it; the six found sites are 'the found members, "
                      "not the family'; a sibling whose falsity is not mechanical is HELD.",
        "★_the_configuration_facts_every_verdict_is_CHECKED_AGAINST": facts,
        "how_the_candidate_population_is_derived": {
            "the_unit": "a comment BLOCK — a run of consecutive comment lines — and not a line. "
                        "The build-file entries put the state claim and its subject on DIFFERENT "
                        "lines of one block, so a per-line scan would miss precisely the group "
                        "the fourth continuation's reconnaissance reported as largest.",
            "the_two_conditions": "the block makes a STATE claim (dormant / no production "
                                  "consumer / no src caller / not wired / a flag default) AND "
                                  "names this family's subject (the joint module, the notation "
                                  "record, or the flag itself). Both are required, so the many "
                                  "TRUE dormancy comments about other modules never enter.",
            "files_scanned": "every .h/.hpp/.cpp/.cc and every CMakeLists.txt under src/",
            "what_is_authored": "the verdict per block and its reason, keyed by the file and the "
                                "block's own first comment line — never by a line number, so the "
                                "table follows its subject when the file moves (the D-307 "
                                "lesson).",
        },
        "counted": {
            "candidate_blocks": len(candidates),
            "false_at_head": len(false_at_head),
            "true_at_head": len(true_at_head),
            "held_for_a_judgment_about_the_analysis": len(held),
            "files_carrying_a_false_block": sorted({c["path"] for c in false_at_head}),
        },
        "★_the_family_is_LARGER_than_the_row_that_found_it": {
            "what_OI_353_recorded": "six sites saying the production record path is default OFF.",
            "what_the_sweep_finds": "the false set is not confined to that claim: the largest "
                                    "group declares the JOINT MODULE'S OWN dormancy — written "
                                    "before the notation switch and describing a state that "
                                    "switch ended — which neither OI-353 nor the phase-1w side "
                                    "finding names. The ruling predicted exactly this in its own "
                                    "words, and the enumeration is why it is not read off a list.",
        },
        "★_the_comment_only_commit_this_sweep_licensed": {
            "what_it_did": "Ruling 16's second half, performed against this enumeration: every "
                           "FALSE-AT-HEAD block was corrected and nothing else was touched. Each "
                           "correction changes only the false claim — the arm, the flag default, "
                           "or the build state — and leaves every accurate sentence in the block "
                           "standing. No behaviour changes: the diff is comments and build-file "
                           "comments only.",
            "what_it_deliberately_did_NOT_touch": "the ten HELD blocks. Their claims are about "
                                                  "whether a joint-internal module is ON the live "
                                                  "path, which needs the call graph rather than a "
                                                  "file-level fact — the ruling's own clause: a "
                                                  "sibling whose falsity is not mechanical is "
                                                  "HELD, not edited.",
            "blocks_corrected": len(CORRECTED),
            "the_corrections": [
                {"path": p, "former_first_comment_line": ln, "what_was_corrected": what}
                for (p, ln), what in sorted(CORRECTED.items())
            ],
        },
        "verdicts": candidates,
    }


# ---------------------------------------------------------------------------------------------
# THE AUTHORED TABLE.
#
# FALSE-AT-HEAD is claimed only where fact 1 or fact 2 refutes the block MECHANICALLY.  Fact 1:
# the flag's default is TRUE, so every "default OFF" claim about it is false by reading one line.
# Fact 2: non-test src/ translation units outside the joint module reference the joint/record
# symbols, so every "no production consumer / no src caller" claim about them is false by the
# same kind of reading.  Nothing here rests on a judgment about what the analysis computes.
# ---------------------------------------------------------------------------------------------
_CM = "src/composing/analysis/CMakeLists.txt"

# ── FALSE AT HEAD: refuted by fact 1 (the flag default) or fact 2 (a named outside caller) ────
_v(_CM, "# sectionrecordadapter — the RECORD-path variant of analyzeSection (seams part 2, "
        "partition P2b):", FALSE_AT_HEAD,
   "TWO false claims in one block, each refuted by a derived fact. It says the adapter is DORMANT "
   "with 'no src/ caller yet' — fact 2 names non-test src/ callers of analyzeSectionFromRecord; "
   "and it says the named consumer sits 'behind the default-OFF useJointNotationRecord flag' — "
   "fact 1 reads that default as TRUE. The block's substance (what the adapter derives, and that "
   "it never re-decodes) is accurate and is not touched.")
_v(_CM, "# joint/ — THE JOINT KEY/MODE/CHORD ESTIMATOR (the OI-180 sanctioned dual path). The",
   FALSE_AT_HEAD,
   "Says 'DORMANT: no production consumer — nothing in src/ calls any joint symbol'. Fact 2 "
   "refutes that sentence literally, at the files. The rest of the block — what the module reads, "
   "what it never reads, and that its tables load at runtime — is accurate and is not touched.")
_v(_CM, "# jointnotationrecord — the A-native NOTATION OUTPUT-SURFACE RECORD (contract §3): the "
        "one output", FALSE_AT_HEAD,
   "Says 'DORMANT (declared dormancy — named consumer: the seams dispatch)'. The seams dispatch "
   "landed and fact 2 names the callers. The contract description above it is accurate and is not "
   "touched.")
_v("src/composing/analysis/joint/jointnotationproducer.h",
   "// ── The record-producing entry + the two seam views (notation output-surface contract §1) "
   "──────────", FALSE_AT_HEAD,
   "Says the increment 'leaves them DORMANT (declared dormancy — nothing in src/ calls them yet)'. "
   "Fact 2 names the callers of exactly this producer. What the producer composes, and that it "
   "adds no inference, is accurate and is not touched.")
_v("src/composing/analysis/joint/jointnotationrecord.h",
   "// ── The NOTATION OUTPUT-SURFACE RECORD (the A-native record; notation output-surface "
   "contract §3) ──", FALSE_AT_HEAD,
   "Says 'DORMANT (declared dormancy, fact-publication corollary): the NAMED consumer is the seams "
   "dispatch … Nothing in src/ reads it yet.' Fact 2 refutes the last sentence. The §3.1–§3.6 "
   "contract account and the never-re-decodes clause are accurate and are not touched.")
_v("src/composing/analysis/section/sectionrecordadapter.h",
   "// ── composing/analysis/section/sectionrecordadapter ──────────────────────────",
   FALSE_AT_HEAD,
   "The header's own status paragraph, in the same words as its build entry: 'DORMANT (declared "
   "dormancy — no src/ caller yet; … behind the default-OFF useJointNotationRecord flag). "
   "Byte-identical on production by construction: nothing calls it.' Fact 1 refutes the default "
   "and fact 2 refutes the dormancy. Everything else the header states about the mapping is "
   "accurate and is not touched.")
_v("src/notation/internal/notationcomposingbridge.cpp",
   "// Record arm (default OFF, useJointNotationRecord): the note seam is a VIEW into the "
   "whole-score", FALSE_AT_HEAD,
   "One of OI-353's six. Fact 1 refutes the parenthetical; everything the comment says about what "
   "the note seam is, and about the failure behaviour, is accurate and is not touched.")
_v("src/notation/internal/notationcomposingbridge.cpp",
   "// Record path (default OFF, useJointNotationRecord): derive the AnalyzedSection from the "
   "joint", FALSE_AT_HEAD,
   "One of OI-353's six. Fact 1 refutes the parenthetical; the derivation the comment describes is "
   "accurate and is not touched.")
_v("src/notation/internal/notationimplodebridge.cpp",
   "// Record path (default OFF, useJointNotationRecord): derive the AnalyzedSection from the "
   "joint", FALSE_AT_HEAD,
   "One of OI-353's six. Fact 1 refutes the parenthetical; the derivation the comment describes is "
   "accurate and is not touched.")
_v("src/notation/internal/notationtuningbridge.cpp",
   "// ── Harmonic analysis (record path default OFF, useJointNotationRecord) ───", FALSE_AT_HEAD,
   "One of OI-353's six. Fact 1 refutes the parenthetical; the rest of the block, including which "
   "record fields the tuning path reads, is accurate and is not touched.")
_v("src/composing/tests/section_record_adapter_tests.cpp",
   "// Seams part 2, partition P2b — the record-path variant of analyzeSection. Coverage for",
   FALSE_AT_HEAD,
   "A TEST file, but the claim it closes with is about `src/`: 'DORMANT: nothing in src/ calls the "
   "adapter.' Fact 2 refutes it. What the test covers is accurate and is not touched. It is in the "
   "family because the family is the CLAIM, not the directory.")
_v("src/composing/tests/joint_producer_tests.cpp",
   "// Joint estimator — the RECORD-PRODUCING ENTRY + the two seam views (notation output-surface "
   "contract", FALSE_AT_HEAD,
   "Closes 'DORMANT: nothing in src/ reads the producer or the views.' Fact 2 names the readers. "
   "The account of what the tests assert is accurate and is not touched.")
_v("src/composing/tests/joint_record_tests.cpp",
   "// Joint estimator — the NOTATION OUTPUT-SURFACE RECORD (contract §3.1–§3.3) coverage tests "
   "for", FALSE_AT_HEAD,
   "Closes 'The module stays DORMANT — nothing in src/ reads the record.' Fact 2 refutes it. The "
   "account of what the tests check is accurate and is not touched.")

# ── TRUE AT HEAD: the claim is about a DIFFERENT flag or a module that is still dormant ───────
_v(_CM, "# functionrelationallabel — Architectural Layer 5 (FUNCTION), Phase 5c Step 5: the",
   TRUE_AT_HEAD,
   "A Layer-5 module the record path does not reach. Neither fact touches it: no outside src/ "
   "caller is named for it, and the flag it does not mention is not its subject.")
_v(_CM, "# jointkeydecision — the scoped constrained-joint KEY decision (J-key-i;", TRUE_AT_HEAD,
   "Its default-OFF claim is about `jointKeyWiringEnabled()`, a DIFFERENT flag from the notation "
   "record's. Fact 1 is about `useJointNotationRecord` and does not reach it.")
_v(_CM, "# jointfactadapter — the \"score -> facts\" build step (Task C): builds the decoder's "
        "Piece inputs", HELD,
   "Says 'Still DORMANT (driven only by --joint-* diagnostics)'. Deciding this needs the CALL "
   "GRAPH — whether the live record producer drives the fact adapter — rather than a file-level "
   "reference, and neither derived fact establishes it. The ruling's own clause governs: a sibling "
   "whose falsity is not mechanical is HELD, not edited.")
_v("src/composing/analysis/engravingbridge/phraseboundaryview.h",
   "// ── composing/analysis/engravingbridge — the owned phrase-boundary primitive ──",
   TRUE_AT_HEAD,
   "Its CONSUMER STATUS paragraph names the joint-key re-key pass gated on "
   "`jointKeyWiringEnabled()` and the batch diagnostics — a different flag and a different path. "
   "Neither fact reaches it.")
_v("src/composing/analysis/function/forwardoverride.h",
   "// ── composing/analysis/function/forwardoverride ──────────────────────────────",
   TRUE_AT_HEAD,
   "A Layer-5 module with no outside src/ caller named by fact 2; its dormancy claim stands.")
_v("src/composing/analysis/function/functionrelationallabel.h",
   "// ── composing/analysis/function/functionrelationallabel ──────────────────────",
   TRUE_AT_HEAD,
   "Same class as its build entry: a Layer-5 module the record path does not reach, with no "
   "outside src/ caller named by fact 2.")
_v("src/composing/analysis/grouping/groupinglayer.h",
   "// ── composing/analysis/grouping — Architectural Layer 6 (GROUPING) ────────────",
   TRUE_AT_HEAD,
   "A Layer-6 module with no outside src/ caller named by fact 2; its dormancy claim stands.")
_v("src/composing/analysis/region/regionanalyzer.cpp",
   "// ── J-key-iii — the joint re-key pass (the FIRST intentional production behavior",
   TRUE_AT_HEAD,
   "Gated on `jointKeyWiringEnabled()` — a DIFFERENT flag. Fact 1 does not reach it.")
_v("src/composing/analysis/region/regionanalyzer.cpp",
   "// PIN #2 (§15-3, Phase-5c Step-4): re-derive the override-readiness forward-carry",
   TRUE_AT_HEAD,
   "Its default-OFF claim names `jointKeyWiringEnabled()` explicitly — a different flag.")
_v("src/composing/analysis/region/regionanalyzer.cpp",
   "// ── J-key-iii — joint re-key 2-pass (the FIRST intentional production behavior",
   TRUE_AT_HEAD,
   "Same flag, same reason: `jointKeyWiringEnabled()`, not the notation-record flag.")
_v("src/composing/analysis/section/jointkeydecision.cpp",
   "// J-key-iii production wiring flag.  Default OFF ⇒ byte-identical baseline.  The",
   TRUE_AT_HEAD,
   "This block IS the J-key wiring flag's own account of itself, and that flag's default is OFF. "
   "Fact 1 is about a different flag.")
_v("src/composing/analysis/section/sectionanalyzer.cpp",
   "// Layer B — 1-region-island key stabilization.  J-key-iii: when the joint", TRUE_AT_HEAD,
   "Its 'Default OFF ⇒ unchanged' is the J-key wiring flag again, not the notation-record flag.")
_v("src/composing/analysis/section/sectionanalyzer.h",
   "// ── Key-area grouping (shared by the legacy and record arms) ──────────────────",
   TRUE_AT_HEAD,
   "It reaches the scan by naming the record arm, and it makes NO dormancy or default claim about "
   "it — it describes a helper shared by both arms and says one field has no production consumer "
   "reading it AS A PROBABILITY, which neither fact touches.")
_v("src/composing/composingconfiguration.cpp",
   "// Internal migration switch — default TRUE since the user-ratified switch (2026-07-27):",
   TRUE_AT_HEAD,
   "This block is fact 1's own site and states the default correctly, together with what the "
   "explicit false selects. It is the standard the rest of the family is graded against.")
_v("src/composing/icomposinganalysisconfiguration.h",
   "/// INTERNAL MIGRATION SWITCH (default TRUE since the user-ratified switch of", TRUE_AT_HEAD,
   "The interface's own account, and it agrees with fact 1: default TRUE, the record IS the "
   "production notation analysis, the legacy branch compiled and dormant.")

# ── HELD: the falsity, if any, needs the call graph — a judgment, not a file-level fact ───────
_v("src/composing/analysis/joint/jointadapter.h",
   "// The joint estimator's factor log-probability provider — the C++ port of", HELD,
   "Says 'DORMANT (no production consumer)'. No outside src/ file references this symbol, so fact "
   "2 does not refute it literally; whether it is nonetheless ON the live path is a call-graph "
   "question about how the decode is composed. HELD, not edited.")
_v("src/composing/analysis/joint/jointdecoder.h",
   "// The joint estimator's DECODER — the C++ port of the exact block-factorized semi-Markov "
   "Viterbi in", HELD,
   "Same shape as the adapter: 'DORMANT (no production consumer)', with no outside src/ reference "
   "to refute it literally. HELD.")
_v("src/composing/analysis/joint/jointfactadapter.h",
   "// ── The joint estimator's FACT ADAPTER (score -> Piece) ─────────────────────────────────"
   "─────────", HELD,
   "Same shape, and it is the header of the build entry held above for the same reason. HELD.")
_v("src/composing/analysis/joint/jointtables.h",
   "// Runtime loader for the joint estimator's committed generative tables. The frozen tables",
   HELD,
   "Says 'This module is DORMANT — no production path reads it.' Whether the live producer reads "
   "the tables THROUGH the embedded artifacts rather than this loader is exactly the distinction "
   "the block draws elsewhere, and settling it needs the call graph. HELD.")
_v("src/composing/analysis/joint/labelclass.h",
   "// The joint estimator's chord-class value type — the C++ decode-side port of", HELD,
   "Says 'This module is DORMANT — no production path reads it.' Same call-graph question. HELD.")
_v("src/composing/tests/joint_decoder_tests.cpp",
   "// Joint estimator, commit 2: DECODE PARITY against the established Python probe. The C++ "
   "decoder must", HELD,
   "Closes 'the module stays dormant', about the DECODER — the same held call-graph question, "
   "restated in a test header. HELD, and it is named so it moves with the module it describes.")
_v("src/composing/tests/joint_modal_tests.cpp",
   "// Joint estimator — the §3.4 UN-ROUNDED MODAL READING (contract §3.4 / §5.4) coverage tests "
   "for", HELD,
   "Closes 'The module stays DORMANT', about the modal-reading primitive. Same held question.")
_v("src/composing/tests/joint_slice_tests.cpp",
   "// Joint estimator — the POSTERIOR SLICE (notation output-surface contract §3.3 group (i)) "
   "coverage", HELD,
   "Closes 'the module stays dormant', about the posterior slice, which the record attaches. Same "
   "held question.")
_v("src/composing/tests/joint_tables_tests.cpp",
   "// Commit 1 of the joint-estimator C++ module build: the LabelClass value type, the weight",
   HELD,
   "Closes 'The module is DORMANT — no production path reads it', about the loader and the value "
   "type. Same held question as their two headers.")


# ── THE CORRECTIONS the comment-only commit made, each keyed by the block's FORMER first line ──
_fixed(_CM, "# sectionrecordadapter — the RECORD-path variant of analyzeSection (seams part 2, "
            "partition P2b):",
       "CORRECTED. 'DORMANT — no src/ caller yet … behind the default-OFF useJointNotationRecord "
       "flag' now states what is true at HEAD: LIVE on the production notation path since the "
       "2026-07-27 notation switch, the flag defaulting TRUE, with the legacy path compiled and "
       "dormant behind an explicit false. Nothing else in the entry moved.")
_fixed(_CM, "# joint/ — THE JOINT KEY/MODE/CHORD ESTIMATOR (the OI-180 sanctioned dual path). The",
       "CORRECTED. 'DORMANT: no production consumer — nothing in src/ calls any joint symbol' now "
       "states both adoptions: the batch/corpus surface at OI-178 (2026-07-26) and the in-app "
       "notation surface at the notation switch (2026-07-27). Nothing else in the entry moved.")
_fixed(_CM, "# jointnotationrecord — the A-native NOTATION OUTPUT-SURFACE RECORD (contract §3): "
            "the one output",
       "CORRECTED. 'DORMANT (declared dormancy — named consumer: the seams dispatch)' now records "
       "that the named consumer landed and the notation bridges read the record. The §3.1–§3.6 "
       "contract account is untouched.")
_fixed("src/composing/analysis/joint/jointnotationproducer.h",
       "// ── The record-producing entry + the two seam views (notation output-surface contract "
       "§1) ──────────",
       "CORRECTED. 'leaves them DORMANT (declared dormancy — nothing in src/ calls them yet)' now "
       "records that the seams-part-2 consumer side LANDED and the producer and both views are "
       "live. What the producer composes, and that it adds no inference, is untouched.")
_fixed("src/composing/analysis/joint/jointnotationrecord.h",
       "// ── The NOTATION OUTPUT-SURFACE RECORD (the A-native record; notation output-surface "
       "contract §3) ──",
       "CORRECTED. 'DORMANT (declared dormancy …). Nothing in src/ reads it yet.' now records that "
       "the in-app notation path reads the record. The pure-function clause and the whole contract "
       "account are untouched.")
_fixed("src/composing/tests/joint_producer_tests.cpp",
       "// Joint estimator — the RECORD-PRODUCING ENTRY + the two seam views (notation "
       "output-surface contract",
       "CORRECTED. 'DORMANT: nothing in src/ reads the producer or the views' now records that the "
       "notation bridges read them. What the tests assert is untouched.")
_fixed("src/composing/tests/joint_record_tests.cpp",
       "// Joint estimator — the NOTATION OUTPUT-SURFACE RECORD (contract §3.1–§3.3) coverage "
       "tests for",
       "CORRECTED. 'The module stays DORMANT — nothing in src/ reads the record' now records that "
       "the notation bridges read it. What the tests check is untouched.")
_fixed("src/composing/tests/section_record_adapter_tests.cpp",
       "// Seams part 2, partition P2b — the record-path variant of analyzeSection. Coverage for",
       "CORRECTED. 'DORMANT: nothing in src/ calls the adapter' now records that the notation "
       "bridges call it. The coverage description is untouched.")
_fixed("src/notation/internal/notationcomposingbridge.cpp",
       "// Record arm (default OFF, useJointNotationRecord): the note seam is a VIEW into the "
       "whole-score",
       "CORRECTED — one of OI-353's six. 'default OFF' now reads 'default ON … the production "
       "notation analysis since the user-ratified notation switch of 2026-07-27'. Everything the "
       "block says about the seam and its failure behaviour is untouched.")
_fixed("src/notation/internal/notationcomposingbridge.cpp",
       "// Record path (default OFF, useJointNotationRecord): derive the AnalyzedSection from the "
       "joint",
       "CORRECTED — one of OI-353's six. Same correction, same untouched substance.")
_fixed("src/notation/internal/notationimplodebridge.cpp",
       "// Record path (default OFF, useJointNotationRecord): derive the AnalyzedSection from the "
       "joint",
       "CORRECTED — one of OI-353's six. Same correction, same untouched substance.")
_fixed("src/notation/internal/notationtuningbridge.cpp",
       "// ── Harmonic analysis (record path default OFF, useJointNotationRecord) ───",
       "CORRECTED — one of OI-353's six. Same correction; which record fields the tuning path "
       "reads is untouched.")
_v("src/composing/analysis/section/sectionrecordadapter.cpp",
   "// ── The record-path variant of analyzeSection ────────────────────────────────", FALSE_AT_HEAD,
   "★ THE BLOCK THE FIRST RUN OF THIS SWEEP MISSED, and it is recorded as a miss rather than "
   "quietly absorbed. It said 'DORMANT — no src/ caller yet', which fact 2 refutes. It escaped the "
   "population because the subject pattern matched 'record path' with a space and this block writes "
   "'record-path' with a hyphen; the pattern is widened above and the miss is named there. It was "
   "found by ANOTHER tool's STOP — the phase-1w legacy verification, whose own side-finding table "
   "carries the same site — which is the cross-check working.")
_fixed("src/composing/analysis/section/sectionrecordadapter.cpp",
       "// ── The record-path variant of analyzeSection "
       "────────────────────────────────",
       "CORRECTED. 'DORMANT — no src/ caller yet' now records that the notation bridges call the "
       "adapter. The pointer to the header for the contract and the isolation rules is untouched.")
_fixed("src/composing/analysis/section/sectionrecordadapter.h",
       "// ── composing/analysis/section/sectionrecordadapter ──────────────────────────",
       "CORRECTED. The header's status paragraph — 'DORMANT (declared dormancy — no src/ caller "
       "yet; … behind the default-OFF useJointNotationRecord flag)' — now states the live arm, the "
       "true default, and what an explicit false selects. The mapping account is untouched. The "
       "block stays in the derived population because it still names the legacy path as dormant, "
       "which is true.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--list", action="store_true",
                    help="print the derived candidate blocks with their text and stop — the "
                         "reading surface a verdict must be authored from")
    args = ap.parse_args()
    if args.list:
        for c in scan():
            print(f"=== {c['path']}:{c['first_line_number']}")
            for ln in c["block"]:
                print("   " + ln.rstrip())
        return 0
    art = build()
    text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = read(OUT) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the files: arm_comment_sweep.json does not re-derive")
            return 1
        print("the Ruling-16 sweep re-derives from the files")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    c = art["counted"]
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  {c['candidate_blocks']} candidate block(s): {c['false_at_head']} false at HEAD, "
          f"{c['true_at_head']} true, {c['held_for_a_judgment_about_the_analysis']} held")
    return 0


if __name__ == "__main__":
    sys.exit(main())
