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


def _rn_base_cased(rn: str) -> str:
    """Extract the diatonic degree part, PRESERVING case.

    DCML and our analyzer both encode chord quality in the Roman-numeral
    case (uppercase = major, lowercase = minor; e.g. DCML "v" = natural-minor
    v, DCML "V" = common-practice raised V).  This sibling of `_rn_base`
    preserves that distinction so a degree-with-quality comparison can be
    made — without losing it to the case-collapsing `.upper()` that
    `_rn_base` applies for music21 alignment.

    Extensions and inversion figures (7, 65, 42, °7, ø7, add6, etc.) are
    stripped — only the bare degree token is kept.  Empty input returns
    an empty string; an unparseable input is passed through stripped.
    """
    s = rn.strip()
    if not s:
        return ""
    m = _RN_BASE_PATTERN.match(s)
    return m.group(0) if m else s


# ══════════════════════════════════════════════════════════════════════════
# Alignment
# ══════════════════════════════════════════════════════════════════════════
# OI-125: measurement-decision tolerances — ONE named home per instrument, with provenance.
# These are hand-set with a documented rationale but NOT independently derived / oracle-established
# (#19); re-derivation is later (Stage-5-adjacent) work, flagged per constant. They are NOT fittable
# scorer constants (→ NOT param_manifest.json rows) — they are grading conventions of the comparator.
# NOTE: the robust A-8 grid (compare_rn.grid_score_regions) UNIONS boundaries and needs no overlap
# threshold, so these govern only the batch-stop / secondary-metric / oracle-root alignment.
ALIGN_OVERLAP_FRACTION = 0.5   # a (ours, DCML/m21) pair aligns iff overlap ≥ this fraction of EITHER
                               # duration (lenient OR). [hand-set; re-derivation flagged]
ALIGN_BEAT_DISTANCE_TOL = 0.5  # measure-anchored mode only: max |beat| distance for a match, in beats.
                               # [hand-set; re-derivation flagged]
EXTRAPOLATION_BEATS_PER_MEASURE = 4  # beats/measure ASSUMED when extrapolating a DCML tick beyond the
                               # anchored measures (the rntxt/WiR path lacks abs_tick) — a silent 4/4
                               # approximation for non-4/4 meters. [hand-set; re-derivation flagged]


def _overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    return max(0, min(a_end, b_end) - max(a_start, b_start))


def align_regions(ours: list[Region], theirs: list[Region]) -> list[tuple[Region, Optional[Region]]]:
    """
    For each of our regions, find the `theirs` region with the longest tick
    overlap.  A pair is aligned iff the overlap covers ≥50% of *either*
    region's duration (lenient OR — a sub-beat region fully contained in a
    longer `theirs` region stays aligned, and a `theirs` region fully
    contained in our region also stays aligned).
    """
    aligned: list[tuple[Region, Optional[Region]]] = []

    for our in ours:
        our_dur = our.end_tick - our.start_tick
        best_overlap = 0
        best: Optional[Region] = None
        best_their_dur = 0

        for their in theirs:
            ov = _overlap(our.start_tick, our.end_tick,
                          their.start_tick, their.end_tick)
            if ov > best_overlap:
                best_overlap = ov
                best = their
                best_their_dur = their.end_tick - their.start_tick

        if best is not None and our_dur > 0 and best_overlap > 0 \
                and ((best_overlap / our_dur) >= ALIGN_OVERLAP_FRACTION
                     or (best_their_dur > 0 and best_overlap / best_their_dur >= ALIGN_OVERLAP_FRACTION)):
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


# ── DCML region matching ──────────────────────────────────────────────────
# Two matching modes are supported:
#   "time-overlap" (default): convert DCML (measure, beat) onsets to ticks
#       using the analyzer regions' (measure, beat, start_tick) anchors, treat
#       each DCML region as spanning [start_tick, next_dcml.start_tick), and
#       match each of our regions to the DCML region with the maximum tick
#       overlap.  A pair is aligned iff the overlap covers ≥50% of *either*
#       region's duration (lenient OR — a sub-beat region fully contained in
#       a longer DCML region is still aligned).
#   "beat-snap" (legacy): match by smallest |Δbeat| within the same measure,
#       tolerance 0.5 beats.  Retained as a backward-compat flag.
#
# The time-overlap mode is needed because Iters 72/73/83 introduced sub-beat
# region boundaries that DCML's beat-anchored annotations cannot reach, so
# beat-snap silently flagged genuinely-correct regions as unaligned.

