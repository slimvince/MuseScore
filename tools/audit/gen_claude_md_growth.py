#!/usr/bin/env python3
"""WHAT ADDED LINES TO `CLAUDE.md` SINCE THE PRUNING MEASUREMENT — attributed at the git objects.

WHY THIS EXISTS.  `cc_instruction_claude_md_prune_at_amendment_2026_09_07.md` Task 1.  The
governing-surface split archived nine spans out of `CLAUDE.md` on 2026-08-17 and left nine
pointer lines, a net removal of sixty-one lines — and the file is nonetheless LONGER today than
it was at the commit the pruning measurement was taken at.  The dispatch could not close that gap
from the file alone and ordered it closed AT THE OBJECTS, so that the tidy it orders runs against
a known cause rather than against a diagnosis.

★ IT MEASURES.  IT MOVES NOTHING AND IT EDITS `CLAUDE.md` NOT AT ALL.

WHAT IS DERIVED AND WHAT IS AUTHORED.

  DERIVED   the commit chain from the range's end back to its start, walked one PARENT link at a
            time out of the commit objects themselves; which of those commits changed `CLAUDE.md`,
            by comparing the blob identity the object store gives for the file at each of them;
            the added and removed line counts for each such commit, from git's own numstat; the
            line count of the file at each end of the range; and every sum.
  AUTHORED  the two ends of the range, and ONE STATEMENT PER TOUCHING COMMIT of what it added,
            written from the diff itself.

★ THE STATEMENTS ARE READ FROM THE DIFF AND NEVER FROM A COMMIT SUBJECT.  A commit message says
what its author meant to do; the diff says what the file received.  The dispatch orders the first
of those excluded by name, because this artifact's whole purpose is to establish a cause rather
than to repeat a claim.

★ WHY THE HISTORY IS WALKED BY PARENT LINK RATHER THAN LISTED BY A LOG COMMAND.  D-253 permits
four git forms, all by explicit hash — `git show <sha>:path`, `git show --stat <sha>`,
`git cat-file`, `git diff <shaA> <shaB>` — and names a branch-tip or log read as never trusted for
what is current.  A commit object read by `git cat-file` carries its own parent, so the chain is
content-addressed at every step and no log command is needed.

THE STOPS — each one a way this attribution could be wrong while looking complete:
  * the walk not reaching the range's start halts it, so a chain that is not the one claimed
    cannot be published as though it were;
  * a touching commit with no authored statement halts it, so no line change is attributed by
    silence;
  * an authored statement naming a commit the walk does not place as touching halts it, so the
    statements and the measurement cannot drift apart;
  * the per-commit nets not summing to the difference between the two ends' line counts halts it.
    That last one is the load-bearing check: it is what makes the enumeration COMPLETE rather than
    merely non-empty, because a touching commit left out of it would break the sum.

★ WHAT IT DOES NOT ESTABLISH.  That two omissions could not cancel: the sum closing proves the
enumeration accounts for the net, not that no pair of equal-and-opposite errors exists.  The
blob-identity comparison is what bounds that — a commit that changed the file at all changes its
blob identity — so the residual risk is a commit the WALK does not carry, which the walk's own
start-reached STOP is what covers.

Run:
    python tools/audit/gen_claude_md_growth.py            # write the artifact
    python tools/audit/gen_claude_md_growth.py --check     # re-derive it
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output          # noqa: E402  (path set above)
import gen_governing_surface_spans as coarse         # noqa: E402  the pruning measurement's pin (#6)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

OUT = os.path.join(HERE, "claude_md_growth_2026_09_07.json")

SUBJECT = "CLAUDE.md"

# The range's START is the commit the pruning measurement was taken at, IMPORTED from the
# decomposition that owns it rather than restated (#6): a disagreement about which commit that is
# would make this attribution a statement about a different range.
RANGE_START = coarse.PINNED_COMMIT
RANGE_START_IS = ("the commit the governing-surface span decomposition was measured at — the "
                  "measurement the user ruled the pruning wave from")

# The range's END: Task 0 of the executing dispatch, pushed before this task began. An explicit
# hash, which is the only git read D-253 permits.
RANGE_END = "d125281a43192f23a65711199b3ccc27f7f07356"
RANGE_END_IS = ("Task 0 of `cc_instruction_claude_md_prune_at_amendment_2026_09_07.md`, pushed "
                "before this task began. It does not touch the subject file")

DISPATCH = "cc_instruction_claude_md_prune_at_amendment_2026_09_07.md"

# ── AUTHORED — one statement per touching commit, written from that commit's own diff ──────────
# Keyed by the commit's full hash. Every one was read as a diff of the subject file between that
# commit and its parent, with the file tools and with `git diff` by explicit hash; none is taken
# from a commit subject, which the dispatch excludes by name.
STATEMENTS: dict[str, str] = {
    "53e552296ff47d74a7481ef2272682c82531de46":
        "THE EXECUTED GOVERNING-SURFACE SPLIT. Nine spans left the file — two preserved former "
        "wordings, four declined-alternatives or accepted-costs records, and three self-declared "
        "historical blocks — and nine compact dated archive pointers took their place, one per "
        "site, each naming `CLAUDE_ARCHIVE.md`, the span's line count, its class and its opening. "
        "This is the only commit in the range that REMOVES text, and it is the removal the "
        "dispatch's own premise accounts for.",
    "466781625554dc252dd1146a0425bc29086d0884":
        "RULE (a) OF THE OPEN-ITEMS REGISTER SECTION AMENDED, plus its dated amendment record. The "
        "rule's own clause grew — the session-start read moved from the whole INDEX to the derived "
        "gating answer, with the INDEX kept as the authoritative status surface — and a dated "
        "pointer paragraph was added beneath the section, naming the ruling, the executing "
        "dispatch, the #19 precondition, and `CLAUDE_ARCHIVE.md` as where the superseded wording "
        "now lives. THE SUPERSEDED WORDING IS NOT IN THE DIFF: it left in the same act.",
    "15dfb0e1729c3d34bcef18ab37415909139c69a8":
        "`BUILD_AND_TEST.md` DEMOTED TO A CONDITIONAL SESSION-START READ, plus two dated records. "
        "The list heading changed from three files to two, a conditional heading and the demoted "
        "entry were added, then a dated record of the demotion naming its ruling and its archive "
        "home, and a record of `DECISIONS.md` being considered for the same treatment and RULED "
        "OUT, with the ground stated so a later ruling can answer it. THE SUPERSEDED THREE-FILE "
        "LIST IS NOT IN THE DIFF: it left in the same act.",
    "594074e1e1900079e449d2b79a38920d21bca6e6":
        "RULE (a)'s POINTER NARROWED TO THE GATING-ROW IDENTITIES, plus its dated record and the "
        "#19 distinction. The rule's clause grew — the pointer now names `gating_ids` and says "
        "where the grounds stand and when they are opened — followed by a dated record naming the "
        "ruling and the archive home, and a block stating what the GENERATOR proves on every run, "
        "so that a narrower pointer is not read as a weaker establishment. THE SUPERSEDED WORDING "
        "IS NOT IN THE DIFF: it left in the same act.",
    "4c47b55f3ded9f731f60691faec871646fdc4d7b":
        "THREE SHARPENING PARAGRAPHS ADDED INSIDE PRINCIPLES #18, #19 AND #24, and nothing "
        "removed. #18 gains the clause that Class A reaches a causal claim only where the claim is "
        "checkable; #19 gains the clause naming its four objects and stating that a session, a "
        "person or a conversation is never the object of a Class B demand; #24 gains the clause "
        "that a condition which cannot be established at an inspectable object is DECLARED as a "
        "bound. All three are new operative rule text.",
    "3e75ef85bce5805eefee0f5015da59d88cc0582a":
        "ONE NEW CONVENTIONS BULLET, and nothing removed: the ordinary session-start read binds "
        "even when the opening instruction names a single file, with its ratification, its "
        "retrospective finding and its measured evidence. New operative rule text.",
}


class Stop(Exception):
    """A demand of the attribution is unmet. Never a warning, never a gap left unstated."""


def git(*args: str, stdin: bytes | None = None) -> str:
    proc = subprocess.run(["git", "-C", ROOT, *args], input=stdin,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def chain() -> list[str]:
    """Every commit from the range's start to its end, walked by PARENT link, oldest first.

    Read out of the commit objects with `git cat-file`, which is content-addressed at every step —
    so the chain re-derives forever and no log command is trusted for what the history is.
    """
    walk = [RANGE_END]
    seen = {RANGE_END}
    while walk[-1] != RANGE_START:
        body = git("cat-file", "-p", walk[-1])
        parents = [line.split()[1] for line in body.splitlines() if line.startswith("parent ")]
        if not parents:
            raise Stop(f"the walk reached a commit with no parent ({walk[-1][:10]}) before "
                       f"reaching the range's start {RANGE_START[:10]} — the range's ends are not "
                       f"on one chain and this attribution would be about a history that is not "
                       f"the one it claims")
        nxt = parents[0]        # first parent: the branch's own line of development
        if nxt in seen:
            raise Stop(f"the walk revisited {nxt[:10]} — the chain is not a chain")
        seen.add(nxt)
        walk.append(nxt)
    return list(reversed(walk))


def blob_ids(commits: list[str]) -> dict[str, str | None]:
    """The object identity of `CLAUDE.md` at each commit — None where the commit has no such file.

    ONE `git cat-file --batch-check` process for the whole chain: the identity is what decides
    whether a commit changed the file at all, and comparing identities is both exact and cheap.
    """
    query = "".join(f"{sha}:{SUBJECT}\n" for sha in commits).encode("utf-8")
    out = git("cat-file", "--batch-check", stdin=query).splitlines()
    if len(out) != len(commits):
        raise Stop(f"the object store answered {len(out)} of {len(commits)} identity queries — "
                   f"the chain and the answers cannot be paired")
    ids: dict[str, str | None] = {}
    for sha, line in zip(commits, out):
        parts = line.split()
        ids[sha] = parts[0] if len(parts) >= 2 and parts[1] == "blob" else None
    return ids


def line_count(sha: str) -> int:
    return len(git("show", f"{sha}:{SUBJECT}").splitlines())


def build() -> dict:
    commits = chain()
    if commits[0] != RANGE_START or commits[-1] != RANGE_END:
        raise Stop("the walk's ends are not the range's ends")
    ids = blob_ids(commits)

    touching = []
    for parent, child in zip(commits, commits[1:]):
        if ids[parent] == ids[child]:
            continue
        numstat = git("diff", "--numstat", parent, child, "--", SUBJECT).split()
        if len(numstat) < 2:
            raise Stop(f"{child[:10]} changes the subject file's object identity but git reports "
                       f"no numstat for it — the two readings disagree")
        added, removed = int(numstat[0]), int(numstat[1])
        touching.append({
            "commit": child,
            "its_parent_in_this_chain": parent,
            "lines_added": added,
            "lines_removed": removed,
            "net_lines": added - removed,
            "what_it_added": STATEMENTS.get(child),
            "how_the_statement_was_made":
                "read at the diff of the subject file between this commit and its parent; never "
                "from a commit subject",
        })

    unstated = [t["commit"] for t in touching if not t["what_it_added"]]
    if unstated:
        raise Stop(f"touching commit(s) with no authored statement: "
                   f"{[c[:10] for c in unstated]} — a line change may not be attributed by "
                   f"silence")
    carried = {t["commit"] for t in touching}
    stray = sorted(c for c in STATEMENTS if c not in carried)
    if stray:
        raise Stop(f"authored statement(s) naming a commit the walk does not place as touching: "
                   f"{[c[:10] for c in stray]} — the statements and the measurement have drifted "
                   f"apart")

    start_lines, end_lines = line_count(RANGE_START), line_count(RANGE_END)
    net = sum(t["net_lines"] for t in touching)
    closes = net == end_lines - start_lines
    if not closes:
        raise Stop(f"the touching commits' nets sum to {net:+d} where the two ends differ by "
                   f"{end_lines - start_lines:+d} — the enumeration does not account for the "
                   f"growth, and a sum that does not close is reported rather than adjusted")

    removing = [t for t in touching if t["net_lines"] < 0]
    adding = [t for t in touching if t["net_lines"] > 0]
    return {
        "what_this_is":
            "WHAT ADDED LINES TO `CLAUDE.md` BETWEEN THE PRUNING MEASUREMENT AND THIS BATCH, "
            "attributed per commit at the git objects. A MEASUREMENT ONLY: nothing is moved and "
            "the subject file is not edited. Every figure here is computed; none is transcribed "
            "(D-431).",
        "generated_by": "tools/audit/gen_claude_md_growth.py",
        "dispatch": f"{DISPATCH}, Task 1",
        "the_subject": SUBJECT,
        "the_range": {
            "start": RANGE_START,
            "what_that_commit_is": RANGE_START_IS,
            "end": RANGE_END,
            "what_that_commit_is_": RANGE_END_IS,
            "commits_in_the_chain": len(commits),
            "how_the_chain_was_walked":
                "one PARENT link at a time out of the commit objects themselves, with "
                "`git cat-file` — content-addressed at every step, so no log command is trusted "
                "for what the history is (D-253)",
        },
        "the_two_ends_measured": {
            "lines_at_the_range_start": start_lines,
            "lines_at_the_range_end": end_lines,
            "net_lines": end_lines - start_lines,
        },
        "the_attribution": {
            "commits_that_touched_the_subject": len(touching),
            "their_nets_sum_to": net,
            "the_sum_closes_against_the_two_ends": closes,
            "★_what_the_closing_sum_establishes_and_what_it_does_not":
                "ESTABLISHED: the enumerated commits account for the whole net change, so no "
                "touching commit is missing whose effect the others do not already carry. NOT "
                "ESTABLISHED: that two omissions could not cancel. What bounds that is the "
                "identity comparison — a commit that changed the file at all changes its blob "
                "identity — so the residual risk lies in the WALK, which its own start-reached "
                "STOP covers.",
            "the_commits": touching,
        },
        "★_the_shape_the_attribution_shows": {
            "commits_with_a_negative_net": len(removing),
            "the_one_removing_commit":
                "exactly one commit in the range removes text on balance: the executed "
                "governing-surface split. Its net is published with it above.",
            "commits_with_a_positive_net": len(adding),
            "everything_else_is_addition":
                "every other touching commit adds on balance. Read at their diffs, they are of "
                "two kinds: AMENDMENT RECORDS — an amended clause plus the dated paragraph "
                "recording the amendment, its ruling and where the superseded wording now lives — "
                "and new operative rule text with nothing superseded. Which commit is which is "
                "stated per commit above.",
            "★_what_this_refutes_and_what_it_confirms": {
                "confirmed":
                    "the growth since the split is dominated by amendment apparatus. Which "
                    "commit is an amendment record and which is new rule text is stated per "
                    "commit above, and the added-line figures that decide it are computed there.",
                "refuted":
                    "that the growth is caused by rule (D) not being followed. In every one of the "
                    "three amendments the superseded wording is ABSENT FROM THE DIFF — it was "
                    "moved to `CLAUDE_ARCHIVE.md` in the same act and a compact dated pointer was "
                    "left at the site, which is rule (D)'s own prescribed shape. What the "
                    "amendments added is the POINTER AND ITS GROUND, which rule (D) requires.",
                "★_what_neither_of_those_says":
                    "Nothing here is a claim about the preserve-in-place material the file still "
                    "carries. This artifact's range begins at the pruning measurement; text older "
                    "than that range is outside what it can see, and is the separate subject of "
                    "this dispatch's Task 2.",
            },
        },
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="re-derive the attribution and report whether the artifact matches")
    args = ap.parse_args(argv)

    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"

    if args.check:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE: the CLAUDE.md growth attribution does not re-derive")
            return 1
        print("the CLAUDE.md growth attribution re-derives")
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", os.path.relpath(OUT, ROOT))

    e, a = art["the_two_ends_measured"], art["the_attribution"]
    print(f"  {e['lines_at_the_range_start']} -> {e['lines_at_the_range_end']} lines "
          f"({e['net_lines']:+d}) over {art['the_range']['commits_in_the_chain']} commits")
    print(f"  {a['commits_that_touched_the_subject']} touched the file; their nets sum to "
          f"{a['their_nets_sum_to']:+d}; the sum closes: {a['the_sum_closes_against_the_two_ends']}")
    for t in a["the_commits"]:
        print(f"    {t['commit'][:10]}  +{t['lines_added']} -{t['lines_removed']}  "
              f"net {t['net_lines']:+d}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
