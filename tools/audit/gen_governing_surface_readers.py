#!/usr/bin/env python3
"""WHO READS, ANCHORS INTO, QUOTES OR PARSES THE FIVE MANDATORY-READ FILES — measured before any act.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §5(A) of
`cowork_rulings_2026_08_16_preparation_return.md`, which binds the third batch's F13 lesson to this
work PROSPECTIVELY: *"these are the most anchored, quoted and parsed files in the tree (the F2/F4
findings; the one index parser; the register's anchors), so the split's full reach is MEASURED
before any act."*  F13 is the finding that a mutation's reach was assumed rather than measured, and
the assumption was false.  This tool is that measurement, taken before anything moves.

★ IT MEASURES AND IT PROPOSES NOTHING ABOUT ANY READER.  No file is edited, no reader is retired,
and no anchor is re-aimed.  It also GENERATES the ratification surface from its own artifact and
the span decomposition's, because the ruling delivers ONE surface built from both.

★ NO NAMING IS RECORDED BY THE LINE IT WAS FOUND ON, and that is deliberate twice over.  It is the
record's own rule — a coordinate goes stale on the next insertion above it, so a naming is located
by its CONTENT (D-307).  And it is what makes this artifact reproducible: several of the files that
name these five are GENERATED, so a line number inside one of them shifts whenever that generator
runs, and the check would go red with nothing in the record having moved — the OI-301 / OI-305
shape.  MEASURED, not argued: one such field drifted by a single line between two runs of the guard
classification, and it is struck rather than tolerated.

WHAT IS DERIVED, per file, at the current tree:
  * NAMERS       — every tracked file whose text names it, with an example naming quoted.
  * ANCHORS      — every naming of the form `<name>:<line>`, which is a citation INTO the file that
                   a later insertion above that line silently breaks. This is the class the anchor
                   machinery exists for, and the one an unreconciled split would corrupt.
  * PARSERS      — every tracked `.py` whose source both names the file and composes a path to it
                   or reads it. A tool that PARSES a file is broken by a change of shape, not only
                   by a change of line numbers, which is why it is separated from prose citation.
  * REGISTER HOMES — the decisions register's entries homed in the file, with the line each cites.
                   These are the anchored VERBATIMS the establishment pass locates on every run:
                   moving the text they quote is the failure the register's own guard catches.

WHAT IT DOES NOT ESTABLISH, stated before its first use.  A naming is evidence that something
points at the file, NOT that it depends on it; and the scan sees TRACKED files only, so a reader
outside the tracked tree is invisible to it. A path COMPUTED at run time carries no literal to
find — the same bound the retirement caller-check publishes of itself, repeated here rather than
quietly dropped.

THE STOPS:
  * a file the ruling names that the tree does not carry STOPS it;
  * the span decomposition artifact missing, or covering a different file set, STOPS it — the
    surface is generated from BOTH artifacts and may not be built from half of them;
  * a per-file naming tally that does not account for the namings found STOPS it.

Run:
  python tools/audit/gen_governing_surface_readers.py
  python tools/audit/gen_governing_surface_readers.py --check
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

import gen_governing_surface_spans as spans                        # noqa: E402  (path set above)

OUT = HERE / "governing_surface_readers.json"
SPANS = HERE / "governing_surface_spans.json"
SURFACE = (ROOT / "ratification_surfaces"
           / "cowork_governing_surface_split_2026_08_16.md")
BACKBONE = HERE / "decisions" / "backbone_decisions.json"

FILES = spans.FILES          # IMPORTED, never restated (#6)

# ★ THIS MEASUREMENT'S OWN OUTPUTS ARE NOT READERS OF THE FILES IT MEASURES, and counting them
# would make the artifact unreproducible BY CONSTRUCTION: each of the three names all five files,
# so writing them changes the very population the next run counts, and the check goes red without
# anything in the record having moved. The same shape the guard runner already normalizes away for
# a self-stamped commit hash. Nothing else is excluded — an artifact that genuinely names one of
# these files is a naming, whoever produced it.
OWN_OUTPUTS = frozenset({
    "tools/audit/governing_surface_readers.json",
    "tools/audit/governing_surface_spans.json",
    "ratification_surfaces/cowork_governing_surface_split_2026_08_16.md",
})

# A naming that composes a path or reads the file, rather than citing it in prose.
PARSE_SIGNAL = re.compile(
    r"(ROOT|REPO|HERE|Path)\s*/\s*[\"']|open\(|read_text|read_bytes|"
    r"ls-tree|cat-file|\"show\"|'show'")


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning."""


