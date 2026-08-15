#!/usr/bin/env python3
"""THE ARTIFACT INVENTORY — every tracked file at one commit, classified by a mechanical signature.

Dispatch: `cc_instruction_artifact_inventory.md`, Task 1 (Cowork, 2026-08-15), executing §2.10 of
`cowork_rulings_2026_08_15_method_directions.md`: *"A DERIVED walk of the tree (never hand-listed),
every file classified by mechanical signature into classes with an unclassified STOP."*

WHY IT EXISTS.  The derivation-first repair needs to know what the repository HOLDS before any
phase can say what it READS.  The user directed that this walk come before the phases are drafted,
and that it be DERIVED rather than hand-listed, because a hand-listed inventory is a memory of the
tree rather than a reading of it.  This tool is the walk.  It PROPOSES nothing: the role, mining
and retirement verdicts are authored on the ruling surface
(`tools/audit/gen_artifact_inventory_surface.py`), which imports this file's class list and cannot
carry a class this file does not publish.

WHAT IS DERIVED AND WHAT IS AUTHORED, stated because the difference is the whole value:

  DERIVED  — the population (every blob and every submodule link the named commit's tree carries,
             read from the git object by explicit hash), every count, every total in bytes, every
             per-file class assignment, the example paths, and the untracked appendix.
  AUTHORED — the SIGNATURE TABLE below: which path shapes name which class, in which order, and
             what each class is called.  Nothing else.  No file is classed by a judgment of its
             substance, which is assumption A1 of the dispatch and is checked by the STOP.

THE SIGNATURE IS PATH AND EXTENSION ONLY.  The dispatch admits a banner as a third signature kind.
None is used: every tracked file at the commit this ran against is classed by where it sits and
what it is called.  That is a stronger position than the dispatch requires and it is recorded here
so a later reader does not add a content read casually — a signature that opens a file is one that
can be argued about, and this table cannot.

THE STOPS, so this cannot silently stop being a derivation:
  1. an UNCLASSIFIED file is a STOP — the dispatch's own stop rule, and the refutation condition of
     its prediction P1.  A file is never dropped, never bucketed as `other`, never skipped;
  2. a class in the authored table that matches NOTHING is a STOP — a rule that has stopped
     applying is a rule about a tree that no longer exists, and carrying it would let the table
     drift away from the repository silently;
  3. the derived population must reconcile with the tree's own entry count — a difference means the
     walk dropped something, and it halts rather than publishing a short list;
  4. `--check` re-derives at the commit the committed artifact RECORDS, so it passes indefinitely;
     and it separately re-runs the classification at the CURRENT tree and STOPS if anything there
     is unclassified.  The second half is the live one: a file added by a later commit that no rule
     names must halt this tool rather than enter a later pass ungraded.

WHAT THIS DOES NOT DO.  It moves, renames, retires, archives and deletes nothing — the dispatch
says in terms that every retirement is a PROPOSAL on the ruling surface and that the user rules.
It reads no file's content.  It makes no comparison against the code in either direction, takes no
view on whether anything it lists should exist, and expresses no verdict of any kind.

Usage:
  python tools/audit/gen_artifact_inventory.py            # write the artifact at the current tree
  python tools/audit/gen_artifact_inventory.py --check    # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import posixpath
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "tools" / "audit" / "artifact_inventory.json"


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning, never a skipped file."""


# ── matcher primitives — the only shapes a signature may take ────────────────────────────────────
# Each returns a predicate over (path, basename, extension).  They are deliberately few: a
# signature that needs a fourth shape is a signature that has started reasoning about substance.

def under(*prefixes):
    """The path sits inside one of these directories."""
    return lambda p, b, e: any(p == x.rstrip("/") or p.startswith(x) for x in prefixes)


def segment(*names):
    """One of the path's directory names is exactly this — reaches nested copies too."""
    wanted = set(names)
    return lambda p, b, e: bool(wanted & set(p.split("/")[:-1]))


def at_root_named(*names):
    """The path IS one of these repository-root entries."""
    wanted = set(names)
    return lambda p, b, e: p in wanted


def exact_path(*paths):
    """The path IS one of these, named in full from the repository root."""
    wanted = set(paths)
    return lambda p, b, e: p in wanted


def at_root_any_name():
    """Any file sitting directly at the repository root, whatever it is called."""
    return lambda p, b, e: "/" not in p


def at_root_prefixed(*prefixes):
    """A repository-root file whose name starts with one of these."""
    return lambda p, b, e: "/" not in p and any(b.startswith(x) for x in prefixes)


def at_root_ext(*exts):
    """A repository-root file with one of these extensions."""
    wanted = set(exts)
    return lambda p, b, e: "/" not in p and e in wanted


def in_dir_ext(directory, *exts):
    """A file directly inside this directory with one of these extensions."""
    wanted = set(exts)
    return lambda p, b, e: posixpath.dirname(p) == directory.rstrip("/") and e in wanted


def in_dir(directory):
    """A file directly inside this directory, at any extension."""
    return lambda p, b, e: posixpath.dirname(p) == directory.rstrip("/")


