#!/usr/bin/env python3
"""gen_harness_dispositions.py — Pass-1 (blind enumerative) dispositions for the
SHARED-HARNESS population of the EG-7 layer-5 + instruments certification audit.

Scope: every deep inventory row tagged INSTRUMENT-HARNESS in the committed layer-5
partition (tools/audit/l5/pass1_partition.json) — i.e. the 870 rows of
tools/batch_analyze.cpp (functions + numeric literals + branches + cross-layer
includes). This is the third and last pass-1 session (after the dormant resolver and
the Python instruments); the whole-scope second pass and the certification decision
are separate.

Protocol (cowork_audit_protocol.md):
  P1  the row list is machine-generated (this script only READS the committed
      l5_*.csv inventory; it invents no rows).
  P2  every row gets a verdict from a CLOSED set — no silent skip. The harness is
      BOTH a program with production-shaped behavior and an instrument, so:
        functions   -> SURVIVES              (live harness code; nothing retires)
        literals     -> ESTABLISHED / UNFIT / DEAD  (with a manifest-presence note
                                                      where the value is inference-affecting)
        branches     -> SURVIVES
        crosslayer   -> SURVIVES              (the top driver legitimately consumes
                                               every layer's published surface)
      "no issue" is itself a recorded verdict with a stated reason.
  P3  the contract direction (BUILD_AND_TEST.md / printHelp / docs) is checked in
      BOTH directions; the code->doc gaps (flags parsed but absent from help) are
      flagged rows here.
  P4  behavioral characterization is recorded in the report, not this file.

This script is VERDICT-EMBODYING (it encodes this session's dispositions). It is the
harness analogue of gen_resolver_dispositions.py / gen_instruments_core_dispositions.py
/ gen_grading_fitting_dispositions.py.

Output (stamped to HEAD + corpus hash c50002fee1):
  tools/audit/l5/pass1_dispositions_harness.csv   — every row, one verdict each
  tools/audit/l5/pass1_dispositions_harness.json  — per-class counts + flagged rows
"""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
TARGET = "tools/batch_analyze.cpp"
CORPUS_HASH = "c50002fee1"

# ── The flagged rows (findings), keyed by (kind, line) — plain-language slugs, no
#    invented numbering. Each carries a one-sentence plain-language note. Everything
#    NOT listed here gets the default verdict for its kind (a recorded "no issue"). ──

# LITERAL findings ------------------------------------------------------------------
DEFAULT_MODE_PRIOR_LINES = list(range(196, 217))  # the 21 hand-set "Default" mode priors
ONSET_THRESHOLD_LINES = {597, 2555, 3718}         # onsetBoundaryThreshold = 0.25 (x3)
# Preset scoring constants that ARE recorded in tools/param_manifest.json (G2/G3/G5/G6):
PRESET_CONST_LINES = {4220, 4223, 4226, 4227, 4228, 4229, 4230, 4231,
                      4235, 4236, 4248, 4249, 4255, 4256, 4277}

LITERAL_FLAGS = {}
for ln in DEFAULT_MODE_PRIOR_LINES:
    LITERAL_FLAGS[ln] = (
        "default-preset-mode-priors-hand-copied",
        "One of 21 mode-prior values hand-copied from composingconfiguration.cpp into "
        "applyPreset()'s 'Default' branch; sync is enforced ONLY by a code comment "
        "(no mechanical check) and the values are NOT recorded in tools/param_manifest.json "
        "(which is chord-scoring scoped) — a value-copied inference-affecting constant "
        "(guiding #6 unification / #17f manifest).")
for ln in ONSET_THRESHOLD_LINES:
    LITERAL_FLAGS[ln] = (
        "onset-boundary-threshold-hardcoded",
        "onsetBoundaryThreshold is hard-coded to 0.25, duplicating the "
        "IComposingAnalysisConfiguration default the user-facing bridge reads; a "
        "documented latent divergence (roadmap 0.6) — the two coincide today but nothing "
        "mechanically keeps them equal, so a config-default change would make batch stop "
        "measuring the user pipeline.")