def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode not in (0, 1):
        raise Stop(f"git {' '.join(args)} failed: "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def namings(name: str) -> list[tuple[str, int, str]]:
    """Every tracked line naming the file — ONE `git grep` for the whole tree (the F26 lesson)."""
    out = []
    for line in git("grep", "-n", "-I", "-F", "--", name).split("\n"):
        if not line.strip():
            continue
        parts = line.split(":", 2)
        if len(parts) != 3 or not parts[1].isdigit():
            continue
        path, lineno, text = parts[0], int(parts[1]), parts[2]
        out.append((path.replace("\\", "/"), lineno, text))
    return out


def register_homes(name: str) -> list[dict]:
    data = json.loads(BACKBONE.read_text(encoding="utf-8"))
    rows = []
    for entry in data["decisions"]:
        home = entry["home"]
        if home.split(":")[0].replace("\\", "/") != name:
            continue
        cited = home.split(":", 1)[1] if ":" in home else None
        rows.append({"entry": entry["id"], "cites": cited})
    return sorted(rows, key=lambda r: r["entry"])


def measure(name: str) -> dict:
    if not (ROOT / name).is_file():
        raise Stop(f"a file the ruling names for the measurement is missing: {name}")
    anchor = re.compile(re.escape(name) + r":\d+")

    found = [row for row in namings(name) if row[0] not in OWN_OUTPUTS]
    per_file: dict[str, dict] = {}
    anchors, parsers = [], []
    for path, lineno, text in found:
        if path == name:
            continue
        rec = per_file.setdefault(path, {"namings": 0, "anchored_namings": 0,
                                         "an_example": " ".join(text.split())[:180]})
        rec["namings"] += 1
        for hit in anchor.findall(text):
            rec["anchored_namings"] += 1
            anchors.append({"in": path, "the_anchor": hit})
        if path.endswith(".py") and PARSE_SIGNAL.search(text):
            parsers.append({"tool": path, "the_line": " ".join(text.split())[:180]})

    total = sum(r["namings"] for r in per_file.values())
    counted = sum(1 for path, _l, _t in found if path != name)
    if total != counted:
        raise Stop(f"{name}: the per-file tally accounts for {total} namings against {counted} "
                   f"found — the tally has stopped accounting for the scan")

    homes = register_homes(name)
    return {
        "file": name,
        "namers": len(per_file),
        "namings": total,
        "anchored_namings": len(anchors),
        "files_carrying_an_anchor": len({a["in"] for a in anchors}),
        "tools_that_parse_or_read_it": sorted({p["tool"] for p in parsers}),
        "decisions_register_entries_homed_here": len(homes),
        "of_those_citing_a_line": sum(1 for h in homes if h["cites"]),
        "★_why_the_anchored_namings_matter_most":
            "an anchor is a citation INTO the file at a LINE. Moving a span above it silently "
            "re-points it at something else, which is the failure the anchor machinery and the "
            "register's establishment pass exist against — and the reason the ruling orders this "
            "measurement BEFORE any act rather than after one.",
        "the_anchors": anchors,
        "the_parsers": parsers,
        "the_register_homes": homes,
        "the_namers": dict(sorted(per_file.items())),
    }


def build() -> dict:
    if not SPANS.exists():
        raise Stop(f"the span decomposition artifact is missing: {SPANS} — the surface is "
                   f"generated from BOTH artifacts and may not be built from half of them")
    decomposition = json.loads(SPANS.read_text(encoding="utf-8"))
    measured = [f["file"] for f in decomposition["per_file"]]
    if measured != list(FILES):
        raise Stop(f"the span decomposition covers {measured}, and this measurement covers "
                   f"{list(FILES)} — the two artifacts must be about the same files")

    per_file = [measure(name) for name in FILES]
    return {
        "what_this_is":
            "WHO READS, ANCHORS INTO, QUOTES OR PARSES THE FIVE MANDATORY-READ FILES, measured at "
            "the current tree BEFORE any pruning act. A MEASUREMENT ONLY: nothing is edited, no "
            "reader is retired, no anchor is re-aimed. It is the second of the two artifacts the "
            "ruled read-only pruning batch delivers.",
        "generator": "tools/audit/gen_governing_surface_readers.py",
        "dispatch": "cc_instruction_preparation_fifth.md, Task 2",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §5(A)",
            "why_it_runs_BEFORE_any_act":
                "these are the most anchored, quoted and parsed files in the tree (the F2/F4 "
                "findings; the one index parser; the register's anchors), so the split's full "
                "reach is MEASURED before any act",
        },
        "★_what_this_measurement_does_NOT_establish":
            "That a naming is a DEPENDENCY, or that a file naming none of these depends on none "
            "of them. The scan sees TRACKED files only, and a path composed at run time carries "
            "no literal to find — the same bound the retirement caller-check publishes of itself.",
        "the_totals": {
            "namers": sum(f["namers"] for f in per_file),
            "namings": sum(f["namings"] for f in per_file),
            "anchored_namings": sum(f["anchored_namings"] for f in per_file),
            "register_entries_homed_in_these_files":
                sum(f["decisions_register_entries_homed_here"] for f in per_file),
        },
        "per_file": per_file,
    }


