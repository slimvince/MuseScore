#!/usr/bin/env python3
"""
compare_analyses.py — Three-level comparison of batch_analyze output vs music21 output.

For each aligned region pair, classifies agreement as:

  full_agree          root pitch class + quality + Roman numeral all match
  near_agree          music21's chord matches our 2nd or 3rd alternative
  chord_agree_rn_differs   same root + quality, different Roman numeral
                           (extension/inversion labelling difference)
  chord_agree_key_differs  same chord identity, different key context
                           (expected in modulating passages)
  chord_disagree      different root or quality — genuine analysis difference
  unaligned           no corresponding region found (time-range mismatch)

Alignment strategy:
  For each of our regions [startTick, endTick), find the music21 chord with the
  longest overlap with that time span.  If overlap / our_duration >= 0.5 the
  regions are considered aligned.

Usage:
    python tools/compare_analyses.py <ours.json> <music21.json> [--html out.html]
    python tools/compare_analyses.py --help
"""

from __future__ import annotations

import argparse
import json
import re as _re2
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dcml_parser import DcmlRegion


# ══════════════════════════════════════════════════════════════════════════
# Data types
# ══════════════════════════════════════════════════════════════════════════

@dataclass
class Region:
    measure_number:   int
    beat:             float
    start_tick:       int
    end_tick:         int
    duration:         float
    root_pc:          int
    quality:          str
    chord_symbol:     str
    roman_numeral:    str
    key:              str
    key_confidence:   float
    diatonic_to_key:  Optional[bool]
    alternatives:     list[dict] = field(default_factory=list)
    # Enriched fields (present when JSON was produced by batch_analyze ≥ 5.0)
    chord_score:      Optional[float] = None
    chord_score_margin: Optional[float] = None
    bass_pc:          Optional[int]   = None
    bass_is_root:     Optional[bool]  = None
    note_count:       Optional[int]   = None
    pitch_class_set:  Optional[int]   = None
    key_runner_up:    Optional[dict]  = None   # {"key": str, "confidence": float} or None


@dataclass
class ComparedRegion:
    ours:           Region
    theirs:         Optional[Region]
    category:       str
    notes:          str = ""
    # Three-way DCML fields (populated when --dcml is supplied)
    dcml_region:    Optional[object] = field(default=None, repr=False)  # DcmlRegion | None
    three_way_cat:  str = "no_dcml"


# ══════════════════════════════════════════════════════════════════════════
# Loading helpers
# ══════════════════════════════════════════════════════════════════════════

def _load_region(d: dict) -> Region:
    cs  = d.get("chordScore")
    csm = d.get("chordScoreMargin")
    bpc = d.get("bassPitchClass")
    bir = d.get("bassIsRoot")
    nc  = d.get("noteCount")
    pcs = d.get("pitchClassSet")
    kru = d.get("keyModeRunnerUp")  # dict or None
    return Region(
        measure_number    = d.get("measureNumber", 0),
        beat              = float(d.get("beat", 1.0)),
        start_tick        = int(d.get("startTick", 0)),
        end_tick          = int(d.get("endTick", 0)),
        duration          = float(d.get("duration", 0.0)),
        root_pc           = int(d.get("rootPitchClass", -1)),
        quality           = str(d.get("quality", "Unknown")),
        chord_symbol      = str(d.get("chordSymbol", "")),
        roman_numeral     = str(d.get("romanNumeral", "")),
        key               = str(d.get("key", "")),
        key_confidence    = float(d.get("keyConfidence", 0.0)),
        diatonic_to_key   = d.get("diatonicToKey"),
        alternatives      = list(d.get("alternatives", [])),
        chord_score       = float(cs)  if cs  is not None else None,
        chord_score_margin= float(csm) if csm is not None else None,
        bass_pc           = int(bpc)   if bpc is not None else None,
        bass_is_root      = bool(bir)  if bir is not None else None,
        note_count        = int(nc)    if nc  is not None else None,
        pitch_class_set   = int(pcs)   if pcs is not None else None,
        key_runner_up     = kru if isinstance(kru, dict) else None,
    )


