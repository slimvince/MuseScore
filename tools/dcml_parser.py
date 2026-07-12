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
import json
import os
import re
import sys
from dataclasses import dataclass, field, replace
from fractions import Fraction
from typing import List, Optional


# Ticks per quarter note.  batch_analyze defines region durations as ticks/480,
# so the GT absolute tick from a quarter-position is quarterbeats * 480 (audit
# L4.1: exact, pickup-aware, verified tick-for-tick on 18 pieces / 3 corpora).
TICKS_PER_QUARTER = 480


@dataclass
class DcmlRegion:
    measure_number: int
    beat: float
    global_key: str
    local_key: str
    chord_symbol: str       # raw DCML chord string (e.g. "V65")
    roman_numeral: str      # extracted numeral (e.g. "V")
    root_pc: Optional[int]  # computed from numeral + local key, or None
    # Absolute tick of the annotation onset, derived from the DCML
    # `quarterbeats` column (round(Fraction(quarterbeats) * 480)).  Present on
    # the TSV path (parse_abc_harmonies_file); None on the rntxt path (When in
    # Rome has no absolute-quarter column — it stays on measure-anchored
    # reconstruction).  When present, the comparator aligns by this exact tick
    # instead of rebuilding ticks from measure_number+beat (audit P0/L4.1).
    abs_tick: Optional[int] = None
    # ── L6 oracle columns (additive; TSV path only) ──────────────────────────
    # The DCML `cadence` and `phraseend` GT columns, carried verbatim when the
    # row bears one (else None).  These are the Layer-6 punctuation-span /
    # cadence-location oracles (design §10); they do NOT participate in the RN /
    # root / key read surface — purely additive, so the BIR gate is byte-identical.
    # NOTE: a cadence/phraseend marker may sit on a REST row (empty numeral) that
    # this region stream skips (10.7% of phraseend, 1.1% of cadence markers across
    # the dev beds).  For a COMPLETE marker-tick set independent of the numeral,
    # use parse_cadence_phrase_markers(); these region fields only carry the marker
    # of a region that also bears a scoreable numeral.
    cadence: Optional[str] = None
    phraseend: Optional[str] = None
    # ── L4 / pedal evidence columns (additive; TSV path only) ────────────────
    # The DLC `figbass` and `pedal` GT columns, carried verbatim when the row
    # bears one (else None).  `figbass` = the inversion figured-bass digits
    # (e.g. "6", "64", "7", "65", "43", "2") — the notated-inversion / N10
    # evidence channel.  `pedal` = the pedal-point column (the sustained scale
    # degree beneath the harmony) — the N20 pedal-point-span GT.  Like
    # cadence/phraseend these do NOT participate in the RN / root / key read
    # surface — purely additive, so the BIR gate is byte-identical.  Present on
    # the TSV path (parse_abc_harmonies_file); None on the rntxt path (When in
    # Rome has no figured-bass / pedal columns).  Exposed at the Wave-3 addendum
    # (cc_wave3_addendum_report.md); no consumer reads them yet.
    figbass: Optional[str] = None
    pedal: Optional[str] = None


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