def under_with_ext(prefix, *exts):
    """Anywhere below this directory, with one of these extensions."""
    wanted = set(exts)
    return lambda p, b, e: p.startswith(prefix) and e in wanted


def any_of(*preds):
    return lambda p, b, e: any(f(p, b, e) for f in preds)


# ── AUTHORED — THE SIGNATURE TABLE.  Ordered; the FIRST rule that matches decides. ───────────────
# Three columns: the class name, the signature stated in words (published in the artifact so a
# reader can check the rule against the members without reading this file), and the matcher.
# `descend` marks the classes whose per-file assignments are published whole — the dispatch names
# the prose and tools areas, and its prediction P2 expects the per-item ruling to be needed there.

SIGNATURE_TABLE = [
    # ---- our own analysis, the subject of everything ------------------------------------------
    ("our-analysis-tests-and-fixtures",
     "anywhere below `src/composing/tests/` — the composing module's own test sources, its "
     "fixtures and the two chord-analyzer catalog files",
     under("src/composing/tests/"), True),
    ("our-analysis-source",
     "anywhere below `src/composing/` that is not its tests directory",
     under("src/composing/"), True),
    ("our-pipeline-snapshot-goldens",
     "anywhere below `src/notation/tests/pipeline_snapshot_tests/snapshots/` — the pinned "
     "per-piece output the P1/P2/P3/P4 snapshot suite compares against",
     under("src/notation/tests/pipeline_snapshot_tests/snapshots/"), True),
    ("our-pipeline-snapshot-test-harness",
     "the remaining files of `src/notation/tests/pipeline_snapshot_tests/` — the suite that reads "
     "those goldens, its build file, its environment and its corpus description",
     under("src/notation/tests/pipeline_snapshot_tests/"), True),

    # ---- code we did not write -----------------------------------------------------------------
    ("third-party-vendored-code",
     "any path with a `thirdparty` directory name in it, at the repository root or nested inside "
     "a module — vendored libraries carried in-tree with their own upstream history",
     segment("thirdparty"), False),
    ("upstream-application-source",
     "anywhere below `src/` not already claimed above — MuseScore's own application code, which "
     "this fork carries and edits in a few recorded places",
     under("src/"), False),
    ("upstream-application-resources",
     "anywhere below `share/` or `fonts/` — templates, translations, sounds, styles, icons and "
     "type faces shipped with the application",
     under("share/", "fonts/"), False),
    ("upstream-application-tests",
     "anywhere below `test/` or `vtest/` — MuseScore's integration suite and its visual "
     "regression material",
     under("test/", "vtest/"), False),

    # ---- the build and the repository's own configuration ---------------------------------------
    ("build-and-continuous-integration-configuration",
     "anywhere below `buildscripts/` or `.github/`, plus every `CMakeLists.txt`, `*.cmake`, "
     "`CMakePresets.json`, `Doxyfile.plugins`, `pyproject.toml`, `pdm.lock` and every `*.bat` or "
     "`*.sh` build launcher at the repository root",
     any_of(under("buildscripts/", ".github/"),
            lambda p, b, e: b == "CMakeLists.txt" or e == ".cmake",
            at_root_named("CMakePresets.json", "Doxyfile.plugins", "pyproject.toml", "pdm.lock",
                          "ninja_build.sh"),
            at_root_ext(".bat")), False),
    ("repository-metadata-and-legal-notices",
     "the repository's own dot-files and notices: `.gitignore`, `.gitattributes`, `.gitmodules`, "
     "`.clangd`, `.coderabbit.yaml`, `.git-blame-ignore-revs`, anything below `.tx/`, "
     "`.vscode_template/` or `hooks/`, the `muse` submodule link, and `LICENSE.txt`, `README.md`, "
     "`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`",
     any_of(under(".tx/", ".vscode_template/", "hooks/"),
            at_root_named(".gitignore", ".gitattributes", ".gitmodules", ".clangd",
                          ".coderabbit.yaml", ".git-blame-ignore-revs", "muse",
                          "LICENSE.txt", "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md")),
     False),

    # ---- the governing record --------------------------------------------------------------------
    ("governing-documents",
     "the seven repository-root documents a session is instructed to read: `CLAUDE.md`, "
     "`ARCHITECTURE.md`, `DECISIONS.md`, `OPEN_ITEMS.md`, `STATUS.md`, `BUILD_AND_TEST.md`, "
     "`DEFECT_TYPES.md`",
     at_root_named("CLAUDE.md", "ARCHITECTURE.md", "DECISIONS.md", "OPEN_ITEMS.md", "STATUS.md",
                   "BUILD_AND_TEST.md", "DEFECT_TYPES.md"), True),
    ("governing-documents-superseded-halves",
     "`STATUS_ARCHIVE.md` and `cowork_handoff_archive.md` — the halves the 2026-07-18 split moved "
     "out of the two live documents above, reference-only and outside the session-start reads",
     at_root_named("STATUS_ARCHIVE.md", "cowork_handoff_archive.md"), True),
    ("the-open-items-register-detail-files",
     "anywhere below `open_items/` — one detail file per row plus the split reconciliation "
     "artifact; the INDEX itself is a governing document above",
     under("open_items/"), True),
    ("the-decisions-register-group-files",
     "anywhere below `decisions/` — the rendered per-group entry files; the INDEX itself is a "
     "governing document above",
     under("decisions/"), True),
    ("ratification-surfaces",
     "anywhere below `ratification_surfaces/` — the reading surfaces a ruling was taken on",
     under("ratification_surfaces/"), True),

    # ---- the writing side's own record ------------------------------------------------------------
    ("writing-side-ruling-records",
     "repository-root files whose name begins `cowork_rulings_`, `cowork_ruling_`, "
     "`cowork_owner_rulings_`, `cowork_pending_rulings_` or `cowork_document_route_rulings_`",
     at_root_prefixed("cowork_rulings_", "cowork_ruling_", "cowork_owner_rulings_",
                      "cowork_pending_rulings_", "cowork_document_route_rulings_"), True),
    ("writing-side-session-records",
     "`cowork_handoff.md`, `cowork_away_returns.md`, and repository-root files beginning "
     "`cowork_instruction_` — the running session record and the dispatches the writing side "
     "wrote to itself",
     any_of(at_root_named("cowork_handoff.md", "cowork_away_returns.md"),
            at_root_prefixed("cowork_instruction_")), True),
    ("writing-side-design-documents",
     "every other repository-root file beginning `cowork_` — designs, audits, dossiers, plans, "
     "inventories and findings authored by the writing side",
     at_root_prefixed("cowork_"), True),
    ("writing-side-scratch-directories",
     "anywhere below a dated `cowork_scratch_*` directory or below `scratch_artifacts/`",
     any_of(under("scratch_artifacts/"),
            lambda p, b, e: p.startswith("cowork_scratch_")), True),

    # ---- the coding side's own record ---------------------------------------------------------------
    ("dispatches-to-the-coding-side",
     "repository-root files beginning `cc_instruction_` — one dispatch per CC session",
     at_root_prefixed("cc_instruction_"), True),
    ("reports-from-the-coding-side",
     "every other repository-root file beginning `cc_` — the reports, dossiers and measurement "
     "outputs CC returned",
     at_root_prefixed("cc_"), True),

    # ---- the documentation directory ------------------------------------------------------------------
    ("llm-triage-prompts",
     "anywhere below `docs/prompts/`",
     under("docs/prompts/"), False),
    ("documentation-directory-superseded",
     "anywhere below `docs/old_docs/`",
     under("docs/old_docs/"), True),
    ("published-research-papers",
     "anywhere below `docs/research_papers/`",
     under("docs/research_papers/"), True),
    ("generated-api-documentation-assets",
     "anywhere below `docs/apidocs_static/`, plus `docs/index.html`",
     any_of(under("docs/apidocs_static/"), exact_path("docs/index.html")), False),
    ("documentation-directory-prose",
     "every remaining file directly inside `docs/` — specifications, design documents, "
     "reconstructions, policies and findings interleaved in one directory",
     under("docs/"), True),

    # ---- the audit apparatus ---------------------------------------------------------------------------
    ("audit-apparatus-generators",
     "every `*.py` anywhere below `tools/audit/`",
     under_with_ext("tools/audit/", ".py"), True),
    ("audit-apparatus-artifacts",
     "everything else below `tools/audit/` — the generated JSON, JSONL, Markdown and text these "
     "generators write",
     under("tools/audit/"), True),

    # ---- measurement, corpora and fitted material ---------------------------------------------------------
    ("the-hard-stop-reference",
     "anywhere below `tools/robust_stop/` — the committed reference the block-(A) regression stop "
     "is diffed against, and its snapshots",
     under("tools/robust_stop/"), True),
    ("joint-estimator-tables-and-fit-records",
     "anywhere below `tools/joint_estimator/` or `tools/fit_ledgers/` — the estimator's committed "
     "tables and adoption record, and the per-fit ledgers",
     under("tools/joint_estimator/", "tools/fit_ledgers/"), True),
    ("calibration-maps-and-their-snapshots",
     "anywhere below `tools/calibration_maps/`",
     under("tools/calibration_maps/"), True),
    ("notation-seam-artifacts",
     "anywhere below `tools/notation_seams/`",
     under("tools/notation_seams/"), True),
    ("musical-score-collections-held-for-research",
     "anywhere below `tools/extra scores/` — the acquired collections, research material rather "
     "than gate material until a deliberate re-baseline promotes any of it",
     under("tools/extra scores/"), False),
    ("corpus-and-parameter-registries",
     "the registry and manifest files sitting directly in `tools/`: `corpus_registry.json`, "
     "`extra_scores_registry.json`, `score_census_registry.json`, `stage5_split_registry.json`, "
     "`param_manifest.json`, `snapshot_sources_manifest.json`, and the committed baseline JSON "
     "beside them",
     exact_path("tools/corpus_registry.json", "tools/extra_scores_registry.json",
                "tools/score_census_registry.json", "tools/stage5_split_registry.json",
                "tools/param_manifest.json", "tools/snapshot_sources_manifest.json",
                "tools/bir_false_baseline.json", "tools/bir_true_baseline.json",
                "tools/check_corelli_raw.json"), True),
    ("measurement-and-analysis-tools",
     "the executable measurement and analysis sources sitting directly in `tools/` — every "
     "`*.py`, `*.sh` and `batch_analyze.cpp`",
     any_of(in_dir_ext("tools", ".py", ".sh"), exact_path("tools/batch_analyze.cpp")), True),
    ("measurement-outputs-recorded-beside-the-tools",
     "the recorded outputs sitting directly in `tools/` — every `*.txt`, `*.log` and "
     "`REPRODUCIBILITY.md`",
     any_of(in_dir_ext("tools", ".txt", ".log"), exact_path("tools/REPRODUCIBILITY.md")), True),
    ("our-measurement-tool-test-material",
     "anywhere below `tools/tests/` — the cross-language constant checks and their fixtures",
     under("tools/tests/"), True),
    ("probe-outputs-and-their-snapshots",
     "anywhere below `tools/reports/`, `tools/term_inventory/` or "
     "`tools/refresh_divergence_20260424/` — dated probe outputs kept beside their generator",
     under("tools/reports/", "tools/term_inventory/", "tools/refresh_divergence_20260424/"), True),
    ("upstream-developer-tooling",
     "everything else below `tools/` — MuseScore's own developer utilities (`jsdoc`, `bww2mxml`, "
     "`codestyle`, `fonttools`, `miditools`, `translations`, `ziprw`, `coverage`, "
     "`check_build_without_qt`, `checkheaders`, `release_notes`, `soundfonts`) and the chord "
     "diagram converter",
     under("tools/"), False),

    # ---- other workspaces ----------------------------------------------------------------------------------
    ("idiom-discovery-workspace",
     "anywhere below `idiom_discovery/`",
     under("idiom_discovery/"), True),
    ("ai-assistant-design-notes",
     "anywhere below `ai-assistant/`",
     under("ai-assistant/"), True),
    ("demonstration-and-sandbox-material",
     "anywhere below `demos/` or `sandbox/`",
     under("demos/", "sandbox/"), False),

    # ---- what is at the repository root and belongs to none of the above ---------------------------------------
    ("root-level-project-prose-outside-the-naming-conventions",
     "`REFACTOR_DEDUPLICATION_PLAN.md`, `PHASE1_BUILD_ERROR_TRIAGE_PROMPT.md` and "
     "`contrapunctus_findings.md` — project prose at the repository root carrying none of the "
     "`cowork_`, `cc_` or governing-document names",
     at_root_named("REFACTOR_DEDUPLICATION_PLAN.md", "PHASE1_BUILD_ERROR_TRIAGE_PROMPT.md",
                   "contrapunctus_findings.md"), True),
    ("stray-working-files-committed-to-the-repository-root",
     "every remaining file sitting DIRECTLY at the repository root, plus the three top-level "
     "directories `META-INF/`, `Thumbnails/` and `Testing/` — dumped analysis JSON, diagnostic "
     "text, logs, an exported musical score and an audio file, application settings written by a "
     "run, and the unpacked members of a musical score container together with the CTest "
     "temporary directory. ★ THIS RULE IS BOUNDED ON PURPOSE: it is the last rule, and a "
     "deliberately narrow one, so that a file in a top-level directory no rule names reaches the "
     "unclassified STOP instead of being swallowed here.",
     any_of(at_root_any_name(), under("META-INF/", "Thumbnails/", "Testing/")), True),
]

