#!/usr/bin/env python3
"""
dcml_parser.py — Parses harmonic annotation files in two formats:

1. DCML TSV format (ABC Beethoven corpus):
   TSV with columns mc, beat, globalkey, localkey, chord, numeral.

2. rntxt format (When in Rome corpus):
   Plain-text Roman numeral annotations with inline key changes.
   Example line: "m3 IV b2.5 viio6 b3 I"

Usage:
    from dcml_parser import parse_dcml_file, parse_rntxt_file, find_wir_file
    regions = parse_dcml_file("path/to/bwv66.6.tsv")       # DCML TSV
    regions = parse_rntxt_file("path/to/analysis.txt")     # When in Rome rntxt
"""

import csv
import os
import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DcmlRegion:
    measure_number: int
    beat: float
    global_key: str
    local_key: str
    chord_symbol: str       # raw DCML chord string (e.g. "V65")
    roman_numeral: str      # extracted numeral (e.g. "V")
    root_pc: Optional[int]  # computed from numeral + local key, or None


def parse_dcml_file(path: str) -> List[DcmlRegion]:
    """
    Parse a DCML TSV annotation file.
    Returns list of DcmlRegion sorted by measure + beat.
    Skips rows with missing or unparseable numeral fields.
    """
    regions = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            try:
                mc   = int(row.get('mc', 0))
                beat = float(row.get('beat', 1.0))
                globalkey = row.get('globalkey', '')
                localkey  = row.get('localkey', '')
                relativeroot = row.get('relativeroot', '')
                chord     = row.get('chord', '')
                numeral   = row.get('numeral', '')

                if not numeral or numeral in ('.', '~', '@none'):
                    continue  # rest or unparseable

                effective_key = _resolve_effective_dcml_key(localkey, globalkey, relativeroot)
                regions.append(DcmlRegion(
                    measure_number=mc,
                    beat=beat,
                    global_key=globalkey,
                    local_key=localkey,
                    chord_symbol=chord,
                    roman_numeral=numeral,
                    root_pc=_compute_root_pc(numeral, effective_key),
                ))
            except (ValueError, KeyError):
                continue  # skip malformed rows

    regions.sort(key=lambda r: (r.measure_number, r.beat))
    return regions


# Scale degree semitones from tonic for major and minor
_DEGREE_SEMITONES_MAJOR = [0, 2, 4, 5, 7, 9, 11]  # I II III IV V VI VII
_DEGREE_SEMITONES_MINOR = [0, 2, 3, 5, 7, 8, 10]  # i ii bIII iv v bVI bVII

_DEGREE_MAP = {
    'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6,
}

_NOTE_TO_PC = {
    'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11,
}


def _key_to_tonic_pc(key: str) -> int:
    """Convert DCML key string (e.g. 'C', 'f#', 'Bb') to tonic pitch class."""
    if not key:
        return 0
    base = key[0].upper()
    pc = _NOTE_TO_PC.get(base, 0)
    suffix = key[1:].lower()
    pc = (pc + suffix.count('#') - suffix.count('b')) % 12
    return pc


def _compute_root_pc(numeral: str, key: str) -> Optional[int]:
    """
    Compute root pitch class from a DCML Roman numeral and key string.
    Returns None if the numeral cannot be parsed.
    DCML key: uppercase = major (e.g. 'G'), lowercase = minor (e.g. 'g').
    """
    try:
        tonic_pc  = _key_to_tonic_pc(key)
        is_minor  = key[0].islower() if key else False
        semitones = (_DEGREE_SEMITONES_MINOR if is_minor
                     else _DEGREE_SEMITONES_MAJOR)

        # Strip prefix modifier (b or #)
        n = numeral.lstrip()
        prefix = ''
        if n.startswith('b'):
            prefix = 'b'; n = n[1:]
        elif n.startswith('#'):
            prefix = '#'; n = n[1:]

        # Strip quality/inversion suffixes to isolate degree
        degree_str = re.match(r'^(VII|VI|IV|V|III|II|I)', n.upper())
        if not degree_str:
            return None

        degree_idx = _DEGREE_MAP[degree_str.group(1)]
        root_pc = (tonic_pc + semitones[degree_idx]) % 12
        if prefix == 'b':
            root_pc = (root_pc - 1) % 12
        elif prefix == '#':
            root_pc = (root_pc + 1) % 12

        return root_pc
    except Exception:
        return None