def load_analysis(path: Path) -> tuple[dict, list[Region]]:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    regions = [_load_region(r) for r in data.get("regions", [])]
    return data, regions


# ══════════════════════════════════════════════════════════════════════════
# Quality normalisation (handles minor differences in string form)
# ══════════════════════════════════════════════════════════════════════════

_QUALITY_NORMALISE = {
    "HalfDiminished": "HalfDiminished",
    "halfdim":        "HalfDiminished",
    "half-diminished":"HalfDiminished",
    "dim7":           "Diminished",
    "Diminished":     "Diminished",
    "diminished":     "Diminished",
    "Augmented":      "Augmented",
    "augmented":      "Augmented",
    "Major":          "Major",
    "major":          "Major",
    "Minor":          "Minor",
    "minor":          "Minor",
    "Suspended2":     "Suspended2",
    "Suspended4":     "Suspended4",
    "Power":          "Power",
}

def _norm_quality(q: str) -> str:
    return _QUALITY_NORMALISE.get(q, q)


# ── Roman numeral normalisation ────────────────────────────────────────────
# Strip extensions (7, 9, M7, add6, …) to compare just the diatonic degree.
import re as _re
_RN_BASE_PATTERN = _re.compile(r"^(#|b)?(I{1,3}|IV|VI{0,2}|V{1,2}|ii{0,2}|iv|vi{0,2}|vii?|N|It|Fr|Ger)", _re.IGNORECASE)


def _rn_base(rn: str) -> str:
    """Extract only the diatonic degree part from a Roman numeral string."""
    m = _RN_BASE_PATTERN.match(rn.strip())
    return m.group(0).upper() if m else rn.upper()


# ══════════════════════════════════════════════════════════════════════════
# Alignment
# ══════════════════════════════════════════════════════════════════════════

def _overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    return max(0, min(a_end, b_end) - max(a_start, b_start))


def align_regions(ours: list[Region], theirs: list[Region]) -> list[tuple[Region, Optional[Region]]]:
    """
    For each of our regions, find the music21 region with the longest overlap.
    Returns a list of (ours_region, best_match_or_None) pairs.
    """
    aligned: list[tuple[Region, Optional[Region]]] = []

    for our in ours:
        our_dur = our.end_tick - our.start_tick
        best_overlap = 0
        best: Optional[Region] = None

        for their in theirs:
            ov = _overlap(our.start_tick, our.end_tick,
                          their.start_tick, their.end_tick)
            if ov > best_overlap:
                best_overlap = ov
                best = their

        # Only consider it aligned if the best overlap covers ≥ 50% of our region
        if best is not None and our_dur > 0 and best_overlap / our_dur >= 0.5:
            aligned.append((our, best))
        else:
            aligned.append((our, None))

    return aligned


# ══════════════════════════════════════════════════════════════════════════
# Classification
# ══════════════════════════════════════════════════════════════════════════

def _roots_match(ours: Region, theirs: Region) -> bool:
    return ours.root_pc == theirs.root_pc


def _quality_matches(ours: Region, theirs: Region) -> bool:
    return _norm_quality(ours.quality) == _norm_quality(theirs.quality)


def _chord_matches(ours: Region, theirs: Region) -> bool:
    return _roots_match(ours, theirs) and _quality_matches(ours, theirs)


def _rn_matches(ours: Region, theirs: Region) -> bool:
    return _rn_base(ours.roman_numeral) == _rn_base(theirs.roman_numeral)


def _key_matches(ours: Region, theirs: Region) -> bool:
    # Compare only the tonic name (strip "major" / "minor" variant)
    def _tonic(k: str) -> str:
        return k.split()[0].lower() if k else ""
    return _tonic(ours.key) == _tonic(theirs.key)


