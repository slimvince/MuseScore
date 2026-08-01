#!/usr/bin/env python3
"""Generate DECISIONS.md — the decisions register (OI-208), in the ratified shape.

The register is GENERATED from `backbone_decisions.json` (the adjudication's
judgment) plus `cluster_dispositions.json` (the coverage figures), so that no
number in the document is hand-transcribed (CLAUDE.md #17f) and the document
cannot drift from the data behind it (#10).

To change an entry, edit `backbone_decisions.json` and re-run this generator.

Usage
    python tools/audit/decisions/gen_decisions_register.py
    python tools/audit/decisions/gen_decisions_register.py --check   # regenerate and diff
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
>
> **GENERATED FILE — do not hand-edit.** Source of record:
> `tools/audit/decisions/backbone_decisions.json`; generator
> `tools/audit/decisions/gen_decisions_register.py`. Every number below is computed, never
> transcribed.

## How to read an entry

Each entry has five parts.

- **The decision, verbatim** — quoted exactly from the document that records it, word for word.
  (Where the source wrote the passage inside a quotation block, its `>` markers are dropped so the
  entry reads cleanly; nothing else is altered.) Quoted text keeps its original wording even where
  that wording uses a word in a non-musical sense; the plain restatement beneath it does not.
- **In plain words** — one or two sentences, written for a reader who knows music but not this
  project's private vocabulary.
- **Status** — see the table below. Where the record does not say when a decision was made or
  who ratified it, the entry says **not stated**. Nothing is inferred.
- **Home** — where the decision is actually recorded, as `file:line`. A decision about how a
  layer should work belongs in that layer's section of `ARCHITECTURE.md`; entries marked
  **home is not a layer specification** are decisions recorded somewhere else, which is a
  documentation gap and carries an `OPEN_ITEMS.md` row.
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

    out: list[str] = [PREAMBLE, ""]

    out.append("## What is in this register, counted")
    out.append("")
    out.append(f"**{len(decisions)} decisions**, grouped by subject. They were enumerated by reading "
               "the `ARCHITECTURE.md` layer specifications in full, because a decision written as "
               "plain specification carries no ruling vocabulary and no text search can find it. "
               "Every verbatim quote below is mechanically checked to exist at the place it is "
               "cited to (`gen_cluster_dispositions.py --verify`).")
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
    out.append(f"| Decisions recorded outside any layer specification | {len(nonspec)} |")
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
        out.append(f"## {g['id']}. {g['title']}")
        out.append("")
        for d in members:
            out.append(f"### {d['id']} — {d['title']}")
            out.append("")
            for line in d["verbatim"].splitlines():
                stripped = re.sub(r"^\s*>+\s?", "", line)
                out.append(f"> {stripped}" if stripped.strip() else ">")
            out.append("")
            out.append(f"**In plain words.** {d['plain']}")
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
                "  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`."
            out.append(f"**Home.** `{d['home']}`{homemark}")
            out.append("")
            out.append(f"**Provenance.** {d['status_source']}")
            out.append("")
        out.append("---")
        out.append("")

    out.append("## Provenance of this register")
    out.append("")
    out.append(f"- Adjudication: the OI-207 decision-conformance adjudication, 2026-08-01, "
               f"at commit `{dh['head_commit']}`.")
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate into memory and report whether the committed file matches")
    args = ap.parse_args()

    backbone = json.loads(BACKBONE.read_text(encoding="utf-8"))
    disp = json.loads(DISPOSITIONS.read_text(encoding="utf-8"))
    text = render(backbone, disp)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        same = current == text
        print("DECISIONS.md " + ("matches the data" if same else "IS STALE vs the data"))
        return 0 if same else 1

    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO).as_posix()} "
          f"({len(backbone['decisions'])} decisions, {len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
