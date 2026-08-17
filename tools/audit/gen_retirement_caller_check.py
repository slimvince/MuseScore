#!/usr/bin/env python3
"""DOES ANYTHING STILL POINT AT A FILE FLAGGED FOR RETIREMENT — established at the objects?

THE STANDING WARNING THIS DISCHARGES.  The ruled artifact inventory flags nine retirement
candidacies, and the user's own ruling attaches the same guard to all of them
(`cowork_rulings_2026_08_15_inventory_sitting.md` §3.16): *"every flag is a CANDIDACY; retirement is
archive-with-record, nothing destroyed (#12); no archiving executes on the name-scan signal alone —
the caller-check at the objects comes first"*.  The pruning plan repeats it
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §8): *"no archiving executes
on the citation-scan signal alone — the caller-check at the objects precedes every wave."*  This is
that check.

WHY THE NAME-SCAN SIGNAL WAS NOT ENOUGH, in the surface's own words: an absent citation is evidence
that the GOVERNING RECORD names nothing, not that nothing anywhere depends on the file — *"a tool
imported by another tool is invisible to it"*.  So this check reads the WHOLE tracked tree at an
explicit commit rather than the seven governing documents.

★ THIS TOOL ARCHIVES, MOVES, RENAMES AND DELETES NOTHING.  It publishes a verdict per candidacy and
a caller list per member.  A PASSES-THE-CHECK verdict confers nothing: archiving is a later
dispatch's act, taken after this artifact is verified at the objects.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   the candidacy population — the flagged classes and, for a partly-flagged class, the
            flagged side of its citation split — IMPORTED from `gen_artifact_inventory_surface`
            rather than re-listed here (#6, one path per concern), so this tool and the ruling
            surface cannot disagree about which files are flagged; every member path, read from the
            committed artifact inventory; every reference, found in the tracked tree at an explicit
            commit; every count.
  AUTHORED  the ruled CONDITION per candidacy, each carrying the sentence of the ruling record it
            was read from — and every one of those sentences is LOCATED in that record on every
            run, so a condition cannot outlive the words that imposed it.

★ WHAT A REFERENCE IS HERE, AND WHAT IT IS NOT.  A file REFERENCES a candidate when its text at the
measured commit contains the candidate's base name.  That covers the three kinds the dispatch names
— an import, a path written out, a tool reading a file by name — and it is deliberately GENEROUS:
erring toward finding a caller errs away from archiving something that is still used, which is the
safe direction for a candidacy nobody has ruled on.  What it does NOT cover, stated before its first
use: a reference built at run time from pieces (a directory joined to a name, a name assembled from
a pattern) carries no literal to find, and a binary file is not searched at all.  **So NONE FOUND
means no literal naming was found in text, never that nothing depends on the file.**

★ REFERENCES FROM INSIDE THE CANDIDATE'S OWN CLASS ARE SET ASIDE, NOT DROPPED (#12).  The dispatch
asks for references from outside the candidate's own class, because a class retiring as a whole
carries its internal cross-references with it.  Every such reference is still counted and published
in its own field, so the exclusion can be checked rather than trusted.

★★ THE RULED READING, ADDED 2026-08-16 — A NAMING FROM A TREE-ENUMERATING RECORD DOES NOT HOLD A
CANDIDATE.  The first run of this check returned every candidacy HELD-BY-CALLERS and reported that
the naming was mostly done by records that name every path by construction, which says nothing
about whether anything DEPENDS on a file.  The question was returned undecided and the user ruled
it (`cowork_rulings_2026_08_16_preparation_return.md` §1, Alternative A).  What the ruling adds,
and what it forbids:

  * every caller is classified by KIND, and the classification is **DERIVED** — *"never a
    naming-breadth threshold ... and never a hand-typed exemption list"*;
  * a caller established as an ENUMERATOR — a generated file, or a surface rendered from one,
    whose generator enumerates the tracked tree — has its namings **published as data**, holding
    nothing;
  * **a caller whose kind cannot be derived STOPS to the user** rather than being guessed; its
    namings HOLD in the meantime, which is the conservative direction;
  * namings from FELLOW FLAGGED FILES are **set aside into their own field**, like same-class
    namings — files archived together keep resolving each other through the archive record (#12).
    Nothing is dropped; every set-aside naming stays published;
  * every surviving holder is published **BY KIND** — a tool reading the file by name, a
    mandatory-read or boot listing, a prose citation — and **the follow-up question, whether a
    prose citation holds, is DEFERRED to that evidence and is NOT decided here.**

★★ THE DEFERRED QUESTION IS ANSWERED, AND THE NINE UNDERIVABLE CALLERS ARE RULED — 2026-08-17,
`cowork_rulings_2026_08_17_callers_sitting.md`, held at the census's own published evidence.  Four
rulings, all four USER-RULED INPUTS rather than derived classifications, and each is marked as such
wherever it changes a verdict here:

  * **the nine KIND-UNDERIVABLE callers are ENUMERATOR-class** (§1), *"on the published
    evidence ... Their namings are published as data and hold nothing"*.  The membership is
    DERIVED from the census reading the sitting was held over, read at the git object of the
    commit that carries it, and each derived caller is then LOCATED in the sitting record itself —
    never retyped;
  * **a prose citation does NOT hold a candidate** (§2) — the deferred question, answered;
  * **a naming outside the ruling's three kinds — a data record — does NOT hold** (§3), on the
    same ground and more strongly;
  * **a tool reading the file by name, and a mandatory-read or boot listing, HOLD** (§4), *"under
    every part of this sitting"* — each breaks in fact when the file moves.

★ WHAT §1 DOES NOT DO, in the ruling's own words: *"A future caller the derivation cannot place
still STOPS to the user; nothing here creates a precedent for guessing."*  So the override reaches
exactly the nine callers the sitting read and no others: a caller this derivation cannot place
today is KIND-UNDERIVABLE, HOLDS, and returns to the user exactly as before.

★ HOW A CALLER'S KIND IS DERIVED, in two links, each published per caller with its evidence.  The
dispatch's own assumption A2 names both: *"a generated file names its generator ... and whether
that generator enumerates the tracked tree is readable at the generator's own source"*.

  LINK 1, caller -> generator, by TWO routes, and which one fired is recorded per caller:
    route A  the caller's own text DECLARES its generator (a `generator`, `generated_by` or
             `instrument` field; a rendered surface's own `Generated by` line);
    route B  a tracked Python source WRITES the caller's path.  Derived by parsing every tracked
             `*.py` at the measured commit and resolving each write site's path expression to a
             repository-relative path — never by matching a base name, which would confuse a
             reader of a file with its writer.
  LINK 2, generator -> ENUMERATING?, by three routes, each recorded:
    the generator's own source calls a tracked-tree enumeration; or it imports a module that
    does; or it READS an artifact whose own generator does — which is the ruling's *"or a surface
    rendered from one"* limb, and is why the property is closed transitively rather than read off
    one file.

★ WHAT THE KIND CLASSIFICATION DOES NOT ESTABLISH, stated before its first use.  That a caller is
NOT an enumerator is established only as far as link 1 reaches: a file produced by something other
than a tracked Python source, and declaring nothing, is reported as not produced by the record's
own machinery, and that is a statement about the record's machinery rather than about the file's
history.  The direction of the residual error is the safe one — such a caller HOLDS.

WHY THE READING IS PINNED TO A COMMIT.  A check that re-read the working tree would go red the first
time anybody wrote a file that happens to name a candidate — the tree moving on correctly, which is
the OI-301/OI-305 shape.  So the measurement is taken at an explicit commit, that commit is recorded
inside the artifact, and `--check` re-derives at the recorded one.  What stays LIVE is the
population: it is re-imported on every run and reconciled with the graded set in BOTH directions.

THE STOPS:
  * a flagged class the committed inventory does not carry STOPS the tool;
  * a flagged class the inventory publishes no members for STOPS it — the member list cannot be
    derived, and nothing here is hand-listed;
  * a candidacy with no authored condition record, or a condition record naming a candidacy the
    derivation does not carry, STOPS it — in BOTH directions;
  * a condition whose quoted sentence is no longer found in the ruling record STOPS it;
  * a verdict outside the closed three-value vocabulary STOPS it;
  * a candidacy with no verdict, or a verdict count that does not account for the population,
    STOPS it.

Run:
  python tools/audit/gen_retirement_caller_check.py --at <commit>   # measure and write
  python tools/audit/gen_retirement_caller_check.py --check         # re-derive, exit 1 on drift
"""
from __future__ import annotations

import ast
import json
import posixpath
import re
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)
import gen_artifact_inventory as inventory_tool                   # noqa: E402  (the signature, once)
import gen_artifact_inventory_surface as surface                  # noqa: E402  (the flags, once)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
RULING = ROOT / "cowork_rulings_2026_08_15_inventory_sitting.md"
READING_RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
CALLERS_RULING = ROOT / "cowork_rulings_2026_08_17_callers_sitting.md"
OUT = ROOT / "tools" / "audit" / "retirement_caller_check.json"

# The commit whose git OBJECT carries the census reading the callers sitting was held over. Its
# KIND-UNDERIVABLE list is exactly the population §1 rules on, so the nine are DERIVED from it
# rather than typed here. An explicit hash, the only git read D-253 permits.
CALLERS_RULING_EVIDENCE_COMMIT = "e94f765c25b49d2c9ffa47b1a296302debc25ce6"

PASSES = "PASSES-THE-CHECK"
HELD_CALLERS = "HELD-BY-CALLERS"
HELD_CONDITION = "HELD-BY-CONDITION"
VERDICTS = (PASSES, HELD_CALLERS, HELD_CONDITION)

NO_CONDITION = "none — the ruling attaches no condition beyond this check"

# ── the closed CALLER-KIND vocabulary of the ruled reading (§1, 2026-08-16) ──────────────────────
# Exactly one of these is assigned to every caller, and only the first holds nothing.
KIND_ENUMERATOR = "ENUMERATOR"
KIND_GENERATED_NOT_ENUMERATING = "GENERATED-BUT-NOT-ENUMERATING"
KIND_NOT_GENERATED = "NOT-PRODUCED-BY-THE-RECORD'S-OWN-MACHINERY"
KIND_UNDERIVABLE = "KIND-UNDERIVABLE"
CALLER_KINDS = (KIND_ENUMERATOR, KIND_GENERATED_NOT_ENUMERATING,
                KIND_NOT_GENERATED, KIND_UNDERIVABLE)
