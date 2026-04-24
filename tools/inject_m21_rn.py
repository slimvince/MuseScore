#!/usr/bin/env python3
"""
inject_m21_rn.py — Inject music21 Roman-numeral labels into a MusicXML file.

Each label is inserted as a <direction type="words"> above the first staff,
placed at the correct beat position via <offset>.  Open the resulting XML in
MuseScore, then run 'Implode → Chord Staff' to see our analysis below and the
music21 labels above.

Source XML and .music21.json files live in tools/corpus/ (working copies
exported from the music21 corpus via music21_batch.py).

Annotated output (_m21.xml) is written to tools/corpus_m21_xml/ by default.

Usage:
    python tools/inject_m21_rn.py bwv66.6           # writes corpus_m21_xml/bwv66.6_m21.xml
    python tools/inject_m21_rn.py --all             # process all files that have both json files
    python tools/inject_m21_rn.py --out DIR bwv66.6 # write to DIR/bwv66.6_m21.xml

By default, reads from tools/corpus/ relative to CWD or one directory up.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# We manipulate the XML as text rather than via ElementTree so we can insert
# blocks of text at arbitrary positions without ElementTree mangling namespaces,
# encoding declarations, or attribute ordering.

DIVISIONS_PER_QUARTER_MS  = 480   # MuseScore internal ticks per quarter note
RATIO = None  # set per-file from <divisions> in the XML


def find_corpus_file(name: str, corpus_dir: Path) -> tuple[Path | None, Path | None, Path | None]:
    """Return (xml_path, m21_json, ours_json) for a chorale name like 'bwv66.6'."""
    # Short name match (new convention: bwv66.6.xml)
    xml = corpus_dir / f"{name}.xml"
    m21 = corpus_dir / f"{name}.music21.json"
    ours = corpus_dir / f"{name}.ours.json"
    if xml.exists() and m21.exists():
        return xml, m21, ours if ours.exists() else None

    # Legacy: long mangled filenames (old convention encodes the full source path)
    pattern = re.compile(re.escape(name) + r'\.mxl\.xml$')
    for f in corpus_dir.glob("*.xml"):
        if pattern.search(f.name):
            base = f.with_suffix("")  # strips .xml → long stem
            m21c = base.with_suffix(".music21.json")
            oursc = base.with_suffix(".ours.json")
            if m21c.exists():
                return f, m21c, oursc if oursc.exists() else None

    return None, None, None


def build_direction_xml(rn: str, key: str, xml_offset: int) -> str:
    """Return a MusicXML <direction> block for a single Roman-numeral label."""
    label = f"{rn}  [{key}]"
    # Escape XML special chars
    label = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    offset_block = ""
    if xml_offset != 0:
        offset_block = f"\n        <offset>{xml_offset}</offset>"
    return (
        f'      <direction placement="above">\n'
        f'        <direction-type>\n'
        f'          <words font-size="7" font-style="italic">{label}</words>\n'
        f'        </direction-type>{offset_block}\n'
        f'      </direction>\n'
    )


def inject(xml_path: Path, m21_json_path: Path, out_path: Path) -> bool:
    xml_text = xml_path.read_text(encoding="utf-8")
    with open(m21_json_path, encoding="utf-8") as f:
        m21 = json.load(f)

    regions = m21.get("regions", [])
    if not regions:
        print(f"  No regions in {m21_json_path.name}", file=sys.stderr)
        return False

    # Read divisions-per-quarter from XML (assume consistent throughout)
    div_match = re.search(r"<divisions>\s*(\d+)\s*</divisions>", xml_text)
    if not div_match:
        print(f"  No <divisions> in {xml_path.name}", file=sys.stderr)
        return False
    divisions = int(div_match.group(1))
    ratio = divisions / DIVISIONS_PER_QUARTER_MS  # xml_divisions per MS tick

    # Group regions by measure number; compute per-measure start tick.
    from collections import defaultdict
    by_measure: dict[int, list[dict]] = defaultdict(list)
    for r in regions:
        by_measure[r["measureNumber"]].append(r)

    measure_start_tick: dict[int, int] = {}
    for mnum, rlist in by_measure.items():
        measure_start_tick[mnum] = min(r["startTick"] for r in rlist)

    # Build map: measure_number → list of (xml_offset, rn_text, key)
    insertions: dict[int, list[tuple[int, str, str]]] = defaultdict(list)
    for mnum, rlist in by_measure.items():
        ms_tick = measure_start_tick[mnum]
        for r in sorted(rlist, key=lambda x: x["startTick"]):
            raw_offset = (r["startTick"] - ms_tick) * ratio
            xml_offset = int(round(raw_offset))
            insertions[mnum].append((xml_offset, r["romanNumeral"], r["key"]))

    # We only inject into the FIRST <part> to keep the score clean.
    # Find the character range of the first <part>...</part>.
    first_part_match = re.search(r'<part\b[^>]*>', xml_text)
    if not first_part_match:
        print(f"  No <part> found in {xml_path.name}", file=sys.stderr)
        return False
    part_start_pos = first_part_match.start()
    part_end_match  = re.search(r'</part>', xml_text[part_start_pos:])
    if not part_end_match:
        print(f"  No </part> found", file=sys.stderr)
        return False
    part_end_pos = part_start_pos + part_end_match.end()
    part_text = xml_text[part_start_pos:part_end_pos]

    # For each measure in the first part, insert directions before the first <note>.
    # We process measures in reverse order so that string positions stay valid
    # as we insert text.
    def process_part(text: str) -> str:
        # Find all measures: collect their positions so we can process in reverse.
        measure_spans = []
        for m in re.finditer(r'<measure\b[^>]*\bnumber="(\d+)"[^>]*>(.*?)</measure>',
                              text, re.DOTALL):
            measure_spans.append((m.start(), m.end(), int(m.group(1)), m))

        # Process in reverse so indices stay valid.
        for (mstart, mend, mnum, _) in reversed(measure_spans):
            if mnum not in insertions:
                continue

            # Find the position of the first <note> inside this measure.
            measure_body = text[mstart:mend]
            note_match = re.search(r'<note\b', measure_body)
            if not note_match:
                continue  # no notes — skip (e.g. whole-rest measure might differ)
            insert_pos = mstart + note_match.start()

            # Build all direction blocks for this measure sorted by offset.
            blocks = "".join(
                build_direction_xml(rn, key, off)
                for (off, rn, key) in sorted(insertions[mnum])
            )
            text = text[:insert_pos] + blocks + text[insert_pos:]

        return text

    new_part_text = process_part(part_text)
    new_xml = xml_text[:part_start_pos] + new_part_text + xml_text[part_end_pos:]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_xml, encoding="utf-8")
    print(f"  Written: {out_path}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", metavar="NAME",
                        help="Chorale name(s), e.g. bwv66.6")
    parser.add_argument("--all", action="store_true",
                        help="Process all corpus files")
    parser.add_argument("--out", metavar="DIR", default=None,
                        help="Output directory (default: same as corpus dir)")
    args = parser.parse_args()

    # Locate corpus directory (source XMLs + JSON analyses)
    for candidate in [Path("tools/corpus"), Path("../tools/corpus"),
                      Path("tools/tools/corpus")]:
        if candidate.exists():
            corpus_dir = candidate
            break
    else:
        print("ERROR: cannot find corpus directory", file=sys.stderr)
        sys.exit(1)

    # Default output: corpus_m21_xml/ sibling of corpus/
    default_out_dir = corpus_dir.parent / "corpus_m21_xml"

    if args.all:
        # Enumerate XML files that have a matching .music21.json.
        # Skips _m21.xml files (our own output) and legacy long-named files
        # that duplicate a short-named entry.
        pairs: list[tuple[Path, Path]] = []
        seen_stems: set[str] = set()
        for xml_path in sorted(corpus_dir.glob("*.xml")):
            if xml_path.stem.endswith("_m21"):
                continue  # skip annotated output files
            # Prefer short names; skip legacy long-mangled duplicates
            stem = re.sub(r'\.mxl$', '', xml_path.stem)
            if stem in seen_stems:
                continue
            m21_path = corpus_dir / f"{stem}.music21.json"
            if not m21_path.exists():
                # Legacy: try the full long-name variant
                m21_path = xml_path.with_name(xml_path.stem + ".music21.json")
            if m21_path.exists():
                pairs.append((xml_path, m21_path))
                seen_stems.add(stem)

        out_dir = Path(args.out) if args.out else default_out_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        ok = fail = 0
        for xml_path, m21_path in pairs:
            stem = re.sub(r'\.mxl$', '', xml_path.stem)
            out_path = out_dir / f"{stem}_m21.xml"
            print(f"Processing {xml_path.name[:50]} …")
            if inject(xml_path, m21_path, out_path):
                ok += 1
            else:
                fail += 1
        print(f"\nDone: {ok} ok, {fail} failed")
        return

    names = args.names
    if not names:
        parser.print_help()
        sys.exit(0)

    out_dir = Path(args.out) if args.out else default_out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    ok = fail = 0
    for name in names:
        xml_path, m21_path, _ = find_corpus_file(name, corpus_dir)
        if xml_path is None:
            print(f"  NOT FOUND: {name}", file=sys.stderr)
            fail += 1
            continue

        out_path = out_dir / f"{name}_m21.xml"
        print(f"Processing {name} …")
        if inject(xml_path, m21_path, out_path):
            ok += 1
        else:
            fail += 1

    print(f"\nDone: {ok} ok, {fail} failed")


if __name__ == "__main__":
    main()
