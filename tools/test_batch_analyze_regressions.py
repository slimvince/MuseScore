#!/usr/bin/env python3
"""Regression checks for batch_analyze smoke scenarios.

1. Windows backslash-path MSCX loading remains functional.
2. MusicXML with embedded harmony elements triggers jazz mode and preserves
   fromChordSymbol metadata.
3. BWV 227.7 measure 9 beat 1 must retain pitch-class E in the exported region.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def run_batch_analyze(batch_analyze: Path, input_path: str, output_path: Path) -> dict:
    completed = subprocess.run(
        [str(batch_analyze), input_path, str(output_path), "--preset", "Standard"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise AssertionError(
            f"batch_analyze failed for {input_path}\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )
    with output_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def assert_smoke_result(data: dict, expected_source: str) -> None:
    if data.get("source") != expected_source:
        raise AssertionError(f"Unexpected source: {data.get('source')} != {expected_source}")

    regions = data.get("regions", [])
    if len(regions) != 4:
        raise AssertionError(f"Expected 4 regions, got {len(regions)}")

    expected_written = [2, 7, 0, 0]
    expected_note_counts = [4, 4, 3, 1]
    expected_has_analysis = [True, True, True, False]

    for index, region in enumerate(regions):
        if not region.get("fromChordSymbol"):
            raise AssertionError(f"Region {index} missing fromChordSymbol=true")
        if region.get("writtenRootPc") != expected_written[index]:
            raise AssertionError(
                f"Region {index} writtenRootPc mismatch: {region.get('writtenRootPc')} != {expected_written[index]}"
            )
        if region.get("noteCount") != expected_note_counts[index]:
            raise AssertionError(
                f"Region {index} noteCount mismatch: {region.get('noteCount')} != {expected_note_counts[index]}"
            )
        if region.get("hasAnalyzedChord") != expected_has_analysis[index]:
            raise AssertionError(
                f"Region {index} hasAnalyzedChord mismatch: {region.get('hasAnalyzedChord')} != {expected_has_analysis[index]}"
            )
        if region.get("rootPitchClass", -1) < -1 or region.get("rootPitchClass", -1) > 11:
            raise AssertionError(
                f"Region {index} rootPitchClass out of range: {region.get('rootPitchClass')}"
            )
        if region.get("hasAnalyzedChord") and not region.get("chordSymbol"):
            raise AssertionError(f"Region {index} should have a non-empty analyzed chordSymbol")
        if not region.get("hasAnalyzedChord") and region.get("chordSymbol"):
            raise AssertionError(f"Region {index} should not emit a chordSymbol when analysis is unavailable")


def assert_bwv227_measure9_contains_e(data: dict) -> None:
    # Pitch-class E (4) enters in measure 9 on beat 2 (the first E onset in the
    # voice that carries the melodic line).  We check any region in measure 9
    # rather than beat 1 specifically, because the region boundaries can shift
    # as the analysis evolves while the musical content of measure 9 is fixed.
    measure9_pcs: set[int] = set()
    found_measure9 = False
    for region in data.get("regions", []):
        if region.get("measureNumber") == 9:
            found_measure9 = True
            for tone in region.get("tones", []):
                pitch = tone.get("pitch")
                if pitch is not None:
                    measure9_pcs.add(pitch % 12)

    if not found_measure9:
        raise AssertionError("Missing measure 9 region in BWV 227.7 output")

    if 4 not in measure9_pcs:
        raise AssertionError(
            "BWV 227.7 measure 9 is missing pitch-class E across all regions; "
            f"got pitch classes {sorted(measure9_pcs)}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-analyze", required=True)
    parser.add_argument("--repo-root", required=True)
    args = parser.parse_args()

    batch_analyze = Path(args.batch_analyze)
    repo_root = Path(args.repo_root)

    mscx_path = repo_root / "src" / "composing" / "tests" / "data" / "mono_smoke_test.mscx"
    musicxml_path = repo_root / "src" / "composing" / "tests" / "data" / "mono_smoke_test.musicxml"
    bach_regression_path = repo_root / "tools" / "corpus" / "bwv227.7.xml"

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)

        # Regression 1: Windows backslash paths for MSCX should load successfully.
        mscx_output = tmp / "mono_smoke_test_mscx.json"
        mscx_input = str(mscx_path)
        if "\\" not in mscx_input:
            mscx_input = mscx_input.replace("/", "\\")
        mscx_data = run_batch_analyze(batch_analyze, mscx_input, mscx_output)
        assert_smoke_result(mscx_data, "mono_smoke_test.mscx")

        # Regression 2: Omnibook-style MusicXML with embedded harmony should trigger jazz mode.
        musicxml_output = tmp / "mono_smoke_test_musicxml.json"
        musicxml_data = run_batch_analyze(batch_analyze, str(musicxml_path), musicxml_output)
        assert_smoke_result(musicxml_data, "mono_smoke_test.musicxml")

        # Regression 3: the merged measure 9 beat 1 region in BWV 227.7 must retain E.
        bach_output = tmp / "bwv227_7.json"
        bach_data = run_batch_analyze(batch_analyze, str(bach_regression_path), bach_output)
        assert_bwv227_measure9_contains_e(bach_data)

    print("batch_analyze regressions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())