# BRANCH findings (the arg parser) --------------------------------------------------
BRANCH_FLAGS = {
    3982: ("flags-absent-from-help",
           "'--reachback-ab' is parsed here but is absent from printHelp() and "
           "BUILD_AND_TEST.md (documented only in an in-code comment) — an undocumented "
           "measurement mode on the shared harness (contract code->doc)."),
    4093: ("flags-absent-from-help",
           "The five '--key-in-*' emission-weight override flags are parsed here but are "
           "absent from printHelp() and BUILD_AND_TEST.md (documented only in an in-code "
           "comment) — undocumented measurement modes on the shared harness (contract "
           "code->doc)."),
    4593: ("standard-output-crlf-vs-diagnostic-lf",
           "The standard analysis output file is opened with QIODevice::Text, so on Windows "
           "the committed .ours.json corpus is written with CRLF line endings; every "
           "diagnostic path instead writes with std::ofstream(std::ios::binary) (LF only). "
           "The two output paths use different line-ending disciplines; corpus byte-identity "
           "holds only while regeneration stays on Windows with Text mode (confirmed CRLF vs "
           "LF and reproduce-identical this session)."),
}

# FUNCTION findings -----------------------------------------------------------------
# The inventory's over-capture-biased C++ scanner emitted a spurious function row for a
# CALL site; and main() carries the abrupt-exit asymmetry note.
FUNCTION_FLAGS = {
    (748, 749): ("inventory-overcapture-call-as-function",
                 "Not a second definition of locateMeasureByTick — this is a CALL site "
                 "inside convertNotationRegion; the over-capture-biased C++ inventory "
                 "scanner (bias disclosed in tools/audit/l5/manifest.json) emitted a "
                 "spurious function row. The real definition is at 438-470."),
    (3859, 4622): ("exit-path-asymmetry",
                   "main() ends the standard analysis path by force-exiting "
                   "(TerminateProcess/std::_Exit, bypassing static destructors to dodge a "
                   "Qt-TLS shutdown hang), while the ~10 diagnostic early-return paths "
                   "return normally and DO run that destructor sequence; the two exit "
                   "disciplines are inconsistent (whether the diagnostic returns are ever "
                   "exposed to the same 'some runs' hang is unestablished — not observed on "
                   "--validate-slices/--decode-chords this session)."),
}


# ── Rule-based default classification for the un-flagged majority ──────────────────

def literal_class(line: int, value: str, func: str, context: str) -> tuple[str, str]:
    """Return (subclass, note) for an ESTABLISHED literal. Every literal in this file
    is ESTABLISHED — a formatting precision, a music-theory constant (pitch-class
    arithmetic), a structural cap/index, an init value, or a diagnostic-only threshold
    on a default-off path (never on the byte-identical corpus surface)."""
    v = value.strip()
    if line in PRESET_CONST_LINES:
        return ("inference-affecting-manifested",
                "Per-carrier preset scoring constant delivered by the preset builder; "
                "recorded in tools/param_manifest.json (G2/G3/G5/G6). NOTE: the manifest's "
                "batch_analyze.cpp line references (~3843-3898) are stale vs HEAD (~4220-4256).")
    # diagnostic-only thresholds / bounds on default-off paths
    diag_notes = {
        1787: "per-PC display floor (0.001) in the --diagnose-measures dump (default off).",
        1820: "oracle-cell display cutoff (0.75 of top) in --diagnose-measures (default off).",
        1388: "'uncertain' display flag bar (keySeqMargin<1.0) in --dump-region-keymargin (default off).",
        2565: "range-set cap (24) bounding the --reachback-ab diagnostic (default off; HELD).",
        2596: "reach-back hard step bound (8) on the --reachback-ab diagnostic (default off; HELD).",
        3267: "impassable override bar (1e9) disabling the fine-grain override on the "
              "--fullspine-no-override probe arm (default off).",
    }
    if line in diag_notes:
        return ("diagnostic-threshold", diag_notes[line])
    if line in (667, 719):
        return ("serialization-projection",
                "appendCappedAlternatives cap (3) — the documented per-consumer batch "
                "serialization projection (FQ-6); value unchanged.")
    # music-theory pitch-class arithmetic
    if v in ("12", "7") or (v == "3" and "%" in context) or (v == "6" and "f > 6" in context):
        return ("music-theory", "Pitch-class / fifths arithmetic (12 pcs, 7=fifths-per-step); a music-theory fact.")
    if v == "16" and "keyKey" in func:
        return ("structural", "keyKey() hash offset (join-probe dedup); structural, output-neutral.")
    if v == "64" and "keyKey" in func:
        return ("structural", "keyKey() hash stride (mode*64); structural, output-neutral.")
    # formatting precision / buffer sizes
    if v in ("3", "4", "5", "6") and ("fmtDouble" in context or "precision" in context):
        return ("formatting", "fmtDouble output precision (significant digits); serialization formatting.")
    if v in ("8", "64") and "buf" in context:
        return ("formatting", "stack buffer size for snprintf; structural.")
    if v in ("0.0", "1.0", "0.00"):
        return ("init-or-neutral", "Neutral initializer / beat base (1.0) / zero default; output-structural.")
    if v in ("2",) and ("size()" in context or "< 2" in context or ">= 2" in context or "ok ? 0 : 2" in context):
        return ("structural", "Cardinality guard / exit-code constant; structural.")
    return ("formatting-or-structural",
            "Serialization precision, index, buffer size, or structural cardinality "
            "constant; output-structural, not an inference lever.")


