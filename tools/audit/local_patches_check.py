#!/usr/bin/env python3
"""Are the local patches to MuseScore's own code still present at HEAD?

WHAT THIS IS.  Task 5 of the phase-1q wave
(`cc_instruction_phase1q_reclassification_and_guards.md` §6), on the user's ruling of
2026-08-03 (X5).  `CLAUDE.md`'s "Local patches — do not revert" section carries edits to code
this project does not own, each stated as do-not-revert **against a dependency update**.  Until
now nothing verified they were still there.

WHY THIS ONE MATTERS MORE THAN THE OTHER MECHANISMS IN THIS SET.  A dependency update that
reverts one of these is a **silent** failure: nothing errors, both suites pass, and the patched
behaviour quietly returns to upstream's.  One of the three changes the analysis INPUT on the
zero-signature stems (the MusicXML declared-mode import fix), so a silent revert would move the
measured figures with no diff to point at.  This is the only mechanism in the current set that
guards the SYSTEM rather than the paperwork.

THE PATCH LIST IS DERIVED FROM `CLAUDE.md`, NOT HARD-CODED (#17f applied to the check's own
input).  The section's `###` subsections and their `**File:**` lines are read from the document,
so a fourth patch recorded there is covered without editing this file.  What this file holds is
one thing per patch that cannot be derived from prose: the MARKER — the text that must be
present, or must be absent, in the patched file.  **A recorded patch with no marker is a STOP**,
not a silent pass: the check refuses to report a clean run over a patch it is not testing.

THE RETIREMENT PATH — mandatory, because a check that can never stop failing gets disabled.
When upstream fixes a defect this project patched locally, the patch is retired by adding ONE
line to its `CLAUDE.md` subsection, in this form:

    **★ SUPERSEDED UPSTREAM (YYYY-MM-DD):** <what upstream did>; upstream <commit-or-release>.

The marking must carry an upstream reference — a commit hash of at least seven hex digits, or a
release identifier — and a marking without one is a STOP, so a patch cannot be retired by
assertion.  A superseded patch is reported RETIRED and its marker is not tested.

ESTABLISHMENT (#19).  `--establish` proves the check DETECTS a deliberately absent patch, not
only that it passes on the present ones — a check that only ever passes is not established.  Two
kinds of instance, and the artifact reports them apart:
  * **synthetic** — the real file content, mutated in memory so the patch is absent (a removal
    patch's forbidden text re-inserted; an addition patch's required text deleted), for every
    marker.  The check must then FAIL on that content.
  * **from the record** — where the `CLAUDE.md` subsection names the commit that applied the
    patch, the file as it stood at that commit's PARENT is read (`git show <hash>^:<path>`, a
    read-only git object query by explicit hash) and the check must FAIL on it.  This is a real
    unpatched file rather than a constructed one.  Where no commit is recorded, the artifact
    says so rather than leaving the absence unexplained.

Run:
    python tools/audit/local_patches_check.py                 # check HEAD
    python tools/audit/local_patches_check.py --establish [--check]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CLAUDE_MD = os.path.join(ROOT, "CLAUDE.md")
ESTABLISH_OUT = os.path.join(HERE, "local_patches_establishment.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

SECTION_HEADING = "## Local patches — do not revert"
SUPERSEDED = re.compile(r"\*\*★?\s*SUPERSEDED UPSTREAM\s*\(([^)]*)\)\s*:?\*\*(.*)", re.I)
UPSTREAM_REF = re.compile(r"\b[0-9a-f]{7,40}\b|\bv?\d+\.\d+(?:\.\d+)?\b|\brelease\s+\S+", re.I)
FILE_FIELD = re.compile(r"^\*\*File:\*\*\s*`([^`]+)`")
COMMIT_FIELD = re.compile(r"^\*\*Commit:\*\*\s*`([0-9a-f]{7,40})`")


# ── AUTHORED: one marker set per patched file ───────────────────────────────
# `kind` is what the patch DID: "removed" means the text must now be ABSENT, "added" means it
# must be PRESENT.  `pattern` is a regular expression.  `why` says what the marker is testing,
# in the terms `CLAUDE.md`'s own subsection uses.
MARKERS: dict[str, list[dict]] = {
    "muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp": [
        {"kind": "removed", "pattern": r"ptMinTrackSize\s*\.\s*[xy]\s*=",
         "why": "the two assignments the patch removed, which set the minimum window size to "
                "the full monitor work area inside the WM_GETMINMAXINFO handler. "
                "`CLAUDE.md`: \"Do not restore the `ptMinTrackSize` lines.\""},
        {"kind": "added", "pattern": r"Do NOT set ptMinTrackSize here",
         "why": "the guard comment the patch left in place of the removed lines. It is this "
                "project's own text, so its presence is positive evidence of the patch rather "
                "than of upstream's shape."},
    ],
    "src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp": [
        {"kind": "added", "pattern": r"oldKeySig\.mode\(\)\s*!=\s*key\.mode\(\)",
         "why": "the mode term the patch adds to the KeySig-dedup guard, without which a "
                "0-fifths key signature carrying an explicit <mode> is dropped."},
        {"kind": "added", "pattern": r"const\s+KeySigEvent\s+oldKeySig",
         "why": "the prevailing KeySigEvent the patch fetches so the guard can read the mode at "
                "all; upstream reads only the Key fifths."},
    ],
    "src/engraving/dom/chordlist.cpp": [
        {"kind": "removed", "pattern": r'tok1\s*=\s*u"sus"',
         "why": "the redundant case-sensitive assignment the patch removed — the underlying "
                "cause of the \"sussus\" double-rendering defect. The correct lowercase path "
                "`tok1L = u\"sus\"` is upstream's and stays."},
    ],
}


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def patches() -> list[dict]:
    """The patch list, derived from `CLAUDE.md`'s own section."""
    lines = read(CLAUDE_MD).splitlines()
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == SECTION_HEADING)
    except StopIteration:
        raise SystemExit(f"CLAUDE.md no longer carries the heading {SECTION_HEADING!r}; this "
                         "check derives its patch list from that section and will not guess")
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))

    out: list[dict] = []
    cur: dict | None = None
    for i in range(start + 1, end):
        ln = lines[i]
        if ln.startswith("### "):
            cur = {"title": ln[4:].strip(), "heading_line": i + 1, "file": None,
                   "commit": None, "superseded": None, "body": []}
            out.append(cur)
            continue
        if cur is None:
            continue
        cur["body"].append(ln)
        m = FILE_FIELD.match(ln)
        if m and cur["file"] is None:
            cur["file"] = m.group(1)
        m = COMMIT_FIELD.match(ln)
        if m and cur["commit"] is None:
            cur["commit"] = m.group(1)
        m = SUPERSEDED.search(ln)
        if m and cur["superseded"] is None:
            cur["superseded"] = {"date": m.group(1).strip(), "text": m.group(2).strip(),
                                 "line": i + 1}
    for p in out:
        p.pop("body")
    return out


