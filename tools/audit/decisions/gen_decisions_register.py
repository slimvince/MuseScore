#!/usr/bin/env python3
"""Generate the decisions register (OI-208), in the ratified shape.

Since 2026-08-02 (user-directed, at the 228-entry ratification review) the register is emitted
in the INDEX-PLUS-DETAIL shape the open-items register ratified on 2026-07-26: `DECISIONS.md`
is the LEAN INDEX (one table row per decision: ID, title, status, home), and the full entries
(verbatim quote, plain restatement, Why, status, home, provenance) live in one generated file
per group under `decisions/`. The register was previously one file; at 228 full entries it no
longer rendered.

The register is GENERATED from `backbone_decisions.json` (the adjudication's
judgment) plus `cluster_dispositions.json` (the coverage figures), so that no
number in the document is hand-transcribed (CLAUDE.md #17f) and the document
cannot drift from the data behind it (#10).

To change an entry, edit `backbone_decisions.json` and re-run this generator.

Usage
    python tools/audit/decisions/gen_decisions_register.py
    python tools/audit/decisions/gen_decisions_register.py --check   # regenerate and diff ALL emitted files
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
BACKBONE = HERE / "backbone_decisions.json"
DISPOSITIONS = HERE / "cluster_dispositions.json"
OUT = REPO / "DECISIONS.md"

NO_RATIONALE = "derivation not recorded."

NONSPEC_MARK = {
    "gap": "⚠ **home is not the specification that owns it** — a documentation gap; see "
           "`OPEN_ITEMS.md`.",
    "project-convention": "— a project-wide convention with no owning layer; this is its correct "
                          "home.",
    "process": "— a decision about how the work is done, not about the system; this is its "
               "correct home.",
    "unhomed": "⚠ **recorded only on a tracking surface** — an open-item row or a session handoff "
               "block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.",
}
NONSPEC_LABEL = {
    "gap": "a documentation gap",
    "project-convention": "a project-wide convention, correctly homed",
    "process": "a decision about the process, correctly homed",
    "unhomed": "recorded only on a tracking surface, with no home at all",
}

STATUS_LABEL = {
    "live": "LIVE",
    "superseded-by": "SUPERSEDED BY",
    "superseded-in-fact": "SUPERSEDED IN FACT",
    "shelved-with-evidence": "SHELVED WITH EVIDENCE",
    "falsified": "FALSIFIED",
    "deferred": "DEFERRED",
    "not-stated": "NOT STATED",
}

PREAMBLE = """# DECISIONS — the decisions register

> **What this is.** One entry per recorded decision about how this system works: what was
> decided, in the words it was decided in, what it means in plain language, and whether it
> still stands. Nothing else. Whether the code currently obeys a decision is **not** recorded
> here — that is tracked in `OPEN_ITEMS.md` as ordinary rows, each pointing back at the
> decision it violates. The two things change on different clocks, and holding them in one row
> produces a register that silently goes stale.
>
> **Shape ratified by the user, 2026-07-28** (`open_items/OI-208.md`, three rulings).
> **Populated by the OI-207 decision-conformance adjudication, 2026-08-01.**
> **Content RATIFIED by the user, 2026-08-02:** the 115 originally-enumerated entries with the
> user's review corrections applied, and the 113 completion-pass entries (reviewed via the
> pending-ratification reading aid). **Second ratification event, 2026-08-02:** the 23
> residual-pass entries (D-232…D-254), with two qualifications recorded in the entries
> themselves — the four intonation entries (D-244…D-247) ratified-for-now, to be reviewed when
> that held feature's implementation is revisited; and D-248 (tonicization labels deferred)
> ratified with its revisit to be PLANNED (row OI-267 — for maximum-precision inference the
> feature may be needed). **Third ratification event, 2026-08-02:** the 27 phase-1d entries
> (D-255…D-281 — D-266 and D-278 under individual rulings recorded in their entries and at their
> homes) and the four OI-270 split entries (D-282…D-285, each superseded-by its named
> successors). The register-level ratification does not overwrite
> per-entry provenance — an entry saying "ratifier not stated" still means the original record
> of THAT decision does not say; what the 2026-08-02 ratifications establish is that these
> entries are the standing decisions of record.
>
> **GENERATED FILE — do not hand-edit.** Source of record:
> `tools/audit/decisions/backbone_decisions.json`; generator
> `tools/audit/decisions/gen_decisions_register.py`. Every number below is computed, never
> transcribed.
>
> **This file is the INDEX** (the open-items register's index-plus-detail shape, applied here
> 2026-08-02 when the one-file register outgrew rendering): one row per decision below; the FULL
> entries — verbatim quote, plain restatement, Why, status, home, provenance — are in one
> generated file per group under `decisions/`, linked from each group heading.

