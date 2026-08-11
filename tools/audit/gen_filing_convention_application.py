#!/usr/bin/env python3
"""gen_filing_convention_application.py -- the DERIVED candidate set for the filing convention.

THE CONVENTION is the user's Ruling 62 of 2026-08-11
(`cowork_rulings_2026_08_11_fourteenth_stop.md`), homed at `cowork_design_doc_template.md` beside
the kind list.  It is NOT restated here (#6).  This file finds the documents it applies to.

WHAT IS DERIVED and what is AUTHORED, stated first because everything below depends on it:

DERIVED  - the candidate population, from SIGNATURES OF OVERTAKING carried in a document's own
           banner or closing line, over a NAMED surface set.  The signatures are the derivation;
           the surface set is authored and stated in full below.
AUTHORED - the per-candidate VERDICT (which branch of the convention it falls in, or HELD), each
           with its reason.  A verdict is a judgment and is marked as one on every row, so no
           reader takes it for a measured quantity (D-431).

WHY SIGNATURES OF OVERTAKING RATHER THAN SIGNATURES OF BEING A REPORT.  The convention governs a
document the record has left behind.  Enumerating every report in the tree would enumerate a
different class -- most reports are accurate records of what they found and are overtaken by
nothing.  What this derivation looks for is a document whose OWN TEXT signals that its subject has
moved: a closing line declaring its findings resolved, deleted or superseded, or a top banner whose
status a later ruling has falsified.

THE THREE STOPS:
  1. a SEED the record already knows about that the derivation does not find -- the derivation is
     then NOT SOUND, is reported as such, and its population stays advisory (D-661);
  2. a derived candidate with no authored verdict -- an unclassified candidate is a STOP, never a
     silent pass;
  3. an authored verdict for a document the derivation no longer carries -- the tree moving under
     the table.

THE BOUND ON THIS DERIVATION, stated on its own artifact rather than measured (D-673, the user's
Ruling 60 of the same date): the reach of these signatures against the text they scan has never
been measured, so an empty result over any surface bounds nothing.  The test D-673 fixes is whether
an ANALYSIS DECISION consumes the enumeration; none does -- what consumes it is a filing act over
documents -- so the bound is stated and a detection measurement is not owed.

Usage:
    python tools/audit/gen_filing_convention_application.py [--check] [--derive-only]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from output_encoding import use_utf8_output                       # noqa: E402  (path set above)

use_utf8_output()

OUT = HERE / "filing_convention_application.json"
REGISTER = HERE / "decisions" / "backbone_decisions.json"

# ── AUTHORED: the named surface set the derivation runs over ────────────────────────────────────
#
# "Named surfaces" is D-661's own requirement: a completeness claim means complete relative to a
# NAMED derivation and to nothing wider.  These are this project's own documentation surfaces.
# MuseScore's upstream documentation, the source tree and the build directories are excluded
# because the convention is about OUR record; the two registers are excluded because a register is
# its own kind with its own rules (the kind list says so).
SURFACE_GLOBS = [
    "*.md",                        # the repository root's own documents
    "docs/*.md",
    "ratification_surfaces/*.md",
    "tools/*.md",
    "tools/*/*.md",
]
EXCLUDED_DIRS = {
    "decisions", "open_items",     # the two registers -- their own kind, their own rules
    "old_docs", "apidocs_static",  # MuseScore's own documentation
}
EXCLUDED_NAMES = {
    "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
}

# ── DERIVED: the two signatures of OVERTAKING ───────────────────────────────────────────────────
#
# S1 -- the CLOSING-LINE fate signature.  Within the document's last lines, a line that declares
#       its own subject's fate: a status line, or a line naming a commit, that says the thing the
#       document describes was resolved, deleted, removed, retired, superseded or falsified.
S1_TAIL_LINES = 25
S1_FATE = re.compile(
    r"(?i)\b(resolved in|deleted|removed|retired|superseded|falsified|no longer (?:exists|present))\b")
S1_MARKER = re.compile(r"(?i)(^\s*>?\s*\*{0,2}status\b|[0-9a-f]{7,40})")

# S2 -- the BANNER-over-a-falsified-subject signature.  The top block carries a status a later act
#       may have overtaken, AND the register holds an entry whose content is falsified, shelved or
#       superseded and whose own record names this document.
S2_BANNER_LINES = 20
S2_STATUS = re.compile(
    r"(?i)\b(draft|ratification-gated|for sign-off|no code|proposed|pending)\b")
SUPERSEDED_STATUSES = {"falsified", "shelved", "superseded-by", "superseded-in-fact"}

# ── AUTHORED: the seeds -- what the record already knows, demoted to SEED VERDICTS (D-661) ───────
#
# They are NOT the population.  They are what the derivation is measured against: a derivation that
# misses a document the record already holds cannot be trusted to have found the ones it does not.
SEEDS = {
    "docs/symbol_input_audit.md":
        "OPEN_ITEMS.md OI-322 -- a completed audit describing, in the present tense, code its own "
        "closing line says was deleted.",
    "docs/stage4c_cadence_key_design.md":
        "OPEN_ITEMS.md OI-332 item (3) -- a design whose approach the register records FALSIFIED "
        "one day later, carrying no note of it.",
}

BRANCH_ONE = "BRANCH ONE -- a dated report: RE-BANNER as a historical record, body untouched"
BRANCH_TWO = "BRANCH TWO -- a live governing surface: CORRECT the body"
CONFORMANT = "NO ACT OWED -- the document already states its own fate where a reader meets it first"
HELD = "HELD to the user -- the two branches do not decide it"

# ── AUTHORED: the verdict per derived candidate ─────────────────────────────────────────────────
#
# Each verdict is a judgment made by READING the document's own banner and closing line in place.
# `acted` records whether the act was performed, and by which wave -- so a reader can tell a
# verdict that is owed from one that is discharged.
def _v(verdict: str, why: str, acted: str | None = None) -> dict:
    row = {"verdict": verdict, "why": why}
    if acted:
        row["acted"] = acted
    return row


APPLIED = ("2026-08-11, `cc_instruction_return_continuation_14.md` Task 0/2, on the user's "
           "Ruling 62")

VERDICTS: dict[str, dict] = {
    "STATUS.md": _v(
        BRANCH_TWO,
        "A live status surface a session reads at start — the kind list's kind 7. Its job is to be "
        "true now, so it is corrected rather than bannered. The signature fires on a dated entry "
        "INSIDE the running log, which the surface's own convention moves to its archive; the act "
        "the record actually owes here is `OPEN_ITEMS.md` OI-47, which names four submission-era "
        "sections and the banner half it asks for."),
    "STATUS_ARCHIVE.md": _v(
        CONFORMANT,
        "It IS the historical record, and it says so in its own first two lines: moved verbatim out "
        "of the live status surface, NOT part of the session-start read, nothing edited. That is "
        "the branch-one banner already standing."),
    "cc_instruction_phase1s_stale_rules_and_enumeration.md": _v(
        CONFORMANT,
        "A DISPATCH — kind 3 of the kind list, an exempt genre. A dispatch is an instruction to one "
        "session, dated by construction, and the record of what it did is the report or returns "
        "entry it produced. It describes no state the record has left behind."),
    "cc_instruction_phase1z_commit_and_instrument_record.md": _v(
        CONFORMANT,
        "A DISPATCH, on the same ground as its sibling above."),
    "cc_key_grading_and_calibration_rebaseline_report.md": _v(
        CONFORMANT,
        "A dated report carrying its date, its dispatch and the ruling it executed at the head. The "
        "signature fires on the report's own account of a snapshot IT took — a finding, not a fate "
        "that has overtaken it."),
    "cc_oi207_residual_pass_report.md": _v(
        CONFORMANT,
        "Its banner opens `Status: DELIVERED 2026-08-02` with the freeze it ran under. The "
        "signature fires on a measured line count inside the body."),
    "cc_stage2a_wip_triage_report.md": _v(
        CONFORMANT,
        "A dated read-only classification whose banner states its scope discipline and its date. "
        "The signature fires on a QUESTION the report puts to its reader, not on a fate."),
    "cc_stage3_4i_dossier.md": _v(
        CONFORMANT,
        "Header carries its date, its base commit and its owner. The signature fires on the "
        "dossier's own finding that no gate was retired — the opposite of a fate declaration."),
    "cc_stage5_phase2_2d_report.md": _v(
        CONFORMANT,
        "Header carries its dispatch, the HEAD it ran at and its nature (measurement only, no "
        "adoption). The signature fires on that scope statement."),
    "cowork_phase2_architecture_review.md": _v(
        HELD,
        "A dated architecture review whose banner marks five load-bearing claims as PENDING a later "
        "empirical pass. Whether that pass overtook the review is not settled by either branch, and "
        "the superseded register entry homed in it is superseded in its own right rather than by "
        "anything about this document. Held rather than bannered by stretch."),
    "docs/iter92_joint_bass_chord_scoring.md": _v(
        HELD,
        "Its banner is already updated and accurate — the design is implemented and committed, and "
        "the follow-up scope it names has landed. Its SUBJECT is the legacy scorer awaiting "
        "deletion at the retirement map, so whether it becomes a historical record is decided by "
        "that scheduled event and not by this convention."),
    "docs/key_path_design.md": _v(
        BRANCH_TWO,
        "A live design surface, and both of its defects already have rows that name the act: "
        "`OPEN_ITEMS.md` OI-317 (its banner says the document is uncommitted and under a commit "
        "hold, which is false at HEAD) and OI-315 (its §2.1/§5 self-contradiction about the removed "
        "piece-start shortcut). The convention says which branch; those rows say what to write."),
    "docs/policy2_coalescing_map.md": _v(
        CONFORMANT,
        "Dated at the head, and its own opening table is a CLOSED-DIVERGENCES table that states "
        "each subject's fate with the commit that closed it, where a reader meets it first. That is "
        "what branch one exists to produce, arrived at by the document's own construction."),
    "docs/stage4b_design.md": _v(
        BRANCH_ONE,
        "Its banner reads `DRAFT — ratification-gated … No code is written until this design is "
        "ratified`. The design LANDED, and the decision it carries is recorded superseded-in-fact "
        "in the register. So a reader meeting the banner first is told the opposite of what "
        "happened — the OI-322 shape one document over.",
        APPLIED),
    "docs/symbol_input_audit.md": _v(
        BRANCH_ONE,
        "The SEED, and the instance the ruling names first: the body describes `analyzeScoreJazz`, "
        "the injection flag and the jazz-mode field as live code across five sections, while the "
        "final line says they were deleted. A reader who stops before the last line is told the "
        "opposite of HEAD.",
        APPLIED),
    "ratification_surfaces/cowork_pending_ratifications_next_session.md": _v(
        CONFORMANT,
        "★ IT ALREADY CARRIES THE BRANCH-ONE BANNER, and it is the model instance: `STATUS: RULED "
        "AND APPLIED (user, 2026-08-03) — SUPERSEDED BY ITS OWN EXECUTION`, with the body `retained "
        "unedited beneath, under #12, as the record of what was put to the user and in what words`. "
        "Nothing is owed, and the convention did not invent this shape — it generalizes it."),
}

# ── The ruling's own named instances that this derivation does NOT carry ────────────────────────
#
# Recorded here so the acts performed under Ruling 62 are all readable in one place, and so that a
# document acted on but absent from the population cannot be mistaken for one the derivation found.
NAMED_BY_THE_RULING_BUT_NOT_DERIVED = {
    "docs/stage4c_cadence_key_design.md": {
        "why_the_ruling_names_it": (
            "`OPEN_ITEMS.md` OI-332 item (3): it designs the key-agnostic local cadence detector the "
            "register records FALSIFIED at its precision ceiling one day later, and carries no note "
            "of it — while carrying an inline supersession note elsewhere, so the omission is not "
            "simple neglect."),
        "why_the_derivation_MISSES_it": (
            "★ THIS IS THE DERIVATION'S OWN SOUNDNESS FAILURE AND IT IS DIAGNOSED RATHER THAN "
            "PATCHED. S2 asks the register for an entry whose STATUS is falsified/shelved/"
            "superseded. The entry that records this falsification is D-290, and its own status is "
            "LIVE — the FINDING stands; what was falsified is the approach the document designs. So "
            "the signature encodes a wrong premise: a falsified approach does not show up as a "
            "falsified-status entry. It is REPORTED and the signature is NOT re-tuned here, because "
            "widening a derivation at the moment its own seed exposes it is one step from fitting "
            "it to the cases that motivated it (DT-2)."),
        "verdict": BRANCH_ONE,
        "acted": APPLIED,
    },
}


def _iter_surface_files() -> list[Path]:
    seen: dict[str, Path] = {}
    for pattern in SURFACE_GLOBS:
        for p in sorted(ROOT.glob(pattern)):
            if not p.is_file():
                continue
            if p.name in EXCLUDED_NAMES:
                continue
            if any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts):
                continue
            seen[p.relative_to(ROOT).as_posix()] = p
    return [seen[k] for k in sorted(seen)]


def _register_falsified_documents() -> dict[str, list[str]]:
    """Documents the register names in a FALSIFIED / SHELVED / SUPERSEDED entry's own record."""
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    by_doc: dict[str, list[str]] = {}
    names = [p.relative_to(ROOT).as_posix() for p in _iter_surface_files()]
    for e in data["decisions"]:
        if e.get("status") not in SUPERSEDED_STATUSES:
            continue
        text = " ".join(str(e.get(f) or "") for f in
                        ("home", "rationale", "status_source", "superseded_by"))
        for n in names:
            if n in text or Path(n).name in text:
                by_doc.setdefault(n, []).append(e["id"])
    return {k: sorted(set(v)) for k, v in by_doc.items()}