def marker_findings(pattern: str, kind: str, content: str) -> str | None:
    """None when the marker is satisfied; otherwise what is wrong."""
    hit = re.search(pattern, content)
    if kind == "removed" and hit:
        return f"the removed text is BACK: /{pattern}/ matches {hit.group(0)!r}"
    if kind == "added" and not hit:
        return f"the added text is GONE: /{pattern}/ matches nothing"
    return None


def check_patch(p: dict, content: str | None) -> dict:
    """One patch's verdict over `content` (None = read the working tree)."""
    rec = {"title": p["title"], "file": p["file"], "commit": p["commit"],
           "superseded": p["superseded"], "markers": [], "verdict": None}

    if p["file"] is None:
        rec["verdict"] = "STOP"
        rec["problem"] = ("the subsection carries no `**File:**` line, so the check cannot tell "
                          "which file it protects")
        return rec

    if p["superseded"]:
        if not UPSTREAM_REF.search(p["superseded"]["text"]):
            rec["verdict"] = "STOP"
            rec["problem"] = ("marked SUPERSEDED UPSTREAM with no upstream commit or release "
                              "named; a patch may not be retired by assertion")
            return rec
        rec["verdict"] = "RETIRED"
        return rec

    marks = MARKERS.get(p["file"])
    if not marks:
        rec["verdict"] = "STOP"
        rec["problem"] = (f"`CLAUDE.md` records a patch to {p['file']} and this check has no "
                          "presence marker for it. Add one to MARKERS — a recorded patch that is "
                          "not tested must not read as a clean run.")
        return rec

    if content is None:
        path = os.path.join(ROOT, p["file"])
        if not os.path.exists(path):
            rec["verdict"] = "FAIL"
            rec["markers"] = [{"why": "the patched file itself is missing", "problem": path}]
            return rec
        content = read(path)

    bad = False
    for m in marks:
        problem = marker_findings(m["pattern"], m["kind"], content)
        rec["markers"].append({"kind": m["kind"], "pattern": m["pattern"], "why": m["why"],
                               "ok": problem is None, "problem": problem})
        bad = bad or problem is not None
    rec["verdict"] = "FAIL" if bad else "PRESENT"
    return rec


