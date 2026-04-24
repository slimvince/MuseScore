#!/usr/bin/env python3
"""
check_parity.py — Compare batch_analyze batch output against notation-bridge output.

The script runs batch_analyze three times for one score:
  - --dump-regions batch
  - --dump-regions notation
  - --dump-regions notation-premerge

It then matches each batch region to the closest notation region by start tick,
using end tick, measure number, and beat as tie-breakers, and reports whether
the two paths agree on region boundaries and harmonic identity.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class MeasureRange:
    start: int
    end: int
    label: str

    def contains(self, measure_number: int) -> bool:
        return self.start <= measure_number <= self.end


@dataclass
class MatchResult:
    batch_region: dict
    notation_region: dict | None
    tick_diff: int
    tick_match: bool
    exact_start_match: bool
    exact_span_match: bool
    root_match: bool
    quality_match: bool
    tone_set_match: bool


def _find_batch_analyze(hint: str | None) -> Path | None:
    candidates: list[Path] = []
    if hint:
        candidates.append(Path(hint))

    candidates.extend([
        REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        REPO_ROOT / "ninja_build" / "batch_analyze",
    ])

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return None


def _parse_measure_range(spec: str) -> MeasureRange:
    text = spec.strip()
    if not text:
        raise argparse.ArgumentTypeError("measure range cannot be empty")

    if "-" in text:
        left, right = text.split("-", 1)
        start = int(left)
        end = int(right)
    else:
        start = int(text)
        end = start

    if start <= 0 or end <= 0 or end < start:
        raise argparse.ArgumentTypeError(f"invalid measure range '{spec}'")

    return MeasureRange(start=start, end=end, label=text)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _run_batch_analyze(
    executable: Path,
    score_path: Path,
    output_path: Path,
    preset_name: str,
    dump_mode: str,
) -> dict:
    command = [
        str(executable),
        str(score_path),
        str(output_path),
        "--preset",
        preset_name,
        "--dump-regions",
        dump_mode,
    ]
    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=180,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(
            f"batch_analyze failed for mode '{dump_mode}' with exit code {result.returncode}: {stderr}"
        )

    if not output_path.exists():
        raise RuntimeError(f"batch_analyze did not create output file for mode '{dump_mode}'")

    return _load_json(output_path)


def _pitch_class_set(region: dict) -> tuple[int, ...]:
    if region.get("pitchClassSet") is not None:
        bitmask = int(region["pitchClassSet"])
        return tuple(pc for pc in range(12) if bitmask & (1 << pc))

    pitch_classes = {
        int(tone["pitch"]) % 12
        for tone in region.get("tones", [])
        if "pitch" in tone
    }
    return tuple(sorted(pitch_classes))


def _best_notation_index(batch_region: dict, notation_regions: list[dict], unused_indices: set[int]) -> int | None:
    if not unused_indices:
        return None

    batch_start = int(batch_region.get("startTick", 0))
    batch_end = int(batch_region.get("endTick", 0))
    batch_measure = int(batch_region.get("measureNumber", 0))
    batch_beat = float(batch_region.get("beat", 0.0))

    def sort_key(index: int) -> tuple[float, ...]:
        notation_region = notation_regions[index]
        return (
            abs(int(notation_region.get("startTick", 0)) - batch_start),
            abs(int(notation_region.get("endTick", 0)) - batch_end),
            abs(int(notation_region.get("measureNumber", 0)) - batch_measure),
            abs(float(notation_region.get("beat", 0.0)) - batch_beat),
            index,
        )

    return min(unused_indices, key=sort_key)


def compare_regions(
    batch_regions: list[dict],
    notation_regions: list[dict],
    tick_tolerance: int = 240,
) -> tuple[list[MatchResult], list[int]]:
    results: list[MatchResult] = []
    unused_notation_indices = set(range(len(notation_regions)))

    for batch_region in batch_regions:
        notation_index = _best_notation_index(batch_region, notation_regions, unused_notation_indices)
        notation_region = notation_regions[notation_index] if notation_index is not None else None
        if notation_index is not None:
            unused_notation_indices.remove(notation_index)

        if notation_region is None:
            results.append(
                MatchResult(
                    batch_region=batch_region,
                    notation_region=None,
                    tick_diff=sys.maxsize,
                    tick_match=False,
                    exact_start_match=False,
                    exact_span_match=False,
                    root_match=False,
                    quality_match=False,
                    tone_set_match=False,
                )
            )
            continue

        batch_start = int(batch_region.get("startTick", 0))
        notation_start = int(notation_region.get("startTick", 0))
        batch_end = int(batch_region.get("endTick", 0))
        notation_end = int(notation_region.get("endTick", 0))
        tick_diff = abs(notation_start - batch_start)

        results.append(
            MatchResult(
                batch_region=batch_region,
                notation_region=notation_region,
                tick_diff=tick_diff,
                tick_match=tick_diff <= tick_tolerance,
                exact_start_match=batch_start == notation_start,
                exact_span_match=(batch_start == notation_start and batch_end == notation_end),
                root_match=(
                    int(batch_region.get("rootPitchClass", -1))
                    == int(notation_region.get("rootPitchClass", -1))
                ),
                quality_match=(
                    str(batch_region.get("quality", ""))
                    == str(notation_region.get("quality", ""))
                ),
                tone_set_match=(_pitch_class_set(batch_region) == _pitch_class_set(notation_region)),
            )
        )

    return results, sorted(unused_notation_indices)


def _summarize(results: list[MatchResult]) -> dict[str, int]:
    return {
        "tick_tolerance_matches": sum(1 for result in results if result.tick_match),
        "exact_start_matches": sum(1 for result in results if result.exact_start_match),
        "exact_span_matches": sum(1 for result in results if result.exact_span_match),
        "root_matches": sum(1 for result in results if result.root_match),
        "quality_matches": sum(1 for result in results if result.quality_match),
        "root_quality_matches": sum(1 for result in results if result.root_match and result.quality_match),
        "tone_set_matches": sum(1 for result in results if result.tone_set_match),
        "full_matches": sum(
            1
            for result in results
            if result.exact_span_match
            and result.root_match
            and result.quality_match
            and result.tone_set_match
        ),
    }


def _region_in_focus(region: dict | None, focus_ranges: list[MeasureRange]) -> bool:
    if region is None:
        return False
    measure_number = int(region.get("measureNumber", 0))
    return any(focus.contains(measure_number) for focus in focus_ranges)


def _describe_region(region: dict | None) -> str:
    if region is None:
        return "<none>"

    measure_number = int(region.get("measureNumber", 0))
    beat = float(region.get("beat", 0.0))
    start_tick = int(region.get("startTick", 0))
    end_tick = int(region.get("endTick", 0))
    chord_symbol = str(region.get("chordSymbol", "")) or "<no-symbol>"
    quality = str(region.get("quality", "Unknown"))
    root_pitch_class = int(region.get("rootPitchClass", -1))
    tone_set = ",".join(str(pc) for pc in _pitch_class_set(region))
    return (
        f"m{measure_number} b{beat:g} {chord_symbol} ({quality}, root={root_pitch_class}) "
        f"ticks {start_tick}-{end_tick} pcs[{tone_set}]"
    )


def _format_mismatch(result: MatchResult) -> list[str]:
    lines = [
        f"  batch:    {_describe_region(result.batch_region)}",
        f"  notation: {_describe_region(result.notation_region)}",
    ]

    details: list[str] = []
    if not result.tick_match:
        details.append(f"tick diff {result.tick_diff} exceeds tolerance")
    if not result.exact_span_match:
        details.append("span differs")
    if not result.root_match:
        details.append("root differs")
    if not result.quality_match:
        details.append("quality differs")
    if not result.tone_set_match:
        details.append("tone set differs")

    if details:
        lines.append(f"  issues:   {', '.join(details)}")
    return lines


def _focus_section(
    label: str,
    focus_ranges: list[MeasureRange],
    matches: list[MatchResult],
    notation_regions: list[dict],
    unmatched_notation: list[int],
) -> list[str]:
    lines = [f"{label}:"]
    mismatches = [
        result
        for result in matches
        if (
            _region_in_focus(result.batch_region, focus_ranges)
            or _region_in_focus(result.notation_region, focus_ranges)
        )
        and not (
            result.exact_span_match
            and result.root_match
            and result.quality_match
            and result.tone_set_match
        )
    ]
    unmatched = [
        notation_regions[index]
        for index in unmatched_notation
        if _region_in_focus(notation_regions[index], focus_ranges)
    ]

    if not mismatches and not unmatched:
        lines.append("  No mismatches found in this measure range.")
        return lines

    for mismatch in mismatches:
        lines.extend(_format_mismatch(mismatch))

    for notation_region in unmatched:
        lines.append(f"  unmatched notation: {_describe_region(notation_region)}")

    return lines


def build_report(
    score_path: Path,
    batch_dump: dict,
    notation_dump: dict,
    notation_premerge_dump: dict,
    matches: list[MatchResult],
    unmatched_notation: list[int],
    tick_tolerance: int,
    focus_ranges: list[MeasureRange],
) -> str:
    batch_regions = batch_dump.get("regions", [])
    notation_regions = notation_dump.get("regions", [])
    notation_premerge_regions = notation_premerge_dump.get("regions", [])
    summary = _summarize(matches)

    lines = [
        f"Score: {score_path.resolve()}",
        f"Batch analysis path: {batch_dump.get('analysisPath', '<unknown>')}",
        f"Notation analysis path: {notation_dump.get('analysisPath', '<unknown>')}",
        f"Batch regions: {len(batch_regions)}",
        f"Notation regions: {len(notation_regions)}",
        f"Notation pre-merge regions: {len(notation_premerge_regions)}",
        "",
        f"Start-tick matches within tolerance ({tick_tolerance}): {summary['tick_tolerance_matches']}/{len(matches)}",
        f"Exact start-tick matches: {summary['exact_start_matches']}/{len(matches)}",
        f"Exact span matches: {summary['exact_span_matches']}/{len(matches)}",
        f"Root matches: {summary['root_matches']}/{len(matches)}",
        f"Quality matches: {summary['quality_matches']}/{len(matches)}",
        f"Root + quality matches: {summary['root_quality_matches']}/{len(matches)}",
        f"Tone-set matches: {summary['tone_set_matches']}/{len(matches)}",
        f"Full structural matches: {summary['full_matches']}/{len(matches)}",
    ]

    if unmatched_notation:
        lines.append(f"Unmatched notation regions: {len(unmatched_notation)}")

    lines.append("")

    root_or_quality_mismatches = [
        result
        for result in matches
        if not result.root_match or not result.quality_match
    ]
    if root_or_quality_mismatches:
        lines.append("Root/quality mismatches:")
        for mismatch in root_or_quality_mismatches:
            lines.extend(_format_mismatch(mismatch))
    else:
        lines.append("No root/quality mismatches found.")

    if focus_ranges:
        lines.append("")
        for focus in focus_ranges:
            lines.extend(
                _focus_section(
                    f"Focus measures {focus.label}",
                    [focus],
                    matches,
                    notation_regions,
                    unmatched_notation,
                )
            )
            lines.append("")

    lines.extend([
        "Closest-match comparison method: nearest notation region by start tick,",
        "then by end tick, measure number, and beat as tie-breakers.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare batch_analyze batch output against notation-bridge output for one score."
    )
    parser.add_argument("score", help="Path to the score file to analyze")
    parser.add_argument(
        "--batch-analyze",
        dest="batch_analyze",
        help="Path to batch_analyze executable (default: resolve from build tree)",
    )
    parser.add_argument(
        "--preset",
        default="Standard",
        help="Mode-prior preset to pass through to batch_analyze (default: Standard)",
    )
    parser.add_argument(
        "--tick-tolerance",
        type=int,
        default=240,
        help="Maximum start-tick difference considered a tolerant match (default: 240)",
    )
    parser.add_argument(
        "--focus-measures",
        action="append",
        default=[],
        help="Measure range to highlight in the report, e.g. 8-10 or 16",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the text report",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    score_path = Path(args.score)
    if not score_path.exists():
        print(f"ERROR: score not found: {score_path}", file=sys.stderr)
        return 1

    executable = _find_batch_analyze(args.batch_analyze)
    if executable is None:
        print("ERROR: batch_analyze not found. Build it first or pass --batch-analyze.", file=sys.stderr)
        return 1

    try:
        focus_ranges = [_parse_measure_range(spec) for spec in args.focus_measures]
    except argparse.ArgumentTypeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="parity_", dir=str(REPO_ROOT / "tools" / "reports")) as temp_dir:
        temp_root = Path(temp_dir)
        batch_dump = _run_batch_analyze(
            executable,
            score_path,
            temp_root / "batch.json",
            args.preset,
            "batch",
        )
        notation_dump = _run_batch_analyze(
            executable,
            score_path,
            temp_root / "notation.json",
            args.preset,
            "notation",
        )
        notation_premerge_dump = _run_batch_analyze(
            executable,
            score_path,
            temp_root / "notation-premerge.json",
            args.preset,
            "notation-premerge",
        )

        matches, unmatched_notation = compare_regions(
            batch_dump.get("regions", []),
            notation_dump.get("regions", []),
            tick_tolerance=args.tick_tolerance,
        )
        report = build_report(
            score_path=score_path,
            batch_dump=batch_dump,
            notation_dump=notation_dump,
            notation_premerge_dump=notation_premerge_dump,
            matches=matches,
            unmatched_notation=unmatched_notation,
            tick_tolerance=args.tick_tolerance,
            focus_ranges=focus_ranges,
        )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")

    sys.stdout.write(report)

    full_match_count = sum(
        1
        for result in matches
        if result.exact_span_match
        and result.root_match
        and result.quality_match
        and result.tone_set_match
    )
    perfect = full_match_count == len(matches) and not unmatched_notation
    return 0 if perfect else 2


if __name__ == "__main__":
    raise SystemExit(main())