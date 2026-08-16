#!/usr/bin/env python3
"""EVERY READER OF THE OLD PHASE-1 GATE ARTIFACTS — enumerated before anything freezes.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §4 of
`cowork_rulings_2026_08_16_preparation_return.md` (the soft-discard's REACH, Alternative A as
recommended): *"The surface's R1 check — the enumeration of every reader of the old phase-1 gate
artifacts at the current commit — runs BEFORE anything freezes; a live consumer outside the
superseded program is a STOP-and-report."*

WHAT IS BEING FROZEN, AND WHAT FREEZING MEANS.  The ruling moves the checks that exist only to
derive the SUPERSEDED three-phase structure's phase-1 gate into the guard set's historical class:
their committed artifacts stay on disk exactly as they are, and are never regenerated again.  A
frozen artifact is therefore still READABLE.  What a freeze takes away is not the file but its
FUTURE MOVEMENT — the artifact stops tracking the record.  That is why this enumeration asks, per
reader, whether the reader needs the derivation to keep moving.

THE THREE VERDICTS, which are the ruling's own three words, and the one judgment declared rather
than buried.  The ruling names three classes — the superseded program's own apparatus, a historical
record, or a LIVE consumer — and every naming here is placed in one of them:

  * `the-superseded-programs-own-apparatus` — the naming file is part of the phase-1 gate
    derivation family: one of its generators, one of its artifacts, or a check whose OWN population
    is imported from one of those artifacts.
  * `a-historical-record` — the naming is a CITATION and not a read.  The file names the artifact
    in prose or carries it as a row of a generated census; it opens nothing.  A citation is INERT
    under a freeze, because the artifact is frozen IN PLACE and stays readable.
    ★ THE JUDGMENT, DECLARED: the ruling's three-value vocabulary has no fourth value for a
    citation inside a LIVE governing surface, and this pass does not invent one.  Every citation is
    placed here, and the `citation_subkind` field says which kind of citation it is — a record of an
    act, a governing-surface pointer, or a generated census row — with the naming line QUOTED, so a
    reader who thinks a pointer deserves its own class can see every one of them without
    re-deriving anything.
  * `a-LIVE-consumer` — a check that reads a frozen artifact (or imports a frozen generator) and
    whose own population comes from somewhere else, so it needs the derivation to keep moving.
    **NON-EMPTY IS A STOP**: that is the ruling's own instruction.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  AUTHORED  the six generators the ruling names, each quoted from the ruling record and located in
            it on every run; nothing else.
  DERIVED   each generator's own output artifact; the enumeration of every tracked file naming any
            of them, read from the GIT OBJECTS at the commit the artifact records; whether each
            naming is a code read or a citation, taken from the file's own string constants rather
            than from its prose; the import graph among the checks; each reader's own population
            source; every verdict; and every count.

★ WHY THE ENUMERATION IS PINNED TO A COMMIT.  Read at whatever the current commit happens to be,
this check would go red the first time anybody writes a file that names one of the artifacts —
which is the `OPEN_ITEMS.md` OI-301 / OI-305 shape.  It is therefore taken at the commit the
artifact RECORDS, from content-addressed objects, and re-derives forever.  What stays LIVE is the
apparatus: every named generator must still exist and must still name its own artifact, and a
generator that has gone halts this check rather than shrinking the population silently.

THE STOPS, so this cannot quietly stop being an enumeration:
  * a sentence of the ruling that ordered this check no longer in its ruling record STOPS it — a
    pass may not outlive the words that ordered it;
  * a named generator the tree does not carry STOPS it;
  * a named generator whose own output artifact cannot be derived from its source STOPS it;
  * a naming file the classification cannot place STOPS it;
  * a non-empty LIVE-consumer class STOPS it — the ruling's own instruction;
  * a verdict tally that does not account for the namings STOPS it.

Run:
  python tools/audit/gen_phase1_gate_readers.py           # write the artifact
  python tools/audit/gen_phase1_gate_readers.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "phase1_gate_readers.json")
RULING = "cowork_rulings_2026_08_16_preparation_return.md"

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# Parsing another check's source raises SyntaxWarning for an invalid escape inside a pattern
# string. That is a fact about the file being read, not a finding of this pass, and letting it
# reach the captured output would put text into the guard record that no verdict here rests on.
warnings.filterwarnings("ignore", category=SyntaxWarning)


class Stop(Exception):
    """A demand of this enumeration is unmet. Never a warning."""


# ── AUTHORED (the only authored input) — the six generators the ruling names ──────────────────
# Quoted from `cowork_rulings_2026_08_16_preparation_return.md` §4 and from the executing
# dispatch's Task 1, and located in the ruling record on every run by the sentences below.
FAMILY_GENERATORS = [
    "tools/audit/gen_phase1_completion_inventory.py",
    "tools/audit/gen_phase1_finish_line.py",
    "tools/audit/decisions/gen_outstanding_delegations.py",
    "tools/audit/decisions/gen_finish_line_item1_routes.py",
    "tools/audit/decisions/gen_item1_rehome_blocker.py",
    "tools/audit/decisions/gen_r1_superseded_reach.py",
]

# The two whose artifacts the ruling calls "the old phase-1 gate artifacts" by name.
GATE_DERIVATIONS = [
    "tools/audit/gen_phase1_completion_inventory.py",
    "tools/audit/gen_phase1_finish_line.py",
]

RULING_SENTENCES = {
    "what runs before anything freezes":
        "The surface's R1 check — the enumeration of every reader of the old phase-1 gate "
        "artifacts at the current commit — runs BEFORE anything freezes; a live consumer outside "
        "the superseded program is a STOP-and-report.",
    "what happens to the superseded members":
        "The SUPERSEDED members move to the guard set's historical class by an authored "
        "classification change committed with the act, their committed artifacts frozen in place "
        "as record (#12), never regenerated again; the close names every member.",
}

RECORD_OF_AN_ACT = re.compile(
    r"^(cc_instruction_|cc_report_|cowork_rulings_|cowork_away_returns\.md$|"
    r"cowork_handoff\.md$|cowork_instruction_|cowork_scratch_|STATUS\.md$|STATUS_ARCHIVE\.md$)")
GOVERNING = {"CLAUDE.md", "ARCHITECTURE.md", "OPEN_ITEMS.md", "DECISIONS.md",
             "BUILD_AND_TEST.md"}


# ── reading the tree at one commit, from content-addressed objects ────────────────────────────
def git(*args: str) -> bytes:
    proc = subprocess.run(["git", "-C", ROOT, *args], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop("git failed: " + " ".join(args) + " — "
                   + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout


def head_commit() -> str:
    return git("rev-parse", "HEAD").decode().strip()


def tracked_at(commit: str) -> list[str]:
    out = git("ls-tree", "-r", "--name-only", "-z", commit).decode("utf-8", "replace")
    return sorted(p for p in out.split("\0") if p)


_BLOBS: dict[tuple[str, str], str | None] = {}


def blob_at(commit: str, path: str) -> str | None:
    cached = _BLOBS.get((commit, path), Ellipsis)
    if cached is not Ellipsis:
        return cached                                  # type: ignore[return-value]
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{commit}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        text = None
    else:
        try:
            text = proc.stdout.decode("utf-8")
        except UnicodeDecodeError:
            text = None
    _BLOBS[(commit, path)] = text
    return text


def files_naming(commit: str, needle: str) -> list[str]:
    """Every tracked file whose blob at `commit` contains `needle`, as a fixed string.

    `git grep` over the commit rather than a blob-by-blob walk: the walk spawns one process per
    tracked file and takes minutes on this tree, which would make a guard nobody wants to run.
    Both readings are of the same content-addressed objects and agree; this one is faster.
    """
    proc = subprocess.run(
        ["git", "-C", ROOT, "grep", "--no-color", "-I", "-F", "-l", "-z", "-e", needle, commit],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode not in (0, 1):
        raise Stop("git grep failed: " + proc.stderr.decode("utf-8", "replace").strip())
    prefix = commit + ":"
    found = []
    for record in proc.stdout.decode("utf-8", "replace").split("\0"):
        if not record:
            continue
        found.append(record[len(prefix):] if record.startswith(prefix) else record)
    return sorted(found)


# ── the ruling, located on every run ──────────────────────────────────────────────────────────
def flatten(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_ruling() -> dict[str, str]:
    path = os.path.join(ROOT, RULING)
    if not os.path.exists(path):
        raise Stop(f"the ruling record this check serves is missing: {RULING}")
    with open(path, encoding="utf-8") as fh:
        text = flatten(fh.read())
    missing = [name for name, quote in RULING_SENTENCES.items() if flatten(quote) not in text]
    if missing:
        raise Stop("a sentence of the ruling that ordered this enumeration is no longer in its "
                   f"ruling record, so the pass would outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


# ── each generator's own output artifact, DERIVED from its source ─────────────────────────────
JSON_LITERAL = re.compile(r'"([A-Za-z0-9_\-]+\.json)"')


def artifact_of(rel: str, source: str) -> str:
    """The .json this generator writes, derived from its own source rather than typed here."""
    base = os.path.basename(rel)[:-3]
    expected = (base[4:] if base.startswith("gen_") else base) + ".json"
    if expected not in set(JSON_LITERAL.findall(source)):
        raise Stop(f"{rel} does not name its own output artifact {expected} — the derivation "
                   f"this check rests on does not hold for it, and it is not guessed")
    for directory in ("tools/audit", "tools/audit/decisions"):
        if os.path.exists(os.path.join(ROOT, directory, expected)):
            return f"{directory}/{expected}"
    raise Stop(f"{rel}'s derived output artifact {expected} is on no path this check knows")


# ── the import graph among the checks under tools/audit ───────────────────────────────────────
def import_graph(commit: str, tracked: list[str]) -> dict[str, set[str]]:
    modules: dict[str, str] = {}
    sources: dict[str, str] = {}
    for path in tracked:
        if path.startswith("tools/audit/") and path.endswith(".py"):
            text = blob_at(commit, path)
            if text is None:
                continue
            sources[path] = text
            modules[os.path.basename(path)[:-3]] = path
    graph: dict[str, set[str]] = {path: set() for path in sources}
    for path, text in sources.items():
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in modules:
                        graph[path].add(modules[alias.name])
            elif isinstance(node, ast.ImportFrom):
                if node.module in modules:
                    graph[path].add(modules[node.module])
    return graph


def string_constants(text: str) -> set[str]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            found.add(node.value)
    return found


def reachable(graph: dict[str, set[str]], startpoint: str) -> set[str]:
    seen, stack = set(), [startpoint]
    while stack:
        current = stack.pop()
        for nxt in graph.get(current, ()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def citation_subkind(path: str) -> str:
    base = os.path.basename(path)
    if base in GOVERNING or path.startswith("open_items/") or path.startswith("decisions/"):
        return "a-governing-or-tracking-surface-pointer"
    if path.startswith("tools/") and path.endswith(".json"):
        return "a-row-of-a-generated-census-or-enumeration"
    if path.startswith("ratification_surfaces/"):
        return "a-ruling-surface-pointer"
    if RECORD_OF_AN_ACT.match(base):
        return "a-record-of-an-act"
    return "a-document-citation"


def naming_lines(text: str, needles: list[str], limit: int = 2) -> list[dict]:
    rows = []
    for number, line in enumerate(text.splitlines(), start=1):
        if any(needle in line for needle in needles):
            trimmed = line.strip()
            rows.append({"line": number,
                         "text": trimmed if len(trimmed) <= 220 else trimmed[:217] + "..."})
            if len(rows) >= limit:
                break
    return rows


def build(commit: str | None = None) -> dict:
    ruling = locate_ruling()
    measured_at = commit or head_commit()
    tracked = tracked_at(measured_at)
    tracked_set = set(tracked)

    missing = [g for g in FAMILY_GENERATORS if g not in tracked_set]
    if missing:
        raise Stop(f"the ruling names generator(s) the tree does not carry: {missing}")

    sources = {g: blob_at(measured_at, g) for g in FAMILY_GENERATORS}
    for generator, text in sources.items():
        if text is None:
            raise Stop(f"{generator} could not be read at {measured_at}")
    artifacts = {g: artifact_of(g, sources[g]) for g in FAMILY_GENERATORS}
    gate_artifacts = {artifacts[g] for g in GATE_DERIVATIONS}
    family_artifacts = set(artifacts.values())
    base_names = {os.path.basename(a): a for a in family_artifacts}

    graph = import_graph(measured_at, tracked)
    imports_a_family_generator = {
        path: sorted(reachable(graph, path) & set(FAMILY_GENERATORS)) for path in graph
    }

    # every tracked file naming any of the six artifacts, at the recorded commit
    namings: dict[str, dict[str, list[dict]]] = {}
    candidates: set[str] = set()
    for base in base_names:
        candidates.update(files_naming(measured_at, base))
    for path in sorted(candidates):
        text = blob_at(measured_at, path)
        if text is None:
            continue
        hits = {base: naming_lines(text, [base]) for base in base_names if base in text}
        if hits:
            namings[path] = hits

    rows, live_consumers = [], []
    for path in sorted(namings):
        named = sorted(namings[path])
        text = blob_at(measured_at, path) or ""
        is_python = path.endswith(".py")
        constants = string_constants(text) if is_python else set()
        reads = sorted(base for base in named if base in constants)
        family_imports = imports_a_family_generator.get(path, [])
        own_artifact = path in family_artifacts
        is_generator = path in FAMILY_GENERATORS

        # a reader's own population source: does it read a GATE artifact as its population?
        reads_gate = sorted(base for base in reads if base_names[base] in gate_artifacts)

        if is_generator or own_artifact:
            verdict = "the-superseded-programs-own-apparatus"
            ground = ("the file IS a member of the phase-1 gate derivation family — "
                      + ("one of the six generators the ruling names"
                         if is_generator else "one of those generators' own output artifacts"))
        elif family_imports:
            verdict = "the-superseded-programs-own-apparatus"
            ground = ("the file IMPORTS a family generator transitively, so it is a view of the "
                      f"same derivation: {family_imports}")
        elif reads:
            # a check that reads a family artifact without importing a family generator
            verdict = ("the-superseded-programs-own-apparatus" if reads_gate
                       else "a-LIVE-consumer")
            ground = (
                "the file READS a phase-1 gate artifact as its own POPULATION — its subject IS "
                f"that population, so it belongs to the same program: {reads_gate}"
                if reads_gate else
                "the file reads a family artifact and takes no population from the gate itself")
            if verdict == "a-LIVE-consumer":
                live_consumers.append(path)
        else:
            verdict = "a-historical-record"
            ground = ("the naming is a CITATION and not a read: the file names the artifact in "
                      "text and carries it in no string constant it opens")

        rows.append({
            "path": path,
            "names": named,
            "verdict": verdict,
            "the_ground": ground,
            "is_one_of_the_six_generators": is_generator,
            "is_one_of_their_artifacts": own_artifact,
            "reads_it_as_a_string_constant": reads,
            "reads_a_gate_artifact_as_its_population": reads_gate,
            "imports_a_family_generator_transitively": family_imports,
            "citation_subkind": None if (reads or family_imports or is_generator or own_artifact)
                                else citation_subkind(path),
            "the_naming_quoted": {base: namings[path][base] for base in named},
        })

    unplaced = [r["path"] for r in rows if r["verdict"] not in (
        "the-superseded-programs-own-apparatus", "a-historical-record", "a-LIVE-consumer")]
    if unplaced:
        raise Stop(f"the classification cannot place: {unplaced}")

    tally: dict[str, int] = {}
    for row in rows:
        tally[row["verdict"]] = tally.get(row["verdict"], 0) + 1
    if sum(tally.values()) != len(rows):
        raise Stop("the verdict tally does not account for the namings")

    # the downstream fact a reader must meet: what the code readers themselves feed
    downstream = []
    for row in rows:
        if row["verdict"] != "the-superseded-programs-own-apparatus":
            continue
        if row["is_one_of_the_six_generators"] or row["is_one_of_their_artifacts"]:
            continue
        if not row["reads_a_gate_artifact_as_its_population"]:
            continue
        base = os.path.basename(row["path"])[:-3]
        produced = (base[4:] if base.startswith("gen_") else base) + ".json"
        consumers = sorted(
            other for other in files_naming(measured_at, produced)
            if other.endswith(".py") and other != row["path"]
            and produced in string_constants(blob_at(measured_at, other) or ""))
        downstream.append({
            "the_check": row["path"],
            "its_population_comes_from": row["reads_a_gate_artifact_as_its_population"],
            "its_own_artifact": produced,
            "checks_that_read_that_artifact": consumers,
            "★_what_this_means_under_a_freeze": (
                "This check is NOT frozen and keeps running; what freezes is its INPUT. Its "
                "population therefore stops moving, and any check listed above inherits that "
                "frozen population one link further down. Nothing halts and nothing is destroyed; "
                "what is lost is the population's future movement, which is stated here rather "
                "than left for a reader to discover."),
        })

    return {
        "what_this_is":
            "Every reader, at one commit, of the old phase-1 gate artifacts and their derivation "
            "family's outputs — the R1 check the user's ruling of 2026-08-16 §4 orders to run "
            "BEFORE anything freezes.",
        "generator": "tools/audit/gen_phase1_gate_readers.py",
        "dispatch": "cc_instruction_preparation_fourth.md, Task 1 (R1)",
        "the_ruling_that_ordered_it": {
            "source": f"{RULING} §4",
            "every_sentence_located_in_that_record_on_this_run": ruling,
        },
        "measured_at_commit": measured_at,
        "★_why_the_reading_is_pinned_to_that_commit": (
            "Read at whatever the current commit happens to be, this check would go red the first "
            "time anybody writes a file naming one of these artifacts — the OI-301 / OI-305 "
            "shape. Every reading below is taken from the git objects at the commit recorded "
            "above, so it re-derives forever. What stays LIVE is the apparatus: a named generator "
            "the tree no longer carries, or one that no longer names its own artifact, halts this "
            "check."),
        "the_family": {
            "★_what_is_authored_here": "the six generators, named by the ruling and by the "
                                       "executing dispatch. Nothing else on this page is authored.",
            "generators": FAMILY_GENERATORS,
            "the_two_the_ruling_calls_the_gate_derivations": GATE_DERIVATIONS,
            "each_generators_own_output_artifact_DERIVED_from_its_source":
                {g: artifacts[g] for g in FAMILY_GENERATORS},
        },
        "the_verdict_vocabulary": {
            "the-superseded-programs-own-apparatus":
                "the naming file is part of the phase-1 gate derivation family — a generator, one "
                "of their artifacts, a transitive importer of a generator, or a check whose own "
                "POPULATION is a gate artifact.",
            "a-historical-record":
                "the naming is a CITATION and not a read. It is inert under a freeze, because the "
                "artifact is frozen IN PLACE and stays readable. ★ THE JUDGMENT, DECLARED: the "
                "ruling's vocabulary has no fourth value for a citation inside a LIVE governing "
                "surface, and this pass invents none; `citation_subkind` says which kind each "
                "citation is and the naming line is quoted, so a reader who would class a pointer "
                "differently can see every one without re-deriving anything.",
            "a-LIVE-consumer":
                "a check that reads a frozen artifact, or imports a frozen generator, and takes "
                "its population from somewhere else — so it needs the derivation to keep moving. "
                "NON-EMPTY IS A STOP, which is the ruling's own instruction.",
        },
        "the_tally": tally,
        "★_the_LIVE_consumer_class": {
            "count": len(live_consumers),
            "members": live_consumers,
            "what_a_non_empty_class_means": "the ruling's STOP: the assumption R1 that no live "
                                            "consumer outside the superseded program reads these "
                                            "artifacts would be falsified.",
        },
        "★_the_downstream_fact_a_reader_must_meet": downstream,
        "★_what_this_enumeration_does_NOT_assert": (
            "That a file naming none of these artifacts depends on none of them. A path built at "
            "run time carries no literal to find, and a naming inside a binary blob is not read "
            "here — the same bound the retirement caller-check publishes of itself. It also "
            "asserts nothing about whether any verdict is RIGHT: the ground of each is published "
            "beside it and the naming is quoted, so the reading is the user's."),
        "readers": rows,
    }


def main(argv: list[str]) -> int:
    if "--check" in argv:
        if not os.path.exists(OUT):
            print("FAIL: the artifact is missing:", os.path.relpath(OUT, ROOT))
            return 1
        with open(OUT, encoding="utf-8") as fh:
            have = json.load(fh)
        rebuilt = build(have.get("measured_at_commit"))
        text = json.dumps(rebuilt, indent=1, ensure_ascii=False) + "\n"
        with open(OUT, encoding="utf-8") as fh:
            if fh.read() != text:
                print("FAIL: the phase-1 gate reader enumeration does not re-derive")
                return 1
        print(f"the phase-1 gate reader enumeration re-derives: {len(rebuilt['readers'])} naming "
              f"file(s), {rebuilt['★_the_LIVE_consumer_class']['count']} live consumer(s)")
        return 0

    built = build()
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(built, indent=1, ensure_ascii=False) + "\n")
    print("wrote", os.path.relpath(OUT, ROOT))
    for verdict, count in sorted(built["the_tally"].items()):
        print(f"  {verdict}: {count}")
    live = built["★_the_LIVE_consumer_class"]
    print(f"  LIVE consumers outside the superseded program: {live['count']}")
    if live["count"]:
        raise Stop(f"LIVE consumer(s) outside the superseded program: {live['members']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