# Canonical pc -> note-name (uppercase = the major spelling). Single-sourced here and
# reused by _resolve_dcml_key and the OI-142 transposition helper (#6). Grading uses only
# tonic pc + major/minor case, so any enharmonic spelling of a pc is faithful.
_PC_TO_NOTE = {0: 'C', 1: 'C#', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F',
               6: 'F#', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'}


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

        degree_token = degree_str.group(1)
        degree_idx = _DEGREE_MAP[degree_token]
        root_pc = (tonic_pc + semitones[degree_idx]) % 12

        # Minor-key raised submediant / leading tone (audit P2).  DCML and
        # music21 root a lowercase vi / vii in a minor key a semitone ABOVE the
        # natural-minor scale degree: vi -> raised submediant (+9 over tonic),
        # vii -> leading tone (+11), matching harmonic-minor practice.  An
        # uppercase VI / VII is the natural submediant (bVI, +8) / subtonic
        # (bVII, +10).  Case is the disambiguator (verified against music21
        # roman.RomanNumeral, 0/CC oracle).  Degrees I..V are unaffected by case
        # (v and V both root at +7).  The explicit b/# prefix is then applied on
        # top of the cased value (so #vio -> +10, #viio -> +0, matching music21).
        if is_minor and degree_idx in (5, 6):
            # n has had its b/# prefix stripped above; check the degree's case
            # in the original (un-uppercased) token.
            if n[:len(degree_token)].islower():
                root_pc = (root_pc + 1) % 12

        if prefix == 'b':
            root_pc = (root_pc - 1) % 12
        elif prefix == '#':
            root_pc = (root_pc + 1) % 12

        return root_pc
    except Exception:
        return None


def _parse_fraction(value: str, default: Fraction = Fraction(0)) -> Fraction:
    """Parse a DCML numeric cell as an exact Fraction.

    DCML TSV numeric columns (mn_onset, quarterbeats, duration_qb, …) hold
    *whole-note-fraction strings* like "1/2", "3/8", "7/16", "9/2", "0".
    ``float("1/2")`` raises ValueError — the bug (audit P0) that silently
    dropped 58.9% of all annotations via a bare ``except: continue``.
    ``Fraction("1/2")`` parses them exactly; ``Fraction("0")`` and integer
    strings parse too.  Empty cells return the default.
    """
    s = (value or '').strip()
    if not s:
        return default
    return Fraction(s)


def parse_abc_harmonies_file(
        path: str,
        abs_onset_col: str = 'quarterbeats_all_endings',
        skipped: Optional[list] = None,
) -> List[DcmlRegion]:
    """
    Parse an ABC / DCML .harmonies.tsv file (used by ALL TSV corpora — corelli,
    mozart, chopin, beethoven, grieg, schumann, dvorak, tchaikovsky, cpe_bach,
    bach_suites).

    The TSV uses column 'mn' (measure number) and 'mn_onset' (quarter-beat
    offset within the measure, 0-indexed) — both stored as *whole-note-fraction
    strings* (e.g. "1/4").  ``beat = float(mn_onset) + 1.0`` (1-indexed quarter
    beats).  Per audit P0, these are parsed with :class:`fractions.Fraction`,
    NOT ``float`` — ``float("1/4")`` raised ``ValueError`` and a bare
    ``except: continue`` discarded every off-downbeat annotation (58.9% of GT).

    Absolute alignment (audit L4.1): each region carries ``abs_tick =
    round(Fraction(<abs_onset_col>) * 480)`` so the comparator aligns by exact
    tick instead of the measure-anchor reconstruction (which only ever saw the
    surviving downbeats and ballooned each span to a whole measure).

    ``abs_onset_col`` defaults to ``'quarterbeats_all_endings'`` — the absolute
    quarter position counting EVERY written ending once, which matches our
    repeat-unexpanded reading (no ``expandRepeats`` anywhere in the pipeline).
    This resolves audit P4 universally and as a real fix, not a quarantine: on
    repeat-bearing movements plain ``quarterbeats`` runs ~bars ahead (it elides
    first-ending material), and using it made Beethoven align ~12pp worse; the
    all-endings column recovers every one of the 29 repeat-bearing Beethoven
    movements (and chopin/mozart/schumann/grieg/bach_suites repeats) while being
    BYTE-IDENTICAL on movements without repeats (where the two columns are
    equal).  If the chosen column is empty for a row, the other quarterbeats
    column is used as a fallback so a sparsely-populated column never silently
    drops abs_tick.

    The 'numeral' column contains the Roman numeral (e.g. 'I', 'V', 'IV'); the
    'localkey' column contains the local key (absolute, or a Roman numeral
    relative to globalkey, resolved before computing root_pc).

    ``skipped``: if a list is supplied, each unparseable/empty-numeral row that
    is NOT a deliberate rest is appended as ``(row_index, reason)`` so no row is
    silently discarded (audit P0: narrow the bare except).  Rows that are
    legitimate rests ('.', '~', '@none', empty numeral) are NOT recorded as
    skips — they carry no harmony to score.
    """
    regions = []
    local_skips: list = []
    other_col = ('quarterbeats_all_endings'
                 if abs_onset_col == 'quarterbeats' else 'quarterbeats')
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for idx, row in enumerate(reader):
            numeral = row.get('numeral', '')
            if not numeral or numeral in ('.', '~', '@none'):
                continue  # deliberate rest / unannotated — not a drop
            try:
                mn = int(row.get('mn', row.get('mc', 0)))
                mn_onset = _parse_fraction(row.get('mn_onset', '0'))
                beat = float(mn_onset) + 1.0  # 1-indexed quarter beat
                globalkey = row.get('globalkey', '')
                localkey = row.get('localkey', '')
                relativeroot = row.get('relativeroot', '')
                chord = row.get('chord', '')

                qb_raw = row.get(abs_onset_col, '') or row.get(other_col, '')
                abs_tick: Optional[int] = None
                if (qb_raw or '').strip():
                    abs_tick = round(_parse_fraction(qb_raw) * TICKS_PER_QUARTER)

                # L6 oracle columns (additive) — carried verbatim, None when empty.
                cadence = (row.get('cadence') or '').strip() or None
                phraseend = (row.get('phraseend') or '').strip() or None
                # figbass (N10 inversion figured-bass) + pedal (N20 pedal-point) —
                # additive, carried verbatim, None when empty.  No consumer reads
                # them yet (Wave-3 addendum exposure); the RN read surface is unchanged.
                figbass = (row.get('figbass') or '').strip() or None
                pedal = (row.get('pedal') or '').strip() or None

                effective_key = _resolve_effective_dcml_key(localkey, globalkey, relativeroot)
                regions.append(DcmlRegion(
                    measure_number=mn,
                    beat=beat,
                    global_key=globalkey,
                    local_key=localkey,
                    chord_symbol=chord,
                    roman_numeral=numeral,
                    root_pc=_compute_root_pc(numeral, effective_key),
                    abs_tick=abs_tick,
                    cadence=cadence,
                    phraseend=phraseend,
                    figbass=figbass,
                    pedal=pedal,
                ))
            except (ValueError, KeyError, ZeroDivisionError) as exc:
                # A genuinely malformed harmony row.  Record it — do NOT let it
                # vanish into a bare `continue` (the P0 failure mode).
                local_skips.append((idx, f"{type(exc).__name__}: {exc}"))
                continue

    if skipped is not None:
        skipped.extend(local_skips)
    elif local_skips:
        # No collector supplied — surface the count so a silent drop can't recur.
        print(f"[dcml_parser] {os.path.basename(path)}: skipped "
              f"{len(local_skips)} malformed harmony row(s): "
              f"{local_skips[:3]}{' …' if len(local_skips) > 3 else ''}",
              file=sys.stderr)

    regions.sort(key=lambda r: (r.measure_number, r.beat))
    return regions


@dataclass
class DcmlMarker:
    """A single L6-oracle marker (a `cadence` or `phraseend` cell) from a DCML
    .harmonies.tsv row, carried with its absolute tick.  Unlike a DcmlRegion this
    is emitted for EVERY row bearing the column — including rest rows (empty
    numeral) that the region stream skips — so the marker-tick set is complete."""
    abs_tick: Optional[int]   # round(Fraction(<quarterbeats col>) * 480), or None
    label: str                # verbatim cell value (e.g. "PAC", "HC.SIM", "}{")
    measure_number: int
    beat: float
    kind: str                 # 'cadence' or 'phraseend'


def parse_cadence_phrase_markers(
        path: str,
        abs_onset_col: str = 'quarterbeats_all_endings',
) -> "tuple[List[DcmlMarker], List[DcmlMarker]]":
    """Extract the DCML `cadence` and `phraseend` GT markers from a
    .harmonies.tsv, INDEPENDENT of the `numeral` column.

    Returns ``(cadence_markers, phraseend_markers)``, each sorted by abs_tick.

    Why a dedicated reader (not just the DcmlRegion fields): a marker may sit on a
    REST row (deliberate rest / unannotated harmony — empty numeral) that
    :func:`parse_abc_harmonies_file` skips.  Measured across the L6 dev beds, that
    is **10.7% of phraseend markers** and **1.1% of cadence markers** — dropping
    them would corrupt the punctuation-span-boundary GT set.  This reader visits
    every row and keeps every non-empty cell, so the oracle tick set is complete.

    Tick derivation reuses the EXACT arithmetic of the RN read surface
    (``round(Fraction(<abs_onset_col>) * TICKS_PER_QUARTER)`` with the same
    all-endings / plain-quarterbeats fallback), so marker ticks and region ticks
    live on one tick basis.  ``abs_tick`` is None only when both quarterbeats
    columns are empty for the row.
    """
    cadence_markers: List[DcmlMarker] = []
    phrase_markers: List[DcmlMarker] = []
    other_col = ('quarterbeats_all_endings'
                 if abs_onset_col == 'quarterbeats' else 'quarterbeats')
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            cad = (row.get('cadence') or '').strip()
            phr = (row.get('phraseend') or '').strip()
            if not cad and not phr:
                continue
            try:
                mn = int(row.get('mn', row.get('mc', 0)))
            except (ValueError, TypeError):
                mn = 0
            mn_onset = _parse_fraction(row.get('mn_onset', '0'))
            beat = float(mn_onset) + 1.0
            qb_raw = row.get(abs_onset_col, '') or row.get(other_col, '')
            abs_tick: Optional[int] = None
            if (qb_raw or '').strip():
                abs_tick = round(_parse_fraction(qb_raw) * TICKS_PER_QUARTER)
            if cad:
                cadence_markers.append(
                    DcmlMarker(abs_tick, cad, mn, beat, 'cadence'))
            if phr:
                phrase_markers.append(
                    DcmlMarker(abs_tick, phr, mn, beat, 'phraseend'))

    _tick_key = lambda m: (m.abs_tick if m.abs_tick is not None else -1,
                           m.measure_number, m.beat)
    cadence_markers.sort(key=_tick_key)
    phrase_markers.sort(key=_tick_key)
    return cadence_markers, phrase_markers


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

        degree_token = degree_match.group(1)
        degree_idx = _DEGREE_MAP[degree_token]
        local_tonic_pc = (global_tonic + semitones[degree_idx]) % 12
        # Minor-key raised submediant / leading tone (audit P2, tonicized path):
        # a lowercase vi / vii tonicization target in a minor global key roots a
        # semitone above the natural-minor degree (vi->+9, vii->+11), matching
        # _compute_root_pc and music21.  Without this, an applied chord like
        # 'V7/vi' or 'V/vii' in a minor key tonicizes a key a semitone flat.
        if global_minor and degree_idx in (5, 6):
            if n[:len(degree_token)].islower():
                local_tonic_pc = (local_tonic_pc + 1) % 12
        if prefix == 'b':
            local_tonic_pc = (local_tonic_pc - 1) % 12
        elif prefix == '#':
            local_tonic_pc = (local_tonic_pc + 1) % 12

        # Convert pitch class back to a note name (single-sourced module constant, #6)
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

# A tonicization target is a bare Roman-numeral degree (optionally accidental).
# Used to disambiguate the OVERLOADED slash in WiR rntxt: a '/' precedes a
# tonicization ('V/vi') but ALSO appears inside figured-bass inversions
# ('V6/5', '4/3') and the half-diminished sigil ('vii/o7').  Only a trailing
# slash-segment that is a pure degree token is a tonicization.
_RNTXT_TARGET_RE = re.compile(
    r'^[#b]?(?:VII|VI|IV|V|III|II|I|vii|vi|iv|v|iii|ii|i)$')


def _split_rntxt_applied(numeral: str) -> tuple[str, str]:
    """Split a WiR rntxt numeral into (primary_chord, tonicization_target).

    The trailing '/'-segment is treated as a tonicization target ONLY when it is
    a bare Roman-numeral degree; otherwise the slash belongs to a figured-bass
    inversion ('V6/5' -> ('V6/5', '')) or the half-dim sigil ('vii/o7' ->
    ('vii/o7', '')).  'V/vi' -> ('V', 'vi'); 'V6/5/iv' -> ('V6/5', 'iv');
    'vii/o7/V' -> ('vii/o7', 'V').  Multi-level tonicization ('V/V/V') resolves
    only the last level ('V/V', 'V'), matching the TSV single-level relativeroot
    behavior.
    """
    if '/' not in numeral:
        return numeral, ''
    head, _, tail = numeral.rpartition('/')
    if _RNTXT_TARGET_RE.match(tail):
        return head, tail
    return numeral, ''


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
            # Applied / secondary chords (V/V, viio7/V, V65/IV): resolve the
            # tonicized target to its absolute key BEFORE rooting the primary
            # numeral, exactly as the TSV path does via relativeroot (audit P1).
            # The previous code rooted the primary in the LOCAL key — e.g.
            # 'V/vi' in B-flat was rooted F instead of the true D (877/880
            # applied rntxt rows mis-rooted, 0.3% oracle agreement).
            primary, target = _split_rntxt_applied(numeral)
            effective_key = _resolve_dcml_key(target, key) if target else key
            root_pc = _compute_root_pc(primary, effective_key)
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


# ══════════════════════════════════════════════════════════════════════════
# OI-142 corpus-transposition correction — the ONE shared WiR loading substrate
# ══════════════════════════════════════════════════════════════════════════
# 12 of 326 WiR-covered Bach-chorale editions are TRANSPOSED relative to their
# When-in-Rome reference (a constant whole-piece root offset; our reading follows
# the notated signature, the WiR edition is in another key — NOT a key-inference
# error). Per the user's 2026-07-12 decision (register OI-142, ARITHMETIC
# CORRECTION), the grading applies each piece's committed offset to the ground
# truth HERE — at the single loading substrate every graded consumer imports — so
# a corrected piece grades identically everywhere with no consumer-side special-
# casing. The offsets + their independent re-verification live in the committed
# data file below (no code carries the numbers). See CLAUDE.md gate block (A),
# cc_key_grading_rebaseline_report.md, cc_key_mode_inference_diagnosis_report.md §5.

_TRANSPOSE_OFFSETS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "robust_stop",
    "corpus_transposition_offsets.json")