# ── AUTHORED — the prediction this run grades, quoted from the dispatch ───────────────────────────
P1_SOURCE = ("`cc_instruction_artifact_inventory.md` §0a, prediction P1: \"an authored signature "
             "table of well under forty classes covers every tracked file at HEAD, with the "
             "upstream MuseScore code, the build system and the third-party libraries each ONE "
             "class with one verdict, so the fork's size costs nothing. What would refute it: a "
             "final run whose unclassified bucket is non-empty — which is a STOP, not a "
             "remainder.\" Registered expectation, moderate confidence, no authority.")
P1_CLASS_CEILING = 40
P1_SINGLE_CLASS_SUBJECTS = {
    "the upstream MuseScore code": "upstream-application-source",
    "the build system": "build-and-continuous-integration-configuration",
    "the third-party libraries": "third-party-vendored-code",
}

# AUTHORED — which classes hold material this project did not author.  Marked as authored because
# it is a judgment about provenance, and published only so P1's class count can be read against the
# thing P1's own sentence claims: that the fork's SIZE costs nothing.  It grades no file.
CLASSES_NOT_AUTHORED_BY_THIS_PROJECT = (
    "third-party-vendored-code",
    "upstream-application-source",
    "upstream-application-resources",
    "upstream-application-tests",
    "build-and-continuous-integration-configuration",
    "repository-metadata-and-legal-notices",
    "upstream-developer-tooling",
    "demonstration-and-sandbox-material",
    "generated-api-documentation-assets",
    "musical-score-collections-held-for-research",
)