# ── the ratification surface, GENERATED from both artifacts ──────────────────────────────────────

def render_surface(readers: dict, decomposition: dict) -> str:
    by_name = {f["file"]: f for f in readers["per_file"]}
    spans_by_name = {f["file"]: f for f in decomposition["per_file"]}
    out: list[str] = []

    def add(line: str = "") -> None:
        out.append(line)

    add("# The governing-surface split — what each part of the five mandatory reads is, "
        "and where it should live")
    add()
    add("> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING IS "
        "EXECUTED.**")
    add("> No governing file is edited by the measurement this surface reports, no span is moved, "
        "and no")
    add("> fate below is decided. Every fate is a PROPOSAL. The user rules this surface; ONE later "
        "dispatch")
    add("> then executes what is ruled, and nothing before that.")
    add(">")
    add("> **GENERATED, not hand-written.** Every count, every span and every reader below comes "
        "from two")
    add("> committed artifacts — `tools/audit/governing_surface_spans.json` and")
    add("> `tools/audit/governing_surface_readers.json` — and nothing is typed by hand.")
    add()

    add("## 0. What is being decided, explained from scratch")
    add()
    add("**The five files.** Every session — the writing side and the coding side alike — is "
        "ordered to read")
    add("five files before it does anything else: `CLAUDE.md` (the standing rules), "
        "`OPEN_ITEMS.md` (the")
    add("open-issues index), `DECISIONS.md` (the index of what was decided), `STATUS.md` (what "
        "state the")
    add("work is in) and `BUILD_AND_TEST.md` (how to build, test and measure). They are the "
        "mandatory reads.")
    add()
    add("**The problem, in the user's own words:** *\"we need to prune (at least) claude.md and "
        "open_items.md")
    add("because the mandatory reads at session start for you and CC are too large (we are already "
        "hitting")
    add("quality problems - and there are also other issues like real monetary cost and response "
        "times).\"*")
    add()
    add("**What is NOT being proposed.** Nothing is deleted. A span that moves is moved WHOLE to a "
        "place")
    add("that keeps it — an archive file, or the document that properly owns it — with a dated "
        "pointer left")
    add("at the site it came from. Nothing is lost, which is the standing no-information-loss rule.")
    add()

    add("## 1. The test every fate below is proposed under, as the user ruled it")
    add()
    add("The line is **not** current-versus-old. It is **READERSHIP: who needs this span, and "
        "when.**")
    add()
    add("- **STAYS AT SITE** — a span that changes what a working session does or how it reads a "
        "rule today:")
    add("  the rule itself, the purpose that bounds its application, live caveats, STOP conditions.")
    add("- **ARCHIVES, with a dated pointer at the site** — a span whose only reader is someone "
        "re-opening")
    add("  the decision or auditing its history: preserved former wordings, declined alternatives, "
        "accepted")
    add("  costs, founding narratives, superseded baselines. That reader needs it at the moment of")
    add("  re-opening, not at session start, and the pointer takes them there.")
    add("- **MOVES TO ITS PROPER HOME** — a span that is not archive material but mis-homed.")
    add("- **THE DOUBT DEFAULT: a span the test cannot place STAYS AT SITE.** A wrongly archived "
        "operative")
    add("  span fails silently; wrongly kept noise fails visibly and cheaply. Staying is the "
        "recoverable")
    add("  direction.")
    add()
    add("**Every span this measurement could not place positively is marked as doubt-defaulted "
        "below, and")
    add("its proposed fate is STAYS AT SITE.** That is the ruled default applied mechanically, "
        "never a")
    add("judgment stretched to reach a verdict.")
    add()

    add("## 2. How big the problem is — the measurement, per file")
    add()
    add("| file | characters | lines | spans | anchored namings into it | register entries homed "
        "here |")
    add("|---|---:|---:|---:|---:|---:|")
    for name in FILES:
        s, r = spans_by_name[name], by_name[name]
        add(f"| `{name}` | {s['characters']:,} | {s['lines']:,} | {s['spans']:,} | "
            f"{r['anchored_namings']:,} | {r['decisions_register_entries_homed_here']:,} |")
    add(f"| **total** | **{decomposition['the_totals']['characters']:,}** | | "
        f"**{decomposition['the_totals']['spans']:,}** | "
        f"**{readers['the_totals']['anchored_namings']:,}** | "
        f"**{readers['the_totals']['register_entries_homed_in_these_files']:,}** |")
    add()

    add("## 3. What each file is made of, by class")
    add()
    add("The classes are the ruling's own. Each span is placed by a recognizer over its own text, "
        "and the")
    add("marker that placed it is published in the artifact beside the verdict.")
    add()
    for name in FILES:
        s = spans_by_name[name]
        add(f"### `{name}`")
        add()
        add("| class | spans | characters | share of the file |")
        add("|---|---:|---:|---:|")
        for category in spans.CLASSES:
            cell = s["by_class"][category]
            share = (100.0 * cell["characters"] / s["characters"]) if s["characters"] else 0.0
            add(f"| {category} | {cell['spans']:,} | {cell['characters']:,} | {share:.1f}% |")
        doubt = s["characters_placed_by_the_doubt_default"]
        share = (100.0 * doubt / s["characters"]) if s["characters"] else 0.0
        add(f"| — of which no recognizer placed (**doubt-defaulted**) | | {doubt:,} | "
            f"{share:.1f}% |")
        add()

    add("## 4. The proposed fates, per class")
    add()
    add("Each fate below applies to every span of that class, in every file. The per-span list is "
        "in the")
    add("artifact; nothing is decided per span by hand, which is what keeps this a measurement "
        "rather than")
    add("a sweep of judgments.")
    add()
    add("| class | proposed fate | why, under the ruled test |")
    add("|---|---|---|")
    for category, fate, why in PROPOSED_FATES:
        add(f"| {category} | **{fate}** | {why} |")
    add()

    add("## 5. What a split would have to reconcile — the readers, measured before any act")
    add()
    add("This is the half the third batch's STOP made mandatory: a mutation's reach is MEASURED "
        "before the")
    add("act, never assumed. An **anchor** is a citation into a file AT A LINE; moving a span "
        "above it")
    add("silently re-points it at something else.")
    add()
    add("| file | files naming it | namings | anchored namings | files carrying an anchor | tools "
        "that read or parse it |")
    add("|---|---:|---:|---:|---:|---:|")
    for name in FILES:
        r = by_name[name]
        add(f"| `{name}` | {r['namers']:,} | {r['namings']:,} | {r['anchored_namings']:,} | "
            f"{r['files_carrying_an_anchor']:,} | {len(r['tools_that_parse_or_read_it']):,} |")
    add()
    add("**The tools that read or parse each file**, which are what a change of SHAPE breaks "
        "rather than a")
    add("change of line numbers:")
    add()
    for name in FILES:
        r = by_name[name]
        add(f"- `{name}` — " + (", ".join(f"`{t}`" for t in r["tools_that_parse_or_read_it"])
                                or "*none found*"))
    add()
    add("**What this does NOT establish:** " + readers["★_what_this_measurement_does_NOT_establish"])
    add()

    add("## 6. What this surface asks the user to rule")
    add()
    add("1. **The per-class fates in §4** — each one, as proposed or amended.")
    add("2. **Whether the doubt-defaulted share in §3 is acceptable as it stands**, or whether a "
        "further")
    add("   measured pass should try to place more of it before anything moves. It is the largest "
        "share")
    add("   of every file, and under the ruled default every character of it stays at site.")
    add("3. **Where each archive destination is**, for the classes proposed to archive — an "
        "existing")
    add("   archive file, or a new one created by the executing act on the established pattern.")
    add("4. **Which `STATUS.md` entries are SUPERSEDED**, which is the one class this test "
        "deliberately")
    add("   does not decide. That file's own rule already says a superseded entry moves to "
        "`STATUS_ARCHIVE.md`")
    add("   instead of accumulating, and ruling (C) brings that rule into the executing act; what "
        "the")
    add("   measurement adds is that this is the largest single block of the five files.")
    add()
    add("**★ ONE LIMITATION OF THE MEASUREMENT, STATED RATHER THAN LEFT TO BE FOUND.** A span is "
        "classed")
    add("from its own text by a recognizer, and a span that is MIXED — live rule text with an "
        "archive")
    add("marker inside it — is classed by the marker. The span rule cuts a block again at every ★ "
        "marker,")
    add("which is the record's own way of opening an amendment, and that correction was made "
        "because")
    add("without it three spans carried 26.8% of `CLAUDE.md` into an archive class. The residual "
        "risk is")
    add("the same shape at a finer grain, and it runs in the ARCHIVE direction — the one the doubt "
        "default")
    add("exists to prevent — so the executing dispatch reads every span it archives rather than "
        "trusting")
    add("its class.")
    add()
    add("**Nothing here is ruled.** No file is edited, no span is moved, no anchor is re-aimed and "
        "no")
    add("reader is touched. This surface proposes; the user rules; ONE later dispatch performs — "
        "in that")
    add("order and no other.")
    add()
    add("*Generated by `tools/audit/gen_governing_surface_readers.py` from "
        "`tools/audit/governing_surface_spans.json` and `tools/audit/governing_surface_readers.json`, "
        "2026-08-16, dispatch `cc_instruction_preparation_fifth.md` Task 2.*")
    return "\n".join(out) + "\n"