def derive() -> dict:
    falsified = _register_falsified_documents()
    rows = []
    for p in _iter_surface_files():
        rel = p.relative_to(ROOT).as_posix()
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        body = [ln for ln in lines if ln.strip()]
        tail = body[-S1_TAIL_LINES:]
        banner = body[:S2_BANNER_LINES]

        s1_hits = [ln.strip() for ln in tail if S1_FATE.search(ln) and S1_MARKER.search(ln)]
        s2_status = [ln.strip() for ln in banner if S2_STATUS.search(ln)]
        s2 = bool(s2_status) and rel in falsified

        if not s1_hits and not s2:
            continue
        rows.append({
            "document": rel,
            "signature": ([f"S1 closing-line fate ({len(s1_hits)} line(s))"] if s1_hits else [])
                         + (["S2 banner over a falsified/shelved/superseded subject"] if s2 else []),
            "s1_lines": s1_hits[:3],
            "s2_register_entries": falsified.get(rel, []) if s2 else [],
            "is_a_seed": rel in SEEDS,
        })
    return {"rows": rows, "ids": [r["document"] for r in rows]}


def build() -> dict:
    derived = derive()
    ids = derived["ids"]

    # STOP 1 -- soundness against the seeds. A derivation that misses what the record already holds
    # cannot be trusted with what it does not, so this is REPORTED and the population goes advisory
    # rather than being narrowed to fit (D-661; fitting it to the seeds is DT-2).
    missed_seeds = sorted(s for s in SEEDS if s not in ids)

    # STOP 2 -- an unclassified candidate.
    unclassified = sorted(i for i in ids if i not in VERDICTS)
    if unclassified:
        raise SystemExit(
            "STOP: derived candidates with no authored verdict: " + ", ".join(unclassified)
            + ". An unclassified candidate is a STOP, never a silent pass (D-661).")

    # STOP 3 -- a verdict for a document the derivation no longer carries.
    stray = sorted(v for v in VERDICTS if v not in ids)
    if stray:
        raise SystemExit(
            "STOP: authored verdicts for documents the derivation does not carry: "
            + ", ".join(stray) + " -- the tree has moved under the table.")

    for r in derived["rows"]:
        r.update(VERDICTS[r["document"]])
        r["authored"] = "the verdict and its reason. The signature and the population are derived."

    by_branch: dict[str, list[str]] = {}
    for r in derived["rows"]:
        by_branch.setdefault(r["verdict"], []).append(r["document"])

    return {
        "purpose": (
            "The DERIVED candidate set for the filing convention (the user's Ruling 62 of "
            "2026-08-11), with an authored verdict per candidate. NOT a completion statement and "
            "not an authorization for any fix, design or inference change."
        ),
        "generated_by": "tools/audit/gen_filing_convention_application.py",
        "the_convention_is_homed_elsewhere_and_is_not_restated_here":
            "cowork_design_doc_template.md, beside the kind list (#6).",
        "what_is_derived_and_what_is_authored": {
            "derived": "the candidate population, from signatures of OVERTAKING carried in a "
                       "document's own banner or closing line, over the named surface set below",
            "authored": "the surface set, the signatures themselves, the seeds, and the VERDICT "
                        "per candidate with its reason",
            "why_it_matters": "A verdict is a judgment about a document and can be wrong; a "
                              "population is derived and cannot (D-431).",
        },
        "the_named_surface_set": {
            "globs": SURFACE_GLOBS,
            "excluded_directories": sorted(EXCLUDED_DIRS),
            "excluded_names": sorted(EXCLUDED_NAMES),
            "why_these": (
                "This project's own documentation. MuseScore's upstream documentation, the source "
                "tree and the build directories are outside the convention's subject; the two "
                "registers are excluded because a register is its own kind under the kind list, "
                "with its own rules."
            ),
        },
        "the_signatures": {
            "S1_closing_line_fate": (
                "Within the document's last non-blank lines, a line that declares its own subject's "
                "fate -- resolved, deleted, removed, retired, superseded or falsified -- carried on "
                "a status line or beside a commit name."
            ),
            "S2_banner_over_a_falsified_subject": (
                "The top block carries a status a later act may have overtaken (draft, "
                "ratification-gated, for sign-off, no code, proposed, pending) AND the register "
                "holds an entry whose content is falsified, shelved or superseded and whose own "
                "record names this document."
            ),
            "why_overtaking_rather_than_report_kind": (
                "The convention governs a document the record has LEFT BEHIND. Enumerating every "
                "report in the tree enumerates a different class -- most reports are accurate "
                "records of what they found and are overtaken by nothing."
            ),
        },
        "★_the_bound_on_this_derivation_STATED_rather_than_measured": {
            "the_bound": (
                "The reach of these two signatures against the text they scan HAS NEVER BEEN "
                "MEASURED. An empty result over any surface therefore bounds nothing, and this "
                "enumeration is ADVISORY: it locates candidates, and its silence is not evidence "
                "that none exists."
            ),
            "why_a_measurement_is_not_owed": (
                "D-673 (user, Ruling 60 of 2026-08-11): where an enumerating pattern's reach is "
                "unmeasured the bound may be stated on the pattern's own artifact instead, and the "
                "test is whether an ANALYSIS DECISION consumes the enumeration. None does -- what "
                "consumes this is a filing act over documents. The test is applied PER "
                "ENUMERATION and this bound is not inherited by any other."
            ),
        },
        "the_ruling_s_own_instances_this_derivation_does_NOT_carry":
            NAMED_BY_THE_RULING_BUT_NOT_DERIVED,
        "the_seeds_and_the_soundness_check": {
            "what_a_seed_is": (
                "A document the record already knows is overtaken, demoted to a SEED VERDICT rather "
                "than standing as the population (D-661). Seeds measure the derivation; they are "
                "not the answer."
            ),
            "seeds": SEEDS,
            "seeds_the_derivation_MISSED": missed_seeds,
            "verdict": ("SOUND against its seeds" if not missed_seeds else
                        "NOT SOUND -- it misses a document the record already holds, so the "
                        "population stays advisory and is NOT narrowed to fit (DT-2)"),
        },
        "counted": {
            "candidates": len(ids),
            "seeds": len(SEEDS),
            "by_verdict": {k: len(v) for k, v in sorted(by_branch.items())},
        },
        "by_verdict": {k: sorted(v) for k, v in sorted(by_branch.items())},
        "rows": derived["rows"],
        "what_this_file_does_NOT_do": [
            "It performs no banner insertion and no body correction -- it says which documents the "
            "convention reaches and what each is owed.",
            "It moves no open-items status, no register entry and no home.",
            "It touches no golden, no corpus of scores and nothing in `tools/robust_stop/`, and it "
            "authorizes no fix, design or inference change.",
        ],
    }


def main(argv: list[str]) -> int:
    if "--derive-only" in argv:
        d = derive()
        for r in d["rows"]:
            print(f"  {r['document']}  {r['signature']}  seed={r['is_a_seed']}")
            for ln in r["s1_lines"]:
                print(f"      | {ln[:160]}")
        print(f"{len(d['ids'])} candidate(s)")
        return 0
    data = build()
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        if not OUT.exists():
            print(f"FAIL: {OUT.name} does not exist")
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print(f"FAIL: {OUT.name} differs from what the generator now produces")
            return 1
        c = data["counted"]
        print(f"PASS: {OUT.name} re-derives byte-identically ({c['candidates']} candidate(s); "
              f"{data['the_seeds_and_the_soundness_check']['verdict']})")
        return 0
    OUT.write_text(text, encoding="utf-8")
    c = data["counted"]
    print(f"wrote {OUT}")
    print(f"  {c['candidates']} candidate(s); by verdict: {c['by_verdict']}")
    print(f"  seeds: {data['the_seeds_and_the_soundness_check']['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
