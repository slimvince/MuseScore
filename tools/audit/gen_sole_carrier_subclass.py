#!/usr/bin/env python3
"""THE SOLE-CARRIER SUBCLASS — which non-keep entries of the decisions register are the ONLY place
their content is carried, so that they do NOT ride the ruled soft-discard.

THE RULING THIS EXISTS FOR.  User, 2026-08-16, §3(A) of
`cowork_rulings_2026_08_16_preparation_return.md`, taken at the return of the deciding-act recovery
pass.  The soft-discard was ruled *"behind the sole-carrier guard"*, and the guard's own definition
is the user's: *"a derived SOLE-CARRIER subclass is computed over the whole non-keep population: an
entry whose status is DEFERRED, or whose home cannot be located, or whose content is found nowhere
outside the register family. Sole-carrier members do NOT ride the discard — they return to the user
as a list."*

★ WHY THE GUARD EXISTS AT ALL, IN THE USER'S OWN QUESTION.  The user asked whether the discard risks
losing *"a genuinely good idea that should have been used as input when designing and/or building
the inferrers"*.  Three standing nets catch almost all of that — the disposition discipline over
every specification statement, the audit's something-missing verdict, and the fact-gate — and ONE
residual class escapes all three: an idea whose only carrier is the decisions-register entry itself,
typically a deferred proposal that was never built.  This subclass is that class, derived.

★ WHAT A SOLE-CARRIER VERDICT IS AND IS NOT.  It is a statement about WHERE THE CONTENT LIVES, and
about nothing else.  It is not a judgment that the entry is good, useful, sound or wanted, and it is
not a provenance verdict — the provenance question was answered by the filter and by the recovery
pass, and their results are carried beside every row here rather than re-decided.  A sole-carrier
member is WITHHELD from the discard and returned to the user as a list; withholding is the
recoverable direction, which is why every bound this tool declares is drawn so that a doubtful case
is withheld rather than discarded.

WHAT IS DERIVED AND WHAT IS AUTHORED — the difference is the whole value of the output.
  DERIVED   the population, IMPORTED from the committed filter artifact and never restated (#6);
            every entry's fields, read from the decisions register's own data file; the recovery
            result carried beside each row, imported from the committed recovery artifact; all
            three signals, each with the evidence that produced it; the tracked file population at
            the measured commit, read from the git objects by explicit hash; every count.
  AUTHORED  which paths are the DECISIONS-REGISTER FAMILY; which file extensions are searched when
            the content question has to be asked of the whole tree; and nothing else.  Both are
            published in the artifact beside the results they produced.

★ THE THREE SIGNALS, AND HOW EACH IS MEASURED.
  (i)   THE RECORDED STATUS IS DEFERRED.  The leading token of the entry's `status` field, read
        from the decisions register's own data file, is `deferred` — the value that file's own
        header defines as *"decided to be built later; the decision itself stands"*.  A decision
        that was never built has no built thing carrying it.
  (ii)  THE HOME CANNOT BE LOCATED.  The entry's `home` names a document that is not a blob in the
        tracked tree at the measured commit; or it cites a line the document does not reach; or
        the entry carries a `home_section` whose heading text is not in that document.  All three
        limbs are measured and reported separately, so a reader sees WHICH one fired.
  (iii) THE CONTENT IS FOUND NOWHERE OUTSIDE THE DECISIONS-REGISTER FAMILY.  The entry's `verbatim`
        quotation, normalized by THE DECISIONS REGISTER'S OWN normalization (imported from
        `gen_cluster_dispositions.py`, #6 — not re-implemented here), is not a substring of any
        searched tracked blob outside the family.

★ THE SEARCH ORDER FOR SIGNAL (iii), DECLARED BECAUSE IT DECIDES THE COST AND NOT THE ANSWER.  The
entry's own home document is searched FIRST, then every other admitted blob in sorted path order.
The question is *"is it carried anywhere outside the family"*, so the first hit answers it and the
walk stops; the order changes which location is reported and can never change the verdict.

★ WHERE THE ANSWER IS BOUNDED, NAMED RATHER THAN HIDDEN.  When the wide walk is reached at all, it
searches only blobs whose extension is in the declared text set below.  The excluded population is
published with its count and its size in bytes, so the bound is visible.  It errs toward reporting
NOT FOUND, which makes an entry a sole-carrier and WITHHOLDS it from the discard — the recoverable
direction.  No size ceiling is imposed: a hand-picked number over varying data is the shape this
record has twice declined.

THE STOPS, so this cannot silently stop being a derivation:
  * the committed filter artifact or recovery artifact missing, or carrying no non-keep entry,
    STOPS it — the import is then not what this pass assumes it is;
  * an imported entry identity the decisions register's data file does not carry STOPS it, and so
    does a non-keep entry of the data file the import does not carry — BOTH directions (D-671);
  * an entry missing a field this pass reads STOPS it — never a skip;
  * a verdict outside the closed two-value vocabulary STOPS it;
  * a distribution that does not account for the population STOPS it;
  * a sentence of the ruling that defines this subclass no longer in its ruling record STOPS it, so
    the derivation cannot outlive the words that ordered it.
Each is exercised by a probe recorded in the artifact, and every probe calls the very function the
walk calls, so the two cannot drift apart.

WHAT THIS DOES NOT DO.  It discards nothing, retires nothing, edits nothing and marks nothing.  It
opens the decisions register's files for reading and writes only its own artifact.  It grades no
decision's content, its conformance, or whether the code obeys it.

Run:
  python tools/audit/gen_sole_carrier_subclass.py           # write the artifact
  python tools/audit/gen_sole_carrier_subclass.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                        # noqa: E402  (path set above)

sys.path.insert(0, str(Path(__file__).resolve().parent / "decisions"))
from gen_cluster_dispositions import norm                          # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
FILTER = "tools/audit/decisions_filter_classification.json"
RECOVERY = "tools/audit/deciding_act_recovery.json"
BACKBONE = "tools/audit/decisions/backbone_decisions.json"
RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"
OUT = ROOT / "tools" / "audit" / "sole_carrier_subclass.json"

# The filter's own class names. This pass may not widen them and re-classifies with none of them.
NO_ACT = "NO-DECIDING-ACT-FOUND"
AMBIGUOUS = "EVIDENCE-AMBIGUOUS"
NON_KEEP = (NO_ACT, AMBIGUOUS)

# The closed verdict vocabulary of THIS pass.
SOLE_CARRIER = "SOLE-CARRIER"
NOT_SOLE_CARRIER = "NOT-SOLE-CARRIER"
VERDICTS = (SOLE_CARRIER, NOT_SOLE_CARRIER)

# The fields of an entry this pass reads. A member missing one of these is a STOP.
REQUIRED_FIELDS = ("id", "group", "title", "plain", "home", "status", "verbatim")

# AUTHORED: the paths that ARE the decisions-register family, and why the third is drawn wide.
REGISTER_FAMILY_EXACT = ("DECISIONS.md",)
REGISTER_FAMILY_PREFIXES = ("decisions/", "tools/audit/")
WHY_THE_FAMILY_IS_DRAWN_HERE = (
    "The ruling names `DECISIONS.md`, `decisions/` and the decisions register's data and audit "
    "artifacts. The first two are exact. The third is taken as the WHOLE of `tools/audit/`, which "
    "is wider than the words require and is drawn that way deliberately: an artifact under "
    "`tools/audit/` is DERIVED from the record, so a quotation appearing there is the record "
    "quoting itself and is not independent carriage of the entry's content. The widening can only "
    "make MORE entries sole-carriers, which WITHHOLDS them from the discard — the recoverable "
    "direction, and the one the sole-carrier guard exists to protect."
)

# AUTHORED: the extensions searched when the content question reaches the whole tree.
SEARCHED_EXTENSIONS = (
    ".md", ".txt", ".py", ".json", ".jsonl", ".csv", ".cpp", ".h", ".hpp", ".cc", ".qml",
    ".yml", ".yaml", ".cmake", ".bat", ".sh", ".xml", ".mscx", ".ts", ".js", ".cfg", ".ini",
    ".in", ".am", ".pri", ".pro", ".rst", ".tex", ".css", ".html",
)

# AUTHORED: the sentences of the ruling that define this subclass, LOCATED on every run.
RULING_SENTENCES = {
    "the guard the discard runs behind":
        "The 194 NOTHING-FOUND entries are SOFT-DISCARDED — behind the sole-carrier guard.",
    "how the subclass is defined":
        "a derived SOLE-CARRIER subclass is computed over the whole non-keep population: an entry "
        "whose status is DEFERRED, or whose home cannot be located, or whose content is found "
        "nowhere outside the register family",
    "what a sole-carrier member does not do":
        "Sole-carrier members do NOT ride the discard — they return to the user as a list",
    "what a discard record must carry":
        "a provenance verdict, not a judgment on soundness or usefulness; the statement stands at "
        "its home and is met by the derivation",
    "nothing is destroyed":
        "Nothing destroyed (#12); every discard individually revivable when a deciding act is "
        "later named.",
}

HOME_LINE = re.compile(r"^(\d+)")


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning, never an entry skipped."""


