#!/usr/bin/env python3
"""
inject_dcml_rn.py — Inject WiR DCML Roman-numeral labels AND our batch_analyze
chord output into a MusicXML file, so a human can compare both readings side by
side in MuseScore.

For each (measure, beat) position the script emits TWO <direction> blocks:
  - GT: <key>:<roman>     placed above the staff (DCML ground truth)
  - US: <chord> [<roman>] placed below the staff (our analyzer output)

Source XML lives in tools/corpus/ (read-only). DCML annotations live under
tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/<N>/
analysis.txt. Output goes to tools/corpus_dcml_xml/<stem>_dcml.xml.

Usage:
    python tools/inject_dcml_rn.py bwv310
    python tools/inject_dcml_rn.py --all     # all 5 hard-coded targets
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# MuseScore internal ticks per quarter note — used by our batch_analyze.
DIVISIONS_PER_QUARTER_MS = 480

# Hard-coded BWV → WiR folder mapping for the five target scores.
# (WiR uses Riemenschneider numbering, which does not match BWV order.)
WIR_MAP = {
    "bwv103.6": "120",
    "bwv283":   "198",
    "bwv293":   "154",
    "bwv310":   "238",
    "bwv319":   "181",
}

TARGETS = list(WIR_MAP.keys())

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "tools" / "corpus"
WIR_BASE = (REPO_ROOT / "tools" / "dcml" / "when_in_rome" / "Corpus"
            / "Early_Choral" / "Bach,_Johann_Sebastian" / "Chorales")
OUT_DIR = REPO_ROOT / "tools" / "corpus_dcml_xml"
BATCH_ANALYZE = REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe"


# ---------------------------------------------------------------------------
# DCML annotation parser
# ---------------------------------------------------------------------------

# A token in the DCML stream is one of:
#   - "mN" or "mNvarX"  (measure marker)
#   - "bX" or "bX.Y"    (beat marker)
#   - "<KEY>:"           (key marker — uppercase = major, lowercase = minor;
#                         e.g. "G:", "e:", "b:", "F#:", "bb:")
#   - "||" / ":||" / "|"   (phrase markers — ignored)
#   - everything else    (Roman-numeral chord label at the current beat in the
#                         current key)

KEY_RE     = re.compile(r"^[A-Ga-g][b#]?:$")
BEAT_RE    = re.compile(r"^b(\d+(?:\.\d+)?)$")
MEASURE_RE = re.compile(r"^m(\d+)(?:var\d+)?$")
PHRASE_RE  = re.compile(r"^(\|\||:\|\||\|)$")


def parse_dcml(analysis_path: Path) -> list[tuple[str, float, str, str]]:
    """Parse a WiR DCML analysis.txt and return labels.

    Returns a list of (measure_token, beat, key, roman) tuples where:
      - measure_token is the raw measure number string (e.g. "0", "1", "4")
      - beat is float (1.0, 2.0, 2.5, ...)
      - key is the most recent key marker including its colon (e.g. "G:", "e:")
      - roman is the chord symbol token (e.g. "I6", "viio6/V", "ii/o2")

    Variant lines (mNvarX) are skipped to avoid stacking redundant labels.
    """
    if not analysis_path.exists():
        return []

    labels: list[tuple[str, float, str, str]] = []
    current_key = ""

    for raw_line in analysis_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # Strip header lines, Notes, Form lines, etc. — only process lines
        # beginning with "m<digits>".
        if not line.startswith("m") or len(line) < 2 or not line[1].isdigit():
            continue

        tokens = line.split()
        # First token is the measure marker. Skip variant measures.
        m_match = MEASURE_RE.match(tokens[0])
        if not m_match:
            continue
        if "var" in tokens[0]:
            continue
        measure_str = m_match.group(1)
        current_beat = 1.0

        for tok in tokens[1:]:
            if PHRASE_RE.match(tok):
                continue
            b_match = BEAT_RE.match(tok)
            if b_match:
                current_beat = float(b_match.group(1))
                continue
            if KEY_RE.match(tok):
                current_key = tok  # keep the colon
                continue
            # Everything else is a Roman-numeral label.
            labels.append((measure_str, current_beat, current_key, tok))

    return labels


# ---------------------------------------------------------------------------
# batch_analyze JSON loader
# ---------------------------------------------------------------------------

def ensure_batch_json(stem: str, json_dir: Path) -> Path:
    """Run batch_analyze if no JSON exists yet; return path to JSON."""
    json_dir.mkdir(parents=True, exist_ok=True)
    out_path = json_dir / f"{stem}_our.json"
    if out_path.exists() and out_path.stat().st_size > 0:
        return out_path

    score = CORPUS_DIR / f"{stem}.xml"
    if not score.exists():
        raise FileNotFoundError(f"score not found: {score}")
    if not BATCH_ANALYZE.exists():
        raise FileNotFoundError(f"batch_analyze not built: {BATCH_ANALYZE}")

    print(f"  running batch_analyze on {stem}.xml ...")
    cp = subprocess.run(
        [str(BATCH_ANALYZE), str(score), "--preset", "Baroque"],
        capture_output=True, text=True, check=False,
    )
    if cp.returncode != 0:
        raise RuntimeError(f"batch_analyze failed for {stem}: {cp.stderr[:500]}")
    out_path.write_text(cp.stdout, encoding="utf-8")
    return out_path


def load_our_regions(json_path: Path) -> list[dict]:
    """Return our analyzer's regions (each has measureNumber, beat, chordSymbol,
    romanNumeral, startTick, endTick)."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    return data.get("regions", [])