P2_SOURCE = ("`cc_instruction_artifact_inventory.md` §0a, prediction P2: \"per-item descent "
             "(beyond class-level verdicts) is needed only inside `docs/`, `tools/`, and the "
             "repository-root prose surfaces, where specifications, reports, plans and generated "
             "artifacts interleave. What would refute it: a class elsewhere whose members need "
             "opposite verdicts.\" P2 is graded at the RULING SURFACE, not here: whether a class "
             "needs opposite verdicts is a statement about verdicts, and this file authors none.")

# ── AUTHORED — the probes that establish the table can FAIL, and does what it says ────────────────
# #19: a check that cannot fail establishes nothing.  The first probe is the load-bearing one — the
# last rule in the table is bounded rather than a catch-all precisely so that this probe is
# UNCLASSIFIED, which is what makes the unclassified STOP a live mechanism rather than a sentence.
# Every probe is a SYNTHETIC path handed to the classifier; none reads the tree, so they are
# deterministic and are re-verified by `--check`.
ESTABLISHMENT_PROBES = [
    ("a_directory_no_rule_names/anything.txt", None,
     "THE LOAD-BEARING PROBE. A file in a top-level directory the table does not name must reach "
     "the unclassified STOP. If this probe ever classifies, the STOP has stopped being able to "
     "fire and the empty bucket has stopped meaning anything."),
    ("src/composing/analysis/chordanalyzer.cpp", "our-analysis-source",
     "the analysis source the whole project is about"),
    ("src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml",
     "our-analysis-tests-and-fixtures",
     "a catalog file — inside the composing module but claimed by the tests rule, which is "
     "ordered first"),
    ("src/engraving/dom/chordlist.cpp", "upstream-application-source",
     "MuseScore's own code, including the file carrying a recorded fork-local edit"),
    ("src/importexport/mei/thirdparty/libmei/att.cpp", "third-party-vendored-code",
     "a vendored library NESTED inside a module — the directory-name rule must reach it, not only "
     "the copy at the repository root"),
    ("CLAUDE.md", "governing-documents",
     "a governing document, which must not fall through to the repository-root catch-all"),
    ("cowork_rulings_2026_08_15_period_start.md", "writing-side-ruling-records",
     "a ruling record, which must not fall through to the general `cowork_` design class"),
    ("cc_instruction_artifact_inventory.md", "dispatches-to-the-coding-side",
     "a dispatch, which must not fall through to the general `cc_` report class"),
    ("zzz_a_file_nobody_has_written_yet.txt",
     "stray-working-files-committed-to-the-repository-root",
     "an unnamed file AT the repository root — this one is caught on purpose, and the contrast "
     "with the first probe is the whole point of bounding the last rule"),
]