def _matches_alternative(theirs: Region, ours: Region) -> bool:
    """Returns True if music21's chord matches one of our alternatives (indices 1-2)."""
    for alt in ours.alternatives:
        if (int(alt.get("rootPitchClass", -99)) == theirs.root_pc
                and _norm_quality(alt.get("quality", "")) == _norm_quality(theirs.quality)):
            return True
    return False


def classify(ours: Region, theirs: Optional[Region]) -> ComparedRegion:
    if theirs is None:
        return ComparedRegion(ours=ours, theirs=theirs, category="unaligned")

    if _chord_matches(ours, theirs):
        if _rn_matches(ours, theirs):
            return ComparedRegion(ours=ours, theirs=theirs, category="full_agree")
        if _key_matches(ours, theirs):
            return ComparedRegion(ours=ours, theirs=theirs, category="chord_agree_rn_differs",
                                  notes=f"ours={ours.roman_numeral} theirs={theirs.roman_numeral}")
        return ComparedRegion(ours=ours, theirs=theirs, category="chord_agree_key_differs",
                              notes=f"ours_key={ours.key} theirs_key={theirs.key}")

    # Primary chord differs — check alternatives
    if _matches_alternative(theirs, ours):
        return ComparedRegion(ours=ours, theirs=theirs, category="near_agree",
                              notes="music21 matches our 2nd/3rd candidate")

    return ComparedRegion(
        ours=ours, theirs=theirs, category="chord_disagree",
        notes=(f"ours={ours.chord_symbol}({ours.root_pc}) "
               f"theirs={theirs.chord_symbol}({theirs.root_pc})")
    )


# ══════════════════════════════════════════════════════════════════════════
# Summary statistics
# ══════════════════════════════════════════════════════════════════════════

CATEGORIES = [
    "full_agree",
    "near_agree",
    "chord_agree_rn_differs",
    "chord_agree_key_differs",
    "chord_disagree",
    "unaligned",
]

def summarize(compared: list[ComparedRegion]) -> dict[str, int]:
    counts: dict[str, int] = {c: 0 for c in CATEGORIES}
    for cr in compared:
        counts[cr.category] = counts.get(cr.category, 0) + 1
    return counts


def agreement_rate(counts: dict[str, int]) -> float:
    """Fraction of regions that are full_agree or near_agree."""
    total = sum(counts.values())
    if total == 0:
        return 0.0
    agreed = counts.get("full_agree", 0) + counts.get("near_agree", 0)
    return agreed / total


def chord_identity_agreement(counts: dict[str, int]) -> tuple[int, float]:
    """Root + quality agreement regardless of key context.

    Returns (count, rate) where rate is over aligned regions only
    (excludes unaligned).  This is the most diagnostically meaningful
    figure when comparing against a tool that uses a different key-detection
    algorithm (e.g. music21's global Krumhansl-Schmuckler vs our local window).
    """
    total_aligned = sum(counts.values()) - counts.get("unaligned", 0)
    if total_aligned == 0:
        return 0, 0.0
    agreed = (counts.get("full_agree", 0)
              + counts.get("chord_agree_rn_differs", 0)
              + counts.get("chord_agree_key_differs", 0))
    return agreed, (agreed / total_aligned)


# ══════════════════════════════════════════════════════════════════════════
# Three-way comparison (ours vs music21 vs DCML)
# ══════════════════════════════════════════════════════════════════════════

THREE_WAY_CATEGORIES = [
    "all_agree",
    "dcml_ours_agree",
    "music21_dcml_agree",
    "all_differ",
    "no_dcml",
]

