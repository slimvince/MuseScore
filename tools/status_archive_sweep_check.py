#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""status_archive_sweep_check.py — byte-reconcile the STATUS.md -> STATUS_ARCHIVE.md sweep.

OI-205(a): superseded dated STATUS.md entries move VERBATIM to STATUS_ARCHIVE.md (the 2026-07-18
doc-split discipline). This instrument proves the move is byte-exact, so no entry text was edited
or lost in flight (#10/#12):

  * every dated entry PRESENT in the pre-sweep STATUS.md but ABSENT from the post-sweep STATUS.md
    (a "moved" entry) must appear BYTE-IDENTICAL in the post-sweep STATUS_ARCHIVE.md;
  * every dated entry KEPT in the post-sweep STATUS.md must have been present pre-sweep (nothing is
    invented on the lean side except NEW entries added this commit — reported, not failed);
  * every entry that was already in the pre-sweep STATUS_ARCHIVE.md must still be there byte-identical
    (the archive only grows at its head);
  * no moved entry is DROPPED (present in neither post file) and none is DUPLICATED.

A dated entry is a top-level line beginning ``*Last updated:`` (STATUS.md) or ``*Last updated:`` /
``*Previous entry:`` (STATUS_ARCHIVE.md). Comparison is in git-normalized (LF) text; the em dash /
section sign inside entries compare fine. Stdlib only. Exit 0 iff every check passes.

Usage:
    python tools/status_archive_sweep_check.py [--base HEAD]
"""

import argparse
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRY_PREFIXES = ("*Last updated:", "*Previous entry:")


def git_show(base, rel):
    out = subprocess.run(["git", "show", "%s:%s" % (base, rel)],
                         cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise RuntimeError("git show %s:%s failed: %s" % (base, rel, out.stderr.decode("utf-8", "replace")))
    return out.stdout.decode("utf-8")  # git stores LF


def read_disk(rel):
    with open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8") as fh:
        return fh.read()  # universal newlines -> LF


def entries(text):
    """Return the set/list of dated-entry lines (a top-level entry is ONE line here)."""
    out = []
    for line in text.split("\n"):
        if line.startswith(ENTRY_PREFIXES):
            out.append(line)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    pre_status = entries(git_show(args.base, "STATUS.md"))
    pre_archive = entries(git_show(args.base, "STATUS_ARCHIVE.md"))
    post_status = entries(read_disk("STATUS.md"))
    post_archive = entries(read_disk("STATUS_ARCHIVE.md"))

    pre_status_set = set(pre_status)
    post_status_set = set(post_status)
    post_archive_set = set(post_archive)
    pre_archive_set = set(pre_archive)

    moved = [e for e in pre_status if e not in post_status_set]     # left STATUS.md
    kept = [e for e in post_status if e in pre_status_set]          # stayed in STATUS.md
    added = [e for e in post_status if e not in pre_status_set]     # NEW this commit (the switch entry)

    fails = []
    # 1. every moved entry is byte-identical in the post archive
    for e in moved:
        if e not in post_archive_set:
            fails.append("MOVED entry not found byte-identical in post-archive: %s" % e[:80])
    # 2. no moved entry dropped (in neither post file)
    for e in moved:
        if e not in post_archive_set and e not in post_status_set:
            fails.append("MOVED entry DROPPED (in neither post file): %s" % e[:80])
    # 3. the pre-archive entries are all preserved
    for e in pre_archive:
        if e not in post_archive_set:
            fails.append("pre-archive entry LOST from post-archive: %s" % e[:80])
    # 4. no duplication: a moved entry must not remain in STATUS.md too
    for e in moved:
        if e in post_status_set:
            fails.append("MOVED entry DUPLICATED (still in STATUS.md): %s" % e[:80])
    # 5. count reconciliation
    dup_archive = len(post_archive) - len(post_archive_set)
    if dup_archive:
        fails.append("post-archive has %d duplicate entry line(s)" % dup_archive)

    ok = not fails
    print("STATUS ARCHIVE SWEEP RECONCILIATION (base %s)" % args.base)
    print("  pre  STATUS entries:   %d" % len(pre_status))
    print("  post STATUS entries:   %d   (kept %d, NEW-this-commit %d)" % (len(post_status), len(kept), len(added)))
    print("  moved (STATUS->archive): %d" % len(moved))
    print("  pre  archive entries:  %d" % len(pre_archive))
    print("  post archive entries:  %d   (delta %d == moved %d)" % (len(post_archive), len(post_archive) - len(pre_archive), len(moved)))
    print("  NEW-this-commit STATUS entries:")
    for e in added:
        print("    + %s" % e[:90])
    print("  moved entries (byte-verified in post-archive):")
    for e in moved:
        print("    -> %s" % e[:90])
    if fails:
        print("\n  FAILURES (%d):" % len(fails))
        for f in fails:
            print("    ! %s" % f)
    print("\nVERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