def run_check() -> tuple[list[dict], int]:
    recs = [check_patch(p, None) for p in patches()]
    bad = sum(1 for r in recs if r["verdict"] in ("FAIL", "STOP"))
    return recs, bad


# ── establishment (#19) ─────────────────────────────────────────────────────
def mutate(content: str, marker: dict) -> tuple[str, str]:
    """The same file with the patch UNDONE, and how it was undone."""
    if marker["kind"] == "added":
        hit = re.search(marker["pattern"], content)
        if not hit:
            raise SystemExit("cannot build the unpatched form: the added text is already absent")
        return content[:hit.start()] + content[hit.end():], "deleted the text the patch added"
    # a removal patch: put the forbidden text back, in a form the pattern matches
    reinstated = {
        r"ptMinTrackSize\s*\.\s*[xy]\s*=": "    minMaxInfo->ptMinTrackSize.x = 1;\n",
        r'tok1\s*=\s*u"sus"': '            tok1 = u"sus";\n',
    }.get(marker["pattern"])
    if reinstated is None:
        raise SystemExit(f"no unpatched specimen for the removal marker {marker['pattern']!r}")
    return content + "\n" + reinstated, "re-inserted the text the patch removed"


def git_show(hashish: str, path: str) -> tuple[str | None, str]:
    try:
        out = subprocess.run(["git", "show", f"{hashish}:{path}"], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError as exc:
        return None, f"git is not runnable here ({exc})"
    if out.returncode != 0:
        return None, (out.stderr or "").strip()[:200]
    return out.stdout, ""


def establish() -> dict:
    ps = patches()
    present_rows = [check_patch(p, None) for p in ps]

    synthetic: list[dict] = []
    for p in ps:
        for m in MARKERS.get(p["file"] or "", []):
            content = read(os.path.join(ROOT, p["file"]))
            unpatched, how = mutate(content, m)
            rec = check_patch(p, unpatched)
            synthetic.append({
                "file": p["file"], "marker": m["pattern"], "kind": m["kind"],
                "how_the_patch_was_undone": how,
                "verdict_on_the_unpatched_content": rec["verdict"],
                "detected": rec["verdict"] == "FAIL",
            })

    from_record: list[dict] = []
    for p in ps:
        if not p["commit"]:
            from_record.append({
                "file": p["file"], "available": False,
                "why_not": "the `CLAUDE.md` subsection records no `**Commit:**` field, so the "
                           "pre-patch object cannot be named by explicit hash. The synthetic "
                           "instance above is this patch's whole establishment."})
            continue
        content, err = git_show(p["commit"] + "^", p["file"])
        if content is None:
            from_record.append({"file": p["file"], "available": False,
                                "commit": p["commit"], "why_not": err})
            continue
        rec = check_patch(p, content)
        from_record.append({
            "file": p["file"], "available": True, "commit": p["commit"],
            "object_read": f"{p['commit']}^:{p['file']}",
            "verdict_on_the_real_unpatched_file": rec["verdict"],
            "detected": rec["verdict"] == "FAIL",
        })

    det = [r for r in synthetic if r["detected"]]
    rec_det = [r for r in from_record if r.get("detected")]
    rec_av = [r for r in from_record if r.get("available")]
    return {
        "purpose": "Establishment (#19) of tools/audit/local_patches_check.py: that it DETECTS a "
                   "deliberately absent patch, not only that it passes on the present ones. A "
                   "check that only ever passes is not established.",
        "patch_list_source": "derived from CLAUDE.md's 'Local patches — do not revert' section; "
                             "the subsections and their `**File:**` lines are read from the "
                             "document, never hard-coded here.",
        "at_head": {
            "patches": len(present_rows),
            "present": sum(1 for r in present_rows if r["verdict"] == "PRESENT"),
            "retired": sum(1 for r in present_rows if r["verdict"] == "RETIRED"),
            "failing": sum(1 for r in present_rows if r["verdict"] == "FAIL"),
            "stopped": sum(1 for r in present_rows if r["verdict"] == "STOP"),
            "rows": present_rows,
        },
        "detection_synthetic": {
            "instances": len(synthetic), "detected": len(det),
            "detection_rate": round(len(det) / len(synthetic), 3) if synthetic else None,
            "rows": synthetic,
        },
        "detection_from_the_record": {
            "instances_available": len(rec_av), "detected": len(rec_det),
            "rows": from_record,
        },
        "what_this_does_not_measure":
            "A false-positive rate. There is no population of legitimate edits that could trip "
            "this check: a marker fires only when the patched text itself moves, which is the "
            "event it exists for. Stating that rather than reporting a zero measured over "
            "nothing.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--establish", action="store_true",
                    help="measure the check against deliberately unpatched content")
    ap.add_argument("--check", action="store_true",
                    help="with --establish: regenerate into memory and diff the artifact")
    args = ap.parse_args()

    if args.establish:
        art = establish()
        text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            have = read(ESTABLISH_OUT) if os.path.exists(ESTABLISH_OUT) else ""
            if have != text:
                print("STALE: local_patches_establishment.json does not re-derive")
                return 1
            print("the local-patches establishment artifact re-derives")
            return 0
        open(ESTABLISH_OUT, "w", encoding="utf-8", newline="").write(text)
        s, r = art["detection_synthetic"], art["detection_from_the_record"]
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")
        print(f"  synthetic unpatched forms detected: {s['detected']}/{s['instances']}")
        for row in s["rows"]:
            if not row["detected"]:
                print(f"    MISSED: {row['file']} {row['marker']}")
        print(f"  real pre-patch objects detected:    {r['detected']}/{r['instances_available']}")
        for row in r["rows"]:
            if not row.get("available"):
                print(f"    unavailable: {row['file']} — {row['why_not'][:80]}")
        return 0

    recs, bad = run_check()
    for r in recs:
        print(f"  [{r['verdict']}] {r['file']}  — {r['title']}")
        if r["verdict"] == "STOP":
            print(f"      {r['problem']}")
        for m in r["markers"]:
            if not m.get("ok"):
                print(f"      {m['problem']}")
                print(f"      marker: {m['why']}")
    print(f"{len(recs)} recorded patch(es); {bad} failing or stopped")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