def three_way_classify(ours_root_pc: Optional[int],
                        theirs_root_pc: Optional[int],
                        dcml_root_pc: Optional[int]) -> str:
    """
    Classify a three-way comparison by root pitch class agreement.
    Returns one of:
      'all_agree'              — all three match
      'dcml_ours_agree'        — DCML + ours match, music21 differs
      'music21_dcml_agree'     — music21 + DCML match, we differ (genuine error)
      'all_differ'             — all three disagree
      'no_dcml'                — DCML data not available for this region
    """
    if dcml_root_pc is None:
        return 'no_dcml'
    if ours_root_pc is None or theirs_root_pc is None:
        return 'no_dcml'
    ours_dcml   = (ours_root_pc   == dcml_root_pc)
    theirs_dcml = (theirs_root_pc == dcml_root_pc)
    if ours_dcml and theirs_dcml:
        return 'all_agree'
    if ours_dcml and not theirs_dcml:
        return 'dcml_ours_agree'
    if theirs_dcml and not ours_dcml:
        return 'music21_dcml_agree'
    return 'all_differ'


def _extract_mode(key_str: str) -> str:
    """Extract mode abbreviation from key string like 'Gmaj', 'ADor', 'F#Mixolyd'."""
    m = _re2.match(r'^[A-G][#b]?(.+)$', key_str)
    return m.group(1) if m else key_str


def align_dcml_regions(ours_regions: list[Region],
                        dcml_regions: list) -> list[Optional[object]]:
    """
    For each of our regions, find the DCML region with matching measure number
    and beat within 0.5.  Returns a parallel list of DcmlRegion | None.
    """
    result: list[Optional[object]] = []
    for our in ours_regions:
        best = None
        best_dist = float('inf')
        for dr in dcml_regions:
            if dr.measure_number != our.measure_number:
                continue
            dist = abs(dr.beat - our.beat)
            if dist < best_dist and dist <= 0.5:
                best_dist = dist
                best = dr
        result.append(best)
    return result


# ══════════════════════════════════════════════════════════════════════════
# Direct two-way comparison: ours vs any DCML-format reference
# Used for corpora where music21 is not available (e.g. ABC Beethoven).
# ══════════════════════════════════════════════════════════════════════════

@dataclass
class DcmlDirectResult:
    """Result of a direct two-way comparison between our analysis and a DCML source."""
    ours:       Region
    dcml:       Optional[object]   # DcmlRegion | None
    category:   str                # 'dcml_agree' | 'dcml_disagree' | 'unaligned'


def compare_ours_vs_dcml_direct(
        ours_regions: list[Region],
        dcml_regions: list,
) -> list[DcmlDirectResult]:
    """
    Direct two-way comparison of our regions against DCML annotations.
    Each of our regions is matched to the DCML region with the closest
    measure+beat (within 0.5 beats).  Category:

      dcml_agree     — root pitch class matches
      dcml_disagree  — root pitch class differs (genuine analysis difference)
      unaligned      — no DCML region within tolerance
    """
    results = []
    for ours in ours_regions:
        best = None
        best_dist = float('inf')
        for dr in dcml_regions:
            if dr.measure_number != ours.measure_number:
                continue
            dist = abs(dr.beat - ours.beat)
            if dist < best_dist and dist <= 0.5:
                best_dist = dist
                best = dr

        if best is None:
            results.append(DcmlDirectResult(ours=ours, dcml=None, category='unaligned'))
        elif best.root_pc is not None and best.root_pc == ours.root_pc:
            results.append(DcmlDirectResult(ours=ours, dcml=best, category='dcml_agree'))
        else:
            results.append(DcmlDirectResult(ours=ours, dcml=best, category='dcml_disagree'))
    return results


def dcml_direct_summarize(results: list[DcmlDirectResult]) -> dict:
    """
    Aggregate counts and bassIsRoot breakdown for a direct two-way comparison.
    Returns a dict with keys: total, aligned, agree, disagree, unaligned,
    agree_pct, disagree_pct, align_pct, bass_is_root_in_disagree,
    bass_is_root_pct_of_disagree.
    """
    total     = len(results)
    aligned   = sum(1 for r in results if r.category != 'unaligned')
    agree     = sum(1 for r in results if r.category == 'dcml_agree')
    disagree  = sum(1 for r in results if r.category == 'dcml_disagree')
    unaligned = total - aligned

    bir_in_disagree = sum(
        1 for r in results
        if r.category == 'dcml_disagree' and r.ours.bass_is_root
    )

    return {
        'total':           total,
        'aligned':         aligned,
        'agree':           agree,
        'disagree':        disagree,
        'unaligned':       unaligned,
        'align_pct':       100 * aligned  / total    if total    else 0.0,
        'agree_pct':       100 * agree    / aligned  if aligned  else 0.0,
        'disagree_pct':    100 * disagree / aligned  if aligned  else 0.0,
        'bass_is_root_in_disagree':      bir_in_disagree,
        'bass_is_root_pct_of_disagree':  100 * bir_in_disagree / disagree if disagree else 0.0,
    }