def parse_abc_harmonies_file(path: str) -> List[DcmlRegion]:
    """
    Parse an ABC Beethoven corpus .harmonies.tsv file.

    The ABC TSV uses column 'mn' (measure number) and 'mn_onset' (quarter-beat
    offset within the measure, 0-indexed) rather than the 'beat' column used by
    some other DCML variants.  beat = mn_onset + 1.0 (1-indexed quarter beats).

    The 'numeral' column contains the Roman numeral (e.g. 'I', 'V', 'IV').
    The 'localkey' column contains the local key (e.g. 'I' = same as global, or
    'vi' = relative minor).  'globalkey' gives the piece key (e.g. 'F', 'g').

    DCML localkey is relative when it looks like a Roman numeral (e.g. 'I', 'IV').
    We resolve it to an absolute key before computing root_pc.
    """
    regions = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            try:
                mn       = int(row.get('mn', row.get('mc', 0)))
                mn_onset = float(row.get('mn_onset', 0.0))
                beat     = mn_onset + 1.0  # convert to 1-indexed beat
                globalkey = row.get('globalkey', '')
                localkey  = row.get('localkey', '')
                relativeroot = row.get('relativeroot', '')
                chord     = row.get('chord', '')
                numeral   = row.get('numeral', '')

                if not numeral or numeral in ('.', '~', '@none'):
                    continue

                effective_key = _resolve_effective_dcml_key(localkey, globalkey, relativeroot)
                regions.append(DcmlRegion(
                    measure_number=mn,
                    beat=beat,
                    global_key=globalkey,
                    local_key=localkey,
                    chord_symbol=chord,
                    roman_numeral=numeral,
                    root_pc=_compute_root_pc(numeral, effective_key),
                ))
            except (ValueError, KeyError):
                continue

    regions.sort(key=lambda r: (r.measure_number, r.beat))
    return regions


def _resolve_dcml_key(localkey: str, globalkey: str) -> str:
    """
    Resolve a DCML local key string to an absolute key string suitable for
    _compute_root_pc().

    DCML localkey is either:
    - An absolute key (e.g. 'F', 'g', 'Bb') — used directly.
    - A relative Roman numeral (e.g. 'I', 'IV', 'vi') — the tonic of the local
      key is computed as the corresponding scale degree of the globalkey.

    Returns a key string like 'C', 'g', 'f#' etc.
    If resolution fails, falls back to globalkey.
    """
    if not localkey:
        return globalkey

    # If localkey looks like an absolute key (starts with A-G or a-g followed
    # by optional #/b), use it directly.
    if re.match(r'^[A-Ga-g][#b]?$', localkey):
        return localkey

    # Otherwise treat it as a Roman numeral relative to globalkey.
    try:
        global_tonic = _key_to_tonic_pc(globalkey)
        global_minor = globalkey[0].islower() if globalkey else False
        semitones = _DEGREE_SEMITONES_MINOR if global_minor else _DEGREE_SEMITONES_MAJOR

        n = localkey.lstrip()
        prefix = ''
        if n.startswith('b'):
            prefix = 'b'; n = n[1:]
        elif n.startswith('#'):
            prefix = '#'; n = n[1:]

        local_minor = n[0].islower()
        degree_match = re.match(r'^(VII|VI|IV|V|III|II|I)', n.upper())
        if not degree_match:
            return globalkey

        degree_idx = _DEGREE_MAP[degree_match.group(1)]
        local_tonic_pc = (global_tonic + semitones[degree_idx]) % 12
        if prefix == 'b':
            local_tonic_pc = (local_tonic_pc - 1) % 12
        elif prefix == '#':
            local_tonic_pc = (local_tonic_pc + 1) % 12

        # Convert pitch class back to a note name
        _PC_TO_NOTE = {0:'C', 1:'C#', 2:'D', 3:'Eb', 4:'E', 5:'F',
                       6:'F#', 7:'G', 8:'Ab', 9:'A', 10:'Bb', 11:'B'}
        note = _PC_TO_NOTE.get(local_tonic_pc, 'C')
        return note.lower() if local_minor else note
    except Exception:
        return globalkey