## How to read an entry

Each entry has six parts.

- **The decision, verbatim** — quoted exactly from the document that records it, word for word.
  (Where the source wrote the passage inside a quotation block, its `>` markers are dropped so the
  entry reads cleanly; nothing else is altered.) Quoted text keeps its original wording even where
  that wording uses a word in a non-musical sense; the plain restatement beneath it does not.
- **In plain words** — one or two sentences, written for a reader who knows music but not this
  project's private vocabulary.
- **Why** — the defense the record gives for the decision: the published research or algorithm
  adopted, the measurement that decided it, or the constraint that forced it, cited to where it
  is written down. Where the record gives none, this reads **derivation not recorded** — the gap
  is stated, never filled in afterwards from memory. (Standing rule: `CLAUDE.md` Conventions,
  *every design decision carries its defense at its home*, user-directed 2026-08-01.)
- **Status** — see the table below. Where the record does not say when a decision was made or
  who ratified it, the entry says **not stated**. Nothing is inferred.
- **Home** — where the decision is actually recorded, as `file:line`. A decision about how a
  layer should work belongs in that layer's section of `ARCHITECTURE.md`, and a decision about
  anything else belongs in the specification that owns it. Where the home is neither, the entry
  says which of four cases it is: a **documentation gap** (a decision that governs a layer or a
  component, not findable from that layer's section — it carries an `OPEN_ITEMS.md` row); a
  decision **recorded only on a tracking surface** (an open-item row or a session handoff block —
  a place for tracking work, not a home for a standing decision); a **project-wide convention**
  with no owning layer, correctly homed in `CLAUDE.md` or the architectural principles; or a
  **decision about the process**, not about the system.
- **Provenance** — where the status comes from, and any later ruling that bears on it.

### The status words

| Status | Meaning |
|---|---|
| **LIVE** | In force. Nothing in the record supersedes, shelves or falsifies it. |
| **SUPERSEDED BY** | A later ruling replaces it. The replacement is named. |
| **SUPERSEDED IN FACT** | A later *build* replaced what it governs, without any ruling that names it. Recorded exactly that way — never quietly upgraded to "superseded by". |
| **SHELVED WITH EVIDENCE** | Withdrawn against a cited measurement. |
| **FALSIFIED** | A cited measurement contradicts it. |
| **DEFERRED** | Decided to be built later. The decision itself stands. |
| **NOT STATED** | The record does not say. |

### Terms used in the plain-language restatements

Standard music theory is used in its standard sense throughout. The terms below are this
project's own and are defined here because they are used before any entry explains them.

| Term | Meaning |
|---|---|
| **layer** | One stage of the analysis, responsible for one question. The stages are: reading the notes; cutting the music into stretches of unchanging sound; deciding the tonality; deciding the chord; deciding the chord's role; and assembling the result for display. |
| **slice** | The smallest stretch of music analysed: a span during which exactly the same notes are sounding. It begins when any note starts or stops and ends at the next such moment. |
| **onset / release** | The moment a note is struck and the moment it stops sounding. |
| **sounding note set** | Every note actually sounding during a stretch — including notes struck earlier and still held. Distinct from the notes *struck* at the start of that stretch. |
| **pitch class** | A note name irrespective of octave: every C is the same pitch class. |
| **the joint estimator** | The current analysis engine. It decides the tonality, the major/minor character, the chord, and where one chord ends and the next begins, all together in one pass rather than one after another. |
| **decode** | One run of that engine over a piece: the search for the best overall reading. |
| **emission** | The part of the engine that asks "how well do these notes fit this chord in this key?" for one moment of music. |
| **prior** | A standing assumption about how likely something is before any notes are examined — for instance that a piece is more likely to be in a common mode than a rare one. |
| **the corpus** | The 326 annotated Bach chorales the engine's numbers were learned from and is graded against. |
| **ground truth** | The published human annotations we grade against — here the *When in Rome* / DCML analyses of those chorales. |
| **held-out** | Music deliberately kept back from the learning step so that the reported accuracy is measured on material the engine has not seen. |
| **content score** | A number the engine assigns to a candidate reading. Higher is better. It is not a probability and cannot be read as one. |
| **gap (in nats)** | The difference between the best reading's content score and the next one's, on the engine's own scale. A larger gap means a more clear-cut decision. *Nats* is the unit that scale is expressed in. |
| **the record** | The single assembled result the program reads when it shows you anything about harmony: the committed reading for each stretch, its alternatives, and the facts derived from them. |
| **the record arm / the legacy arm** | The two code paths that can produce that result — the current one built on the joint estimator, and the older stage-by-stage one it replaced. The current one is what runs. |
| **the robust unit** | The way accuracy is measured: the music is cut at every boundary either we or the annotator placed, and agreement is counted by how much *time* it covers, so that a change in how finely we cut cannot move the number. |
| **the hard stop** | The rule that decides whether a change may ship: the total time on which we name the wrong chord root, counted only where the root is decidable at all, must not increase. |
| **measurement tool** | A script that measures something. (Never called an "instrument" in this project's writing — that word is reserved for a violin.) |
"""


def head_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    except Exception:
        return "unknown"


def render(backbone: dict, disp: dict) -> str:
    decisions = backbone["decisions"]
    groups = backbone["groups"]
    dh = disp["header"]

    status_counts: dict[str, int] = {}
    for d in decisions:
        status_counts[d["status"]] = status_counts.get(d["status"], 0) + 1
    nostated_date = sum(1 for d in decisions if d["date"] == "not stated")
    nostated_who = sum(1 for d in decisions if d["ratified_by"] == ["not stated"])
    nonspec = [d for d in decisions if not d.get("home_is_layer_spec")]
    no_rationale = [d for d in decisions if not d.get("rationale")]

    out: list[str] = [PREAMBLE, ""]

    out.append("## What is in this register, counted")
    out.append("")
    out.append(f"**{len(decisions)} decisions**, grouped by subject. They were enumerated by reading "
               "`ARCHITECTURE.md` and `CLAUDE.md` in full, because a decision written as plain "
               "specification carries no ruling vocabulary and no text search can find it, and by "
               "following the recorded rulings that live only in an open-item row, a handoff "
               "block, or one of the standing decision-bearing surfaces. Every verbatim quote "
               "below is mechanically checked to exist at the place it is cited to, and to start "
               "at the line it is cited to (`gen_cluster_dispositions.py --verify`), and every "
               "`D-…` and `OI-…` cross-reference is checked to resolve.")
    out.append("")
    out.append("| | Count |")
    out.append("|---|---|")
    out.append(f"| Decisions recorded | **{len(decisions)}** |")
    for st in ("live", "superseded-in-fact", "superseded-by", "deferred",
               "shelved-with-evidence", "falsified", "not-stated"):
        if status_counts.get(st):
            out.append(f"| — of which {STATUS_LABEL[st].lower()} | {status_counts[st]} |")
    out.append(f"| Decisions whose date is not stated in the record | {nostated_date} |")
    out.append(f"| Decisions whose ratifier is not stated in the record | {nostated_who} |")
    out.append(f"| Decisions recorded outside the specification that owns them | {len(nonspec)} |")
    for kind in ("gap", "unhomed", "project-convention", "process"):
        k = sum(1 for d in nonspec if d.get("nonspec_kind", "gap") == kind)
        if k:
            out.append(f"| — of which {NONSPEC_LABEL[kind]} | {k} |")
    out.append(f"| Decisions whose defense the record does not state | {len(no_rationale)} |")
    out.append("")
    out.append(f"That last row is the one meant to fall. **{len(decisions) - len(no_rationale)} of "
               f"{len(decisions)}** decisions here can point at the research, the measurement, or "
               "the constraint that decided them; the rest cannot, and say so. Filling a gap means "
               "recording the defense where the decision lives — never writing one afterwards from "
               "memory.")
    out.append("")
    out.append("Alongside the register, every one of the harvested statements about decisions in "
               "this repository has been given a recorded disposition, so that none was silently "
               "passed over:")
    out.append("")
    out.append("| | Count |")
    out.append("|---|---|")
    cc = dh["completeness_check"]
    out.append(f"| Harvested statements | **{cc['occurrences_total']}** |")
    out.append(f"| Groups of near-identical statements (\"clusters\") | **{cc['clusters']}** |")
    out.append(f"| Clusters carrying a recorded disposition | **{cc['dispositioned']}** |")
    for k, v in dh["disposition_counts"].items():
        out.append(f"| — {k} | {v} |")
    out.append("")
    out.append("The full disposition table, and the numbered rule behind each one, are in "
               "`tools/audit/decisions/cluster_dispositions.csv` and "
               "`tools/audit/decisions/disposition_manifest.json`.")
    out.append("")
    sc = backbone["header"].get("scope")
    if sc:
        out.append("### What was read, and what was not")
        out.append("")
        out.append(f"**Read in full.** {sc['read_in_full']}")
        out.append("")
        out.append(f"**Not read in full.** {sc['not_read_in_full']}")
        out.append("")
        out.append(f"**The remainder, measured.** {sc['measured_remainder']}")
        out.append("")
        out.append(f"*Why this is stated at all:* {sc['why_declared']}")
        out.append("")
    out.append("---")
    out.append("")

    for g in groups:
        members = [d for d in decisions if d["group"] == g["id"]]
        if not members:
            continue
        gfile = group_filename(g)
        out.append(f"## {g['id']}. {g['title']} — [full entries]({gfile})")
        out.append("")
        out.append("| ID | Decision | Status | Home |")
        out.append("|---|---|---|---|")
        for d in members:
            st = STATUS_LABEL.get(d["status"], d["status"].upper())
            if d["status"] == "superseded-by" and d.get("superseded_by"):
                st = f"{st} {d['superseded_by']}"
            home = d["home"].split(":")[0]
            homeflag = "" if d.get("home_is_layer_spec") else {
                "gap": " ⚠gap", "unhomed": " ⚠tracking-surface-only",
                "project-convention": "", "process": "",
            }.get(d.get("nonspec_kind", "gap"), " ⚠gap")
            why = "" if d.get("rationale") else " · derivation not recorded"
            out.append(f"| {d['id']} | {d['title'].replace('|', '/')} | {st}{why} | `{home}`{homeflag} |")
        out.append("")

    out.append("## Provenance of this register")
    out.append("")
    # `head_commit` is HEAD when the DISPOSITION layer was last generated, which is not the
    # same event as the adjudication.  The two were conflated until 2026-08-02, when the
    # phase-1 pass regenerated the dispositions and the line silently re-stamped itself to a
    # commit made after the adjudication it names (DT-12, caught by the standing self-check).
    out.append("- Adjudication: the OI-207 decision-conformance adjudication, 2026-08-01, at "
               "commit `58dea6702ac8aa9d5ef8b89244b94d587a75f7a5`.")
    out.append(f"- Coverage figures above regenerated at commit `{dh['head_commit']}`.")
    out.append(f"- Backbone data: `{BACKBONE.relative_to(REPO).as_posix()}` "
               f"(sha256 `{dh['inputs']['backbone']['sha256'][:16]}…`).")
    out.append(f"- Harvest: `{dh['inputs']['candidates']['file']}` "
               f"(sha256 `{dh['inputs']['candidates']['sha256'][:16]}…`).")
    out.append(f"- Clustering: `{dh['inputs']['clusters']['file']}` "
               f"(sha256 `{dh['inputs']['clusters']['sha256'][:16]}…`).")
    out.append("- Shape: `open_items/OI-208.md` (user-ratified 2026-07-28).")
    out.append("- Standing rule for keeping it current: a new ratification, shelving or "
               "falsification gets its entry in `backbone_decisions.json` — and a regenerated "
               "`DECISIONS.md` — in the same commit that records it.")
    out.append("")
    return "\n".join(out) + "\n"


def group_filename(g: dict) -> str:
    return f"decisions/group_{g['id']}.md"


def render_entry(d: dict) -> list[str]:
    out: list[str] = []
    out.append(f"### {d['id']} — {d['title']}")
    out.append("")
    for line in d["verbatim"].splitlines():
        stripped = re.sub(r"^\s*>+\s?", "", line)
        out.append(f"> {stripped}" if stripped.strip() else ">")
    out.append("")
    out.append(f"**In plain words.** {d['plain']}")
    out.append("")
    out.append(f"**Why.** {d.get('rationale') or NO_RATIONALE}")
    out.append("")
    st = STATUS_LABEL.get(d["status"], d["status"].upper())
    if d["status"] == "superseded-by" and d.get("superseded_by"):
        st = f"{st} {d['superseded_by']}"
    when = "date not stated" if d["date"] == "not stated" else f"decided {d['date']}"
    who = ("ratifier not stated" if d["ratified_by"] == ["not stated"]
           else "ratified by " + ", ".join(d["ratified_by"]))
    out.append(f"**Status.** {st} · {when} · {who}")
    out.append("")
    homemark = "" if d.get("home_is_layer_spec") else \
        "  " + NONSPEC_MARK.get(d.get("nonspec_kind", "gap"), NONSPEC_MARK["gap"])
    out.append(f"**Home.** `{d['home']}`{homemark}")
    out.append("")
    out.append(f"**Provenance.** {d['status_source']}")
    out.append("")
    return out


def render_group_file(g: dict, members: list[dict]) -> str:
    out: list[str] = []
    out.append(f"# Decisions group {g['id']} — {g['title']}")
    out.append("")
    out.append("> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,")
    out.append("> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);")
    out.append("> the source of record is `tools/audit/decisions/backbone_decisions.json`; the")
    out.append("> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an")
    out.append("> entry, edit the data and regenerate.")
    out.append("")
    for d in members:
        out.extend(render_entry(d))
    return "\n".join(out) + "\n"


def emit_all(backbone: dict, disp: dict) -> dict[Path, str]:
    files: dict[Path, str] = {OUT: render(backbone, disp)}
    for g in backbone["groups"]:
        members = [d for d in backbone["decisions"] if d["group"] == g["id"]]
        if members:
            files[REPO / group_filename(g)] = render_group_file(g, members)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate into memory and report whether every emitted file matches")
    args = ap.parse_args()

    backbone = json.loads(BACKBONE.read_text(encoding="utf-8"))
    disp = json.loads(DISPOSITIONS.read_text(encoding="utf-8"))
    files = emit_all(backbone, disp)

    if args.check:
        stale = [p for p, text in files.items()
                 if (p.read_text(encoding="utf-8") if p.exists() else "") != text]
        if stale:
            for p in stale:
                print(f"STALE vs the data: {p.relative_to(REPO).as_posix()}")
            return 1
        print(f"the register matches the data ({len(files)} files: the index + "
              f"{len(files) - 1} group files)")
        return 0

    (REPO / "decisions").mkdir(exist_ok=True)
    for p, text in files.items():
        p.write_text(text, encoding="utf-8")
    print(f"wrote {len(files)} files: DECISIONS.md (the index, "
          f"{len(files[OUT].splitlines())} lines) + {len(files) - 1} group files under decisions/ "
          f"({len(backbone['decisions'])} decisions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
