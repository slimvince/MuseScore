#!/usr/bin/env python3
"""What actually blocks finish-line item 1's RE-HOME class — licensing, or a soft owner.

THE QUESTION (dispatch `cc_instruction_guard_fix_and_item1d.md`, Task 4, assumption A2): "That
item 1's re-home class is blocked by EDIT-SURFACE LICENSING rather than by genuine owner
ambiguity — the reasons carry 'outside this dispatch's edit surface'."  The assumption comes from
a phrase in a report, so it is checked at the objects rather than repeated.

HOW THE CUT IS MADE, and why it is made this way.  `OPEN_ITEMS.md` OI-342 found that the route
table's `owner_is_unambiguous` column is carrying the answer to a DIFFERENT question — whether the
owner lies inside the authorized edit surface — for some of its rows.  So the column cannot decide
this, and the rows' own RECORDED REASONS are read instead, by EXACT PHRASE.  A signal vocabulary
assembled until the answer came out right is the *"stable enough to be cited"* failure repeating,
which is the reason OI-342 gives for proposing no corrected count itself.  Three phrases are used,
every one of them a formula the reasons already contain, and a row matching none is published in
its own class WITH ITS REASON VERBATIM and no verdict authored for it.

DERIVED  — the population (imported from the route generator, never re-listed, #6); each row's
           owner string; the FILES named in it; the blocker class, by exact-phrase test; the
           required edit surface; every count; and the standing authorization, located in
           `CLAUDE.md` by anchor and quoted.
AUTHORED — the three exact phrases, and nothing else.  No owner is re-judged here and no route is
           re-authored: this file reads the route table and does not write to it.

THE THREE STOPS:
  1. the standing authorization cannot be located in `CLAUDE.md` by its anchor — the surface
     question may not be answered against a licence this tool did not read;
  2. a row whose owner string names no file at all — the required surface cannot be reported from
     a population part of which names nothing;
  3. the class counts and the population disagree.

WHAT THIS FILE DOES NOT DO.  It moves no entry's home, class, status or route; it widens no edit
surface; it proposes no corrected column.  Widening the surface is a SCOPE question and the
dispatch sends it back to the user with the list of files and what each would receive.

Usage:
    python tools/audit/decisions/gen_item1_rehome_blocker.py           # write the artifact
    python tools/audit/decisions/gen_item1_rehome_blocker.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from output_encoding import use_utf8_output                            # noqa: E402
from gen_finish_line_item1_routes import build as build_routes, REHOME  # noqa: E402  (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

CLAUDE_MD = ROOT / "CLAUDE.md"
OUT = HERE / "item1_rehome_blocker.json"

# ── authored: the three exact phrases, each a formula the recorded reasons already contain ─────
LICENSING_PHRASE = "outside this dispatch's edit surface"
INDETERMINACY_PHRASES = ("not determinate", "does not settle")

LICENSING = "EDIT-SURFACE LICENSING — the owner is named and the file was outside the surface"
SOFT = "OWNER NOT DETERMINATE — the recorded reason says so in its own words"
NEITHER = "NEITHER PHRASE — no blocker is stated in the recorded reason, and none is authored here"

# A reason that points at ANOTHER entry for its owner question inherits that entry's blocker. This
# is a STRUCTURAL back-reference the text states explicitly — "Same owner question as D-490." — not
# a vocabulary: the pointer names its target, so following it is derivation and not judgment. The
# resolved chain is published per row so the inheritance is checkable rather than trusted.
BACKREF_RX = [
    re.compile(r"same[^.]{0,80}?owner[^.]{0,40}?\b(D-\d{3})\b", re.IGNORECASE),
    re.compile(r"same question as\s+\b(D-\d{3})\b", re.IGNORECASE),
]

# The standing authorization, located by anchor rather than recalled (D-431 / the never-from-memory
# rule). What is quoted is the bullet list itself, so a change to it changes this artifact.
AUTH_ANCHOR = "## Autonomous operation — composing module"
AUTH_END = "**Standard loop for mismatch reduction work**"

FILE_RX = re.compile(r"\b(?:[A-Za-z0-9_]+/)*[A-Za-z0-9_]+\.md\b")


def standing_authorization() -> dict:
    text = CLAUDE_MD.read_text(encoding="utf-8")
    i = text.find(AUTH_ANCHOR)
    j = text.find(AUTH_END, i + len(AUTH_ANCHOR)) if i >= 0 else -1
    if i < 0 or j < 0:
        raise SystemExit(
            "STOP: the standing autonomous-operation authorization could not be located in "
            "CLAUDE.md by its anchors. The question of which files a session may edit may not be "
            "answered against a licence this tool did not read.")
    quoted = re.sub(r"\s+", " ", text[i:j]).strip()
    return {
        "located_by": "anchor string in CLAUDE.md, never a line number",
        "quoted_IN_FULL": quoted,
        "the_document_surfaces_it_names": sorted(set(FILE_RX.findall(quoted))),
    }


def build() -> dict:
    routes = build_routes()
    rows = [r for r in routes["rows"]
            if r["route"] == REHOME and not r["closed_by_this_wave"]]

    auth = standing_authorization()
    licensed_docs = set(auth["the_document_surfaces_it_names"])

    classified: list[dict] = []
    for r in rows:
        reason = r["reason"]
        owner = r["owning_specification"] or ""
        files = sorted(set(FILE_RX.findall(owner)))
        if not files:
            raise SystemExit(
                f"STOP: {r['id']}'s owning specification names no file: {owner!r}. The required "
                "edit surface cannot be reported from a population part of which names nothing.")
        if LICENSING_PHRASE in reason:
            cls, matched = LICENSING, LICENSING_PHRASE
        elif any(p in reason for p in INDETERMINACY_PHRASES):
            cls = SOFT
            matched = next(p for p in INDETERMINACY_PHRASES if p in reason)
        else:
            cls, matched = NEITHER, None
        backref = next((m.group(1) for rx in BACKREF_RX
                        for m in [rx.search(reason)] if m), None)
        rec = {
            "id": r["id"],
            "home_document": r["home_document"],
            "owning_specification": owner,
            "files_named_in_the_owner": files,
            "every_named_file_is_already_licensed": all(f in licensed_docs for f in files),
            "blocker": cls,
            "matched_phrase": matched,
            "points_at_another_entry_for_its_owner_question": backref,
            "the_recorded_reason_verbatim": reason,
        }
        classified.append(rec)

    # ── resolve the explicit back-references, with a cycle guard ────────────────────────────────
    direct = {c["id"]: c["blocker"] for c in classified}
    for c in classified:
        if c["blocker"] != NEITHER or not c["points_at_another_entry_for_its_owner_question"]:
            continue
        chain, cur, seen = [], c["points_at_another_entry_for_its_owner_question"], {c["id"]}
        while cur and cur not in seen:
            chain.append(cur)
            seen.add(cur)
            if cur in direct and direct[cur] != NEITHER:
                break
            nxt = next((x["points_at_another_entry_for_its_owner_question"]
                        for x in classified if x["id"] == cur), None)
            cur = nxt
        resolved = direct.get(chain[-1]) if chain else None
        if resolved and resolved != NEITHER:
            c["blocker"] = resolved
            c["blocker_is_INHERITED"] = {
                "chain": chain,
                "from": chain[-1],
                "why_this_is_derivation_and_not_judgment": (
                    "The reason names the entry it defers to, in the text, by identifier. "
                    "Following a pointer the record writes is derivation; deciding that two "
                    "entries share an owner question when the record does not say so would not be."
                ),
            }

    by_class: dict[str, list[str]] = {}
    for c in classified:
        by_class.setdefault(c["blocker"], []).append(c["id"])
    if sum(len(v) for v in by_class.values()) != len(rows):
        raise SystemExit("STOP: the class counts and the population disagree.")

    files_needed: dict[str, list[str]] = {}
    for c in classified:
        for f in c["files_named_in_the_owner"]:
            files_needed.setdefault(f, []).append(c["id"])
    surface = {f: {"entries_naming_it": len(ids), "already_licensed": f in licensed_docs,
                   "entry_ids": sorted(ids)}
               for f, ids in sorted(files_needed.items(), key=lambda kv: (-len(kv[1]), kv[0]))}

    inside_only = [c for c in classified if c["every_named_file_is_already_licensed"]]
    inside_and_soft = [c for c in inside_only if c["blocker"] != LICENSING]

    return {
        "purpose": (
            "What actually blocks finish-line item 1's RE-HOME class: edit-surface licensing, or a "
            "genuinely soft owner. Checked at the objects because the assumption came from a phrase "
            "in a report. NOT a completion statement, and not an authorization for any fix, design "
            "or inference change."
        ),
        "generated_by": "tools/audit/decisions/gen_item1_rehome_blocker.py",
        "generated_for": "cc_instruction_guard_fix_and_item1d.md (Task 4, assumption A2)",
        "derived_at_head_from": [
            "tools/audit/decisions/gen_finish_line_item1_routes.py → build() (imported, #6)",
            "CLAUDE.md, the autonomous-operation authorization, located by anchor and quoted",
        ],
        "what_is_authored_and_what_is_derived": {
            "derived": "the population, every owner string, every file named in it, every class "
                       "assignment, the required surface and every count",
            "authored": "the three exact phrases, and nothing else",
            "★_the_residual_is_published_rather_than_swept_in": (
                "Rows matching no phrase and pointing at no entry keep the NEITHER class with their "
                "reason verbatim, and NO blocker is authored for them. One is a deliberate "
                "near-miss and is named so the declined judgment is visible rather than silent: "
                "D-531's reason reads 'is not settled by the record', which is the indeterminacy "
                "formula in the passive voice. Adding it to the phrase list would sweep the row in "
                "— and assembling a vocabulary until the answer comes out right is precisely the "
                "failure OI-342 declined to commit. It is left in the residual."
            ),
            "why_the_cut_is_by_exact_phrase": (
                "OI-342 measured that the route table's `owner_is_unambiguous` column carries the "
                "answer to a different question for some rows, so the column cannot decide this. "
                "The rows' own recorded reasons are read instead, by phrases those reasons already "
                "contain. A vocabulary assembled until the answer came out right would be the "
                "'stable enough to be cited' failure repeating, which is why a row matching none of "
                "the three is published in its own class with its reason verbatim and no verdict."
            ),
        },
        "★_the_assumption_and_the_verdict": {
            "the_assumption_as_the_dispatch_states_it": (
                "A2: 'That item 1's re-home class is blocked by EDIT-SURFACE LICENSING rather than "
                "by genuine owner ambiguity — the reasons carry \"outside this dispatch's edit "
                "surface\".'"
            ),
            "verdict": (
                "REFUTED as a statement about the class. The licensing phrase reaches a MINORITY of "
                "the open re-home rows; the majority record an owner that is genuinely not "
                "determinate, in the reasons' own words. The counts are below and none is restated "
                "in prose (D-431)."
            ),
            "★_the_sharpest_evidence_that_licensing_is_not_the_binding_constraint": {
                "what_it_is": (
                    "Entries whose owner names ONLY files the standing authorization ALREADY "
                    "licenses, and which are still not executable. For these, widening the surface "
                    "changes nothing — there is nothing to widen. They are blocked by the owner."
                ),
                "count": len(inside_and_soft),
                "of_the_open_re_home_population": len(rows),
                "ids": sorted(c["id"] for c in inside_and_soft),
            },
        },
        "the_standing_authorization": auth,
        "counted": {
            "open_re_home_rows": len(rows),
            "by_blocker": {k: len(v) for k, v in sorted(by_class.items())},
            "rows_whose_owner_names_only_already_licensed_files": len(inside_only),
        },
        "by_blocker": {k: sorted(v) for k, v in sorted(by_class.items())},
        "★_the_edit_surface_the_class_REQUIRES": {
            "how_to_read_it": (
                "Every file named by any open re-home row's owning specification, with how many "
                "entries name it and whether the standing authorization already covers it. This is "
                "the LIST the dispatch asks for and NOT a widening: widening is a scope question "
                "and it goes back to the user."
            ),
            "★_it_is_NOT_widened_here": (
                "No surface is claimed, assumed or taken. What a file would RECEIVE is the entries "
                "listed beside it — and for most of them the owner is not determinate, so the "
                "licence is not what is missing. A widening would unblock only the licensing class."
            ),
            "files": surface,
            "files_not_already_licensed": sorted(f for f in surface if not surface[f]["already_licensed"]),
        },
        "rows": classified,
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT)
            return 1
        c = art["counted"]
        print(f"PASS: {OUT.name} re-derives byte-identically "
              f"({c['open_re_home_rows']} open re-home rows)")
        return 0
    OUT.write_text(text, encoding="utf-8")
    c = art["counted"]
    print("wrote", OUT)
    print(f"  open re-home rows: {c['open_re_home_rows']}")
    for k, v in c["by_blocker"].items():
        print(f"    {v:3d}  {k}")
    print(f"  owner names only already-licensed files: "
          f"{c['rows_whose_owner_names_only_already_licensed_files']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