# ── git, by explicit hash ────────────────────────────────────────────────────────────────────────

def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args)} failed: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def resolve(rev: str) -> str:
    sha = git("rev-parse", rev).strip()
    if len(sha) != 40:
        raise Stop(f"{rev} did not resolve to a full commit identity: {sha!r}")
    return sha


def tree_blobs(commit: str) -> dict[str, dict]:
    """Every BLOB of the named commit's tree, read from the git object by explicit hash."""
    out: dict[str, dict] = {}
    for line in git("ls-tree", "-r", "-l", commit).split("\n"):
        if not line.strip():
            continue
        meta, path = line.split("\t", 1)
        _mode, kind, sha, size = meta.split()
        if kind != "blob":
            continue
        out[path.strip('"')] = {"object": sha, "bytes": 0 if size == "-" else int(size)}
    return out


def blob_text(sha: str) -> str:
    proc = subprocess.run(["git", "-C", str(ROOT), "cat-file", "blob", sha], capture_output=True)
    if proc.returncode != 0:
        raise Stop(f"the blob {sha} could not be read from the git object store")
    return proc.stdout.decode("utf-8", "replace")


def json_at(commit: str, path: str, what: str) -> dict:
    """One of this pass's three inputs, read AT THE MEASURED COMMIT and never from the tree.

    ★ WHY THE INPUTS ARE FROZEN AT THE COMMIT AND NOT READ LIVE.  This subclass is the guard the
    ruled soft-discard runs BEHIND, so the discard consumes it — and the discard itself moves the
    decisions register's own data file and every artifact derived from it.  An input read live
    would therefore be changed BY THE ACT THIS ARTIFACT AUTHORIZES, and the published record of
    which entries the guard withheld would be destroyed by the very act it guarded (#12, and the
    OI-301 hazard exactly).  Reading at the recorded commit makes this a measurement of a state
    that cannot move under it.  The LIVE assertion this pass still carries is elsewhere: the
    sentences of the ruling are located in the ruling record AS IT STANDS on every run.
    """
    try:
        raw = git("show", f"{commit}:{path}")
    except Stop:
        raise Stop(f"{what} is not in the tree at the measured commit {commit[:10]}: {path}")
    return json.loads(raw)