DEFAULT_DCML_MATCH_MODE = "time-overlap"


def _median(values: list[float]) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    n = len(s)
    return s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2])


def _infer_ticks_per_beat(ours_regions: list[Region]) -> float:
    """Estimate ticks-per-beat from analyzer region durations (median)."""
    samples = [
        (r.end_tick - r.start_tick) / r.duration
        for r in ours_regions
        if r.duration > 0 and r.end_tick > r.start_tick
    ]
    return _median(samples) if samples else 480.0


def _build_measure_anchors(ours_regions: list[Region],
                            tpb: float) -> dict[int, int]:
    """
    For each measure_number observed in the analyzer regions, derive the tick
    at beat 1 of that measure.  Uses the region with the smallest beat in
    each measure as anchor:
        measure_start_tick = region.start_tick - (region.beat - 1) * tpb.
    """
    anchors: dict[int, tuple[int, float]] = {}
    for r in ours_regions:
        cur = anchors.get(r.measure_number)
        if cur is None or r.beat < cur[1]:
            anchors[r.measure_number] = (r.start_tick, r.beat)
    return {m: int(round(at - (ab - 1) * tpb)) for m, (at, ab) in anchors.items()}


def _dcml_tick_for(measure: int, beat: float,
                   measure_starts: dict[int, int],
                   tpb: float) -> Optional[int]:
    """Convert a DCML (measure, beat) onset to a tick.  Linearly interpolates
    across measures with no analyzer-region anchor."""
    if not measure_starts:
        return None
    if measure in measure_starts:
        return int(round(measure_starts[measure] + (beat - 1) * tpb))
    prev_m = max((m for m in measure_starts if m < measure), default=None)
    next_m = min((m for m in measure_starts if m > measure), default=None)
    if prev_m is not None and next_m is not None and next_m > prev_m:
        prev_t = measure_starts[prev_m]
        next_t = measure_starts[next_m]
        tick_per_measure = (next_t - prev_t) / (next_m - prev_m)
        m_start = prev_t + (measure - prev_m) * tick_per_measure
        return int(round(m_start + (beat - 1) * tpb))
    if prev_m is not None:
        return int(round(measure_starts[prev_m]
                         + (measure - prev_m) * EXTRAPOLATION_BEATS_PER_MEASURE * tpb
                         + (beat - 1) * tpb))
    if next_m is not None:
        return int(round(measure_starts[next_m]
                         - (next_m - measure) * EXTRAPOLATION_BEATS_PER_MEASURE * tpb
                         + (beat - 1) * tpb))
    return None


def _dcml_time_spans(ours_regions: list[Region],
                     dcml_regions: list) -> list[tuple[int, int]]:
    """
    Compute (start_tick, end_tick) for each DCML region.  Each region's
    end_tick is the start_tick of the next DCML region (or the piece's end
    tick).  Spans where the start tick cannot be resolved come back as (-1,-1).
    """
    if not dcml_regions or not ours_regions:
        return []
    tpb = _infer_ticks_per_beat(ours_regions)
    measure_starts = _build_measure_anchors(ours_regions, tpb)
    piece_end = max(r.end_tick for r in ours_regions) if ours_regions else 0
    # Prefer the exact absolute tick the TSV parser derived from the
    # `quarterbeats` column (audit P0/L4.1) — it is pickup-aware and needs no
    # measure-anchor reconstruction.  Fall back to the measure-anchor rebuild
    # for sources without abs_tick (the rntxt / When-in-Rome path, which has no
    # absolute-quarter column).
    starts: list[Optional[int]] = [
        dr.abs_tick if getattr(dr, 'abs_tick', None) is not None
        else _dcml_tick_for(dr.measure_number, dr.beat, measure_starts, tpb)
        for dr in dcml_regions
    ]
    spans: list[tuple[int, int]] = []
    for i, s in enumerate(starts):
        if s is None:
            spans.append((-1, -1))
            continue
        end = piece_end
        for j in range(i + 1, len(starts)):
            if starts[j] is not None and starts[j] > s:
                end = starts[j]
                break
        spans.append((s, max(end, s)))
    return spans