_TRANSPOSE_OFFSETS_CACHE: Optional[dict] = None


def _load_transposition_offsets() -> dict:
    """Load the committed OI-142 offsets file once ({stem: int offset}). A missing or
    malformed file yields {} (no correction) — the 314 untouched pieces are unaffected
    either way, and the substrate degrades to the plain parse."""
    global _TRANSPOSE_OFFSETS_CACHE
    if _TRANSPOSE_OFFSETS_CACHE is None:
        try:
            with open(_TRANSPOSE_OFFSETS_PATH, encoding='utf-8') as f:
                data = json.load(f)
            _TRANSPOSE_OFFSETS_CACHE = {
                stem: int(entry["offset"]) % 12
                for stem, entry in data.get("offsets", {}).items()
            }
        except (OSError, ValueError, KeyError, TypeError):
            _TRANSPOSE_OFFSETS_CACHE = {}
    return _TRANSPOSE_OFFSETS_CACHE


def wir_transposition_offset(stem: str) -> int:
    """The committed OI-142 transposition offset (semitones) for `stem`; 0 if not transposed."""
    return _load_transposition_offsets().get(stem, 0)


def _transpose_key_string(key: str, offset: int) -> str:
    """Transpose a DCML key string's tonic up by `offset` semitones, preserving mode (case).
    Empty/None passes through unchanged."""
    if not key:
        return key
    tonic = _key_to_tonic_pc(key)
    is_minor = key[0].islower()
    note = _PC_TO_NOTE[(tonic + offset) % 12]
    return note.lower() if is_minor else note