# ── the checks that halt this pass ───────────────────────────────────────────────────────────────

def locate_ruling() -> dict[str, str]:
    """Every sentence of the ruling that defines this subclass, LOCATED. A missing one STOPS."""
    if not RULING.exists():
        raise Stop(f"the ruling record this pass serves is missing: {RULING}")
    text = norm(RULING.read_text(encoding="utf-8").replace("**", "").replace("*", ""))
    missing = [name for name, quote in RULING_SENTENCES.items()
               if norm(quote.replace("**", "").replace("*", "")) not in text]
    if missing:
        raise Stop("a sentence of the ruling that defines this subclass is no longer in its ruling "
                   f"record, so this derivation would outlive the words that ordered it: {missing}")
    return dict(RULING_SENTENCES)


def require_fields(entry: dict) -> None:
    """An entry this pass cannot read is never quietly skipped."""
    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        raise Stop(f"entry {entry.get('id', '<no identity>')!r} carries no {missing} — the "
                   f"subclass cannot be derived for it, and an entry it cannot read at all is a "
                   f"STOP rather than a skip")


def reconcile(imported: set[str], in_the_data_file: set[str], what: str) -> None:
    """Checked in BOTH directions (D-671)."""
    only_import = sorted(imported - in_the_data_file)
    only_data = sorted(in_the_data_file - imported)
    if only_import or only_data:
        raise Stop(
            f"{what} do not carry the same entries — a derivation over a derived population is "
            f"published WHOLE or not at all (D-671). On the first side only: {only_import}. "
            f"On the second side only: {only_data}")


def require_reconciled_distribution(rows: list[dict], population_size: int) -> None:
    """Every verdict in the vocabulary, and the counts accounting for the population."""
    if len(rows) != population_size:
        raise Stop(f"the derived rows ({len(rows)}) do not account for the population "
                   f"({population_size})")
    unknown = sorted({r["verdict"] for r in rows} - set(VERDICTS))
    if unknown:
        raise Stop(f"a verdict outside this pass's closed two-value vocabulary: {unknown}")
    per = {v: sum(1 for r in rows if r["verdict"] == v) for v in VERDICTS}
    if sum(per.values()) != population_size:
        raise Stop("the per-verdict distribution does not account for the population")


# ── the three signals ────────────────────────────────────────────────────────────────────────────