KINDS_THAT_HOLD = (KIND_GENERATED_NOT_ENUMERATING, KIND_NOT_GENERATED, KIND_UNDERIVABLE)

# ── the closed HOLDER-KIND vocabulary, taken from the ruling's own three words ───────────────────
HOLDER_TOOL = "a tool reading the file by name"
HOLDER_MANDATORY = "a mandatory-read or boot listing"
HOLDER_PROSE = "a prose citation"
HOLDER_OTHER = "outside the three kinds the ruling names"
HOLDER_KINDS = (HOLDER_TOOL, HOLDER_MANDATORY, HOLDER_PROSE, HOLDER_OTHER)

# ── THE USER-RULED HALF of the holder vocabulary (the callers sitting, 2026-08-17, §§2-4) ────────
# Exactly two of the four HOLD. This is a RULED input, not a derivation: the tool derives which
# kind a holder is, and the ruling decides which kinds hold. Both halves are published per member.
HOLDER_KINDS_THAT_HOLD = (HOLDER_TOOL, HOLDER_MANDATORY)
HOLDER_KINDS_THAT_HOLD_NOTHING = (HOLDER_PROSE, HOLDER_OTHER)
USER_RULED = "USER-RULED at the 2026-08-17 callers sitting"
DERIVED_KIND = "derived by this tool's own two links"


class Stop(Exception):
    """The check cannot be published as an enumeration. Never a warning."""


# ── AUTHORED: the ruled condition per candidacy, each with the sentence it was read from ─────────
#
# The condition is what the user's ruling attaches to a candidacy BEYOND this check. Three shapes
# appear in the ruling record and no fourth: mining must run first, the members must be seen by the
# user first, or nothing. Every quoted sentence below is LOCATED in the ruling record on every run.
CONDITIONS: dict[str, tuple[str, str]] = {
    "writing-side-scratch-directories": (
        NO_CONDITION,
        "The scratch directories: no role, not mined, retirement candidate CONFIRMED as a flag."),
    "llm-triage-prompts": (
        NO_CONDITION,
        "The LLM triage prompts: retirement candidates (the user was shown the live-consumer "
        "caveat and named none)."),
    "measurement-outputs-recorded-beside-the-tools": (
        "mined first — the class goes to the fact-gate, and only the members it leaves unnamed "
        "are flagged",
        "Class 36: fact-gate, then unnamed members flagged."),
    "idiom-discovery-workspace": (
        "mined first — the fact-gate takes the warnings before the class becomes a candidacy",
        "Idiom-discovery workspace: fact-gate for warnings, then retirement candidate."),
    "ai-assistant-design-notes": (
        NO_CONDITION,
        "The separate-assistant notes: retirement candidate (the user was shown the "
        "bears-on-analysis caveat and named nothing)."),
    "stray-working-files-committed-to-the-repository-root": (
        "the members are seen by the user first — the ruling names the unpacked score-container "
        "members specifically, before any archiving",
        "The stray root files: retirement candidate as a class, the unpacked score-container "
        "members seen by the user before any archiving."),
    "documentation-directory-prose": (
        "mined first — the uncited side becomes a candidacy only once it has been mined",
        "the uncited 15 are retirement candidates once mined."),
    "measurement-and-analysis-tools": (
        "mined first — the uncited side goes to the fact-gate before it is a candidacy, and the "
        "ruling names this very caller-check as preceding any archiving",
        "Class 35's split stands (30 cited: machinery; 100 uncited: fact-gate then retirement "
        "candidates, caller-check at the objects before any archiving executes)."),
    "reports-from-the-coding-side": (
        "mined first — the uncited side becomes a candidacy only once it has been mined",
        "Class 21's split stands; the uncited 30 are retirement candidates once mined."),
}

# A file-name-shaped token, the same shape the ruling surface's own citation scan uses.
NAME_TOKEN = re.compile(r"[A-Za-z0-9_.\-]+\.[A-Za-z0-9]+")


# `core.quotepath=false` is not cosmetic and not optional: without it git C-quotes any path holding
# a non-ASCII byte, and this repository has one — a triage prompt named after a diminished chord
# symbol. A quoted path is not the path, so `cat-file` reports it missing and the walk stops. Set
# once, on every git call this file makes, so the two can never disagree.
GIT_BASE = ["git", "-C", str(ROOT), "-c", "core.quotepath=false"]


