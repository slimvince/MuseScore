#!/usr/bin/env python3
"""THE FINER `CLAUDE.md` SPLIT — the reach refreshed, and the ratification surface GENERATED.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 4 of
`cowork_rulings_2026_08_17_sixth_return.md`: the finer measured pass *"delivers a new
ratification surface with per-span fates ... every doubt still defaults to STAYS AT SITE and
every doubt-defaulted span is marked ... nothing moves until the user rules that surface."*

WHAT IT DOES.  Two things, and neither of them edits `CLAUDE.md`.

  1. REFRESHES THE REACH for `CLAUDE.md` at this pass's own commit — who names it, who anchors
     into it at a LINE, which tools parse it, and which register entries are homed in it. The
     split moved anchors, so a surface proposing further moves must carry CURRENT reach. The scan
     is IMPORTED from `gen_governing_surface_readers.measure` rather than re-implemented (#6);
     that module's own artifact and surface re-derive byte-identically, which its `--check`
     proves.
  2. GENERATES the ratification surface from the two artifacts. Nothing on it is hand-typed.

★ WHY NOTHING IS EXCLUDED FROM THE SCAN, stated because the coarse pass DOES exclude three files.
It excludes its own outputs, because each of them names all five governing files and writing them
would change the population the next run counts — unreproducible by construction. That hazard
does not arise here: this pass reads at a PINNED COMMIT at which its own outputs do not exist. So
the reach reported below counts every tracked naming there is, the coarse pass's own artifacts
among them, and is a wider figure than that pass's for that reason.

★ THE SPAN ARTIFACT IS PINNED (2026-08-17).  This surface has been PUT AND RULED, so it may not be
rewritten by a later change to the artifact it was generated from.  The span artifact is read at
the git object of the commit the ruling record names as where the surface was ruled; the full
reason, and the declared departure it was taken under, are at `SPANS_PINNED_AT` below.

THE STOPS:
  * the span artifact missing, or covering a different file, STOPS it — the surface is generated
    from both artifacts and may not be built from half of them;
  * the PINNED span artifact unreadable at its commit STOPS it, and so does a pinned artifact
    whose own reading commit is not the finer pass's pin;
  * a per-file naming tally that does not account for the namings found STOPS it (imported).

Run:
  python tools/audit/gen_claude_md_finer_surface.py
  python tools/audit/gen_claude_md_finer_surface.py --check
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_governing_surface_readers as readers                    # noqa: E402  (path set above)
import gen_claude_md_finer_spans as finer                          # noqa: E402  (path set above)
import gen_governing_surface_spans as coarse                       # noqa: E402  (path set above)

OUT = HERE / "claude_md_finer_readers.json"
SPANS = HERE / "claude_md_finer_spans.json"
SPANS_PATH = "tools/audit/claude_md_finer_spans.json"
SURFACE = ROOT / "ratification_surfaces" / "cowork_claude_md_finer_split_2026_08_17.md"

SUBJECT = finer.SUBJECT
PINNED_COMMIT = finer.PINNED_COMMIT

# ★ THE SPAN ARTIFACT IS READ AT THE COMMIT THE SURFACE WAS RULED AT, NOT FROM THE WORKING TREE
# (`cc_instruction_preparation_ninth.md` Task 0b; a DECLARED DEPARTURE from that dispatch's words,
# reported for the user's ruling and taken in the recoverable direction).
#
# WHAT THIS SURFACE IS. It is a RATIFICATION SURFACE that has been PUT AND RULED: Rulings 1-3 of
# `cowork_rulings_2026_08_17_seventh_return.md` were taken against it, and Rulings 1-2 of
# `cowork_rulings_2026_08_17_eighth_return.md` closed the two spans it proposed. That record's own
# §5 states the finer-archive question is CLOSED.
#
# WHAT FORCED THE PIN. Ruling 1 of the eighth-return record ordered a STANDING CONSTRAINT written
# into `gen_claude_md_finer_spans.py` — a span whose archive classification derives from text
# inside an archive pointer is not archivable wherever the pointer sits. Answering it moved the
# span at pinned lines 53-60 out of the archive classes, which is the ruling working. Regenerating
# THIS surface from the moved artifact would have rewritten the proposal the user actually ruled
# on: the 53-60 row would read STAYS AT SITE, and the surface's own answer sentence would fall
# from "1 span, 845 characters ... proposed on ground no reading has yet refused" to zero. That
# destroys the evidence of what was PUT, which is what #12 and the ruled Kind-1 treatment of
# `cowork_rulings_2026_08_16_preparation_return.md` §6 both exist to prevent, and the executing
# dispatch's own registered expectation forbids moving a population anywhere in that act.
#
# THE PIN'S SHAPE IS THE RULED ONE, applied to a third tool: the check reads its input from the
# git OBJECT at the commit the committed surface records, so the surface stands byte-unchanged as
# the ruling's permanent evidence, still guarded against corruption, permanently insensitive to
# the acts it authorized. The commit is the one the ruling record's own provenance names as where
# the surface was ruled. A later ruling can unpin this in one edit; nothing is lost either way.
#
# ★ THE PIN IS NOW A RULED CLASS, AND THIS ONE IS RECORDED UNDER IT RATHER THAN RE-TAKEN (user,
# 2026-08-17, Ruling 1 of `cowork_rulings_2026_08_17_ninth_return.md`; recorded here by
# `cc_instruction_preparation_tenth.md` Task 1).  What was a declared departure applied to a third
# tool is the rule: *A GENERATED DOCUMENT PUT TO THE USER FOR A RULING JOINS THE PINNED KIND AT THE
# MOMENT IT IS RULED FROM.*  The commit below is unchanged — it is already the commit the ruling
# record names, and re-taking it would move a value for no reason.  The class rule's own home is
# `tools/audit/gen_guard_classification.py`; the derived membership is
# `tools/audit/evidence_pin_membership.json`.
#
# ★ WHAT THE PIN DOES NOT FREEZE, stated so it is not mistaken for the F22 ossification.  The
# UNDERLYING DATA FILE is not pinned and continues to re-derive: `gen_claude_md_finer_spans.py`
# re-cuts and re-classes `CLAUDE.md` on every run, and its own `--check` is what proves the cut
# still accounts for the file.  What is fixed here is ONE thing — the rendering of the document the
# user ruled from.  A later ruling can unpin this member in one edit.
SPANS_PINNED_AT = "cfb69a7ecb21351382b25206616a0349214e44f8"
SPANS_PINNED_AT_IS = (
    "the commit `cowork_rulings_2026_08_17_seventh_return.md` names in its own provenance as where "
    "the surface was ruled: \"The surface ruled is "
    "`ratification_surfaces/cowork_claude_md_finer_split_2026_08_17.md` at commit `cfb69a7ecb`\"")


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning."""