def three_way_summarize(compared: list[ComparedRegion]) -> dict[str, int]:
    """Count three-way categories across all compared regions."""
    counts: dict[str, int] = {c: 0 for c in THREE_WAY_CATEGORIES}
    for cr in compared:
        counts[cr.three_way_cat] = counts.get(cr.three_way_cat, 0) + 1
    return counts


def mode_breakdown_of_errors(compared: list[ComparedRegion]) -> dict[str, int]:
    """
    For music21_dcml_agree cases, count occurrences by our inferred mode.
    High counts for non-Ionian/Aeolian modes suggest mode inference errors.
    """
    mode_counts: dict[str, int] = {}
    for cr in compared:
        if cr.three_way_cat == 'music21_dcml_agree':
            mode = _extract_mode(cr.ours.key)
            mode_counts[mode] = mode_counts.get(mode, 0) + 1
    return mode_counts


def bass_is_root_breakdown(compared: list[ComparedRegion]) -> Optional[dict[str, int]]:
    """
    For music21_dcml_agree (genuine error) and all_agree cases, count how many
    have bassIsRoot=True.  Returns None if no region has bassIsRoot data.
    """
    data: dict[str, dict] = {
        'music21_dcml_agree': {'bass_is_root': 0, 'bass_not_root': 0},
        'all_agree':          {'bass_is_root': 0, 'bass_not_root': 0},
    }
    has_data = False
    for cr in compared:
        if cr.ours.bass_is_root is None:
            continue
        has_data = True
        cat = cr.three_way_cat
        if cat not in data:
            continue
        key = 'bass_is_root' if cr.ours.bass_is_root else 'bass_not_root'
        data[cat][key] += 1
    return data if has_data else None


def note_count_breakdown(compared: list[ComparedRegion]) -> Optional[dict[int, dict[str, int]]]:
    """
    For music21_dcml_agree and all_agree cases, count by noteCount (distinct PCs).
    Returns {noteCount: {'music21_dcml_agree': N, 'all_agree': N}, ...}
    or None if no region has noteCount data.
    """
    counts: dict[int, dict[str, int]] = {}
    has_data = False
    for cr in compared:
        if cr.ours.note_count is None:
            continue
        has_data = True
        nc = cr.ours.note_count
        if nc not in counts:
            counts[nc] = {'music21_dcml_agree': 0, 'all_agree': 0}
        cat = cr.three_way_cat
        if cat in counts[nc]:
            counts[nc][cat] += 1
    return counts if has_data else None


def score_margin_by_category(
        compared: list[ComparedRegion]) -> Optional[dict[str, dict]]:
    """
    For music21_dcml_agree and all_agree cases, compute average chordScoreMargin.
    Narrow margin on errors = ambiguous (fix might help); wide margin = confident wrong.
    Returns {category: {'count': N, 'avg_margin': float, 'low_confidence_pct': float}}
    or None if no region has chordScoreMargin data.
    """
    buckets: dict[str, list[float]] = {
        'music21_dcml_agree': [],
        'all_agree': [],
    }
    has_data = False
    for cr in compared:
        if cr.ours.chord_score_margin is None:
            continue
        has_data = True
        if cr.three_way_cat in buckets:
            buckets[cr.three_way_cat].append(cr.ours.chord_score_margin)
    if not has_data:
        return None
    result: dict[str, dict] = {}
    for cat, margins in buckets.items():
        if not margins:
            result[cat] = {'count': 0, 'avg_margin': 0.0, 'low_confidence_pct': 0.0}
        else:
            avg = sum(margins) / len(margins)
            low_conf = sum(1 for m in margins if m < 0.5) / len(margins)
            result[cat] = {
                'count': len(margins),
                'avg_margin': avg,
                'low_confidence_pct': low_conf,
            }
    return result


