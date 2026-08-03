#!/usr/bin/env python3
"""Enumerate the paths git reports as changed — and NOTHING else.

WHAT THIS IS.  Task 1 of the phase-1s wave
(`cc_instruction_phase1s_stale_rules_and_enumeration.md` §2), on the user's ruling of
2026-08-03 (Y1).  It is the sanctioned way to answer *which paths changed* — before a commit,
and after one — without breaking the file-tools rule (register entry **D-253**).

WHY IT IS NOT A NARROWING OF THAT RULE.  D-253's recorded defense is specific: a stale mount
made the shell path return wrong CONTENT while the file tools read the live disk correctly, and
the git-object exemption survives because content-addressed reads are self-verifying — they
error loudly rather than returning silently-wrong content.  **Both halves of that defense are
about content.**  A list of which paths changed is not content, so the rule's letter is
untouched and what changes is only that the answer now comes from a committed tool instead of a
raw shell command.  Without that reasoning recorded here this tool looks like a wrapper around a
forbidden command, which is exactly what it must not be.

★ THE STRUCTURAL PROPERTY, WHICH IS THE WHOLE JUSTIFICATION.  This module is incapable of
returning file content, by construction rather than by intent:

  1. **It never opens a file for reading.**  There is no read-mode `open()` anywhere below.  The
     only writes are the establishment artifact and the establishment's own fixture files, which
     live in a temporary directory outside this repository.
  2. **Every git invocation comes from the frozen table `ALLOWED` below**, and `_git()` refuses
     to run anything else.  The caller supplies no git arguments at all — the command-line flags
     select a row of that table, they do not build one.
  3. **Every row of that table is a git subcommand that cannot emit file content.**
     `status --porcelain`, `diff --name-status` and `diff-tree --name-status` emit a status code
     and a path per record and nothing more.  `diff-tree` is used rather than `show` on purpose:
     `git show <blob-sha>` prints the blob, and `--name-status` does not suppress it, whereas
     `diff-tree` walks commits and trees only and errors on a blob.
  4. **Only two fields per record ever reach the output** — a status code and a path — because
     the parsers return exactly those and the emitters print exactly those.

The one argument this tool accepts from a caller is a commit hash, and it is validated against
`^[0-9a-f]{7,40}$` before use, so no ref, no pathspec and no option can be smuggled through it.

WHAT IT COVERS, AND WHAT IT DOES NOT — stated plainly, because a control believed to be in place
and not in place is worse than none (#19):

  * It reports what GIT reports.  A path git ignores (`.gitignore`) is invisible to it, which is
    the same blind spot every git-based answer has and is why `.claude/settings.json` does not
    appear in any enumeration here.
  * An untracked DIRECTORY is one record naming the directory, not one record per file inside
    it.  That is git's own `--untracked-files=normal`, kept because `=all` expands one scratch
    directory in this repository into hundreds of thousands of characters — output large enough
    to be its own failure under `CLAUDE.md`'s bash Rule 2.
  * `--commit` on a MERGE commit reports nothing: `diff-tree` without `-m`/`-c` emits no records
    for a merge.  This project's waves do not commit merges; if one ever does, the empty result
    must not be read as "the commit touched nothing".
  * It answers WHICH paths, never WHAT changed in them.  Reading a changed file is the file
    tools' job, and that is the division the rule draws.

ESTABLISHMENT (#19).  `--establish` builds a throwaway git repository in a temporary directory,
makes a KNOWN set of modifications in it — one added file, one modified, one deleted, one
renamed, one untracked — and checks that the enumeration reports exactly that set, at the
working tree, at the index, and at a commit.  It then checks that a CLEAN tree reports nothing,
which is the other half the dispatch names.  The artifact is
`tools/audit/changed_paths_establishment.json`.

There is deliberately no `--check` re-derive mode: reading the artifact back would be a
read-mode open, and the structural property above is worth more than the convenience.  The
artifact's own freshness is checked by this tool itself — regenerate it and run the enumeration;
if it changed, it appears in the list.

Run:
    python tools/audit/changed_paths.py                       # the working tree
    python tools/audit/changed_paths.py --staged              # what is staged
    python tools/audit/changed_paths.py --commit <sha>        # what a commit touched
    python tools/audit/changed_paths.py --establish           # measure the tool itself
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ESTABLISH_OUT = os.path.join(HERE, "changed_paths_establishment.json")

REV = re.compile(r"^[0-9a-f]{7,40}$")

# ── the frozen table (structural property 2 and 3) ───────────────────────────
# `{rev}` is the ONLY substitution, and only a validated hash may fill it. Nothing here can
# emit the content of a file; see the docstring for why `diff-tree` and not `show`.
ALLOWED: dict[str, tuple[str, ...]] = {
    # `--untracked-files=normal` (git's default) collapses an untracked DIRECTORY into one
    # record. That is deliberate: `=all` expands `scratch_artifacts/` alone into hundreds of
    # thousands of characters, and a single tool call producing output that large is the very
    # thing `CLAUDE.md`'s bash Rule 2 forbids. The cost is stated in `coverage_limits`.
    "worktree": ("status", "--porcelain=v1", "-z"),
    "staged": ("diff", "--cached", "--name-status", "-z"),
    "commit": ("diff-tree", "--no-commit-id", "--name-status", "-r", "-z", "{rev}"),
}


def _git(mode: str, cwd: str, rev: str | None = None) -> str:
    """Run one row of ALLOWED. Refuses anything that is not a row of it."""
    if mode not in ALLOWED:
        raise SystemExit(f"changed_paths: {mode!r} is not one of the sanctioned enumerations")
    argv = []
    for part in ALLOWED[mode]:
        if part == "{rev}":
            if rev is None or not REV.match(rev):
                raise SystemExit("changed_paths: --commit takes an explicit hash "
                                 "(7-40 hex characters), never a ref or a pathspec")
            argv.append(rev)
        else:
            argv.append(part)
    proc = subprocess.run(["git", "-C", cwd] + argv, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=False)
    if proc.returncode != 0:
        raise SystemExit("changed_paths: git failed — "
                         + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout.decode("utf-8", "replace")


# ── the parsers (structural property 4: two fields out, never more) ──────────
def _parse_status(out: str) -> list[tuple[str, str]]:
    """`XY path` records, NUL-separated; a rename/copy carries its origin in the next field.

    The two-character code is kept WHOLE and never stripped: `X` is the index and `Y` the
    working tree, so `M ` (staged) and ` M` (unstaged) are different facts and collapsing them
    to `M` would answer a question this tool is not being asked.
    """
    fields = [f for f in out.split("\0") if f != ""]
    rows: list[tuple[str, str]] = []
    i = 0
    while i < len(fields):
        rec = fields[i]
        i += 1
        if len(rec) < 4:
            continue
        code, path = rec[:2], rec[3:]
        if code[0] in ("R", "C") and i < len(fields):
            origin = fields[i]
            i += 1
            rows.append((code, f"{origin} -> {path}"))
        else:
            rows.append((code, path))
    return rows


def _parse_name_status(out: str) -> list[tuple[str, str]]:
    """`STATUS` NUL `path` [NUL `path2` for a rename or a copy] records."""
    fields = [f for f in out.split("\0") if f != ""]
    rows: list[tuple[str, str]] = []
    i = 0
    while i < len(fields):
        code = fields[i]
        i += 1
        if i >= len(fields):
            break
        path = fields[i]
        i += 1
        if code and code[0] in ("R", "C") and i < len(fields):
            rows.append((code, f"{path} -> {fields[i]}"))
            i += 1
        else:
            rows.append((code, path))
    return rows


def enumerate_paths(mode: str, cwd: str = ROOT, rev: str | None = None) -> list[dict]:
    out = _git(mode, cwd, rev)
    rows = _parse_status(out) if mode == "worktree" else _parse_name_status(out)
    return [{"code": c, "path": p} for c, p in rows]


# ── establishment (#19) ──────────────────────────────────────────────────────
def _run(argv: list[str], cwd: str) -> None:
    proc = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode != 0:
        raise SystemExit("changed_paths --establish: setup command failed: "
                         + " ".join(argv) + "\n"
                         + proc.stdout.decode("utf-8", "replace"))


def _write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:      # write-mode only
        fh.write(text)


def establish() -> dict:
    """A throwaway repository, a KNOWN set of modifications, and a clean tree."""
    tmp = tempfile.mkdtemp(prefix="changed_paths_establish_")
    ident = ["-c", "user.name=establishment", "-c", "user.email=establishment@invalid",
             "-c", "commit.gpgsign=false"]
    _run(["git", "init", "-q", tmp], cwd=tempfile.gettempdir())
    for name in ("kept.txt", "modified.txt", "deleted.txt", "renamed_from.txt"):
        _write(os.path.join(tmp, name), f"{name}\n")
    _write(os.path.join(tmp, "sub", "nested.txt"), "nested\n")
    _run(["git", "add", "-A"], cwd=tmp)
    _run(["git"] + ident + ["commit", "-q", "-m", "base"], cwd=tmp)
    base_clean = enumerate_paths("worktree", tmp)

    # the KNOWN set
    _write(os.path.join(tmp, "modified.txt"), "modified.txt changed\n")
    os.remove(os.path.join(tmp, "deleted.txt"))
    os.rename(os.path.join(tmp, "renamed_from.txt"), os.path.join(tmp, "renamed_to.txt"))
    _write(os.path.join(tmp, "added.txt"), "added\n")
    _write(os.path.join(tmp, "untracked.txt"), "untracked\n")
    expected_worktree = {"modified.txt", "deleted.txt", "renamed_from.txt",
                         "renamed_to.txt", "added.txt", "untracked.txt"}
    worktree = enumerate_paths("worktree", tmp)
    seen_worktree = set()
    for r in worktree:
        seen_worktree.update(p.strip() for p in r["path"].split("->"))

    _run(["git", "add", "-A"], cwd=tmp)
    staged = enumerate_paths("staged", tmp)
    seen_staged = set()
    for r in staged:
        seen_staged.update(p.strip() for p in r["path"].split("->"))
    # a rename is reported as one record naming both paths, or as add+delete; both are the
    # same path set, which is why the check is on the SET and not on the record count.
    expected_staged = expected_worktree - {"untracked.txt"} | {"untracked.txt"}

    _run(["git"] + ident + ["commit", "-q", "-m", "the known set"], cwd=tmp)
    head = subprocess.run(["git", "-C", tmp, "rev-parse", "HEAD"],
                          stdout=subprocess.PIPE, text=True).stdout.strip()
    at_commit = enumerate_paths("commit", tmp, head)
    seen_commit = set()
    for r in at_commit:
        seen_commit.update(p.strip() for p in r["path"].split("->"))
    after_clean = enumerate_paths("worktree", tmp)

    # A commit hash is required, and a ref must be refused.
    refused_a_ref = False
    try:
        enumerate_paths("commit", tmp, "HEAD")
    except SystemExit:
        refused_a_ref = True
    refused_an_unsanctioned_mode = False
    try:
        enumerate_paths("show", tmp)
    except SystemExit:
        refused_an_unsanctioned_mode = True

    return {
        "purpose": "Establishment (#19) of tools/audit/changed_paths.py: that it reports a "
                   "KNOWN set of modifications correctly, and reports NOTHING when the tree is "
                   "clean. Both are the conditions the phase-1s dispatch names (§2.2).",
        "the_structural_property": {
            "claim": "The module cannot return file content. It never opens a file for "
                     "reading; every git invocation comes from the frozen ALLOWED table; every "
                     "row of that table is a subcommand that emits a status code and a path "
                     "and nothing else; and only those two fields reach the output.",
            "why_diff_tree_and_not_show": "`git show <blob-sha>` prints the blob and "
                                          "`--name-status` does not suppress it. `diff-tree` "
                                          "walks commits and trees only and errors on a blob, "
                                          "so the content path does not exist rather than "
                                          "being avoided.",
            "refused_a_ref_where_a_hash_is_required": refused_a_ref,
            "refused_an_unsanctioned_enumeration": refused_an_unsanctioned_mode,
        },
        "clean_tree_reports_nothing": {
            "before_the_modifications": {"records": len(base_clean), "rows": base_clean},
            "after_committing_them": {"records": len(after_clean), "rows": after_clean},
            "both_empty": not base_clean and not after_clean,
        },
        "a_known_set_of_modifications": {
            "expected_paths": sorted(expected_worktree),
            "working_tree": {"records": len(worktree), "rows": worktree,
                             "paths_seen": sorted(seen_worktree),
                             "exact": seen_worktree == expected_worktree},
            "staged": {"records": len(staged), "rows": staged,
                       "paths_seen": sorted(seen_staged),
                       "exact": seen_staged == expected_staged},
            "at_the_commit": {"records": len(at_commit), "rows": at_commit,
                              "paths_seen": sorted(seen_commit),
                              "exact": seen_commit == expected_staged},
        },
        "coverage_limits": [
            "It reports what GIT reports: an ignored path is invisible to it, which is why "
            "`.claude/settings.json` appears in no enumeration here.",
            "An untracked DIRECTORY is one record naming the directory, not one record per "
            "file inside it (git's `--untracked-files=normal`). A count of records is "
            "therefore a lower bound on a count of untracked files.",
            "`--commit` on a MERGE commit reports nothing (diff-tree emits no records for a "
            "merge without -m/-c). An empty result on a merge is not 'touched nothing'.",
            "It answers WHICH paths, never WHAT changed in them — reading a changed file stays "
            "the file tools' job, which is the division D-253 draws.",
        ],
        "how_this_artifact_is_kept_fresh": "There is no --check mode, deliberately: reading "
                                           "the artifact back would be a read-mode open and "
                                           "the structural property is worth more. Regenerate "
                                           "with --establish and then run the enumeration — a "
                                           "changed artifact appears in the list.",
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Enumerate changed paths. Reports paths and status codes only.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--staged", action="store_true", help="what is staged for commit")
    g.add_argument("--commit", metavar="SHA", help="what a commit touched (explicit hash)")
    ap.add_argument("--json", metavar="PATH",
                    help="write the enumeration to PATH as a generated artifact (D-431)")
    ap.add_argument("--establish", action="store_true",
                    help="measure the tool against a known set and a clean tree")
    args = ap.parse_args()

    if args.establish:
        art = establish()
        _write(ESTABLISH_OUT, json.dumps(art, indent=2, ensure_ascii=False) + "\n")
        k = art["a_known_set_of_modifications"]
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")
        print(f"  clean tree reports nothing: {art['clean_tree_reports_nothing']['both_empty']}")
        for where in ("working_tree", "staged", "at_the_commit"):
            print(f"  the known set at the {where}: exact={k[where]['exact']} "
                  f"({k[where]['records']} record(s))")
        print("  refuses a ref where a hash is required: "
              f"{art['the_structural_property']['refused_a_ref_where_a_hash_is_required']}")
        print("  refuses an unsanctioned enumeration: "
              f"{art['the_structural_property']['refused_an_unsanctioned_enumeration']}")
        ok = (art["clean_tree_reports_nothing"]["both_empty"]
              and all(k[w]["exact"] for w in ("working_tree", "staged", "at_the_commit")))
        return 0 if ok else 1

    mode = "commit" if args.commit else ("staged" if args.staged else "worktree")
    rows = enumerate_paths(mode, ROOT, args.commit)
    if args.json:
        path = args.json if os.path.isabs(args.json) else os.path.join(ROOT, args.json)
        _write(path, json.dumps({
            "purpose": "A run of tools/audit/changed_paths.py. Generated so a report cites "
                       "this file rather than transcribing the list (D-431).",
            "enumeration": mode,
            "commit": args.commit,
            "records": len(rows),
            "rows": rows,
            "establishment": "tools/audit/changed_paths_establishment.json",
        }, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {args.json}: {len(rows)} record(s)")
    for r in rows:
        print(f"{r['code']}\t{r['path']}")
    print(f"{len(rows)} changed path record(s) [{mode}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
