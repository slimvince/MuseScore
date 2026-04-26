#!/usr/bin/env python3
# Python interpreter: /c/s/MS/.venv/Scripts/python.exe  (mainline venv)
"""Convert a music21-derived JSON to a ground_truth_response.json.

CLI: convert_music21_ground_truth.py <music21_json_path> <output_dir>

Reads the music21 JSON produced by the Bach-chorale corpus pipeline and emits
<source>.ground_truth_response.json matching the unified schema used by the
LLM and analyzer responses (metadata + tool_input top-level keys).

Beat-range convention: "1-2" means "beats 1 through 2 inclusive within the
measure," so a 2-beat region starting on beat 1 is "1-2", and a 1-beat region
is just "1". The v1.3 comparator must be aware of this convention.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Pitch-class to note-name (flat spelling by default).
# Enharmonic mismatches against TPC-aware analyzer spellings (e.g., D# vs Eb)
# are expected; the comparator handles them as interpretation questions.
# ---------------------------------------------------------------------------
PC_TO_LETTER_FLATS: dict[int, str] = {
    0: "C",  1: "Db", 2: "D",  3: "Eb", 4: "E",  5: "F",
    6: "Gb", 7: "G",  8: "Ab", 9: "A", 10: "Bb", 11: "B",
}

KEY_MODE_MAP: dict[str, tuple[str, str]] = {
    "major":      ("Ionian",      "{root} major"),
    "minor":      ("Aeolian",     "{root} minor"),
    "ionian":     ("Ionian",      "{root} major"),
    "dorian":     ("Dorian",      "{root} dorian"),
    "phrygian":   ("Phrygian",    "{root} phrygian"),
    "lydian":     ("Lydian",      "{root} lydian"),
    "mixolydian": ("Mixolydian",  "{root} mixolydian"),
    "aeolian":    ("Aeolian",     "{root} minor"),
    "locrian":    ("Locrian",     "{root} locrian"),
}


def derive_chord_label(region: dict) -> str:
    """Translate a music21 region dict to a conventional chord symbol.

    Strategy: rootPitchClass for the root letter, quality for triad type,
    chordSymbol prose for seventh extensions.

    quality=="Unknown" always returns "" (no reliable label).
    Unrecognized chordSymbol strings fall through to triad-fallback using
    the quality field — still more informative than an empty string.
    """
    pc = region.get("rootPitchClass")
    quality = region.get("quality", "")
    cs_prose = (region.get("chordSymbol") or "").lower()

    if pc is None or quality == "Unknown":
        return ""

    root = PC_TO_LETTER_FLATS[pc]

    # Seventh extensions — check before triad fallback
    if "dominant seventh" in cs_prose:
        return root + "7"
    if "half diminished" in cs_prose:
        return root + "m7b5"
    if "diminished seventh" in cs_prose and "incomplete" not in cs_prose:
        return root + "dim7"
    if "minor seventh" in cs_prose:
        return root + "m7"
    if "major seventh" in cs_prose:
        return root + "maj7"

    # Triad fallback
    if quality == "Major":
        return root
    if quality == "Minor":
        return root + "m"
    if quality == "Diminished":
        return root + "dim"

    return ""


def parse_music21_key(key_str: str) -> tuple[str, str]:
    """Parse a music21 key string into (normalized_key, mode_name).

    E.g. 'g minor' -> ('G minor', 'Aeolian')
         'c# major' -> ('C# major', 'Ionian')
    """
    parts = (key_str or "").strip().split()
    if len(parts) != 2:
        return key_str, "other"
    raw_root, raw_mode = parts
    letter = raw_root[0].upper()
    accidental = raw_root[1:] if len(raw_root) > 1 else ""
    root = letter + accidental
    mode_info = KEY_MODE_MAP.get(raw_mode.lower())
    if mode_info is None:
        return f"{root} {raw_mode}", "other"
    mode_name, key_template = mode_info
    return key_template.format(root=root), mode_name


def beat_range_str(beat: float, duration: float) -> str:
    """Derive beat-range string from beat onset and duration.

    Convention: "1-2" means beats 1 through 2 inclusive.
    A 2-beat region starting on beat 1 spans beats 1-2 -> "1-2".
    A 1-beat region starting on beat 3 is just "3".
    """
    start_f = float(beat)
    start = int(start_f) if start_f.is_integer() else round(start_f, 3)
    end_raw = float(beat) + float(duration) - 1.0
    end = int(end_raw) if float(end_raw).is_integer() else round(end_raw, 3)
    if start == end:
        return f"{start}"
    return f"{start}-{end}"


def find_score_sibling(music21_json_path: Path) -> Path | None:
    """Return the source score file (xml/musicxml/mscz) beside the JSON, or None."""
    stem = music21_json_path.stem
    # Strip the ".music21" part if present (e.g. bwv10.7.music21.json -> bwv10.7)
    if stem.endswith(".music21"):
        stem = stem[: -len(".music21")]
    parent = music21_json_path.parent
    for ext in (".xml", ".musicxml", ".mscz"):
        candidate = parent / (stem + ext)
        if candidate.exists():
            return candidate
    return None


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def convert(music21_json_path: Path, output_dir: Path) -> None:
    raw_bytes = music21_json_path.read_bytes()
    data = json.loads(raw_bytes)

    source = data["source"]
    detected_key = data.get("detectedKey", "")
    key_confidence = data.get("keyConfidence", 0.0)
    regions = data.get("regions", [])

    # Score sibling (e.g. bwv10.7.xml)
    sibling = find_score_sibling(music21_json_path)
    if sibling is not None:
        score_path = str(sibling.resolve())
        score_content_hash = hash_file(sibling)
    else:
        # Sibling not found — use the music21 JSON path itself as fallback.
        # This is not an error for the converter; the comparator can note it.
        score_path = str(music21_json_path.resolve())
        score_content_hash = ""

    music21_hash_prefix = hashlib.sha256(raw_bytes).hexdigest()[:16]
    model_response_id = f"deterministic-{music21_hash_prefix}"

    timestamp_utc = datetime.now(timezone.utc).isoformat()

    judgments = []
    for region in regions:
        measure = region["measureNumber"]
        beat = region["beat"]
        duration = region.get("duration", 1.0)
        tick_start = region.get("startTick", 0)
        tick_end = region.get("endTick", 0)

        chord_label = derive_chord_label(region)
        chord_label_raw = region.get("chordSymbol") or ""
        roman_numeral = region.get("romanNumeral") or ""
        diatonic_raw = region.get("diatonicToKey")
        diatonic_to_key = bool(diatonic_raw) if diatonic_raw is not None else None

        region_key_str = region.get("key") or detected_key
        normalized_key, mode_name = parse_music21_key(region_key_str)

        judgments.append({
            "measure": measure,
            "beat_range": beat_range_str(beat, duration),
            "tick_start": tick_start,
            "tick_end": tick_end,
            "chord_label": chord_label,
            "chord_label_raw": chord_label_raw,
            "chord_label_alternatives": [],
            "key": normalized_key,
            "mode": mode_name,
            "confidence": "very_high",
            "confidence_raw": 1.0,
            "reasoning": "Music21 ground-truth label.",
            "roman_numeral": roman_numeral,
            "diatonic_to_key": diatonic_to_key,
        })

    output = {
        "metadata": {
            "score_basename": source,
            "score_path": score_path,
            "score_content_hash": score_content_hash,
            "requested_model": "music21-bach-chorales-v1",
            "provider": "music21_ground_truth",
            "model": "music21-bach-chorales-v1",
            "model_response_id": model_response_id,
            "prompt_version": "v1.3-prep",
            "system_prompt_hash": "",
            "tool_definition_hash": "",
            "timestamp_utc": timestamp_utc,
            "input_tokens": 0,
            "output_tokens": 0,
            "stop_reason": "completed",
            "is_authoritative": True,
            "ground_truth_source": "music21",
            "music21_detected_key": detected_key,
            "music21_key_confidence": key_confidence,
        },
        "tool_input": {
            "judgments": judgments,
            "key_summary": detected_key,
            "ambiguity_flags": [],
            "format_friction": "",
        },
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{source}.ground_truth_response.json"
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(
        f"provider=music21_ground_truth  judgments={len(judgments)}"
        f"  output={out_path}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert music21 JSON to ground_truth_response.json"
    )
    parser.add_argument("music21_json_path", type=Path, help="Input music21 JSON file")
    parser.add_argument("output_dir", type=Path, help="Directory to write output JSON")
    args = parser.parse_args()

    if not args.music21_json_path.exists():
        print(f"Error: input file not found: {args.music21_json_path}", file=sys.stderr)
        sys.exit(1)

    convert(args.music21_json_path, args.output_dir)


if __name__ == "__main__":
    main()