# ══════════════════════════════════════════════════════════════════════════
# Plain-text report
# ══════════════════════════════════════════════════════════════════════════

def print_report(ours_meta: dict, m21_meta: dict,
                 compared: list[ComparedRegion]) -> None:
    counts = summarize(compared)
    total  = sum(counts.values())
    rate   = agreement_rate(counts)

    print(f"\n{'='*70}")
    print(f"  Source:        {ours_meta.get('source', '?')}")
    print(f"  Our key:       {ours_meta.get('detectedKey', '?')}")
    print(f"  music21 key:   {m21_meta.get('detectedKey', '?')}")
    print(f"  Our regions:   {len(compared)}")
    print(f"  m21 regions:   {len(m21_meta.get('regions', []))}")
    print(f"  Agreement:     {rate:.1%}")
    print(f"{'='*70}\n")

    for cat in CATEGORIES:
        n = counts[cat]
        bar = "#" * min(40, int(n * 40 / max(total, 1)))
        print(f"  {cat:<28} {n:>4}  {bar}")

    chord_id_count, chord_id_rate = chord_identity_agreement(counts)
    total_aligned = total - counts.get("unaligned", 0)
    print(f"\n  {'chord_identity_agree':<28} {chord_id_count:>4}"
          f"  ({chord_id_rate:.1%} of {total_aligned} aligned regions)")
    print()

    disagree = [cr for cr in compared if cr.category == "chord_disagree"]
    if disagree:
        print(f"  chord_disagree details ({len(disagree)} regions):\n")
        for cr in disagree[:20]:
            rn_ours  = cr.ours.roman_numeral
            rn_them  = cr.theirs.roman_numeral if cr.theirs else "—"
            print(f"    m{cr.ours.measure_number:<3} beat{cr.ours.beat:.1f}"
                  f"  {cr.ours.chord_symbol:<10} vs {cr.theirs.chord_symbol if cr.theirs else '—':<10}"
                  f"  RN: {rn_ours:<8} vs {rn_them}")
        if len(disagree) > 20:
            print(f"    … and {len(disagree) - 20} more")
        print()

    # Three-way summary (only if DCML data was supplied)
    tw_counts = three_way_summarize(compared)
    has_dcml = any(cr.three_way_cat != 'no_dcml' for cr in compared)
    if has_dcml:
        tw_total = sum(tw_counts[c] for c in THREE_WAY_CATEGORIES if c != 'no_dcml')
        print(f"  Three-way comparison (ours vs music21 vs DCML):\n")
        labels = {
            'all_agree':           'all_agree',
            'dcml_ours_agree':     'dcml_ours_agree (m21 wrong)',
            'music21_dcml_agree':  'music21_dcml_agree (we wrong)',
            'all_differ':          'all_differ',
            'no_dcml':             'no_dcml_data',
        }
        for cat in THREE_WAY_CATEGORIES:
            n = tw_counts[cat]
            denom = tw_total if cat != 'no_dcml' else sum(tw_counts.values())
            pct = n / max(denom, 1)
            print(f"    {labels[cat]:<35} {n:>4}  ({pct:.1%})")
        print()

        mode_bd = mode_breakdown_of_errors(compared)
        if mode_bd:
            print(f"  Mode breakdown of music21_dcml_agree (genuine errors):\n")
            for mode, cnt in sorted(mode_bd.items(), key=lambda x: -x[1]):
                diatonic = mode in ('maj', 'min')
                flag = '' if diatonic else '  <- non-diatonic'
                print(f"    {mode:<15} {cnt:>4}{flag}")
            print()

        bir = bass_is_root_breakdown(compared)
        if bir:
            print(f"  bassIsRoot breakdown (genuine errors vs all_agree):\n")
            for cat in ('music21_dcml_agree', 'all_agree'):
                bd = bir[cat]
                total = bd['bass_is_root'] + bd['bass_not_root']
                pct = bd['bass_is_root'] / max(total, 1)
                print(f"    {cat:<25}  bassIsRoot={bd['bass_is_root']}/{total} ({pct:.0%})")
            print()

        nc_bd = note_count_breakdown(compared)
        if nc_bd:
            print(f"  noteCount breakdown (genuine errors vs all_agree):\n")
            print(f"    {'NCs':<6} {'errors':>7} {'correct':>8}")
            for nc in sorted(nc_bd.keys()):
                e = nc_bd[nc].get('music21_dcml_agree', 0)
                a = nc_bd[nc].get('all_agree', 0)
                print(f"    {nc:<6} {e:>7} {a:>8}")
            print()

        sm = score_margin_by_category(compared)
        if sm:
            print(f"  chordScoreMargin (avg) per category:\n")
            for cat in ('music21_dcml_agree', 'all_agree'):
                d = sm.get(cat, {})
                if d.get('count', 0) == 0:
                    continue
                print(f"    {cat:<25}  avg={d['avg_margin']:.3f}"
                      f"  low-conf(<0.5)={d['low_confidence_pct']:.0%}")
            print()