def _best_dcml_match_by_overlap(our: Region,
                                 dcml_regions: list,
                                 dcml_spans: list[tuple[int, int]],
                                 ) -> Optional[object]:
    """Return the DCML region with maximum tick overlap with `our`, aligned
    iff the overlap covers ≥50% of *either* region's duration (lenient OR)."""
    our_dur = our.end_tick - our.start_tick
    if our_dur <= 0:
        return None
    best = None
    best_ov = 0
    best_their_dur = 0
    for dr, (ds, de) in zip(dcml_regions, dcml_spans):
        if ds < 0 or de <= ds:
            continue
        ov = _overlap(our.start_tick, our.end_tick, ds, de)
        if ov > best_ov:
            best_ov = ov
            best = dr
            best_their_dur = de - ds
    if best is None or best_ov == 0:
        return None
    if (best_ov / our_dur) >= ALIGN_OVERLAP_FRACTION \
            or (best_their_dur > 0 and best_ov / best_their_dur >= ALIGN_OVERLAP_FRACTION):
        return best
    return None


def align_dcml_regions(ours_regions: list[Region],
                        dcml_regions: list,
                        mode: str = DEFAULT_DCML_MATCH_MODE,
                        ) -> list[Optional[object]]:
    """
    For each of our regions, return the matching DCML region (or None).

    mode = "time-overlap" (default): best tick-overlap match, lenient OR-50%.
    mode = "beat-snap"   (legacy):   smallest |Δbeat| within same measure,
                                     tolerance 0.5 beats.
    """
    if mode == "time-overlap":
        spans = _dcml_time_spans(ours_regions, dcml_regions)
        if not spans:
            return [None] * len(ours_regions)
        return [_best_dcml_match_by_overlap(our, dcml_regions, spans)
                for our in ours_regions]

    # ── beat-snap (legacy) ────────────────────────────────────────────────
    result: list[Optional[object]] = []
    for our in ours_regions:
        best = None
        best_dist = float('inf')
        for dr in dcml_regions:
            if dr.measure_number != our.measure_number:
                continue
            dist = abs(dr.beat - our.beat)
            if dist < best_dist and dist <= ALIGN_BEAT_DISTANCE_TOL:
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
    # Case-sensitive Roman-numeral-degree agreement (e.g. DCML "V" vs ours
    # "V"); None when there is no aligned DCML row or either side's RN is
    # empty / unparseable.  Reported independently of `category` — a chord
    # whose root_pc matches DCML may still have a different RN base (e.g.
    # our key context differs from DCML's local key), and conversely the
    # RN base may match while root_pc differs (uncommon, usually a fifths
    # offset that the histogram-based root match happens to forgive).
    rn_agree:   Optional[bool] = None


def compare_ours_vs_dcml_direct(
        ours_regions: list[Region],
        dcml_regions: list,
        mode: str = DEFAULT_DCML_MATCH_MODE,
) -> list[DcmlDirectResult]:
    """
    Direct two-way comparison of our regions against DCML annotations.
    Uses `align_dcml_regions(mode=...)` to pair each of our regions with at
    most one DCML region.  Category:

      dcml_agree     — root pitch class matches
      dcml_disagree  — root pitch class differs (genuine analysis difference)
      unaligned      — no DCML region matched

    `rn_agree` is populated alongside `category` whenever an aligned DCML
    region with a non-empty Roman numeral is found; the comparison is on the
    case-sensitive degree base (see `_rn_base_cased`).
    """
    matches = align_dcml_regions(ours_regions, dcml_regions, mode=mode)
    results: list[DcmlDirectResult] = []
    for ours, dr in zip(ours_regions, matches):
        rn_agree: Optional[bool] = None
        if dr is not None:
            dcml_rn = _rn_base_cased(getattr(dr, 'roman_numeral', '') or '')
            ours_rn = _rn_base_cased(ours.roman_numeral or '')
            if dcml_rn and ours_rn:
                rn_agree = (dcml_rn == ours_rn)
        if dr is None:
            results.append(DcmlDirectResult(ours=ours, dcml=None, category='unaligned',
                                             rn_agree=rn_agree))
        elif dr.root_pc is not None and dr.root_pc == ours.root_pc:
            results.append(DcmlDirectResult(ours=ours, dcml=dr, category='dcml_agree',
                                             rn_agree=rn_agree))
        else:
            results.append(DcmlDirectResult(ours=ours, dcml=dr, category='dcml_disagree',
                                             rn_agree=rn_agree))
    return results


