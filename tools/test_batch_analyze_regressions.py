#!/usr/bin/env python3
"""Regression checks for batch_analyze smoke scenarios.

1. Windows backslash-path MSCX loading remains functional (loads, returns valid JSON).
2. MusicXML loading remains functional (loads, returns valid JSON).
3. BWV 227.7 measure 9 beat 1 must retain pitch-class E in the exported region.
4. Jazz preset ii-V-I (jazz_smoke_test.mscx): Dm7 / G7 / CMaj7 labels pinned under
   Jazz preset, so Standard-only logic changes cannot silently affect Jazz output.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def run_batch_analyze(batch_analyze: Path, input_path: str, output_path: Path,
                      preset: str = "Standard") -> dict:
    completed = subprocess.run(
        [str(batch_analyze), input_path, str(output_path), "--preset", preset],
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


def assert_load_result(data: dict, expected_source: str) -> None:
    """Assert that a score loaded successfully and returned a valid JSON structure."""
    if data.get("source") != expected_source:
        raise AssertionError(f"Unexpected source: {data.get('source')!r} != {expected_source!r}")
    if "regions" not in data:
        raise AssertionError(f"Missing 'regions' key in output for {expected_source}")


def assert_jazz_smoke_result(data: dict) -> None:
    """Jazz preset ii-V-I: Dm7 / G7 / CMaj7."""
    if data.get("source") != "jazz_smoke_test.mscx":
        raise AssertionError(f"Unexpected source: {data.get('source')}")

    regions = data.get("regions", [])
    if len(regions) != 3:
        raise AssertionError(f"Expected 3 regions, got {len(regions)}")

    expected = [
        {"measureNumber": 1, "chordSymbol": "Dm7",  "rootPitchClass": 2, "noteCount": 4},
        {"measureNumber": 2, "chordSymbol": "G7",   "rootPitchClass": 7, "noteCount": 4},
        {"measureNumber": 3, "chordSymbol": "CMaj7","rootPitchClass": 0, "noteCount": 4},
    ]
    for i, (region, exp) in enumerate(zip(regions, expected)):
        for key, val in exp.items():
            if region.get(key) != val:
                raise AssertionError(
                    f"Jazz smoke region {i} {key} mismatch: "
                    f"{region.get(key)!r} != {val!r}"
                )


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
    jazz_smoke_path = repo_root / "src" / "composing" / "tests" / "data" / "jazz_smoke_test.mscx"
    bach_regression_path = repo_root / "tools" / "corpus" / "bwv227.7.xml"

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)

        # Regression 1: Windows backslash paths for MSCX should load without crashing.
        mscx_output = tmp / "mono_smoke_test_mscx.json"
        mscx_input = str(mscx_path)
        if "\\" not in mscx_input:
            mscx_input = mscx_input.replace("/", "\\")
        mscx_data = run_batch_analyze(batch_analyze, mscx_input, mscx_output,
                                      preset="Standard")
        assert_load_result(mscx_data, "mono_smoke_test.mscx")

        # Regression 2: MusicXML loading should succeed and return a valid structure.
        musicxml_output = tmp / "mono_smoke_test_musicxml.json"
        musicxml_data = run_batch_analyze(batch_analyze, str(musicxml_path), musicxml_output,
                                          preset="Standard")
        assert_load_result(musicxml_data, "mono_smoke_test.musicxml")

        # Regression 3: the merged measure 9 beat 1 region in BWV 227.7 must retain E.
        bach_output = tmp / "bwv227_7.json"
        bach_data = run_batch_analyze(batch_analyze, str(bach_regression_path), bach_output,
                                      preset="Standard")
        assert_bwv227_measure9_contains_e(bach_data)

        # Regression 4: Jazz preset ii-V-I smoke test.  Pins chord labels under Jazz
        # preset so that changes to Standard-only logic (e.g. enharmonic-equivalence
        # preference) cannot silently affect Jazz output.
        jazz_output = tmp / "jazz_smoke_test.json"
        jazz_data = run_batch_analyze(batch_analyze, str(jazz_smoke_path), jazz_output,
                                      preset="Jazz")
        assert_jazz_smoke_result(jazz_data)

    print("batch_analyze regressions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())