# ══════════════════════════════════════════════════════════════════════════
# HTML report fragment (used by run_validation.py)
# ══════════════════════════════════════════════════════════════════════════

_CAT_COLOUR = {
    "full_agree":             "#2ecc71",
    "near_agree":             "#82e0aa",
    "chord_agree_rn_differs": "#f7dc6f",
    "chord_agree_key_differs":"#fad7a0",
    "chord_disagree":         "#e74c3c",
    "unaligned":              "#bdc3c7",
}


_THREE_WAY_COLOUR = {
    "all_agree":           "#2ecc71",
    "dcml_ours_agree":     "#f7dc6f",
    "music21_dcml_agree":  "#e74c3c",
    "all_differ":          "#e8a0e8",
    "no_dcml":             "#eeeeee",
}


def render_html_fragment(ours_meta: dict, m21_meta: dict,
                         compared: list[ComparedRegion]) -> str:
    """Return an HTML <section> block for one chorale's comparison."""
    counts = summarize(compared)
    rate   = agreement_rate(counts)
    source = ours_meta.get("source", "?")
    chord_id_count, chord_id_rate = chord_identity_agreement(counts)

    has_dcml = any(cr.three_way_cat != 'no_dcml' for cr in compared)
    tw_counts = three_way_summarize(compared)

    rows = []
    for cr in compared:
        colour = _CAT_COLOUR.get(cr.category, "#ffffff")
        their_sym = cr.theirs.chord_symbol if cr.theirs else "—"
        their_rn  = cr.theirs.roman_numeral if cr.theirs else "—"
        their_key = cr.theirs.key           if cr.theirs else "—"
        dcml_rn   = cr.dcml_region.roman_numeral if cr.dcml_region else "—"
        tw_colour = _THREE_WAY_COLOUR.get(cr.three_way_cat, "#eeeeee")
        dcml_cell = (f"<td>{dcml_rn}</td>"
                     f"<td style='background:{tw_colour}'>{cr.three_way_cat}</td>"
                     if has_dcml else "")
        rows.append(
            f"<tr style='background:{colour}'>"
            f"<td>{cr.ours.measure_number}</td>"
            f"<td>{cr.ours.beat:.1f}</td>"
            f"<td>{cr.ours.chord_symbol}</td>"
            f"<td>{cr.ours.roman_numeral}</td>"
            f"<td>{cr.ours.key}</td>"
            f"<td>{their_sym}</td>"
            f"<td>{their_rn}</td>"
            f"<td>{their_key}</td>"
            f"<td>{cr.category}</td>"
            f"<td>{cr.notes}</td>"
            f"{dcml_cell}"
            f"</tr>"
        )

    bar_cells = "".join(
        f"<td style='background:{_CAT_COLOUR[c]};width:{counts[c]}px;height:12px;' title='{c}: {counts[c]}'></td>"
        for c in CATEGORIES
    )

    tw_summary = ""
    if has_dcml:
        tw_total = sum(tw_counts[c] for c in THREE_WAY_CATEGORIES if c != 'no_dcml')
        tw_parts = " / ".join(
            f"{tw_counts[c]} {c}"
            for c in ['all_agree', 'dcml_ours_agree', 'music21_dcml_agree', 'all_differ']
        )
        tw_summary = f"&nbsp;&nbsp;<strong>3-way:</strong> {tw_parts} (of {tw_total})"

    dcml_header = ("<th>DCML RN</th><th>3-way</th>" if has_dcml else "")

    return f"""
<details id="{source}">
<summary>
  <strong>{source}</strong>
  &nbsp;&nbsp;agreement: <strong>{rate:.1%}</strong>
  &nbsp;&nbsp;chord-identity: <strong>{chord_id_rate:.1%}</strong>
  &nbsp;({counts['full_agree']} full + {counts['near_agree']} near / {sum(counts.values())} regions)
  {tw_summary}
  <table style='display:inline-table;border-collapse:collapse;vertical-align:middle'>
  <tr>{bar_cells}</tr></table>
</summary>
<table border='1' cellpadding='3' style='border-collapse:collapse;font-size:12px;margin:8px 0'>
<thead><tr>
  <th>Meas</th><th>Beat</th>
  <th>Our chord</th><th>Our RN</th><th>Our key</th>
  <th>m21 chord</th><th>m21 RN</th><th>m21 key</th>
  <th>Category</th><th>Notes</th>
  {dcml_header}
</tr></thead>
<tbody>{"".join(rows)}</tbody>
</table>
</details>
"""