def _transpose_region(r: DcmlRegion, offset: int) -> DcmlRegion:
    """Return a copy of DcmlRegion transposed up by `offset` semitones: root_pc + global_key
    + local_key shift by offset; the Roman-numeral / chord_symbol strings are key-relative and
    stay verbatim (a transposed edition plays the same functional progression). Internally
    consistent: 'V' under the shifted local key roots at the shifted root_pc."""
    if offset % 12 == 0:
        return r
    return replace(
        r,
        root_pc=(None if r.root_pc is None else (r.root_pc + offset) % 12),
        global_key=_transpose_key_string(r.global_key, offset),
        local_key=_transpose_key_string(r.local_key, offset),
    )


def load_wir_regions(wir_base: str, stem: str) -> List[DcmlRegion]:
    """THE shared When-in-Rome ground-truth loading substrate.

    Resolve the analysis.txt for `stem`, parse it (parse_rntxt_file), and apply the committed
    OI-142 corpus-transposition correction so the 12 transposed editions grade against what OUR
    score actually contains — through this one path, no consumer-side special-casing. Every
    graded consumer (a8_rebaseline_measure, characterise_bir_false, measure_joint_probe,
    classify_key_disagreement) loads WiR through here so a corrected piece grades identically
    everywhere. Returns [] when the stem has no WiR reference. For a non-transposed stem the
    result is byte-identical to parse_rntxt_file(find_wir_file(...))."""
    path = find_wir_file(wir_base, stem)
    if not path:
        return []
    regions = parse_rntxt_file(path)
    offset = wir_transposition_offset(stem)
    if offset:
        regions = [_transpose_region(r, offset) for r in regions]
    return regions