# AUTHORED — one proposed fate per class, with its reason stated against the ruled test.
PROPOSED_FATES = (
    (spans.OPERATIVE, "STAYS AT SITE",
     "It is the rule itself, or a span no recognizer placed elsewhere. The ruled doubt default is "
     "that a span the test cannot place stays at site."),
    (spans.RESOLVED_ROW, "ARCHIVES, with a dated pointer at the site",
     "A resolved row's only reader is someone auditing the history of an issue that is closed. The "
     "interim reading scope already skips these rows at session start, so archiving them makes "
     "physical a boundary the user has already ruled."),
    (spans.HISTORICAL, "ARCHIVES, with a dated pointer at the site",
     "The span says of ITSELF that it is historical or superseded. Its reader is someone re-opening "
     "the decision; the pointer takes them there."),
    (spans.FORMER_WORDING, "ARCHIVES, with a dated pointer at the site",
     "The ruling names preserved former wordings as archive material by name. Information loss is "
     "not at stake: preservation elsewhere-with-record is what the register split already did."),
    (spans.DEFENSE, "ARCHIVES, with a dated pointer at the site",
     "The ruling names declined alternatives and accepted costs by name. NOTE THE NARROWNESS: only "
     "a span carrying an explicit declined-alternative or accepted-cost marker is in this class — "
     "a rule's PURPOSE stays at site, because the ruled test says the purpose that bounds a rule's "
     "application is operative."),
    (spans.POINTER, "NOT DECIDED BY THIS TEST — governed by `STATUS.md`'s own archive rule",
     "A dated entry recording a completed batch. The readership test does not settle it and this "
     "surface does not stretch to a verdict: `STATUS.md` carries its OWN rule — *a superseded "
     "entry moves to `STATUS_ARCHIVE.md` instead of accumulating here* — and ruling (C) already "
     "brings that rule into the executing act. What the measurement contributes is the size: this "
     "class is the largest single block of the five files, so which entries are superseded is a "
     "question worth answering rather than a formality. Until it is answered the ruled default "
     "holds and every character of it stays at site."),
)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive both outputs and report whether they match")
    args = ap.parse_args(argv)

    readers = build()
    decomposition = json.loads(SPANS.read_text(encoding="utf-8"))
    text = json.dumps(readers, indent=1, ensure_ascii=False) + "\n"
    surface = render_surface(readers, decomposition)

    if args.check:
        drift = 0
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("STALE: the governing-surface reader inventory does not re-derive")
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("STALE: the governing-surface split ruling surface does not re-derive")
            drift = 1
        if not drift:
            print("the governing-surface reader inventory and its ruling surface re-derive")
        return drift

    OUT.write_text(text, encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT).as_posix())
    print("wrote", SURFACE.relative_to(ROOT).as_posix())
    for f in readers["per_file"]:
        print(f"  {f['file']:<20} {f['namers']:>5} namers, {f['namings']:>6} namings, "
              f"{f['anchored_namings']:>5} anchored, "
              f"{len(f['tools_that_parse_or_read_it']):>3} tools read it")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
