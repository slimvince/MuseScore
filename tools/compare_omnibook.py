"""Phase 1a validation: Charlie Parker Omnibook.

Compares our analyzed root (rootPitchClass) against the written chord symbol
root (writtenRootPc) for each region. Only regions where fromChordSymbol=true
are compared.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter


BREAKDOWN_QUALITY_ORDER = [
    "Major",
    "Minor",
    "Dominant7",
    "Major7",
    "Minor7",
    "HalfDiminished",
    "Diminished",
    "Augmented",
    "Suspended4",
    "Suspended2",
    "Other",
]


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def infer_source_dir(ours_dir: str, explicit_source_dir: str | None) -> str | None:
    if explicit_source_dir:
        return explicit_source_dir

    normalized = ours_dir.replace("\\", "/").lower()
    if "omnibook" in normalized:
        return os.path.join("tools", "corpus_omnibook_src", "omnibook_xml", "Omnibook xml")
    if "effendi" in normalized:
        return os.path.join("tools", "corpus_effendi_src")
    if "rampageswing_sample" in normalized:
        return os.path.join("tools", "corpus_rampageswing_sample")
    if "rampageswing" in normalized:
        return os.path.join("tools", "corpus_rampageswing_full")
    return None


def normalize_written_quality(kind_value: str | None, kind_text_attr: str | None) -> str:
    tokens = " ".join(filter(None, [kind_value, kind_text_attr])).strip().lower()

    if not tokens:
        return "Other"
    if "half-diminished" in tokens or "m7b5" in tokens or "ø" in tokens:
        return "HalfDiminished"
    if (
        "major-seventh" in tokens
        or "major-ninth" in tokens
        or "major-11th" in tokens
        or "major-13th" in tokens
        or "maj7" in tokens
        or "maj9" in tokens
        or "maj11" in tokens
        or "maj13" in tokens
        or "Δ7" in tokens
    ):
        return "Major7"
    if (
        "minor-seventh" in tokens
        or "minor-ninth" in tokens
        or "minor-11th" in tokens
        or "minor-13th" in tokens
        or "min7" in tokens
        or "min9" in tokens
        or "min11" in tokens
        or "min13" in tokens
        or "m11" in tokens
        or "m13" in tokens
        or "m9" in tokens
        or "m7" in tokens
    ):
        return "Minor7"
    if (
        "dominant" in tokens
        or "dominant-seventh" in tokens
        or "dominant-ninth" in tokens
        or "dominant-11th" in tokens
        or "dominant-13th" in tokens
        or tokens == "7"
        or tokens == "9"
        or tokens == "11"
        or tokens == "13"
        or "7alt" in tokens
    ):
        return "Dominant7"
    if "diminished" in tokens or "dim" in tokens or "o7" in tokens:
        return "Diminished"
    if "suspended-fourth" in tokens or "sus4" in tokens or tokens == "sus":
        return "Suspended4"
    if "suspended-second" in tokens or "sus2" in tokens:
        return "Suspended2"
    if "augmented" in tokens or "+" in tokens:
        return "Augmented"
    if "minor" in tokens:
        return "Minor"
    if "major" in tokens:
        return "Major"
    return "Other"


def load_musicxml_root(source_path: str) -> ET.Element:
    if source_path.lower().endswith(".mxl"):
        with zipfile.ZipFile(source_path) as archive:
            score_member = None
            if "META-INF/container.xml" in archive.namelist():
                container_root = ET.fromstring(archive.read("META-INF/container.xml"))
                for elem in container_root.iter():
                    if local_name(elem.tag) == "rootfile":
                        full_path = elem.attrib.get("full-path")
                        if full_path:
                            score_member = full_path
                            break
            if score_member is None:
                for name in archive.namelist():
                    if name.lower().endswith(".xml") and not name.startswith("META-INF/"):
                        score_member = name
                        break
            if score_member is None:
                raise ValueError(f"No score XML found in {source_path}")
            return ET.fromstring(archive.read(score_member))

    return ET.parse(source_path).getroot()


def normalize_json_written_quality(label: str | None) -> str | None:
    if not label:
        return None
    normalized = normalize_written_quality(label, None)
    return None if normalized == "Other" else normalized


def round_position_beat(value: float) -> float:
    return round(value, 6)


def extract_written_qualities_by_position(source_path: str) -> dict[tuple[int, float], str]:
    root = load_musicxml_root(source_path)

    position_qualities: dict[tuple[int, float], Counter[str]] = {}

    for part in root:
        if local_name(part.tag) != "part":
            continue

        measure_number = 0
        divisions = 1
        for measure in part:
            if local_name(measure.tag) != "measure":
                continue

            measure_number += 1
            offset = 0
            for child in measure:
                child_name = local_name(child.tag)

                if child_name == "attributes":
                    for grandchild in child:
                        if local_name(grandchild.tag) == "divisions" and (grandchild.text or "").strip():
                            divisions = max(int((grandchild.text or "1").strip()), 1)
                            break
                    continue

                if child_name == "harmony":
                    kind_value = None
                    kind_text_attr = None
                    for grandchild in child:
                        if local_name(grandchild.tag) == "kind":
                            kind_value = (grandchild.text or "").strip()
                            kind_text_attr = (grandchild.attrib.get("text") or "").strip()
                            break

                    beat = round_position_beat(1.0 + (offset / divisions))
                    key = (measure_number, beat)
                    if key not in position_qualities:
                        position_qualities[key] = Counter()
                    position_qualities[key][normalize_written_quality(kind_value, kind_text_attr)] += 1
                    continue

                if child_name not in {"note", "backup", "forward"}:
                    continue

                duration_value = None
                for grandchild in child:
                    if local_name(grandchild.tag) == "duration" and (grandchild.text or "").strip():
                        duration_value = int((grandchild.text or "0").strip())
                        break

                if duration_value is None:
                    continue
                if child_name == "backup":
                    offset -= duration_value
                else:
                    offset += duration_value

    return {
        key: quality_counter.most_common(1)[0][0]
        for key, quality_counter in position_qualities.items()
    }


def format_breakdown_row(label: str, agree: int, total: int, wrong_counter: Counter[str]) -> str:
    pct = (agree / total * 100.0) if total else 0.0
    wrong_quality = wrong_counter.most_common(1)[0][0] if wrong_counter else "-"
    return f"{label:<16} {agree:>5} {total:>5} {pct:>9.1f}% {wrong_quality}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ours-dir", default="tools/corpus_omnibook", help="Directory containing *.ours.json outputs")
    parser.add_argument("--breakdown", action="store_true", help="Show agreement breakdown by written chord quality")
    parser.add_argument("--source-dir", help="Optional directory containing the source MusicXML files")
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(args.ours_dir, "*.ours.json")))
    source_dir = infer_source_dir(args.ours_dir, args.source_dir)
    total_files = len(files)
    total_regions = 0
    compared_regions = 0
    agreeing_regions = 0
    all_note_count_distribution: Counter[int] = Counter()
    compared_note_count_distribution: Counter[int] = Counter()
    no_analyzed_chord_regions = 0
    zero_region_files: list[str] = []
    per_file: list[tuple[str, int, int, float]] = []
    breakdown = {
        quality: {
            "agree": 0,
            "total": 0,
            "wrong": Counter(),
        }
        for quality in BREAKDOWN_QUALITY_ORDER
    }
    breakdown_warnings: list[str] = []

    for path in files:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)

        regions = data.get("regions", [])
        chord_symbol_regions = [region for region in regions if region.get("fromChordSymbol")]

        written_qualities_by_position: dict[tuple[int, float], str] = {}
        if args.breakdown:
            if not source_dir:
                breakdown_warnings.append(
                    f"{os.path.basename(path)}: source-dir inference unavailable; skipping breakdown for this file"
                )
            else:
                source_path = os.path.join(source_dir, data.get("source", ""))
                if not os.path.exists(source_path):
                    breakdown_warnings.append(
                        f"{os.path.basename(path)}: missing source MusicXML at {source_path}"
                    )
                else:
                    written_qualities_by_position = extract_written_qualities_by_position(source_path)

        total_regions += len(regions)
        if not regions:
            zero_region_files.append(os.path.basename(path))

        file_total = 0
        file_agree = 0
        for region in regions:
            if not region.get("fromChordSymbol"):
                continue

            all_note_count_distribution[region.get("noteCount", -1)] += 1
            written_quality = normalize_json_written_quality(region.get("writtenQuality")) if args.breakdown else None
            if args.breakdown and written_qualities_by_position:
                region_key = (
                    int(region.get("measureNumber", -1)),
                    round_position_beat(float(region.get("beat", 0.0))),
                )
                source_quality = written_qualities_by_position.get(region_key)
                if source_quality is not None:
                    written_quality = source_quality
                elif written_quality is None:
                    breakdown_warnings.append(
                        f"{os.path.basename(path)}: no deduplicated harmony at measure {region_key[0]} beat {region_key[1]}"
                    )

            if not region.get("hasAnalyzedChord", True):
                no_analyzed_chord_regions += 1
                continue

            written = region.get("writtenRootPc", -1)
            analyzed = region.get("rootPitchClass", -1)
            if written < 0 or analyzed < 0:
                no_analyzed_chord_regions += 1
                continue

            file_total += 1
            compared_regions += 1
            compared_note_count_distribution[region.get("noteCount", -1)] += 1

            if written == analyzed:
                file_agree += 1
                agreeing_regions += 1

            if written_quality in breakdown:
                breakdown[written_quality]["total"] += 1
                if written == analyzed:
                    breakdown[written_quality]["agree"] += 1
                else:
                    breakdown[written_quality]["wrong"][region.get("quality", "Unknown")] += 1

        if file_total > 0:
            per_file.append(
                (
                    os.path.basename(path),
                    file_agree,
                    file_total,
                    file_agree / file_total,
                )
            )

    agreement = (agreeing_regions / compared_regions) if compared_regions else 0.0

    print(f"Files processed: {total_files}")
    print(f"Total regions: {total_regions}")
    print(
        f"Comparable chord-symbol regions: {compared_regions}"
    )
    print(
        f"Root agreement: {agreeing_regions}/{compared_regions} = {agreement:.1%}"
    )
    print()

    print("All fromChordSymbol noteCount distribution:")
    for note_count, count in sorted(all_note_count_distribution.items()):
        print(f"  {note_count}: {count}")
    print()

    print(f"No analyzed chord regions: {no_analyzed_chord_regions}")
    print()

    print("Comparable noteCount distribution:")
    for note_count, count in sorted(compared_note_count_distribution.items()):
        print(f"  {note_count}: {count}")
    print()

    print("5 lowest-agreement solos:")
    for name, agree, total, pct in sorted(per_file, key=lambda row: (row[3], row[0]))[:5]:
        print(f"  {name}: {agree}/{total} = {pct:.0%}")
    print()

    print("5 highest-agreement solos:")
    for name, agree, total, pct in sorted(per_file, key=lambda row: (row[3], row[0]), reverse=True)[:5]:
        print(f"  {name}: {agree}/{total} = {pct:.0%}")
    print()

    if args.breakdown:
        print("Breakdown by written chord quality:")
        print(f"{'Written quality':<16} {'Agree':>5} {'Total':>5} {'Agree %':>10} Most common wrong answer quality")
        for quality in BREAKDOWN_QUALITY_ORDER:
            row = breakdown[quality]
            print(format_breakdown_row(quality, row["agree"], row["total"], row["wrong"]))
        print()

        if breakdown_warnings:
            print("Breakdown warnings:")
            for warning in breakdown_warnings[:10]:
                print(f"  {warning}")
            if len(breakdown_warnings) > 10:
                print(f"  ... {len(breakdown_warnings) - 10} more")
            print()

    print(f"Zero-region solos: {len(zero_region_files)}")
    for name in zero_region_files:
        print(f"  {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())