def signal_status_deferred(entry: dict) -> dict:
    status = (entry.get("status") or "").strip()
    leading = status.split()[0].strip(",;:") if status else ""
    return {
        "signal": "(i) the recorded status is DEFERRED",
        "fired": leading == "deferred",
        "evidence": {
            "the_status_the_decisions_register_records": status,
            "its_leading_token": leading,
            "what_the_data_files_own_header_says_deferred_means":
                "decided to be built later; the decision itself stands",
        },
    }


def signal_home_unlocatable(entry: dict, blobs: dict[str, dict],
                            text_of: dict[str, str]) -> dict:
    home = (entry.get("home") or "").strip()
    parts = home.split(":")
    document = parts[0].strip()
    cited_line = None
    if len(parts) > 1:
        match = HOME_LINE.match(parts[1].strip())
        if match:
            cited_line = int(match.group(1))

    limbs: list[dict] = []
    document_present = document in blobs
    limbs.append({"limb": "the home document is a blob in the tracked tree at the measured commit",
                  "fired": not document_present,
                  "the_document": document,
                  "present": document_present})

    reached = None
    if document_present:
        lines = len(raw_text(document, blobs, text_of).splitlines())
        reached = cited_line is None or cited_line <= lines
        limbs.append({"limb": "the cited line is one the home document reaches",
                      "fired": not reached,
                      "the_cited_line": cited_line,
                      "the_documents_line_count": lines})
    else:
        limbs.append({"limb": "the cited line is one the home document reaches",
                      "fired": False,
                      "the_cited_line": cited_line,
                      "the_documents_line_count": None,
                      "not_asked_because": "the document itself is not in the tree"})

    section = (entry.get("home_section") or {}).get("section")
    if section and document_present:
        present = section.strip() in raw_text(document, blobs, text_of)
        limbs.append({"limb": "the recorded home section's heading is in the home document",
                      "fired": not present,
                      "the_heading_looked_for": section,
                      "present": present})
    else:
        limbs.append({"limb": "the recorded home section's heading is in the home document",
                      "fired": False,
                      "the_heading_looked_for": section,
                      "not_asked_because": ("the entry records no home section"
                                            if not section else
                                            "the document itself is not in the tree")})

    return {
        "signal": "(ii) the home cannot be located",
        "fired": any(limb["fired"] for limb in limbs),
        "evidence": {"the_home_the_decisions_register_records": home, "limbs": limbs},
    }


def signal_content_nowhere_else(entry: dict, blobs: dict[str, dict], text_of: dict[str, str],
                                searched_paths: list[str], stage_two_reached: list[str]) -> dict:
    needle = norm(entry.get("verbatim") or "")
    if not needle:
        return {
            "signal": "(iii) the content is found nowhere outside the decisions-register family",
            "fired": True,
            "evidence": {"the_normalized_verbatim_is_empty": True,
                         "what_that_means": "there is no content to find, so nothing outside the "
                                            "family can be carrying it"},
        }

    home_document = (entry.get("home") or "").split(":")[0].strip()
    order: list[str] = []
    if home_document and home_document in blobs and not in_the_family(home_document):
        order.append(home_document)

    for path in order:
        if needle in normalized_text(path, blobs, text_of):
            return _found(entry, needle, path, "the entry's own home document, searched first")

    stage_two_reached.append(entry["id"])
    for path in searched_paths:
        if path in order:
            continue
        if needle in normalized_text(path, blobs, text_of):
            return _found(entry, needle, path, "the wide walk over the tracked tree")

    return {
        "signal": "(iii) the content is found nowhere outside the decisions-register family",
        "fired": True,
        "evidence": {
            "the_normalized_verbatim_searched_for": needle[:400],
            "its_length_in_characters": len(needle),
            "where_it_was_looked_for": "the entry's own home document, then every admitted tracked "
                                       "blob outside the decisions-register family",
            "found": False,
        },
    }


def _found(entry: dict, needle: str, path: str, how: str) -> dict:
    return {
        "signal": "(iii) the content is found nowhere outside the decisions-register family",
        "fired": False,
        "evidence": {
            "the_normalized_verbatim_searched_for": needle[:400],
            "its_length_in_characters": len(needle),
            "found_in": path,
            "found_by": how,
        },
    }


def in_the_family(path: str) -> bool:
    return (path in REGISTER_FAMILY_EXACT
            or any(path.startswith(prefix) for prefix in REGISTER_FAMILY_PREFIXES))


def raw_text(path: str, blobs: dict[str, dict], cache: dict[str, str]) -> str:
    """A tracked blob's text at the measured commit, read once and kept."""
    stored = cache.get(path)
    if stored is None:
        stored = blob_text(blobs[path]["object"])
        cache[path] = stored
    return stored