ESTABLISHMENT_CAVEAT = (
    "#19, NOT DISCHARGED HERE. The signature table above is AUTHORED, and the only thing that "
    "checks it is the unclassified STOP — which establishes that every file matched SOME rule, and "
    "nothing at all about whether it matched the RIGHT one. A file sitting in a directory whose "
    "name misdescribes it is classed by the misdescription, and this tool cannot know. What would "
    "settle the other half is a reading of a sample of members per class against the class's own "
    "stated signature, which is an act named here and not started. A reader may not take an empty "
    "unclassified bucket as evidence that the classification is correct.")


def git(*args) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def resolve(rev: str) -> str:
    sha = git("rev-parse", rev).strip()
    if len(sha) != 40:
        raise Stop(f"{rev} did not resolve to a full commit identity: {sha!r}")
    return sha


def tree_entries(commit: str):
    """Every entry of the named commit's tree, read from the git object by explicit hash."""
    raw = git("ls-tree", "-r", "-l", commit)
    entries = []
    for line in raw.split("\n"):
        if not line.strip():
            continue
        meta, path = line.split("\t", 1)
        file_mode, kind, sha, size = meta.split()
        entries.append({"path": path.strip('"'), "kind": kind, "object": sha,
                        "bytes": 0 if size == "-" else int(size)})
    plain = git("ls-tree", "-r", "--name-only", commit)
    expected = len([x for x in plain.split("\n") if x.strip()])
    if len(entries) != expected:
        raise Stop(f"the walk produced {len(entries)} entries where the tree names {expected} — "
                   f"the walk dropped something and is not publishing a short list")
    return entries


def classify(path: str) -> tuple[str, int]:
    base = posixpath.basename(path)
    ext = base[base.rfind("."):].lower() if "." in base[1:] else ""
    for index, (name, _signature, matcher, _descend) in enumerate(SIGNATURE_TABLE):
        if matcher(path, base, ext):
            return name, index
    return "", -1


def reject_if_unclassified(paths: list[str]) -> None:
    """The unclassified STOP, in ONE place so the establishment probe below exercises the same
    code path `build` does rather than a re-statement of it (#6)."""
    if paths:
        raise Stop(f"{len(paths)} file(s) matched no rule in the signature table — this is the "
                   f"dispatch's own stop rule and prediction P1's refutation condition. "
                   f"First ten: {paths[:10]}")