def git(*args: str) -> str:
    proc = subprocess.run([*GIT_BASE, *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode not in (0, 1):        # git grep exits 1 on "no match", which is not failure
        raise Stop("git failed: " + " ".join(args) + " — "
                   + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout.decode("utf-8", "replace")


def tree_paths(commit: str) -> list[str]:
    """Every tracked path at `commit`, read from the git object with paths unquoted."""
    return [line for line in git("ls-tree", "-r", "--name-only", commit).splitlines()
            if line.strip()]


def normalized(text: str) -> str:
    """Whitespace collapsed and emphasis marks removed, so a quote survives line wrapping."""
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_conditions() -> dict[str, str]:
    """Every authored condition's sentence, LOCATED in the ruling record. A missing one STOPS."""
    if not RULING.exists():
        raise Stop(f"the ruling record is missing: {RULING}")
    text = normalized(RULING.read_text(encoding="utf-8"))
    missing = [name for name, (_c, quote) in CONDITIONS.items()
               if normalized(quote) not in text]
    if missing:
        raise Stop("a condition's quoted sentence is no longer in the ruling record, so the "
                   f"condition would outlive the words that imposed it: {missing}")
    return {name: quote for name, (_c, quote) in CONDITIONS.items()}


# ══ THE RULED READING'S KIND DERIVATION (user, 2026-08-16, §1) ═══════════════════════════════════
#
# AUTHORED and published: the sentences of the ruling this reading is taken from, LOCATED in that
# record on every run, exactly as the candidacy conditions are — a reading may not outlive the words
# that imposed it.
READING_SENTENCES = {
    "the reading itself":
        "A naming from a tree-enumerating record does not hold a candidate.",
    "what the classification may not be":
        "Never a naming-breadth threshold (the twice-declined shape) and never a hand-typed "
        "exemption list.",
    "what an underivable kind does":
        "A caller whose kind cannot be derived STOPS to the user rather than being guessed.",
    "the fellow-flagged set-aside":
        "Namings from fellow flagged files are set aside into their own field, like same-class "
        "namings",
    "the deferred question":
        "The re-run publishes each surviving holder BY KIND — a tool reading the file by name, a "
        "mandatory-read or boot listing, a prose citation — and the follow-up question (does a "
        "prose citation hold, given that archive-with-record keeps it resolvable?) is DEFERRED to "
        "that evidence.",
    "what it archives":
        "Nothing is archived by this ruling.",
}

# AUTHORED and published: what counts as ENUMERATING THE TRACKED TREE at a generator's own source.
# Every one of these names files by construction rather than by depending on any of them, which is
# the property the ruling turns on.
#
# ★ THE SIGNAL IS SOUGHT AMONG THE SOURCE'S STRING CONSTANTS, NOT IN ITS TEXT, AND THE DIFFERENCE
# WAS MEASURED RATHER THAN ASSUMED. A first version matched the source text, and two generators
# came back enumerating on the strength of PROSE: a corpus registry builder whose notes field says
# an inventory was "taken from git objects (ls-tree)", and the shell-read guard, whose forbidden-
# utility list contains the word `grep`. Neither calls git to enumerate anything. A constant that
# IS the subcommand is a git argument; a sentence that mentions it is a sentence.
#
# The two tests below, and why they differ. A constant EQUAL to `ls-tree`, `ls-files` or
# `diff-tree`, or one OPENING with `--porcelain`, is a git argument and nothing else — no other
# use of those spellings exists. `grep` is an ordinary word, so it counts only where the source
# puts it in a git command: as an argument to a helper whose name ends in `git`, or beside the
# constant `git` in the same call or list.
STRONG_ENUMERATION_CONSTANTS = {
    "ls-tree": "git ls-tree — every path of a commit's tree",
    "ls-files": "git ls-files — every tracked path",
    "diff-tree": "git diff-tree — every path a commit touched",
}
PORCELAIN_PREFIX = "--porcelain"
PORCELAIN_LABEL = "git status --porcelain — every changed path"
GIT_CONTEXT_CONSTANTS = {
    "grep": "git grep over the tree — every path whose text matches",
}

# AUTHORED and published: the spellings by which a generated file DECLARES its generator. The
# spellings are authored; every value they capture is DERIVED from the caller's own text and quoted.
#
# ★ EVERY ONE IS ANCHORED TO THE START OF A LINE, AND THE ANCHOR IS NOT COSMETIC. The first run of
# this derivation classified a coding-side report as a generated artifact because the report says,
# in prose, that a DIFFERENT file is generated by a tool — a sentence about someone else read as a
# declaration about itself. A declaration opens its line; a mention does not.
DECLARATION_KEYS = [
    ("a `generator` field", re.compile(r'(?m)^\s*"generator"\s*:\s*"([^"]+\.py)"')),
    ("a `generated_by` field", re.compile(r'(?m)^\s*"generated_by"\s*:\s*"([^"]+\.py)"')),
    ("an `instrument` field", re.compile(r'(?m)^\s*"instrument"\s*:\s*"([^"]+\.py)"')),
    ("a rendered surface's own `Generated by` line",
     re.compile(r"(?m)^[\s>*_`(\[]{0,6}Generated by [`\"]([^`\"]+\.py)[`\"]")),
]

# AUTHORED and published: the ruling's *"or a surface rendered from one"* limb, taken from the
# surface's OWN declaration of what it was rendered from. `from` may sit on the next line, so the
# whitespace between the two is allowed to span one.
RENDERED_FROM = re.compile(
    r"(?m)^[\s>*_`(\[]{0,6}Generated by [`\"][^`\"]+\.py[`\"]\s+from\s+[`\"]([^`\"]+)[`\"]")

# AUTHORED and published: which file extensions make a holder A TOOL READING THE FILE BY NAME, and
# which make it A PROSE CITATION. The holder-kind rule is applied in the order the function below
# states, and every holder carries the line its naming was found on, so a verdict can be checked by
# eye.
#
# ★ A DATA FILE IS DELIBERATELY IN NEITHER SET. A `.json` or `.csv` record that names a flagged
# file is not a tool reading it and not prose citing it, so it lands in the fourth bucket — outside
# the three kinds the ruling names — rather than being counted as a tool. Calling a data record a
# tool would inflate exactly the kind the user is most likely to read as a real dependency.
TOOL_EXTENSIONS = (".py", ".cpp", ".h", ".hpp", ".c", ".cc", ".cmake", ".bat", ".sh", ".ps1")
PROSE_EXTENSIONS = (".md", ".rst")
BUILD_FILE_NAMES = ("CMakeLists.txt",)

WRITE_MODE = re.compile(r"[wax]")


def locate_reading() -> dict[str, str]:
    """Every sentence of the ruled reading, LOCATED in the 2026-08-16 record. A missing one STOPS."""
    if not READING_RULING.exists():
        raise Stop(f"the ruling record for the reading is missing: {READING_RULING}")
    text = normalized(READING_RULING.read_text(encoding="utf-8"))
    missing = [name for name, quote in READING_SENTENCES.items() if normalized(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruled reading is no longer in its ruling record, so the "
                   f"reading would outlive the words that imposed it: {missing}")
    return dict(READING_SENTENCES)


# AUTHORED and published: the sentences of the CALLERS SITTING this run's four USER-RULED inputs
# are taken from, LOCATED in that record on every run — a ruling may not outlive its own words.
CALLERS_SENTENCES = {
    "the nine are ENUMERATOR-class":
        "All nine are ruled ENUMERATOR-class on the published evidence",
    "what their namings do":
        "Their namings are published as data and hold nothing.",
    "a prose citation":
        "The 356 prose-citation namings stay published; they hold nothing.",
    "the fourth bucket":
        "hold nothing, on the same ground as §2 and more strongly",
    "what continues to hold":
        "A tool reading the file by name, and a mandatory-read or boot listing, HOLD under every "
        "part of this sitting",
    "what it does not license":
        "A future caller the derivation cannot place still STOPS to the user; nothing here creates "
        "a precedent for guessing.",
}


def locate_callers_ruling() -> dict[str, str]:
    """Every sentence of the callers sitting, LOCATED in its record. A missing one STOPS."""
    if not CALLERS_RULING.exists():
        raise Stop(f"the callers sitting's ruling record is missing: {CALLERS_RULING}")
    text = normalized(CALLERS_RULING.read_text(encoding="utf-8"))
    missing = [name for name, quote in CALLERS_SENTENCES.items() if normalized(quote) not in text]
    if missing:
        raise Stop("a sentence of the callers sitting is no longer in its ruling record, so this "
                   f"run's ruled inputs would outlive the words that imposed them: {missing}")
    return dict(CALLERS_SENTENCES)


def user_ruled_enumerators() -> tuple[set[str], list[dict]]:
    """The nine callers §1 rules ENUMERATOR-class — DERIVED from the evidence, never typed here.

    ★ WHERE THE MEMBERSHIP COMES FROM, and why it is not a list in this file. The sitting was held
    at the census's own published KIND-UNDERIVABLE population, read by the writing side at the git
    object of the commit that carries that reading. So the membership IS that list, taken from the
    same object; nothing is retyped and nothing is matched by hand.

    ★ AND THE RECORD IS ASKED TO AGREE. Each derived caller's base name is then LOCATED in the
    sitting record itself. A derived set the record does not describe halts this tool instead of
    ruling on a population the user never saw — which is the same shape every other ruled input
    here carries, applied to a membership rather than to a sentence.
    """
    raw = git("show", f"{CALLERS_RULING_EVIDENCE_COMMIT}:tools/audit/retirement_caller_check.json")
    if not raw.strip():
        raise Stop("the census reading the callers sitting was held over is not in the tree at "
                   f"{CALLERS_RULING_EVIDENCE_COMMIT[:10]} — §1's population cannot be derived")
    evidence = json.loads(raw)
    listed = evidence["★_the_caller_kind_classification"][
        "★_the_KIND_UNDERIVABLE_list_returning_to_the_user"]["callers"]
    if not listed:
        raise Stop("the census reading the sitting was held over carries no KIND-UNDERIVABLE "
                   "caller, so §1 would rule on an empty population")

    record = CALLERS_RULING.read_text(encoding="utf-8")
    rows, absent = [], []
    for entry in listed:
        path = entry["caller"]
        base = posixpath.basename(path)
        if base not in record:
            absent.append(path)
            continue
        rows.append({
            "caller": path,
            "how_the_kind_was_settled": USER_RULED,
            "the_ruling": "cowork_rulings_2026_08_17_callers_sitting.md §1",
            "the_reason_the_derivation_published_when_the_sitting_read_it": entry["why"],
            "located_in_the_sitting_record_by": base,
        })
    if absent:
        raise Stop(f"the derived §1 population names {absent}, which the callers sitting's own "
                   f"record does not describe — the derivation and the ruling have drifted apart, "
                   f"and this tool does not rule on a population the user never saw")
    return {r["caller"] for r in rows}, rows


def _norm_path(value: str) -> str:
    """A repository-relative POSIX path with `.` and `..` segments resolved. ROOT is the empty string."""
    parts: list[str] = []
    for segment in value.replace("\\", "/").split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if parts:
                parts.pop()
            continue
        parts.append(segment)
    return "/".join(parts)


class SourceFacts:
    """One tracked Python source, parsed: what it writes, what it reads, what it imports.

    Nothing here is hand-listed. The write and read sites are found in the syntax tree, and each
    site's path expression is RESOLVED to a repository-relative path by evaluating the constants
    and the name chain it is built from — so `open(os.path.join(OUTDIR, "x.json"), "w")` resolves
    to the file it actually writes rather than to a base name that some other file might share.
    """

    def __init__(self, path: str, source: str) -> None:
        self.path = path
        self.text = source
        self.parsed = False
        self.parse_error = ""
        self.names: dict[str, str] = {}
        self.writes: set[str] = set()
        self.reads: set[str] = set()
        self.unresolved_write_literals: set[str] = set()
        self.imports: set[str] = set()
        self.enumeration_evidence: list[dict] = []
        try:
            # A warning raised by ANOTHER file's source is not this tool's finding, and letting it
            # reach the output would put a third party's escape sequence in a guard's captured text.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                tree = ast.parse(source)
        except (SyntaxError, ValueError) as exc:      # a Python 2 file, or a broken one
            self.parse_error = f"{type(exc).__name__}: {exc}"
            return
        self.parsed = True
        self._resolve_module_names(tree)
        self._collect_imports(tree)
        self._collect_sites(tree)
        self._find_enumeration(tree)

    # ---- the path-expression evaluator ---------------------------------------------------------
    def _eval(self, node, params: dict[str, str] | None = None) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            if node.id == "__file__":
                return self.path
            if params and node.id in params:
                return params[node.id]
            return self.names.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            left = self._eval(node.left, params)
            right = self._eval(node.right, params)
            if left is None or right is None:
                return None
            return _norm_path(left + "/" + right)
        if isinstance(node, ast.Attribute):
            if node.attr == "parent":
                inner = self._eval(node.value, params)
                return None if inner is None else _norm_path(inner + "/..")
            if node.attr in ("resolve", "absolute", "expanduser"):
                return self._eval(node.value, params)
            return None
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in ("Path", "str"):
                return self._eval(node.args[0], params) if node.args else None
            if isinstance(func, ast.Attribute):
                if func.attr in ("resolve", "absolute", "expanduser"):
                    return self._eval(func.value, params)
                if func.attr == "join":
                    joined: list[str] = []
                    for arg in node.args:
                        piece = self._eval(arg, params)
                        if piece is None:
                            return None
                        joined.append(piece)
                    return _norm_path("/".join(joined))
                if func.attr in ("abspath", "realpath", "normpath"):
                    return self._eval(node.args[0], params) if node.args else None
                if func.attr == "dirname":
                    inner = self._eval(node.args[0], params) if node.args else None
                    return None if inner is None else _norm_path(inner + "/..")
        return None

    def _resolve_module_names(self, tree: ast.Module) -> None:
        for statement in tree.body:
            if not isinstance(statement, ast.Assign) or len(statement.targets) != 1:
                continue
            target = statement.targets[0]
            if not isinstance(target, ast.Name):
                continue
            value = self._eval(statement.value)
            if value is not None:
                self.names[target.id] = value

    def _collect_imports(self, tree: ast.Module) -> None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                self.imports.add(node.module.split(".")[0])

    @staticmethod
    def _is_write_open(call: ast.Call) -> bool:
        mode = None
        if len(call.args) >= 2 and isinstance(call.args[1], ast.Constant):
            mode = call.args[1].value
        for keyword in call.keywords:
            if keyword.arg == "mode" and isinstance(keyword.value, ast.Constant):
                mode = keyword.value.value
        return isinstance(mode, str) and bool(WRITE_MODE.search(mode))

    @staticmethod
    def _is_read_open(call: ast.Call) -> bool:
        mode = None
        if len(call.args) >= 2 and isinstance(call.args[1], ast.Constant):
            mode = call.args[1].value
        for keyword in call.keywords:
            if keyword.arg == "mode" and isinstance(keyword.value, ast.Constant):
                mode = keyword.value.value
        if mode is None:
            return True
        return isinstance(mode, str) and not WRITE_MODE.search(mode)

    def _site_targets(self, tree, params: dict[str, str] | None = None):
        """Yield (kind, target-node) for every write or read site in `tree`."""
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if isinstance(func, ast.Name) and func.id == "open" and node.args:
                yield ("write" if self._is_write_open(node) else
                       "read" if self._is_read_open(node) else "read"), node.args[0]
            elif isinstance(func, ast.Attribute):
                if func.attr in ("write_text", "write_bytes"):
                    yield "write", func.value
                elif func.attr in ("read_text", "read_bytes"):
                    yield "read", func.value

    def _writing_helpers(self, tree: ast.Module) -> dict[str, set[int]]:
        """A function in this module that writes one of its own parameters, and which one.

        One level only, and stated as a bound rather than left implicit: a write reached through
        two helpers is not found, and the caller it would have produced therefore keeps holding.
        """
        helpers: dict[str, set[int]] = {}
        for statement in ast.walk(tree):
            if not isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            names = [a.arg for a in statement.args.args]
            indices = set()
            for kind, target in self._site_targets(statement):
                if kind == "write" and isinstance(target, ast.Name) and target.id in names:
                    indices.add(names.index(target.id))
            if indices:
                helpers[statement.name] = indices
        return helpers

    def _collect_sites(self, tree: ast.Module) -> None:
        helpers = self._writing_helpers(tree)
        for kind, target in self._site_targets(tree):
            resolved = self._eval(target)
            if resolved is None:
                if kind == "write":
                    for inner in ast.walk(target):
                        if isinstance(inner, ast.Constant) and isinstance(inner.value, str):
                            self.unresolved_write_literals.add(inner.value)
                continue
            (self.writes if kind == "write" else self.reads).add(_norm_path(resolved))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            for index in helpers.get(node.func.id, ()):
                if index >= len(node.args):
                    continue
                resolved = self._eval(node.args[index])
                if resolved is None:
                    for inner in ast.walk(node.args[index]):
                        if isinstance(inner, ast.Constant) and isinstance(inner.value, str):
                            self.unresolved_write_literals.add(inner.value)
                else:
                    self.writes.add(_norm_path(resolved))

    @staticmethod
    def _shallow_constants(node) -> list[str]:
        """The string constants of an expression, one level into a list or a tuple."""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return [node.value]
        if isinstance(node, (ast.List, ast.Tuple)):
            return [e.value for e in node.elts
                    if isinstance(e, ast.Constant) and isinstance(e.value, str)]
        return []

    def _git_argument_constants(self, tree: ast.Module) -> set[str]:
        """Every string constant this source hands to git as an argument."""
        found: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = (node.func.id if isinstance(node.func, ast.Name)
                        else node.func.attr if isinstance(node.func, ast.Attribute) else "")
                consts: list[str] = []
                for arg in node.args:
                    consts.extend(self._shallow_constants(arg))
                if name.lower().rstrip("_").endswith("git") or "git" in consts:
                    found.update(consts)
            elif isinstance(node, (ast.List, ast.Tuple)):
                consts = [e.value for e in node.elts
                          if isinstance(e, ast.Constant) and isinstance(e.value, str)]
                if "git" in consts:
                    found.update(consts)
        return found

    def _find_enumeration(self, tree: ast.Module) -> None:
        every = {c.value for c in ast.walk(tree)
                 if isinstance(c, ast.Constant) and isinstance(c.value, str)}
        as_git_argument = self._git_argument_constants(tree)
        for constant in sorted(every):
            label = STRONG_ENUMERATION_CONSTANTS.get(constant)
            if label is None and constant.startswith(PORCELAIN_PREFIX):
                label = PORCELAIN_LABEL
            if label is None:
                continue
            self.enumeration_evidence.append(
                {"signal": label, "the_string_constant_it_was_found_as": constant})
        for constant in sorted(as_git_argument):
            label = GIT_CONTEXT_CONSTANTS.get(constant)
            if label:
                self.enumeration_evidence.append(
                    {"signal": label,
                     "the_string_constant_it_was_found_as": constant,
                     "and_it_counted_because": "the source hands it to git as an argument"})


def parse_python_sources(commit: str, paths: list[str]) -> dict[str, SourceFacts]:
    """Every tracked `*.py` at `commit`, parsed. Read from the git objects in one batch."""
    sources = [p for p in paths if p.endswith(".py")]
    facts: dict[str, SourceFacts] = {}
    if not sources:
        return facts
    request = "".join(f"{commit}:{p}\n" for p in sources).encode("utf-8")
    proc = subprocess.run(["git", "-C", str(ROOT), "-c", "core.quotepath=false",
                           "cat-file", "--batch"],
                          input=request, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop("git cat-file --batch failed while reading the Python sources: "
                   + proc.stderr.decode("utf-8", "replace").strip())
    stream, offset = proc.stdout, 0
    for path in sources:
        end = stream.index(b"\n", offset)
        header = stream[offset:end].decode("utf-8", "replace").split()
        if len(header) != 3 or header[1] != "blob":
            raise Stop(f"git cat-file returned an unexpected header for {path!r}: {header}")
        size = int(header[2])
        body = stream[end + 1:end + 1 + size].decode("utf-8", "replace")
        offset = end + 1 + size + 1
        facts[path] = SourceFacts(path, body)
    return facts


def generator_status(facts: dict[str, SourceFacts]) -> tuple[dict[str, dict], dict[str, dict],
                                                             dict[str, set[str]]]:
    """Which generators ENUMERATE THE TRACKED TREE, which merely TOUCH an enumeration, and who
    writes what.

    ★ THE LINE BETWEEN THE TWO IS WHERE THIS DERIVATION IS HONEST OR NOT, so it is drawn here and
    stated rather than buried. A generator whose OWN SOURCE calls a tracked-tree enumeration
    produces a record that names paths because they exist — established. A generator that merely
    IMPORTS such a module, or READS an artifact one produced, may be passing the enumeration
    through into its own output or may be consuming it for something else entirely, and NOTHING IN
    THE SOURCE SEPARATES THOSE TWO. The first run of this derivation treated the second as the
    first, and the visible consequence was that the decisions register's own AUTHORED data file was
    classified as a tree enumeration, because three tools that edit fields inside it read an
    enumeration somewhere. So the weaker relation establishes nothing: it makes the caller
    KIND-UNDERIVABLE, which is what the ruling itself requires of a kind that cannot be derived.

    Returns (enumerating, ambiguous, written_by).
    """
    written_by: dict[str, set[str]] = {}
    for path, fact in facts.items():
        for produced in fact.writes:
            written_by.setdefault(produced, set()).add(path)

    by_module: dict[str, set[str]] = {}
    for path in facts:
        by_module.setdefault(posixpath.basename(path)[:-3], set()).add(path)

    enumerating: dict[str, dict] = {}
    for path, fact in facts.items():
        if fact.enumeration_evidence:
            enumerating[path] = {"route": "its own source enumerates the tracked tree",
                                 "evidence": fact.enumeration_evidence}

    ambiguous: dict[str, dict] = {}
    for path, fact in facts.items():
        if path in enumerating:
            continue
        here = posixpath.dirname(path)
        for module in sorted(fact.imports):
            for sibling in sorted(p for p in by_module.get(module, ())
                                  if posixpath.dirname(p) == here):
                if sibling in enumerating:
                    ambiguous[path] = {
                        "relation": f"it imports `{module}` ({sibling}), which enumerates the "
                                    f"tree, and nothing in the source establishes whether the "
                                    f"enumeration reaches its own output"}
                    break
            if path in ambiguous:
                break
        if path in ambiguous:
            continue
        for consumed in sorted(fact.reads):
            for producer in sorted(written_by.get(consumed, ())):
                if producer in enumerating:
                    ambiguous[path] = {
                        "relation": f"it reads `{consumed}`, which {producer} produces from a tree "
                                    f"enumeration, and nothing in the source establishes whether "
                                    f"the enumeration passes through into its own output"}
                    break
            if path in ambiguous:
                break
    return enumerating, ambiguous, written_by


def producers_of(path: str, facts: dict[str, SourceFacts], declared: list[dict],
                 tracked: set[str]) -> tuple[list[dict], list[str]]:
    """LINK 1 — the generators established for one caller, and what could not be resolved.

    ★ A SELF-REFERENCE IS NOT A DECLARATION, and the exclusion is the second thing the first run of
    this derivation got wrong. A generator's own source contains the very field literal it writes
    into its artifact — `"generated_by": "tools/audit/gen_x.py"` sits inside `gen_x.py` — so a
    generator read as declaring ITSELF became a generated artifact, and three measurement tools
    were classified as tree enumerations. A file naming itself says nothing about who produced it.
    """
    producers: list[dict] = []
    unresolved: list[str] = []
    for record in declared:
        target = _norm_path(record["generator"])
        if target == path:
            continue
        if target in tracked:
            producers.append({"generator": target,
                              "link": "route A — the caller's own text declares it",
                              "evidence": record["quoted"]})
        else:
            unresolved.append(f"the caller declares the generator {record['generator']!r}, which "
                              f"the tree does not carry at the measured commit")
    for source_path, fact in sorted(facts.items()):
        if path in fact.writes and source_path != path:
            producers.append({"generator": source_path,
                              "link": "route B — this tracked Python source writes the caller's "
                                      "path, resolved from its own write site",
                              "evidence": f"a write site in {source_path} resolves to {path}"})
    return producers, unresolved


def classify_caller(path: str, facts: dict[str, SourceFacts], enumerating: dict[str, dict],
                    ambiguous: dict[str, dict], declared: list[dict], rendered_from: list[dict],
                    tracked: set[str], enumerator_artifacts: set[str],
                    ruled_enumerators: set[str]) -> dict:
    """ONE caller's kind, with the evidence for each link. Exactly one kind, never a default."""
    base = posixpath.basename(path)
    producers, unresolved = producers_of(path, facts, declared, tracked)

    # ★ THE USER-RULED INPUT COMES FIRST, AND IT IS MARKED AS ONE. §1 of the callers sitting ruled
    # the nine callers this derivation could not place ENUMERATOR-class at their published reasons.
    # It is a RULING over a named population, not a rule this tool derives, so the verdict carries
    # `how_the_kind_was_settled` and every derived verdict carries it too — a reader can tell which
    # is which without reading this file. It reaches those nine and no others: a caller the
    # derivation cannot place TODAY still returns to the user, which §1 says in terms.
    if path in ruled_enumerators:
        return {"caller_kind": KIND_ENUMERATOR,
                "how_the_kind_was_settled": USER_RULED,
                "producers": producers,
                "why": "USER-RULED at the 2026-08-17 callers sitting (§1): the derivation could "
                       "not place this caller, the reason it published was put to the user with "
                       "the eight others, and the user ruled all nine ENUMERATOR-class on that "
                       "published evidence — five produced by generators consuming a "
                       "tree-enumeration product, four named as write targets by enumerating "
                       "generators through paths the parser could not resolve. Its namings are "
                       "published as data and hold nothing.",
                "holds": False}

    established = [p for p in producers if p["generator"] in enumerating]
    if established:
        return {"caller_kind": KIND_ENUMERATOR, "how_the_kind_was_settled": DERIVED_KIND,
                "producers": producers,
                "why": "its generator enumerates the tracked tree, so it names paths because they "
                       "exist rather than because anyone chose them: "
                       + "; ".join(f"{p['generator']} — {enumerating[p['generator']]['route']}"
                                   for p in established),
                "how_the_generator_enumerates": [
                    {"generator": p["generator"], **enumerating[p["generator"]]}
                    for p in established],
                "holds": False}

    rendered = [r for r in rendered_from if _norm_path(r["source"]) in enumerator_artifacts]
    if rendered:
        return {"caller_kind": KIND_ENUMERATOR, "how_the_kind_was_settled": DERIVED_KIND,
                "producers": producers,
                "why": "it DECLARES ITSELF rendered from an artifact that is itself an "
                       "enumeration of the tracked tree — the ruling's *or a surface rendered from "
                       "one* limb, taken from the surface's own words: "
                       + "; ".join(r["source"] for r in rendered),
                "how_the_generator_enumerates": [
                    {"rendered_from": r["source"], "quoted": r["quoted"]} for r in rendered],
                "holds": False}

    touching = [p for p in producers if p["generator"] in ambiguous]
    if touching:
        unresolved += [f"{p['generator']} produces this caller and {ambiguous[p['generator']]['relation']}"
                       for p in touching]

    if not producers:
        for source_path, fact in sorted(facts.items()):
            if base in fact.unresolved_write_literals and source_path in enumerating:
                unresolved.append(
                    f"no producer resolved for this caller, but the enumerating generator "
                    f"{source_path} carries a write site naming {base!r} whose path could not be "
                    f"resolved — so it cannot be established that nothing produces it")

    if unresolved:
        return {"caller_kind": KIND_UNDERIVABLE, "how_the_kind_was_settled": DERIVED_KIND,
                "producers": producers,
                "why": "the derivation reached a producer relation it could not resolve, and the "
                       "ruling forbids guessing: " + "; ".join(sorted(set(unresolved))),
                "holds": True}

    if not producers:
        return {"caller_kind": KIND_NOT_GENERATED, "how_the_kind_was_settled": DERIVED_KIND,
                "producers": [],
                "why": "no tracked Python source writes this path and the caller declares no "
                       "generator, so the record's own machinery does not produce it",
                "holds": True}

    return {"caller_kind": KIND_GENERATED_NOT_ENUMERATING, "how_the_kind_was_settled": DERIVED_KIND,
            "producers": producers,
            "why": "a generator is established for it and no generator of it enumerates the "
                   "tracked tree, so its naming carries information about a dependency",
            "holds": True}


def holder_kind(path: str, governing: set[str], governing_dirs: tuple[str, ...]) -> str:
    """WHICH of the ruling's three kinds a surviving holder is. Applied in this order."""
    base = posixpath.basename(path)
    if path in governing or path.split("/")[0] in governing_dirs:
        return HOLDER_MANDATORY
    if base in BUILD_FILE_NAMES or path.endswith(TOOL_EXTENSIONS):
        return HOLDER_TOOL
    if path.endswith(PROSE_EXTENSIONS):
        return HOLDER_PROSE
    return HOLDER_OTHER


def members_of(inv: dict, classes: dict, name: str) -> tuple[list[str], str]:
    """Every member path of a class, DERIVED — by two routes, neither of them a hand-list.

    ROUTE 1, used wherever it is available: the inventory PUBLISHES `every_member` for the classes
    the ruling surface descends into.

    ROUTE 2, for a flagged class the inventory does not descend into and therefore publishes no
    members for: apply the inventory's OWN published signature — imported from its generator, not
    restated — to the tree at the commit the inventory RECORDS, which is the tree its own class
    counts were taken at. The derived count is then cross-checked against the count the inventory
    publishes for that class, and a disagreement STOPS the tool, so the second route cannot quietly
    produce a different population from the one the ruling classified.

    ★ WHY ROUTE 2 IS NOT HAND-LISTING, which the dispatch forbids: no path is typed here. The rule
    that produces the list is the one the inventory published and the user's ruling was taken over.
    """
    published = classes[name].get("every_member")
    if published:
        return sorted(m["path"] for m in published), "published by the inventory as `every_member`"

    at = inv["derived_at_commit"]
    derived = sorted(p for p in tree_paths(at) if inventory_tool.classify(p)[0] == name)
    expected = classes[name]["files"]
    if len(derived) != expected:
        raise Stop(f"the member list derived for {name!r} by the inventory's own signature at its "
                   f"own commit holds {len(derived)} files where the inventory publishes "
                   f"{expected} — the two disagree, so the population cannot be taken")
    return derived, ("derived by applying the inventory's own published signature to the tree at "
                     f"the commit it records ({at}), because the inventory publishes no member "
                     f"list for this class; the derived count was cross-checked against the "
                     f"{expected} files the inventory reports for it")


def candidacies(inv: dict) -> dict[str, dict]:
    """The flagged population, IMPORTED from the ruling surface's own authored flags (#6)."""
    classes = {c["class"]: c for c in inv["the_classes"]}

    whole = [n for n, e in surface.PROPOSALS.items() if e.get("retirement_candidate") is True]
    partly = {n: [side for side, e in sides.items() if e.get("retirement_candidate")]
              for n, sides in surface.SPLIT_PROPOSALS.items()
              if any(e.get("retirement_candidate") for e in sides.values())}

    for name in whole + list(partly):
        if name not in classes:
            raise Stop(f"a flagged class is not in the committed inventory: {name!r}")
    for name in partly:
        if not classes[name].get("every_member"):
            raise Stop(f"the inventory publishes no members for the mixed class {name!r}, so its "
                       f"citation split cannot be taken and nothing here is hand-listed")

    text, _sources = surface.governing_text()
    names = surface.cited_names(text)

    out: dict[str, dict] = {}
    for name in whole:
        members, how = members_of(inv, classes, name)
        out[name] = {
            "flagged": "the whole class",
            "how_the_member_list_was_derived": how,
            "members": members,
        }
    for name, sides in partly.items():
        members = []
        for member in classes[name]["every_member"]:
            base = posixpath.basename(member["path"])
            side = "cited" if base in names else "uncited"
            if side in sides:
                members.append(member["path"])
        out[name] = {
            "flagged": "the " + " and ".join(sorted(sides)) + " side of the citation split",
            "how_the_member_list_was_derived":
                "published by the inventory as `every_member`, then split by the citation scan "
                "re-run at the governing record — the same scan the ruling surface splits by (#6)",
            "members": sorted(members),
        }

    authored = set(CONDITIONS)
    derived = set(out)
    if authored != derived:
        raise Stop("the authored condition records and the derived candidacies disagree. "
                   f"Derived with no condition record: {sorted(derived - authored)}. "
                   f"Condition records naming no derived candidacy: {sorted(authored - derived)}")
    return out


def class_of_every_path(inv: dict) -> dict[str, str]:
    """Which class each member path belongs to, for the same-class exclusion."""
    owner = {}
    for c in inv["the_classes"]:
        for member in c.get("every_member", []):
            owner[member["path"]] = c["class"]
    return owner


def naming_files(commit: str, bases: set[str]) -> list[str]:
    """Every tracked path at `commit` whose text contains one of the candidate base names.

    One `git grep` over the whole tree: `-F` takes the names as fixed strings, `-I` skips binary
    blobs, `--name-only` returns paths rather than matched lines (a matched line in a generated
    artifact can be megabytes long, and the attribution is taken by re-reading the file anyway).
    """
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                     encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sorted(bases)) + "\n")
        pattern_file = fh.name
    try:
        listed = git("grep", "-I", "-F", "--name-only", "-f", pattern_file, commit)
    finally:
        Path(pattern_file).unlink(missing_ok=True)

    prefix = commit + ":"
    paths = []
    for line in listed.splitlines():
        if not line.strip():
            continue
        paths.append(line[len(prefix):] if line.startswith(prefix) else line)
    return sorted(set(paths))


def references(commit: str, bases: set[str]) -> tuple[dict[str, set[str]],
                                                      dict[tuple[str, str], str],
                                                      dict[str, list[dict]],
                                                      dict[str, list[dict]]]:
    """Every tracked file at `commit` whose text names one of `bases`, mapped base -> paths.

    The naming files are read back through ONE `git cat-file --batch` rather than one process per
    file, so the attribution is exact — each file's whole text is scanned for file-name-shaped
    tokens — without paying a subprocess per naming file.

    Two further things are taken from the same pass, so no file is read twice: the LINE each naming
    was first found on, which is the evidence the ruled reading requires beside every surviving
    holder; and any GENERATOR the file declares for itself, which is route A of the kind
    derivation.
    """
    paths = naming_files(commit, bases)
    hits: dict[str, set[str]] = {b: set() for b in bases}
    evidence: dict[tuple[str, str], str] = {}
    declarations: dict[str, list[dict]] = {}
    rendered: dict[str, list[dict]] = {}
    if not paths:
        return hits, evidence, declarations, rendered

    request = "".join(f"{commit}:{p}\n" for p in paths).encode("utf-8")
    proc = subprocess.run(["git", "-C", str(ROOT), "-c", "core.quotepath=false",
                           "cat-file", "--batch"],
                          input=request, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop("git cat-file --batch failed: "
                   + proc.stderr.decode("utf-8", "replace").strip())

    stream, offset = proc.stdout, 0
    for path in paths:
        end = stream.index(b"\n", offset)
        header = stream[offset:end].decode("utf-8", "replace").split()
        if len(header) != 3 or header[1] != "blob":
            raise Stop(f"git cat-file returned an unexpected header for {path!r}: {header}")
        size = int(header[2])
        body = stream[end + 1:end + 1 + size].decode("utf-8", "replace")
        offset = end + 1 + size + 1          # the trailing newline git writes after each object
        for line in body.splitlines():
            for match in NAME_TOKEN.finditer(line):
                token = match.group(0)
                if token not in hits:
                    continue
                hits[token].add(path)
                if (token, path) in evidence:
                    continue
                # The window is centred on the NAMING rather than cut from the start of the line:
                # a generated record's lines run to thousands of characters, and a fragment that
                # stops before the name it is evidence for is not evidence.
                start, end = max(0, match.start() - 90), min(len(line), match.end() + 90)
                evidence[(token, path)] = (("..." if start else "") + line[start:end].strip()
                                           + ("..." if end < len(line) else ""))
        for label, pattern in DECLARATION_KEYS:
            match = pattern.search(body)
            if match:
                declarations.setdefault(path, []).append(
                    {"declaration": label, "generator": match.group(1),
                     "quoted": " ".join(match.group(0).split())[:240]})
        match = RENDERED_FROM.search(body)
        if match:
            rendered.setdefault(path, []).append(
                {"source": match.group(1), "quoted": " ".join(match.group(0).split())[:240]})
    return hits, evidence, declarations, rendered


def build(commit: str) -> dict:
    inv_path = ROOT / "tools" / "audit" / "artifact_inventory.json"
    if not inv_path.exists():
        raise Stop(f"the committed artifact inventory is missing: {inv_path}")
    inv = json.loads(inv_path.read_text(encoding="utf-8"))

    quotes = locate_conditions()
    reading = locate_reading()
    callers_ruling = locate_callers_ruling()
    ruled_enumerator_rows_all: list[dict]
    ruled_enumerators, ruled_enumerator_rows_all = user_ruled_enumerators()
    population = candidacies(inv)
    owner = class_of_every_path(inv)

    every_member = {p for c in population.values() for p in c["members"]}
    bases = {posixpath.basename(p) for p in every_member}
    hits, evidence, declarations, rendered_from = references(commit, bases)

    # ── the ruled reading's kind derivation, over exactly the callers this run found ─────────────
    tracked = set(tree_paths(commit))
    facts = parse_python_sources(commit, sorted(tracked))
    enumerating, ambiguous, written_by = generator_status(facts)
    enumerator_artifacts = {a for p in enumerating for a in facts[p].writes}
    governing = set(surface.GOVERNING_DOCUMENTS)
    governing_dirs = tuple(surface.GOVERNING_DIRECTORIES)

    # A base name shared by several tracked paths makes every naming of it ambiguous, because the
    # reference test is a base-name match by design. Measured per member rather than left as a
    # caveat, so a reader can tell an ambiguous holding from a definite one.
    base_counts: dict[str, int] = {}
    for tracked_path in tracked:
        key = posixpath.basename(tracked_path)
        base_counts[key] = base_counts.get(key, 0) + 1

    callers_found = sorted({p for base in bases for p in hits.get(base, set())})
    kinds = {path: classify_caller(path, facts, enumerating, ambiguous,
                                   declarations.get(path, []), rendered_from.get(path, []),
                                   tracked, enumerator_artifacts, ruled_enumerators)
             for path in callers_found}
    # The ruled nine, restricted to the callers this run actually found. A ruled caller the scan no
    # longer sees is published rather than dropped, so the ruling's reach stays readable (#12).
    ruled_enumerator_rows = [r for r in ruled_enumerator_rows_all if r["caller"] in kinds]
    ruled_but_not_found = [r["caller"] for r in ruled_enumerator_rows_all if r["caller"] not in kinds]
    unknown_kind = sorted(k["caller_kind"] for k in kinds.values()
                          if k["caller_kind"] not in CALLER_KINDS)
    if unknown_kind:
        raise Stop(f"a caller reached a kind outside the closed vocabulary: {sorted(set(unknown_kind))}")

    rows = []
    for name in sorted(population):
        condition, _quote = CONDITIONS[name]
        members, held, internal_only = [], [], []
        for path in population[name]["members"]:
            base = posixpath.basename(path)
            found = sorted(hits.get(base, set()) - {path})
            inside = [p for p in found if owner.get(p) == name]
            remainder = [p for p in found if owner.get(p) != name]
            fellow = [p for p in remainder if p in every_member]
            outside = [p for p in remainder if p not in every_member]
            enumerator_namings = [p for p in outside
                                  if kinds[p]["caller_kind"] == KIND_ENUMERATOR]
            by_kind = [p for p in outside if kinds[p]["caller_kind"] in KINDS_THAT_HOLD]
            # ★ THE SECOND FILTER IS THE CALLERS SITTING'S §§2-4, AND IT IS A RULED INPUT.
            # Surviving the caller-kind derivation is no longer enough: of the four HOLDER kinds
            # the ruling's own vocabulary carries, exactly two HOLD — a tool reading the file by
            # name, and a mandatory-read or boot listing. A prose citation and a naming outside
            # those three kinds stay PUBLISHED and hold nothing.
            holders = [p for p in by_kind
                       if holder_kind(p, governing, governing_dirs) in HOLDER_KINDS_THAT_HOLD]
            not_holding_by_holder_kind = [p for p in by_kind if p not in holders]
            members.append({
                "path": path,
                "its_base_name_is_unique_in_the_tracked_tree": base_counts[base] == 1,
                "holding_callers": [
                    {"caller": p,
                     "caller_kind": kinds[p]["caller_kind"],
                     "how_the_caller_kind_was_settled": kinds[p]["how_the_kind_was_settled"],
                     "why_this_kind": kinds[p]["why"],
                     "holder_kind": holder_kind(p, governing, governing_dirs),
                     "why_this_holder_kind_HOLDS": USER_RULED + " (§4): a tool reading the file by "
                                                   "name, and a mandatory-read or boot listing, "
                                                   "HOLD — each breaks in fact when the file moves",
                     "the_line_the_naming_was_found_on": evidence.get((base, p), "")}
                    for p in holders],
                "namings_whose_HOLDER_KIND_was_ruled_to_hold_nothing_published_not_dropped": [
                    {"caller": p,
                     "caller_kind": kinds[p]["caller_kind"],
                     "holder_kind": holder_kind(p, governing, governing_dirs),
                     "why_it_holds_nothing": USER_RULED
                     + (" (§2): archive-with-record keeps every citation resolvable — the dated "
                        "pointer takes a reader to the moved target — and the prose-naming "
                        "population moves with the record's layout rather than with any dependency "
                        "(finding F35, measured twice in both directions)"
                        if holder_kind(p, governing, governing_dirs) == HOLDER_PROSE else
                        " (§3): a data record that names a flagged file without reading it as a "
                        "tool and without citing it as prose holds nothing, on the same ground as "
                        "§2 and more strongly — such namings are overwhelmingly enumeration "
                        "echoes"),
                     "the_line_the_naming_was_found_on": evidence.get((base, p), "")}
                    for p in not_holding_by_holder_kind],
                "enumerator_namings_published_as_data_holding_nothing": [
                    {"caller": p,
                     "how_the_caller_kind_was_settled": kinds[p]["how_the_kind_was_settled"],
                     "how_its_generator_enumerates": kinds[p].get(
                         "how_the_generator_enumerates", []),
                     "the_line_the_naming_was_found_on": evidence.get((base, p), "")}
                    for p in enumerator_namings],
                "namings_from_fellow_flagged_files_set_aside_not_dropped": fellow,
                "references_from_inside_its_own_class_set_aside_not_dropped": inside,
                "member_verdict": HELD_CALLERS if holders else PASSES,
            })
            if holders:
                held.append(path)
            elif inside or fellow or enumerator_namings or not_holding_by_holder_kind:
                internal_only.append(path)

        if held:
            verdict = HELD_CALLERS
            ground = ("at least one member is named at the measured commit by a caller that HOLDS "
                      "under the ruled reading AND under the callers sitting's ruled holder kinds "
                      "— a caller outside its own class, not a fellow flagged file, not an "
                      "enumerator, and reading the file as a tool or listing it as a mandatory "
                      "read; each is listed per member with its kind, its holder kind and the "
                      "line the naming was found on")
        elif condition != NO_CONDITION:
            verdict = HELD_CONDITION
            ground = ("no member is named from outside its own class at the measured commit, and "
                      f"a ruled condition still stands: {condition}")
        else:
            verdict = PASSES
            ground = ("no member is held by a caller at the measured commit under the ruled "
                      "reading, and the ruling attaches no further condition. IT CONFERS NOTHING: "
                      "archiving is a later dispatch's act")

        if verdict not in VERDICTS:
            raise Stop(f"candidacy {name!r} reached a verdict outside the closed vocabulary")

        rows.append({
            "candidacy": name,
            "what_is_flagged": population[name]["flagged"],
            "how_the_member_list_was_derived": population[name]["how_the_member_list_was_derived"],
            "members_flagged": len(population[name]["members"]),
            "ruled_condition": condition,
            "the_ruling_sentence_it_was_read_from": quotes[name],
            "verdict": verdict,
            "why_this_verdict": ground,
            "members_held_by_callers": sorted(held),
            "members_whose_every_naming_was_set_aside_or_published_as_data":
                sorted(internal_only),
            "members_with_no_naming_found_anywhere":
                sorted(m["path"] for m in members
                       if not m["holding_callers"]
                       and not m[
                           "namings_whose_HOLDER_KIND_was_ruled_to_hold_nothing_published_not_dropped"]
                       and not m["enumerator_namings_published_as_data_holding_nothing"]
                       and not m["namings_from_fellow_flagged_files_set_aside_not_dropped"]
                       and not m["references_from_inside_its_own_class_set_aside_not_dropped"]),
            "every_member": members,
        })

    if len(rows) != len(population):
        raise Stop("a candidacy reached no verdict")
    tally = {v: sum(1 for r in rows if r["verdict"] == v) for v in VERDICTS}
    if sum(tally.values()) != len(rows):
        raise Stop("the verdict tally does not account for the candidacies")

    # WHO DOES THE NAMING — derived, and the reason it is published is in the artifact below. A
    # caller naming a large share of the flagged population is enumerating the tree rather than
    # depending on any file in it, and that is visible here as a count instead of being decided by
    # a threshold nobody ruled.
    naming: dict[str, int] = {}
    for name in population:
        for member in population[name]["members"]:
            for caller in hits.get(posixpath.basename(member), set()) - {member}:
                naming[caller] = naming.get(caller, 0) + 1
    flagged_total = sum(len(c["members"]) for c in population.values())
    who = [{"caller": c,
            "caller_kind": kinds[c]["caller_kind"],
            "how_the_caller_kind_was_settled": kinds[c]["how_the_kind_was_settled"],
            "holder_kind_if_it_holds": (holder_kind(c, governing, governing_dirs)
                                        if kinds[c]["caller_kind"] in KINDS_THAT_HOLD else None),
            "it_holds": (kinds[c]["caller_kind"] in KINDS_THAT_HOLD
                         and holder_kind(c, governing, governing_dirs)
                         in HOLDER_KINDS_THAT_HOLD),
            "flagged_files_it_names": n,
            "share_of_the_flagged_population": round(n / flagged_total, 4),
            "why_this_kind": kinds[c]["why"],
            "producers_found": kinds[c]["producers"]}
           for c, n in sorted(naming.items(), key=lambda kv: (-kv[1], kv[0]))]

    kind_tally = {k: sum(1 for v in kinds.values() if v["caller_kind"] == k)
                  for k in CALLER_KINDS}
    if sum(kind_tally.values()) != len(kinds):
        raise Stop("the caller-kind tally does not account for the callers found")
    underivable = sorted(p for p, v in kinds.items() if v["caller_kind"] == KIND_UNDERIVABLE)
    holder_tally: dict[str, int] = {k: 0 for k in HOLDER_KINDS}
    holders_by_kind: dict[str, list[dict]] = {k: [] for k in HOLDER_KINDS}
    seen_holder: set[tuple[str, str]] = set()
    # ★ BOTH SIDES ARE TALLIED, and that is deliberate. The callers sitting decided which holder
    # kinds HOLD; it did not un-publish the others — its own words are that they stay published.
    # So every surviving naming of every kind is counted here with a `does_it_hold` bit, and the
    # per-member `holding_callers` field is where the ruling's effect is visible.
    NOTHING = "namings_whose_HOLDER_KIND_was_ruled_to_hold_nothing_published_not_dropped"
    for row in rows:
        for member in row["every_member"]:
            for entry in member["holding_callers"] + member[NOTHING]:
                key = (member["path"], entry["caller"])
                if key in seen_holder:
                    continue
                seen_holder.add(key)
                holder_tally[entry["holder_kind"]] += 1
                holders_by_kind[entry["holder_kind"]].append(
                    {"flagged_file": member["path"], "held_by": entry["caller"],
                     "caller_kind": entry["caller_kind"],
                     "does_it_hold": entry["holder_kind"] in HOLDER_KINDS_THAT_HOLD,
                     "the_line_the_naming_was_found_on":
                         entry["the_line_the_naming_was_found_on"]})
    unparsed = sorted(p for p, f in facts.items() if not f.parsed)
    shared_base = sorted(m["path"] for row in rows for m in row["every_member"]
                         if not m["its_base_name_is_unique_in_the_tracked_tree"])
    held_on_a_shared_base = sorted(m["path"] for row in rows for m in row["every_member"]
                                   if not m["its_base_name_is_unique_in_the_tracked_tree"]
                                   and m["holding_callers"])

    return {
        "what_this_is":
            "THE CALLER-CHECK AT THE OBJECTS, over every ruled retirement candidacy. For each "
            "flagged file it reports what still names it in the tracked tree at an explicit "
            "commit, the ruled condition still governing its archiving, and one verdict per "
            "candidacy. IT ARCHIVES, MOVES, RENAMES AND DELETES NOTHING, and a PASSES-THE-CHECK "
            "verdict confers nothing — archiving is a later dispatch's act, taken after this "
            "artifact is verified at the objects.",
        "generator": "tools/audit/gen_retirement_caller_check.py",
        "dispatch": "cc_instruction_preparation_eighth.md, Task 3 (the regeneration under the "
                    "2026-08-17 callers sitting's four ruled inputs); the RE-RUN under the "
                    "2026-08-16 ruled reading was cc_instruction_preparation_second.md, Task 1; "
                    "first run cc_instruction_preparation_opening.md, Task 3",
        "the_standing_warning_this_discharges": {
            "source": "cowork_rulings_2026_08_15_inventory_sitting.md §3.16",
            "quoted": "every flag is a CANDIDACY; retirement is archive-with-record, nothing "
                      "destroyed (#12); no archiving executes on the name-scan signal alone — the "
                      "caller-check at the objects comes first",
            "and_the_pruning_plan":
                "ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md §8: \"no "
                "archiving executes on the citation-scan signal alone — the caller-check at the "
                "objects precedes every wave.\"",
        },
        "measured_at_commit": commit,
        "★_why_the_commit_is_recorded_and_what_it_bounds":
            "The reading is a statement about the tracked tree AT THIS COMMIT and at no other. A "
            "later commit can add a caller, and this artifact will not know; its staleness bound "
            "is therefore explicit rather than implied. `--check` re-derives at this recorded "
            "commit, so the check passes indefinitely instead of going red the first time anybody "
            "writes a file naming a candidate — the OI-301/OI-305 shape avoided by construction. "
            "What stays LIVE is the population: the flags are re-imported from the ruling "
            "surface's generator on every run, and the citation split that decides which members "
            "of a mixed class are flagged is RE-SCANNED at the governing record as it stands — the "
            "same live property that generator's own check carries, so a document that starts or "
            "stops being cited moves side here too rather than staying where a dated reading put "
            "it.",
        "what_is_DERIVED": [
            "the candidacy population — the flagged classes and the flagged side of each split — "
            "imported from tools/audit/gen_artifact_inventory_surface.py's own authored flags, so "
            "this check and the ruling surface cannot disagree about what is flagged (#6)",
            "every member path, read from the committed artifact inventory and never hand-listed",
            "every reference, found in the tracked tree at the recorded commit",
            "every caller's KIND under the ruled reading, and the two links it is derived through",
            "every count and every verdict tally",
        ],
        "what_is_AUTHORED": [
            "the ruled condition per candidacy, each carrying the sentence of the ruling record it "
            "was read from — and every sentence is located in that record on every run",
            "which git subcommands count as enumerating the tracked tree, which spellings declare "
            "a generator, and which extensions make a holder a tool — each published in full "
            "beside the verdicts it produced",
        ],
        "★_what_a_reference_is_here_and_what_it_is_not": {
            "what_counts": "A file REFERENCES a candidate when its text at the measured commit "
                           "contains the candidate's base name. That covers an import, a path "
                           "written out and a tool reading a file by name — the three kinds the "
                           "dispatch names.",
            "deliberately_generous": "Erring toward finding a caller errs away from archiving "
                                     "something still in use, which is the safe direction for a "
                                     "candidacy nobody has ruled on.",
            "★_what_NONE_FOUND_does_not_mean":
                "A reference assembled at run time from pieces carries no literal to find, and a "
                "binary blob is not searched at all. NONE FOUND means no literal naming was found "
                "in text at this commit — never that nothing depends on the file.",
            "★_and_what_a_FOUND_naming_does_not_mean_where_the_base_name_is_shared":
                "The test is a base-name match, so a member whose base name several tracked paths "
                "share is named by every mention of any of them — a `README.md` inside a flagged "
                "directory is held by every sentence in the record that says README.md. Each "
                "member now carries `its_base_name_is_unique_in_the_tracked_tree`, measured "
                "against the whole tree at this commit, and the count of members with a shared "
                "base name is published below, so an ambiguous holding is visible instead of "
                "being a caveat somebody has to remember.",
            "same_class_references_are_set_aside_not_dropped":
                "The dispatch asks for references from OUTSIDE the candidate's own class, because "
                "a class retiring as a whole carries its internal cross-references with it. Every "
                "such reference is published in its own per-member field, so the exclusion can be "
                "checked rather than trusted (#12).",
            "fellow_flagged_references_are_set_aside_not_dropped":
                "Added by the ruled reading of 2026-08-16: a naming by ANOTHER flagged file, in "
                "any candidacy, is set aside into its own field on the same ground — files "
                "archived together keep resolving each other through the archive record. Every "
                "one stays published (#12).",
        },
        "the_verdict_vocabulary": {
            PASSES: "no member is named from outside its own class, and no ruled condition stands",
            HELD_CALLERS: "at least one member is named from outside its own class; each caller "
                          "is named per member",
            HELD_CONDITION: "no such caller, but a ruled condition still governs archiving",
            "★_the_order_the_three_are_applied_in_and_why":
                "callers first, condition second. A caller is a fact about the tree and a "
                "condition is an act somebody still owes; where both hold, the verdict names the "
                "fact and the condition is still published in the row beside it, so neither is "
                "lost.",
        },
        "the_tally": tally,
        "★_the_members_whose_base_name_the_tree_does_not_make_unique": {
            "why_it_matters": "The reference test is a base-name match by design, so a naming of a "
                              "shared base name may be about a different file entirely. A holding "
                              "that rests on one is not established the way a holding on a unique "
                              "base name is.",
            "members_with_a_shared_base_name": shared_base,
            "of_those_the_ones_this_run_reports_HELD": held_on_a_shared_base,
        },
        "★_the_ruled_reading_this_run_is_taken_under": {
            "authority": "cowork_rulings_2026_08_16_preparation_return.md §1 (the user's word: "
                         "\"A.\" — Alternative A, adopted whole)",
            "every_sentence_located_in_that_record_on_this_run": reading,
            "★_what_the_first_run_found_and_why_the_ruling_was_needed":
                "The first run returned every candidacy HELD-BY-CALLERS and reported that the "
                "naming was mostly done by records that name every path by construction — the "
                "artifact inventory itself, the ruling surface generated from it, the decision "
                "harvest, the file tables. Such a naming carries no information about whether "
                "anything DEPENDS on the file, which is what this check exists to establish. The "
                "question was returned undecided rather than settled by a session, because "
                "settling it would have meant an authored exemption list or a hand-picked "
                "threshold over varying data.",
            "what_the_ruling_changed_here":
                "A caller established as an ENUMERATOR has its namings published as data and holds "
                "nothing; a naming from a FELLOW FLAGGED FILE is set aside into its own field; a "
                "caller whose kind cannot be derived HOLDS and returns to the user; and every "
                "surviving holder is published BY KIND with the line its naming was found on.",
            "★_what_the_ruling_did_NOT_change":
                "Nothing is archived, moved, renamed or deleted by it, and a PASSES-THE-CHECK "
                "verdict still confers nothing — the pruning wave's own dispatch executes it "
                "later, with every ruled condition (mined-first; members-seen-by-the-user-first) "
                "intact.",
        },
        "★_the_caller_kind_classification": {
            "what_is_DERIVED": [
                "the caller population — every tracked file the naming scan found, never listed "
                "here",
                "link 1, caller -> generator: route A, the generator the caller's own text "
                "declares, quoted from the line it was found on; route B, the tracked Python "
                "sources whose WRITE SITES resolve to the caller's repository-relative path",
                "link 2, generator -> enumerating: the tracked-tree enumeration in the generator's "
                "own source, quoted from the line it was found on; or an import of a module that "
                "has one; or a read of an artifact whose own generator has one",
                "every kind, every tally and every holder kind",
            ],
            "what_is_AUTHORED": [
                "which git subcommands count as enumerating the tracked tree — published in full, "
                "with the string constant it was found as quoted per generator, and sought among "
                "the source's CONSTANTS rather than in its text, so a sentence mentioning `ls-tree` "
                "is not read as a call to it",
                "the spellings by which a generated file declares its generator",
                "which file extensions make a holder a tool reading the file by name, and the "
                "order the three holder kinds are applied in",
            ],
            "★_why_it_is_neither_of_the_two_shapes_the_ruling_forbids":
                "It is not a naming-breadth threshold: no count of how many files a caller names "
                "enters the rule anywhere. It is not a hand-typed exemption list: no caller is "
                "named in this file, and a record becomes an enumerator only by carrying a "
                "resolvable producer whose source enumerates.",
            "the_closed_vocabulary": {
                KIND_ENUMERATOR: "a generated file, or a surface rendered from one, whose "
                                 "generator enumerates the tracked tree — its namings are "
                                 "published as data and HOLD NOTHING",
                KIND_GENERATED_NOT_ENUMERATING: "a generator is established for it and none of its "
                                                "generators enumerates the tree — its naming HOLDS",
                KIND_NOT_GENERATED: "no tracked Python source writes it and it declares no "
                                    "generator — its naming HOLDS",
                KIND_UNDERIVABLE: "a producer relation was reached that could not be resolved. Its "
                                  "naming HOLDS in the meantime, which is the conservative "
                                  "direction, and it RETURNS TO THE USER",
            },
            "the_kind_tally": kind_tally,
            "★_the_KIND_UNDERIVABLE_list_returning_to_the_user": {
                "the_ruling": reading["what an underivable kind does"],
                "callers": [{"caller": p, "why": kinds[p]["why"]} for p in underivable],
                "these_namings_HOLD_in_the_meantime": True,
            },
            "★_what_this_classification_does_NOT_establish":
                "That a caller is NOT an enumerator is established only as far as link 1 reaches. "
                "A file produced by something other than a tracked Python source, and declaring "
                "nothing, is reported as not produced by the record's own machinery — a statement "
                "about the record's machinery, not about the file's history. The residual error "
                "runs in the safe direction: such a caller HOLDS. Two bounds are stated rather "
                "than left implicit: a write reached through two helper functions is not found, "
                "and a write site whose path expression cannot be resolved sends its caller to "
                "KIND-UNDERIVABLE rather than to a guess.",
            "tracked_python_sources_parsed": len(facts),
            "generators_whose_own_source_enumerates_the_tracked_tree": {
                path: enumerating[path] for path in sorted(enumerating)},
            "★_generators_that_only_TOUCH_an_enumeration_and_establish_nothing": {
                "why_they_establish_nothing":
                    "Importing a module that enumerates, or reading an artifact one produced, may "
                    "mean the enumeration passes through into this generator's own output or may "
                    "mean it is consumed for something else, and nothing in the source separates "
                    "the two. A caller produced by one of these is KIND-UNDERIVABLE and HOLDS. The "
                    "first run of this derivation treated the weaker relation as the stronger one, "
                    "and classified the decisions register's own AUTHORED data file as a tree "
                    "enumeration.",
                "generators": {path: ambiguous[path] for path in sorted(ambiguous)},
            },
            "tracked_python_sources_that_would_not_parse": unparsed,
            "what_an_unparsed_source_costs": "It can produce no producer link, so any caller it "
                                             "writes keeps holding. The list is published so the "
                                             "cost is visible rather than assumed to be zero.",
        },
        "★_THE_FOUR_USER_RULED_INPUTS_OF_THE_2026_08_17_CALLERS_SITTING": {
            "★_why_they_are_published_apart_from_everything_else_in_this_artifact":
                "They are RULINGS, not derivations. Everywhere one of them changes a verdict, the "
                "verdict carries `how_the_kind_was_settled` or a `why_it_holds_nothing` naming the "
                "sitting, so a reader can tell a ruled input from a derived classification without "
                "reading the generator. The distinction is the dispatch's own requirement.",
            "authority": "cowork_rulings_2026_08_17_callers_sitting.md (the user's word: \"I agree "
                         "on yor recommendations\" — quoted verbatim in that record's §0)",
            "every_sentence_located_in_that_record_on_this_run": callers_ruling,
            "★_1_the_nine_KIND_UNDERIVABLE_callers_are_ENUMERATOR_class": {
                "the_ruling": callers_ruling["the nine are ENUMERATOR-class"],
                "★_how_the_membership_is_DERIVED_and_never_retyped":
                    "The sitting was held at the census's own published KIND-UNDERIVABLE "
                    "population, read by the writing side at the git object of the commit that "
                    "carries that reading. The membership IS that list, taken from the same "
                    "object; each derived caller's base name is then LOCATED in the sitting record "
                    "itself, and a derived set the record does not describe HALTS this tool rather "
                    "than ruling on a population the user never saw.",
                "the_evidence_commit": CALLERS_RULING_EVIDENCE_COMMIT,
                "count": len(ruled_enumerator_rows),
                "callers": ruled_enumerator_rows,
                "ruled_callers_this_run_no_longer_finds":
                    {"count": len(ruled_but_not_found), "callers": ruled_but_not_found,
                     "why_published": "a ruled caller the naming scan no longer sees is published "
                                      "rather than dropped, so the ruling's reach stays readable "
                                      "(#12)"},
                "★_what_it_does_NOT_license": callers_ruling["what it does not license"],
            },
            "★_2_and_3_which_HOLDER_KINDS_hold": {
                "a_prose_citation": callers_ruling["a prose citation"],
                "a_naming_outside_the_three_kinds": callers_ruling["the fourth bucket"],
                "what_holds": callers_ruling["what continues to hold"],
                "the_kinds_that_HOLD": list(HOLDER_KINDS_THAT_HOLD),
                "the_kinds_that_HOLD_NOTHING": list(HOLDER_KINDS_THAT_HOLD_NOTHING),
                "★_nothing_is_dropped":
                    "Every naming whose holder kind was ruled to hold nothing stays PUBLISHED, per "
                    "member, in its own field with the line it was found on and the ground it was "
                    "ruled on (#12). What changed is what a naming DOES, never whether it is "
                    "recorded.",
            },
            "★_what_this_sitting_did_NOT_do":
                "It archives nothing. A verdict that flips toward PASSES-THE-CHECK by these inputs "
                "confers CANDIDACY only, and every ruled condition on the archiving wave — "
                "mined-first, members-seen-by-the-user-first for the stray root files — stands "
                "untouched.",
        },
        "★_every_surviving_holder_BY_KIND_and_the_question_DEFERRED_to_it": {
            "the_ruling": reading["the deferred question"],
            "★_THE_DEFERRED_QUESTION_IS_ANSWERED": "It was deferred by the 2026-08-16 ruling to "
                                                   "this evidence and ANSWERED at the 2026-08-17 "
                                                   "callers sitting: a prose citation does NOT "
                                                   "hold, nor does a naming outside the three "
                                                   "kinds. The tallies below are unchanged — every "
                                                   "holder of every kind is still counted and "
                                                   "published — and what the answer changes is "
                                                   "which of them reaches a member's "
                                                   "`holding_callers`.",
            "what_the_fourth_bucket_is": "A holder that is none of the ruling's three kinds — "
                                         "chiefly a DATA record (`.json`, `.csv`, a text dump) "
                                         "that names a flagged file without reading it as a tool "
                                         "and without citing it as prose. It is published rather "
                                         "than forced into one of the three, because forcing it "
                                         "would inflate the kind a reader is most likely to take "
                                         "for a real dependency.",
            "the_holder_kind_tally": holder_tally,
            "holders_by_kind": holders_by_kind,
        },
        "who_does_the_naming": who,
        "the_flagged_population_size": flagged_total,
        "candidacies": rows,
    }


def main(argv: list[str]) -> int:
    check = "--check" in argv
    commit = None
    if "--at" in argv:
        commit = argv[argv.index("--at") + 1]
        if not re.fullmatch(r"[0-9a-f]{7,40}", commit):
            raise Stop(f"--at takes an explicit commit hash, not {commit!r}")

    if check:
        if not OUT.exists():
            print("FAIL: the caller-check artifact is missing:", OUT)
            return 1
        have = json.loads(OUT.read_text(encoding="utf-8"))
        commit = commit or have["measured_at_commit"]

    if commit is None:
        raise Stop("--at <commit> is required when writing: the reading is a statement about one "
                   "tree and the commit is part of the finding")

    artifact = build(commit)
    text = json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"

    if check:
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: the caller-check does not re-derive:", OUT)
            return 1
        print("the retirement caller-check re-derives")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print(f"  measured at {commit}")
    for row in artifact["candidacies"]:
        print(f"  [{row['verdict']}] {row['candidacy']} "
              f"({row['members_flagged']} flagged, "
              f"{len(row['members_held_by_callers'])} held by callers)")
    kind = artifact["★_the_caller_kind_classification"]
    for name, count in kind["the_kind_tally"].items():
        print(f"  caller kind {name}: {count}")
    print("  KIND-UNDERIVABLE callers returning to the user: "
          f"{len(kind['★_the_KIND_UNDERIVABLE_list_returning_to_the_user']['callers'])}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