# ══════════════════════════════════════════════════════════════════════════
# Public API used by run_validation.py
# ══════════════════════════════════════════════════════════════════════════

def compare_files(ours_path: Path, m21_path: Path,
                   dcml_regions: Optional[list] = None,
                   ) -> tuple[dict, dict, list[ComparedRegion]]:
    """Load and compare two analysis JSON files.  Returns (ours_meta, m21_meta, compared).

    If dcml_regions is supplied, each ComparedRegion will have dcml_region and
    three_way_cat populated.
    """
    ours_meta, ours_regions = load_analysis(ours_path)
    m21_meta,  m21_regions  = load_analysis(m21_path)

    aligned  = align_regions(ours_regions, m21_regions)
    compared = [classify(ours_r, their_r) for ours_r, their_r in aligned]

    if dcml_regions is not None:
        dcml_matches = align_dcml_regions(ours_regions, dcml_regions)
        for cr, dm in zip(compared, dcml_matches):
            cr.dcml_region = dm
            dcml_pc = dm.root_pc if dm is not None else None
            their_pc = cr.theirs.root_pc if cr.theirs is not None else None
            cr.three_way_cat = three_way_classify(cr.ours.root_pc, their_pc, dcml_pc)

    return ours_meta, m21_meta, compared


# ══════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare batch_analyze output against music21 output.",
    )
    parser.add_argument("ours",   help="Path to batch_analyze .ours.json")
    parser.add_argument("theirs", help="Path to .music21.json")
    parser.add_argument("--html", metavar="FILE",
                        help="Write an HTML report fragment to this file")
    args = parser.parse_args()

    ours_meta, m21_meta, compared = compare_files(Path(args.ours), Path(args.theirs))
    print_report(ours_meta, m21_meta, compared)

    if args.html:
        fragment = render_html_fragment(ours_meta, m21_meta, compared)
        Path(args.html).write_text(fragment, encoding="utf-8")
        print(f"HTML fragment written to {args.html}")


if __name__ == "__main__":
    main()
