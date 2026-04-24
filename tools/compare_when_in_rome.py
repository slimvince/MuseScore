"""When in Rome validation: compare analyzed roots against RomanText annotations.

For each `*.ours.json` output with an adjacent `analysis.txt`, parse the RomanText
analysis with music21, resolve each Roman numeral to an absolute root pitch class,
and compare it against the nearest analyzed region by measure + beat.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


MUSIC21_FALLBACK_SITE_PACKAGES = (
    r"C:\Users\vince\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages"
)


def import_music21_converter():
    try:
        from music21 import converter  # type: ignore
    except (ModuleNotFoundError, ImportError):
        for name in list(sys.modules):
            if name == "music21" or name.startswith("music21."):
                sys.modules.pop(name, None)
        if MUSIC21_FALLBACK_SITE_PACKAGES not in sys.path:
            sys.path.insert(0, MUSIC21_FALLBACK_SITE_PACKAGES)
        from music21 import converter  # type: ignore
    return converter


@dataclass(frozen=True)
class Annotation:
    measure: int
    beat: float
    tick: int
    root_pc: int
    figure: str
    key: str


@dataclass(frozen=True)
class Region:
    measure: int
    beat: float
    start_tick: int
    end_tick: int
    root_pc: int
    quality: str


def round_beat(value: float) -> float:
    return round(float(value), 6)


def encode_score_relative_path(score_path: Path, wir_dir: Path) -> str:
    relative = score_path.relative_to(wir_dir).as_posix()
    if relative.lower().endswith(".mxl"):
        relative = relative[:-4]
    return relative.replace("/", "__")


def build_analysis_index(wir_dir: str | Path) -> dict[str, Path]:
    wir_root = Path(wir_dir)
    index: dict[str, Path] = {}
    for analysis_path in wir_root.glob("**/analysis.txt"):
        score_path = analysis_path.with_name("score.mxl")
        if not score_path.exists():
            continue
        encoded = encode_score_relative_path(score_path, wir_root)
        index[f"{encoded}.ours.json"] = analysis_path
    return index


def resolve_analysis_path(json_path: str | Path, analysis_index: dict[str, Path]) -> Path | None:
    return analysis_index.get(Path(json_path).name)


def parse_analysis(analysis_path: str | Path) -> list[Annotation]:
    converter = import_music21_converter()
    score = converter.parse(str(analysis_path), format="romanText")

    annotations: list[Annotation] = []
    for rn in score.flatten().getElementsByClass("RomanNumeral"):
        try:
            root = rn.root()
        except Exception:
            continue
        if root is None:
            continue
        annotations.append(
            Annotation(
                measure=int(rn.measureNumber),
                beat=round_beat(rn.beat),
                tick=int(round(float(rn.getOffsetInHierarchy(score)) * 480.0)),
                root_pc=int(root.pitchClass),
                figure=str(rn.figure),
                key=str(rn.key),
            )
        )
    return annotations


def load_our_regions(json_path: str | Path) -> list[Region]:
    with open(json_path, encoding="utf-8") as handle:
        data = json.load(handle)

    regions: list[Region] = []
    for region in data.get("regions", []):
        root_pc = int(region.get("rootPitchClass", -1))
        if root_pc < 0:
            continue
        regions.append(
            Region(
                measure=int(region.get("measureNumber", -1)),
                beat=round_beat(region.get("beat", 0.0)),
                start_tick=int(region.get("startTick", -1)),
                end_tick=int(region.get("endTick", -1)),
                root_pc=root_pc,
                quality=str(region.get("quality", "Unknown")),
            )
        )
    return regions


def find_matching_region(
    regions: list[Region],
    annotation_tick: int,
    beat_tolerance: float,
    ticks_per_beat: int,
) -> Region | None:
    for region in regions:
        if region.start_tick <= annotation_tick < region.end_tick:
            return region

    tick_tolerance = int(round(beat_tolerance * ticks_per_beat))
    best_region: Region | None = None
    best_distance: int | None = None

    for region in regions:
        distance = abs(region.start_tick - annotation_tick)
        if distance > tick_tolerance:
            continue
        if best_distance is None or distance < best_distance:
            best_region = region
            best_distance = distance

    return best_region


def compare_file(
    json_path: str | Path,
    analysis_index: dict[str, Path],
    beat_tolerance: float,
    ticks_per_beat: int,
) -> dict:
    analysis_path = resolve_analysis_path(json_path, analysis_index)
    if analysis_path is None:
        return {
            "json_path": str(json_path),
            "analysis_path": None,
            "annotations": 0,
            "compared": 0,
            "agree": 0,
            "no_match": 0,
            "missing_analysis": True,
            "parse_error": False,
        }

    regions = load_our_regions(json_path)
    try:
        annotations = parse_analysis(analysis_path)
    except Exception as exc:
        return {
            "json_path": str(json_path),
            "analysis_path": str(analysis_path),
            "annotations": 0,
            "compared": 0,
            "agree": 0,
            "no_match": 0,
            "missing_analysis": False,
            "parse_error": True,
            "error": str(exc),
        }

    compared = 0
    agree = 0
    no_match = 0
    disagreements: list[tuple[Annotation, Region]] = []

    for annotation in annotations:
        region = find_matching_region(regions, annotation.tick, beat_tolerance, ticks_per_beat)
        if region is None:
            no_match += 1
            continue

        compared += 1
        if region.root_pc == annotation.root_pc:
            agree += 1
        else:
            disagreements.append((annotation, region))

    return {
        "json_path": str(json_path),
        "analysis_path": str(analysis_path),
        "annotations": len(annotations),
        "compared": compared,
        "agree": agree,
        "no_match": no_match,
        "missing_analysis": False,
        "parse_error": False,
        "disagreements": disagreements,
    }


def genre_from_json_path(json_path: str | Path) -> str:
    return Path(json_path).name.split("__", 1)[0]


def collect_json_files(ours_dir: str | Path, json_files: list[str] | None) -> list[str]:
    if json_files:
        return [str(Path(path)) for path in json_files]
    return sorted(glob.glob(os.path.join(str(ours_dir), "*.ours.json")))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ours-dir", default="tools/corpus_when_in_rome")
    parser.add_argument("--wir-dir", default="tools/dcml/when_in_rome/Corpus")
    parser.add_argument("--beat-tolerance", type=float, default=0.5)
    parser.add_argument("--ticks-per-beat", type=int, default=480)
    parser.add_argument("--json-file", action="append", help="Compare only the given output JSON file")
    parser.add_argument("--show-disagreements", type=int, default=5)
    args = parser.parse_args()

    files = collect_json_files(args.ours_dir, args.json_file)
    analysis_index = build_analysis_index(args.wir_dir)
    files_compared = 0
    total_annotations = 0
    total = 0
    agree = 0
    no_match = 0
    missing_analysis = 0
    parse_failures = 0
    genre_stats: dict[str, Counter[str]] = {}
    per_file_results: list[dict] = []

    for json_path in files:
        result = compare_file(json_path, analysis_index, args.beat_tolerance, args.ticks_per_beat)
        per_file_results.append(result)

        if result["missing_analysis"]:
            missing_analysis += 1
            continue

        if result.get("parse_error"):
            parse_failures += 1
            continue

        files_compared += 1
        genre = genre_from_json_path(json_path)
        stats = genre_stats.setdefault(genre, Counter())
        stats["files"] += 1
        stats["annotations"] += result["annotations"]
        stats["compared"] += result["compared"]
        stats["agree"] += result["agree"]
        stats["no_match"] += result["no_match"]

        total_annotations += result["annotations"]
        total += result["compared"]
        agree += result["agree"]
        no_match += result["no_match"]

    agreement = (agree / total) if total else 0.0
    unmatched_rate = (no_match / total_annotations) if total_annotations else 0.0
    print(f"Files considered: {len(files)}")
    print(f"Files compared: {files_compared}")
    print(f"Files with missing analysis.txt: {missing_analysis}")
    print(f"Files with parse failures: {parse_failures}")
    print(f"Total annotations: {total_annotations}")
    print(f"Annotations matched to regions: {total}")
    print(f"Agree: {agree}  Agreement: {agreement:.1%}")
    print(f"No match: {no_match}  Unmatched rate: {unmatched_rate:.1%}")
    print()

    if genre_stats:
        print("By genre:")
        for genre in sorted(genre_stats):
            stats = genre_stats[genre]
            genre_agreement = (stats["agree"] / stats["compared"]) if stats["compared"] else 0.0
            genre_unmatched = (stats["no_match"] / stats["annotations"]) if stats["annotations"] else 0.0
            print(
                f"  {genre:30} {stats['files']:4} files  "
                f"agree {stats['agree']:5}/{stats['compared']:<5} = {genre_agreement:.1%}  "
                f"unmatched {stats['no_match']:5}/{stats['annotations']:<5} = {genre_unmatched:.1%}"
            )
        print()

    shown = 0
    for result in per_file_results:
        if result.get("missing_analysis"):
            continue
        if result.get("parse_error"):
            continue
        disagreements = result.get("disagreements", [])
        if not disagreements:
            continue
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

    if parse_failures:
        print()
        print("Parse failures:")
        for result in per_file_results:
            if not result.get("parse_error"):
                continue
            print(f"  {Path(result['json_path']).name}: {result.get('error', 'unknown parse error')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())