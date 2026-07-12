#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# EG-7 Layer-5 + instruments certification — PASS 1, partition 2a (the regression-stop-core
# instruments: the 7 measurement-chain .py files the project's regression stops stand on).
# The disposition generator (protocol P1/P2, #17(f) generated-artifact rule): it enumerates
# EVERY deep inventory row tagged to the 7 core instrument files and assigns each a verdict
# from the closed rubric, with a stated reason. "No issue" is itself a recorded claim with a
# reason (P2). Findings are encoded as explicit per-row overrides (keyed by file+line+table),
# never hand-typed into the output. Findings the mechanical ast inventory did not emit a row
# for (bare except-handlers, a string dict, a unary-minus sentinel) are appended as auditor
# 'finding(auditor)' rows (P3 negative-space) so none is lost.
#
# Reads the committed inventory CSVs under tools/audit/l5/ (scope, not verdicts) and writes
# pass1_dispositions_instruments_core.csv + .json. Read-only over the corpus and production
# code (an audit instrument, not inference code). Findings are identified by plain-language
# slug (the audit convention — no invented numbering scheme, matching gen_resolver_dispositions.py);
# the Fnn 'ref' column is a compact within-report cross-reference index only.
#
# Run:  python tools/audit/l5/gen_instruments_core_dispositions.py
import csv, json, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))

CORE = [
    "tools/a8_rebaseline_measure.py", "tools/compare_analyses.py", "tools/compare_rn.py",
    "tools/characterise_bir_false.py", "tools/dcml_parser.py", "tools/robust_stop_diff.py",
    "tools/run_bach_preset.py",
]
TABLES = ["functions", "literals", "branches", "fields", "io", "crosslayer"]
DEAD_FUNCS = {("tools/dcml_parser.py", "parse_dcml_file"), ("tools/dcml_parser.py", "find_dcml_file")}

SLUGS = {
 "F1": "dead-parse-dcml-file-superseded",
 "F2": "dead-find-dcml-file-unreferenced",
 "F3": "compute-root-pc-broad-except-silent-none",
 "F4": "resolve-dcml-key-broad-except-silent-globalkey-fallback",
 "F5": "region-alignment-overlap-tolerance-hand-set",
 "F6": "measure-length-four-four-assumption-in-extrapolation",
 "F7": "quality-normalise-map-completeness-unproven",
 "F8": "root-pc-minus-one-sentinel-false-agreement",
 "F9": "note-name-to-pc-mapping-duplicated-three-sites",
 "F10": "score-piece-bare-except-silent-whole-piece-drop",
 "F11": "normalise-rn-strips-all-parenthetical-figures",
 "F12": "corrupt-ours-json-folded-into-no-wir-count",
 "F13": "cell-class-split-no-independent-cross-check",
 "F14": "validate-corpus-dir-skips-music21-json-fingerprint",
 "F15": "manifest-omits-music21-json-fingerprint",
 "F16": "robust-stop-diff-reads-rekeyed-manifest-no-cross-check",
 "F17": "per-score-subprocess-timeout-hardcoded",
 "F18": "music21-version-detection-truncated-read-window",
}