# ---------------------------------------------------------------------------
# MusicXML insertion
# ---------------------------------------------------------------------------

def build_direction(label: str, placement: str, default_y: int | None,
                    xml_offset: int) -> str:
    """Build a single <direction> block containing one <words> element."""
    label = (label.replace("&", "&amp;")
                  .replace("<", "&lt;")
                  .replace(">", "&gt;"))
    dy_attr = f' default-y="{default_y}"' if default_y is not None else ""
    offset_block = ""
    if xml_offset != 0:
        offset_block = f"\n        <offset>{xml_offset}</offset>"
    return (
        f'      <direction placement="{placement}">\n'
        f'        <direction-type>\n'
        f'          <words font-size="7" font-weight="bold"{dy_attr}>'
        f'{label}</words>\n'
        f'        </direction-type>{offset_block}\n'
        f'      </direction>\n'
    )


def inject(stem: str, analysis_path: Path, our_json: Path, out_path: Path) -> bool:
    """Inject GT (DCML) and US (our analyzer) labels into the score."""
    xml_path = CORPUS_DIR / f"{stem}.xml"
    xml_text = xml_path.read_text(encoding="utf-8")

    dcml_labels = parse_dcml(analysis_path)
    if not dcml_labels:
        print(f"  no DCML labels parsed for {stem}", file=sys.stderr)

    our_regions = load_our_regions(our_json)
    if not our_regions:
        print(f"  no our-regions in {our_json}", file=sys.stderr)

    # Read divisions from XML (must be consistent throughout).
    div_match = re.search(r"<divisions>\s*(\d+)\s*</divisions>", xml_text)
    if not div_match:
        print(f"  no <divisions> in {xml_path.name}", file=sys.stderr)
        return False
    divisions = int(div_match.group(1))

    # Beat 1 → offset 0; beat 2 → offset = divisions; etc. (assumes 4/4-ish)
    def beat_to_xml_offset(beat: float) -> int:
        # Beat 1.0 → 0, beat 2.0 → divisions, beat 1.5 → divisions/2.
        return int(round((beat - 1.0) * divisions))

    # Build insertion map keyed by measure_str → list of direction blocks
    # (each entry is (xml_offset, block_text)) for sorting/dedup.
    insertions: dict[str, list[tuple[int, str]]] = defaultdict(list)

    # --- GT labels (above) ----------------------------------------------
    for (m_str, beat, key, roman) in dcml_labels:
        label = f"GT: {key}{roman}" if key else f"GT: {roman}"
        block = build_direction(label, placement="above",
                                default_y=30,
                                xml_offset=beat_to_xml_offset(beat))
        insertions[m_str].append((beat_to_xml_offset(beat), block))

    # --- US labels (below) ----------------------------------------------
    # Our regions use 1-based integer measureNumber and float beat. Map to
    # the same measure_str the XML uses. If a corresponding measure_str exists
    # in the XML use that; otherwise stringify the integer.
    # (We only know the XML measure-number set after scanning the XML; do that
    #  in process_part.)
    pending_us: list[tuple[int, float, str]] = []
    for r in our_regions:
        m_num = r["measureNumber"]
        beat = float(r.get("beat", 1.0))
        chord = r.get("chordSymbol", "")
        roman = r.get("romanNumeral", "")
        if chord or roman:
            label = f"US: {chord} [{roman}]"
        else:
            label = "US: (none)"
        pending_us.append((m_num, beat, label))

    # ---- Inject into the FIRST <part> only -----------------------------
    first_part_match = re.search(r'<part\b[^>]*>', xml_text)
    if not first_part_match:
        print(f"  no <part> in {xml_path.name}", file=sys.stderr)
        return False
    part_start_pos = first_part_match.start()
    part_end_rel = re.search(r'</part>', xml_text[part_start_pos:])
    if not part_end_rel:
        print(f"  no </part> in {xml_path.name}", file=sys.stderr)
        return False
    part_end_pos = part_start_pos + part_end_rel.end()
    part_text = xml_text[part_start_pos:part_end_pos]

    # Discover the measure numbers actually present in the first part.
    measure_spans = []
    for m in re.finditer(
        r'<measure\b[^>]*\bnumber="([^"]+)"[^>]*>(.*?)</measure>',
        part_text, re.DOTALL,
    ):
        measure_spans.append((m.start(), m.end(), m.group(1)))

    xml_measure_numbers = {m_str for _, _, m_str in measure_spans}

    # Resolve US labels against the actual XML measure_str set.
    for (m_num, beat, label) in pending_us:
        # Try the raw integer first.
        m_str_candidate = str(m_num)
        if m_str_candidate not in xml_measure_numbers:
            # Some scores have implicit pickup at number=0 — try that.
            # Otherwise skip with a warning.
            print(f"  warning: our region m={m_num} not in XML measure numbers "
                  f"for {stem}; skipping", file=sys.stderr)
            continue
        block = build_direction(label, placement="below",
                                default_y=-60,
                                xml_offset=beat_to_xml_offset(beat))
        insertions[m_str_candidate].append((beat_to_xml_offset(beat), block))

    # Process measures in REVERSE order so that string positions stay valid
    # as we insert text.
    new_part_text = part_text
    for (mstart, mend, m_str) in reversed(measure_spans):
        if m_str not in insertions:
            continue
        # Find the position of the first <note> inside this measure.
        measure_body = new_part_text[mstart:mend]
        note_match = re.search(r'<note\b', measure_body)
        if not note_match:
            continue
        insert_pos = mstart + note_match.start()

        # Sort by (xml_offset, GT-first-US-second order encoded in label).
        # Stable sort: GT vs US is encoded in the block text itself; we just
        # sort by xml_offset.
        sorted_blocks = sorted(insertions[m_str], key=lambda t: t[0])
        blocks_text = "".join(block for _, block in sorted_blocks)

        new_part_text = (new_part_text[:insert_pos]
                         + blocks_text
                         + new_part_text[insert_pos:])

    new_xml = (xml_text[:part_start_pos]
               + new_part_text
               + xml_text[part_end_pos:])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_xml, encoding="utf-8")
    print(f"  written: {out_path} "
          f"(DCML labels: {len(dcml_labels)}, US regions: {len(our_regions)})")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stems", nargs="*", help="score stems (e.g. bwv310)")
    ap.add_argument("--all", action="store_true",
                    help="process all five targets")
    ap.add_argument("--json-dir", default="/c/tmp/spotcheck",
                    help="directory to read/write batch_analyze JSON outputs")
    args = ap.parse_args()

    stems = TARGETS if args.all else args.stems
    if not stems:
        ap.print_help()
        sys.exit(0)

    json_dir_arg = args.json_dir
    # Honour both /c/tmp/... (msys) and C:/tmp/... (windows) styles.
    if json_dir_arg.startswith("/c/"):
        json_dir_arg = "C:" + json_dir_arg[2:]
    json_dir = Path(json_dir_arg)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    ok = fail = 0
    for stem in stems:
        if stem not in WIR_MAP:
            print(f"  unknown stem: {stem}", file=sys.stderr)
            fail += 1
            continue
        wir_folder = WIR_MAP[stem]
        analysis_path = WIR_BASE / wir_folder / "analysis.txt"
        if not analysis_path.exists():
            print(f"  missing WiR analysis: {analysis_path}", file=sys.stderr)
            fail += 1
            continue

        # Use cached JSON in json_dir if present (the previous task's outputs
        # used names like bwv310_out.json — fall back to that pattern too).
        our_json_alt = json_dir / f"{stem}_out.json"
        if our_json_alt.exists():
            our_json = our_json_alt
        else:
            try:
                our_json = ensure_batch_json(stem, json_dir)
            except Exception as exc:
                print(f"  batch_analyze error for {stem}: {exc}", file=sys.stderr)
                fail += 1
                continue

        out_path = OUT_DIR / f"{stem}_dcml.xml"
        print(f"Processing {stem} ...")
        try:
            if inject(stem, analysis_path, our_json, out_path):
                ok += 1
            else:
                fail += 1
        except Exception as exc:
            print(f"  inject error: {exc}", file=sys.stderr)
            fail += 1

    print(f"\nDone: {ok} ok, {fail} failed")


if __name__ == "__main__":
    main()