# ── DCML-anchored matching ────────────────────────────────────────────────
# Inverts the iteration: walks every DCML annotation and picks the single
# best of our regions for it (largest tick overlap).  Answers the question
# "for each chord DCML annotates, did we get it right?" — closer in intent
# to what the old beat-snap numbers tried to measure, but without the
# sampling bias (every DCML annotation counts, not just the ones where one
# of our regions happens to land near the beat).

@dataclass
class DcmlAnchoredResult:
    """One result row per DCML annotation."""
    dcml:       object                 # DcmlRegion
    ours:       Optional[Region]       # best-overlapping ours region (or None)
    category:   str                    # 'dcml_agree' | 'dcml_disagree' | 'no_ours_coverage'
    # Case-sensitive Roman-numeral-degree agreement (e.g. DCML "V" vs ours
    # "V").  None when either side's RN is empty / unparseable, or when no
    # ours region overlaps this DCML annotation.  Reported independently of
    # `category` so the two signals can be cross-tabulated.
    rn_agree:   Optional[bool] = None


def compare_dcml_anchored(
        ours_regions: list[Region],
        dcml_regions: list,
) -> list[DcmlAnchoredResult]:
    """
    DCML-anchored time-overlap comparison.  For each DCML annotation, find
    the ours region with the largest tick overlap of its span and compare
    root pitch class.  No alignment threshold is applied — every DCML
    annotation is counted, and 'no_ours_coverage' is only emitted when
    literally zero overlap exists.

    The `rn_agree` field on each row is populated with the case-sensitive
    Roman-numeral-degree agreement (see `_rn_base_cased`) whenever there is
    ours coverage and both sides have a parseable Roman numeral.
    """
    if not ours_regions or not dcml_regions:
        return [
            DcmlAnchoredResult(dcml=dr, ours=None, category='no_ours_coverage')
            for dr in dcml_regions
        ]
    spans = _dcml_time_spans(ours_regions, dcml_regions)
    out: list[DcmlAnchoredResult] = []
    for dr, (ds, de) in zip(dcml_regions, spans):
        if ds < 0 or de <= ds:
            out.append(DcmlAnchoredResult(dcml=dr, ours=None,
                                           category='no_ours_coverage'))
            continue
        best = None
        best_ov = 0
        for r in ours_regions:
            ov = _overlap(r.start_tick, r.end_tick, ds, de)
            if ov > best_ov:
                best_ov = ov
                best = r
        if best is None or best_ov == 0:
            out.append(DcmlAnchoredResult(dcml=dr, ours=None,
                                           category='no_ours_coverage'))
            continue
        rn_agree: Optional[bool] = None
        dcml_rn = _rn_base_cased(getattr(dr, 'roman_numeral', '') or '')
        ours_rn = _rn_base_cased(best.roman_numeral or '')
        if dcml_rn and ours_rn:
            rn_agree = (dcml_rn == ours_rn)
        if dr.root_pc is not None and dr.root_pc == best.root_pc:
            out.append(DcmlAnchoredResult(dcml=dr, ours=best,
                                           category='dcml_agree',
                                           rn_agree=rn_agree))
        else:
            out.append(DcmlAnchoredResult(dcml=dr, ours=best,
                                           category='dcml_disagree',
                                           rn_agree=rn_agree))
    return out


