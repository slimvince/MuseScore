#!/usr/bin/env python3
"""Compare Bach batch_analyze output against local When in Rome analyses.

This comparator is annotation-centric:
for each When in Rome RomanText annotation, find the analyzed region that is
active at that annotation tick (or the nearest region start within a small
fallback window) and compare root pitch class.

It is intended as a structural reference for Bach chorales and avoids the
surface-label overlap bias of the music21 comparator.
"""

from __future__ import annotations

import argparse
import glob
import json
from collections import Counter
from pathlib import Path

import dcml_parser as dcml
from compare_when_in_rome import find_matching_region, load_our_regions, parse_analysis


def collect_json_files(ours_dir: str | Path, json_files: list[str] | None) -> list[str]:
    if json_files:
        return [str(Path(path)) for path in json_files]
    return sorted(glob.glob(str(Path(ours_dir) / "*.ours.json")))


def resolve_wir_analysis(wir_dir: str | Path, stem: str) -> str | None:
    return dcml.find_wir_file(str(wir_dir), stem)


def compare_file(
    json_path: str | Path,
    wir_dir: str | Path,
    beat_tolerance: float,
    ticks_per_beat: int,
) -> dict:
    json_file = Path(json_path)
    stem = json_file.name.replace(".ours.json", "")
    analysis_path = resolve_wir_analysis(wir_dir, stem)
    if analysis_path is None:
        return {
            "json_path": str(json_file),
            "analysis_path": None,
            "annotations": 0,
            "matched": 0,
            "agree": 0,
            "disagree": 0,
            "no_match": 0,
            "missing_analysis": True,
            "parse_error": False,
            "disagreements": [],
        }

    regions = load_our_regions(json_file)
    try:
        annotations = parse_analysis(analysis_path)
    except Exception as exc:
        return {
            "json_path": str(json_file),
            "analysis_path": str(analysis_path),
            "annotations": 0,
            "matched": 0,
            "agree": 0,
            "disagree": 0,
            "no_match": 0,
            "missing_analysis": False,
            "parse_error": True,
            "error": str(exc),
            "disagreements": [],
        }

    matched = 0
    agree = 0
    no_match = 0
    disagreements: list[tuple[object, object]] = []

    for annotation in annotations:
        region = find_matching_region(regions, annotation.tick, beat_tolerance, ticks_per_beat)
        if region is None:
            no_match += 1
            continue

        matched += 1
        if region.root_pc == annotation.root_pc:
            agree += 1
        else:
            disagreements.append((annotation, region))

    return {
        "json_path": str(json_file),
        "analysis_path": str(analysis_path),
        "annotations": len(annotations),
        "matched": matched,
        "agree": agree,
        "disagree": matched - agree,
        "no_match": no_match,
        "missing_analysis": False,
        "parse_error": False,
        "disagreements": disagreements,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ours-dir", default="tools/validation_bach_postport/corpus")
    parser.add_argument("--wir-dir", default="tools/dcml/when_in_rome")
    parser.add_argument("--beat-tolerance", type=float, default=0.5)
    parser.add_argument("--ticks-per-beat", type=int, default=480)
    parser.add_argument("--json-file", action="append", help="Compare only the given output JSON file")
    parser.add_argument("--show-disagreements", type=int, default=5)
    parser.add_argument("--summary-json", help="Write machine-readable summary JSON to this path")
    args = parser.parse_args()

    files = collect_json_files(args.ours_dir, args.json_file)

    files_compared = 0
    missing_analysis = 0
    parse_failures = 0
    total_annotations = 0
    matched = 0
    agree = 0
    no_match = 0
    per_file_results: list[dict] = []

    for json_path in files:
        result = compare_file(json_path, args.wir_dir, args.beat_tolerance, args.ticks_per_beat)
        per_file_results.append(result)

        if result["missing_analysis"]:
            missing_analysis += 1
            continue
        if result["parse_error"]:
            parse_failures += 1
            continue

        files_compared += 1
        total_annotations += result["annotations"]
        matched += result["matched"]
        agree += result["agree"]
        no_match += result["no_match"]

    disagree = matched - agree
    alignment_rate = (matched / total_annotations) if total_annotations else 0.0
    agreement_rate = (agree / matched) if matched else 0.0
    total_coverage = (agree / total_annotations) if total_annotations else 0.0

    summary = {
        "files_considered": len(files),
        "files_compared": files_compared,
        "files_with_missing_analysis": missing_analysis,
        "files_with_parse_failures": parse_failures,
        "total_annotations": total_annotations,
        "matched_annotations": matched,
        "no_match": no_match,
        "alignment_rate": alignment_rate,
        "agree": agree,
        "disagree": disagree,
        "root_agreement_rate": agreement_rate,
        "root_agreement_over_total_annotations": total_coverage,
    }

    print(f"Files considered: {len(files)}")
    print(f"Bach chorales with WIR analysis.txt: {files_compared}")
    print(f"Files with missing analysis.txt: {missing_analysis}")
    print(f"Files with parse failures: {parse_failures}")
    print(f"Total WIR annotations: {total_annotations}")
    print(f"Annotations matched to our regions: {matched}")
    print(f"No matching region: {no_match}  No-match rate: {(no_match / total_annotations):.1%}" if total_annotations else "No matching region: 0")
    print(f"Root agree: {agree}/{matched} = {agreement_rate:.1%}" if matched else "Root agree: N/A")
    print(f"Root disagree: {disagree}/{matched}" if matched else "Root disagree: N/A")
    print(f"Agreement over all annotations: {total_coverage:.1%}" if total_annotations else "Agreement over all annotations: N/A")

    shown = 0
    for result in per_file_results:
        if result.get("missing_analysis") or result.get("parse_error"):
            continue
        disagreements = result.get("disagreements", [])
        if not disagreements:
            continue
        print()
        print(Path(result["json_path"]).name)
        for annotation, region in disagreements[: args.show_disagreements]:
            print(
                "  "
                f"m{annotation.measure} b{annotation.beat}: {annotation.figure} in {annotation.key} "
                f"ann_pc={annotation.root_pc} vs ours_pc={region.root_pc} ({region.quality})"
            )
        shown += 1
        if shown >= args.show_disagreements:
            break

    if args.summary_json:
        Path(args.summary_json).write_text(json.dumps(summary, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())