def run_establishment_probes() -> list:
    """Hand synthetic paths to the classifier and check each lands where it must (#19)."""
    results = []
    for path, expected, why in ESTABLISHMENT_PROBES:
        got, _index = classify(path)
        got_name = got or None
        if got_name != expected:
            raise Stop(f"establishment probe failed: {path!r} classified as {got_name!r} where "
                       f"{expected!r} was required — {why}")
        results.append({"probe_path": path,
                        "required": expected if expected else "UNCLASSIFIED — the STOP fires",
                        "observed": got_name if got_name else "UNCLASSIFIED — the STOP fires",
                        "agrees": True,
                        "why_this_probe_exists": why})

    # The probes above establish that the CLASSIFIER returns nothing for an unnamed directory.
    # This one establishes the other half — that the STOP actually raises on such a path — by
    # calling the very function `build` calls, so the two cannot drift apart.
    fired = False
    try:
        reject_if_unclassified(["a_directory_no_rule_names/anything.txt"])
    except Stop:
        fired = True
    if not fired:
        raise Stop("the unclassified STOP did not raise when handed an unclassified path — the "
                   "empty bucket in this artifact would then mean nothing")
    results.append({"probe_path": "(the STOP itself, handed one unclassified path)",
                    "required": "raises and halts the tool",
                    "observed": "raises and halts the tool",
                    "agrees": True,
                    "why_this_probe_exists":
                        "The classifier probe above shows a path CAN come back unclassified; this "
                        "shows the tool then STOPS. Without both halves an empty bucket is "
                        "consistent with a stop rule that never runs."})
    return results