def dcml_anchored_summarize(results: list[DcmlAnchoredResult]) -> dict:
    """Aggregate counts for a DCML-anchored comparison.  Denominator is the
    set of DCML annotations whose root pitch class could be resolved (some
    DCML rows are e.g. @none / unparseable and have root_pc=None).

    Roman-numeral agreement is reported as a separate metric alongside
    root-pc agreement.  The RN denominator (`rn_scoreable`) is the set of
    DCML annotations that have ours coverage AND both sides resolve a
    parseable degree base.  The two cross-tabulation buckets
    `rn_agree_in_root_disagree` and `rn_disagree_in_root_agree` give a quick
    read on whether the analyzer is naming the degree right while picking
    the wrong root_pc (a key-context error rather than a chord-identity
    error), or vice versa.
    """
    total              = len(results)
    no_ours_coverage   = sum(1 for r in results if r.category == 'no_ours_coverage')
    with_ours_coverage = total - no_ours_coverage
    agree              = sum(1 for r in results if r.category == 'dcml_agree')
    disagree           = sum(1 for r in results if r.category == 'dcml_disagree')
    # Only count rows where DCML resolved a root_pc; some annotations
    # (@none, unparseable applied chords) have root_pc=None and are skipped.
    scoreable = sum(1 for r in results
                    if r.dcml is not None and r.dcml.root_pc is not None
                    and r.category != 'no_ours_coverage')
    bir_in_disagree = sum(
        1 for r in results
        if r.category == 'dcml_disagree' and r.ours is not None
        and r.ours.bass_is_root
    )
    # ── Roman numeral agreement ──────────────────────────────────────────
    rn_scoreable = sum(1 for r in results if r.rn_agree is not None)
    rn_agree     = sum(1 for r in results if r.rn_agree is True)
    rn_disagree  = sum(1 for r in results if r.rn_agree is False)
    rn_agree_in_root_disagree = sum(
        1 for r in results
        if r.rn_agree is True and r.category == 'dcml_disagree'
    )
    rn_disagree_in_root_agree = sum(
        1 for r in results
        if r.rn_agree is False and r.category == 'dcml_agree'
    )
    return {
        'total_dcml':           total,
        'with_ours_coverage':   with_ours_coverage,
        'scoreable':            scoreable,
        'agree':                agree,
        'disagree':             disagree,
        'no_ours_coverage':     no_ours_coverage,
        'coverage_pct':         100 * with_ours_coverage / total if total else 0.0,
        'agree_pct':            100 * agree / scoreable if scoreable else 0.0,
        'bass_is_root_in_disagree':     bir_in_disagree,
        'bass_is_root_pct_of_disagree': 100 * bir_in_disagree / disagree if disagree else 0.0,
        'rn_scoreable':                 rn_scoreable,
        'rn_agree':                     rn_agree,
        'rn_disagree':                  rn_disagree,
        'rn_agree_pct':                 100 * rn_agree / rn_scoreable if rn_scoreable else 0.0,
        'rn_agree_in_root_disagree':    rn_agree_in_root_disagree,
        'rn_disagree_in_root_agree':    rn_disagree_in_root_agree,
    }


def dcml_direct_summarize(results: list[DcmlDirectResult]) -> dict:
    """
    Aggregate counts and bassIsRoot breakdown for a direct two-way comparison.
    Returns a dict with keys: total, aligned, agree, disagree, unaligned,
    agree_pct, disagree_pct, align_pct, bass_is_root_in_disagree,
    bass_is_root_pct_of_disagree.

    Roman-numeral agreement is reported as a separate metric alongside
    root-pc agreement (denominator = aligned rows with a parseable RN base
    on both sides).
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

    rn_scoreable = sum(1 for r in results if r.rn_agree is not None)
    rn_agree     = sum(1 for r in results if r.rn_agree is True)
    rn_disagree  = sum(1 for r in results if r.rn_agree is False)
    rn_agree_in_root_disagree = sum(
        1 for r in results
        if r.rn_agree is True and r.category == 'dcml_disagree'
    )
    rn_disagree_in_root_agree = sum(
        1 for r in results
        if r.rn_agree is False and r.category == 'dcml_agree'
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
        'rn_scoreable':                  rn_scoreable,
        'rn_agree':                      rn_agree,
        'rn_disagree':                   rn_disagree,
        'rn_agree_pct':                  100 * rn_agree / rn_scoreable if rn_scoreable else 0.0,
        'rn_agree_in_root_disagree':     rn_agree_in_root_disagree,
        'rn_disagree_in_root_agree':     rn_disagree_in_root_agree,
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
                   dcml_match_mode: str = DEFAULT_DCML_MATCH_MODE,
                   ) -> tuple[dict, dict, list[ComparedRegion]]:
    """Load and compare two analysis JSON files.  Returns (ours_meta, m21_meta, compared).

    If dcml_regions is supplied, each ComparedRegion will have dcml_region and
    three_way_cat populated.  `dcml_match_mode` selects the DCML alignment
    strategy ("time-overlap" by default; pass "beat-snap" for legacy behavior).
    """
    ours_meta, ours_regions = load_analysis(ours_path)
    m21_meta,  m21_regions  = load_analysis(m21_path)

    aligned  = align_regions(ours_regions, m21_regions)
    compared = [classify(ours_r, their_r) for ours_r, their_r in aligned]

    if dcml_regions is not None:
        dcml_matches = align_dcml_regions(ours_regions, dcml_regions,
                                          mode=dcml_match_mode)
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
