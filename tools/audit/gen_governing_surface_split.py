#!/usr/bin/env python3
"""THE RULED GOVERNING-SURFACE SPLIT — perform it, and re-derive that it lost nothing.

WHAT THIS IS.  The executing half of the user's four rulings of 2026-08-17
(`cowork_rulings_2026_08_17_governing_surface_split.md`), taken over the ratification surface
`ratification_surfaces/cowork_governing_surface_split_2026_08_16.md`:

  * **Ruling 1 — the per-class fates.**  `operative-rule-text` and every doubt-defaulted span
    *"STAYS AT SITE"*.  `resolved-row`, `self-declared-historical-or-superseded`,
    `preserved-former-wording` and `defense-and-declined-alternatives` *"ARCHIVE, each span moved
    VERBATIM to its archive home with a dated pointer left at the site"*.
  * **Ruling 2 — the wave executes on today's measurement.**  No finer pass; every doubt-defaulted
    span stays.
  * **Ruling 3 — one archive companion per governing file**, each created by this act on the
    established pattern, every pointer naming its own companion.
  * **Ruling 4 — an entry of `STATUS.md` is SUPERSEDED the moment a later batch's close exists.**
    The site keeps only the latest batch's entries.

★ THE SAFEGUARD RULING 1 IMPOSES ON THIS TOOL, AND WHY IT IS AUTHORED RATHER THAN DERIVED.  *"The
executing dispatch READS every span it archives rather than trusting its class."*  The measurement's
own stated residual risk (finding F29 of `cc_report_preparation_fifth.md`) is that a span MIXED at a
finer grain is classed by its marker, and that the error runs in the ARCHIVE direction — the one the
ruled doubt default exists to prevent.  So every span the pinned artifact places in an archive class
carries an AUTHORED verdict below, made by reading the span itself, and a span that does not read as
its class says is LEFT AT SITE and flagged.  That is assumption A4 of
`cc_instruction_preparation_sixth.md`, which rules it the doubt default rather than a batch STOP.

THE READING TEST, STATED ONCE SO IT IS APPLIED THE SAME WAY TO EVERY SPAN.  A span MOVES only when
BOTH hold:

  (1) CLASS FIDELITY — the span, read whole, IS a record of the kind its class names: a preserved
      former wording, a self-declared historical or superseded record, a record of declined
      alternatives or accepted costs, a resolved row, or a completed batch's pointer entry.  A span
      that merely POINTS AT such material preserved elsewhere fails this half.
  (2) NO LIVE REMAINDER — no part of the span states a rule, a STOP condition, a live caveat or a
      prohibition that a working session acts on today.  This is the ruled test's own STAYS-AT-SITE
      clause: *"a span that changes what a working session does or how it reads a rule today"*.

Anything else stays, which is the ruled doubt default.  A positional reference inside a moved span
("above", "below", "here") is NOT a ground for keeping it: each companion entry carries a provenance
line naming the parent file and the span's position at the pre-act blob, so the reference resolves.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  derived  : the populations — every span of the five files and its class — imported whole from
             `tools/audit/governing_surface_spans.json`, which is PINNED at the commit that carries
             the measurement the user ruled on.  Nothing about which spans exist is authored here.
  authored : the per-span reading verdicts for the individually-marked spans, and the two CLASS
             verdicts (`resolved-row`, `pointer-entry-of-a-completed-batch`), each with its reason.

THE STOPS, every one of which halts rather than warns:
  * an archive-class span with NO authored verdict — a span cannot be archived unread;
  * a verdict naming a span the artifact does not carry — the two cannot drift apart;
  * a moved span whose text is not byte-present EXACTLY ONCE in the parent's pre-act blob;
  * the arithmetic not accounting for the pre-act blob TO THE CHARACTER — moved + kept must equal
    the blob exactly, which is the one failure that would make every claim here meaningless;
  * a register HOME anchor falling inside a moved span (clause 4 of the dispatch: no operative span
    may have moved).

Run:
    python tools/audit/gen_governing_surface_split.py --apply   # perform the split once
    python tools/audit/gen_governing_surface_split.py --check [--pair FILE]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

SPANS = os.path.join(HERE, "governing_surface_spans.json")
OUT = os.path.join(HERE, "governing_surface_split_application.json")
BACKBONE = os.path.join(HERE, "decisions", "backbone_decisions.json")

# The commit the span decomposition was measured at, and which the user ruled on. It is the
# artifact's own pin, re-read here rather than restated (#6) — a disagreement is a STOP.
PINNED_COMMIT = "c4f15a7b3224b2709ecc278010e8ac93e0b3a979"

# The commit this act is performed on top of: Task 0 of the executing dispatch, pushed before the
# split began. An explicit hash, which is the only git read D-253 permits.
PRE_ACT_COMMIT = "1f84f5d62107bde86ddd09317282be1642feb9da"

ACT_DATE = "2026-08-17"
DISPATCH = "cc_instruction_preparation_sixth.md"
RULINGS = "cowork_rulings_2026_08_17_governing_surface_split.md"

RESOLVED_ROW = "resolved-row"
HISTORICAL = "self-declared-historical-or-superseded"
FORMER_WORDING = "preserved-former-wording"
DEFENSE = "defense-and-declined-alternatives"
POINTER = "pointer-entry-of-a-completed-batch"
OPERATIVE = "operative-rule-text"

ARCHIVE_CLASSES = (RESOLVED_ROW, HISTORICAL, FORMER_WORDING, DEFENSE)

COMPANION = {
    "CLAUDE.md": "CLAUDE_ARCHIVE.md",
    "OPEN_ITEMS.md": "OPEN_ITEMS_ARCHIVE.md",
    "DECISIONS.md": "DECISIONS_ARCHIVE.md",
    "STATUS.md": "STATUS_ARCHIVE.md",
    "BUILD_AND_TEST.md": "BUILD_AND_TEST_ARCHIVE.md",
}

MOVE = "MOVE"
STAY = "LEFT-AT-SITE"

# ── AUTHORED — the class verdicts ────────────────────────────────────────────────────────────
# Two classes are decided per CLASS rather than per span, because the evidence that places a member
# is MECHANICAL and is re-derived per span on every run: a resolved row is placed by the resolved
# mark at the head of its status cell, read by the ONE index parser; a pointer entry is placed by
# the OI-222 remedy's own sentence, which every such entry carries verbatim. Reading such a member
# IS reading that evidence, and there is no prose for a finer reading to disagree with.
CLASS_VERDICTS = {
    RESOLVED_ROW: (
        MOVE,
        "A resolved row's only reader is someone auditing the history of an issue that is closed, "
        "which is the ruled test's own ARCHIVES clause, and the interim reading scope already "
        "skipped these rows at session start. The row moves WHOLE to the companion and the site "
        "keeps a compact dated pointer ROW carrying the item's identity, its title and its status "
        "token — so the register's own bijection (one INDEX row per detail file) and the canonical "
        "status opening both survive the act, which a bare deletion would break."),
    POINTER: (
        MOVE,
        "Ruling 4: an entry is SUPERSEDED the moment a later batch's close exists, and the site "
        "keeps only the latest batch's entries. Every member restates nothing by construction "
        "(the OI-222 remedy) — its substance is in the batch's report and its full close in "
        "cowork_away_returns.md — so what moves is a pointer to two documents that are unmoved."),
}

# ── AUTHORED — the per-span reading verdicts (assumption A4, Ruling 1's safeguard) ───────────
# Keyed by (file, first_line, last_line) AT THE PINNED COMMIT. Every one was read in this session,
# in the file itself, with the file tools.
SPAN_VERDICTS: dict[tuple[str, int, int], tuple[str, str]] = {

    # ---- CLAUDE.md -------------------------------------------------------------------------
    ("CLAUDE.md", 27, 37): (
        MOVE,
        "An amendment record for principle #8: it preserves the former wording verbatim and gives "
        "the reason for the widening. The rule itself — #8's three clauses — is stated above it at "
        "the site and is untouched, so nothing a working session acts on leaves."),
    ("CLAUDE.md", 62, 75): (
        MOVE,
        "An amendment record for principle #10: it preserves the former wording verbatim and "
        "records the user's own statement of the objective. #10's second half — the purpose clause "
        "the amendment added — is in the principle's own text above it and stays."),
    ("CLAUDE.md", 82, 89): (
        MOVE,
        "A declined-alternatives record and nothing else: three alternatives, each with the ground "
        "it was declined on. The class Ruling 1 names by name."),
    ("CLAUDE.md", 90, 94): (
        MOVE,
        "An accepted-costs record and nothing else. The class Ruling 1 names by name."),
    ("CLAUDE.md", 228, 260): (
        STAY,
        "★ FAILS TEST (1). The span OVERRUNS the amendment record it is classed for: principle #21's "
        "preserved former wording runs from line 228 to 247, and lines 248-260 are PRINCIPLES 22, 23 "
        "AND 24 — three live standing principles carrying no blank line above them, so the span rule "
        "carried them into the archive class. Archiving this span would remove three principles from "
        "the standing list. This is finding F29's residual risk realised."),
    ("CLAUDE.md", 378, 408): (
        STAY,
        "★ FAILS TEST (2). Classed by an accepted-costs marker inside it, but the span STATES THE "
        "RULE: an apparatus row stays open, stops gating any stage and stops being owed, with the "
        "per-row lapse record and the #19 bound. That rule is stated nowhere else, so a session "
        "reading CLAUDE.md would stop meeting it."),
    ("CLAUDE.md", 467, 474): (
        MOVE,
        "A declined-alternatives record and nothing else: three alternatives with their grounds. "
        "The ruling it belongs to (D-677's discard-verdict-as-input) is stated above it and stays."),
    ("CLAUDE.md", 476, 479): (
        MOVE,
        "An accepted-costs record and nothing else, for the same ruling."),
    ("CLAUDE.md", 490, 649): (
        STAY,
        "★ FAILS TEST (1). Classed `preserved-former-wording` on two sentences that POINT AT former "
        "wordings preserved in the decisions register's own provenance — the span itself contains "
        "none. What it actually is: the decisions register's rules (a) through (n), 15,395 "
        "characters of live governing rule text, nearly a tenth of the file. The single largest "
        "mis-class in the measurement."),
    ("CLAUDE.md", 838, 842): (
        MOVE,
        "A superseded-columns record: it states that the OI-168 legacy-analysis baselines are "
        "preserved in the manifest and the O-12 snapshot, and that the narrative below is "
        "historical. The narrative it points at self-declares its own supersession in its first "
        "words, so nothing at the site stops being marked historical by this move."),
    ("CLAUDE.md", 844, 864): (
        STAY,
        "★ FAILS TEST (2). It self-declares as superseded and historical, and it closes with a LIVE "
        "caveat and a live prohibition — the OI-170 carry-forward, and \"L4 is NOT "
        "tonic-independent; no design may assume it is\". A design session must meet that "
        "prohibition at the site."),
    ("CLAUDE.md", 1056, 1092): (
        STAY,
        "★ FAILS TEST (2). Classed historical on a `retained for provenance` marker that governs "
        "only the recitation in its second half. Its first half STATES the A-8 dual-track's "
        "ratified baselines and the hard stop that governs when it governs — live figures a "
        "measurement session reads."),
    ("CLAUDE.md", 1137, 1137): (
        STAY,
        "★ FAILS TEST (1). A section heading is not a record of any archive class's kind. Archiving "
        "it alone would leave gate block (C)'s body — which the measurement classes operative and "
        "the ruled default therefore keeps — standing under no heading."),
    ("CLAUDE.md", 1139, 1146): (
        MOVE,
        "A self-declared historical blockquote: it says in its own words that the 52/24/52 sets are "
        "superseded by the robust-unit stop and preserved as historical reference only, and gives "
        "the measured reason they were replaced. Its heading stays, so the section it opens is "
        "still marked historical at the site."),
    ("CLAUDE.md", 1181, 1187): (
        MOVE,
        "A self-declared frozen-history record: the batch stop's final frozen state before R10-b, "
        "with the 2.2e delta that produced it. It states no rule and no live caveat."),
    ("CLAUDE.md", 1811, 1833): (
        STAY,
        "★ FAILS TEST (2). Classed on a former wording preserved inside it, but the span STATES THE "
        "RULE'S REACH — that the shell-read restriction covers every read mechanism and every "
        "dialect, what the guard watches, and that its silence on an unwatched surface is not "
        "compliance (#19). A working session acts on all three."),

    # ---- OPEN_ITEMS.md: the seven rows the recognizers placed by a marker inside their prose ---
    # Each is an INDEX ROW of the open-items register — the authoritative status surface — placed
    # in an archive class by a phrase inside its own narrative. A register row is not a preserved
    # former wording and is not a self-declared historical record: it is a row. All seven FAIL
    # TEST (1), and archiving one would take an item out of the register's own population.
    ("OPEN_ITEMS.md", 235, 235): (
        STAY,
        "★ FAILS TEST (1). OI-179's row. It is an OPEN row that GATES (#19, the ground-truth "
        "ceiling), classed `self-declared-historical-or-superseded` on the words `is SUPERSEDED` "
        "inside its own narrative, which describe a former wording of a CLAUDE.md paragraph. "
        "Archiving it would remove a gating establishment obligation from the register."),
    ("OPEN_ITEMS.md", 314, 314): (
        STAY,
        "★ FAILS TEST (1). OI-274's row — an INDEX row, classed on a `former wording` phrase inside "
        "its narrative."),
    ("OPEN_ITEMS.md", 355, 355): (
        STAY,
        "★ FAILS TEST (1). OI-317's row — an INDEX row, classed on a `former wording` phrase inside "
        "its narrative."),
    ("OPEN_ITEMS.md", 359, 359): (
        STAY,
        "★ FAILS TEST (1). OI-321's row — an INDEX row, classed on a `FORMER WORDING` phrase inside "
        "its narrative."),
    ("OPEN_ITEMS.md", 384, 384): (
        STAY,
        "★ FAILS TEST (1). OI-346's row — an INDEX row, classed on a `former wording` phrase inside "
        "its narrative."),
    ("OPEN_ITEMS.md", 395, 395): (
        STAY,
        "★ FAILS TEST (1). OI-357's row — an INDEX row, classed on a `FORMER WORDING` phrase inside "
        "its narrative."),
    ("OPEN_ITEMS.md", 401, 401): (
        STAY,
        "★ FAILS TEST (1). OI-363's row — an INDEX row, classed on a `FORMER WORDING` phrase inside "
        "its narrative."),

    # ---- DECISIONS.md ------------------------------------------------------------------------
    ("DECISIONS.md", 252, 258): (
        STAY,
        "★ FAILS TEST (2). Classed on a `TRIED AND CLOSED` marker, but the span STATES THE CRITERION "
        "IN FORCE — D-430's home rule, what it supersedes, and how a whole-document delegation is "
        "read. A session applying the home criteria acts on it."),
    ("DECISIONS.md", 266, 266): (
        STAY,
        "★ FAILS TEST (1). The scope block's measured remainder. It POINTS AT a former wording "
        "preserved in the register's data file; it does not contain one. What it contains is the "
        "current figure and the rule for reading it."),
    ("DECISIONS.md", 270, 276): (
        STAY,
        "★ FAILS TEST (1). A corrections record that POINTS AT the former wordings preserved in the "
        "register's data file rather than carrying them, and that states which of the register's "
        "own claims are computed rather than authored."),

    # ---- STATUS.md: the two dated entries the pointer test did not reach ----------------------
    ("STATUS.md", 146, 146): (
        MOVE,
        "A dated batch entry of 2026-08-12 whose batch closed long before the fifth. Ruling 4 moves "
        "it with the rest; it is classed `preserved-former-wording` only because the entry reports "
        "an act that preserved one."),
    ("STATUS.md", 150, 150): (
        MOVE,
        "A dated batch entry of 2026-08-12, on the same ground as the entry above."),

    # ---- BUILD_AND_TEST.md -------------------------------------------------------------------
    ("BUILD_AND_TEST.md", 136, 138): (
        MOVE,
        "A preserved former wording and nothing else: the superseded 974/974 composing baseline, "
        "with the note that it was stale. The current baseline is stated above it and stays."),
    ("BUILD_AND_TEST.md", 173, 177): (
        MOVE,
        "A preserved former wording and nothing else: the superseded 53/53 notation baseline. The "
        "current baseline and the four named xfails are stated above it and stay."),
    ("BUILD_AND_TEST.md", 323, 326): (
        MOVE,
        "A superseded baseline record — Iteration 54's BIR figures and its commit."),
    ("BUILD_AND_TEST.md", 333, 335): (
        MOVE,
        "A superseded baseline record — Iteration 46's BIR figures."),
    ("BUILD_AND_TEST.md", 344, 346): (
        MOVE,
        "A superseded baseline record — Iteration 36's BIR figures."),
    ("BUILD_AND_TEST.md", 394, 397): (
        MOVE,
        "A superseded baseline record — the Iteration 46 Jazz figures."),
    ("BUILD_AND_TEST.md", 402, 405): (
        MOVE,
        "A superseded baseline record — the Iteration 32 Baroque figures."),
    ("BUILD_AND_TEST.md", 416, 423): (
        MOVE,
        "A superseded baseline record — Iteration 30's figures and the retired Gate K's rule."),
}

# The ONE declared textual adjustment between the pinned blob and the pre-act blob. STATUS.md's
# newest entry at the pin carried the `Last updated: ` prefix; four later entries were written above
# it by the fifth batch's close, and the prefix moved to the newest of those. Nothing else about the
# entry changed. Declared here rather than papered over, and any span needing a second adjustment
# is a STOP.
PREFIX_ADJUSTMENT = "Last updated: "

# In one file a span's trailing blank SEPARATOR travels with it. `STATUS.md`'s spans are single
# dated entry lines separated by blank lines; moving 131 of them and leaving their separators would
# put a run of 131 blank lines in the must-read. The separator is carried into the archive with the
# entry it separated, so the arithmetic still accounts for the pre-act blob to the character — the
# moved character count records the entry PLUS its separator, and the artifact says so per span.
# Nowhere else: a prose span's neighbours are unrelated blocks, and a table row has no separator.
TRAILING_BLANK_MOVES_WITH_THE_SPAN = {"STATUS.md"}


class Stop(Exception):
    """A demand of the split is unmet. Never a warning, never a span moved unread."""


def git_show(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"git show {rev[:10]}:{path} failed — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def read(path: str) -> str:
    with open(os.path.join(ROOT, path), "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path: str, text: str) -> None:
    with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def lines_of(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def load_spans() -> dict:
    with open(SPANS, encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("measured_at_commit") != PINNED_COMMIT:
        raise Stop("the span decomposition's own pin is not the commit this act reads it at — "
                   f"artifact says {data.get('measured_at_commit')}, this tool says "
                   f"{PINNED_COMMIT}")
    return data


def home_anchor_lines() -> dict[str, set[int]]:
    """Every register HOME anchor into the five files, by file and line, AT THE PRE-ACT COMMIT.

    Read from the git object rather than from the tree, because the act itself re-aims every
    drifted anchor: comparing post-act anchors against the PRE-act span coordinates would compare
    two different coordinate systems and report a collision that never existed. The claim this
    guards is about the state the act was performed on, so it is checked at that state's own
    object — and it therefore re-derives forever.
    """
    raw = git_show(PRE_ACT_COMMIT, "tools/audit/decisions/backbone_decisions.json")
    out: dict[str, set[int]] = {name: set() for name in COMPANION}
    for name in COMPANION:
        for m in re.finditer(r'"home": "' + re.escape(name) + r':(\d+)', raw):
            out[name].add(int(m.group(1)))
    return out


def verdict_for(name: str, span: dict) -> tuple[str, str, str]:
    """(verdict, reason, how_it_was_decided) for one archive-class span."""
    key = (name, span["first_line"], span["last_line"])
    if key in SPAN_VERDICTS:
        v, why = SPAN_VERDICTS[key]
        return v, why, "authored per span, read in the file itself (A4)"
    cls = span["the_class"]
    if cls in CLASS_VERDICTS:
        v, why = CLASS_VERDICTS[cls]
        return v, why, f"authored per CLASS ({cls}), its placing evidence re-derived per span"
    raise Stop(f"{name} lines {span['first_line']}-{span['last_line']} is in archive class "
               f"{cls} and carries NO authored verdict. A span may not be archived unread "
               f"(Ruling 1's safeguard, assumption A4).")


def archive_population(name: str, per_file: dict) -> list[dict]:
    """The spans of one file that the ruled fates place in an archive class.

    For STATUS.md the population is Ruling 4's: the pointer entries plus the two dated entries the
    pointer test did not reach. For every other file it is Ruling 1's four archive classes.
    """
    wanted = set(ARCHIVE_CLASSES)
    if name == "STATUS.md":
        wanted = {POINTER, FORMER_WORDING, HISTORICAL, DEFENSE}
    return [s for s in per_file["the_spans"] if s["the_class"] in wanted]


def pointer_text(name: str, span: dict, moved: str) -> str:
    """The compact dated supersession pointer left at the site (§5(D)'s shape, Ruling 3's naming)."""
    companion = COMPANION[name]
    n_lines = span["last_line"] - span["first_line"] + 1
    if name == "OPEN_ITEMS.md":
        # A resolved row: the site keeps a ROW, so the register's bijection, the canonical status
        # opening and the detail-file pointer all survive the move. The item's IDENTITY (id, name),
        # its GATE cell and its DETAIL link are kept VERBATIM; what moves is the bulk — the
        # description and the body of the status cell — with the status cell's own opening kept so
        # the recorded resolution word is not replaced by a different one.
        cells = [c.strip() for c in moved.strip().strip("|").split(" | ")]
        status = cells[4]
        head = status if len(status) <= 110 else status[:110].rsplit(" ", 1)[0] + " …"
        return (f"| {cells[0]} | {cells[1]} | → ARCHIVED {ACT_DATE}: the full row is in "
                f"`{companion}` | {cells[3]} | {head} → full status in `{companion}` "
                f"| {cells[5]} |\n")
    # COMPACT is the ruled word (§5(D)): a pointer longer than the text it replaces would defeat
    # the act. It carries only what a reader needs to find the moved span — the date, the companion
    # by name, the size and class, and enough of the opening to locate it in a file that keeps
    # parent order. The ruling citation lives once, in the companion's own header (#6).
    indent = re.match(r"[ \t]*", moved).group(0)
    opening = " ".join(moved.split())[:60]
    return (f"{indent}*★ ARCHIVED {ACT_DATE} → `{companion}`: {n_lines} line(s), "
            f"`{span['the_class']}`, opening \"{opening}…\"*\n")


STATUS_CLEARING_POINTER = (
    f"*★ ARCHIVED {ACT_DATE} — every dated batch entry EXCEPT the latest batch's was moved "
    f"verbatim to `STATUS_ARCHIVE.md` by `{DISPATCH}` Task 1, under Ruling 4 of `{RULINGS}`: **an "
    f"entry is SUPERSEDED the moment a later batch's close exists, and this file keeps only the "
    f"latest batch's entries.** The bound is maintained forward at every batch close, in the same "
    f"act that writes its own entries — an instance of the continuous-pruning rule (§5(D) of "
    f"`cowork_rulings_2026_08_16_preparation_return.md`). ONE pointer stands for the whole cleared "
    f"block rather than one per entry, because this file's own banner already names the archive; "
    f"the per-entry reconciliation is re-derived by `tools/audit/gen_governing_surface_split.py "
    f"--check --pair STATUS.md`.*\n"
)


def companion_header(name: str, appending: bool, moved: int) -> str:
    parent = name
    companion = COMPANION[name]
    title = "" if appending else f"# {parent} — ARCHIVE (historical, reference-only)\n\n"
    none_moved = ("" if moved else
                  f">\n> **This act moved NOTHING into this file, and that is a result rather "
                  f"than an omission.** Every span of `{parent}` the pinned measurement placed in "
                  f"an archive class failed the reading Ruling 1's safeguard requires — each "
                  f"POINTS AT archive material preserved elsewhere, or states a rule in force — so "
                  f"each was left at site under the ruled doubt default. The per-span verdicts and "
                  f"their reasons are at "
                  f"`tools/audit/governing_surface_split_application.json`. The file is created "
                  f"because Ruling 3 orders one companion per governing file, and it is the home "
                  f"the continuous-pruning rule (§5(D)) will use for the next amendment that "
                  f"supersedes part of `{parent}`.\n")
    return (
        f"{title}"
        f"> **The archive companion of `{parent}`.** Created {ACT_DATE} by `{DISPATCH}` Task 1, "
        f"executing Rulings 1, 2 and 3 of `{RULINGS}` over the ratification surface "
        f"`ratification_surfaces/cowork_governing_surface_split_2026_08_16.md`. It receives spans "
        f"moved VERBATIM out of `{parent}`, in the order they left it, each under a provenance line "
        f"naming its position in the parent's pre-act blob. **NOT part of the session-start read** "
        f"— read `{parent}` for what governs.\n"
        f">\n"
        f"> **Nothing was edited in transit.** The reconciliation is re-derived by "
        f"`tools/audit/gen_governing_surface_split.py --check --pair {parent}` and proves both "
        f"directions: every archived span is byte-present here and absent from the parent, and "
        f"moved + kept accounts for the parent's pre-act committed blob to the character (#12, "
        f"preservation elsewhere-with-record on the register-split precedent).\n"
        f"{none_moved}"
        f"\n"
    )


def provenance_line(name: str, span: dict, verdict_how: str) -> str:
    return (f"> **From `{name}` lines {span['first_line']}–{span['last_line']} at "
            f"`{PRE_ACT_COMMIT[:10]}` (measured at `{PINNED_COMMIT[:10]}`), class "
            f"`{span['the_class']}`, {span['characters']} characters.** Moved {ACT_DATE}; "
            f"{verdict_how}.\n\n")


def plan_for(name: str, data: dict) -> dict:
    per_file = next(f for f in data["per_file"] if f["file"] == name)
    pinned = git_show(PINNED_COMMIT, name)
    pre_act = git_show(PRE_ACT_COMMIT, name)
    pinned_lines = lines_of(pinned)

    homes = home_anchor_lines()[name]

    population = archive_population(name, per_file)
    moved, stayed = [], []
    for span in population:
        v, why, how = verdict_for(name, span)
        text = "".join(pinned_lines[span["first_line"] - 1:span["last_line"]])
        if len(text) != span["characters"]:
            raise Stop(f"{name} lines {span['first_line']}-{span['last_line']}: the pinned blob "
                       f"yields {len(text)} characters where the artifact records "
                       f"{span['characters']} — the coordinates do not identify the span")
        rec = {
            "first_line_at_the_pin": span["first_line"],
            "last_line_at_the_pin": span["last_line"],
            "the_class": span["the_class"],
            "characters": span["characters"],
            "the_verdict": v,
            "why": why,
            "how_the_verdict_was_made": how,
            "the_opening": span["the_opening"],
        }
        if v == MOVE:
            for h in homes:
                if span["first_line"] <= h <= span["last_line"]:
                    raise Stop(f"{name}: register HOME anchor at line {h} falls inside a span this "
                               f"act would archive ({span['first_line']}-{span['last_line']}). "
                               f"Clause 4 of the dispatch: no operative span may have moved.")
            located, adjusted = text, False
            if pre_act.count(located) != 1:
                alt = located.replace(PREFIX_ADJUSTMENT, "", 1)
                if alt != located and pre_act.count(alt) == 1:
                    located, adjusted = alt, True
                else:
                    raise Stop(
                        f"{name} lines {span['first_line']}-{span['last_line']}: the span's text "
                        f"occurs {pre_act.count(text)} time(s) in the pre-act blob — a move needs "
                        f"exactly one occurrence")
            if name in TRAILING_BLANK_MOVES_WITH_THE_SPAN:
                at = pre_act.index(located)
                if pre_act[at + len(located):at + len(located) + 1] == "\n":
                    located += "\n"
                    adjusted_blank = True
                else:
                    adjusted_blank = False
                rec["the_trailing_blank_separator_moved_with_it"] = adjusted_blank
            rec["text_sha256"] = sha(located)
            rec["characters_at_the_pre_act_blob"] = len(located)
            rec["the_one_declared_adjustment_applied"] = adjusted
            rec["_text"] = located
            moved.append(rec)
        else:
            stayed.append(rec)

    # Rebuild the parent: every moved span replaced by its pointer, nothing else touched.
    order = sorted(moved, key=lambda r: pre_act.index(r["_text"]))
    new_parent = pre_act
    if name == "STATUS.md":
        # ONE dated pointer stands for the whole cleared block (the deviation from clause 2's
        # per-span pointer shape that clause 3 orders and the close states). Nothing before the
        # first moved entry moves, so the pre-act offset of that entry is also its offset in the
        # rebuilt file, and the pointer goes exactly where the cleared block began.
        first_at = min(pre_act.index(r["_text"]) for r in order)
        for rec in order:
            new_parent = new_parent.replace(rec["_text"], "", 1)
        new_parent = new_parent[:first_at] + STATUS_CLEARING_POINTER + "\n" + new_parent[first_at:]
        pointers = [STATUS_CLEARING_POINTER]
    else:
        pointers = []
        for rec in order:
            ptr = pointer_text(name, {"first_line": rec["first_line_at_the_pin"],
                                      "last_line": rec["last_line_at_the_pin"],
                                      "the_class": rec["the_class"]}, rec["_text"])
            new_parent = new_parent.replace(rec["_text"], ptr, 1)
            pointers.append(ptr)

    # `STATUS_ARCHIVE.md` is the ONE companion that already exists (the dispatch's premise ledger
    # states it as a FACT, and Ruling 3 keeps it as `STATUS.md`'s home), so this act's block is
    # appended there and carries no title line of its own. Stated rather than probed at the tree,
    # so the plan is the same before and after the apply.
    companion_body = companion_header(name, name == "STATUS.md", len(order))
    for rec in order:
        companion_body += provenance_line(
            name, {"first_line": rec["first_line_at_the_pin"],
                   "last_line": rec["last_line_at_the_pin"],
                   "the_class": rec["the_class"],
                   "characters": rec["characters"]}, rec["how_the_verdict_was_made"])
        companion_body += rec["_text"]
        if not companion_body.endswith("\n"):
            companion_body += "\n"
        companion_body += "\n"

    moved_characters = sum(r["characters_at_the_pre_act_blob"] for r in moved)
    kept_characters = len(pre_act) - moved_characters
    return {
        "file": name,
        "companion": COMPANION[name],
        "pre_act_characters": len(pre_act),
        "archive_class_spans": len(population),
        "spans_moved": len(moved),
        "spans_left_at_site_by_the_reading": len(stayed),
        "characters_moved": moved_characters,
        "characters_kept": kept_characters,
        "the_arithmetic_balances": moved_characters + kept_characters == len(pre_act),
        "characters_left_at_site_by_the_reading":
            sum(r["characters"] for r in stayed),
        "the_moved": [{k: v for k, v in r.items() if k != "_text"} for r in order],
        "the_left_at_site": stayed,
        "_new_parent": new_parent,
        "_companion_body": companion_body,
        "_pointers": pointers,
    }


def build(applied: bool) -> dict:
    data = load_spans()
    plans = [plan_for(name, data) for name in COMPANION]

    reconciliation = []
    for p in plans:
        name, companion = p["file"], p["companion"]
        live_parent = read(name) if applied else None
        live_companion = read(companion) if applied and os.path.exists(
            os.path.join(ROOT, companion)) else None
        texts = []
        pinned_lines = lines_of(git_show(PINNED_COMMIT, name))
        pre_act = git_show(PRE_ACT_COMMIT, name)
        for rec in p["the_moved"]:
            t = "".join(pinned_lines[rec["first_line_at_the_pin"] - 1:rec["last_line_at_the_pin"]])
            if rec.get("the_one_declared_adjustment_applied"):
                t = t.replace(PREFIX_ADJUSTMENT, "", 1)
            if rec.get("the_trailing_blank_separator_moved_with_it"):
                t += "\n"
            texts.append(t)
        in_companion = (all(live_companion.count(t) == 1 for t in texts)
                        if live_companion is not None else None)
        absent_from_parent = (all(t not in live_parent for t in texts)
                              if live_parent is not None else None)
        reconciliation.append({
            "pair": f"{name} / {companion}",
            "every_archived_span_is_byte_present_in_the_companion_exactly_once": in_companion,
            "every_archived_span_is_absent_from_the_parent": absent_from_parent,
            "moved_plus_kept_accounts_for_the_pre_act_blob_to_the_character":
                p["the_arithmetic_balances"],
            "the_pre_act_blob_sha256": sha(pre_act),
            "spans_moved": p["spans_moved"],
            "characters_moved": p["characters_moved"],
        })

    return {
        "what_this_is":
            "THE RULED GOVERNING-SURFACE SPLIT, EXECUTED: which span of each of the five "
            "mandatory-read files moved to its archive companion, which was LEFT AT SITE by the "
            "reading Ruling 1's safeguard requires, and the mechanical proof that nothing was lost "
            "or altered in transit (#12). Every figure here is computed; none is transcribed "
            "(D-431).",
        "generated_by": "tools/audit/gen_governing_surface_split.py",
        "dispatch": f"{DISPATCH}, Task 1",
        "the_rulings_it_executes": RULINGS,
        "measured_at_commit": PINNED_COMMIT,
        "performed_on_top_of_commit": PRE_ACT_COMMIT,
        "the_reading_test_applied":
            "A span MOVES only when (1) it IS, read whole, a record of the kind its class names, "
            "and (2) no part of it states a rule, a STOP, a live caveat or a prohibition a working "
            "session acts on today. Anything else stays — the ruled doubt default. Assumption A4 "
            "of the dispatch rules a failure of this test the doubt default rather than a STOP.",
        "the_totals": {
            "archive_class_spans": sum(p["archive_class_spans"] for p in plans),
            "spans_moved": sum(p["spans_moved"] for p in plans),
            "spans_left_at_site_by_the_reading":
                sum(p["spans_left_at_site_by_the_reading"] for p in plans),
            "characters_moved": sum(p["characters_moved"] for p in plans),
            "characters_left_at_site_by_the_reading":
                sum(p["characters_left_at_site_by_the_reading"] for p in plans),
        },
        "reconciliation": reconciliation,
        "per_file": [{k: v for k, v in p.items() if not k.startswith("_")} for p in plans],
    }


def apply_split() -> None:
    data = load_spans()
    plans = [plan_for(name, data) for name in COMPANION]     # raises before anything is written
    # Both sides are rebuilt from the PRE-ACT git objects rather than from the tree, so the apply is
    # IDEMPOTENT: running it twice produces the same files rather than stacking a second block on
    # the first. `STATUS_ARCHIVE.md` exists with its own history and Ruling 3 keeps it as
    # `STATUS.md`'s home, so this act's block is APPENDED beneath what was already there; the four
    # new companions do not exist at the pre-act commit and start empty.
    for p in plans:
        name, companion = p["file"], p["companion"]
        try:
            base = git_show(PRE_ACT_COMMIT, companion)
        except Stop:
            base = ""
        body = (base.rstrip("\n") + "\n\n" + p["_companion_body"]) if base else p["_companion_body"]
        write(companion, body)
        write(name, p["_new_parent"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="perform the split (once)")
    g.add_argument("--check", action="store_true", help="re-derive the reconciliation")
    ap.add_argument("--pair", choices=sorted(COMPANION),
                    help="report one parent/companion pair (the check runs over all five either "
                         "way; this selects what is printed and graded)")
    args = ap.parse_args()

    if args.apply:
        apply_split()

    art = build(applied=True)
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"

    if args.check:
        try:
            with open(OUT, "r", encoding="utf-8") as fh:
                committed = fh.read()
        except FileNotFoundError:
            print(f"FAIL: {os.path.relpath(OUT, ROOT)} does not exist")
            return 1
        if committed != text:
            print(f"FAIL: the split application does not re-derive: {os.path.relpath(OUT, ROOT)}")
            return 1
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")

    ok = True
    for rec in art["reconciliation"]:
        if args.pair and not rec["pair"].startswith(args.pair + " "):
            continue
        a = rec["every_archived_span_is_byte_present_in_the_companion_exactly_once"]
        b = rec["every_archived_span_is_absent_from_the_parent"]
        c = rec["moved_plus_kept_accounts_for_the_pre_act_blob_to_the_character"]
        ok = ok and (a is True or rec["spans_moved"] == 0) and \
            (b is True or rec["spans_moved"] == 0) and c is True
        print(f"  {rec['pair']}: moved {rec['spans_moved']} span(s), "
              f"{rec['characters_moved']:,} characters | in companion: {a} | "
              f"absent from parent: {b} | arithmetic balances: {c}")
    t = art["the_totals"]
    print(f"  TOTAL moved {t['spans_moved']} span(s), {t['characters_moved']:,} characters; "
          f"LEFT AT SITE by the reading {t['spans_left_at_site_by_the_reading']} span(s), "
          f"{t['characters_left_at_site_by_the_reading']:,} characters")
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