def _resolve_effective_dcml_key(localkey: str, globalkey: str, relativeroot: str = '') -> str:
    """
    Resolve the effective tonic for a DCML row before applying the row's numeral.

    Resolution order:
      1. Resolve localkey against the global key.
      2. If relativeroot is present (e.g. V/III, ii65/v), resolve that tonicized
         area against the already-resolved local key.

    This preserves plain rows while giving applied/secondary functions their
    correct absolute root pitch classes.
    """
    effective_key = _resolve_dcml_key(localkey, globalkey)

    if relativeroot and relativeroot not in ('.', '@none'):
        effective_key = _resolve_dcml_key(relativeroot, effective_key)

    return effective_key


def find_dcml_file(dcml_dir: str, bwv_stem: str) -> Optional[str]:
    """
    Find the DCML TSV file for a given BWV stem (e.g. 'bwv66.6').
    Tries common DCML filename patterns.
    Returns full path or None if not found.
    """
    bwv_match = re.search(r'bwv(\d+)(?:\.(\d+))?', bwv_stem, re.IGNORECASE)
    if not bwv_match:
        return None

    bwv_num = bwv_match.group(1)
    bwv_sub = bwv_match.group(2)  # may be None for standalone chorales

    # Build candidate suffixes: plain and zero-padded
    plain   = 'bwv' + bwv_num
    padded3 = 'bwv' + bwv_num.zfill(3)
    padded4 = 'bwv' + bwv_num.zfill(4)

    try:
        entries = os.listdir(dcml_dir)
    except OSError:
        return None

    for fname in entries:
        if not fname.endswith('.tsv'):
            continue
        f_lower = fname.lower()
        if plain in f_lower or f_lower.startswith(padded3) or f_lower.startswith(padded4):
            # If the stem includes a movement number, require it to appear in the filename too
            if bwv_sub and bwv_sub not in fname:
                continue
            return os.path.join(dcml_dir, fname)

    return None


# ══════════════════════════════════════════════════════════════════════════
# rntxt format parser (When in Rome corpus)
# ══════════════════════════════════════════════════════════════════════════

# Matches a key-change token like "G:", "d:", "f#:", "Bb:"
_KEY_TOKEN = re.compile(r'^[A-Ga-g][b#]?:$')

# Matches a beat-position token like "b1", "b2.5", "b3.75"
_BEAT_TOKEN = re.compile(r'^b(\d+(?:\.\d+)?)$')

# Matches the start of a Roman numeral (optionally preceded by b or # alteration)
_NUMERAL_TOKEN = re.compile(
    r'^[b#]?(?:VII|VI|IV|V|III|II|I|vii|vi|iv|v|iii|ii|i)',
    re.IGNORECASE
)

# Tokens to silently skip
_SKIP_TOKENS = {'||', ':||', '|', '|:', '||:', 'Cad.', 'Cad'}