def function_role(name: str) -> tuple[str, str]:
    OUTPUT_SURFACES = {
        "writeJson", "writeKeyCandidateDump", "writeCadenceAnchorJson", "writeModulationJson",
        "writeJointKeyJson", "writeTonicizationJson", "writeL5Json", "writeRegionKeyMarginJson",
        "writeFanoutJson", "writeDiagnosticJson", "runSliceValidation", "runKeyModeDecode",
        "runReachBackAB", "runChordDecode", "runVlDump", "runFullSpine", "runJointProbe",
        "fsGroupingJson",
    }
    PIPELINE = {"analyzeScore", "analyzeScoreNotation", "convertNotationRegion",
                "convertNotationRegions", "inferLocalKey", "main"}
    if name == "applyPreset":
        return ("preset-builder",
                "The preset builder: the named presets read the single-source "
                "modePriorPresets() table (published, consumed — good); the 'Default' branch "
                "hand-copies composingconfiguration.cpp (see the flagged mode-prior rows).")
    if name in OUTPUT_SURFACES:
        return ("output-surface",
                "Instrument output surface. Establishment: it CLAIMS to serialize the named "
                "analysis view; the diagnostic dumps return before / append after the "
                "standard writeJson and are default-off, so the committed corpus is "
                "byte-identical (reproduce-check confirmed this session).")
    if name in PIPELINE:
        return ("pipeline-driver",
                "Drives the real analysis pipeline (regionanalyzer / keyresolver / "
                "chordanalyzer) and shapes its output into the serialized AnalyzedRegion.")
    return ("plumbing",
            "Harness plumbing / formatting helper (JSON escaping, name mappers, module "
            "init, score load, staff eligibility, measure location); no inference decision.")


def branch_role(func: str, kind: str) -> str:
    if func == "main":
        return ("Argument-parse / dispatch / disk-write branch in main(); routes to the "
                "standard path or a default-off diagnostic path.")
    return (f"Serialization / guard {kind} branch in {func}; shapes JSON output or guards "
            "an edge case (empty regions, missing measure, absent chord).")


def crosslayer_note(target: str) -> str:
    if target == "external":
        return "Include of an external framework header (Qt / muse / engraving); harness substrate."
    return (f"Cross-layer include of the '{target}' analysis area; the top-level driver "
            "legitimately consumes that layer's published surface (dependency-appropriate).")


# ── Build the disposition rows ─────────────────────────────────────────────────────

def read_rows(csv_name: str) -> list[dict]:
    path = HERE / csv_name
    with path.open(newline="", encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh) if r["file"] == TARGET]