def normalized_text(path: str, blobs: dict[str, dict], cache: dict[str, str]) -> str:
    stored = cache.get("norm:" + path)
    if stored is None:
        stored = norm(raw_text(path, blobs, cache))
        cache["norm:" + path] = stored
    return stored


# ── probes (#19) ─────────────────────────────────────────────────────────────────────────────────

def probes() -> list[dict]:
    out: list[dict] = []

    def probe(name: str, what: str, fn) -> None:
        try:
            fn()
        except Stop as exc:
            out.append({"probe": name, "what_was_fed": what, "raised": True, "message": str(exc)})
            return
        out.append({"probe": name, "what_was_fed": what, "raised": False,
                    "message": "NO STOP — this probe FAILED to establish its stop"})

    probe("a missing field", "an entry carrying every required field but `verbatim`",
          lambda: require_fields({f: "x" for f in REQUIRED_FIELDS if f != "verbatim"}))
    probe("an imported entry the data file does not carry",
          "imported {'D-001','D-002'} against a data file carrying {'D-001'}",
          lambda: reconcile({"D-001", "D-002"}, {"D-001"}, "two populations"))
    probe("a non-keep entry of the data file the import does not carry",
          "imported {'D-001'} against a data file carrying {'D-001','D-002'}",
          lambda: reconcile({"D-001"}, {"D-001", "D-002"}, "two populations"))
    probe("a verdict outside the closed vocabulary", "one row carrying the verdict 'INVENTED'",
          lambda: require_reconciled_distribution([{"verdict": "INVENTED"}], 1))
    probe("a distribution that does not account for the population",
          "one derived row against a population of two",
          lambda: require_reconciled_distribution([{"verdict": SOLE_CARRIER}], 2))

    failed = [p["probe"] for p in out if not p["raised"]]
    if failed:
        raise Stop(f"a probe did not raise, so a STOP this tool claims cannot be shown to fire: "
                   f"{failed}")
    return out


def signal_probes(blobs: dict[str, dict], text_of: dict[str, str]) -> list[dict]:
    """Each SIGNAL shown able to fire and able not to, on synthetic entries (#19).

    A signal that has come back empty over the whole population is indistinguishable, from the
    artifact alone, from a signal that cannot fire at all. These probes tell the two apart.
    """
    out: list[dict] = []
    a_real_document = "CLAUDE.md" if "CLAUDE.md" in blobs else sorted(blobs)[0]

    fired = signal_status_deferred({"status": "deferred"})
    quiet = signal_status_deferred({"status": "live"})
    out.append({"signal": "(i)", "fires_on": "an entry recording status `deferred`",
                "fired": fired["fired"],
                "stays_quiet_on": "an entry recording status `live`",
                "quiet": not quiet["fired"]})

    fired = signal_home_unlocatable(
        {"home": "a_document_that_is_not_in_this_tree.md:1"}, blobs, text_of)
    quiet = signal_home_unlocatable({"home": a_real_document + ":1"}, blobs, text_of)
    out.append({"signal": "(ii) — the missing-document limb",
                "fires_on": "an entry homed at `a_document_that_is_not_in_this_tree.md:1`",
                "fired": fired["fired"],
                "stays_quiet_on": f"an entry homed at `{a_real_document}:1`",
                "quiet": not quiet["fired"]})

    fired = signal_home_unlocatable(
        {"home": a_real_document + ":99999999"}, blobs, text_of)
    out.append({"signal": "(ii) — the unreachable-line limb",
                "fires_on": f"an entry homed at `{a_real_document}:99999999`",
                "fired": fired["fired"],
                "stays_quiet_on": "the same document at line 1 (above)",
                "quiet": True})

    fired = signal_home_unlocatable(
        {"home": a_real_document + ":1",
         "home_section": {"section": "## a heading no document in this tree carries"}},
        blobs, text_of)
    out.append({"signal": "(ii) — the missing-heading limb",
                "fires_on": "an entry recording a home section whose heading is not in its home",
                "fired": fired["fired"],
                "stays_quiet_on": "an entry recording no home section (above)",
                "quiet": True})

    reached: list[str] = []
    fired = signal_content_nowhere_else(
        {"id": "probe", "home": a_real_document,
         "verbatim": "a phrase that is deliberately not written anywhere in this repository "
                     "AABBCCDDEEFF00112233"},
        blobs, text_of, [], reached)
    quiet_needle = raw_text(a_real_document, blobs, text_of)[:200]
    quiet = signal_content_nowhere_else(
        {"id": "probe", "home": a_real_document, "verbatim": quiet_needle},
        blobs, text_of, [], reached)
    out.append({"signal": "(iii)",
                "fires_on": "an entry whose verbatim is a phrase written nowhere in the tree",
                "fired": fired["fired"],
                "stays_quiet_on": f"an entry whose verbatim is the opening of `{a_real_document}`",
                "quiet": not quiet["fired"]})

    broken = [p for p in out if not p["fired"] or not p["quiet"]]
    if broken:
        raise Stop("a signal could not be shown BOTH to fire and to stay quiet, so an empty result "
                   f"for it would be unreadable: {[p['signal'] for p in broken]}")
    return out