def parse_rntxt_file(path: str) -> List[DcmlRegion]:
    """
    Parse a When-in-Rome rntxt annotation file.
    Returns list of DcmlRegion sorted by measure + beat.

    rntxt format (per measure line):
        m{N} [b{beat}] [Key:] Numeral [b{beat}] [Key:] Numeral ...
    Variant lines (m{N}var{K}) and Note: lines are skipped.
    Key changes are tracked; the current key applies to all subsequent chords.
    """
    global_key = 'C'
    current_key = global_key
    regions: List[DcmlRegion] = []
    header_done = False

    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    for raw_line in lines:
        line = raw_line.strip()

        if not header_done:
            if line.startswith('m') and not line.startswith('Note:'):
                header_done = True
            else:
                continue

        if not line.startswith('m'):
            continue

        # Skip variant lines (mNvarK)
        measure_match = re.match(r'^m(\d+)(var\d+)?\s', line)
        if not measure_match:
            continue
        if measure_match.group(2):
            continue

        measure_number = int(measure_match.group(1))
        tokens = line.split()[1:]

        current_beat = 1.0
        # Accumulate the last chord at each (measure, beat) — handles key changes mid-beat.
        beat_chords: dict[float, tuple[str, str]] = {}

        i = 0
        while i < len(tokens):
            tok = tokens[i]
            i += 1

            if tok in _SKIP_TOKENS:
                continue

            beat_m = _BEAT_TOKEN.match(tok)
            if beat_m:
                current_beat = float(beat_m.group(1))
                continue

            if _KEY_TOKEN.match(tok):
                current_key = tok[:-1]
                # Update global_key from first key seen (approximate)
                if global_key == 'C' and not regions:
                    global_key = current_key
                continue

            if _NUMERAL_TOKEN.match(tok):
                beat_chords[current_beat] = (current_key, tok)
                continue

        for beat, (key, numeral) in sorted(beat_chords.items()):
            # For secondary dominants (V/V, vii/o7/V), use the primary numeral only.
            primary = numeral.split('/')[0] if '/' in numeral else numeral
            root_pc = _compute_root_pc(primary, key)
            regions.append(DcmlRegion(
                measure_number=measure_number,
                beat=beat,
                global_key=global_key,
                local_key=key,
                chord_symbol=numeral,
                roman_numeral=primary,
                root_pc=root_pc,
            ))

    regions.sort(key=lambda r: (r.measure_number, r.beat))
    return regions


# ══════════════════════════════════════════════════════════════════════════
# When in Rome file lookup
# ══════════════════════════════════════════════════════════════════════════

# Cache: wir_base_dir → {bwv_stem: analysis_txt_path}
_WIR_CACHE: dict[str, dict[str, str]] = {}


def _build_wir_index(wir_base: str) -> dict[str, str]:
    """
    Scan the When-in-Rome Chorales directory and build a bwv_stem → analysis.txt
    path mapping by reading each remote.json for its music21 corpus path.
    """
    import json as _json

    chorales_dir = os.path.join(wir_base, "Corpus", "Early_Choral",
                                "Bach,_Johann_Sebastian", "Chorales")
    index: dict[str, str] = {}

    try:
        folders = os.listdir(chorales_dir)
    except OSError:
        return index

    for folder in folders:
        rjson_path = os.path.join(chorales_dir, folder, "remote.json")
        txt_path   = os.path.join(chorales_dir, folder, "analysis.txt")
        if not os.path.exists(rjson_path) or not os.path.exists(txt_path):
            continue
        try:
            with open(rjson_path, encoding='utf-8') as f:
                data = _json.load(f)
            for m21path in data.get("music21", []):
                stem = re.sub(r'\.mxl$', '', m21path.split('/')[-1])
                index[stem] = txt_path
        except Exception:
            continue

    return index


def find_wir_file(wir_base: str, bwv_stem: str) -> Optional[str]:
    """
    Find the When-in-Rome analysis.txt for a given BWV stem (e.g. 'bwv66.6').
    wir_base: root of the cloned When-in-Rome repository.
    Returns full path to analysis.txt or None if not found.
    """
    if wir_base not in _WIR_CACHE:
        _WIR_CACHE[wir_base] = _build_wir_index(wir_base)
    return _WIR_CACHE[wir_base].get(bwv_stem)
