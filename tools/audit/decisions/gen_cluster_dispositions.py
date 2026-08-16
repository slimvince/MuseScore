#!/usr/bin/env python3
"""OI-207 adjudication, Task 3 — give every harvested cluster a recorded disposition.

A layer OVER the harvest (`decision_candidates.json`) and the clustering
(`decision_clusters.json`), which it never writes.  It reads the hand-authored
backbone (`backbone_decisions.json` — the adjudication's Task-1/Task-2 judgment,
enumerated by reading the ARCHITECTURE.md layer specifications in full) and
assigns each of the 14,460 clusters exactly one disposition from the ratified
vocabulary.

The permitted dispositions (OI-207 dispatch, Task 3):

    restates        the cluster restates a backbone decision (named)
    not-a-decision  narrative, an instruction to a working session, a heading
    boilerplate     the labelled boilerplate bucket, confirmed
    no-spec-home    a decision whose only recorded home is outside a layer
                    specification — the valuable class, which feeds Task 4
    unresolved      could not be told.  Permitted and wanted: an honest
                    unresolved beats a guessed disposition, and the count is
                    itself a finding about the record's legibility.

Every disposition is produced by a NUMBERED, STATED bulk rule; the rule that
fired and the number of clusters it covered are both recorded, so the judgment
is reviewable rather than hidden inside a total.  No cluster may carry more than
one disposition and none may carry none — `--check` proves both.

Usage
    python tools/audit/decisions/gen_cluster_dispositions.py --verify
        Establishment pass (#19): every backbone verbatim quote must be found in
        the file it is cited to.  Exits nonzero on any miss.

    python tools/audit/decisions/gen_cluster_dispositions.py
        Writes cluster_dispositions.json / .csv / disposition_manifest.json.

    python tools/audit/decisions/gen_cluster_dispositions.py --check
        Re-reads the emitted artifacts and proves the coverage guarantee.

    python tools/audit/decisions/gen_cluster_dispositions.py --producible
        PRODUCIBILITY pass: compiles every register pattern and runs the whole
        derivation in memory, writing nothing.  Exits nonzero if the layer could
        not be produced at all.

WHY PRODUCIBILITY IS A SEPARATE CHECK FROM `--check` (added 2026-08-07 on the user's
ruling; `OPEN_ITEMS.md` OI-333).  `--check` RE-READS the emitted artifacts; the write
path RE-DERIVES them, and the two share no code path.  So `--check` proves that the
committed artifact covers every cluster exactly once — which was true throughout — and
is structurally incapable of noticing that the artifact can no longer be PRODUCED.  It
did not notice: six register patterns carried unescaped markdown emphasis, the write
mode died with an uncaught `re.PatternError`, and the check went on passing at every
tree.  `--producible` is the missing half and is deliberately NARROW.  `--check`'s
re-read semantics are UNCHANGED: a coverage proof and a producibility proof are
different concerns, and making one check do both would make the coverage guarantee fail
for every reason a regeneration can fail (#6 — two narrow checks, not one broad one).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent

sys.path.insert(0, str(HERE.parent))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

CANDIDATES = HERE / "decision_candidates.json"
CLUSTERS = HERE / "decision_clusters.json"
BACKBONE = HERE / "backbone_decisions.json"

OUT_JSON = HERE / "cluster_dispositions.json"
OUT_CSV = HERE / "cluster_dispositions.csv"
OUT_MANIFEST = HERE / "disposition_manifest.json"

DISPOSITIONS = ("restates", "not-a-decision", "boilerplate", "no-spec-home", "unresolved")

# ── The bulk rules, in the order they are applied.  First match wins. ─────────
# Each entry: (rule id, the rule as it is stated in the report).
RULES = [
    ("BR-1", "The clustering layer already labelled this cluster boilerplate "
             "(a recurring heading, table header row, or standing dispatch instruction line). "
             "Confirmed, not re-judged."),
    ("BR-2", "Every occurrence in the cluster is a section HEADING. A heading names a subject; "
             "it does not state a decision."),
    ("BR-3", "The cluster's text matches at least one backbone decision whose home IS a layer "
             "specification. Recorded as restating that decision (named)."),
    ("BR-4", "The cluster's text matches one or more backbone decisions, ALL of which are recorded "
             "outside any layer specification. Recorded as a decision with no layer-specification "
             "home (named) — the Task-4 documentation-gap class."),
    ("BR-5", "The text is an instruction to a working session or dispatch scaffolding "
             "(a read-only / no-src-change banner, a push or commit instruction, a session-start "
             "reading instruction, a build-and-test instruction), not a decision about the system."),
    ("BR-6", "A Claude Code session report or dispatch whose text is a measurement or delivery "
             "narrative (it carries a figure, a test count, a commit hash, or a delivery/verification "
             "verb) and matches no backbone decision. A report of work done, not a ruling."),
    ("BR-7", "A table row admitted by the harvest's BROAD signature tier only — an inventory or "
             "status cell, not a stated decision."),
    # ── BR-9 … BR-13 were added by the OI-207 residual second pass (2026-08-02).  Each
    #    clears a class the first pass left in BR-8, and each is stated so it can be
    #    disputed a class at a time.  All five run AFTER BR-3/BR-4, so a cluster that
    #    names a backbone decision is never swept by them.
    ("BR-9", "The unit is a list lead-in: with markdown stripped its text ends in a colon and "
             "contains no sentence-ending period before it, so it introduces a list whose items "
             "are separate units. Like a heading (BR-2) it names a subject and states nothing."),
    ("BR-10", "The unit is a row, or a section header, of the OPEN-ITEMS REGISTER (`OPEN_ITEMS.md` "
              "or `open_items/OI-*.md`). That register records issues, their status and their "
              "provenance; the ratified ruling 1 on `open_items/OI-208.md` puts decisions in the "
              "decisions register and non-conformance here. A row of it is a tracked issue."),
    ("BR-11", "The unit is in a Claude Code DISPATCH (`cc_instruction_*.md`) and carries none of "
              "the stated ruling words (RULING_VOCABULARY below). A dispatch is an instruction to "
              "a working session — scope, task, stop condition, reporting requirement. The ratified "
              "decisions-register rules make a dispatch a CITER of decisions (rule (b)) and put a "
              "new ratification in the register in the commit that records it (rule (c)), so a "
              "dispatch is never a home of record."),
    ("BR-12", "The unit is in a Claude Code session REPORT (`cc_*.md` that is not a dispatch) and "
              "carries none of the stated ruling words. A report records work done. Same "
              "register-rule reasoning as BR-11. This is BR-6 widened from its narrative-pattern "
              "test to the whole report class, minus the ruling vocabulary."),
    ("BR-13", "The unit is a comment in a TEST file (`src/**/tests/**`) and carries none of the "
              "stated ruling words. A test comment states what the test pins; the decision it pins "
              "is stated in the specification, which is where BR-3 finds it."),
    # ── BR-14 … BR-16 were added by the phase-1d enumeration wave (2026-08-02).  Each widens an
    #    existing rule's stated reasoning to prose of the same surface, under the SAME ruling
    #    vocabulary, and each runs after BR-3/BR-4.  The wave deliberately added NO rule over
    #    `tools/` script comments or `src` production comments: those two surfaces are RESERVED
    #    (see UNRESOLVED_RESERVATIONS below), because sweeping them would pre-empt the sealed
    #    measurement-tools partition and the scoring-model reading that own them.
    ("BR-14", "The unit is narrative prose of the OPEN-ITEMS register (`OPEN_ITEMS.md` or "
              "`open_items/OI-*.md`) that is not a row or a section header, and carries none of "
              "the stated ruling words. BR-10's reasoning, widened from the rows to the prose "
              "around them: a detail file carries narrative and provenance only and is never a "
              "status of record (its own standing banner), so its prose tracks an issue."),
    ("BR-15", "The unit is in the SESSION HANDOFF (`cowork_handoff.md`) and carries none of the "
              "stated ruling words. A handoff block hands a session over; `OPEN_ITEMS.md` OI-240 "
              "and OI-266 establish that it tracks work and is not a home for a standing "
              "decision, and the six standing rules that were recorded there are now homed "
              "(D-249…D-254). Same register-rule reasoning as BR-11/BR-12."),
    ("BR-16", "The unit is a row of the defect-type catalog (`DEFECT_TYPES.md`). The catalog "
              "itself is register entry D-213; a row of it is a catalogued problem TYPE with its "
              "detection signature, which is a diagnostic aid, not a decision about the system."),
    ("BR-17", "The unit is in the SESSION-HANDOFF ARCHIVE (`cowork_handoff_archive.md`) and carries "
              "none of the stated ruling words. BR-15's reasoning, and ONLY because the phase-1e "
              "second-partition wave READ THIS FILE IN FULL (all 5,704 lines, 2026-08-02): the "
              "archive is the handoff's own superseded blocks moved verbatim, and `OPEN_ITEMS.md` "
              "OI-240/OI-266 establish that a handoff block tracks work and is not a home for a "
              "standing decision. The archives are swept by no rule until they are read — the "
              "founding case of this audit lived in one of them."),
    ("BR-18", "The unit is in the STATUS ARCHIVE (`STATUS_ARCHIVE.md`) and carries none of the "
              "stated ruling words. BR-17's rule one file over, and ONLY because the file is now "
              "READ IN FULL — the phase-1e wave read lines 1-118 and 301-929, the phase-1f wave "
              "read the measured remainder (lines 119-300 and 930-3,861, 2026-08-02). Until then "
              "this surface deliberately carried NO rule and its residual share was marked UNREAD "
              "rather than judged. A superseded dated STATUS entry hands a session over and "
              "reports work done; `OPEN_ITEMS.md` OI-240/OI-266 establish that a tracking surface "
              "is not a home for a standing decision, and `STATUS.md:5-6` declares this file "
              "reference-only. The read is what licenses the rule, and the ruling-vocabulary "
              "exemption still holds every statement that carries a ruling word back for a reader."),
    ("BR-8", "Residual: none of the above applies. Recorded UNRESOLVED — the honest outcome, and "
             "the count is a finding about the record's legibility."),
]

# ── The RESERVATIONS (phase-1d enumeration wave, 2026-08-02) ──────────────────
# Why the residue is what it is, per surface, stated so that what remains is a JUDGED residue
# with a reason rather than an unread one.  These do NOT change any disposition — every cluster
# below stays `unresolved`.  They are emitted into the manifest beside the partition counts so a
# later pass reads the reason with the number.
UNRESOLVED_RESERVATIONS = {
    "tools/ script comments":
        "RESERVED for the sealed measurement-tools partition (the second partition of the "
        "OI-199 review, Cowork's ordering amendment). These scripts ARE the subject of that "
        "review, and register entry D-281 — found by this wave — shows the surface carries real "
        "decisions, so a bulk sweep here would both pre-empt the review and be the blind class "
        "sweep the ruling-vocabulary guardrail exists to forbid.",
    "src production comments":
        "RESERVED for a reading against `docs/scoring_model.md` §4/§8. These are largely the "
        "musical-reasoning comments register entry D-123 REQUIRES at every non-obvious scoring "
        "weight, so they state design decisions with their defense (D-195) and cannot be swept "
        "as narrative; settling each means comparing it with the scoring model's own §4 term "
        "table and §8 constraint list, which is a reading this wave did not reach.",
    "cc_* session reports": "The BR-12 EXEMPTION SET — units the sweep refused because they "
                            "carry a ruling word. Already judged once; each needs a reader.",
    "cc_instruction_* dispatches": "The BR-11 EXEMPTION SET — units the sweep refused because "
                                   "they carry a ruling word. Each needs a reader.",
    "src test comments": "The BR-13 EXEMPTION SET — units the sweep refused because they carry "
                         "a ruling word. Each needs a reader.",
    "cowork_* design documents": "A MEASURED PARTITION, still open. **27 of the 143 documents on "
                                 "this surface and the `docs/` one are read IN FULL** — 21 by the "
                                 "phase-1d wave (whose note does not split them between the two "
                                 "surfaces, so neither does this one), `cowork_stage5_fitter_"
                                 "design.md` (its single largest holder at 55 clusters) by "
                                 "phase-1f, and five by the phase-1g triage wave "
                                 "(`cowork_layer4_chordsymbol_design.md`, "
                                 "`cowork_layer5_function_design.md`, `docs/decoder_design.md`, "
                                 "`docs/scoring_model.md`, `docs/redesign_plan.md`). **116 are "
                                 "unread.** Correction of record carried by phase 1g: "
                                 "`docs/beam_widening_design.md` appears in BOTH the phase-1d and "
                                 "the phase-1f read lists, so the pre-1g distinct count was 22, "
                                 "not the 23 the record stated, and the pre-1g unread population "
                                 "was 121, not 120. NO BULK RULE is written over this surface even "
                                 "where a document HAS been read in full, and that is deliberate: "
                                 "BR-17/BR-18's reasoning is that a tracking surface is not a home "
                                 "for a standing decision, and a ratified design document is "
                                 "exactly the opposite — OI-268 records the standing decisions "
                                 "living on this surface. A read design document therefore yields "
                                 "entries, not a sweep. The per-file classification of the whole "
                                 "unread population is `tools/audit/decisions/phase1g_triage.md`.",
    "docs/ design documents": "Same treatment as the `cowork_*` surface, and the same reason for "
                              "having no bulk rule. `docs/beam_widening_design.md` was read in "
                              "full by phase-1d and again by phase-1f; `docs/decoder_design.md`, "
                              "`docs/scoring_model.md` and `docs/redesign_plan.md` by phase-1g. "
                              "The per-file classification of the unread remainder is "
                              "`tools/audit/decisions/phase1g_triage.md`.",
    "the two archives": "BOTH ARE NOW READ IN FULL — `cowork_handoff_archive.md` (5,704 lines) by "
                        "the phase-1e second-partition wave, `STATUS_ARCHIVE.md` (3,861 lines) "
                        "across phase-1e (lines 1-118 and 301-929) and phase-1f (the measured "
                        "remainder, lines 119-300 and 930-3,861), all 2026-08-02. That is what "
                        "licenses BR-17 and BR-18 over their non-ruling prose. What survives here "
                        "is the two rules' EXEMPTION SET: units that carry a ruling word, held "
                        "back by the guardrail for a reader rather than swept. The archives are "
                        "never swept before being read — the founding case of this audit (the "
                        "Stage-3.1b shelving, now register entry D-286) lived in one of them, and "
                        "so do the two standing 'do not retry' gate deferrals this wave entered "
                        "(D-300, D-301) and the third MuseScore-core edit (D-315, rowed OI-273).",
    "governing: ARCHITECTURE.md": "Already READ IN FULL by the 2026-08-01 completion pass; this "
                                  "residue is prose that reading judged not to state a distinct "
                                  "decision. Judged, not unread.",
    "governing: CLAUDE.md": "Already READ IN FULL by the 2026-08-01 completion pass; same "
                            "character as the ARCHITECTURE.md residue.",
    "the open-items register": "The BR-14 exemption set — open-items prose carrying a ruling "
                               "word, which is where a non-conformance row quotes the decision "
                               "it violates. Each needs a reader.",
    "the session handoff": "The BR-15 exemption set — handoff prose carrying a ruling word.",
    "mixed sources": "Clusters whose occurrences span more than one surface. No bulk rule ever "
                     "sweeps one, by construction.",
}

HEADING_KINDS = {"heading"}

# The ruling vocabulary that EXEMPTS a unit from the BR-11 / BR-12 / BR-13 sweeps.  A unit
# in a dispatch, a report or a test file that uses any of these words is NOT swept: it is
# left in BR-8 for a reader.  The list is stated here, and echoed into the manifest, so the
# boundary of each sweep is reviewable rather than implicit.
RULING_VOCABULARY = [
    r"\bratified\b", r"\bratification\b", r"\bshelved\b", r"\bfalsifie[sd]\b",
    r"\bdead end\b", r"\bdo not (re-?attempt|retry|re-?try|pursue|add|use|revert|remove)\b",
    r"\bDECIDED\b", r"\bDECISION\b", r"\bthe rule is\b", r"\bmust not\b",
    r"\bforbidden\b", r"\bnever (add|use|read|be|do|widen|assume)\b",
    r"\buser[- ](ruled|directed|ratified|decision|mandate)\b",
    r"\brejected\b", r"\bwithdrawn\b", r"\boverturned\b", r"\bsuperseded by\b",
    r"\bretired\b", r"\bdeferred (to|until|indefinitely)\b", r"\bstanding rule\b",
    r"\bpolicy\b", r"\bconvention\b",
]

SESSION_INSTRUCTION_PATTERNS = [
    r"\bread[- ]only\b.*\b(no|zero)\b.*\b(src/|code|behavior|behaviour|commit|build)\b",
    r"\bno\s+`?src/`?\s+change\b",
    r"\bpush(ed)?\s+(to\s+)?origin\b",
    r"\bat\s+(the\s+)?session\s+start\b",
    r"\bread\s+(this|these|the following)\b.*\bbefore\b",
    r"\brun\s+the\s+(tests|suites|build)\b",
    r"\bboth\s+test\s+suites\s+must\s+pass\b",
    r"\bcommit\s+only\s+when\s+explicitly\s+asked\b",
    r"\bexit:\$\?\b",
    r"\bgtest_filter\b",
    r"^\s*```",
    r"\bdo\s+NOT\s+(ask|stop|proceed)\b",
    r"\bdispatch\b.*\b(task\s+\d|scope|hard stop)\b",
    r"\bstanding self-check\b",
]

REPORT_NARRATIVE_PATTERNS = [
    r"\b(delivered|verified|measured|reproduced|regenerated|re-ran|re-run)\b",
    r"\b\d+/\d+\b",
    r"\bbyte-identical\b",
    r"\b[0-9a-f]{8,10}\b",
    r"\bPASS\b|\bFAIL\b",
    r"\b\d+(\.\d+)?\s?%",
    r"\bcommit\b",
    r"\btests?\s+(pass|green)\b",
]


def norm(text: str) -> str:
    """Normalize for quote matching: drop markdown blockquote markers and collapse whitespace."""
    lines = [re.sub(r"^\s*>+\s?", "", ln) for ln in text.splitlines()]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO,
                                       text=True).strip()
    except Exception:
        return "unknown"


# ── Establishment: every backbone quote must be findable at its cited home ────

def find_start_line(lines: list[str], needle: str, span: int) -> int | None:
    """First 1-based line at which `needle` (normalized) starts, or None."""
    # A window of span+4 lines starting anywhere at or before the true start still contains the
    # needle, so the FIRST match is up to 4 lines early. The LAST match is the true start.
    window = span + 4
    last = None
    for i in range(len(lines)):
        if not lines[i]:
            continue
        joined = re.sub(r"\s+", " ", " ".join(lines[i:i + window])).strip()
        if needle in joined:
            last = i + 1
    return last


def verify_backbone(backbone: dict) -> int:
    """Establishment (#19): every verbatim quote must exist at its cited home, AND the cited
    line number must be where it actually starts (DT-12 — a stale anchor is a defect type)."""
    misses, drifted, unanchored = [], [], []
    text_cache: dict[str, str] = {}
    line_cache: dict[str, list[str]] = {}
    for d in backbone["decisions"]:
        home = d["home"]
        parts = home.split(":")
        fname = parts[0]
        cited = None
        if len(parts) > 1:
            m = re.match(r"(\d+)", parts[1])
            if m:
                cited = int(m.group(1))
        path = REPO / fname
        if fname not in text_cache:
            if not path.exists():
                misses.append((d["id"], home, "home file does not exist"))
                text_cache[fname] = ""
                line_cache[fname] = []
                continue
            raw = path.read_text(encoding="utf-8", errors="replace")
            text_cache[fname] = norm(raw)
            line_cache[fname] = [re.sub(r"\s+", " ", re.sub(r"^\s*>+\s?", "", ln)).strip()
                                 for ln in raw.splitlines()]
        needle = norm(d["verbatim"])
        if not needle:
            misses.append((d["id"], home, "empty verbatim"))
            continue
        if needle not in text_cache[fname]:
            misses.append((d["id"], home, "verbatim NOT FOUND in the cited home"))
            continue
        if cited is None:
            unanchored.append((d["id"], home))
            continue
        found = find_start_line(line_cache[fname], needle, len(d["verbatim"].splitlines()))
        if found is None:
            misses.append((d["id"], home, "found in the file but not resolvable to a start line"))
        elif found != cited:
            drifted.append((d["id"], home, found))

    # Cross-reference guard.  The 2026-08-01 correction pass found 17 provenance references
    # pointing at the wrong OPEN_ITEMS row, because they were written before the rows existed
    # and never reconciled — including one to a number no row ever received.  A reference that
    # names nothing is mechanically catchable, so it is caught here rather than by reading.
    # ★ THE RETIRED BLOCK IS CONSULTED BESIDE THE LIVE ENTRIES (user, 2026-08-16, §4 limb 4 of
    # `cowork_rulings_2026_08_16_preparation_return.md`).  A soft-discarded entry is RETIRED from
    # the live record and NOT destroyed (#12): it stays in the same data file, whole, and stays
    # revivable.  A surviving entry that names one is therefore pointing at something the record
    # still holds, and reporting it DANGLING would say the opposite.  What this does not do is
    # widen anything else: nothing below reads the retired block, so no retired entry's verbatim
    # is located, no retired home is checked, and no count moves.
    known_d = {d["id"] for d in backbone["decisions"]}
    known_d |= {r["the_entry"]["id"]
                for r in backbone.get("retired_entries", {}).get("entries", [])}
    index_text = (REPO / "OPEN_ITEMS.md").read_text(encoding="utf-8", errors="replace")
    known_oi = set(re.findall(r"^\| (OI-\d+) \|", index_text, re.M))
    dangling = []
    for d in backbone["decisions"]:
        blob = " ".join(str(d.get(f, "")) for f in ("status_source", "rationale", "plain", "home"))
        for ref in sorted(set(re.findall(r"\bD-\d+\b", blob))):
            if ref not in known_d:
                dangling.append((d["id"], ref, "no such register entry"))
        for ref in sorted(set(re.findall(r"\bOI-\d+\b", blob))):
            if ref not in known_oi:
                dangling.append((d["id"], ref, "no such row in the OPEN_ITEMS.md index"))

    # Field-shape guard.  The register renders `ratified_by` as either "ratifier not stated"
    # (the list ["not stated"]) or "ratified by <names>".  An EMPTY list renders as a dangling
    # "ratified by " with nothing after it — a silent-empty render, caught here rather than by
    # a reader.  Same for an empty date.  Found by the OI-207 residual second pass, on its own
    # first write of new entries (the standing self-check, reading the diff).
    shape = []
    for d in backbone["decisions"]:
        if not d.get("ratified_by"):
            shape.append((d["id"], "ratified_by is empty — use [\"not stated\"]"))
        if not d.get("date"):
            shape.append((d["id"], "date is empty — use \"not stated\""))
    for did, why in shape:
        print(f"  FIELD SHAPE {did}: {why}")
    if shape:
        misses.append(("field shapes", "-", f"{len(shape)} empty required field(s)"))

    n = len(backbone["decisions"])
    print(f"backbone decisions: {n}")
    print(f"cross-references resolving: {'ALL' if not dangling else f'{len(dangling)} DANGLING'}")
    for did, ref, why in dangling:
        print(f"  DANGLING {did} -> {ref}: {why}")
    if dangling:
        misses.append(("cross-references", "-", f"{len(dangling)} dangling"))
    print(f"verbatim quotes found at their cited home: {n - len(misses)}/{n}")
    print(f"cited line numbers correct: {n - len(misses) - len(drifted) - len(unanchored)}"
          f"/{n - len(misses) - len(unanchored)}"
          f"   ({len(unanchored)} cited to a file with no line number, by design)")
    for mid, home, why in misses:
        print(f"  MISS {mid} ({home}): {why}")
    for mid, home, found in drifted:
        print(f"  LINE DRIFT {mid}: cited {home}, actually starts at line {found}")
    return 1 if (misses or drifted) else 0


# ── The disposition pass ─────────────────────────────────────────────────────

def build_matchers(backbone: dict):
    out = []
    for d in backbone["decisions"]:
        pats = [re.compile(p, re.IGNORECASE) for p in d.get("patterns", [])]
        out.append((d["id"], bool(d.get("home_is_layer_spec")), pats))
    return out


def strip_markdown(text: str) -> str:
    """Drop emphasis/code/quote/heading marks and collapse whitespace, for the BR-9 shape test."""
    return re.sub(r"\s+", " ", re.sub(r"[*_`>#]", "", text)).strip()


def is_list_leadin(text: str) -> bool:
    """BR-9: ends in a colon with no sentence-ending period before it."""
    t = strip_markdown(text)
    return t.endswith(":") and "." not in t.rstrip(":")


def files_of(members) -> set:
    return {o["file"] for m in members for o in m["source_occurrences"]}


def _all(files, pred) -> bool:
    """True when the cluster is wholly inside the named class (a mixed cluster is never swept)."""
    return bool(files) and all(pred(f) for f in files)


def in_open_items(f: str) -> bool:
    return f == "OPEN_ITEMS.md" or f.startswith("open_items/")


def in_dispatch(f: str) -> bool:
    return f.startswith("cc_instruction_")


def in_session_report(f: str) -> bool:
    return f.startswith("cc_") and not f.startswith("cc_instruction_")


def in_test_file(f: str) -> bool:
    return f.startswith("src/") and "/tests/" in f


def in_handoff(f: str) -> bool:
    return f == "cowork_handoff.md"


def in_read_handoff_archive(f: str) -> bool:
    """`cowork_handoff_archive.md` — the SESSION-HANDOFF ARCHIVE.

    This predicate exists only because the phase-1e second-partition wave READ THIS FILE
    IN FULL (all 5,704 lines, 2026-08-02).  The archives are otherwise swept by NO rule, on
    purpose: the founding case of the decision-conformance audit (the Stage-3.1b shelving)
    lived in one of them, and a blind class sweep is exactly how it went missing.  Reading
    the surface is what licenses the rule.
    """
    return f == "cowork_handoff_archive.md"


def in_read_status_archive(f: str) -> bool:
    """`STATUS_ARCHIVE.md` — the STATUS ARCHIVE.

    BR-17's predicate, one file over.  It exists only because the file is now READ IN FULL:
    the phase-1e wave read lines 1-118 and 301-929, the phase-1f wave read the measured
    remainder (lines 119-300 and 930-3,861, 2026-08-02).  Until the second half was read this
    surface deliberately carried no rule at all and its share of the residual was marked
    UNREAD rather than judged.  Same reasoning as BR-17: a superseded dated STATUS entry hands
    a session over and reports work done; `OPEN_ITEMS.md` OI-240 and OI-266 establish that a
    tracking surface is not a home for a standing decision, and `STATUS.md:5-6` declares this
    file reference-only.  The ruling-vocabulary exemption still applies, so every statement in
    it that carries a ruling word survives for a reader.
    """
    return f == "STATUS_ARCHIVE.md"


def in_defect_types(f: str) -> bool:
    return f == "DEFECT_TYPES.md"


def surface(f: str) -> str:
    """The source surface a file belongs to — the axis the unresolved residual is partitioned on."""
    if in_test_file(f):
        return "src test comments"
    if f.startswith("src/"):
        return "src production comments"
    if f.startswith("tools/"):
        return "tools/ script comments"
    if f.startswith("docs/"):
        return "docs/ design documents"
    if in_open_items(f):
        return "the open-items register"
    if f in ("STATUS_ARCHIVE.md", "cowork_handoff_archive.md"):
        return "the two archives"
    if f == "cowork_handoff.md":
        return "the session handoff"
    if f.startswith("cowork_"):
        return "cowork_* design documents"
    if in_dispatch(f):
        return "cc_instruction_* dispatches"
    if f.startswith("cc_"):
        return "cc_* session reports"
    return f"governing: {f}"


def disposition_pass(candidates, clusters, backbone):
    by_id = {c["id"]: c for c in candidates}
    matchers = build_matchers(backbone)
    sess = [re.compile(p, re.IGNORECASE | re.MULTILINE) for p in SESSION_INSTRUCTION_PATTERNS]
    rep = [re.compile(p, re.IGNORECASE) for p in REPORT_NARRATIVE_PATTERNS]
    ruling = [re.compile(p, re.IGNORECASE) for p in RULING_VOCABULARY]

    rows = []
    rule_counts = {rid: 0 for rid, _ in RULES}
    disp_counts = {d: 0 for d in DISPOSITIONS}

    for cl in clusters:
        members = [by_id[m] for m in cl["member_ids"] if m in by_id]
        texts = []
        seen = set()
        for m in members:
            t = m["decision_text"]
            if t not in seen:
                seen.add(t)
                texts.append(t)
        joined = "\n".join(texts)
        kinds = {m["unit_kind"] for m in members}
        cats = {m["category"] for m in members}
        tiers = {m["tier"] for m in members}

        cl_files = files_of(members)
        carries_ruling_word = any(p.search(joined) for p in ruling)

        named, named_spec, named_nospec = [], [], []
        for did, is_spec, pats in matchers:
            if any(p.search(joined) for p in pats):
                named.append(did)
                (named_spec if is_spec else named_nospec).append(did)

        if cl.get("boilerplate_class"):
            rule, disp, decs = "BR-1", "boilerplate", []
        elif kinds and kinds <= HEADING_KINDS:
            rule, disp, decs = "BR-2", "not-a-decision", []
        elif named_spec:
            rule, disp, decs = "BR-3", "restates", named
        elif named_nospec:
            rule, disp, decs = "BR-4", "no-spec-home", named_nospec
        elif any(p.search(joined) for p in sess):
            rule, disp, decs = "BR-5", "not-a-decision", []
        elif cats == {"cc_reports"} and any(p.search(joined) for p in rep):
            rule, disp, decs = "BR-6", "not-a-decision", []
        elif kinds == {"table_row"} and tiers == {"broad"}:
            rule, disp, decs = "BR-7", "not-a-decision", []
        elif texts and all(is_list_leadin(t) for t in texts):
            rule, disp, decs = "BR-9", "not-a-decision", []
        elif _all(cl_files, in_open_items) and (
                kinds <= {"table_row"} or all(
                    strip_markdown(t).startswith("Section ") for t in texts)):
            rule, disp, decs = "BR-10", "not-a-decision", []
        elif _all(cl_files, in_dispatch) and not carries_ruling_word:
            rule, disp, decs = "BR-11", "not-a-decision", []
        elif _all(cl_files, in_session_report) and not carries_ruling_word:
            rule, disp, decs = "BR-12", "not-a-decision", []
        elif _all(cl_files, in_test_file) and not carries_ruling_word:
            rule, disp, decs = "BR-13", "not-a-decision", []
        elif _all(cl_files, in_open_items) and not carries_ruling_word:
            rule, disp, decs = "BR-14", "not-a-decision", []
        elif _all(cl_files, in_handoff) and not carries_ruling_word:
            rule, disp, decs = "BR-15", "not-a-decision", []
        elif _all(cl_files, in_defect_types):
            rule, disp, decs = "BR-16", "not-a-decision", []
        elif _all(cl_files, in_read_handoff_archive) and not carries_ruling_word:
            rule, disp, decs = "BR-17", "not-a-decision", []
        elif _all(cl_files, in_read_status_archive) and not carries_ruling_word:
            rule, disp, decs = "BR-18", "not-a-decision", []
        else:
            rule, disp, decs = "BR-8", "unresolved", []

        rule_counts[rule] += 1
        disp_counts[disp] += 1
        rows.append({
            "cluster_id": cl["cluster_id"],
            "size": cl["size"],
            "disposition": disp,
            "rule": rule,
            "decisions": decs,
            "categories": sorted(cats),
            "unit_kinds": sorted(kinds),
            "surfaces": sorted({surface(f) for f in cl_files}),
            "files": cl["files"][:5] if cl.get("files") else sorted({
                o["file"] for m in members for o in m["source_occurrences"]})[:5],
        })

    return rows, rule_counts, disp_counts


# ── Producibility: can this layer still be DERIVED at all? ───────────────────
#
# The half `--check` cannot see, because `--check` re-reads what was emitted and the write path
# re-derives it.  Two stages, in the order a regeneration meets them:
#   1. every register pattern COMPILES — the failure that produced OI-333, where six patterns
#      carried unescaped markdown emphasis and the write mode died before writing anything;
#   2. the whole derivation RUNS to completion over the current harvest and clustering, covering
#      every cluster and every occurrence — in memory, writing nothing.
# Nothing is emitted, so this can be run at any tree without touching a committed artifact.

def producible(backbone: dict) -> int:
    bad = []
    total = 0
    for d in backbone["decisions"]:
        for p in d.get("patterns", []):
            total += 1
            try:
                re.compile(p, re.IGNORECASE)
            except re.error as exc:
                bad.append((d["id"], p, str(exc)))
    for did, pat, why in bad:
        print(f"  UNCOMPILABLE {did}: {pat!r} — {why}")
    print(f"register patterns compiling: {total - len(bad)}/{total}")
    if bad:
        print(f"FAIL: the disposition layer CANNOT BE PRODUCED — {len(bad)} register pattern(s) "
              "are not valid regular expressions")
        return 1

    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))["candidates"]
    clusters = json.loads(CLUSTERS.read_text(encoding="utf-8"))["clusters"]
    rows, _rules, _disp = disposition_pass(candidates, clusters, backbone)
    covered = sum(r["size"] for r in rows)
    ok = len(rows) == len(clusters) and covered == len(candidates)
    print(f"derivation dry-run: {len(rows)}/{len(clusters)} clusters, "
          f"{covered}/{len(candidates)} occurrences — nothing written")
    print("OVERALL " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="establishment pass: every backbone verbatim quote must be found "
                         "at its cited home")
    ap.add_argument("--check", action="store_true",
                    help="re-read the emitted artifacts and prove the coverage guarantee")
    ap.add_argument("--producible", action="store_true",
                    help="producibility pass: compile every register pattern and run the whole "
                         "derivation in memory, writing nothing")
    args = ap.parse_args()

    backbone = json.loads(BACKBONE.read_text(encoding="utf-8"))

    if args.verify:
        return verify_backbone(backbone)

    if args.producible:
        return producible(backbone)

    if args.check:
        data = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        clusters = json.loads(CLUSTERS.read_text(encoding="utf-8"))["clusters"]
        rows = data["dispositions"]
        ids_in = {c["cluster_id"] for c in clusters}
        ids_out = [r["cluster_id"] for r in rows]
        ok = True
        if len(ids_out) != len(set(ids_out)):
            print("FAIL: a cluster carries more than one disposition")
            ok = False
        if set(ids_out) != ids_in:
            print(f"FAIL: coverage — {len(ids_in - set(ids_out))} cluster(s) carry no disposition")
            ok = False
        bad = [r["cluster_id"] for r in rows if r["disposition"] not in DISPOSITIONS]
        if bad:
            print(f"FAIL: {len(bad)} disposition(s) outside the permitted vocabulary")
            ok = False
        print(f"clusters in:  {len(ids_in)}")
        print(f"dispositioned: {len(set(ids_out))}")
        print("OVERALL " + ("PASS" if ok else "FAIL"))
        return 0 if ok else 1

    cand = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    clus = json.loads(CLUSTERS.read_text(encoding="utf-8"))
    candidates = cand["candidates"]
    clusters = clus["clusters"]

    rows, rule_counts, disp_counts = disposition_pass(candidates, clusters, backbone)

    covered_occurrences = sum(r["size"] for r in rows)

    # The unresolved residual's partition by source surface — the measured handover to the next
    # pass over BR-8, COMPUTED here rather than counted by hand into a report (#17f).  Each cluster
    # is counted exactly ONCE, so the partition sums to the unresolved total; a cluster whose
    # occurrences span more than one surface is counted under "mixed sources".
    partition = {}
    for r in rows:
        if r["disposition"] != "unresolved":
            continue
        s = r["surfaces"]
        key = s[0] if len(s) == 1 else "mixed sources"
        partition[key] = partition.get(key, 0) + 1
    partition = dict(sorted(partition.items(), key=lambda kv: -kv[1]))

    header = {
        "instrument": "tools/audit/decisions/gen_cluster_dispositions.py",
        "purpose": "OI-207 adjudication Task 3 — one recorded disposition per harvested cluster, "
                   "by numbered bulk rule. NO cluster is left without one.",
        "inputs": {
            "candidates": {"file": str(CANDIDATES.relative_to(REPO)).replace("\\", "/"),
                           "sha256": sha256_of(CANDIDATES),
                           "total_candidates": len(candidates)},
            "clusters": {"file": str(CLUSTERS.relative_to(REPO)).replace("\\", "/"),
                         "sha256": sha256_of(CLUSTERS),
                         "cluster_count": len(clusters)},
            "backbone": {"file": str(BACKBONE.relative_to(REPO)).replace("\\", "/"),
                         "sha256": sha256_of(BACKBONE),
                         "decision_count": len(backbone["decisions"])},
        },
        "head_commit": head_commit(),
        "disposition_vocabulary": list(DISPOSITIONS),
        "ruling_vocabulary_exempting_BR11_BR12_BR13": list(RULING_VOCABULARY),
        "rules": [{"id": rid, "rule": text, "clusters": rule_counts[rid]} for rid, text in RULES],
        "disposition_counts": disp_counts,
        "unresolved_partition_by_surface": partition,
        # Every surviving surface's stated reason, so the residue is JUDGED, not merely counted.
        # A surface that appears in the partition without a reason here is a gap in this block,
        # and is emitted as such rather than silently omitted.
        "unresolved_reservation_by_surface": {
            k: UNRESOLVED_RESERVATIONS.get(k, "NO REASON STATED — this surface needs one.")
            for k in partition
        },
        "completeness_check": {
            "clusters": len(clusters),
            "dispositioned": len(rows),
            "occurrences_covered": covered_occurrences,
            "occurrences_total": len(candidates),
            "complete": len(rows) == len(clusters) and covered_occurrences == len(candidates),
        },
    }

    OUT_JSON.write_text(json.dumps({"header": header, "dispositions": rows},
                                   indent=1, ensure_ascii=False), encoding="utf-8")
    OUT_MANIFEST.write_text(json.dumps(header, indent=1, ensure_ascii=False), encoding="utf-8")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["cluster_id", "size", "disposition", "rule", "decisions",
                    "categories", "unit_kinds", "files"])
        for r in rows:
            w.writerow([r["cluster_id"], r["size"], r["disposition"], r["rule"],
                        ";".join(r["decisions"]), ";".join(r["categories"]),
                        ";".join(r["unit_kinds"]), ";".join(r["files"])])

    print(f"clusters dispositioned: {len(rows)}/{len(clusters)}")
    print(f"occurrences covered:    {covered_occurrences}/{len(candidates)}")
    for rid, text in RULES:
        print(f"  {rid}: {rule_counts[rid]:>6}   {text[:72]}")
    print("dispositions: " + ", ".join(f"{k}={v}" for k, v in disp_counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