def build(commit: str) -> dict:
    probes = run_establishment_probes()
    entries = tree_entries(commit)

    unclassified = []
    per_class_paths: dict[str, list] = defaultdict(list)
    per_class_bytes: Counter = Counter()
    per_class_ext: dict[str, Counter] = defaultdict(Counter)
    for e in entries:
        name, _index = classify(e["path"])
        if not name:
            unclassified.append(e["path"])
            continue
        e["class"] = name
        per_class_paths[name].append(e)
        per_class_bytes[name] += e["bytes"]
        base = posixpath.basename(e["path"])
        per_class_ext[name][base[base.rfind("."):].lower() if "." in base[1:] else "(no extension)"] += 1

    reject_if_unclassified(unclassified)

    empty = [name for name, _s, _m, _d in SIGNATURE_TABLE if not per_class_paths.get(name)]
    if empty:
        raise Stop(f"these classes match nothing in the tree at {commit[:10]}: {empty}. A rule "
                   f"that has stopped applying is a rule about a tree that no longer exists.")

    classes = []
    for order, (name, signature, _matcher, descend) in enumerate(SIGNATURE_TABLE):
        members = sorted(per_class_paths[name], key=lambda x: x["path"])
        block = {
            "class": name,
            "order_in_the_signature_table": order,
            "signature": signature,
            "files": len(members),
            "total_bytes": per_class_bytes[name],
            "extensions_present": dict(sorted(per_class_ext[name].items(),
                                              key=lambda kv: (-kv[1], kv[0]))),
            "example_paths": [m["path"] for m in members[:6]],
            "the_ruling_surface_descends_into_this_class": bool(descend),
        }
        if descend:
            block["every_member"] = [{"path": m["path"], "bytes": m["bytes"]} for m in members]
        classes.append(block)

    # ── the untracked appendix (assumption A2) ───────────────────────────────────────────────────
    # NOT classified, paths only.  It is a reading of the WORKING TREE and therefore a dated one;
    # `--check` excludes it from the byte comparison and says so, because a guard that fails the
    # moment anyone writes a scratch file teaches a reader to ignore the guard set.
    untracked = sorted(p for p in git("ls-files", "--others",
                                      "--exclude-standard").split("\n") if p.strip())
    ignored = sorted(p for p in git("ls-files", "--others", "--ignored", "--exclude-standard",
                                    "--directory", "--no-empty-directory").split("\n") if p.strip())
    scratch_prefixes = ("scratch_artifacts/", "cowork_scratch_")
    untracked_records = [p for p in untracked if not p.startswith(scratch_prefixes)]
    untracked_scratch = [p for p in untracked if p.startswith(scratch_prefixes)]
    ignored_root_files = [p for p in ignored if "/" not in p]
    ignored_directories = [p for p in ignored if "/" in p or p.endswith("/")]

    art = {
        "what_this_is": (
            "THE ARTIFACT INVENTORY: every file the named commit's tree carries, classified by an "
            "authored signature over its path and its extension alone, with the unclassified "
            "bucket empty or the tool stopped. It proposes no role, no mining verdict and no "
            "retirement — those are authored on the ruling surface and ruled by the user. It "
            "moves, renames, retires and deletes nothing."),
        "dispatch": "cc_instruction_artifact_inventory.md",
        "generator": "tools/audit/gen_artifact_inventory.py",
        "reproduce": ("python tools/audit/gen_artifact_inventory.py --check   # re-derives at the "
                      "commit recorded below and exits 1 on drift, then re-runs the "
                      "classification at the current tree and stops if anything is unclassified"),
        "derived_at_commit": commit,
        "★_the_establishment_caveat_of_the_signature_table": ESTABLISHMENT_CAVEAT,
        "what_is_AUTHORED_here": {
            "the_signature_table": (
                "Which path shapes name which class, in which order, and what each class is "
                "called. Published in full beside every class as its `signature`, so the rule can "
                "be checked against the members without reading the generator."),
            "the_signature_kinds_used": (
                "PATH and EXTENSION only. The dispatch admits a banner as a third kind and none "
                "is used: no file's content was read to class it, which is assumption A1 held at "
                "its strongest available reading."),
            "nothing_else": (
                "No role, no mining verdict, no retirement flag, no judgment about whether any "
                "listed file should exist."),
        },
        "what_is_DERIVED": [
            "the population — every entry of the named commit's tree, read from the git object",
            "every count, every total in bytes, every extension tally and every example path",
            "the per-file class assignment for every class the ruling surface descends into",
            "the untracked appendix, which is a dated reading of the working tree",
        ],
        "the_population": {
            "entries_in_the_tree": len(entries),
            "classified": len(entries) - len(unclassified),
            "unclassified": len(unclassified),
            "★_unclassified_is_a_STOP_not_a_bucket": (
                "The dispatch's own stop rule. A non-empty bucket halts this tool before it "
                "writes, so a committed artifact carrying an empty bucket is the only kind that "
                "can exist."),
            "classes_in_the_signature_table": len(SIGNATURE_TABLE),
            "total_bytes": sum(e["bytes"] for e in entries),
        },
        "the_signature_tables_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not": (
                "They establish that the unclassified STOP CAN fire — the first probe is a path "
                "in a top-level directory no rule names, and it must come back unclassified — and "
                "that eight ordering-sensitive placements land where the table says they do. They "
                "establish NOTHING about whether any real file is in the right class; that is the "
                "caveat above, and it is not discharged by a green probe."),
            "probes": probes,
            "every_probe_agrees": all(p["agrees"] for p in probes),
        },
        "the_classes": classes,
        "P1_the_registered_expectation_graded": {
            "★_what_this_grading_is_and_is_not": (
                "The expectation is the dispatch's own, registered before this ran. It carries no "
                "authority. Where a limb differs the derived value governs and the difference is "
                "published as a FINDING — nothing here is adjusted to make a limb agree."),
            "taken_at": P1_SOURCE,
            "limb_1_coverage": {
                "expectation": "the unclassified bucket is empty",
                "derived": "empty",
                "agrees": True,
                "★_what_this_does_and_does_not_establish": (
                    "It establishes that every file matched some rule. It establishes nothing "
                    "about whether it matched the right one — see the caveat above."),
            },
            "limb_2_class_count": {
                "expectation": f"well under {P1_CLASS_CEILING} classes",
                "derived": len(SIGNATURE_TABLE),
                "agrees": len(SIGNATURE_TABLE) < P1_CLASS_CEILING,
                "comfortably_under": len(SIGNATURE_TABLE) <= P1_CLASS_CEILING * 0.75,
                "★_where_the_classes_actually_sit": (
                    "P1's sentence attaches a reason to its ceiling — that the upstream code, the "
                    "build system and the third-party libraries are each ONE class, \"so the "
                    "fork's size costs nothing\". That reason held. The count below is the "
                    "arithmetic that shows where the classes went instead: the material this "
                    "project did not author is a small number of classes covering most of the "
                    "files, and the class count is driven almost entirely by OUR OWN prose, "
                    "record and tooling — which is where prediction P2 already expected the "
                    "per-item descent to be needed."),
                "the_partition_is_AUTHORED": (
                    "Which classes hold material this project did not author is a judgment about "
                    "provenance, not a signature. It is published only to read the count against "
                    "P1's own stated reason, and it grades no file."),
                "not_authored_by_this_project": {
                    "classes": len(CLASSES_NOT_AUTHORED_BY_THIS_PROJECT),
                    "files": sum(c["files"] for c in classes
                                 if c["class"] in CLASSES_NOT_AUTHORED_BY_THIS_PROJECT),
                    "class_names": list(CLASSES_NOT_AUTHORED_BY_THIS_PROJECT),
                },
                "authored_by_this_project": {
                    "classes": len(SIGNATURE_TABLE) - len(CLASSES_NOT_AUTHORED_BY_THIS_PROJECT),
                    "files": sum(c["files"] for c in classes
                                 if c["class"] not in CLASSES_NOT_AUTHORED_BY_THIS_PROJECT),
                },
            },
            "limb_3_one_class_each_for_the_three_named_subjects": {
                subject: {
                    "class": name,
                    "files": next(c["files"] for c in classes if c["class"] == name),
                    "total_bytes": next(c["total_bytes"] for c in classes if c["class"] == name),
                    "is_exactly_one_class": True,
                } for subject, name in P1_SINGLE_CLASS_SUBJECTS.items()
            },
        },
        "P2_is_graded_at_the_ruling_surface": P2_SOURCE,
        "appendix_untracked_and_ignored_paths_NOT_classified": {
            "★_why_they_are_listed_rather_than_classed": (
                "Assumption A2 of the dispatch: the population is the TRACKED tree, and an "
                "untracked file is either scratch or an un-landed record — both for the user to "
                "see, not for a tool to grade. The appendix is present even when empty."),
            "★_why_this_block_is_excluded_from_the_reproduce_check": (
                "It is a reading of the WORKING TREE, not of a git object, so it moves whenever "
                "anyone writes a file. `--check` compares everything else byte for byte and "
                "reports this block's agreement separately, because a guard that goes red the "
                "moment a scratch file is written teaches a reader to ignore the guard set."),
            "★_IGNORED_FILES_ARE_LISTED_TOO_AND_THIS_IS_WHY": (
                "`git status` reports only untracked files that no ignore rule covers, and this "
                "repository ignores `/cc_*.md` — the whole dispatch-and-report family. Listing "
                "only the un-ignored half would therefore have hidden exactly the class A2 exists "
                "to surface: an un-landed record. The ignored half is listed at the repository "
                "root file by file; ignored DIRECTORIES are listed collapsed, because they are "
                "build output and dependency trees."),
            "untracked_candidate_records": {
                "what_they_are": ("untracked, not ignored, and not inside a directory the record "
                                  "names as scratch"),
                "count": len(untracked_records),
                "paths": untracked_records,
            },
            "untracked_inside_a_scratch_directory": {
                "what_they_are": ("untracked, not ignored, inside `scratch_artifacts/` or a dated "
                                  "`cowork_scratch_*` directory"),
                "count": len(untracked_scratch),
                "paths": untracked_scratch,
            },
            "ignored_files_at_the_repository_root": {
                "what_they_are": ("present on disk, covered by an ignore rule, sitting at the "
                                  "repository root — the class that contains un-landed records"),
                "count": len(ignored_root_files),
                "paths": ignored_root_files,
            },
            "ignored_directories_collapsed": {
                "what_they_are": ("ignored directories, listed by their own name rather than "
                                  "walked — build output, dependency trees and editor state"),
                "count": len(ignored_directories),
                "paths": ignored_directories,
            },
        },
        "what_this_does_NOT_do": (
            "It moves, renames, retires, archives and deletes nothing. It edits no document, "
            "opens no file's content, changes no measured value, and touches nothing under "
            "`src/`, `tools/corpus/` or `tools/robust_stop/`. It proposes no verdict of any kind: "
            "role, mining and retirement are authored on the ruling surface and ruled by the "
            "user. It closes no open-items row and writes no decisions-register entry."),
    }
    return art