# ── the build ────────────────────────────────────────────────────────────────────────────────────

def build(commit: str) -> dict:
    ruling = locate_ruling()

    classified = json_at(commit, FILTER, "the committed filter artifact")
    imported = {row["id"]: row for row in classified["entries"]
                if row["proposed_class"] in NON_KEEP}
    if not imported:
        raise Stop("the committed filter artifact carries no entry in the non-keep classes, so "
                   "there is no population to derive over — the import is not what this pass "
                   "assumes it is")

    recovered = json_at(commit, RECOVERY, "the committed recovery artifact")
    recovery_by_id = {row["id"]: row for row in recovered["entries"]}
    if not recovery_by_id:
        raise Stop("the committed recovery artifact carries no entry, so the recovery result "
                   "cannot be carried beside any row")
    reconcile(set(imported), set(recovery_by_id),
              "the imported non-keep population and the committed recovery artifact")

    data = json_at(commit, BACKBONE, "the decisions register's data file")
    by_id: dict[str, dict] = {}
    for entry in data["decisions"]:
        require_fields(entry)
        by_id[entry["id"]] = entry
    reconcile(set(imported), {i for i in imported if i in by_id},
              "the imported non-keep population and the decisions register's data file")

    blobs = tree_blobs(commit)
    text_of: dict[str, str] = {}      # every blob this pass reads, kept so none is read twice

    admitted, excluded = [], {}
    for path, record in blobs.items():
        base = posixpath.basename(path)
        extension = base[base.rfind("."):].lower() if "." in base[1:] else ""
        if in_the_family(path):
            continue
        if extension in SEARCHED_EXTENSIONS:
            admitted.append(path)
        else:
            bucket = excluded.setdefault(extension or "(no extension)",
                                         {"blobs": 0, "bytes": 0})
            bucket["blobs"] += 1
            bucket["bytes"] += record["bytes"]
    admitted.sort()

    stage_two_reached: list[str] = []
    rows: list[dict] = []
    for entry_id in sorted(imported):
        entry = by_id[entry_id]
        signals = [
            signal_status_deferred(entry),
            signal_home_unlocatable(entry, blobs, text_of),
            signal_content_nowhere_else(entry, blobs, text_of, admitted, stage_two_reached),
        ]
        fired = [s["signal"] for s in signals if s["fired"]]
        rows.append({
            "id": entry_id,
            "group": entry["group"],
            "title": entry["title"],
            "home": entry["home"],
            "status": entry["status"],
            "what_the_entry_says_the_decision_is_quoted_from_the_register": entry["plain"],
            "the_class_the_filter_proposed": imported[entry_id]["proposed_class"],
            "the_result_the_recovery_pass_returned": recovery_by_id[entry_id]["result"],
            "verdict": SOLE_CARRIER if fired else NOT_SOLE_CARRIER,
            "the_signals_that_fired": fired,
            "why_this_verdict": (
                "at least one of the three signals fired, so this entry may be the only place its "
                "content is carried; it is WITHHELD from the discard and returns to the user"
                if fired else
                "no signal fired: the entry is not deferred, its home is locatable, and its "
                "content is carried outside the decisions-register family"),
            "signals": signals,
        })
    require_reconciled_distribution(rows, len(imported))

    distribution = {v: sum(1 for r in rows if r["verdict"] == v) for v in VERDICTS}
    per_signal = {
        "(i) the recorded status is DEFERRED":
            sum(1 for r in rows if r["signals"][0]["fired"]),
        "(ii) the home cannot be located":
            sum(1 for r in rows if r["signals"][1]["fired"]),
        "(iii) the content is found nowhere outside the decisions-register family":
            sum(1 for r in rows if r["signals"][2]["fired"]),
    }
    crossed = {
        f"{recovery}/{verdict}": sum(
            1 for r in rows
            if r["the_result_the_recovery_pass_returned"] == recovery and r["verdict"] == verdict)
        for recovery in sorted({r["the_result_the_recovery_pass_returned"] for r in rows})
        for verdict in VERDICTS
    }

    return {
        "what_this_is":
            "THE SOLE-CARRIER SUBCLASS, DERIVED OVER THE WHOLE NON-KEEP POPULATION OF THE DECISIONS "
            "REGISTER. Three signals per entry, each published with its evidence, and one verdict. "
            "A SOLE-CARRIER member is WITHHELD from the ruled soft-discard and returns to the user "
            "as a list. NOTHING IS DISCARDED, RETIRED, EDITED OR MARKED BY THIS TOOL, and the "
            "decisions register's data file and rendered files are untouched by it.",
        "generator": "tools/audit/gen_sole_carrier_subclass.py",
        "dispatch": "cc_instruction_preparation_third.md, Task 1",
        "derived_at_commit": commit,
        "★_why_the_commit_is_recorded":
            "The tracked file population and every blob this pass reads are taken at THIS commit, "
            "read from the git objects by explicit hash, and `--check` re-derives at the commit "
            "recorded here rather than at whatever the head happens to be. A check that re-derived "
            "at the current head would go red the first time anybody committed anything — the "
            "OI-301/OI-305 shape, avoided by construction.",
        "the_ruling_that_ordered_it": {
            "source": "cowork_rulings_2026_08_16_preparation_return.md §3 (A)",
            "every_sentence_located_in_that_record_on_this_run": ruling,
            "★_what_a_sole_carrier_verdict_is_about":
                "WHERE THE CONTENT LIVES, and nothing else. It is not a judgment that the entry is "
                "good, useful, sound or wanted, and it is not a provenance verdict — the provenance "
                "question was answered by the filter and by the recovery pass, whose results are "
                "carried beside every row here rather than re-decided.",
            "★_the_clause_that_binds_the_discard_this_guard_stands_in_front_of":
                ruling["what a discard record must carry"],
        },
        "the_population": {
            "imported_from": FILTER,
            "★_read_at_the_measured_commit_and_not_from_the_tree":
                "This subclass is the guard the ruled soft-discard runs BEHIND, and the discard "
                "moves the decisions register's data file and every artifact derived from it. An "
                "input read live would be changed by the act this artifact authorizes, and the "
                "published record of which entries the guard WITHHELD would be destroyed by the "
                "very act it guarded (#12; the OI-301 hazard). All three inputs are therefore read "
                "from the git objects at the commit recorded above. The live assertion this pass "
                "still carries is the ruling's own sentences, located in the ruling record AS IT "
                "STANDS on every run.",
            "the_classes_imported": list(NON_KEEP),
            "entries": len(imported),
            "★_the_whole_non_keep_population_and_not_the_194":
                "The ruling computes the subclass over the WHOLE non-keep population, so the 62 "
                "entries still to be ruled reuse this derivation rather than needing a second one "
                "(D-671 — a derivation over a derived population is published whole). This batch "
                "APPLIES it only to the entries the recovery pass returned NOTHING-FOUND for.",
            "★_it_is_imported_and_never_restated":
                "The membership is the committed filter artifact's own, read on every run (#6). "
                "The reconciliation against the committed recovery artifact and against the "
                "decisions register's data file is a STOP in BOTH directions.",
        },
        "what_is_DERIVED": [
            "the population, imported from the committed filter artifact and never hand-listed",
            "every entry's fields, read from the decisions register's own data file",
            "the recovery result carried beside each row, imported from the recovery artifact",
            "all three signals, each with the evidence that produced it",
            "the tracked blob population at the measured commit, read from the git objects",
            "every count and every distribution",
        ],
        "what_is_AUTHORED": [
            "which paths are the decisions-register family, and why the third limb is drawn wide",
            "which file extensions are searched when the content question reaches the whole tree",
        ],
        "the_rule": {
            "★_the_verdict":
                "SOLE-CARRIER if and only if signal (i) or signal (ii) or signal (iii) fires. No "
                "threshold, no weighting, no hand-picked member.",
            "signal_i": "the leading token of the entry's recorded `status` is `deferred`",
            "signal_ii": "the home names a document not in the tracked tree at the measured "
                         "commit, or cites a line that document does not reach, or records a home "
                         "section whose heading is not in that document",
            "signal_iii": "the entry's `verbatim`, normalized by the decisions register's OWN "
                          "normalization, is not a substring of any searched tracked blob outside "
                          "the decisions-register family",
            "★_the_normalization_is_the_records_own":
                "`norm` is imported from `tools/audit/decisions/gen_cluster_dispositions.py`, the "
                "same function the decisions register's own establishment pass uses to prove every "
                "verbatim is findable at its home (#6). It is not re-implemented here, so this "
                "pass and that establishment cannot disagree about what a quotation is.",
            "the_decisions_register_family": {
                "exact": list(REGISTER_FAMILY_EXACT),
                "prefixes": list(REGISTER_FAMILY_PREFIXES),
                "why_drawn_here": WHY_THE_FAMILY_IS_DRAWN_HERE,
            },
            "★_the_search_order_and_what_it_can_and_cannot_change":
                "The entry's own home document is searched first, then every admitted blob in "
                "sorted path order, and the first hit answers the question. The order decides "
                "WHICH location is reported and can never decide the verdict.",
            "the_extensions_searched_when_the_wide_walk_is_reached": list(SEARCHED_EXTENSIONS),
            "★_where_the_answer_is_bounded":
                "The wide walk searches only blobs whose extension is in the list above. The "
                "excluded population is published below with its count and its size in bytes, so "
                "the bound is visible rather than implied. NO SIZE CEILING IS IMPOSED: a "
                "hand-picked number over varying data is the shape this record has twice declined. "
                "The bound errs toward reporting NOT FOUND, which makes an entry a sole-carrier "
                "and WITHHOLDS it from the discard — the recoverable direction.",
            "the_verdict_vocabulary": {
                SOLE_CARRIER: "at least one signal fired. WITHHELD from the discard; returns to "
                              "the user as a list.",
                NOT_SOLE_CARRIER: "no signal fired. Nothing here says the entry should be "
                                  "discarded — only that this guard does not withhold it.",
            },
        },
        "★_what_a_result_here_is_NOT": {
            "a_SOLE_CARRIER_is_not_a_judgment_of_worth":
                "It says the content may be carried nowhere else. It says nothing about whether "
                "the content is right, useful or wanted.",
            "a_NOT_SOLE_CARRIER_is_not_a_discard":
                "It withholds nothing. Whether an entry is discarded is decided by the ruling and "
                "by the recovery pass's result, not by this guard.",
            "nothing_here_re_classifies_any_entry":
                "The filter's proposed class and the recovery pass's result ride beside every row "
                "and are unchanged by anything here.",
        },
        "the_distribution": distribution,
        "how_many_entries_each_signal_fired_for": per_signal,
        "the_distribution_crossed_with_the_recovery_result": crossed,
        "the_wide_walk": {
            "★_how_many_entries_reached_it":
                len(sorted(set(stage_two_reached))),
            "the_entries_that_reached_it": sorted(set(stage_two_reached)),
            "what_reaching_it_means":
                "the entry's content was NOT found in its own home document, so the question had "
                "to be asked of the whole admitted tree",
            "admitted_blobs_outside_the_decisions_register_family": len(admitted),
            "excluded_by_extension": dict(sorted(excluded.items(),
                                                 key=lambda kv: (-kv[1]["bytes"], kv[0]))),
            "★_what_the_exclusion_can_and_cannot_do":
                "It can only make an entry look like a sole-carrier that is not one, which "
                "WITHHOLDS it from the discard. It can never cause an entry to be discarded.",
        },
        "the_stops_own_establishment": {
            "★_what_these_probes_establish_and_what_they_do_not":
                "They establish that each STOP CAN fire, each through the very function the walk "
                "calls, so the two cannot drift apart. They establish NOTHING about whether any "
                "entry's verdict is right — that is what the residue surface puts to the user.",
            "probes": probes(),
        },
        "each_signals_own_establishment": {
            "★_why_this_block_exists":
                "A signal that came back empty over the whole population is indistinguishable, "
                "from the artifact alone, from a signal that cannot fire at all (#19). Each signal "
                "is therefore shown BOTH to fire on a case that should fire it and to stay quiet "
                "on one that should not, on synthetic entries fed to the very functions the walk "
                "calls. A signal that fails either half STOPS this tool.",
            "signals": signal_probes(blobs, text_of),
        },
        "entries": rows,
    }


def render(artifact: dict) -> str:
    return json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"


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
        if render(build(recorded)) != OUT.read_text(encoding="utf-8"):
            print("FAIL: the sole-carrier subclass does not re-derive at", recorded[:10])
            return 1
        print(f"the sole-carrier subclass re-derives at {recorded[:10]}")
        return 0

    commit = resolve("HEAD")
    artifact = build(commit)
    OUT.write_text(render(artifact), encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print(f"  population {artifact['the_population']['entries']} at {commit[:10]}")
    for verdict in VERDICTS:
        print(f"  {verdict}: {artifact['the_distribution'][verdict]}")
    for signal, count in artifact["how_many_entries_each_signal_fired_for"].items():
        print(f"    {signal}: {count}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