# finding: (file, line, table_or_None) -> (verdict, ref, note). table None = synthetic auditor row.
FINDINGS = {
 ("tools/dcml_parser.py", 76, "functions"):  ("RETIRES", "F1", "parse_dcml_file: superseded DCML-TSV parser; NO live consumer (referenced only in its own docstring example). Duplicates parse_abc_harmonies_file's concern (#6); still carries the pre-P0 bare `except (ValueError,KeyError): continue` silent-drop pattern (:108), dormant because unconsumed."),
 ("tools/dcml_parser.py", 475, "functions"): ("RETIRES", "F2", "find_dcml_file: DEAD - zero references anywhere in the repo. TSV lookup is done by compare_rn._find_tsv; WiR by find_wir_file. Waste (#6/#12)."),
 ("tools/dcml_parser.py", 189, None): ("SURVIVES", "F3", "_compute_root_pc broad `except Exception: return None`: a mis-parse returns root_pc=None (carried, not dropped) - but a SYSTEMATIC numeral mis-parse silently reduces GT root coverage (region reads as 'no GT root'). Silent-mask risk; narrower except would surface it. [Inventory: ast branch extractor emits no row for except-handlers.]"),
 ("tools/dcml_parser.py", 451, None): ("SURVIVES", "F4", "_resolve_dcml_key broad `except Exception: return globalkey`: any key-resolution error silently falls back to globalkey (wrong local tonic -> wrong root_pc), unlogged. Silent-fallback establishment concern."),
 ("tools/compare_analyses.py", 216, "literals"): ("UNFIT", "F5", "0.5 alignment overlap tolerance (lenient-OR >=50% of EITHER duration). THE core region-alignment measurement decision; rationale documented, value hand-set (not derived/oracle-established). Governs batch-stop + secondary-metric + oracle-metric alignment (NOT the robust grid, which unions boundaries)."),
 ("tools/compare_analyses.py", 516, "literals"): ("UNFIT", "F5", "0.5 DCML overlap tolerance (_best_dcml_match_by_overlap) - same hand-set alignment tolerance as :216."),
 ("tools/compare_analyses.py", 549, "literals"): ("UNFIT", "F5", "0.5 beat-snap tolerance (legacy align mode) - hand-set; legacy backward-compat path."),
 ("tools/compare_analyses.py", 449, "literals"): ("UNFIT", "F6", "`4 * tpb` = hardcoded 4-beats-per-measure assumption in _dcml_tick_for's extrapolation-beyond-anchors fallback. Silent approximation for non-4/4 meters; affects WiR/rntxt alignment (the path lacking abs_tick)."),
 ("tools/compare_analyses.py", 453, "literals"): ("UNFIT", "F6", "`4 * tpb` (second extrapolation branch) - same hardcoded 4/4 assumption as :449."),
 ("tools/compare_analyses.py", 128, None): ("SURVIVES", "F7", "_QUALITY_NORMALISE table: a quality string NOT in the map passes through unnormalised (_norm_quality returns as-is), so an unmapped variant could yield a false quality (dis)agreement. Completeness not proven against both producers' full quality vocabularies. [Inventory: string dict, not a numeric literal.]"),
 ("tools/compare_analyses.py", 99, None): ("SURVIVES", "F8", "root_pc default -1 sentinel on missing rootPitchClass: two regions BOTH missing root compare equal (-1==-1) in _roots_match -> false chord agreement. three_way_classify guards on None not -1, so only the two-way region compare is exposed. [Inventory: unary-minus 1 excluded as trivial.]"),
 ("tools/compare_rn.py", 222, None): ("SURVIVES", "F9", "note-name->pitch-class mapping is DUPLICATED across three sites: dcml_parser._NOTE_TO_PC (:124) and compare_rn._KB_NOTE_DCML (:222) / _KB_NOTE_OURS (:223). One concern (#6) in 3 copies; the _KB_ pair is a declared verbatim port of key_confound.py, still un-unified. (The individual pc values are FACT theory constants; this row records the structural duplication.)"),
 ("tools/compare_rn.py", 514, None): ("SURVIVES", "F10", "score_piece bare `except Exception: return None`: a corrupt ours.json/tsv silently drops the WHOLE piece from the aggregate with no skip counter (unlike dcml_parser's skipped-collector). A systematically failing piece silently shrinks the denominator."),
 ("tools/compare_rn.py", 655, None): ("SURVIVES", "F10", "grid_score_piece_tsv bare `except: return None` - same silent whole-piece drop on the grid path."),
 ("tools/compare_rn.py", 120, "functions"): ("SURVIVES", "F11", "normalise_rn strips ALL parenthetical figures on BOTH sides (_PAREN_FIG_RE): DCML 'V(b9)' vs ours 'V' scores 'exact'. Documented leniency but it can mask a real extension difference in the exact/partial split."),
 ("tools/a8_rebaseline_measure.py", 290, "branches"): ("SURVIVES", "F12", "measure_preset `except Exception: continue` on load_analysis: a corrupt .ours.json is silently folded into the no_wir coverage count (conflates parse-failure with no-WiR-annotation); the gate denominator loses the score with no distinct 'corrupt' accounting."),
 ("tools/a8_rebaseline_measure.py", 97, "functions"): ("SURVIVES", "F13", "cell_class: the class-(a)/(b) split (the hard-stop-governing quantity) is a pure pc-set test on our_region.pitch_class_set. Inherits the RN-bucket self-validation transitively (validated cell membership) but has NO independent second implementation cross-checking the class split. Missing pitchClassSet -> class 'b' (conservative/safe)."),
 ("tools/characterise_bir_false.py", 50, "functions"): ("SURVIVES", "F14", "validate_corpus_dir fingerprints (sha256) only .ours.json, NOT the paired .music21.json ground truth. A stale/foreign music21 export passes the contamination gate undetected - yet a8's variant-(a) genuine filter + this tool's BIR gate READ .music21.json. Establishment gap in the corpus-integrity guard."),
 ("tools/run_bach_preset.py", 77, "functions"): ("SURVIVES", "F15", "_write_manifest records size+sha256 for .ours.json ONLY; music21_version is copy-through informational, explicitly 'NOT enforced'. Root cause of F14: the manifest carries no .music21.json fingerprint, so the GT half is unverifiable at measure time."),
 ("tools/robust_stop_diff.py", 90, "functions"): ("SURVIVES", "F16", "ref_class_durs reads the reference class-(b) baseline from the RE-KEYED manifest.json (separate R10-a assembly) rather than from tools/robust_stop/summary.json (a8's direct output, identical schema to the candidate). No cross-check of the manifest figure vs the run-enumeration it ships beside; a partial re-baseline of one artifact but not the other compares against a stale baseline silently. (Byte-consistent TODAY.)"),
 ("tools/run_bach_preset.py", 206, "literals"): ("SURVIVES", "F17", "subprocess timeout=120s per score: exceed -> FAILED -> complete=False -> fail-loud (not silent). Hardcoded per-score wall; noted, not a defect."),
 ("tools/run_bach_preset.py", 68, "literals"): ("SURVIVES", "F18", "_detect_music21_version reads only the first 4000 chars of each .xml; if <software> is beyond that, returns None silently. Informational only (version not enforced) - minor."),
}
STRENGTH = {
 ("tools/a8_rebaseline_measure.py", 205, "branches"): "STRENGTH: self-validation - variant-(b) bucket_dur asserted byte-identical to the pinned grid_score_regions() per piece; AssertionError on divergence (faithful-reuse proof, principle 19).",
 ("tools/robust_stop_diff.py", 76, "branches"): "STRENGTH: parse_runs fails LOUDLY on any run-line format drift (raises) - enforces the CLAUDE.md 'must not silently shrink the diff base' guarantee.",
 ("tools/characterise_bir_false.py", 91, "branches"): "STRENGTH: per-stem sha256 match vs manifest - the anti-contamination (M3) mechanism, shared with a8 via import (#6).",
 ("tools/run_bach_preset.py", 516, "branches"): "STRENGTH: fail-loud completeness - sys.exit(1) unless ours_count==expected_count (expected derived from the .xml glob).",
}
DORMANT_FIELDS = {"cadence", "phraseend", "figbass", "pedal"}

