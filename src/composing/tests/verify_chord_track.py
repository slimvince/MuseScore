#!/usr/bin/env python3
"""
Standalone verifier for chord track annotations in MusicXML files exported
from MuseScore's "implode to chord track" feature.

Checks internal consistency of chord symbols, Roman numerals, key labels,
non-diatonic markers, cadence labels, and borrowed-chord annotations against
the sounding pitch classes in the source voices.

Usage:
    python verify_chord_track.py [directory_or_file]

Requires only the Python standard library (xml.etree.ElementTree).
"""

from __future__ import annotations

import io
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

STEP_TO_PC: Dict[str, int] = {
    "C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11,
}

PC_TO_NAME: Dict[int, str] = {
    0: "C", 1: "C#/Db", 2: "D", 3: "D#/Eb", 4: "E", 5: "F",
    6: "F#/Gb", 7: "G", 8: "G#/Ab", 9: "A", 10: "A#/Bb", 11: "B",
}

# Scale interval patterns (semitones from tonic)
SCALE_INTERVALS: Dict[str, List[int]] = {
    "major":      [0, 2, 4, 5, 7, 9, 11],
    "ionian":     [0, 2, 4, 5, 7, 9, 11],
    "dorian":     [0, 2, 3, 5, 7, 9, 10],
    "phrygian":   [0, 1, 3, 5, 7, 8, 10],
    "lydian":     [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor":      [0, 2, 3, 5, 7, 8, 10],
    "aeolian":    [0, 2, 3, 5, 7, 8, 10],
    "locrian":    [0, 1, 3, 5, 6, 8, 10],
}

# Mode offsets from Ionian tonic (used for key-sig-based tonic calculation)
MODE_OFFSETS: Dict[str, int] = {
    "major": 0, "ionian": 0,
    "dorian": 2, "phrygian": 4, "lydian": 5,
    "mixolydian": 7, "minor": 9, "aeolian": 9,
    "locrian": 11,
}

# Roman numeral text -> zero-based degree
ROMAN_TO_DEGREE: Dict[str, int] = {
    "I": 0, "i": 0,
    "II": 1, "ii": 1,
    "III": 2, "iii": 2,
    "IV": 3, "iv": 3,
    "V": 4, "v": 4,
    "VI": 5, "vi": 5,
    "VII": 6, "vii": 6,
}

# Quality -> defining intervals (semitones from root)
QUALITY_INTERVALS: Dict[str, List[int]] = {
    "major":                [4, 7],
    "minor":                [3, 7],
    "diminished":           [3, 6],
    "diminished-seventh":   [3, 6, 9],
    "augmented":            [4, 8],
    "dominant":             [4, 7, 10],
    "dominant-ninth":       [4, 7, 10],
    "dominant-11th":        [4, 7, 10],
    "dominant-13th":        [4, 7, 10],
    "minor-seventh":        [3, 7, 10],
    "major-seventh":        [4, 7, 11],
    "minor-ninth":          [3, 7, 10],
    "minor-11th":           [3, 7, 10],
    "minor-13th":           [3, 7, 10],
    "major-ninth":          [4, 7, 11],
    "major-11th":           [4, 7, 11],
    "major-13th":           [4, 7, 11],
    "major-sixth":          [4, 7],
    "minor-sixth":          [3, 7],
    "half-diminished":      [3, 6, 10],
    "suspended-fourth":     [5, 7],
    "suspended-second":     [2, 7],
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ChordSymbol:
    """A chord symbol extracted from a <harmony> with <root>."""
    root_pc: int
    root_name: str
    kind: str           # MusicXML kind value (e.g. "minor-seventh")
    kind_text: str      # display text (e.g. "m7")
    bass_pc: Optional[int] = None
    bass_name: Optional[str] = None
    inversion: Optional[int] = None


@dataclass
class RomanNumeral:
    """A Roman numeral extracted from a <harmony> with <numeral>."""
    text: str           # e.g. "V", "vi", "bIII"
    degree: int         # zero-based: I=0 .. VII=6
    kind: str           # MusicXML kind in the numeral harmony
    inversion: Optional[int] = None
    accidental: int = 0  # -1 for flat prefix, +1 for sharp prefix


@dataclass
class Annotation:
    """A staff text annotation from <direction><words>."""
    text: str
    staff: int = 1


@dataclass
class MeasureData:
    """All extracted data for a single measure position in the chord track."""
    number: str = ""
    chord_symbols: List[ChordSymbol] = field(default_factory=list)
    roman_numerals: List[RomanNumeral] = field(default_factory=list)
    annotations: List[Annotation] = field(default_factory=list)
    # Extracted annotation semantics
    key_label: Optional[str] = None           # e.g. "D major"
    key_tentative: bool = False               # ends with "?"
    non_diatonic: bool = False                # star marker present (any chord)
    borrowed_from: List[str] = field(default_factory=list)  # e.g. ["from G major"]
    cadence: Optional[str] = None             # PAC, PC, DC, HC (measure-level)
    cadence_chord_idx: int = 0               # chord index the cadence label belongs to
    pivot: Optional[str] = None               # pivot text
    key_relationship: Optional[str] = None    # relationship text
    # Per-chord annotation tracking (chord index -> list of annotations)
    per_chord_stars: Dict[int, bool] = field(default_factory=dict)
    per_chord_borrowed: Dict[int, List[str]] = field(default_factory=dict)
    # Chord→RN association: maps chord_symbols index to its RomanNumeral.
    # In MusicXML, a <harmony> with <numeral> follows the <harmony> with <root>
    # it belongs to.  Non-diatonic chords have no Roman numeral, so the lists
    # are not 1:1 — this mapping is the authoritative pairing.
    chord_to_rn: Dict[int, "RomanNumeral"] = field(default_factory=dict)


@dataclass
class KeyState:
    """Current key/mode state as we walk through measures."""
    tonic_pc: int = 2     # default D
    mode: str = "major"   # default major
    label: str = "D major"

    @property
    def scale_pcs(self) -> Set[int]:
        intervals = SCALE_INTERVALS.get(self.mode, SCALE_INTERVALS["major"])
        return {(self.tonic_pc + i) % 12 for i in intervals}

    @property
    def scale_degrees(self) -> List[int]:
        """Pitch class for each scale degree (0-based: 0=tonic, 1=supertonic, ...)."""
        intervals = SCALE_INTERVALS.get(self.mode, SCALE_INTERVALS["major"])
        return [(self.tonic_pc + i) % 12 for i in intervals]


@dataclass
class CheckResult:
    measure: str
    level: str      # "PASS", "WARN", "FAIL"
    message: str
    category: str = ""


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def step_alter_to_pc(step: str, alter: float = 0.0) -> int:
    """Convert a MusicXML step + alter to pitch class (0-11)."""
    base = STEP_TO_PC.get(step, 0)
    return (base + round(alter)) % 12


def pc_name(pc: int) -> str:
    return PC_TO_NAME.get(pc % 12, "?")


def parse_key_fifths(fifths: int) -> int:
    """Convert key signature fifths to Ionian (major) tonic pitch class."""
    return ((fifths * 7) % 12 + 12) % 12


def parse_key_mode_label(text: str) -> Optional[Tuple[int, str, str]]:
    """
    Parse a key/mode label like "D major", "D# Phrygian", "A# Dorian".
    Returns (tonic_pc, mode_lower, full_label) or None.

    Also handles tentative labels wrapped in parens with "?":
      "(B minor?)"  ->  tonic_pc for B, mode="minor", label="B minor"
      "(G Lydian?) (-> relative major)"  ->  tonic_pc for G, mode="lydian"
    """
    # Strip surrounding parens, question marks, and relationship suffixes
    # Pattern: optional "(" + note name + mode + optional "?" + optional ")"
    # followed by optional relationship info
    m = re.match(
        r'\(?\s*([A-G][#b♯♭]*)\s+'
        r'(major|minor|[Ii]onian|[Dd]orian|[Pp]hrygian|[Ll]ydian|'
        r'[Mm]ixolydian|[Aa]eolian|[Ll]ocrian)'
        r'\s*\??\s*\)?',
        text
    )
    if not m:
        return None

    note_str = m.group(1)
    mode_str = m.group(2).lower()

    # Parse the note name
    step = note_str[0]
    alter = 0.0
    for ch in note_str[1:]:
        if ch in ('#', '\u266f'):
            alter += 1.0
        elif ch in ('b', '\u266d'):
            alter -= 1.0

    tonic_pc = step_alter_to_pc(step, alter)
    full_label = f"{note_str} {mode_str}"
    return (tonic_pc, mode_str, full_label)


def parse_roman_text(text: str) -> Tuple[int, int]:
    """
    Parse a Roman numeral text like "V", "vi", "bIII", "#IV".
    Returns (degree_0based, accidental_semitones).
    """
    accidental = 0
    remainder = text
    # Strip leading accidental
    while remainder and remainder[0] in ('b', '#', '\u266d', '\u266f'):
        if remainder[0] in ('b', '\u266d'):
            accidental -= 1
        else:
            accidental += 1
        remainder = remainder[1:]

    # Match the Roman numeral core (strip any trailing quality/inversion suffixes)
    core_match = re.match(r'^(VII|vii|VI|vi|IV|iv|III|iii|II|ii|V|v|I|i)', remainder)
    if core_match:
        core = core_match.group(1)
        degree = ROMAN_TO_DEGREE.get(core, 0)
    else:
        degree = 0

    return (degree, accidental)


def parse_borrowed_source(text: str) -> Optional[Tuple[int, str]]:
    """
    Parse "from X major/minor/Dorian/etc." and return (tonic_pc, mode).
    """
    m = re.match(
        r'from\s+([A-G][#b♯♭]*)\s+'
        r'(major|minor|[Ii]onian|[Dd]orian|[Pp]hrygian|[Ll]ydian|'
        r'[Mm]ixolydian|[Aa]eolian|[Ll]ocrian)',
        text
    )
    if not m:
        return None
    note_str = m.group(1)
    mode_str = m.group(2).lower()

    step = note_str[0]
    alter = 0.0
    for ch in note_str[1:]:
        if ch in ('#', '\u266f'):
            alter += 1.0
        elif ch in ('b', '\u266d'):
            alter -= 1.0

    tonic_pc = step_alter_to_pc(step, alter)
    return (tonic_pc, mode_str)


def get_scale_pcs(tonic_pc: int, mode: str) -> Set[int]:
    """Build the set of diatonic pitch classes for a given tonic and mode."""
    intervals = SCALE_INTERVALS.get(mode, SCALE_INTERVALS["major"])
    return {(tonic_pc + i) % 12 for i in intervals}


def get_scale_degree_pcs(tonic_pc: int, mode: str) -> List[int]:
    """Pitch class for each of the 7 scale degrees."""
    intervals = SCALE_INTERVALS.get(mode, SCALE_INTERVALS["major"])
    return [(tonic_pc + i) % 12 for i in intervals]


# ---------------------------------------------------------------------------
# MusicXML extraction
# ---------------------------------------------------------------------------

def find_parts(root: ET.Element) -> Tuple[List[Tuple[str, str]], Optional[Tuple[str, str]]]:
    """
    Find all parts; return (source_parts, chord_track_part).
    Each part is (part_id, part_name).
    """
    part_list = root.find("part-list")
    if part_list is None:
        return [], None

    parts_info: List[Tuple[str, str]] = []
    chord_track: Optional[Tuple[str, str]] = None

    for sp in part_list.findall("score-part"):
        pid = sp.get("id", "")
        name_el = sp.find("part-name")
        name = name_el.text.strip() if name_el is not None and name_el.text else ""
        parts_info.append((pid, name))
        if "chord" in name.lower():
            chord_track = (pid, name)

    source_parts = [(pid, name) for pid, name in parts_info if chord_track is None or pid != chord_track[0]]
    return source_parts, chord_track


def extract_sounding_pcs(root: ET.Element, source_part_ids: List[str]) -> Dict[str, Set[int]]:
    """
    For each measure number, collect all sounding pitch classes from the source
    parts.  Tied continuations (tie type="stop" without a matching "start" on
    the same note element) still contribute their pitch class - the note is
    sounding.
    """
    measure_pcs: Dict[str, Set[int]] = {}

    for part_el in root.findall("part"):
        pid = part_el.get("id", "")
        if pid not in source_part_ids:
            continue

        for measure_el in part_el.findall("measure"):
            mnum = measure_el.get("number", "?")
            if mnum not in measure_pcs:
                measure_pcs[mnum] = set()

            for note_el in measure_el.findall("note"):
                # Skip rests
                if note_el.find("rest") is not None:
                    continue

                pitch_el = note_el.find("pitch")
                if pitch_el is None:
                    continue

                step_el = pitch_el.find("step")
                if step_el is None or step_el.text is None:
                    continue

                alter_el = pitch_el.find("alter")
                alter = float(alter_el.text) if alter_el is not None and alter_el.text else 0.0

                pc = step_alter_to_pc(step_el.text, alter)
                measure_pcs[mnum].add(pc)

    return measure_pcs


def extract_key_sigs(root: ET.Element, part_id: str) -> Dict[str, int]:
    """
    Extract key signature changes (fifths) from a given part, keyed by measure
    number.  Returns the fifths value active at the start of each measure where
    it changes.
    """
    key_sigs: Dict[str, int] = {}
    for part_el in root.findall("part"):
        if part_el.get("id") != part_id:
            continue
        for measure_el in part_el.findall("measure"):
            mnum = measure_el.get("number", "?")
            attrs = measure_el.find("attributes")
            if attrs is not None:
                key_el = attrs.find("key")
                if key_el is not None:
                    fifths_el = key_el.find("fifths")
                    if fifths_el is not None and fifths_el.text:
                        key_sigs[mnum] = int(fifths_el.text)
    return key_sigs


def extract_chord_track_data(
    root: ET.Element, chord_part_id: str
) -> List[MeasureData]:
    """
    Walk through the chord track part and extract harmony elements,
    direction/words annotations, for each measure.
    """
    measures: List[MeasureData] = []

    for part_el in root.findall("part"):
        if part_el.get("id") != chord_part_id:
            continue

        for measure_el in part_el.findall("measure"):
            md = MeasureData(number=measure_el.get("number", "?"))

            # Iterate children in document order to pair chord symbols with
            # Roman numerals that follow them, and to associate annotations
            # (stars, borrowed-from) with the most recently preceding chord.
            #
            # MusicXML groups harmonies (treble staff) before directions (bass
            # staff, after <backup>).  Track tick position so directions can be
            # paired with the harmony at the same tick rather than always the
            # last one.
            chord_idx = -1  # index of the most recent chord symbol
            current_tick = 0  # cumulative tick within measure
            chord_tick_map: Dict[int, int] = {}  # tick -> chord index
            for child in measure_el:
                if child.tag == "harmony":
                    if _parse_harmony(child, md, chord_idx):
                        chord_idx = len(md.chord_symbols) - 1
                        chord_tick_map[current_tick] = chord_idx
                elif child.tag == "direction":
                    # Find chord at current tick position
                    dir_chord_idx = chord_tick_map.get(current_tick, chord_idx)
                    _parse_direction_per_chord(child, md, dir_chord_idx)
                elif child.tag == "note":
                    # <chord/> notes don't advance the tick
                    if child.find("chord") is None:
                        dur_el = child.find("duration")
                        if dur_el is not None and dur_el.text:
                            current_tick += int(dur_el.text)
                elif child.tag == "forward":
                    dur_el = child.find("duration")
                    if dur_el is not None and dur_el.text:
                        current_tick += int(dur_el.text)
                elif child.tag == "backup":
                    dur_el = child.find("duration")
                    if dur_el is not None and dur_el.text:
                        current_tick -= int(dur_el.text)

            # Parse remaining annotation semantics (key labels, cadences, etc.)
            _classify_annotations(md)
            measures.append(md)

    return measures


def _parse_harmony(harmony_el: ET.Element, md: MeasureData,
                   chord_idx: int) -> bool:
    """Parse a <harmony> element into either a ChordSymbol or RomanNumeral.
    Returns True if a ChordSymbol was added (not a RomanNumeral).

    chord_idx is the index of the most recently added chord symbol; a Roman
    numeral is associated with that chord via md.chord_to_rn."""
    numeral_el = harmony_el.find("numeral")
    root_el = harmony_el.find("root")

    kind_el = harmony_el.find("kind")
    kind_val = kind_el.text.strip() if kind_el is not None and kind_el.text else "major"
    kind_text = kind_el.get("text", "") if kind_el is not None else ""

    inversion_el = harmony_el.find("inversion")
    inversion = int(inversion_el.text) if inversion_el is not None and inversion_el.text else None

    if numeral_el is not None:
        # Roman numeral harmony — associate with the most recent chord symbol
        nr_el = numeral_el.find("numeral-root")
        if nr_el is not None:
            rn_text = nr_el.get("text", "")
            degree, accidental = parse_roman_text(rn_text)
            rn = RomanNumeral(
                text=rn_text,
                degree=degree,
                kind=kind_val,
                inversion=inversion,
                accidental=accidental,
            )
            md.roman_numerals.append(rn)
            if chord_idx >= 0:
                md.chord_to_rn[chord_idx] = rn
        return False

    elif root_el is not None:
        # Chord symbol harmony
        root_step_el = root_el.find("root-step")
        root_alter_el = root_el.find("root-alter")
        if root_step_el is not None and root_step_el.text:
            r_step = root_step_el.text
            r_alter = float(root_alter_el.text) if root_alter_el is not None and root_alter_el.text else 0.0
            r_pc = step_alter_to_pc(r_step, r_alter)
            r_name = r_step
            if r_alter > 0:
                r_name += "#" * int(round(r_alter))
            elif r_alter < 0:
                r_name += "b" * int(round(abs(r_alter)))

            cs = ChordSymbol(
                root_pc=r_pc,
                root_name=r_name,
                kind=kind_val,
                kind_text=kind_text,
            )

            # Bass note
            bass_el = harmony_el.find("bass")
            if bass_el is not None:
                bs_el = bass_el.find("bass-step")
                ba_el = bass_el.find("bass-alter")
                if bs_el is not None and bs_el.text:
                    b_step = bs_el.text
                    b_alter = float(ba_el.text) if ba_el is not None and ba_el.text else 0.0
                    cs.bass_pc = step_alter_to_pc(b_step, b_alter)
                    cs.bass_name = b_step
                    if b_alter > 0:
                        cs.bass_name += "#" * int(round(b_alter))
                    elif b_alter < 0:
                        cs.bass_name += "b" * int(round(abs(b_alter)))

            cs.inversion = inversion
            md.chord_symbols.append(cs)
            return True

    return False


def _parse_direction_per_chord(
    direction_el: ET.Element, md: MeasureData, chord_idx: int
) -> None:
    """Parse <direction> elements and associate per-chord annotations
    (stars, borrowed-from) with the most recently preceding chord."""
    staff_el = direction_el.find("staff")
    staff = int(staff_el.text) if staff_el is not None and staff_el.text else 1

    for dt in direction_el.findall("direction-type"):
        for words_el in dt.findall("words"):
            if words_el.text:
                text = words_el.text.strip()
                if not text:
                    continue
                md.annotations.append(Annotation(text=text, staff=staff))

                # Associate stars, borrowed-from, and cadences with the current chord
                if chord_idx >= 0:
                    if text == "\u2605" or text.strip() == "\u2605":
                        md.per_chord_stars[chord_idx] = True
                    elif text.startswith("from "):
                        md.per_chord_borrowed.setdefault(
                            chord_idx, []
                        ).append(text)
                    elif text in ("PAC", "PC", "DC", "HC"):
                        md.cadence_chord_idx = chord_idx


def _classify_annotations(md: MeasureData) -> None:
    """Classify annotation texts into semantic categories."""
    for ann in md.annotations:
        text = ann.text

        # Non-diatonic star marker
        if text == "\u2605" or text.strip() == "\u2605":
            md.non_diatonic = True
            continue

        # Cadence labels
        if text in ("PAC", "PC", "DC", "HC"):
            md.cadence = text
            continue

        # Borrowed chord source: "from X major/minor/..."
        if text.startswith("from "):
            md.borrowed_from.append(text)
            continue

        # Pivot chord — new format: "vi \u2192 ii" (two Roman numerals separated
        # by U+2192 with no spaces inside either token).  Also handle the old
        # "pivot: …" prefix for backward compatibility with legacy chord staff files.
        if text.startswith("pivot:") or text.startswith("pivot "):
            md.pivot = text
            continue
        if re.match(r'^[^\s(]+\s+\u2192\s+[^\s]+$', text):
            md.pivot = text
            continue

        # Key relationship embedded in parens: "(B minor?) (-> relative minor)"
        # or standalone key label: "D major"
        if "\u2192" in text:
            md.key_relationship = text
            # Try to also extract key from this text
            parsed = parse_key_mode_label(text)
            if parsed:
                md.key_label = f"{parsed[2]}"
                md.key_tentative = "?" in text
            continue

        # Key/mode label
        parsed = parse_key_mode_label(text)
        if parsed:
            md.key_label = f"{parsed[2]}"
            md.key_tentative = "?" in text
            continue


# ---------------------------------------------------------------------------
# Consistency checks
# ---------------------------------------------------------------------------

def run_checks(
    measures: List[MeasureData],
    sounding_pcs: Dict[str, Set[int]],
    initial_key_fifths: int,
) -> List[CheckResult]:
    """Run all consistency checks and return results."""
    results: List[CheckResult] = []
    key = KeyState(
        tonic_pc=parse_key_fifths(initial_key_fifths),
        mode="major",
        label=f"{pc_name(parse_key_fifths(initial_key_fifths))} major",
    )

    prev_measure: Optional[MeasureData] = None
    prev_key = KeyState(tonic_pc=key.tonic_pc, mode=key.mode, label=key.label)

    for md in measures:
        # Update key state if this measure has a key label
        if md.key_label:
            parsed = parse_key_mode_label(md.key_label)
            if parsed:
                prev_key = KeyState(tonic_pc=key.tonic_pc, mode=key.mode, label=key.label)
                key = KeyState(tonic_pc=parsed[0], mode=parsed[1], label=parsed[2])

        pcs = sounding_pcs.get(md.number, set())

        # Process each chord symbol paired with its Roman numeral (if any).
        # Use chord_to_rn for correct pairing — Roman numerals follow their
        # chord symbol in the MusicXML, so non-diatonic chords (no RN) don't
        # shift the mapping.
        for i, cs in enumerate(md.chord_symbols):
            rn = md.chord_to_rn.get(i)
            label = _chord_display(cs, rn)

            # --- Check 1: Root presence ---
            results.append(_check_root_presence(md.number, cs, rn, pcs, label))

            # --- Check 2: Quality consistency ---
            results.append(_check_quality(md.number, cs, rn, pcs, label))

            # --- Check 3: Roman numeral vs stated key ---
            # When a key change happens mid-measure, earlier chords may have
            # been analyzed in the previous key.  Try prev_key as fallback.
            if rn is not None:
                result = _check_roman_degree(md.number, cs, rn, key, label)
                if result.level == "FAIL" and md.key_label:
                    alt = _check_roman_degree(md.number, cs, rn, prev_key, label)
                    if alt.level == "PASS":
                        result = CheckResult(
                            md.number, "PASS",
                            f"{label} -- degree {rn.text} matches previous key "
                            f"{prev_key.label} (mid-measure key change to {key.label})",
                            category="degree-ok-prev-key",
                        )
                results.append(result)

            # --- Check 4: Non-diatonic marker consistency ---
            if rn is not None:
                chord_has_star = md.per_chord_stars.get(i, False)
                results.append(_check_non_diatonic_per_chord(
                    md.number, cs, rn, chord_has_star, key, label))

            # --- Check 5: Cadence pattern consistency ---
            # Check cadence on the chord the label was actually associated with.
            if i == md.cadence_chord_idx and md.cadence and rn is not None:
                # Build a synthetic "previous" MeasureData containing the chord
                # immediately before the cadence resolution chord.
                if i > 0 and md.roman_numerals:
                    # Previous chord is within same measure — find the RN
                    # for chord i-1 (walk backward through chord_to_rn).
                    prev_rn_for_cad = None
                    for ci in range(i - 1, -1, -1):
                        if ci in md.chord_to_rn:
                            prev_rn_for_cad = md.chord_to_rn[ci]
                            break
                    if prev_rn_for_cad is not None:
                        synth_prev = MeasureData(
                            number=md.number,
                            roman_numerals=[prev_rn_for_cad],
                        )
                        results.append(_check_cadence(md, rn, synth_prev, key, label))
                elif prev_measure is not None:
                    results.append(_check_cadence(md, rn, prev_measure, key, label))

            # --- Check 6: Borrowed chord source (per-chord) ---
            chord_borrows = md.per_chord_borrowed.get(i, [])
            for borrow_text in chord_borrows:
                results.append(_check_borrowed(md.number, cs, rn, borrow_text, label))

        prev_measure = md

    # Filter out None results
    return [r for r in results if r is not None]


def _chord_display(cs: ChordSymbol, rn: Optional[RomanNumeral]) -> str:
    """Build a display string for the chord."""
    parts = [cs.root_name]
    if cs.kind_text:
        parts.append(cs.kind_text)
    else:
        # Use kind directly but abbreviated
        kind_abbrev = {
            "major": "", "minor": "m", "dominant": "7",
            "diminished": "dim", "augmented": "aug",
            "suspended-fourth": "sus4", "suspended-second": "sus2",
            "minor-seventh": "m7", "major-seventh": "Maj7",
            "half-diminished": "m7b5",
        }
        parts.append(kind_abbrev.get(cs.kind, cs.kind))

    text = "".join(parts)

    if cs.bass_name:
        text += f"/{cs.bass_name}"

    if rn is not None:
        inv_str = ""
        if rn.inversion is not None:
            inv_labels = {1: " inv1", 2: " inv2", 3: " inv3"}
            inv_str = inv_labels.get(rn.inversion, f" inv{rn.inversion}")
        text += f" ({rn.text}{inv_str})"

    return text


def _check_root_presence(
    mnum: str, cs: ChordSymbol, rn: Optional[RomanNumeral],
    pcs: Set[int], label: str
) -> CheckResult:
    """Check 1: Is the chord root present in the sounding pitch classes?"""
    if not pcs:
        return CheckResult(
            mnum, "WARN",
            f"{label} -- no sounding pitches in source voices",
            category="no-sounding-pitches",
        )

    root_present = cs.root_pc in pcs
    if root_present:
        return CheckResult(
            mnum, "PASS",
            f"{label} -- root {cs.root_name}({cs.root_pc}) present in {_fmt_pcs(pcs)}",
            category="root-presence",
        )
    else:
        return CheckResult(
            mnum, "WARN",
            f"{label} -- root {cs.root_name}({cs.root_pc}) NOT in {_fmt_pcs(pcs)} (may be implied)",
            category="root-absent",
        )


def _check_quality(
    mnum: str, cs: ChordSymbol, rn: Optional[RomanNumeral],
    pcs: Set[int], label: str
) -> CheckResult:
    """Check 2: Are the defining intervals for the quality present?"""
    if not pcs:
        return CheckResult(
            mnum, "PASS",
            f"{label} -- quality {cs.kind}: no sounding pitches to check",
            category="quality-no-data",
        )

    expected_intervals = QUALITY_INTERVALS.get(cs.kind)
    if expected_intervals is None:
        return CheckResult(
            mnum, "PASS",
            f"{label} -- quality '{cs.kind}' not in check table, skipping",
            category="quality-unknown",
        )

    missing = []
    for interval in expected_intervals:
        needed_pc = (cs.root_pc + interval) % 12
        if needed_pc not in pcs:
            missing.append(f"{pc_name(needed_pc)}({needed_pc})")

    if not missing:
        return CheckResult(
            mnum, "PASS",
            f"{label} -- quality {cs.kind_text or cs.kind} intervals present in {_fmt_pcs(pcs)}",
            category="quality-ok",
        )
    else:
        return CheckResult(
            mnum, "WARN",
            f"{label} -- quality {cs.kind_text or cs.kind}: missing {', '.join(missing)} "
            f"in {_fmt_pcs(pcs)}",
            category="quality-missing-interval",
        )


def _check_roman_degree(
    mnum: str, cs: ChordSymbol, rn: RomanNumeral,
    key: KeyState, label: str
) -> CheckResult:
    """Check 3: Does the Roman numeral degree match the chord root in the stated key?"""
    scale_degs = key.scale_degrees
    if rn.degree < 0 or rn.degree >= len(scale_degs):
        return CheckResult(
            mnum, "WARN",
            f"{label} -- degree {rn.text} out of range for scale",
            category="degree-out-of-range",
        )

    expected_pc = (scale_degs[rn.degree] + rn.accidental) % 12
    actual_pc = cs.root_pc

    if actual_pc == expected_pc:
        return CheckResult(
            mnum, "PASS",
            f"{label} -- degree {rn.text} in {key.label}: "
            f"scale[{rn.degree}]={expected_pc}={pc_name(expected_pc)} = root {cs.root_name}({actual_pc})",
            category="degree-ok",
        )
    else:
        # Try to find which degree matches
        matching_deg = None
        for d, spc in enumerate(scale_degs):
            if spc == actual_pc:
                deg_names = ["I", "II", "III", "IV", "V", "VI", "VII"]
                matching_deg = deg_names[d]
                break

        hint = ""
        if matching_deg:
            hint = f". Expected degree {matching_deg} (scale[{scale_degs.index(actual_pc)}]={actual_pc}={pc_name(actual_pc)})"

        return CheckResult(
            mnum, "FAIL",
            f"{label} in {key.label} -- degree {rn.text}: "
            f"scale[{rn.degree}]={expected_pc}={pc_name(expected_pc)}... "
            f"root {cs.root_name}({actual_pc}) != {expected_pc}{hint}",
            category="degree-mismatch",
        )


def _check_non_diatonic(
    mnum: str, cs: ChordSymbol, rn: RomanNumeral,
    md: MeasureData, key: KeyState, label: str
) -> CheckResult:
    """Check 4: Non-diatonic marker consistency (measure-wide star)."""
    return _check_non_diatonic_per_chord(
        mnum, cs, rn, md.non_diatonic, key, label)


def _chord_quality_pcs(cs: ChordSymbol) -> Set[int]:
    """Return the set of pitch classes implied by the chord's quality intervals."""
    intervals = QUALITY_INTERVALS.get(cs.kind, [])
    return {(cs.root_pc + iv) % 12 for iv in intervals}


def _has_non_diatonic_quality(cs: ChordSymbol, scale_pcs: Set[int]) -> Tuple[bool, List[str]]:
    """Check if any quality-defining tones fall outside the scale.
    Returns (has_non_diatonic, list_of_non_diatonic_tone_names)."""
    non_diatonic: List[str] = []
    for iv in QUALITY_INTERVALS.get(cs.kind, []):
        tone_pc = (cs.root_pc + iv) % 12
        if tone_pc not in scale_pcs:
            non_diatonic.append(f"{pc_name(tone_pc)}({tone_pc})")
    return (len(non_diatonic) > 0, non_diatonic)


def _check_non_diatonic_per_chord(
    mnum: str, cs: ChordSymbol, rn: RomanNumeral,
    has_star: bool, key: KeyState, label: str
) -> CheckResult:
    """Check 4: Non-diatonic marker consistency (per-chord star).
    A chord is considered non-diatonic if its root OR any of its defining
    quality tones fall outside the current key's scale."""
    root_diatonic = cs.root_pc in key.scale_pcs
    quality_non_diatonic, nd_tones = _has_non_diatonic_quality(cs, key.scale_pcs)
    chord_is_diatonic = root_diatonic and not quality_non_diatonic

    if has_star:
        if not chord_is_diatonic:
            reason_parts = []
            if not root_diatonic:
                reason_parts.append(
                    f"root {cs.root_name}({cs.root_pc}) is non-diatonic")
            if quality_non_diatonic:
                reason_parts.append(
                    f"quality tones {', '.join(nd_tones)} are non-diatonic")
            return CheckResult(
                mnum, "PASS",
                f"{label} -- star present and {'; '.join(reason_parts)} "
                f"in {key.label} {_fmt_pcs(key.scale_pcs)}",
                category="non-diatonic-ok",
            )
        else:
            return CheckResult(
                mnum, "WARN",
                f"{label} -- star present but root and quality tones "
                f"are all diatonic to {key.label} {_fmt_pcs(key.scale_pcs)}",
                category="non-diatonic-all-diatonic",
            )
    else:
        if chord_is_diatonic:
            return CheckResult(
                mnum, "PASS",
                f"{label} -- no star and chord is fully diatonic to {key.label}",
                category="diatonic-ok",
            )
        else:
            reason_parts = []
            if not root_diatonic:
                reason_parts.append(
                    f"root {cs.root_name}({cs.root_pc}) is non-diatonic")
            if quality_non_diatonic:
                reason_parts.append(
                    f"quality tones {', '.join(nd_tones)} are non-diatonic")
            return CheckResult(
                mnum, "WARN",
                f"{label} -- no star but {'; '.join(reason_parts)} "
                f"in {key.label} {_fmt_pcs(key.scale_pcs)}",
                category="missing-star",
            )


def _check_cadence(
    md: MeasureData, rn: RomanNumeral,
    prev_md: MeasureData, key: KeyState, label: str
) -> CheckResult:
    """Check 5: Cadence pattern consistency."""
    cadence = md.cadence
    cur_degree = rn.degree
    prev_rns = prev_md.roman_numerals
    # Use the last Roman numeral of the previous measure (closest to the barline)
    prev_degree = prev_rns[-1].degree if prev_rns else None
    prev_kind = prev_rns[-1].kind if prev_rns else None

    if prev_degree is None:
        return CheckResult(
            md.number, "WARN",
            f"{label} -- {cadence} cadence: no previous Roman numeral to check",
            category="cadence-no-prev",
        )

    if cadence == "PAC":
        # Standard PAC: V->I.  Also accept viio->I (leading-tone resolution)
        # and dominant-function chords (V7, V9, etc.).
        dominant_prev = prev_degree == 4 or (prev_degree == 6 and prev_kind in (
            "diminished", "diminished-seventh", "half-diminished"))
        ok = dominant_prev and cur_degree == 0
        if ok:
            return CheckResult(
                md.number, "PASS",
                f"{label} -- PAC: {_degree_name(prev_degree)}->I confirmed "
                f"(prev degree {prev_degree}, cur degree {cur_degree})",
                category="cadence-ok",
            )
        else:
            return CheckResult(
                md.number, "FAIL",
                f"{label} -- PAC expected V->I (or viio->I) but got "
                f"degree {prev_degree}->degree {cur_degree} "
                f"({_degree_name(prev_degree)}->{_degree_name(cur_degree)})",
                category="cadence-mismatch",
            )

    elif cadence == "PC":
        # Plagal cadence: IV->I.  Also accept iv->I (minor plagal).
        ok = prev_degree == 3 and cur_degree == 0
        if ok:
            return CheckResult(
                md.number, "PASS",
                f"{label} -- PC: IV->I confirmed",
                category="cadence-ok",
            )
        else:
            return CheckResult(
                md.number, "FAIL",
                f"{label} -- PC expected IV->I but got "
                f"{_degree_name(prev_degree)}->{_degree_name(cur_degree)}",
                category="cadence-mismatch",
            )

    elif cadence == "DC":
        # Deceptive: previous should be V (degree 4), current should NOT be I.
        # Classic DC is V->vi, but V->IV, V->bVI etc. also count.
        ok = prev_degree == 4 and cur_degree != 0
        if ok:
            return CheckResult(
                md.number, "PASS",
                f"{label} -- DC: V->{_degree_name(cur_degree)} confirmed "
                f"(deceptive resolution to non-tonic)",
                category="cadence-ok",
            )
        else:
            detail_parts = []
            if prev_degree != 4:
                detail_parts.append(f"prev degree {prev_degree} != V")
            if cur_degree == 0:
                detail_parts.append("resolved to I (not deceptive)")
            return CheckResult(
                md.number, "FAIL",
                f"{label} -- DC expected V->non-I but: {', '.join(detail_parts)}",
                category="cadence-mismatch",
            )

    elif cadence == "HC":
        # Half cadence: current should be V (degree 4)
        ok = cur_degree == 4
        if ok:
            return CheckResult(
                md.number, "PASS",
                f"{label} -- HC: arrives on V confirmed",
                category="cadence-ok",
            )
        else:
            return CheckResult(
                md.number, "FAIL",
                f"{label} -- HC expected current degree V(4) but got {_degree_name(cur_degree)}({cur_degree})",
                category="cadence-mismatch",
            )

    return CheckResult(
        md.number, "WARN",
        f"{label} -- unknown cadence type '{cadence}'",
        category="cadence-unknown",
    )


def _minor_scale_variants(tonic_pc: int) -> Set[int]:
    """Return the union of natural, harmonic, and melodic minor pitch classes.

    Dominant chords borrowed from minor keys typically use the raised 7th
    (harmonic minor) or raised 6th+7th (melodic minor ascending).  Accepting
    the union avoids false positives on chords like V7 in harmonic minor.
    """
    natural  = get_scale_pcs(tonic_pc, "minor")
    # Harmonic minor: raise the 7th by one semitone
    raised_7 = (tonic_pc + 11) % 12
    # Melodic minor ascending: raise both 6th and 7th
    raised_6 = (tonic_pc + 9) % 12
    return natural | {raised_7, raised_6}


def _check_borrowed(
    mnum: str, cs: ChordSymbol, rn: Optional[RomanNumeral],
    borrowed_text: str, label: str
) -> CheckResult:
    """Check 6: Borrowed chord source consistency."""
    parsed = parse_borrowed_source(borrowed_text)
    if parsed is None:
        return CheckResult(
            mnum, "WARN",
            f"{label} -- could not parse borrowed source: '{borrowed_text}'",
            category="borrowed-parse-error",
        )

    src_tonic, src_mode = parsed
    src_label = f"{pc_name(src_tonic)} {src_mode}"

    # For minor source keys, accept natural + harmonic + melodic minor tones
    if src_mode in ("minor", "aeolian"):
        src_scale = _minor_scale_variants(src_tonic)
    else:
        src_scale = get_scale_pcs(src_tonic, src_mode)

    # Check that the root is diatonic to the source key
    root_in_source = cs.root_pc in src_scale
    if not root_in_source:
        return CheckResult(
            mnum, "FAIL",
            f"{label} -- star \"{borrowed_text}\": root {cs.root_name}({cs.root_pc}) "
            f"is NOT diatonic to {src_label} {_fmt_pcs(src_scale)}",
            category="borrowed-root-not-in-source",
        )

    # Also check that the defining quality intervals are diatonic to source
    expected_intervals = QUALITY_INTERVALS.get(cs.kind)
    if expected_intervals:
        non_diatonic_tones = []
        for interval in expected_intervals:
            tone_pc = (cs.root_pc + interval) % 12
            if tone_pc not in src_scale:
                non_diatonic_tones.append(f"{pc_name(tone_pc)}({tone_pc})")

        if non_diatonic_tones:
            # WARN instead of FAIL: MusicXML's <kind> may not match the
            # analyzer's internal quality (e.g. "F7susb5" exports as
            # kind="dominant", losing the "sus").  The C++ borrowed-chord
            # search validates against the actual internal quality tones,
            # which may differ from the MusicXML quality intervals.
            return CheckResult(
                mnum, "WARN",
                f"{label} -- \"{borrowed_text}\": root {cs.root_name}({cs.root_pc}) is in "
                f"{src_label}, but quality tones {', '.join(non_diatonic_tones)} "
                f"are NOT diatonic to {src_label} {_fmt_pcs(src_scale)}. "
                f"Chord not fully diatonic to claimed source.",
                category="borrowed-quality-not-in-source",
            )

    return CheckResult(
        mnum, "PASS",
        f"{label} -- \"{borrowed_text}\": root and quality tones are diatonic to {src_label}",
        category="borrowed-ok",
    )


def _fmt_pcs(pcs: Set[int]) -> str:
    """Format a set of pitch classes for display."""
    return "{" + ",".join(str(p) for p in sorted(pcs)) + "}"


def _degree_name(degree: int) -> str:
    names = ["I", "II", "III", "IV", "V", "VI", "VII"]
    if 0 <= degree < len(names):
        return names[degree]
    return f"?({degree})"


# ---------------------------------------------------------------------------
# Top-level verification
# ---------------------------------------------------------------------------

def verify_file(filepath: Path) -> Tuple[List[CheckResult], dict]:
    """
    Verify a single MusicXML file.  Returns (results, metadata).
    """
    if filepath.suffix.lower() == ".mxl":
        # Compressed MusicXML: extract the .xml/.musicxml from the ZIP
        with zipfile.ZipFile(filepath, "r") as zf:
            xml_names = [n for n in zf.namelist()
                         if n.endswith((".xml", ".musicxml"))
                         and not n.startswith("META-INF")]
            if not xml_names:
                print(f"  [SKIP] No XML file found inside {filepath.name}")
                return [], {}
            with zf.open(xml_names[0]) as xml_file:
                tree = ET.parse(xml_file)
    else:
        tree = ET.parse(filepath)
    root = tree.getroot()

    source_parts, chord_track = find_parts(root)
    if chord_track is None:
        print(f"  [SKIP] No chord track part found (no part-name containing 'Chord').")
        return [], {}

    source_ids = [pid for pid, _ in source_parts]
    source_names = [name for _, name in source_parts]

    # Extract sounding pitch classes from source parts
    sounding_pcs = extract_sounding_pcs(root, source_ids)

    # Extract key signatures from any source part (they should be consistent)
    key_sigs: Dict[str, int] = {}
    for pid in source_ids:
        key_sigs = extract_key_sigs(root, pid)
        if key_sigs:
            break
    if not key_sigs:
        # Try chord track
        key_sigs = extract_key_sigs(root, chord_track[0])

    initial_fifths = key_sigs.get("1", 0)

    # Extract chord track data
    measures = extract_chord_track_data(root, chord_track[0])

    # Run checks
    results = run_checks(measures, sounding_pcs, initial_fifths)

    meta = {
        "source_parts": ", ".join(source_names),
        "chord_track": chord_track[1],
        "key_sig_fifths": initial_fifths,
        "key_sig_name": _fifths_to_name(initial_fifths),
        "num_measures": len(measures),
    }

    return results, meta


def _fifths_to_name(fifths: int) -> str:
    """Human-readable key name from fifths."""
    major_keys = {
        -7: "Cb", -6: "Gb", -5: "Db", -4: "Ab", -3: "Eb", -2: "Bb", -1: "F",
        0: "C", 1: "G", 2: "D", 3: "A", 4: "E", 5: "B", 6: "F#", 7: "C#",
    }
    name = major_keys.get(fifths, f"({fifths})")
    return f"{name} major"


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_results(
    filepath: Path, results: List[CheckResult], meta: dict,
    verbose: bool = False
) -> dict:
    """Print results for a file and return summary counts."""
    print(f"\n{'=' * 60}")
    print(f"=== Verifying: {filepath.name} ===")
    print(f"{'=' * 60}")

    if not meta:
        return {"pass": 0, "warn": 0, "fail": 0}

    print(f"Parts: {meta['source_parts']} | Chord track: {meta['chord_track']}")
    print(f"Key signature: {meta['key_sig_fifths']} ({meta['key_sig_name']})")
    print(f"Measures: {meta['num_measures']}")
    print()

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    categories: Dict[str, int] = {}

    if not results:
        print("  (no checks to perform -- no chord symbols found)")
        return {"pass": 0, "warn": 0, "fail": 0}

    print("--- Consistency checks ---")
    for r in results:
        counts[r.level] = counts.get(r.level, 0) + 1
        if r.level in ("WARN", "FAIL"):
            categories[r.category] = categories.get(r.category, 0) + 1

        if verbose:
            print(f"[{r.level}] M{r.measure}: {r.message}")
        elif r.level != "PASS":
            print(f"[{r.level}] M{r.measure}: {r.message}")

    # Print a compact pass summary when not verbose
    if not verbose and counts["PASS"] > 0:
        print(f"\n[PASS] {counts['PASS']} checks passed (not shown individually; use -v to see)")

    return {
        "pass": counts["PASS"],
        "warn": counts["WARN"],
        "fail": counts["FAIL"],
        "categories": categories,
    }


def print_summary(
    files_checked: int,
    total_pass: int, total_warn: int, total_fail: int,
    all_categories: Dict[str, int]
) -> None:
    """Print the final summary across all files."""
    total = total_pass + total_warn + total_fail
    print(f"\n{'=' * 60}")
    print(f"=== Summary ===")
    print(f"{'=' * 60}")
    print(f"Files checked: {files_checked}")
    print(f"Total checks: {total}")
    if total > 0:
        print(f"PASS: {total_pass} ({100 * total_pass // total}%)")
        print(f"WARN: {total_warn} ({100 * total_warn // total}%)")
        print(f"FAIL: {total_fail} ({100 * total_fail // total}%)")
    else:
        print("PASS: 0\nWARN: 0\nFAIL: 0")

    if all_categories:
        print(f"\nTop issues:")
        sorted_cats = sorted(all_categories.items(), key=lambda x: -x[1])
        for cat, count in sorted_cats[:15]:
            # Make category names more readable
            display = cat.replace("-", " ").replace("_", " ")
            print(f"  - {display}: {count} occurrences")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]
    verbose = False
    positional: List[str] = []

    for arg in args:
        if arg in ("-v", "--verbose"):
            verbose = True
        elif arg in ("-h", "--help"):
            print("Usage: python verify_chord_track.py [-v|--verbose] [directory_or_file]")
            print()
            print("Verify chord track annotations in MusicXML files.")
            print()
            print("Options:")
            print("  -v, --verbose  Show all check results, including PASS")
            print("  -h, --help     Show this help message")
            print()
            print("If no path is given, processes all *.musicxml and *.mxl files in the")
            print("script's own directory.")
            sys.exit(0)
        else:
            positional.append(arg)

    targets = [Path(p) for p in positional] if positional else [Path(__file__).parent]

    files: List[Path] = []
    for target in targets:
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            files.extend(
                sorted(list(target.glob("*.musicxml")) + list(target.glob("*.mxl")))
            )
        else:
            print(f"Error: '{target}' is not a file or directory.", file=sys.stderr)
            sys.exit(1)

    if not files:
        print(f"No .musicxml/.mxl files found in {[str(t) for t in targets]}.")
        sys.exit(0)

    total_pass = 0
    total_warn = 0
    total_fail = 0
    all_categories: Dict[str, int] = {}
    files_checked = 0

    for f in files:
        try:
            results, meta = verify_file(f)
        except ET.ParseError as e:
            print(f"\n[ERROR] Failed to parse {f.name}: {e}")
            continue

        summary = print_results(f, results, meta, verbose=verbose)
        total_pass += summary.get("pass", 0)
        total_warn += summary.get("warn", 0)
        total_fail += summary.get("fail", 0)

        for cat, count in summary.get("categories", {}).items():
            all_categories[cat] = all_categories.get(cat, 0) + count

        files_checked += 1

    print_summary(files_checked, total_pass, total_warn, total_fail, all_categories)

    # Exit code: 0 if no FAILs, 1 if any FAILs
    sys.exit(1 if total_fail > 0 else 0)


if __name__ == "__main__":
    main()