APPENDIX_KEY = "appendix_untracked_and_ignored_paths_NOT_classified"


def render(art: dict) -> str:
    return json.dumps(art, indent=1, ensure_ascii=False) + "\n"


def main(argv: list[str]) -> int:
    if "--check" in argv:
        if not OUT.exists():
            print("FAIL: artifact missing:", OUT)
            return 1
        committed = json.loads(OUT.read_text(encoding="utf-8"))
        recorded = committed.get("derived_at_commit")
        if not recorded:
            print("FAIL: the committed artifact records no commit to re-derive at")
            return 1
        rebuilt = build(recorded)

        frozen_committed = dict(committed)
        frozen_rebuilt = dict(rebuilt)
        appendix_agrees = frozen_committed.get(APPENDIX_KEY) == frozen_rebuilt.get(APPENDIX_KEY)
        frozen_committed[APPENDIX_KEY] = "(excluded from the comparison — see the block itself)"
        frozen_rebuilt[APPENDIX_KEY] = "(excluded from the comparison — see the block itself)"
        if render(frozen_committed) != render(frozen_rebuilt):
            print("FAIL: re-derivation at", recorded[:10], "differs from the committed artifact")
            return 1

        # the LIVE half — the classification must still cover the tree as it stands now.
        current = resolve("HEAD")
        build(current)      # raises Stop on an unclassified file or an empty class
        print(f"OK: the inventory re-derives at {recorded[:10]}, and the signature table still "
              f"covers the tree at {current[:10]} with nothing unclassified.")
        print(f"    the untracked appendix {'also matches' if appendix_agrees else 'has moved'} "
              f"— excluded from the comparison by design.")
        return 0

    commit = resolve("HEAD")
    art = build(commit)
    OUT.write_text(render(art), encoding="utf-8", newline="")
    print("wrote", OUT)
    pop = art["the_population"]
    print(f"  tree at {commit[:10]}: {pop['entries_in_the_tree']} entries, "
          f"{pop['classified']} classified, {pop['unclassified']} unclassified, "
          f"{pop['classes_in_the_signature_table']} classes")
    g = art["P1_the_registered_expectation_graded"]
    print(f"  P1 coverage limb agrees: {g['limb_1_coverage']['agrees']}; "
          f"class-count limb agrees: {g['limb_2_class_count']['agrees']} "
          f"({g['limb_2_class_count']['derived']} classes)")
    ap = art[APPENDIX_KEY]
    print(f"  appendix: {ap['untracked_candidate_records']['count']} untracked candidate records, "
          f"{ap['untracked_inside_a_scratch_directory']['count']} untracked scratch, "
          f"{ap['ignored_files_at_the_repository_root']['count']} ignored at the root, "
          f"{ap['ignored_directories_collapsed']['count']} ignored directories")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