_THEORY_CTX = ("% 12", "_degree_semitones", "_note_to_pc", "_pc_to_note", "_kb_note",
               "semitones =", "'c': 0", "'i': 0", "0:'c'", "0: 'c'", "degree_idx in (5, 6)",
               "(5, 6)", "(0, 3, 6, 10)", "_t_invariant", "_kb_note_ours", "_kb_note_dcml")

def classify_literal(value, context, func):
    ctx = context.lower()
    if any(t in ctx for t in _THEORY_CTX):
        return ("FACT", "", "pitch-class / diatonic-degree / modular-interval constant (music theory) - e.g. note->pc, scale-degree semitone table, or octave-12 arithmetic.")
    if value in ("480", "480.0"):
        return ("ESTABLISHED", "", "TICKS_PER_QUARTER (batch_analyze ticks/480 convention); documented + verified tick-for-tick on 18 pieces/3 corpora (audit L4.1). Established measurement constant.")
    if value == "12":
        return ("FACT", "", "octave = 12 semitones - pitch-class modular arithmetic (music theory).")
    if value == "9600":
        return ("ESTABLISHED", "", "CLASS_A_INVESTIGATE_TICKS advisory threshold (~20 quarter-notes); documented rationale, ADVISORY-only (never the hard stop).")
    if value in ("100", "100.0"):
        return ("SURVIVES", "", "x100 percentage scaling in a report/summary - presentation.")
    if value in ("40", "70", "65", "200") and ("*" in context or "'='" in context or "min(" in context or "[:200" in context or "<" in context):
        return ("SURVIVES", "", "report formatting literal (bar width / separator / truncation) - presentation.")
    if value == "120":
        return ("SURVIVES", "", "subprocess per-score timeout (seconds); exceed -> FAILED -> fail-loud. Infra wall.")
    if value == "4000":
        return ("SURVIVES", "", "read-window for the music21 <software> tag; miss -> None (informational only).")
    if value == "99":
        return ("SURVIVES", "", "-99 sentinel for a missing alternative rootPitchClass (never a valid pc 0-11).")
    return ("SURVIVES", "", "structural index / slice / small numeric literal in library logic - not an inference-affecting constant.")

