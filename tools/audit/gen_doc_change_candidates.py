#!/usr/bin/env python3
"""THE CANDIDATE PASS -- every documentation change of the restructuring period, enumerated whole
and classified per hunk as PURE RESTRUCTURING or CONTENT CHANGE.

Dispatch: `cc_instruction_evidence_candidate_pass.md` (Cowork, 2026-08-13, on the user's rulings of
that date).  This tool is Task 1 (the enumeration) and Task 2 (the classification) in one artifact,
because the dispatch's ruling 5 makes the sizing and the candidate list the same act: the size
cannot be known without classifying.

WHAT IS AT STAKE, and it is why every rule below leans one way.  A change that should have been
flagged and is not will never be looked at again.  Over-flagging costs review time; under-flagging
costs the objective.  They are not comparable.  So: THE DEFAULT ON DOUBT IS FLAG, and this tool
emits PURE only where a MECHANICAL recognizer fires -- never where a judgment would be needed.

WHAT IS DERIVED AND WHAT IS AUTHORED, stated because the difference is the whole value:

  DERIVED  -- the commit population, from `git rev-list`; every file change and its status,
              from `git show --name-status -M -C`; every hunk and its changed lines, from
              `git show -U0 -M -C`; every cross-file move, from line-multiset matching inside a
              commit; every count in the artifact.
  AUTHORED -- the period's start (a bound taken at the record, with the record citation carried
              beside it and the three inner bounds published as strata); the recognizer set below
              and the OK-list clause each cites; the document-role map; the look-alike signal
              vocabulary.  Each is marked AUTHORED in the artifact and never presented as measured.

THE RECOGNIZERS.  A PURE verdict cites the clause it used, by name (dispatch mechanism 3).  Only
these four fire, and each is a mechanical identity, not an argument:

  RULE-IDENTITY-WHITESPACE  the classification rule's own first limb -- "Content identical but
                            rearranged is PURE".  Fires when the multiset of the hunk's removed
                            lines equals the multiset of its added lines after whitespace
                            normalization.  Covers whitespace and line-ending changes and
                            reordering inside one hunk.
  OK-MOVE-WHOLE             OK list: "Moving content to its owning home, carried whole" /
                            "Splitting or merging documents with content carried whole".  Fires
                            when every non-trivial line the hunk removes reappears, in the SAME
                            COMMIT, as a line added elsewhere, and every non-trivial line it adds
                            was removed elsewhere -- with multiplicity.  A hunk whose counterpart
                            sits in a PRESERVATION context (a "former wording preserved" block) is
                            NOT called a move: the words survive as a quotation while the rule they
                            stated may not, and this tool cannot tell those apart.
  OK-LOCATOR-DELETION       Worked example: "Deleting ~L#### code locators, which D-307 forbids
                            citing by in the first place".  Fires when removed and added lines are
                            equal after deleting `~L<digits>` tokens and at least one such token
                            was removed.
  OK-FOOTER-DATE            Worked example: "A footer date re-stamp".  Fires only when removed and
                            added lines are equal after replacing ISO dates by a placeholder AND
                            every changed line carries a stamp word.  Deliberately narrow: a date
                            inside a ruling sentence is a datum, not a stamp.

THE STRETCH STOP (dispatch mechanism 4) is encoded as the absence of any fifth recognizer.  There
is no clause in this tool that reasons a change into the OK class.

THE FIVE MECHANISMS, and where each lives here:
  1. per hunk, never per commit or per file  -- the unit of every record below is one -U0 hunk.
  2. default on doubt is FLAG                -- `classify()` returns FLAG unless a recognizer fires.
  3. every PURE cites its clause by name     -- `verdict.clause`, and a PURE with no clause STOPS.
  4. the stretch stop                        -- no recognizer admits an argument.
  5. self-classification is declared         -- `authoring_side` per hunk from the commit subject,
                                                and the population-level declaration in the header.

THE STOPS, so this cannot silently stop being an enumeration:
  1. Every enumerated hunk carries a verdict; a hunk with none STOPS the tool (assumption A4).
  2. A PURE verdict with no clause STOPS the tool.
  3. Every boundary commit must be an ancestor of the range end; one that is not STOPS the tool.
  4. Rename detection must have found at least one rename, or the tool records that none exists in
     the population -- it may not simply report zero without saying which (assumption A2).
  5. The reconciliation must balance: file changes enumerated = hunks-enumerated files + files
     explicitly named un-enumerated.  It STOPS otherwise.

WHAT THIS DOES NOT DO.  It restores nothing, reverts nothing, corrects nothing and resolves
nothing.  PURE and CONTENT CHANGE describe what an edit did; neither is a verdict on whether the
edit should have happened.  It makes NO comparison against the code in either direction.

Usage:
  python tools/audit/gen_doc_change_candidates.py            # write the artifacts
  python tools/audit/gen_doc_change_candidates.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_MAIN = ROOT / "tools" / "audit" / "doc_change_candidates.json"
OUT_HUNKS = ROOT / "tools" / "audit" / "doc_change_candidates_hunks.jsonl"

# ── THE PERIOD, AND THE FOUR BOUNDS TAKEN AT THE RECORD ──────────────────────────────────────────
#
# AUTHORED.  The record names no start for "the restructuring period".  What it does name is four
# documentation-restructuring acts, each citable.  The dispatch's rule for exactly this case is
# "go back further, not less -- err early.  Report the bound and what would settle it."  So the
# POPULATION opens at the EARLIEST of the four, and the other three are published as strata, so a
# narrower reading can be taken by the user without this pass being re-run.
#
# The commit named as the start is EXCLUSIVE: the population is its descendants.  It is included as
# a stratum boundary because the act itself is inside the period it opens.
PERIOD_START = "9306dc5072153dec647b227725f626f8741f8c1b"

BOUNDS = [
    {
        "id": "S1-open-items-register",
        "commit": "9306dc5072153dec647b227725f626f8741f8c1b",
        "date": "2026-07-11",
        "act": "The open-items register is created: 91 open items consolidated from 12 scattered "
               "tracking surfaces into one home.",
        "established_at": "CLAUDE.md, the open-items register section -- \"created after a "
                          "full-repo sweep found 91 open items scattered across 12 surfaces with "
                          "11 status contradictions\".",
        "why_this_is_a_restructuring_act": "It moves documentation content out of twelve surfaces "
                                           "into one, which is the shape of every later homing "
                                           "act.  It is the earliest act of that shape the record "
                                           "names.",
    },
    {
        "id": "S2-status-handoff-doc-split",
        "commit": "51d4f6dcf34121a2598750c41b808c2f895ae674",
        "date": "2026-07-18",
        "act": "STATUS.md and cowork_handoff.md are split into lean active must-reads plus "
               "verbatim archives.",
        "established_at": "CLAUDE.md, build-and-test reads -- \"STATUS_ARCHIVE.md and "
                          "cowork_handoff_archive.md hold the superseded historical entries moved "
                          "out by the doc split (cc_instruction_doc_split.md)\".",
        "why_this_is_a_restructuring_act": "Content is moved between documents wholesale.",
    },
    {
        "id": "S3-open-items-register-split",
        "commit": "1e32b5e92e2594d3a8d1752fcea051dab16f60a7",
        "date": "2026-07-27",
        "act": "OPEN_ITEMS.md is split into a lean INDEX plus one detail file per item.",
        "established_at": "CLAUDE.md, the open-items register section -- \"split into index + "
                          "per-item detail files on 2026-07-26, user-ratified option 1\".",
        "why_this_is_a_restructuring_act": "One document becomes many, content carried across.",
    },
    {
        "id": "S4-D231-phase-1",
        "commit": "b006dc15b5f696f2fc86ad72b97fae58d2119cd7",
        "date": "2026-08-02",
        "act": "D-231 ratified: specification completion, then issue-exhaustion, then one fix "
               "plan.  Phase 1 -- the specifications are made COMPLETE AND TRUE -- opens.",
        "established_at": "CLAUDE.md, Conventions -- \"ISSUE-EXHAUSTION AND SPECIFICATION "
                          "COMPLETION BEFORE ANY FIX DESIGN (user-directed, 2026-08-02)\", whose "
                          "phase 1 carries both the homing acts and the doc-sync truth-sync.",
        "why_this_is_a_restructuring_act": "It is the NARROW reading of the period: the program "
                                           "under which the specifications were rewritten, and "
                                           "the one whose truth-sync half is the code-versus-"
                                           "documentation comparison ruling 1 places in the "
                                           "audit's hands rather than here.",
    },
]

# ── THE ENUMERATED SURFACE TYPES ─────────────────────────────────────────────────────────────────
#
# AUTHORED.  Which paths have their HUNKS enumerated.  Everything else is still enumerated at
# FILE-CHANGE level and named un-enumerated, never dropped (dispatch section 0d).
HUNK_GLOBS = ["*.md", "*.py", "*.cpp", "*.h", "*.hpp", "*.sh", "*.bat", "*.cmake",
              "*CMakeLists.txt", "tools/audit/decisions/backbone_decisions.json"]

# AUTHORED.  Build scripts are source, not generated data, however their file happens to be named.
# Without this their comments would fall in the un-enumerated class on the strength of a `.txt`
# suffix, which is a naming accident and not a statement about what the file is.
SOURCE_BASENAMES = {"CMakeLists.txt"}

# AUTHORED, established at CLAUDE.md decisions-register rule (d): "change
# tools/audit/decisions/backbone_decisions.json and regenerate ... never hand-edit the rendered
# files".  So this .json is an AUTHORED surface and its hunks are enumerated, while the .md files
# rendered from it are generated.
AUTHORED_DATA = {"tools/audit/decisions/backbone_decisions.json"}

PROSE_EXT = {".md"}
SOURCE_EXT = {".py", ".cpp", ".h", ".hpp", ".sh", ".bat", ".cmake"}
GENERATED_DATA_EXT = {".json", ".csv", ".txt", ".tsv", ".log", ".jsonl"}
BINARY_EXT = {".mscz", ".mscx", ".musicxml", ".xml", ".png", ".jpg", ".pdf", ".gz", ".zip"}

COMMENT_PREFIX = {".py": ("#",), ".sh": ("#",), ".cmake": ("#",), ".txt": ("#",),
                  ".bat": ("REM", "::", "@REM"),
                  ".cpp": ("//", "/*", "*", "*/"), ".h": ("//", "/*", "*", "*/"),
                  ".hpp": ("//", "/*", "*", "*/")}

# ── DOCUMENT ROLE (AUTHORED, reported and NOT used to exclude anything -- ruling 4) ──────────────
def document_role(path: str) -> str:
    p = path.replace("\\", "/")
    base = p.rsplit("/", 1)[-1]
    if base in ("CLAUDE.md", "ARCHITECTURE.md"):
        return "governing"
    if base in ("OPEN_ITEMS.md", "DECISIONS.md"):
        return "register-index"
    if p.startswith("open_items/") or p.startswith("decisions/"):
        return "register-detail"
    if p.startswith("docs/"):
        return "specification-or-docs"
    if p.startswith("ratification_surfaces/"):
        return "ratification-surface"
    if base in ("STATUS.md", "STATUS_ARCHIVE.md", "BUILD_AND_TEST.md"):
        return "status-or-procedure"
    if base.startswith("cc_instruction_"):
        return "dispatch"
    if base.startswith("cc_"):
        return "cc-report"
    if base.startswith("cowork_"):
        return "cowork-planning-or-ruling"
    if p.startswith("src/"):
        return "source-comment"
    if p.startswith("tools/"):
        return "tool-or-artifact"
    return "other"


def surface_class(path: str) -> str:
    p = path.replace("\\", "/")
    if p in AUTHORED_DATA:
        return "authored-data"
    if p.rsplit("/", 1)[-1] in SOURCE_BASENAMES:
        return "source"
    ext = ("." + p.rsplit(".", 1)[-1].lower()) if "." in p.rsplit("/", 1)[-1] else ""
    if ext in PROSE_EXT:
        return "prose"
    if ext in SOURCE_EXT:
        return "source"
    if ext in GENERATED_DATA_EXT:
        return "generated-or-data"
    if ext in BINARY_EXT:
        return "binary-or-score"
    return "other"


# ── LINE NORMALIZATION AND THE RECOGNIZERS ───────────────────────────────────────────────────────
_WS = re.compile(r"\s+")
_PUNCT_ONLY = re.compile(r"^[-=*#>|_`~\s.+()\[\]{},:;'\"!?/\\]*$")
_LOCATOR = re.compile(r"~L\d+")
_ISO_DATE = re.compile(r"\b20\d\d-\d\d-\d\d\b")
_STAMP_WORD = re.compile(
    r"(regenerated|generated at|generated on|generated by|last updated|as of|re-?stamp|stamped|"
    r"footer)", re.I)

# AUTHORED.  Signals reported beside a FLAG so the user can triage the candidate list without this
# tool deciding anything.  A signal is never a verdict and never turns a FLAG into a PURE.
LOOK_ALIKE = [
    ("clarify-a-rule", re.compile(r"\bclarif", re.I)),
    ("removing-redundancy", re.compile(r"\b(redundan|duplicat|collaps)", re.I)),
    ("caveat-hedge-or-not-claimed", re.compile(r"(NOT claimed|caveat|hedge|\bexcept\b|\bunless\b)")),
    ("example-updated-to-behaviour", re.compile(r"(\be\.g\.|\bexample\b|\bfor instance\b)", re.I)),
    ("banner-or-status", re.compile(r"(STATUS:|SUPERSEDED|SHELVED|RATIFIED|DRAFT|WITHDRAWN|"
                                    r"HISTORICAL|LEGACY)")),
    ("rule-force-word", re.compile(r"\b(MUST|SHALL|SHOULD|MAY|NEVER|ALWAYS|FORBIDDEN|"
                                   r"must|shall|should not)\b")),
    ("measured-value-or-provenance", re.compile(r"(measured|provenance|user-ratified|user-ruled|"
                                                 r"\bratified\b)", re.I)),
    ("preserved-former-wording", re.compile(r"(former wording|preserved in place|preserved "
                                            r"verbatim|#12)", re.I)),
]
_PRESERVATION = re.compile(r"(former wording|formerly|preserved in place|preserved verbatim|"
                           r"superseded|historical|retained for provenance)", re.I)


def norm(s: str) -> str:
    return _WS.sub(" ", s).strip()


def trivial(s: str) -> bool:
    t = norm(s)
    return len(t) < 4 or _PUNCT_ONLY.match(t) is not None


def ms(lines) -> Counter:
    return Counter(norm(x) for x in lines)


# ── GIT ──────────────────────────────────────────────────────────────────────────────────────────
def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding="utf-8", errors="replace").stdout


def git_ok(*args: str) -> bool:
    return subprocess.run(["git", "-C", str(ROOT), *args], stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL).returncode == 0


def unquote(p: str) -> str:
    if p.startswith('"') and p.endswith('"'):
        return p[1:-1].encode("latin-1", "backslashreplace").decode("unicode_escape")
    return p


# ── DIFF PARSING ─────────────────────────────────────────────────────────────────────────────────
_HUNK_HDR = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def parse_hunks(diff_text: str):
    """Yield (path, old_path_or_None, hunk_header, removed_lines, added_lines) per -U0 hunk."""
    path = None
    old_path = None
    in_hunk = False
    hdr = None
    rem: list[str] = []
    add: list[str] = []
    pending_old = None
    pending_new = None

    def flush():
        nonlocal in_hunk, hdr, rem, add
        if in_hunk and hdr is not None and path is not None:
            yield_val = (path, old_path, hdr, rem, add)
            in_hunk, hdr, rem, add = False, None, [], []
            return yield_val
        in_hunk, hdr, rem, add = False, None, [], []
        return None

    for line in diff_text.split("\n"):
        if line.startswith("diff --git "):
            f = flush()
            if f:
                yield f
            path = None
            old_path = None
            pending_old = None
            pending_new = None
            continue
        if line.startswith("rename from "):
            pending_old = unquote(line[len("rename from "):])
            continue
        if line.startswith("copy from "):
            pending_old = unquote(line[len("copy from "):])
            continue
        if line.startswith("rename to ") or line.startswith("copy to "):
            pending_new = unquote(line.split(" to ", 1)[1])
            continue
        if line.startswith("--- "):
            t = line[4:]
            if t != "/dev/null":
                pending_old = unquote(t[2:]) if t.startswith("a/") else unquote(t)
            continue
        if line.startswith("+++ "):
            t = line[4:]
            if t == "/dev/null":
                path = pending_old
                old_path = None
            else:
                path = unquote(t[2:]) if t.startswith("b/") else unquote(t)
                old_path = pending_old if pending_old and pending_old != path else None
            continue
        m = _HUNK_HDR.match(line)
        if m:
            f = flush()
            if f:
                yield f
            in_hunk = True
            hdr = line.split("@@")[1].strip() if "@@" in line else line
            rem, add = [], []
            continue
        if in_hunk:
            if line.startswith("-"):
                rem.append(line[1:])
            elif line.startswith("+"):
                add.append(line[1:])
            elif line.startswith("\\"):
                continue
    f = flush()
    if f:
        yield f


# ── CLASSIFICATION ───────────────────────────────────────────────────────────────────────────────
def comment_kind(path: str, rem, add) -> str:
    ext = ("." + path.rsplit(".", 1)[-1].lower()) if "." in path.rsplit("/", 1)[-1] else ""
    prefixes = COMMENT_PREFIX.get(ext)
    if not prefixes:
        return "not-source"
    lines = [x for x in list(rem) + list(add) if x.strip()]
    if not lines:
        return "blank-only"
    is_c = [x.lstrip().startswith(prefixes) for x in lines]
    if all(is_c):
        return "comment-only"
    if any(is_c):
        return "mixed-comment-and-code"
    return "code-only"


def match_vector(rem, add, commit_added: Counter, commit_removed: Counter):
    """How much of this hunk's changed content is carried elsewhere in the SAME commit.

    Reported on every hunk, flagged or not, because it is what turns a flag into a size: a
    500-line hunk whose 498 lines are carried and whose 2 are new is a two-line evidence
    question wearing a 500-line coat.  It decides nothing -- `classify` alone does that.
    Returns [unmatched_removed, unmatched_added, nontrivial_removed, nontrivial_added].
    """
    nt_rem = Counter(norm(x) for x in rem if not trivial(x))
    nt_add = Counter(norm(x) for x in add if not trivial(x))
    ur = sum(max(0, n - commit_added.get(line, 0)) for line, n in nt_rem.items())
    ua = sum(max(0, n - commit_removed.get(line, 0)) for line, n in nt_add.items())
    return [ur, ua, sum(nt_rem.values()), sum(nt_add.values())]


def classify(rem, add, commit_added: Counter, commit_removed: Counter,
             preservation_partner: bool, file_status: str):
    """Return (verdict, clause_or_reason).  FLAG unless a mechanical recognizer fires."""
    nrem, nadd = ms(rem), ms(add)

    # RULE-IDENTITY-WHITESPACE -- the classification rule's own first limb.
    if nrem == nadd and (rem or add):
        return "PURE", "RULE-IDENTITY-WHITESPACE"

    # OK-LOCATOR-DELETION -- the worked example.
    if _LOCATOR.search("\n".join(rem)):
        srem = Counter(norm(_LOCATOR.sub("", x)) for x in rem)
        sadd = Counter(norm(_LOCATOR.sub("", x)) for x in add)
        if srem == sadd:
            return "PURE", "OK-LOCATOR-DELETION"

    # OK-FOOTER-DATE -- the worked example, deliberately narrow.
    both = list(rem) + list(add)
    if both and _ISO_DATE.search("\n".join(both)) and all(_STAMP_WORD.search(x) for x in both
                                                          if x.strip()):
        drem = Counter(norm(_ISO_DATE.sub("<date>", x)) for x in rem)
        dadd = Counter(norm(_ISO_DATE.sub("<date>", x)) for x in add)
        if drem == dadd:
            return "PURE", "OK-FOOTER-DATE"

    # OK-MOVE-WHOLE -- content carried whole, elsewhere in the same commit.
    nt_rem = [x for x in rem if not trivial(x)]
    nt_add = [x for x in add if not trivial(x)]
    if (nt_rem or nt_add) and not preservation_partner:
        ok = True
        for line, n in Counter(norm(x) for x in nt_rem).items():
            if commit_added.get(line, 0) < n:
                ok = False
                break
        if ok:
            for line, n in Counter(norm(x) for x in nt_add).items():
                if commit_removed.get(line, 0) < n:
                    ok = False
                    break
        if ok:
            return "PURE", "OK-MOVE-WHOLE"

    if not rem:
        shape = "new-file-content" if file_status.startswith("A") else "addition-only"
    elif not add:
        shape = "deletion-only"
    else:
        shape = "modification"
    return "FLAG", shape


_DIGITS = re.compile(r"\d+")
_ANCHOR_FIELD = re.compile(r"(\"(home|anchor|delegation|home_section|source)\"\s*:|\*\*Home\.\*\*|"
                           r"§|\.md:\d|\.cpp:\d|\.h:\d|\.py:\d)")


def look_alike_signals(rem, add) -> list:
    blob = "\n".join(list(rem) + list(add))
    out = [name for name, rx in LOOK_ALIKE if rx.search(blob)]
    # Two FACTUAL shape signals, reported and never decided.  The larger of them turned out to be
    # the dominant shape in the flagged set, which is why it is measured rather than left implicit.
    if rem and add:
        dr = Counter(norm(_DIGITS.sub("#", x)) for x in rem)
        da = Counter(norm(_DIGITS.sub("#", x)) for x in add)
        if dr == da:
            out.append("differs-only-in-digits")
            if _ANCHOR_FIELD.search(blob):
                out.append("differs-only-in-an-anchor-or-line-coordinate")
    return out


def authoring_side(subject: str) -> str:
    s = subject.lower()
    if "(cowork)" in s or s.startswith("docs(cowork"):
        return "cowork-authored, CC-committed"
    if "(cc)" in s or s.startswith("docs(cc"):
        return "cc-authored"
    return "unmarked-in-the-commit-subject"


# ── BUILD ────────────────────────────────────────────────────────────────────────────────────────
def build(end_ref: str = "HEAD"):
    end = git("rev-parse", end_ref).strip()

    for b in BOUNDS:
        if not git_ok("merge-base", "--is-ancestor", b["commit"], end):
            raise SystemExit(f"STOP: boundary commit {b['id']} ({b['commit'][:10]}) is not an "
                             f"ancestor of the range end {end[:10]}.")

    meta_raw = git("log", "--reverse", "--no-merges", "--format=%H\x1f%an\x1f%aI\x1f%s",
                   f"{PERIOD_START}..{end}")
    commits = []
    for line in meta_raw.split("\n"):
        if not line.strip():
            continue
        sha, an, ad, subj = line.split("\x1f", 3)
        commits.append({"sha": sha, "author": an, "date": ad, "subject": subj})

    # Stratum assignment: a commit belongs to the LAST boundary that is its ancestor-or-self.
    order = {c["sha"]: i for i, c in enumerate(commits)}
    bound_pos = []
    for b in BOUNDS:
        bound_pos.append((b["id"], order.get(b["commit"], -1)))
    for c in commits:
        i = order[c["sha"]]
        stratum = BOUNDS[0]["id"]
        for bid, pos in bound_pos:
            if pos >= 0 and i >= pos:
                stratum = bid
        c["stratum"] = stratum

    files_index: dict[str, int] = {}

    def fidx(p: str) -> int:
        if p not in files_index:
            files_index[p] = len(files_index)
        return files_index[p]

    hunks = []
    file_changes = []
    renames = []
    move_pairs = Counter()

    for ci, c in enumerate(commits):
        sha = c["sha"]

        # --- every file change in the commit, with its status (rename/copy detection on) ---
        raw = git("show", "--format=", "--name-status", "-M", "-C", "-z", sha)
        toks = [t for t in raw.split("\0") if t != ""]
        k = 0
        commit_files = []
        while k < len(toks):
            st = toks[k]
            k += 1
            if st[0] in ("R", "C") and k + 1 < len(toks):
                old, new = toks[k], toks[k + 1]
                k += 2
                commit_files.append({"status": st, "path": new, "old_path": old})
                renames.append({"commit": sha, "status": st, "from": old, "to": new})
            elif k < len(toks):
                p = toks[k]
                k += 1
                commit_files.append({"status": st, "path": p, "old_path": None})
            else:
                break

        status_of = {f["path"]: f["status"] for f in commit_files}
        for f in commit_files:
            cls = surface_class(f["path"])
            hunks_enumerated = any_glob_match(f["path"])
            file_changes.append({
                "c": ci, "f": fidx(f["path"]),
                "of": fidx(f["old_path"]) if f["old_path"] else None,
                "st": f["status"], "cls": cls, "role": document_role(f["path"]),
                "he": hunks_enumerated,
            })

        # --- hunks, for the enumerated surface types only ---
        dt = git("show", "--format=", "--no-color", "--no-textconv", "-U0", "-M", "-C", sha,
                 "--", *HUNK_GLOBS)
        raw_hunks = list(parse_hunks(dt))
        if not raw_hunks:
            continue

        commit_removed = Counter()
        commit_added = Counter()
        for _p, _op, _h, rem, add in raw_hunks:
            for x in rem:
                if not trivial(x):
                    commit_removed[norm(x)] += 1
            for x in add:
                if not trivial(x):
                    commit_added[norm(x)] += 1

        # Which hunks sit in a preservation context: their own text says the words are being kept
        # as a quotation.  A move whose counterpart lands there is NOT a move (see the docstring).
        preserved_lines = Counter()
        for _p, _op, _h, rem, add in raw_hunks:
            if _PRESERVATION.search("\n".join(list(rem) + list(add))):
                for x in add:
                    if not trivial(x):
                        preserved_lines[norm(x)] += 1

        for hi, (p, op, hdr, rem, add) in enumerate(raw_hunks):
            cls = surface_class(p)
            ck = comment_kind(p, rem, add)
            st = status_of.get(p, "?")
            in_population = True
            if cls == "source" and ck == "code-only":
                in_population = False

            # The preservation filter, applied in BOTH directions: a hunk whose removed lines
            # reappear inside a "former wording preserved" block, and a hunk that IS such a block.
            # In either case the words survive as a quotation while the rule they stated may not,
            # and this tool cannot tell those apart -- so it does not call it a move.
            pres_partner = (
                any(preserved_lines.get(norm(x), 0) > 0 for x in rem if not trivial(x))
                or _PRESERVATION.search("\n".join(list(rem) + list(add))) is not None)

            mv = match_vector(rem, add, commit_added, commit_removed)

            if in_population:
                verdict, clause = classify(rem, add, commit_added, commit_removed, pres_partner,
                                           st)
            else:
                verdict, clause = "OUT-OF-POPULATION", "code-only-hunk-in-a-source-file"

            if verdict == "PURE" and not clause:
                raise SystemExit("STOP: a PURE verdict with no clause (mechanism 3).")

            rec = {
                "c": ci, "f": fidx(p), "i": hi, "h": hdr, "st": st,
                "d": [len(rem), len(add)], "m": mv,
                "cls": cls, "role": document_role(p), "ck": ck,
                "v": verdict, "k": clause,
                "sig": look_alike_signals(rem, add) if verdict == "FLAG" else [],
                "as": authoring_side(c["subject"]),
                "sc": True,
            }
            if op:
                rec["of"] = fidx(op)
            if pres_partner:
                rec["pres"] = True
            hunks.append(rec)

            if verdict == "PURE" and clause == "OK-MOVE-WHOLE":
                partners = set()
                for _p2, _op2, _h2, rem2, add2 in raw_hunks:
                    if _p2 == p:
                        continue
                    a2 = {norm(x) for x in add2 if not trivial(x)}
                    r2 = {norm(x) for x in rem2 if not trivial(x)}
                    if any(norm(x) in a2 for x in rem if not trivial(x)) or \
                       any(norm(x) in r2 for x in add if not trivial(x)):
                        partners.add(_p2)
                for q in partners:
                    move_pairs[(p, q)] += 1

    return assemble(end, commits, files_index, file_changes, hunks, renames, move_pairs)


def any_glob_match(path: str) -> bool:
    p = path.replace("\\", "/")
    if p in AUTHORED_DATA or p.rsplit("/", 1)[-1] in SOURCE_BASENAMES:
        return True
    ext = ("." + p.rsplit(".", 1)[-1].lower()) if "." in p.rsplit("/", 1)[-1] else ""
    return ext in PROSE_EXT or ext in SOURCE_EXT


def assemble(end, commits, files_index, file_changes, hunks, renames, move_pairs):
    paths = [None] * len(files_index)
    for p, i in files_index.items():
        paths[i] = p

    v = Counter(h["v"] for h in hunks)
    clause = Counter(h["k"] for h in hunks if h["v"] == "PURE")
    flag_shape = Counter(h["k"] for h in hunks if h["v"] == "FLAG")
    by_class = Counter(h["cls"] for h in hunks)
    flag_by_class = Counter(h["cls"] for h in hunks if h["v"] == "FLAG")
    flag_by_role = Counter(h["role"] for h in hunks if h["v"] == "FLAG")
    flag_by_stratum = Counter(commits[h["c"]]["stratum"] for h in hunks if h["v"] == "FLAG")
    all_by_stratum = Counter(commits[h["c"]]["stratum"] for h in hunks)
    flag_by_side = Counter(h["as"] for h in hunks if h["v"] == "FLAG")
    sig = Counter()
    for h in hunks:
        for s in h["sig"]:
            sig[s] += 1

    flags = [h for h in hunks if h["v"] == "FLAG"]
    unmatched_total = sum(h["m"][0] + h["m"][1] for h in flags)
    changed_total = sum(h["m"][2] + h["m"][3] for h in flags)
    unmatched_by_role = Counter()
    unmatched_by_stratum = Counter()
    unmatched_by_shape = Counter()
    for h in flags:
        u = h["m"][0] + h["m"][1]
        unmatched_by_role[h["role"]] += u
        unmatched_by_stratum[commits[h["c"]]["stratum"]] += u
        unmatched_by_shape[h["k"]] += u
    flags_fully_carried = sum(1 for h in flags if h["m"][0] + h["m"][1] == 0
                              and h["m"][2] + h["m"][3] > 0)

    flag_by_file = Counter(paths[h["f"]] for h in hunks if h["v"] == "FLAG")
    unmatched_by_file = Counter()
    for h in flags:
        unmatched_by_file[paths[h["f"]]] += h["m"][0] + h["m"][1]

    digit_only = sum(1 for h in flags if "differs-only-in-digits" in h["sig"])
    anchor_only = sum(1 for h in flags
                      if "differs-only-in-an-anchor-or-line-coordinate" in h["sig"])
    digit_by_file = Counter(paths[h["f"]] for h in flags
                            if "differs-only-in-digits" in h["sig"])

    # The register renders .md surfaces from an authored .json source; both are enumerated, so one
    # content change can appear twice.  Measured rather than argued away.
    mirror_paths = {p for p in paths if p == "DECISIONS.md" or p.startswith("decisions/")}
    mirror_flags = sum(1 for h in flags if paths[h["f"]] in mirror_paths)
    source_flags = sum(1 for h in flags if paths[h["f"]] in AUTHORED_DATA)
    fc_enumerated = sum(1 for f in file_changes if f["he"])
    fc_not = sum(1 for f in file_changes if not f["he"])
    fc_not_by_class = Counter(f["cls"] for f in file_changes if not f["he"])
    fc_not_by_role = Counter(f["role"] for f in file_changes if not f["he"])

    files_with_hunks = {h["f"] for h in hunks}
    fc_enum_no_hunks = [f for f in file_changes if f["he"] and f["f"] not in files_with_hunks]

    # Generator families for the class whose hunks are not enumerated (dispatch 0d / assumption A3).
    fam = Counter()
    for f in file_changes:
        if f["he"]:
            continue
        p = paths[f["f"]]
        fam["/".join(p.split("/")[:-1]) or "(repository top)"] += 1

    stop_a4 = all("v" in h and h["v"] for h in hunks)
    stop_a2 = len(renames) > 0

    art = {
        "what_this_is": (
            "THE CANDIDATE LIST.  Every documentation change of the restructuring period, "
            "enumerated whole and classified per hunk as PURE RESTRUCTURING or CONTENT CHANGE "
            "(FLAG).  The FLAGGED set is the candidate list -- the changes a later act must "
            "examine.  Nothing here is restored, reverted, corrected or resolved, and nothing "
            "here is a verdict on whether a change should have happened."),
        "dispatch": "cc_instruction_evidence_candidate_pass.md",
        "generator": "tools/audit/gen_doc_change_candidates.py",
        "hunk_file": "tools/audit/doc_change_candidates_hunks.jsonl",
        "hunk_record_fields": {
            "c": "index into `commits` below",
            "f": "index into `files` below (the path after any rename or copy)",
            "of": "index into `files` -- the path it came from, when git detected a rename or copy",
            "i": "the hunk's ordinal within its commit's diff",
            "h": "the -U0 hunk header, as `-oldStart,oldLen +newStart,newLen`",
            "st": "the file's status in that commit: A added, M modified, D deleted, R renamed, "
                  "C copied, with git's similarity percentage where it gives one",
            "d": "[lines removed, lines added]",
            "m": "[unmatched removed, unmatched added, non-trivial removed, non-trivial added] -- "
                 "unmatched means not carried by a counterpart elsewhere in the same commit",
            "cls": "surface class", "role": "document role", "ck": "comment kind, for source files",
            "v": "PURE | FLAG | OUT-OF-POPULATION",
            "k": "the OK-list clause for a PURE, or the change shape for a FLAG",
            "sig": "look-alike signals present in the changed text (reporting only, never a "
                   "verdict)",
            "as": "authoring side, read from the commit subject",
            "sc": "self-classified -- true for the whole population, see the declaration below",
            "pres": "present when the hunk sits in, or feeds, a preserved-former-wording context",
            "★_to_retrieve_a_hunk": "git show <sha> -- <path>, at the header's line range.",
        },
        "reproduce": ("python tools/audit/gen_doc_change_candidates.py --check   # re-derives both "
                      "artifacts from git objects and exits 1 on any drift"),
        "range": {
            "start_commit_EXCLUSIVE": PERIOD_START,
            "end_commit": end,
            "commits_in_the_population": len(commits),
            "★_the_start_is_AUTHORED_as_the_earliest_of_four_bounds": (
                "The record names NO start for 'the restructuring period'.  It names four "
                "restructuring acts, each citable, listed under `bounds`.  The dispatch's rule for "
                "this case is 'go back further, not less -- err early', so the population opens at "
                "the EARLIEST of the four and the other three are published as strata below.  "
                "WHAT WOULD SETTLE IT: a user ruling naming the start.  WHAT BOUNDS THE ERROR IN "
                "THE OTHER DIRECTION: no act of this shape earlier than the first bound is named "
                "anywhere in the record, and because principle #10 has demanded documentation-code "
                "sync since long before any of these acts, an earlier start has no establishable "
                "boundary at all -- it would make the period the whole repository history."),
            "bounds": BOUNDS,
        },
        "the_classification_rule": {
            "the_users_words": (
                "PURE restructuring of documentation is OK -- no knowledge loss, no change, no "
                "growth.  Any change to documentation that changes actual meaning, design, "
                "algorithm or content -- regardless of how and where it is documented -- is "
                "probably NOT OK."),
            "the_test": ("before-state against after-state, INSIDE the documentation.  It needs "
                         "neither the code nor the change's recorded reason.  Growth counts."),
            "the_default": "on doubt, FLAG.  This tool emits PURE only where a recognizer fires.",
        },
        "counted": {
            "commits": len(commits),
            "file_changes_enumerated": len(file_changes),
            "file_changes_whose_hunks_are_enumerated": fc_enumerated,
            "file_changes_whose_hunks_are_NOT_enumerated": fc_not,
            "hunks_enumerated": len(hunks),
            "verdicts": dict(v),
            "★_THE_CANDIDATE_LIST_SIZE": v.get("FLAG", 0),
            "★_THE_SECOND_SIZING_COUNT_unmatched_nontrivial_changed_lines_on_flagged_hunks":
                unmatched_total,
            "nontrivial_changed_lines_on_flagged_hunks": changed_total,
            "flagged_hunks_whose_every_changed_line_is_carried_elsewhere_in_the_same_commit":
                flags_fully_carried,
            "★_what_those_three_counts_mean_together": (
                "The first is how many hunks a reviewer must open.  The second is how much text "
                "inside them is NOT accounted for by a carry elsewhere in the same commit -- the "
                "actual evidence question, once relocation is netted out.  The third counts hunks "
                "the carry test matched completely and which are flagged anyway, because a "
                "preservation context, a whitespace difference or the copy sitting in a generated "
                "surface stopped the move recognizer.  NONE of the three is a verdict; the "
                "candidate list is the flagged hunks, all of them."),
            "unmatched_lines_by_document_role": dict(unmatched_by_role.most_common()),
            "unmatched_lines_by_stratum": dict(unmatched_by_stratum),
            "unmatched_lines_by_flag_shape": dict(unmatched_by_shape),
            "pure_by_clause": dict(clause),
            "flag_by_shape": dict(flag_shape),
            "hunks_by_surface_class": dict(by_class),
            "flags_by_surface_class": dict(flag_by_class),
            "flags_by_document_role": dict(flag_by_role),
            "hunks_by_stratum": dict(all_by_stratum),
            "flags_by_stratum": dict(flag_by_stratum),
            "flags_by_authoring_side": dict(flag_by_side),
            "look_alike_signals_on_flagged_hunks": dict(sig.most_common()),
            "distinct_files_touched": len(files_index),
            "renames_and_copies_detected": len(renames),
            "cross_file_move_pairs_detected": len(move_pairs),
        },
        "★_the_largest_shape_inside_the_candidate_list_REPORTED_NOT_CLASSIFIED": {
            "what_it_is": (
                "Flagged hunks whose removed and added text are identical once every run of "
                "digits is masked out.  Overwhelmingly these are the decisions register's `home`, "
                "`anchor` and `delegation` fields -- file:line coordinates re-aimed as the "
                "documents they point into grew -- together with the same fields in the .md "
                "surfaces rendered from that register."),
            "flagged_hunks_of_this_shape": digit_only,
            "of_those_naming_an_anchor_field_or_a_section_sign": anchor_only,
            "share_of_the_candidate_list": (round(digit_only / v["FLAG"], 4)
                                            if v.get("FLAG") else None),
            "by_file": [{"file": p, "hunks": n} for p, n in digit_by_file.most_common(25)],
            "★_why_it_is_REPORTED_and_not_CLASSIFIED_PURE": (
                "The OK list admits 'Re-aiming a drifted pointer or anchor AT THE SAME CONTENT'.  "
                "The qualifier is the whole clause, and nothing mechanical establishes it: showing "
                "that a coordinate still lands on the sentence it used to land on means reading "
                "the target document at both commits.  Arguing from the shape to the clause is "
                "exactly what mechanism 4's stretch stop forbids -- and the record already carries "
                "an instance of the argument failing, a commit whose subject is 'fix the two "
                "over-shifted CLAUDE.md anchors the guard caught'.  So every one of these stays "
                "FLAGGED."),
            "the_act_that_would_settle_the_class": (
                "For each such hunk: resolve the old coordinate in the target document at the "
                "parent commit and the new coordinate at the child commit, and compare the text "
                "they land on.  It is mechanical and it is a DIFFERENT act from this pass; it is "
                "named here so the size of the remainder can be seen, not started."),
        },
        "★_how_to_read_the_strata": (
            "Every hunk carries the stratum of its commit.  A narrower reading of the period -- "
            "for instance the D-231 phase-1 reading, S4 -- is taken by keeping only the strata at "
            "or after that bound.  The enumeration does not have to be re-run for that; nothing "
            "was excluded by it."),
        "the_flagged_set_by_file": [
            {"file": p, "flagged_hunks": n, "unmatched_lines": unmatched_by_file.get(p, 0),
             "role": document_role(p), "class": surface_class(p)}
            for p, n in flag_by_file.most_common()
        ],
        "the_class_whose_hunks_are_NOT_enumerated": {
            "what_it_is": (
                "Generated artifacts and data files -- .json, .csv, .txt and the like -- which "
                "dispatch section 0d makes a SEPARATE CLASS, reported and not dropped, with "
                "recoverability stated per generator family rather than per hunk.  Their FILE "
                "CHANGES are enumerated above and in the hunk file's companion records; their "
                "HUNKS are not."),
            "why_not_per_hunk": (
                "Deliberate, and stated rather than silent: the class carries a change volume "
                "orders of magnitude larger than the prose it derives from, and per-hunk records "
                "for it would bury the candidate list inside regenerated output.  Section 0d asks "
                "for recoverability per family instead, which is what is recorded here."),
            "file_changes_in_the_class": fc_not,
            "by_surface_class": dict(fc_not_by_class),
            "by_document_role": dict(fc_not_by_role),
            "generator_families_by_directory": dict(fam.most_common()),
            "recoverability_A3": "UNESTABLISHED for every family, without exception.",
            "★_why_unestablished_rather_than_assumed": (
                "Assumption A3 says a generated artifact's content is recoverable from its inputs "
                "and that this is a claim about EACH generator, not a blanket one.  Establishing "
                "it means running each family's generator at the commit in question and showing "
                "byte-identity -- an act this pass did not perform for any family.  It is marked "
                "unestablished rather than assumed, which is what A3 requires."),
            "the_act_that_would_establish_it": (
                "Per family: run that family's generator's --check at the relevant commits and "
                "record the byte-identity result.  Several generators in tools/audit/ carry such "
                "such a re-derivation mode; whether every family does is itself unestablished here."),
            "the_one_authored_member_pulled_OUT_of_this_class": {
                "path": sorted(AUTHORED_DATA),
                "why": ("CLAUDE.md's decisions-register rule (d) makes this file the thing a "
                        "human EDITS and the rendered .md files the thing a generator writes.  It "
                        "is therefore an authored surface and its hunks ARE enumerated."),
                "the_stated_bound": (
                    "Any OTHER authored data file sitting inside the un-enumerated class has not "
                    "been identified.  This is a stated bound of the enumeration, not a claim "
                    "that none exists.  What would settle it: a per-file check of which .json "
                    "and .csv paths any committed generator writes."),
            },
        },
        "the_decisions_register_mirror_measured": {
            "flagged_hunks_in_the_authored_source": source_flags,
            "flagged_hunks_in_the_surfaces_rendered_from_it": mirror_flags,
            "★_what_this_is_for": (
                "The two counts bound the double count.  A change to the register's data appears "
                "once in tools/audit/decisions/backbone_decisions.json and again in DECISIONS.md "
                "and decisions/group_*.md, which are rendered from it.  Neither side is dropped -- "
                "ruling 4 forbids excluding by role, and choosing which of the two is 'the real "
                "change' would be this tool deciding something.  The measurement is published so a "
                "reader can net it out deliberately."),
        },
        "generated_prose_surfaces_are_enumerated_ANYWAY": (
            "DECISIONS.md and decisions/group_*.md are rendered from "
            "tools/audit/decisions/backbone_decisions.json and carry a GENERATED FILE banner.  "
            "Their hunks are enumerated all the same, alongside the authored source's, so nothing "
            "is dropped by a role judgment (ruling 4).  The consequence -- that one content change "
            "can appear both in the authored source and in the surface rendered from it -- is "
            "disclosed here rather than removed, because removing it would mean this tool deciding "
            "which of the two is the real change."),
        "assumptions_checked": {
            "A1_period_start_establishable": {
                "verdict": "PARTIAL -- reported as a bound, not as a settled date.",
                "detail": ("The record establishes four restructuring acts and names none of them "
                           "as THE start.  The population opens at the earliest, per the "
                           "dispatch's err-early rule, and every stratum is published so a "
                           "narrower reading costs no re-run."),
            },
            "A2_rename_and_cross_file_move_detection_runs": {
                "verdict": "ESTABLISHED" if stop_a2 else "NOT ESTABLISHED",
                "renames_or_copies_found": len(renames),
                "cross_file_move_pairs_found": len(move_pairs),
                "how_renames_are_detected": "git show --name-status -M -C on every commit.",
                "how_cross_file_moves_are_detected": (
                    "Line-multiset matching WITHIN a commit: a hunk's non-trivial removed lines "
                    "are looked for among the lines added elsewhere in the same commit, and vice "
                    "versa, with multiplicity.  A hunk matched in both directions is called "
                    "OK-MOVE-WHOLE; a hunk matched only partially keeps its unmatched remainder and "
                    "is FLAGGED, which is how a partial carry surfaces instead of hiding."),
                "the_examples": [{"commit": r["commit"], "status": r["status"],
                                  "from": r["from"], "to": r["to"]} for r in renames[:20]],
                "top_cross_file_move_pairs": [
                    {"from": a, "to": b, "hunks": n}
                    for (a, b), n in move_pairs.most_common(20)],
            },
            "A3_generated_artifact_recoverability": {
                "verdict": "UNESTABLISHED for every family -- see the class block above.",
            },
            "A4_every_hunk_receives_a_verdict": {
                "verdict": "ESTABLISHED" if stop_a4 else "NOT ESTABLISHED",
                "hunks_enumerated": len(hunks),
                "hunks_carrying_a_verdict": sum(1 for h in hunks if h.get("v")),
                "reconciliation": {
                    "PURE_plus_FLAG_plus_OUT_OF_POPULATION": sum(v.values()),
                    "equals_hunks_enumerated": sum(v.values()) == len(hunks),
                    "file_changes_with_hunks_enumerated_that_produced_no_hunk":
                        len(fc_enum_no_hunks),
                    "★_what_that_last_count_is": (
                        "File changes of an enumerated type that yielded no -U0 hunk: pure "
                        "renames with no content change, file-permission changes, and empty-file additions.  "
                        "They are counted here rather than lost, and each is present in the file-"
                        "change records."),
                },
            },
        },
        "self_classification_declaration_mechanism_5": {
            "the_declaration": (
                "This classification is performed by an executing CC session.  Every commit in "
                "the population was made by an executing session of that same kind -- the git "
                "author is one identity throughout -- and the prose inside many of them was "
                "authored by Cowork and committed by CC.  So the WHOLE population is "
                "self-classified, and every hunk record carries sc=true rather than the marker "
                "being applied to a subset."),
            "per_hunk_field": "`as` -- the authoring side, read from the commit subject's prefix.",
            "distribution": dict(Counter(h["as"] for h in hunks)),
        },
        "what_the_flagged_set_is_NOT": (
            "It is not a list of errors, and it is not a restoration list.  The restoration "
            "criterion -- restore if and only if the documentation was copied from the "
            "implementation -- is a DIFFERENT test at a LATER stage, and this pass does not apply "
            "it, does not prepare it, and expresses no view on any member's fate."),
        "commits": [{"i": i, "sha": c["sha"], "date": c["date"], "stratum": c["stratum"],
                     "subject": c["subject"]} for i, c in enumerate(commits)],
        "files": paths,
        "file_changes": file_changes,
    }

    if not stop_a4:
        raise SystemExit("STOP: a hunk carries no verdict (assumption A4).")
    if sum(v.values()) != len(hunks):
        raise SystemExit("STOP: the verdict reconciliation does not balance (assumption A4).")
    if fc_enumerated + fc_not != len(file_changes):
        raise SystemExit("STOP: the file-change reconciliation does not balance -- a change is in "
                         "neither the hunk-enumerated class nor the class named un-enumerated.")
    for h in hunks:
        if h["v"] == "PURE" and not h["k"]:
            raise SystemExit("STOP: a PURE verdict with no clause (mechanism 3).")

    return art, hunks


def render(art, hunks):
    main = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    lines = [json.dumps(h, ensure_ascii=False, separators=(",", ":")) for h in hunks]
    return main, "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    end = "HEAD"
    if "--end" in argv:
        end = argv[argv.index("--end") + 1]
    check = "--check" in argv
    if check and OUT_MAIN.exists():
        try:
            end = json.loads(OUT_MAIN.read_text(encoding="utf-8"))["range"]["end_commit"]
        except Exception:
            pass
    art, hunks = build(end)
    main_text, hunk_text = render(art, hunks)
    if check:
        if not OUT_MAIN.exists() or not OUT_HUNKS.exists():
            print("FAIL: artifact missing")
            return 1
        bad = False
        if OUT_MAIN.read_text(encoding="utf-8") != main_text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT_MAIN)
            bad = True
        if OUT_HUNKS.read_text(encoding="utf-8") != hunk_text:
            print("FAIL: re-derivation differs from the committed artifact:", OUT_HUNKS)
            bad = True
        if bad:
            return 1
        print("OK: the candidate pass re-derives byte-identically.")
        return 0
    OUT_MAIN.write_text(main_text, encoding="utf-8")
    OUT_HUNKS.write_text(hunk_text, encoding="utf-8")
    c = art["counted"]
    print("wrote", OUT_MAIN)
    print("wrote", OUT_HUNKS)
    print(f"  commits {c['commits']}, file changes {c['file_changes_enumerated']}, "
          f"hunks {c['hunks_enumerated']}")
    print(f"  verdicts: {c['verdicts']}")
    print(f"  THE CANDIDATE LIST: {c['★_THE_CANDIDATE_LIST_SIZE']} flagged hunks")
    print(f"  PURE by clause: {c['pure_by_clause']}")
    d = art["★_the_largest_shape_inside_the_candidate_list_REPORTED_NOT_CLASSIFIED"]
    print(f"  of the flagged: {d['flagged_hunks_of_this_shape']} differ only in digit runs "
          f"({d['share_of_the_candidate_list']}), "
          f"{d['of_those_naming_an_anchor_field_or_a_section_sign']} naming an anchor field")
    print(f"  unmatched non-trivial changed lines on flagged hunks: "
          f"{c['★_THE_SECOND_SIZING_COUNT_unmatched_nontrivial_changed_lines_on_flagged_hunks']}")
    print(f"  renames/copies {c['renames_and_copies_detected']}, "
          f"cross-file move pairs {c['cross_file_move_pairs_detected']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