def pinned_spans() -> str:
    """The span artifact AS THE RULED SURFACE WAS GENERATED FROM IT, read at the git object.

    A content-addressed read by explicit hash — the one shell mechanism the standing rule permits —
    so this tool cannot be moved by a later change to the working-tree artifact. The reason is at
    `SPANS_PINNED_AT` above.
    """
    proc = subprocess.run(["git", "-C", str(ROOT), "show", f"{SPANS_PINNED_AT}:{SPANS_PATH}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"the pinned span artifact could not be read at "
                   f"{SPANS_PINNED_AT[:10]}:{SPANS_PATH} — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def build_readers() -> dict:
    if not SPANS.exists():
        raise Stop(f"the finer span artifact is missing: {SPANS} — the surface is generated from "
                   f"BOTH artifacts and may not be built from half of them")
    per_file = readers.measure(SUBJECT, commit=PINNED_COMMIT, own_outputs=frozenset())
    return {
        "what_this_is":
            "WHO READS, ANCHORS INTO, QUOTES OR PARSES `CLAUDE.md`, refreshed at the finer pass's "
            "own commit. A MEASUREMENT ONLY: nothing is edited, no reader is retired, no anchor "
            "is re-aimed. Every figure here is computed; none is transcribed (D-431).",
        "generator": "tools/audit/gen_claude_md_finer_surface.py",
        "dispatch": "cc_instruction_preparation_seventh.md, Task 3",
        "measured_at_commit": PINNED_COMMIT,
        "the_scan_is_imported":
            "tools/audit/gen_governing_surface_readers.measure — the same scan the coarse pass "
            "uses, called at this pass's commit rather than re-implemented (#6).",
        "★_nothing_is_excluded_from_this_scan":
            "The coarse pass excludes its own three outputs because each names all five governing "
            "files, so writing them would change the population its next run counts. That hazard "
            "does not arise here: this reading is taken at a PINNED COMMIT at which this pass's "
            "own outputs do not exist. Every tracked naming is therefore counted — the coarse "
            "pass's own artifacts among them — which makes this a WIDER figure than that pass's "
            "and not a comparable one.",
        "★_what_this_measurement_does_NOT_establish":
            "That a naming is a DEPENDENCY, or that a file naming none of these depends on none "
            "of them. The scan sees TRACKED files only, and a path composed at run time carries "
            "no literal to find — the same bound the retirement caller-check publishes of itself. "
            "The parser list is narrower still: a tool reaches it only when the line that names "
            "the file ALSO carries a read signal, so a tool that derives its inputs from "
            "`CLAUDE.md` across two lines is invisible to it.",
        "per_file": [per_file],
    }


def render(spans: dict, reach: dict) -> str:
    r = reach["per_file"][0]
    t = spans["the_totals"]
    out: list[str] = []

    def add(line: str = "") -> None:
        out.append(line)

    add("# The finer `CLAUDE.md` split — what each part of the standing-rules file is, "
        "and where it should live")
    add()
    add("> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING IS "
        "EXECUTED.**")
    add("> `CLAUDE.md` is **byte-unchanged** by the measurement this surface reports. No span is "
        "moved, no")
    add("> anchor is re-aimed, and every fate below is a **PROPOSAL**. The user rules this "
        "surface; ONE")
    add("> later dispatch then executes what is ruled, and nothing before that.")
    add(">")
    add("> **GENERATED, not hand-written.** Every count, every span and every reader below comes "
        "from two")
    add("> committed artifacts — `tools/audit/claude_md_finer_spans.json` and")
    add("> `tools/audit/claude_md_finer_readers.json` — and nothing is typed by hand.")
    add()

    add("## 0. What is being decided, explained from scratch")
    add()
    add("**The file.** `CLAUDE.md` carries this project's standing rules: the guiding principles, "
        "the")
    add("open-items and decisions register conventions, the gate and threshold policy, the "
        "writing and")
    add("working conventions. Every session reads it before doing anything else.")
    add()
    add("**Why it is being looked at again.** The user's pruning direction named this file FIRST. "
        "A")
    add("coarse measurement predicted about 23% of it was archive material; the executed split "
        "moved")
    add("**3.2%**, because the read-before-move safeguard established that the placement was "
        "largely")
    add("wrong. Ruling 4 of `cowork_rulings_2026_08_17_sixth_return.md` therefore commissioned "
        "THIS pass:")
    add("a finer span unit and stricter recognizers, delivering a new surface with per-span "
        "fates.")
    add()
    add("**What is NOT being proposed.** Nothing is deleted. A span that moves is moved WHOLE to "
        "`CLAUDE_ARCHIVE.md`")
    add("with a dated pointer left at the site it came from. Nothing is lost, which is the "
        "standing")
    add("no-information-loss rule.")
    add()

    add("## 1. The test every fate below is proposed under, as the user ruled it")
    add()
    add("§5(E) of `cowork_rulings_2026_08_16_preparation_return.md`. The line is **not** "
        "current-versus-old.")
    add("It is **READERSHIP: who needs this span, and when.**")
    add()
    add("- **STAYS AT SITE** — a span that changes what a working session does or how it reads a "
        "rule today:")
    add("  the rule itself, the purpose that bounds its application, live caveats, STOP "
        "conditions.")
    add("- **ARCHIVES, with a dated pointer at the site** — a span whose only reader is someone "
        "re-opening")
    add("  the decision or auditing its history: preserved former wordings, declined "
        "alternatives, accepted")
    add("  costs, founding narratives, superseded baselines.")
    add("- **THE DOUBT DEFAULT: a span the test cannot place STAYS AT SITE.** A wrongly archived "
        "operative")
    add("  span fails silently; wrongly kept noise fails visibly and cheaply.")
    add()
    add("**Every span this measurement could not place positively is marked doubt-defaulted "
        "below, and its")
    add("proposed fate is STAYS AT SITE.** That is the ruled default applied mechanically, never "
        "a judgment")
    add("stretched to reach a verdict.")
    add()

    add("## 2. What this pass changed, and the measured evidence for each change")
    add()
    add("| what changed | the measured ground |")
    add("|---|---|")
    add(f"| **A cut at every numbered-principle opener** (`{finer.PRINCIPLE_OPENER.pattern}`) | "
        f"{spans['the_cut_rules']['★_this_pass_own_cut']['the_ground']} |")
    add(f"| **A former-wording marker no longer places a span on its own** — a quotation must "
        f"accompany it, beginning within {finer.QUOTATION_WINDOW} characters | "
        f"{spans['the_recognizer_change_and_its_ground']['the_ground']} |")
    add()
    add("**What the stricter recognizer costs, stated so it is chosen rather than discovered:** "
        + spans["the_recognizer_change_and_its_ground"]["★_what_the_floor_costs"])
    add()
    structural = spans["★_the_two_structural_spans_that_are_never_classed_by_their_words"]
    add("**★ AND TWO KINDS OF SPAN ARE NEVER CLASSED BY THE WORDS THEY CONTAIN**, "
        + structural["found_by"])
    add()
    add(f"- **An archive pointer** (`{structural['an_archive_pointer']['the_pattern']}`) — "
        + structural["an_archive_pointer"]["the_ground"])
    add(f"- **A bare section heading** (`{structural['a_bare_heading']['the_pattern']}`) — "
        + structural["a_bare_heading"]["the_ground"])
    add()
    add("Both are placed at site POSITIVELY rather than by the doubt default: "
        + structural["★_why_they_are_placed_POSITIVELY_rather_than_left_to_the_doubt_default"])
    add()

    add("## 3. The measurement")
    add()
    add("| | characters | lines | spans | placed by the doubt default |")
    add("|---|---:|---:|---:|---:|")
    c = spans["against_the_coarse_pass"]["coarse"]
    f = spans["against_the_coarse_pass"]["finer"]
    add(f"| the coarse pass (before the split) | {c['characters']:,} | | {c['spans']:,} | "
        f"{c['characters_placed_by_the_doubt_default']:,} "
        f"({c['share_placed_by_the_doubt_default']}%) |")
    add(f"| **this pass** (after the split) | {t['characters']:,} | {t['lines']:,} | "
        f"{t['spans']:,} | {t['characters_placed_by_the_doubt_default']:,} "
        f"({f['share_placed_by_the_doubt_default']}%) |")
    add()
    add("**The two are measured at DIFFERENT TREES, so the character counts are not comparable "
        "and the")
    add("shares are what to read.** "
        + spans["against_the_coarse_pass"]
              ["★_the_two_are_measured_at_DIFFERENT_TREES_and_the_comparison_is_of_shape_not_size"])
    add()
    add("### By class, with the proposed fate")
    add()
    add("| class | spans | characters | share of the file | proposed fate |")
    add("|---|---:|---:|---:|---|")
    for name in coarse.CLASSES:
        cell = t["by_class"][name]
        if not cell["spans"]:
            continue
        share = 100.0 * cell["characters"] / t["characters"]
        fate = finer.PROPOSED_FATES[name][0]
        add(f"| {name} | {cell['spans']:,} | {cell['characters']:,} | {share:.1f}% | "
            f"**{fate}** |")
    archivable = sum(t["by_class"][k]["characters"] for k in coarse.CLASSES
                     if k != coarse.OPERATIVE)
    add(f"| **proposed to ARCHIVE, in total** | | **{archivable:,}** | "
        f"**{100.0 * archivable / t['characters']:.1f}%** | |")
    add()

    conflict = spans["★_where_this_pass_proposes_archiving_a_span_the_A4_SAFEGUARD_READ_AND_KEPT"]
    add("### ★ Where this pass proposes archiving a span the read-before-move safeguard already "
        "READ and KEPT")
    add()
    add(conflict["what_this_is"])
    add()
    add("**How to read a conflict:** " + conflict["★_how_to_read_a_conflict"])
    add()
    if not conflict["the_conflicts"]:
        add("*None: no span this pass proposes to archive was among the seventeen the safeguard "
            "kept.*")
        add()
    for row in conflict["the_conflicts"]:
        add(f"- **lines {row['the_finer_span'][0]}–{row['the_finer_span'][1]}**, proposed "
            f"`{row['the_class_this_pass_gives_it']}` — opening *\"{row['the_opening'][:120]}…\"*")
        add(f"  - **The safeguard's own reason for keeping it:** {row['the_safeguards_own_reason']}")
    add()

    add("## 4. What a further split would have to reconcile — the reach, refreshed at this tree")
    add()
    add("An **anchor** is a citation into the file AT A LINE; moving a span above it silently "
        "re-points it")
    add("at something else. This is the half the third batch's STOP made mandatory: a mutation's "
        "reach is")
    add("MEASURED before the act, never assumed.")
    add()
    add("| files naming it | namings | anchored namings | files carrying an anchor | tools that "
        "read or parse it | register entries homed here |")
    add("|---:|---:|---:|---:|---:|---:|")
    add(f"| {r['namers']:,} | {r['namings']:,} | {r['anchored_namings']:,} | "
        f"{r['files_carrying_an_anchor']:,} | {len(r['tools_that_parse_or_read_it']):,} | "
        f"{r['decisions_register_entries_homed_here']:,} |")
    add()
    add("**The tools that read or parse it**, which are what a change of SHAPE breaks rather than "
        "a change")
    add("of line numbers:")
    add()
    for tool in r["tools_that_parse_or_read_it"]:
        add(f"- `{tool}`")
    add()
    add("**What this does NOT establish:** "
        + reach["★_what_this_measurement_does_NOT_establish"])
    add()
    add("**Why nothing is excluded from this scan, unlike the coarse pass's:** "
        + reach["★_nothing_is_excluded_from_this_scan"])
    add()

    add("## 5. The proposed fate, per span")
    add()
    add("Every span of the file, in order. **`doubt`** marks a span no recognizer placed — its "
        "fate is the")
    add("ruled default. The evidence that placed each other span is in the artifact beside it.")
    add()
    add("| lines | kind | characters | class | doubt | proposed fate | opening |")
    add("|---:|---|---:|---|:-:|---|---|")
    for span in spans["the_spans"]:
        opening = span["the_opening"].replace("|", "\\|")[:110]
        add(f"| {span['first_line']}–{span['last_line']} | {span['kind']} | "
            f"{span['characters']:,} | {span['the_class']} | "
            f"{'●' if span['placed_by_the_doubt_default'] else ''} | "
            f"{span['the_proposed_fate']} | {opening}… |")
    add()

    add("## 6. What this surface asks the user to rule")
    add()
    add("1. **The per-span fates in §5** — as proposed, or amended span by span.")
    add("2. **Whether the two recognizer changes in §2 are the right ones**, given what each "
        "costs.")
    add(f"3. **Whether the {f['share_placed_by_the_doubt_default']}% left at site by the doubt "
        f"default is acceptable as it stands**, or whether")
    add("   a further pass should try to place more of it. Under the ruled default every "
        "character of it")
    add("   stays.")
    add()
    rest = conflict["★_the_uncontested_remainder"]
    add("**★ THE ANSWER THIS PASS ACTUALLY GIVES, stated plainly because it is the point of "
        "commissioning it.**")
    add(f"At this grain and under these recognizers, **{100.0 * archivable / t['characters']:.1f}% "
        f"of `CLAUDE.md` — {archivable:,} characters in")
    add(f"{sum(t['by_class'][k]['spans'] for k in coarse.CLASSES if k != coarse.OPERATIVE)} spans "
        f"— is placeable as archive material by evidence.** That is more than the 3.2% the split")
    add("moved and far less than the coarse pass's 23% prediction.")
    add()
    add(f"**And the number that actually decides the question is smaller still: "
        f"{conflict['count']} of those spans were")
    add("ALREADY READ AT THE FILE by the split's own safeguard and deliberately KEPT** (§3 "
        "above). Only")
    add(f"**{rest['spans']} span, {rest['characters']:,} characters**, is proposed on ground no "
        f"reading has yet refused. Of the")
    add("contested ones, exactly one — the principle-#21 overrun — is answered by this pass's "
        "finer cut;")
    add("the rest were kept because the span ITSELF states a rule, and no cut answers that.")
    add()
    add("**So: if the goal is a materially smaller `CLAUDE.md`, this measurement says the "
        "recognizers are")
    add("not the route.** What remains is rule text and amendment records that no pattern over "
        "prose")
    add("separates from the rules they amend. That is a finding about the file, not a failure of "
        "the pass,")
    add("and it is stated here rather than left for the user to infer from a small number.")
    add()
    add("**★ ONE LIMITATION, STATED RATHER THAN LEFT TO BE FOUND.** A cut inside a block yields a "
        "span whose")
    add("sentence may continue in the next one, so a span is not guaranteed to be readable on its "
        "own. That")
    add("is why the fates here are PROPOSALS, and why the read-before-move safeguard binds any "
        "later")
    add("executing act exactly as it bound the last one.")
    add()
    add("**Nothing here is ruled.** `CLAUDE.md` is not edited, no span is moved, no anchor is "
        "re-aimed and no")
    add("reader is touched. This surface proposes; the user rules; ONE later dispatch performs — "
        "in that")
    add("order and no other.")
    add()
    add("*Generated by `tools/audit/gen_claude_md_finer_surface.py` from "
        "`tools/audit/claude_md_finer_spans.json` and `tools/audit/claude_md_finer_readers.json`, "
        "2026-08-17, dispatch `cc_instruction_preparation_seventh.md` Task 3.*")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-derive both outputs and report whether they match")
    args = ap.parse_args(argv)

    reach = build_readers()
    spans = json.loads(pinned_spans())
    if spans["generator"] != "tools/audit/gen_claude_md_finer_spans.py":
        raise Stop("the span artifact is not the finer pass's own")
    if spans.get("measured_at_commit") != PINNED_COMMIT:
        raise Stop("the pinned span artifact's own reading commit is not the finer pass's pin — "
                   f"artifact says {spans.get('measured_at_commit')}, this tool says "
                   f"{PINNED_COMMIT}")
    text = json.dumps(reach, indent=1, ensure_ascii=False) + "\n"
    surface = render(spans, reach)

    if args.check:
        drift = 0
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("STALE: the finer CLAUDE.md reader inventory does not re-derive")
            drift = 1
        if not SURFACE.exists() or SURFACE.read_text(encoding="utf-8") != surface:
            print("STALE: the finer CLAUDE.md ruling surface does not re-derive")
            drift = 1
        if not drift:
            print("the finer CLAUDE.md reader inventory and its ruling surface re-derive")
        return drift

    OUT.write_text(text, encoding="utf-8", newline="")
    SURFACE.parent.mkdir(parents=True, exist_ok=True)
    SURFACE.write_text(surface, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT).as_posix())
    print("wrote", SURFACE.relative_to(ROOT).as_posix())
    p = reach["per_file"][0]
    print(f"  {p['namers']} namers, {p['namings']} namings, {p['anchored_namings']} anchored, "
          f"{len(p['tools_that_parse_or_read_it'])} tools read it, "
          f"{p['decisions_register_entries_homed_here']} register homes")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