def main() -> None:
    out_rows: list[dict] = []
    flagged: list[dict] = []

    def emit(kind, ident, line, func, context, verdict, subclass, note,
             flag_slug=None, manifest_present=None):
        row = {
            "kind": kind, "ident": ident, "line": line, "func": func,
            "verdict": verdict, "subclass": subclass,
            "manifest_present": ("" if manifest_present is None else manifest_present),
            "flag": ("yes" if flag_slug else ""), "finding_slug": (flag_slug or ""),
            "note": note, "context": context,
        }
        out_rows.append(row)
        if flag_slug:
            flagged.append({"kind": kind, "line": line, "func": func,
                            "finding_slug": flag_slug, "note": note})

    # functions ---------------------------------------------------------------------
    for r in read_rows("l5_functions.csv"):
        name = r["name"]
        sl, el = int(r["start_line"]), int(r["end_line"])
        subclass, note = function_role(name)
        flag = FUNCTION_FLAGS.get((sl, el))
        if flag:
            emit("function", name, sl, name, f"[{sl}-{el}]", "SURVIVES",
                 subclass, flag[1], flag_slug=flag[0])
        else:
            emit("function", name, sl, name, f"[{sl}-{el}]", "SURVIVES", subclass, note)

    # literals ----------------------------------------------------------------------
    for r in read_rows("l5_literals.csv"):
        line = int(r["line"])
        value, func, context = r["value"], r["func"], r["context"]
        flag = LITERAL_FLAGS.get(line)
        subclass, note = literal_class(line, value, func, context)
        manifest = ("yes" if line in PRESET_CONST_LINES else
                    ("no" if (line in DEFAULT_MODE_PRIOR_LINES or line in ONSET_THRESHOLD_LINES)
                     else "n/a"))
        if flag:
            emit("literal", value, line, func, context, "ESTABLISHED",
                 subclass, flag[1], flag_slug=flag[0], manifest_present=manifest)
        else:
            emit("literal", value, line, func, context, "ESTABLISHED",
                 subclass, note, manifest_present=manifest)

    # branches ----------------------------------------------------------------------
    for r in read_rows("l5_branches.csv"):
        line = int(r["line"])
        kind, func, context = r["kind"], r["func"], r["context"]
        flag = BRANCH_FLAGS.get(line)
        if flag:
            emit("branch", kind, line, func, context, "SURVIVES",
                 "arg-parse-dispatch", flag[1], flag_slug=flag[0])
        else:
            emit("branch", kind, line, func, context, "SURVIVES",
                 ("arg-parse-dispatch" if func == "main" else "serialization-guard"),
                 branch_role(func, kind))

    # crosslayer --------------------------------------------------------------------
    for r in read_rows("l5_crosslayer.csv"):
        line = int(r["line"])
        target, context = r["target_area"], r["include"]
        emit("crosslayer", target, line, "<includes>", context, "SURVIVES",
             ("external-substrate" if target == "external" else "layer-consume"),
             crosslayer_note(target))

    # ── stamp + write ──────────────────────────────────────────────────────────────
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(REPO),
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        head = "unknown"

    verdict_counts: dict[str, int] = {}
    subclass_counts: dict[str, int] = {}
    for r in out_rows:
        verdict_counts[r["verdict"]] = verdict_counts.get(r["verdict"], 0) + 1
        key = f'{r["kind"]}:{r["subclass"]}'
        subclass_counts[key] = subclass_counts.get(key, 0) + 1

    # distinct findings (slug -> count of rows + representative note)
    findings: dict[str, dict] = {}
    for f in flagged:
        slug = f["finding_slug"]
        if slug not in findings:
            findings[slug] = {"slug": slug, "rows": 0, "note": f["note"],
                              "lines": []}
        findings[slug]["rows"] += 1
        findings[slug]["lines"].append(f["line"])

    csv_path = HERE / "pass1_dispositions_harness.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "kind", "ident", "line", "func", "verdict", "subclass",
            "manifest_present", "flag", "finding_slug", "note", "context"])
        w.writeheader()
        for r in sorted(out_rows, key=lambda x: (x["line"], x["kind"])):
            w.writerow(r)

    summary = {
        "audit": "EG-7 Layer-5 + instruments certification, PASS 1 (blind) — SHARED HARNESS",
        "population": "INSTRUMENT-HARNESS (tools/batch_analyze.cpp)",
        "instruction": "cc_instruction_l5_audit_pass1_harness.md",
        "head_commit": head,
        "corpus_hash": CORPUS_HASH,
        "total_rows": len(out_rows),
        "row_counts_by_kind": {
            "function": sum(1 for r in out_rows if r["kind"] == "function"),
            "literal": sum(1 for r in out_rows if r["kind"] == "literal"),
            "branch": sum(1 for r in out_rows if r["kind"] == "branch"),
            "crosslayer": sum(1 for r in out_rows if r["kind"] == "crosslayer"),
        },
        "verdict_counts": verdict_counts,
        "subclass_counts": subclass_counts,
        "flagged_row_count": len(flagged),
        "findings": sorted(findings.values(), key=lambda d: -d["rows"]),
        "reproduce_check": ("byte-identical vs tools/corpus/{baroque,jazz,default} — "
                            "352/352 each preset (this session, scratch regen)"),
    }
    json_path = HERE / "pass1_dispositions_harness.json"
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"rows={len(out_rows)}  flagged={len(flagged)}  findings={len(findings)}")
    print(f"by kind: {summary['row_counts_by_kind']}")
    print(f"verdicts: {verdict_counts}")
    print(f"wrote {csv_path.name} + {json_path.name}")


if __name__ == "__main__":
    main()
