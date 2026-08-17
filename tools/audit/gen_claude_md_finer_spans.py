#!/usr/bin/env python3
"""`CLAUDE.md`, DECOMPOSED AT A FINER GRAIN — the measurement Ruling 4 commissioned.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 4 of
`cowork_rulings_2026_08_17_sixth_return.md` (the user's word: "A."): *"The finer measured pass
over `CLAUDE.md` is COMMISSIONED, read-only, riding the next dispatch: the span unit cuts inside
blocks at the record's own ★ amendment markers and recognizes the amendment-record shape
(ruled-date header, former-wording quote, declined-alternatives paragraph); it delivers a new
ratification surface with per-span fates; every doubt still defaults to STAYS AT SITE and every
doubt-defaulted span is marked; the F29/F33 evidence is input to the recognizers; nothing moves
until the user rules that surface."*

★ IT MEASURES.  IT MOVES NOTHING AND IT EDITS `CLAUDE.md` NOT AT ALL.  The fates it computes are
PROPOSALS on the surface the companion tool generates; the user rules that surface, and a LATER
dispatch executes what is ruled.

WHY A FINER PASS AT ALL — the measured ground, not a preference.  The coarse decomposition
predicted about 23% of `CLAUDE.md` would archive; the executed split moved 3.2%, because the
read-before-move safeguard established that the placement was largely wrong (finding F33).  Two
failures produced almost all of that gap, and each one is answered by one change here:

  * **F33's largest mis-class** — 15,395 characters classed `preserved-former-wording` on two
    sentences that merely POINT AT former wordings preserved elsewhere, the span containing none.
    ANSWERED BY: a former-wording marker no longer places a span on its own; a QUOTATION must
    accompany it.
  * **F33's second case** — an amendment record's span OVERRAN into principles 22, 23 and 24,
    which carry no blank line above them, so archiving it would have removed three standing
    principles from the list.  ANSWERED BY: a cut at every numbered-principle opener.

THE CUT RULES, and the ground of each.  The first four are the coarse pass's, IMPORTED rather than
restated (#6); the fifth is this pass's own.

  1. a BLOCK — a maximal run of consecutive non-blank lines;
  2. a FENCED CODE BLOCK is ONE span whatever blank lines it contains;
  3. a TABLE ROW is its own span;
  4. a block is cut again at every line opening with the record's own ★ marker;
  5. ★ NEW — a block is cut again at every NUMBERED PRINCIPLE OPENER, a line beginning `<n>. `.
     The numbering is the record's own, exactly as the ★ marker is, and F33's second case is the
     measured evidence that without it one marker inside a principle carries its NEIGHBOURS into
     an archive class.

THE CLASSES are the ruled ones, so the fates the user already ruled per class map onto this
measurement unchanged.  `operative-rule-text` is the DOUBT DEFAULT and is recorded per span.

THE AMENDMENT-RECORD SHAPE is published BESIDE the class, never as one.  The ruling names four
parts — a ruled-date header, a former-wording quote, a declined-alternatives paragraph, an
accepted-costs paragraph — and each is looked for independently with its own marker quoted, so a
reader sees WHICH parts a span carries rather than a verdict standing in for them.

★ WHAT THIS MEASUREMENT DOES NOT ESTABLISH, stated before its first use.  That a span classed
`operative-rule-text` IS operative — only that no recognizer placed it elsewhere.  The
recognizers are patterns over prose, their reach is UNMEASURED (#19), and the direction of their
error is the recoverable one: a missed marker keeps a span at site, which is the ruled default.
And the finer cut does not make every span self-contained: a cut inside a block yields a span
whose sentence may continue in the next one, which is why the fates are PROPOSALS a reader rules
rather than an act.

THE STOPS:
  * the subject file missing at the pinned commit STOPS it;
  * the per-class byte counts not summing to the file's own measured size STOPS it — no span may
    be silently dropped, which is the one failure that would make every number here meaningless.

Run:
  python tools/audit/gen_claude_md_finer_spans.py
  python tools/audit/gen_claude_md_finer_spans.py --check
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_governing_surface_spans as coarse                       # noqa: E402  (path set above)

OUT = HERE / "claude_md_finer_spans.json"

SUBJECT = "CLAUDE.md"

# PINNED, for the reason the coarse pass states of itself: this artifact is EVIDENCE FOR A RULING,
# so it may not move under the ruling it supports. The pin is Task 2 of the executing dispatch —
# the commit this task is performed on top of, at which `CLAUDE.md` is byte-identical to the file
# this pass was asked about, and which is content-addressed so the reading re-derives forever.
PINNED_COMMIT = "e94f765c25b49d2c9ffa47b1a296302debc25ce6"
PINNED_COMMIT_IS = ("Task 2 of `cc_instruction_preparation_seventh.md` — the commit this "
                    "read-only measurement is performed on top of. `CLAUDE.md` is untouched by "
                    "this batch, so the pin and the working tree carry the same file.")

# ── AUTHORED — the new cut rule, and the two recognizer parameters, published here ────────────
# A numbered principle opener. The record numbers its standing principles 1..24 in a run with no
# blank line between several of them; F33's second case is the measured evidence for the cut.
PRINCIPLE_OPENER = re.compile(r"^\d{1,2}\.\s")

# A QUOTATION: a run of at least this many characters between quotation marks. Below the floor a
# short quoted phrase inside a rule — a delegation's admitted form, say — would read as a
# preserved wording, which is exactly the confusion F33's largest mis-class is made of.
QUOTATION = re.compile(r"[\"“][^\"”]{%d,}[\"”]" % 40)
QUOTATION_WINDOW = 300      # characters either side of the marker the quotation must fall within

# A ruled-date header: an attribution AND a date, both inside the span's opening. Looked for in
# the opening because that is where the record puts them — an amendment record announces its
# authority first.
ATTRIBUTION = re.compile(
    r"(user-ruled|user-ratified|user-directed|the user's ruling|user's own ruling|"
    r"\buser,\s|ratified by the user|recorded|ruled|corrected|homed here|written into)")
RULED_DATE = re.compile(r"\b20\d\d-\d\d-\d\d\b")
HEADER_WINDOW = 400

DECLINED = tuple(p for p in coarse.DEFENSE_MARKERS if "COST" not in p.upper())
ACCEPTED_COSTS = (r"THE COSTS THE USER ACCEPTED", r"an accepted cost is not a discharged one")

# ── AUTHORED — the two STRUCTURAL spans that may never be classed by their words ──────────────
# ★ FOUND BY THIS PASS'S OWN SELF-CHECK, reading the surface it had just generated. Both were
# proposed for archiving on the first run, and both would have been wrong in the way the ruled
# doubt default exists to prevent.
#
#   1. AN ARCHIVE POINTER. The executed split leaves a compact dated pointer at every site it
#      archives, and that pointer QUOTES its target's class name and the opening of what moved.
#      So a recognizer reading the pointer's words places it in the class of the thing it points
#      at — and archiving a pointer removes the one breadcrumb a reader has back to the moved
#      span, which is the opposite of what the pointer discipline is for.
#
#      ★ THE STANDING CONSTRAINT, ruled 2026-08-17 — Ruling 1 of
#      `cowork_rulings_2026_08_17_eighth_return.md`, quoted verbatim:
#
#          "a span whose archive classification derives from text inside an archive pointer is
#           NOT archivable, wherever in the span the pointer sits."
#
#      and, of the guard as it stood when that ruling was given: "The finer pass's own structural
#      guard fires only when a span BEGINS with a pointer; that guard is hereby insufficient as
#      written."
#
#      WHY THE GUARD WAS INSUFFICIENT, measured rather than argued (finding F44): the ONE span
#      this pass proposed for archiving on ground no reading had refused was classed
#      `defense-and-declined-alternatives` entirely by two archive pointers occupying its LAST TWO
#      LINES — the only occurrence of `DECLINED` and the only occurrence of `THE COSTS THE USER
#      ACCEPTED` both sat inside those pointers, and the span carried no alternative and no cost
#      of its own. `re.match` is anchored at the start of the span, so the guard could not see it.
#
#      WHAT THE WIDENED GUARD DOES: every archive-pointer LINE in a span is located, wherever it
#      sits, and a recognizer marker (or, for a preserved former wording, its accompanying
#      quotation) lying inside one of those lines MAY NOT PLACE THE SPAN. A marker of the same
#      class found OUTSIDE every pointer still places it — the constraint is about where the
#      classifying text sits, not about a span merely containing a pointer. A span left with no
#      admissible marker falls to the ruled DOUBT DEFAULT and stays at site, with the declined
#      placement published beside it, so nothing is dropped and the widening errs only in the
#      recoverable direction.
#   2. A BARE HEADING. A markdown heading line is a span of its own, and its section body is a
#      different span. A heading classed by its own words — "RETROSPECTIVE ... superseded ...
#      historical reference" — would move while everything under it stayed, leaving a headless
#      section and a heading filed under a document it does not belong to.
#
# Both are STRUCTURE rather than content, so both are placed POSITIVELY at site rather than left
# to the doubt default: the evidence is published, so a reader sees a decision rather than an
# absence of one.
ARCHIVE_POINTER = re.compile(r"^\s*\*★ ARCHIVED \d{4}-\d{2}-\d{2}")
BARE_HEADING = re.compile(r"^#{1,6}\s")

# The ruled constraint, quoted verbatim wherever this pass refuses a placement under it, so a
# reader of the artifact meets the rule and not only its effect.
POINTER_CONSTRAINT = (
    "a span whose archive classification derives from text inside an archive pointer is NOT "
    "archivable, wherever in the span the pointer sits — Ruling 1 of "
    "`cowork_rulings_2026_08_17_eighth_return.md`, 2026-08-17")


class Stop(Exception):
    """A demand of the decomposition is unmet. Never a warning, never a span dropped."""


def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def cut_here(line: str) -> bool:
    return bool(coarse.STAR_MARKER.match(line) or PRINCIPLE_OPENER.match(line))


def spans_of(text: str) -> tuple[list[dict], int]:
    """The file, cut into spans by the five rules the module docstring states.

    This is a DIFFERENT UNIT from the coarse pass's, not a second implementation of it: the two
    measurements answer different questions and neither can be derived from the other, so each
    owns its own cut (#6 is about one path per concern, and the concerns differ). Everything the
    two units DO share — the fence, the table row and the ★ marker — is imported.
    """
    lines = text.splitlines(keepends=True)
    out: list[dict] = []
    skipped = 0
    i, n = 0, len(lines)
    while i < n:
        if not lines[i].strip():
            skipped += len(lines[i])
            i += 1
            continue
        start = i
        if coarse.FENCE.match(lines[i]):
            i += 1
            while i < n and not coarse.FENCE.match(lines[i]):
                i += 1
            if i < n:
                i += 1
            out.append({"first_line": start + 1, "last_line": i,
                        "text": "".join(lines[start:i]), "kind": "fenced-block"})
            continue
        if coarse.TABLE_ROW.match(lines[i]):
            out.append({"first_line": i + 1, "last_line": i + 1,
                        "text": lines[i], "kind": "table-row"})
            i += 1
            continue
        i += 1
        while i < n and lines[i].strip() and not coarse.FENCE.match(lines[i]) \
                and not coarse.TABLE_ROW.match(lines[i]) and not cut_here(lines[i]):
            i += 1
        if coarse.STAR_MARKER.match(lines[start]):
            kind = "star-marked sub-block"
        elif PRINCIPLE_OPENER.match(lines[start]):
            kind = "numbered-principle sub-block"
        else:
            kind = "block"
        out.append({"first_line": start + 1, "last_line": i,
                    "text": "".join(lines[start:i]), "kind": kind})
    return out, skipped


def first_match(text: str, patterns):
    for pattern in patterns:
        found = re.search(pattern, text)
        if found:
            return found
    return None


def archive_pointer_regions(text: str) -> list[tuple[int, int]]:
    """Every archive-pointer LINE in the span, as character ranges into the span's own text.

    The unit is the LINE because that is what the executed split writes: one compact dated pointer
    per archived span, on a line of its own. Locating them by line rather than by the whole span's
    opening is exactly what the standing constraint of 2026-08-17 requires — a pointer anywhere in
    the span disqualifies the text inside it from classifying the span.
    """
    regions, at = [], 0
    for line in text.splitlines(keepends=True):
        if ARCHIVE_POINTER.match(line):
            regions.append((at, at + len(line)))
        at += len(line)
    return regions


def inside_a_pointer(at: int, regions: list[tuple[int, int]]) -> bool:
    return any(lo <= at < hi for lo, hi in regions)


def matches_split_by_pointer(text: str, patterns, regions: list[tuple[int, int]]):
    """The first match OUTSIDE every archive pointer, and the first one inside — both published.

    Returning both is what makes the constraint auditable rather than silent: a span declined
    because its only classifying text sits inside a pointer publishes the marker that was refused,
    so a reader sees a decision instead of an absence of one.
    """
    outside = inside = None
    for pattern in patterns:
        for found in re.finditer(pattern, text):
            if inside_a_pointer(found.start(), regions):
                inside = inside or found
            else:
                outside = outside or found
        if outside:
            return outside, inside
    return outside, inside


def former_wording_hits(text: str) -> list[re.Match]:
    """EVERY former-wording marker in the span, in order — not merely the first.

    Taking the first alone is the failure this avoids: a span often ANNOUNCES the preservation in
    its heading and then carries the wording several sentences later, so the first match sits too
    far from the quotation and the span would fall to the doubt default with the evidence sitting
    inside it.
    """
    found = [m for pattern in coarse.FORMER_WORDING_MARKERS for m in re.finditer(pattern, text)]
    return sorted(found, key=lambda m: m.start())


def quotation_near(text: str, at: re.Match) -> re.Match | None:
    """A quotation that BEGINS within the window of the marker — however long it runs.

    Returns the MATCH rather than its text, because the standing constraint of 2026-08-17 needs
    the quotation's OFFSET: a quotation lying inside an archive pointer may not place a span.

    The window bounds where a quotation may START, never where it may END. A preserved wording is
    often several sentences long and runs past any window one could pick, so requiring it to
    close inside the window would reject exactly the longest preservations — the ones a governing
    document actually carries. Measured, not anticipated: principle #21's preserved wording opens
    within the window and closes some four hundred characters past it.
    """
    lo = max(0, at.start() - QUOTATION_WINDOW)
    hi = at.end() + QUOTATION_WINDOW
    for found in QUOTATION.finditer(text, lo):
        if found.start() >= hi:
            break
        return found
    return None


def shape_of(text: str) -> dict:
    """The four parts of an amendment record the ruling names, each looked for on its own.

    ★ EVERY PART IS LOOKED FOR OUTSIDE THE SPAN'S ARCHIVE POINTERS FIRST, under the standing
    constraint of 2026-08-17 stated at the top of this file. Where a part exists ONLY inside a
    pointer, the part is recorded as POINTER-CARRIED and does not place the span; the refused
    marker is published beside it so the decline is readable rather than silent.
    """
    head = text[:HEADER_WINDOW]
    regions = archive_pointer_regions(text)
    attribution = ATTRIBUTION.search(head)
    date = RULED_DATE.search(head)
    parts: dict[str, object] = {}
    if regions:
        parts["archive_pointer_lines_inside_this_span"] = len(regions)
    if attribution and date:
        parts["ruled_date_header"] = {"the_attribution_matched": attribution.group(0),
                                      "the_date_matched": date.group(0)}
    hits = former_wording_hits(text)
    if hits:
        # A marker places the span only when BOTH it and its accompanying quotation lie outside
        # every archive pointer. Preferring a clean placement over the first one found is what
        # keeps the widening from refusing a span that genuinely carries a preserved wording of
        # its own beside a pointer.
        placings = [(m, quotation_near(text, m)) for m in hits]
        clean = next(((m, q) for m, q in placings
                      if q is not None
                      and not inside_a_pointer(m.start(), regions)
                      and not inside_a_pointer(q.start(), regions)), None)
        carried = next(((m, q) for m, q in placings
                        if q is not None
                        and (inside_a_pointer(m.start(), regions)
                             or inside_a_pointer(q.start(), regions))), None)
        marker, quoted = clean or (hits[0], None)
        part = {
            "the_marker_matched": marker.group(0),
            "markers_found_in_the_span": len(hits),
            "a_quotation_accompanies_it": clean is not None,
            "the_quotation": quoted.group(0)[:120] if quoted is not None else None,
        }
        if clean is None and carried is not None:
            part["★_a_placing_marker_was_REFUSED_as_pointer_carried"] = {
                "the_refused_marker": carried[0].group(0),
                "the_refused_quotation": carried[1].group(0)[:120],
                "the_constraint": POINTER_CONSTRAINT,
            }
        parts["former_wording_marker"] = part
    declined, declined_carried = matches_split_by_pointer(text, DECLINED, regions)
    if declined:
        parts["declined_alternatives_paragraph"] = {"the_marker_matched": declined.group(0)}
    elif declined_carried:
        parts["declined_alternatives_paragraph_REFUSED_as_pointer_carried"] = {
            "the_refused_marker": declined_carried.group(0),
            "the_constraint": POINTER_CONSTRAINT,
        }
    costs, costs_carried = matches_split_by_pointer(text, ACCEPTED_COSTS, regions)
    if costs:
        parts["accepted_costs_paragraph"] = {"the_marker_matched": costs.group(0)}
    elif costs_carried:
        parts["accepted_costs_paragraph_REFUSED_as_pointer_carried"] = {
            "the_refused_marker": costs_carried.group(0),
            "the_constraint": POINTER_CONSTRAINT,
        }
    return parts


def classify(text: str, shape: dict) -> tuple[str, dict, bool]:
    # STRUCTURE FIRST. Neither of these may be classed by the words it contains, and neither is
    # left to the doubt default — a positive placement publishes the reason.
    if ARCHIVE_POINTER.match(text):
        return coarse.OPERATIVE, {
            "it_is_an_archive_pointer_left_by_a_previous_act": True,
            "why_it_stays": "the pointer QUOTES the class and the opening of the span it points "
                            "at, so a recognizer reading its words places it in that span's "
                            "class. Archiving it would remove the one breadcrumb a reader has "
                            "back to the moved span, which is the opposite of what the pointer "
                            "discipline is for.",
        }, False
    if BARE_HEADING.match(text) and len(text.strip().splitlines()) == 1:
        return coarse.OPERATIVE, {
            "it_is_a_bare_section_heading": True,
            "why_it_stays": "a heading is a span of its own and its section body is a different "
                            "span, so classing the heading by its own words would move it while "
                            "everything under it stayed — a headless section here and a heading "
                            "filed alone in the companion.",
        }, False

    former = shape.get("former_wording_marker")
    if former and former["a_quotation_accompanies_it"]:
        return coarse.FORMER_WORDING, {
            "the_marker_matched": former["the_marker_matched"],
            "the_quotation_that_places_it": former["the_quotation"],
        }, False
    # ★ The historical recognizer runs under the standing constraint too: a marker found ONLY
    # inside an archive pointer may not place the span, and the refused marker is published.
    regions = archive_pointer_regions(text)
    hit, hit_carried = matches_split_by_pointer(text, coarse.HISTORICAL_MARKERS, regions)
    if hit:
        return coarse.HISTORICAL, {"the_marker_matched": hit.group(0)}, False
    if "declined_alternatives_paragraph" in shape:
        return coarse.DEFENSE, {
            "the_marker_matched": shape["declined_alternatives_paragraph"]["the_marker_matched"],
            "which_part": "a declined-alternatives record"}, False
    if "accepted_costs_paragraph" in shape:
        return coarse.DEFENSE, {
            "the_marker_matched": shape["accepted_costs_paragraph"]["the_marker_matched"],
            "which_part": "an accepted-costs record"}, False
    evidence: dict = {"no_recognizer_placed_it": True}
    if former:
        evidence["a_former_wording_marker_was_found_and_did_NOT_place_it"] = {
            "the_marker_matched": former["the_marker_matched"],
            "why_it_did_not_place_it":
                "no quotation accompanies it, so the span POINTS AT a former wording preserved "
                "elsewhere rather than carrying one. This is finding F33's largest mis-class "
                "answered: the coarse pass placed 15,395 characters of live governing rule text "
                "on exactly this signal.",
        }
    # ★ EVERY PLACEMENT THE STANDING CONSTRAINT REFUSED IS PUBLISHED HERE, so a span that would
    # have been proposed for archiving before 2026-08-17 shows WHY it is now doubt-defaulted
    # rather than simply disappearing from the archive classes.
    refused = {}
    for key, part in (("a_preserved_former_wording", former),
                      ("a_declined_alternatives_record",
                       shape.get("declined_alternatives_paragraph_REFUSED_as_pointer_carried")),
                      ("an_accepted_costs_record",
                       shape.get("accepted_costs_paragraph_REFUSED_as_pointer_carried"))):
        if key == "a_preserved_former_wording":
            carried = (part or {}).get("★_a_placing_marker_was_REFUSED_as_pointer_carried")
            if carried:
                refused[key] = carried
        elif part:
            refused[key] = part
    if hit_carried:
        refused["a_self_declared_historical_block"] = {
            "the_refused_marker": hit_carried.group(0),
            "the_constraint": POINTER_CONSTRAINT,
        }
    if refused:
        evidence["★_an_archive_placement_was_REFUSED_by_the_standing_pointer_constraint"] = {
            "the_constraint": POINTER_CONSTRAINT,
            "archive_pointer_lines_inside_this_span": len(regions),
            "the_refused_placements": refused,
            "what_follows": "the span falls to the ruled DOUBT DEFAULT and STAYS AT SITE. It is "
                            "not dropped: the refused marker stands above, so the user can "
                            "overrule this in one edit rather than rediscover the question.",
        }
    return coarse.OPERATIVE, evidence, True


# ── AUTHORED — the proposed fate per class, under §5(E)'s ruled test ──────────────────────────
# The classes and their fates are the ones the user already ruled on 2026-08-17 (Ruling 1 of the
# governing-surface split record). They are restated here as PROPOSALS over a NEW measurement,
# which is what the surface asks the user to rule; nothing about the class fates is re-decided.
PROPOSED_FATES = {
    coarse.OPERATIVE: ("STAYS AT SITE",
                       "It is the rule itself, or a span no recognizer placed elsewhere. The "
                       "ruled doubt default is that a span the test cannot place stays at site."),
    coarse.FORMER_WORDING: ("ARCHIVES, with a dated pointer at the site",
                            "It CARRIES a preserved former wording — a marker with a quotation "
                            "attached — which §5(E) names as archive material by name."),
    coarse.HISTORICAL: ("ARCHIVES, with a dated pointer at the site",
                        "The span says of ITSELF that it is historical or superseded."),
    coarse.DEFENSE: ("ARCHIVES, with a dated pointer at the site",
                     "It carries an explicit declined-alternative or accepted-cost record, which "
                     "§5(E) names by name. NOTE THE NARROWNESS: a rule's PURPOSE stays at site."),
    coarse.RESOLVED_ROW: ("ARCHIVES, with a dated pointer at the site",
                          "Not reachable in this file, which carries no register rows."),
    coarse.POINTER: ("NOT DECIDED BY THIS TEST",
                     "Not reachable in this file, which carries no dated batch entries."),
}


def build() -> dict:
    try:
        text = git("show", f"{PINNED_COMMIT}:{SUBJECT}")
    except Stop:
        raise Stop(f"{SUBJECT} is not in the tree at the pinned commit {PINNED_COMMIT[:10]}")
    total = len(text)

    rows, by_class, doubt = [], {}, 0
    covered = 0
    all_spans, blank = spans_of(text)
    for span in all_spans:
        shape = shape_of(span["text"])
        category, evidence, defaulted = classify(span["text"], shape)
        size = len(span["text"])
        covered += size
        cell = by_class.setdefault(category, {"spans": 0, "characters": 0})
        cell["spans"] += 1
        cell["characters"] += size
        if defaulted:
            doubt += size
        fate, why = PROPOSED_FATES[category]
        rows.append({
            "first_line": span["first_line"], "last_line": span["last_line"],
            "kind": span["kind"], "characters": size,
            "the_class": category,
            "the_evidence": evidence,
            "the_amendment_record_shape_it_carries": shape,
            "placed_by_the_doubt_default": defaulted,
            "the_proposed_fate": fate if not defaulted else "STAYS AT SITE",
            "why_that_fate": why,
            "the_opening": " ".join(span["text"].split())[:160],
        })

    if covered + blank != total:
        raise Stop(f"{SUBJECT}: the spans and the blank lines account for {covered + blank} "
                   f"characters against a file of {total} — a span has been dropped from the "
                   f"decomposition, which would make every count here meaningless")

    coarse_data = json.loads((HERE / "governing_surface_spans.json").read_text(encoding="utf-8"))
    coarse_file = next(f for f in coarse_data["per_file"] if f["file"] == SUBJECT)

    # ★ THE CROSS-CHECK AGAINST THE A4 SAFEGUARD'S OWN READING. Seventeen spans of the five
    # governing files were READ by the executing dispatch and LEFT AT SITE because they do not
    # read as their class says (finding F33). Where THIS pass proposes archiving one of them, the
    # user is being asked to overturn a reading already performed at the file — so the conflict is
    # named, with the safeguard's own reason quoted, rather than left to be noticed.
    applied = json.loads(
        (HERE / "governing_surface_split_application.json").read_text(encoding="utf-8"))
    left = next(f for f in applied["per_file"] if f["file"] == SUBJECT)["the_left_at_site"]
    conflicts = []
    for row in rows:
        if row["the_class"] == coarse.OPERATIVE:
            continue
        for kept in left:
            head = kept["the_opening"][:100]
            if head and row["the_opening"].startswith(head):
                row["★_the_A4_safeguard_read_this_span_and_LEFT_IT_AT_SITE"] = {
                    "at_the_coarse_pin": [kept["first_line_at_the_pin"],
                                          kept["last_line_at_the_pin"]],
                    "the_safeguards_own_reason": kept["why"],
                    "what_the_user_is_being_asked": "to overturn a reading already performed at "
                                                    "the file, or to agree that this pass's finer "
                                                    "cut answers the reason given",
                }
                conflicts.append({
                    "the_finer_span": [row["first_line"], row["last_line"]],
                    "the_class_this_pass_gives_it": row["the_class"],
                    "the_opening": row["the_opening"],
                    "the_safeguards_own_reason": kept["why"],
                })
                break

    return {
        "what_this_is":
            "`CLAUDE.md`, DECOMPOSED AT A FINER GRAIN AND CLASSED, with a proposed fate per span "
            "under the ruled archivability test. A MEASUREMENT ONLY: `CLAUDE.md` is not edited, "
            "no span is moved, and no fate is decided — the user rules the surface generated from "
            "this artifact, and a LATER dispatch executes what is ruled. Every figure here is "
            "computed; none is transcribed (D-431).",
        "generator": "tools/audit/gen_claude_md_finer_spans.py",
        "dispatch": "cc_instruction_preparation_seventh.md, Task 3",
        "the_ruling_that_commissioned_it": {
            "source": "cowork_rulings_2026_08_17_sixth_return.md §4 (the user's word: \"A.\")",
            "quoted": "The finer measured pass over `CLAUDE.md` is COMMISSIONED, read-only, "
                      "riding the next dispatch: the span unit cuts inside blocks at the record's "
                      "own ★ amendment markers and recognizes the amendment-record shape "
                      "(ruled-date header, former-wording quote, declined-alternatives "
                      "paragraph); it delivers a new ratification surface with per-span fates; "
                      "every doubt still defaults to STAYS AT SITE and every doubt-defaulted span "
                      "is marked; the F29/F33 evidence is input to the recognizers; nothing moves "
                      "until the user rules that surface.",
        },
        "measured_at_commit": PINNED_COMMIT,
        "★_why_the_reading_is_pinned": {
            "what_that_commit_is": PINNED_COMMIT_IS,
            "the_reason": "This artifact is EVIDENCE FOR A RULING, so it may not move under the "
                          "ruling it supports — the same reason the coarse pass pins its own "
                          "reading, measured there rather than anticipated.",
        },
        "the_cut_rules": {
            "imported_from_the_coarse_pass": {
                "a_block": coarse.__doc__ and "a maximal run of consecutive non-blank lines",
                "a_fenced_code_block": "ONE span whatever blank lines it contains",
                "a_table_row": "its own span",
                "a_star_marked_sub_block": "a block is cut again at every line opening with the "
                                           "record's own ★ marker",
            },
            "★_this_pass_own_cut": {
                "a_numbered_principle_opener": PRINCIPLE_OPENER.pattern,
                "the_ground": "finding F33's second case, measured: an amendment record's span "
                              "OVERRAN into principles 22, 23 and 24, which carry no blank line "
                              "above them, so the coarse pass placed three standing principles in "
                              "an archive class.",
            },
        },
        "★_the_two_structural_spans_that_are_never_classed_by_their_words": {
            "found_by": "this pass's own self-check, reading the surface it had just generated. "
                        "Both were proposed for archiving on the first run.",
            "an_archive_pointer": {
                "the_pattern": ARCHIVE_POINTER.pattern,
                "the_ground": "the executed split leaves a compact dated pointer at every site it "
                              "archives, and that pointer QUOTES its target's class and opening, "
                              "so a recognizer reading its words places it in the class of the "
                              "thing it points at. Archiving a pointer removes the one breadcrumb "
                              "back to the moved span.",
                "★_the_standing_constraint_ruled_2026_08_17": {
                    "the_constraint_verbatim": POINTER_CONSTRAINT,
                    "the_ruling": "Ruling 1 of `cowork_rulings_2026_08_17_eighth_return.md`, which "
                                  "also states of the guard as it then stood: \"The finer pass's "
                                  "own structural guard fires only when a span BEGINS with a "
                                  "pointer; that guard is hereby insufficient as written.\"",
                    "what_was_insufficient": "the guard is anchored at the START of a span, so a "
                                             "pointer sitting anywhere else in the span was "
                                             "invisible to it. Measured at finding F44: the ONE "
                                             "span this pass proposed for archiving on ground no "
                                             "reading had refused was classed entirely by two "
                                             "pointers occupying its LAST TWO LINES.",
                    "what_the_widened_guard_does": "every archive-pointer LINE in a span is "
                                                   "located wherever it sits, and a recognizer "
                                                   "marker — or, for a preserved former wording, "
                                                   "its accompanying quotation — lying inside one "
                                                   "of those lines MAY NOT PLACE THE SPAN. A "
                                                   "marker of the same class found OUTSIDE every "
                                                   "pointer still places it.",
                    "what_it_costs": "a span left with no admissible marker falls to the ruled "
                                     "DOUBT DEFAULT and stays at site, with the refused placement "
                                     "published beside it. The widening errs only in the "
                                     "recoverable direction and drops nothing.",
                    "★_it_moves_no_fate": "this is a RECOGNIZER change. "
                                          "`gen_claude_md_finer_archive.py --apply` is not run by "
                                          "it, and `CLAUDE.md` is not touched by it.",
                },
            },
            "a_bare_heading": {
                "the_pattern": BARE_HEADING.pattern,
                "the_ground": "a heading is a span of its own and its section body is another, so "
                              "classing the heading by its own words would move it while "
                              "everything under it stayed — a headless section, and a heading "
                              "filed alone in the companion.",
            },
            "★_why_they_are_placed_POSITIVELY_rather_than_left_to_the_doubt_default":
                "the doubt default records an absence of evidence; these two are decisions with "
                "a reason, and publishing the reason is what lets the user overrule either in one "
                "edit rather than rediscover it.",
        },
        "the_recognizer_change_and_its_ground": {
            "what_changed": "a former-wording marker no longer places a span on its own: a "
                            "QUOTATION must accompany it, within a published window.",
            "the_quotation_pattern": QUOTATION.pattern,
            "the_window_in_characters": QUOTATION_WINDOW,
            "the_ground": "finding F33's largest mis-class, measured: 15,395 characters of live "
                          "governing rule text — the decisions register's rules (a) through (n) — "
                          "were classed `preserved-former-wording` on two sentences that POINT AT "
                          "former wordings preserved in the register's own provenance, the span "
                          "containing none.",
            "★_what_the_floor_costs": "a genuinely preserved wording shorter than the floor, or "
                                      "beginning further from every one of its markers than the "
                                      "window, is NOT placed and falls to the doubt default — it "
                                      "stays at site, which is the recoverable direction. A "
                                      "preservation marked by italics alone, with no quotation "
                                      "marks, is likewise not placed.",
        },
        "the_amendment_record_shape": {
            "what_it_is": "the four parts the ruling names, each looked for independently and "
                          "published per span with its own marker quoted",
            "ruled_date_header": {"attribution": ATTRIBUTION.pattern, "date": RULED_DATE.pattern,
                                  "looked_for_in_the_first_characters": HEADER_WINDOW},
            "former_wording_quote": "a former-wording marker WITH a quotation attached",
            "declined_alternatives_paragraph": list(DECLINED),
            "accepted_costs_paragraph": list(ACCEPTED_COSTS),
            "★_why_it_is_published_beside_the_class_and_never_as_one":
                "a shape is evidence about what a span IS; a class carries a fate. Publishing the "
                "parts separately lets a reader see a span that is an amendment record WITHOUT a "
                "preserved wording — which is the exact case the coarse pass got wrong.",
        },
        "★_what_this_measurement_does_NOT_establish":
            "That a span classed `operative-rule-text` IS operative — only that no recognizer "
            "placed it elsewhere. The recognizers are patterns over prose and their reach is "
            "UNMEASURED (#19). And the finer cut does not make every span self-contained: a cut "
            "inside a block yields a span whose sentence may continue in the next one, which is "
            "why every fate here is a PROPOSAL the user rules.",
        "the_totals": {
            "characters": total,
            "lines": len(text.splitlines()),
            "spans": len(rows),
            "characters_in_the_blank_lines_between_spans": blank,
            "by_class": {c: by_class.get(c, {"spans": 0, "characters": 0})
                         for c in coarse.CLASSES},
            "characters_placed_by_the_doubt_default": doubt,
        },
        "★_where_this_pass_proposes_archiving_a_span_the_A4_SAFEGUARD_READ_AND_KEPT": {
            "what_this_is": "The executed split's own read-before-move safeguard left 17 spans at "
                            "site because they do not read as their class says (finding F33). "
                            "Where this pass proposes archiving one of them, the user is being "
                            "asked to overturn a reading already performed AT THE FILE — so the "
                            "conflict is named here, with the safeguard's own reason quoted, "
                            "rather than left to be noticed.",
            "★_how_to_read_a_conflict": "the safeguard's reason either IS or IS NOT answered by "
                                        "this pass's finer cut, and that is the question. Where "
                                        "the reason was that a span OVERRAN into live rule text, "
                                        "the finer cut answers it. Where the reason was that the "
                                        "span ITSELF states a rule, no cut answers it and the "
                                        "proposal should be refused.",
            "count": len(conflicts),
            "the_conflicts": conflicts,
            "★_the_uncontested_remainder": {
                "what_it_is": "the spans this pass proposes to archive that the safeguard did NOT "
                              "read and keep — the only proposals that ask the user for something "
                              "no reading at the file has already refused",
                "spans": len([r for r in rows if r["the_class"] != coarse.OPERATIVE
                              and "★_the_A4_safeguard_read_this_span_and_LEFT_IT_AT_SITE" not in r]),
                "characters": sum(r["characters"] for r in rows
                                  if r["the_class"] != coarse.OPERATIVE
                                  and "★_the_A4_safeguard_read_this_span_and_LEFT_IT_AT_SITE"
                                  not in r),
            },
        },
        "against_the_coarse_pass": {
            "★_the_two_are_measured_at_DIFFERENT_TREES_and_the_comparison_is_of_shape_not_size":
                "the coarse decomposition was taken BEFORE the executed split, so its character "
                "counts include the 6,540 characters that act archived. What is comparable is the "
                "SHAPE: how much of the file each pass places by evidence rather than by the "
                "doubt default.",
            "coarse": {
                "measured_at_commit": coarse_data["measured_at_commit"],
                "characters": coarse_file["characters"],
                "spans": coarse_file["spans"],
                "characters_placed_by_the_doubt_default":
                    coarse_file["characters_placed_by_the_doubt_default"],
                "share_placed_by_the_doubt_default":
                    round(100.0 * coarse_file["characters_placed_by_the_doubt_default"]
                          / coarse_file["characters"], 1),
            },
            "finer": {
                "measured_at_commit": PINNED_COMMIT,
                "characters": total,
                "spans": len(rows),
                "characters_placed_by_the_doubt_default": doubt,
                "share_placed_by_the_doubt_default": round(100.0 * doubt / total, 1),
            },
        },
        "the_spans": rows,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive the decomposition and report whether the artifact matches")
    args = ap.parse_args(argv)

    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: the finer CLAUDE.md decomposition does not re-derive")
            return 1
        print("the finer CLAUDE.md decomposition re-derives")
    else:
        OUT.write_text(text, encoding="utf-8", newline="")
        print("wrote", OUT.relative_to(ROOT).as_posix())
    t = art["the_totals"]
    print(f"  {t['characters']:,} characters, {t['spans']} spans, "
          f"{t['characters_placed_by_the_doubt_default']:,} by the doubt default "
          f"({100.0 * t['characters_placed_by_the_doubt_default'] / t['characters']:.1f}%)")
    for name, cell in t["by_class"].items():
        if cell["spans"]:
            print(f"    {name:<40} {cell['spans']:>4} spans  {cell['characters']:>7,} characters")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