def base_verdict(table, row):
    f = row["file"]; func = row.get("func", "")
    if table == "functions":
        name = row.get("name", "")
        if (f, name) in DEAD_FUNCS:
            return ("RETIRES", "", f"{name}: dead/superseded instrument function.")
        return ("SURVIVES", "", f"{name}(): live instrument function on the measurement/library path.")
    if table == "literals":
        return classify_literal(row.get("value", ""), row.get("context", ""), func)
    if table == "branches":
        if (f, func) in DEAD_FUNCS:
            return ("RETIRES", "", f"branch inside dead function {func}() - retires with it.")
        return ("SURVIVES", "", f"control-flow guard in {func}() - live measurement/library path.")
    if table == "fields":
        owner = row.get("type_owner", ""); name = row.get("name", "")
        if name in DORMANT_FIELDS and f == "tools/dcml_parser.py":
            return ("PUBLISHED", "", f"DcmlRegion.{name}: additive L6/N10/N20 oracle channel, carried verbatim; declared-dormant (consumer named: parse_cadence_phrase_markers / Wave-3), not waste.")
        return ("SURVIVES", "", f"{owner}.{name}: dataclass field on the compare surface - carried/consumed on the measurement path.")
    if table == "io":
        return ("SURVIVES", "", f"{row.get('call','')} in {func}() - read/write of the measurement I/O surface.")
    if table == "crosslayer":
        return ("SURVIVES", "", f"internal import of {row.get('include','')} - measurement-chain unification DAG (reuse, not duplication).")
    return ("SURVIVES", "", "row.")

def main():
    rows_out = []
    counts = collections.Counter()
    seen = set()
    for table in TABLES:
        with open(os.path.join(HERE, f"l5_{table}.csv"), encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row["file"] not in CORE:
                    continue
                f = row["file"]; ln = int(row.get("line") or row.get("start_line") or 0)
                verdict, ref, note = base_verdict(table, row)
                fk = (f, ln, table)
                if fk in FINDINGS:
                    verdict, ref, note = FINDINGS[fk]; seen.add(fk)
                if fk in STRENGTH:
                    note = note + "  " + STRENGTH[fk]
                counts[verdict] += 1
                rows_out.append({"file": f, "line": ln, "table": table,
                                 "name_or_value": row.get("name") or row.get("value") or row.get("call") or row.get("include") or "",
                                 "func": row.get("func", ""), "verdict": verdict,
                                 "finding_slug": SLUGS.get(ref, ""), "ref": ref, "note": note})
    inv = len(rows_out)
    for (f, ln, tbl), (verdict, ref, note) in FINDINGS.items():
        if tbl is None:
            counts[verdict] += 1
            rows_out.append({"file": f, "line": ln, "table": "finding(auditor)",
                             "name_or_value": SLUGS.get(ref, ref), "func": "", "verdict": verdict,
                             "finding_slug": SLUGS.get(ref, ""), "ref": ref, "note": note})
        else:
            assert (f, ln, tbl) in seen, f"finding not matched to inventory row: {(f,ln,tbl)}"

    rows_out.sort(key=lambda r: (r["file"], r["line"], r["table"]))
    with open(os.path.join(HERE, "pass1_dispositions_instruments_core.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "line", "table", "name_or_value", "func", "verdict", "finding_slug", "ref", "note"])
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    perfile = collections.defaultdict(lambda: collections.Counter())
    flags = collections.defaultdict(list)
    for r in rows_out:
        perfile[r["file"]][r["verdict"]] += 1
        if r["ref"]:
            flags[r["ref"]].append(f"{r['file']}:{r['line']}")
    summary = {
        "audit": "EG-7 L5+instruments PASS-1 partition-2a (regression-stop core, 7 files)",
        "instruction": "cc_instruction_l5_audit_pass1_instruments.md",
        "head_commit": "dc2d564f9e", "corpus_hash": "c50002fee1",
        "scope_files": CORE,
        "inventory_rows": inv, "synthetic_finding_rows": len(rows_out) - inv, "total_rows": len(rows_out),
        "verdict_counts": dict(counts),
        "per_file_verdict": {k: dict(v) for k, v in perfile.items()},
        "findings": {SLUGS.get(k, k): {"ref": k, "sites": v} for k, v in sorted(flags.items())},
    }
    with open(os.path.join(HERE, "pass1_dispositions_instruments_core.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)
    print("inventory rows:", inv, "+ synthetic:", len(rows_out) - inv, "= total:", len(rows_out))
    print("verdicts:", dict(counts))
    print("findings:", {SLUGS.get(k, k): len(v) for k, v in sorted(flags.items())})

if __name__ == "__main__":
    main()
