#!/usr/bin/env python3
# Python interpreter: /c/s/MS/.venv/Scripts/python.exe  (mainline venv)
"""compare_triage.py — LLM-Triage v1.3 Comparator + Triage Queue

CLI: compare_triage.py <score_basename> <output_dir>

Discovers all <basename>.*_response.json files in output_dir, bucketizes
judgments by measure, computes multi-axis chord-label agreement across
sources (analyzer + LLMs + optional ground truth), classifies each cell
by issue type per the documented taxonomy, and emits:

  <basename>.triage_queue.md   — human-readable, prioritised
  <basename>.triage_queue.json — structured, with empty verdict fields

Priority cascade (lower numeric score = more urgent; sort ascending):
  priority_score = base_priority + gt_boost
  gt_boost = -5 when ground_truth_position == "out_of_alignment", else 0

Base priority table:
  1  boundary_disagreement        Source absent from a beat slot others cover
  2  root_disagreement            Different root_pc across sources
  3  quality_disagreement         Same root, different quality
  4  inversion_disagreement_with_gt  Same root+quality, GT sides with one inversion
  5  extension_disagreement_with_gt  Same root+quality+inversion, GT sides with ext
  6  inversion_only               Same root+quality, different bass_pc, no GT signal
  7  extension_only               Same root+quality+inversion, different exts, no GT signal
  8  outlier_voice                N-1 sources agree exactly, 1 disagrees
  9  all_agree                    Exact match across all non-None sources
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Beat-range utilities
# ---------------------------------------------------------------------------

BEAT_END = 99  # sentinel for "end" in beat-range strings


def parse_beat_range(br: str) -> Tuple[int, int]:
    """Parse 'X-Y' or 'X' or 'X-end' to inclusive (start, end) ints.

    'end' and non-numeric tokens map to BEAT_END (99).
    """
    br = br.strip()
    if not br:
        return (0, 0)
    parts = br.split("-", 1)
    def _int(s: str) -> int:
        s = s.strip()
        if s.isdigit():
            return int(s)
        return BEAT_END
    start = _int(parts[0])
    end = _int(parts[1]) if len(parts) == 2 else start
    return (start, end)


def beat_ranges_overlap(r1: Tuple[int, int], r2: Tuple[int, int]) -> bool:
    """True if two inclusive beat-range intervals share at least one beat."""
    return max(r1[0], r2[0]) <= min(r1[1], r2[1])


def overlap_size(r1: Tuple[int, int], r2: Tuple[int, int]) -> int:
    return max(0, min(r1[1], r2[1]) - max(r1[0], r2[0]) + 1)


# ---------------------------------------------------------------------------
# Chord-label parser
# ---------------------------------------------------------------------------

_NOTE_PC: Dict[str, int] = {
    "C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11,
}


@dataclass
class ChordParts:
    root_pc: int          # 0-11, enharmonic-equivalent
    root_letter: str      # original spelling, e.g. "F#" or "Gb"
    quality: str          # "maj","min","dim","aug","sus2","sus4","sus","unknown"
    has_seventh: bool     # any 7th extension present
    has_minor_seventh: bool  # b7 specifically (dominant / minor 7th)
    extensions: frozenset  # tokens like {"9","b9","#11","add9"}
    bass_pc: Optional[int]  # slash-bass pitch class; None if no slash
    bass_letter: Optional[str]
    raw: str              # original chord_label string


def _normalize(s: str) -> str:
    """Replace unusual flat/sharp characters with ASCII equivalents."""
    return s.replace("�", "b").replace("♭", "b").replace("♯", "#")


def _parse_note_head(s: str) -> Optional[Tuple[str, str, int, str]]:
    """Parse leading note name. Returns (UPPER_letter, accidentals, pc, rest)."""
    if not s:
        return None
    letter = s[0].upper()
    if letter not in _NOTE_PC:
        return None
    pc = _NOTE_PC[letter]
    i = 1
    while i < len(s) and s[i] in ("#", "b"):
        pc = (pc + 1) % 12 if s[i] == "#" else (pc - 1) % 12
        i += 1
    return letter, s[1:i], pc, s[i:]


def _find_slash_bass(s: str) -> Tuple[str, Optional[str]]:
    """Split on last '/' where what follows looks like a note (A-G).

    Returns (chord_part, bass_str_or_None).
    '/' that is part of a chord type (e.g. D6/9 where tail starts with a digit)
    is left intact.
    """
    idx = s.rfind("/")
    if idx == -1:
        return s, None
    tail = s[idx + 1:]
    if tail and tail[0].upper() in _NOTE_PC:
        return s[:idx], tail
    return s, None  # e.g. D6/9 — slash separates extension digits


def _parse_body(body: str) -> Tuple[str, bool, bool, frozenset]:
    """Parse body (after root, before slash bass) into quality/ext fields.

    Returns (quality, has_seventh, has_minor_seventh, extensions_frozenset).
    Conservative: when in doubt emit quality='unknown' rather than guess.

    Quality+seventh combinations detected (in priority order):
      dim7          → dim, seventh (diminished 7th = bb7, not b7)
      dim           → dim
      aug           → aug
      mMaj7/minMaj7 → min, seventh (minor major 7th, has_minor_seventh=False)
      Maj7/maj7/M7  → maj, seventh (major 7th, has_minor_seventh=False)
      m/min         → min
      Maj/maj       → maj (explicit)
      sus4/sus2/sus → suspended
      (default)     → maj
    """
    quality = "maj"
    has_seventh = False
    has_minor_seventh = False
    exts: Set[str] = set()

    # Flatten parenthesized groups into the token stream.
    body = re.sub(r"\(([^)]*)\)", lambda m: " " + m.group(1) + " ", body)
    body = body.strip()

    # "alt" suffix (altered chord: dominant 7th with altered tensions)
    if re.search(r"(?:^|[^a-z])alt(?:[^a-z]|$)", body, re.I):
        return "maj", True, True, frozenset({"alt"})

    r = body  # remaining string, consumed left to right

    # --- Quality + seventh type ---

    if re.match(r"dim7", r, re.I):
        quality = "dim"; has_seventh = True; has_minor_seventh = False
        r = r[4:]

    elif re.match(r"dim", r, re.I):
        quality = "dim"
        r = r[3:]

    elif re.match(r"aug", r, re.I):
        quality = "aug"
        r = r[3:]

    # Minor-major 7th: m/min followed by Maj7 or M7
    elif re.match(r"m(?:in?)?[Mm](?:aj)?7", r):
        m_pfx = re.match(r"m(?:in?)?", r, re.I)
        r = r[m_pfx.end():]
        quality = "min"; has_seventh = True; has_minor_seventh = False
        exts.add("maj7")
        mm = re.match(r"[Mm](?:aj)?7", r)
        if mm:
            r = r[mm.end():]

    # Explicit major 7th without minor prefix: Maj7, maj7, M7
    elif re.match(r"(?:[Mm]aj|M)7", r):
        mm = re.match(r"(?:[Mm]aj|M)7", r)
        r = r[mm.end():]
        quality = "maj"; has_seventh = True; has_minor_seventh = False
        exts.add("maj7")

    # Explicit major (no seventh yet): Maj, maj
    elif re.match(r"[Mm]aj", r):
        r = r[3:]
        quality = "maj"

    # Minor: m or min — consume only the quality prefix, extensions come later
    elif re.match(r"m", r):
        m_pfx = re.match(r"m(?:in?)?", r, re.I)
        r = r[m_pfx.end():]
        quality = "min"

    # --- Suspended quality (standalone or after quality prefix) ---
    m_sus = re.match(r"sus(4|2)?", r, re.I)
    if m_sus:
        s_num = m_sus.group(1) or ""
        quality = "sus4" if s_num == "4" else ("sus2" if s_num == "2" else "sus")
        r = r[m_sus.end():]

    # --- Tokenise remaining string for extensions and seventh ---
    pos = 0
    tok = r.strip()

    while pos < len(tok):
        ch = tok[pos]

        if ch == " ":
            pos += 1
            continue

        # "add" prefix followed by optional accidental and number
        if tok[pos:pos + 3].lower() == "add":
            pos += 3
            nm = re.match(r"[b#]?\d+", tok[pos:])
            if nm:
                exts.add("add" + nm.group(0))
                pos += nm.end()
            continue

        # Accidental + digit: b9, #11, b5, etc.
        if ch in ("#", "b") and pos + 1 < len(tok) and tok[pos + 1].isdigit():
            nm = re.match(r"[b#]\d+", tok[pos:])
            if nm:
                exts.add(nm.group(0))
                pos += nm.end()
                continue

        # Plain digit
        if ch.isdigit():
            nm = re.match(r"\d+", tok[pos:])
            num_str = nm.group(0)
            num = int(num_str)
            pos += nm.end()
            if num == 7:
                if not has_seventh:          # don't overwrite maj7 already set
                    has_seventh = True
                    has_minor_seventh = True
            elif num in (9, 11, 13):
                has_seventh = True
                has_minor_seventh = True     # extended dominant implies b7
                exts.add(str(num))
            else:
                exts.add(num_str)            # 6, 5, 2, 4, etc.
            continue

        # "sus" may appear after a numeric token (e.g. "7sus4", "13sus4")
        if tok[pos:pos + 3].lower() == "sus":
            m_sus2 = re.match(r"sus(4|2)?", tok[pos:], re.I)
            if m_sus2:
                s_num = m_sus2.group(1) or ""
                quality = "sus4" if s_num == "4" else ("sus2" if s_num == "2" else "sus")
                pos += m_sus2.end()
                continue

        # Skip unknown characters conservatively
        pos += 1

    return quality, has_seventh, has_minor_seventh, frozenset(exts)


def parse_chord(raw: str) -> Optional[ChordParts]:
    """Parse a chord label string to ChordParts. Returns None for empty label."""
    raw = raw.strip()
    if not raw:
        return None

    s = _normalize(raw)

    chord_part, bass_str = _find_slash_bass(s)

    bass_pc: Optional[int] = None
    bass_letter: Optional[str] = None
    if bass_str:
        result = _parse_note_head(bass_str)
        if result:
            bl_upper, bl_acc, bass_pc, _ = result
            bass_letter = bl_upper + bl_acc

    result = _parse_note_head(chord_part)
    if result is None:
        return ChordParts(
            root_pc=0, root_letter="?", quality="unknown",
            has_seventh=False, has_minor_seventh=False,
            extensions=frozenset(), bass_pc=bass_pc, bass_letter=bass_letter,
            raw=raw,
        )

    root_upper, root_acc, root_pc, body = result
    root_letter = root_upper + root_acc

    quality, has_seventh, has_minor_seventh, extensions = _parse_body(body)

    return ChordParts(
        root_pc=root_pc,
        root_letter=root_letter,
        quality=quality,
        has_seventh=has_seventh,
        has_minor_seventh=has_minor_seventh,
        extensions=extensions,
        bass_pc=bass_pc,
        bass_letter=bass_letter,
        raw=raw,
    )


# ---------------------------------------------------------------------------
# Source loading
# ---------------------------------------------------------------------------

@dataclass
class Source:
    provider: str        # e.g. "claude", "musescore_analyzer", "music21_ground_truth"
    filename: str
    is_authoritative: bool
    model: str
    metadata: dict
    judgments: List[dict]


def _provider_from_filename(path: Path) -> str:
    """Derive a provider name from the filename stem.

    E.g. 'bwv10.7.claude_response.json' → 'claude'
        'pachelbel.llm_response.json'   → 'llm'
    """
    name = path.name
    # Remove trailing _response.json
    stem = re.sub(r"_response\.json$", "", name)
    # Remove the score basename prefix (everything up to and including the last dot before provider)
    # Filenames look like: <basename>.<provider>_response.json
    # basename may contain dots (e.g. bwv10.7), so we find the last segment
    parts = stem.rsplit(".", 1)
    if len(parts) == 2:
        return parts[1]
    return stem


def load_sources(output_dir: Path, basename: str) -> List[Source]:
    pattern = f"{basename}.*_response.json"
    files = sorted(output_dir.glob(pattern))
    if not files:
        print(f"ERROR: no *_response.json files found for '{basename}' in {output_dir}",
              file=sys.stderr)
        sys.exit(1)

    sources = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"ERROR loading {f}: {exc}", file=sys.stderr)
            sys.exit(1)

        top_keys = list(data.keys())
        if set(top_keys) != {"metadata", "tool_input"}:
            print(
                f"ERROR: {f} has unexpected top-level keys {top_keys} "
                f"(expected ['metadata', 'tool_input'])",
                file=sys.stderr,
            )
            sys.exit(1)

        meta = data["metadata"]
        ti = data["tool_input"]
        provider = meta.get("provider") or _provider_from_filename(f)
        is_auth = bool(meta.get("is_authoritative", False))
        model = meta.get("model", "unknown")
        judgments = ti.get("judgments", [])

        sources.append(Source(
            provider=provider,
            filename=f.name,
            is_authoritative=is_auth,
            model=model,
            metadata=meta,
            judgments=judgments,
        ))

    return sources


# ---------------------------------------------------------------------------
# Cell creation (measure-level bucketing + beat-range alignment)
# ---------------------------------------------------------------------------

@dataclass
class CellSourceEntry:
    judgment: dict          # raw judgment dict
    beat_range_actual: str  # the source's own beat-range string
    exact_br_match: bool    # True if beat_range_actual == cell's beat_range


@dataclass
class Cell:
    measure: int
    beat_range: str          # canonical beat-range for this cell
    beat_range_parsed: Tuple[int, int]
    source_entries: Dict[str, CellSourceEntry]  # provider → entry (absent if missing)
    is_boundary_cell: bool   # True if some sources present in measure but absent here


def _group_by_measure(judgments: List[dict]) -> Dict[int, List[dict]]:
    out: Dict[int, List[dict]] = defaultdict(list)
    for j in judgments:
        m = j.get("measure")
        if m is not None:
            out[int(m)].append(j)
    return out


def create_cells(
    sources: List[Source],
) -> List[Cell]:
    """Build comparison cells across all sources.

    Algorithm:
    1. For each measure, collect all (beat_range_str → set_of_providers) across sources.
    2. PRIMARY cells: beat-ranges used by ≥2 sources exactly.
    3. SOLO cells: beat-ranges used by only 1 source that have NO overlap with any
       primary cell → flagged as boundary.
    4. If no primary cells exist in a measure (all sources use unique beat-ranges),
       all are treated as primary.
    5. For each cell, each source is overlap-matched to its best judgment.
    6. A cell is flagged is_boundary_cell when ≥1 source has judgments elsewhere in
       the measure but is absent from this cell (no overlapping judgment).
    """
    # Build measure-indexed judgments per source
    measure_judgments: Dict[str, Dict[int, List[dict]]] = {}
    all_measures: Set[int] = set()
    for src in sources:
        mgr = _group_by_measure(src.judgments)
        measure_judgments[src.provider] = mgr
        all_measures.update(mgr.keys())

    cells: List[Cell] = []

    for measure in sorted(all_measures):
        # Collect beat-ranges per provider for this measure
        br_to_providers: Dict[str, Set[str]] = defaultdict(set)
        for src in sources:
            for j in measure_judgments[src.provider].get(measure, []):
                br = j.get("beat_range", "")
                if br:
                    br_to_providers[br].add(src.provider)

        if not br_to_providers:
            continue

        # PRIMARY: ≥2 providers share the exact beat-range string
        primary_brs: Dict[str, Tuple[int, int]] = {
            br: parse_beat_range(br)
            for br, providers in br_to_providers.items()
            if len(providers) >= 2
        }

        # When no primaries exist, treat all as primary
        if not primary_brs:
            primary_brs = {br: parse_beat_range(br) for br in br_to_providers}

        # SOLO candidates: beat-ranges used by exactly 1 provider
        solo_candidates: Dict[str, Tuple[int, int]] = {
            br: parse_beat_range(br)
            for br, providers in br_to_providers.items()
            if len(providers) == 1
        }

        # Solo cells: solo beat-ranges with NO overlap against any primary
        solo_brs: Dict[str, Tuple[int, int]] = {
            br: parsed
            for br, parsed in solo_candidates.items()
            if not any(
                beat_ranges_overlap(parsed, p_parsed)
                for p_parsed in primary_brs.values()
            )
        }

        cell_brs = {**primary_brs, **solo_brs}

        # Sort cells within measure by (start, end)
        sorted_cell_brs = sorted(cell_brs.items(), key=lambda kv: kv[1])

        for br_str, br_parsed in sorted_cell_brs:
            source_entries: Dict[str, CellSourceEntry] = {}

            for src in sources:
                src_judgments_in_measure = measure_judgments[src.provider].get(measure, [])
                # Find judgments that overlap with this cell
                overlapping = [
                    (j, parse_beat_range(j.get("beat_range", "0")))
                    for j in src_judgments_in_measure
                    if beat_ranges_overlap(br_parsed, parse_beat_range(j.get("beat_range", "0")))
                ]
                if overlapping:
                    # Pick judgment with maximum overlap
                    best_j, best_parsed = max(
                        overlapping,
                        # Primary: maximize overlap; secondary: prefer start closest to cell start
                        key=lambda pair: (
                            overlap_size(br_parsed, pair[1]),
                            -abs(pair[1][0] - br_parsed[0]),
                        ),
                    )
                    source_entries[src.provider] = CellSourceEntry(
                        judgment=best_j,
                        beat_range_actual=best_j.get("beat_range", ""),
                        exact_br_match=(best_j.get("beat_range", "") == br_str),
                    )
                # else: source absent for this cell

            # Boundary flag: any source has judgments in this measure but is absent from this cell
            is_boundary = any(
                src.provider not in source_entries
                and bool(measure_judgments[src.provider].get(measure))
                for src in sources
            )

            cells.append(Cell(
                measure=measure,
                beat_range=br_str,
                beat_range_parsed=br_parsed,
                source_entries=source_entries,
                is_boundary_cell=is_boundary or (br_str in solo_brs),
            ))

    return cells


# ---------------------------------------------------------------------------
# Multi-axis agreement
# ---------------------------------------------------------------------------

@dataclass
class Axes:
    same_root_pc: bool
    same_quality: bool
    same_extension_class: bool   # all share presence/absence of any 7th/ext
    same_full_extensions: bool   # all share exact extension frozenset
    same_inversion: bool         # all share bass_pc (None counts as a value)
    exact_match: bool            # all share raw string verbatim


def compute_axes(parsed_parts: List[Optional[ChordParts]]) -> Axes:
    """Compute agreement axes from a list of ChordParts (None = absent/empty label)."""
    valid = [p for p in parsed_parts if p is not None]
    if len(valid) < 2:
        # 0 or 1 source with a valid label — trivially "agree"
        return Axes(
            same_root_pc=True, same_quality=True,
            same_extension_class=True, same_full_extensions=True,
            same_inversion=True, exact_match=True,
        )

    same_root = len({p.root_pc for p in valid}) == 1
    same_qual = len({p.quality for p in valid}) == 1
    # extension_class: do all agree on whether any 7th or extension is present?
    ext_class = {(p.has_seventh or bool(p.extensions)) for p in valid}
    same_ext_class = len(ext_class) == 1
    same_full_ext = len({p.extensions for p in valid}) == 1
    same_inv = len({p.bass_pc for p in valid}) == 1
    exact = len({p.raw for p in valid}) == 1

    return Axes(
        same_root_pc=same_root,
        same_quality=same_qual,
        same_extension_class=same_ext_class,
        same_full_extensions=same_full_ext,
        same_inversion=same_inv,
        exact_match=exact,
    )


# ---------------------------------------------------------------------------
# Issue-type classification
# ---------------------------------------------------------------------------

def classify_issue(
    cell: Cell,
    axes: Axes,
    n_sources_with_label: int,
    gt_position: str,
) -> Tuple[str, int]:
    """Return (issue_type, base_priority) using the priority cascade.

    Priority table (first match wins):
      1  boundary_disagreement
      2  root_disagreement
      3  quality_disagreement
      4  inversion_disagreement_with_gt
      5  extension_disagreement_with_gt
      6  inversion_only
      7  extension_only
      8  outlier_voice
      9  all_agree
    """
    if cell.is_boundary_cell:
        return "boundary_disagreement", 1

    if not axes.same_root_pc:
        return "root_disagreement", 2

    if not axes.same_quality:
        return "quality_disagreement", 3

    gt_active = gt_position in ("matches_consensus", "matches_minority", "out_of_alignment")

    if not axes.same_inversion:
        if gt_active and gt_position in ("matches_minority", "out_of_alignment"):
            return "inversion_disagreement_with_gt", 4
        return "inversion_only", 6

    if not axes.same_full_extensions:
        if gt_active and gt_position in ("matches_minority", "out_of_alignment"):
            return "extension_disagreement_with_gt", 5
        return "extension_only", 7

    if axes.exact_match:
        return "all_agree", 9

    # Exact mismatch but same root/quality/inversion/extensions:
    # Raw strings differ only in spelling (enharmonic or whitespace) — treat as all_agree
    # unless outlier_voice applies
    # Check outlier: n_sources_with_label sources, exactly 1 disagrees from the rest
    valid_raws = [
        e.judgment.get("chord_label", "")
        for e in cell.source_entries.values()
        if e.judgment.get("chord_label")
    ]
    if len(valid_raws) >= 3:
        from collections import Counter
        counts = Counter(valid_raws)
        most_common_count = counts.most_common(1)[0][1]
        if most_common_count == len(valid_raws) - 1:
            return "outlier_voice", 8

    return "all_agree", 9


def compute_gt_position(
    gt_provider: Optional[str],
    cell: Cell,
    axes: Axes,
    parsed_by_source: Dict[str, Optional[ChordParts]],
    non_gt_providers: List[str],
) -> Tuple[str, Optional[str], Optional[str]]:
    """Return (gt_position, gt_chord_label, non_gt_consensus_chord_label).

    gt_position values: "matches_consensus" | "matches_minority" |
                        "out_of_alignment" | "absent"
    """
    if gt_provider is None or gt_provider not in cell.source_entries:
        return "absent", None, None

    gt_entry = cell.source_entries[gt_provider]
    gt_label = gt_entry.judgment.get("chord_label", "")
    if not gt_label:
        # Ground truth has empty chord_label (quality=Unknown) → treat as absent
        return "absent", "", None

    gt_parsed = parsed_by_source.get(gt_provider)

    # Consensus among non-GT sources
    non_gt_labels = [
        cell.source_entries[p].judgment.get("chord_label", "")
        for p in non_gt_providers
        if p in cell.source_entries
    ]
    non_gt_parsed = [parsed_by_source.get(p) for p in non_gt_providers if p in cell.source_entries]
    non_gt_parsed_valid = [x for x in non_gt_parsed if x is not None]

    if not non_gt_parsed_valid:
        return "absent", gt_label, None

    from collections import Counter
    label_counts = Counter(
        p.raw for p in non_gt_parsed_valid
    )
    consensus_label = label_counts.most_common(1)[0][0] if label_counts else None

    if gt_parsed is None:
        return "absent", gt_label, consensus_label

    # Compare GT root_pc + quality + bass_pc against consensus
    consensus_parsed_list = [p for p in non_gt_parsed_valid]

    # Count non-GT sources that match GT on root_pc
    matching_root = sum(
        1 for p in consensus_parsed_list if p.root_pc == gt_parsed.root_pc
    )
    total_non_gt = len(consensus_parsed_list)

    if matching_root == 0:
        # GT root disagrees with all non-GT sources
        return "out_of_alignment", gt_label, consensus_label

    if matching_root == total_non_gt:
        # All non-GT sources share GT's root. Check inversion (bass_pc).
        matching_inv = sum(
            1 for p in consensus_parsed_list if p.bass_pc == gt_parsed.bass_pc
        )
        if matching_inv == 0:
            # GT inversion disagrees with every non-GT source — still out_of_alignment
            return "out_of_alignment", gt_label, consensus_label
        if matching_inv == total_non_gt:
            return "matches_consensus", gt_label, consensus_label
        # strict majority required to count as consensus (> half, not ≥ half)
        if matching_inv > total_non_gt / 2:
            return "matches_consensus", gt_label, consensus_label
        return "matches_minority", gt_label, consensus_label

    if matching_root > total_non_gt / 2:
        return "matches_consensus", gt_label, consensus_label
    return "matches_minority", gt_label, consensus_label


# ---------------------------------------------------------------------------
# Suggested action hints
# ---------------------------------------------------------------------------

_SUGGESTED_ACTIONS: Dict[str, str] = {
    "boundary_disagreement": (
        "Inspect the score at this measure: one or more sources skipped this "
        "beat region entirely. Decide which beat-range segmentation is correct."
    ),
    "root_disagreement": (
        "Root-note disagreement. Listen/read the score and determine the correct "
        "root. Update the outlier source's analysis or the ground truth."
    ),
    "quality_disagreement": (
        "Same root, different chord quality (e.g. major vs. minor). Check the "
        "third in the score and adjudicate."
    ),
    "inversion_disagreement_with_gt": (
        "Ground truth flags an inversion disagreement. Check the actual bass note "
        "in the score; ground truth may be correct or may reflect Roman-numeral "
        "convention differences."
    ),
    "extension_disagreement_with_gt": (
        "Ground truth disagrees on extensions. Determine whether the passing tone / "
        "extension is structural (chord tone) or ornamental."
    ),
    "inversion_only": (
        "Sources agree on root+quality but differ on bass note / inversion. "
        "Inspect the bass voice and decide if inversion notation is warranted."
    ),
    "extension_only": (
        "Sources agree on root+quality+inversion but differ on extensions (7ths, "
        "9ths, etc.). Low priority — decide whether extensions should be labeled."
    ),
    "outlier_voice": (
        "One source disagrees with the consensus. Likely a model error or an "
        "alternative reading. Check the outlier and decide if it reveals a genuine "
        "ambiguity."
    ),
    "all_agree": (
        "All sources agree. No action needed unless you spot a systematic error "
        "across all sources."
    ),
}


# ---------------------------------------------------------------------------
# Priority bucketing
# ---------------------------------------------------------------------------

def priority_bucket(base_priority: int, gt_position: str) -> str:
    """Map base_priority + GT signal to high/medium/low/all_agree bucket."""
    if base_priority == 9:
        return "all_agree"
    if base_priority <= 3 or gt_position == "out_of_alignment":
        return "high"
    if base_priority <= 6:
        return "medium"
    return "low"


def priority_score(base_priority: int, gt_position: str) -> int:
    """Numeric sort key: lower = more urgent (sort ascending).

    Formula: base_priority + gt_boost
    base_priority 1-9 directly (1=most urgent, 9=all_agree).
    gt_boost = -5 when gt_position == "out_of_alignment" — this shifts GT-contradicted
    cells to negative scores so they sort before base_priority=1 (boundary).

    Example order (ascending):
      -3 (root_disagreement + GT out_of_alignment)
      -1 (inversion_with_gt + GT out_of_alignment)
       1 (boundary_disagreement, no GT)
       2 (root_disagreement, no GT)
       3 (quality_disagreement, no GT)
       ...
       9 (all_agree)
    """
    boost = -5 if gt_position == "out_of_alignment" else 0
    return base_priority + boost


# ---------------------------------------------------------------------------
# Full triage pipeline
# ---------------------------------------------------------------------------

@dataclass
class TriageEntry:
    id: int
    priority_bucket: str
    priority_score_val: int
    base_priority: int
    issue_type: str
    measure: int
    beat_range: str
    tick_start: Optional[int]
    tick_end: Optional[int]
    sources_data: Dict[str, dict]
    axes: Axes
    gt_position: str
    gt_chord_label: Optional[str]
    non_gt_consensus: Optional[str]
    suggested_action: str
    parsed_by_source: Dict[str, Optional[ChordParts]]


def build_triage(
    sources: List[Source],
    cells: List[Cell],
) -> List[TriageEntry]:
    gt_source = next((s for s in sources if s.is_authoritative), None)
    gt_provider = gt_source.provider if gt_source else None
    non_gt_providers = [s.provider for s in sources if not s.is_authoritative]

    entries: List[TriageEntry] = []
    entry_id = 1

    for cell in cells:
        # Parse chord labels for each source present in this cell
        parsed_by_source: Dict[str, Optional[ChordParts]] = {}
        unknown_labels: List[Tuple[str, str]] = []  # (provider, label)

        for src in sources:
            if src.provider not in cell.source_entries:
                parsed_by_source[src.provider] = None
                continue
            label = cell.source_entries[src.provider].judgment.get("chord_label", "")
            parsed = parse_chord(label)
            parsed_by_source[src.provider] = parsed
            if parsed and parsed.quality == "unknown" and label:
                unknown_labels.append((src.provider, label))

        # Collect valid (non-None) parsed parts for axes
        valid_parsed = [p for p in parsed_by_source.values() if p is not None]
        axes = compute_axes(valid_parsed)

        gt_position, gt_label, non_gt_consensus = compute_gt_position(
            gt_provider, cell, axes, parsed_by_source, non_gt_providers
        )

        issue_type, base_prio = classify_issue(
            cell, axes, len(valid_parsed), gt_position
        )

        p_score = priority_score(base_prio, gt_position)
        bucket = priority_bucket(base_prio, gt_position)

        # Build per-source data for output
        sources_data: Dict[str, dict] = {}
        for src in sources:
            if src.provider not in cell.source_entries:
                sources_data[src.provider] = None
                continue
            entry = cell.source_entries[src.provider]
            j = entry.judgment
            parsed = parsed_by_source[src.provider]
            parsed_dict = None
            if parsed:
                parsed_dict = {
                    "root_pc": parsed.root_pc,
                    "root_letter": parsed.root_letter,
                    "quality": parsed.quality,
                    "has_seventh": parsed.has_seventh,
                    "has_minor_seventh": parsed.has_minor_seventh,
                    "extensions": sorted(parsed.extensions),
                    "bass_pc": parsed.bass_pc,
                    "bass_letter": parsed.bass_letter,
                }
            sources_data[src.provider] = {
                "chord_label": j.get("chord_label", ""),
                "beat_range_actual": entry.beat_range_actual,
                "confidence": j.get("confidence", ""),
                "confidence_raw": j.get("confidence_raw"),
                "parsed": parsed_dict,
            }

        # Ticks from the cell's judgments (use GT if available, else first source with ticks)
        tick_start = tick_end = None
        for src in sources:
            if src.provider in cell.source_entries:
                j = cell.source_entries[src.provider].judgment
                if j.get("tick_start") is not None:
                    tick_start = j["tick_start"]
                    tick_end = j.get("tick_end")
                    break

        entries.append(TriageEntry(
            id=entry_id,
            priority_bucket=bucket,
            priority_score_val=p_score,
            base_priority=base_prio,
            issue_type=issue_type,
            measure=cell.measure,
            beat_range=cell.beat_range,
            tick_start=tick_start,
            tick_end=tick_end,
            sources_data=sources_data,
            axes=axes,
            gt_position=gt_position,
            gt_chord_label=gt_label,
            non_gt_consensus=non_gt_consensus,
            suggested_action=_SUGGESTED_ACTIONS.get(issue_type, ""),
            parsed_by_source=parsed_by_source,
        ))
        entry_id += 1

    # Sort: by priority_score ascending, then measure ascending, then beat_range start
    entries.sort(key=lambda e: (e.priority_score_val, e.measure, e.beat_range_parsed[0] if hasattr(e, '_br_parsed') else 0))

    # Fix sort: need beat_range_parsed on entries
    # Re-sort using the cell's beat_range_parsed — attach it
    cell_map = {(c.measure, c.beat_range): c for c in cells}
    entries.sort(key=lambda e: (
        e.priority_score_val,
        e.measure,
        cell_map.get((e.measure, e.beat_range), Cell(0, "", (0, 0), {}, False)).beat_range_parsed[0],
    ))

    # Re-number after sort
    for i, e in enumerate(entries, 1):
        e.id = i

    return entries


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def _confidence_display(c: str, cr: Optional[float]) -> str:
    if cr is not None:
        return f"{c} ({cr:.2f})"
    return c or "—"


def render_markdown(
    basename: str,
    sources: List[Source],
    entries: List[TriageEntry],
    generated_utc: str,
) -> str:
    lines: List[str] = []
    flagged = [e for e in entries if e.priority_bucket != "all_agree"]
    agreed = [e for e in entries if e.priority_bucket == "all_agree"]

    provider_list = ", ".join(
        f"{s.provider} [GT]" if s.is_authoritative else s.provider
        for s in sources
    )

    lines.append(f"# Triage Queue: {basename}")
    lines.append("")
    lines.append(f"Sources: {provider_list}")
    lines.append(f"Total cells: {len(entries)}")
    lines.append(f"Flagged cells: {len(flagged)}")
    lines.append(f"Generated: {generated_utc}")
    lines.append("")

    bucket_order = ["high", "medium", "low"]
    bucket_headings = {"high": "## High priority", "medium": "## Medium priority", "low": "## Low priority"}

    for bucket in bucket_order:
        bucket_entries = [e for e in entries if e.priority_bucket == bucket]
        if not bucket_entries:
            continue
        lines.append(bucket_headings[bucket])
        lines.append("")
        for e in bucket_entries:
            gt_tag = ""
            if e.gt_position == "out_of_alignment":
                gt_tag = " ⚑ GT-contradicted"
            elif e.gt_position == "matches_minority":
                gt_tag = " (GT=minority)"
            lines.append(f"### {e.id}. m{e.measure} beats {e.beat_range}: {e.issue_type}{gt_tag}")
            lines.append("")

            # Source table
            header = "| Source | chord_label | beat_range | confidence | confidence_raw |"
            sep =    "|--------|-------------|------------|------------|----------------|"
            lines.append(header)
            lines.append(sep)
            for src in sources:
                sd = e.sources_data.get(src.provider)
                if sd is None:
                    lines.append(f"| {src.provider} | *(absent)* | — | — | — |")
                else:
                    br_note = sd["beat_range_actual"]
                    if br_note != e.beat_range:
                        br_note = f"{br_note} *"
                    lines.append(
                        f"| {src.provider} | {sd['chord_label'] or '*(empty)*'} "
                        f"| {br_note} "
                        f"| {sd['confidence'] or '—'} "
                        f"| {sd['confidence_raw'] if sd['confidence_raw'] is not None else '—'} |"
                    )
            lines.append("")
            if e.gt_position != "absent":
                lines.append(f"Ground truth position: **{e.gt_position}**")
                lines.append("")
            lines.append(f"Suggested action: {e.suggested_action}")
            lines.append("")

    # All-agree section (collapsed)
    lines.append("## All-agree (collapsed)")
    lines.append("")
    if agreed:
        lines.append(f"{len(agreed)} cells where all sources agreed exactly:")
        lines.append("")
        compact_parts = []
        for e in agreed:
            labels = [
                sd["chord_label"]
                for sd in e.sources_data.values()
                if sd and sd["chord_label"]
            ]
            label = labels[0] if labels else "?"
            compact_parts.append(f"m{e.measure} b{e.beat_range} ({label})")
        # Wrap into readable lines
        line = ""
        for part in compact_parts:
            candidate = (line + ", " + part) if line else part
            if len(candidate) > 100:
                lines.append(line + ",")
                line = part
            else:
                line = candidate
        if line:
            lines.append(line)
    else:
        lines.append("*(none — every cell has at least one disagreement)*")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# JSON output
# ---------------------------------------------------------------------------

def render_json(
    basename: str,
    sources: List[Source],
    entries: List[TriageEntry],
    generated_utc: str,
) -> dict:
    from collections import Counter

    sources_meta = [
        {
            "provider": s.provider,
            "is_authoritative": s.is_authoritative,
            "model": s.model,
            "filename": s.filename,
        }
        for s in sources
    ]

    flagged = [e for e in entries if e.priority_bucket != "all_agree"]
    issue_type_counts: Counter = Counter(e.issue_type for e in entries)
    bucket_counts: Counter = Counter(e.priority_bucket for e in entries)

    def axes_dict(a: Axes) -> dict:
        return {
            "same_root_pc": a.same_root_pc,
            "same_quality": a.same_quality,
            "same_extension_class": a.same_extension_class,
            "same_full_extensions": a.same_full_extensions,
            "same_inversion": a.same_inversion,
            "exact_match": a.exact_match,
        }

    json_entries = []
    for e in entries:
        sources_out = {}
        for prov, sd in e.sources_data.items():
            if sd is None:
                sources_out[prov] = None
            else:
                sources_out[prov] = sd

        json_entries.append({
            "id": e.id,
            "priority": e.priority_bucket,
            "priority_score": e.priority_score_val,
            "issue_type": e.issue_type,
            "measure": e.measure,
            "beat_range": e.beat_range,
            "tick_start": e.tick_start,
            "tick_end": e.tick_end,
            "sources": sources_out,
            "axes": axes_dict(e.axes),
            "ground_truth_position": e.gt_position,
            "ground_truth_chord_label": e.gt_chord_label,
            "non_gt_consensus_chord_label": e.non_gt_consensus,
            "suggested_action": e.suggested_action,
            "verdict": None,
            "verdict_chord_label": None,
            "verdict_notes": None,
            "verdict_user": None,
            "verdict_timestamp": None,
        })

    return {
        "score_basename": basename,
        "generated_utc": generated_utc,
        "sources": sources_meta,
        "summary": {
            "total_cells": len(entries),
            "flagged": len(flagged),
            "by_issue_type": dict(issue_type_counts),
            "by_priority": dict(bucket_counts),
        },
        "entries": json_entries,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="LLM-Triage v1.3 comparator: compare source response JSONs and emit triage queue."
    )
    parser.add_argument("score_basename", help="Score basename, e.g. bwv10.7")
    parser.add_argument("output_dir", help="Directory containing *_response.json files")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not output_dir.is_dir():
        print(f"ERROR: output_dir '{output_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)

    basename = args.score_basename
    sources = load_sources(output_dir, basename)

    if not sources:
        print(f"ERROR: no sources found for '{basename}'", file=sys.stderr)
        sys.exit(1)

    # Warn about unexpected sources (e.g. stale llm_response.json)
    for src in sources:
        if not src.metadata.get("provider"):
            print(
                f"WARNING: {src.filename} has no metadata.provider field; "
                f"treating as provider='{src.provider}' (derived from filename).",
                file=sys.stderr,
            )

    cells = create_cells(sources)
    entries = build_triage(sources, cells)

    generated_utc = datetime.now(timezone.utc).isoformat(timespec="seconds")

    md_path = output_dir / f"{basename}.triage_queue.md"
    json_path = output_dir / f"{basename}.triage_queue.json"

    md_path.write_text(
        render_markdown(basename, sources, entries, generated_utc),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(render_json(basename, sources, entries, generated_utc), indent=2),
        encoding="utf-8",
    )

    flagged = sum(1 for e in entries if e.priority_bucket != "all_agree")
    print(
        f"score={basename}  cells={len(entries)}  flagged={flagged}"
        f"  output={md_path}"
    )


if __name__ == "__main__":
    main()
