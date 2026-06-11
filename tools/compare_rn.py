#!/usr/bin/env python3
"""
compare_rn.py — Roman-numeral-level comparison of batch_analyze output against
DCML harmonies.tsv ground truth.

The existing tools/compare_analyses.py compares root pitch classes and emits
``root_agree`` — that misses quality, inversion, and figured-bass errors that
the BIR metric is blind to.  This script is the Roman-numeral analogue.

For each (our region, DCML annotation) pair matched by tick overlap
(reusing the lenient-OR 50% logic from compare_analyses), the pair is
classified as one of:

  exact            — full RN string matches (after normalisation)
  partial          — root_pc + degree case match, but inversion/extension differs
  key_disagree     — root_pc matches, coarse chord quality matches, but scale
                     degree case differs (key/mode detection error, e.g. V→I)
  quality_disagree — root_pc matches but the coarse chord quality genuinely
                     differs (true chord-quality error, e.g. Maj→Dom7)
  root_err         — root_pc disagrees (same set as BIR=false fraction)

``rn_agree`` = (exact + partial) / matched.

Comparison surface
------------------
Ours:  romanNumeral field, e.g. ``I6``, ``IVM7``, ``vi65``, ``V7``, ``ø7``.
DCML:  the ``chord`` column from harmonies.tsv (stored as
       DcmlRegion.chord_symbol after parse_abc_harmonies_file), e.g.
       ``I6``, ``V(4)``, ``ii%65``, ``vii%7/V``, ``viio6``.

Normalisation applied to both sides before comparison:
  * Strip leading key prefix ``[X:]`` or modulation marker ``→`` from ours.
  * Replace DCML half-diminished sigil ``%`` with our ``ø``.
  * Strip parenthetical figured-bass tokens like ``(2)``, ``(4)``, ``(#11)``
    — our analyzer does not emit these, so they would systematically force
    exact-match failures.  Pairs that differ only by such a token still
    count as ``exact`` after stripping.

Quality is encoded in case (uppercase Roman = major-coloured degree,
lowercase = minor-coloured), so the comparison is case-sensitive on the
degree base.  Suffixes (figures, extensions) have no case ambiguity.

Usage
-----
Single piece:
    python tools/compare_rn.py <ours.json> <dcml.tsv>

One corpus directory:
    python tools/compare_rn.py --corpus DIR --tsv-dir DIR

Cross-corpus (10 non-Bach corpora):
    python tools/compare_rn.py --cross-corpus tools/reports/live_20260603

Add --top-patterns N to control the disagreement-pattern list length.
Add --output FILE to also write the full report there.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Force UTF-8 stdout/stderr so the half-dim sigil 'ø' and other non-cp1252
# characters present in normalised RN strings can be printed on Windows.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import dcml_parser as dcml


REPO_ROOT = Path(__file__).resolve().parent.parent


# ── Per-corpus configuration (same shape as rerun_dcml_comparison.CROSS_CORPORA)
CROSS_CORPORA = OrderedDict([
    ("dvorak",       {"ours_glob": "dvorak_*",       "tsv_dir": "tools/dcml/dvorak_silhouettes/harmonies"}),
    ("chopin",       {"ours_glob": "chopin_*",       "tsv_dir": "tools/dcml/chopin_mazurkas/harmonies"}),
    ("corelli",      {"ours_glob": "corelli_*",      "tsv_dir": "tools/dcml/corelli/harmonies"}),
    ("mozart",       {"ours_glob": "mozart_*",       "tsv_dir": "tools/dcml/mozart_piano_sonatas/harmonies"}),
    ("schumann",     {"ours_glob": "schumann_*",     "tsv_dir": "tools/dcml/schumann_kinderszenen/harmonies"}),
    ("tchaikovsky",  {"ours_glob": "tchaikovsky_*",  "tsv_dir": "tools/dcml/tchaikovsky_seasons/harmonies"}),
    ("grieg",        {"ours_glob": "grieg_*",        "tsv_dir": "tools/dcml/grieg_lyric_pieces/harmonies"}),
    ("beethoven",    {"ours_glob": "beethoven",      "tsv_dir": "tools/dcml/ABC/harmonies"}),
    ("cpe_bach",     {"ours_glob": "cpe_bach_*",     "tsv_dir": "tools/dcml/cpe_bach_keyboard/harmonies"}),
    ("bach_suites",  {"ours_glob": "bach_suites_*",  "tsv_dir": "tools/dcml/bach_en_fr_suites/harmonies"}),
])


# ── Normalisation ─────────────────────────────────────────────────────────

_KEY_PREFIX_RE = re.compile(r'^\s*\[[^\]]+\]\s*')
_MOD_PREFIX_RE = re.compile(r'^\s*[→>]+\s*')
_PAREN_FIG_RE  = re.compile(r'\([^)]*\)')

_DEGREE_RE = re.compile(
    r'^(?P<acc>[#b]?)'
    r'(?P<deg>VII|VI|IV|V|III|II|I|vii|vi|iv|v|iii|ii|i)'
)

# Italian augmented-sixth token ("It", "It6", "It6/ii").  Its leading 'I' would
# otherwise be captured by _DEGREE_RE as the tonic degree (Stage 2.2-ii F-2).
_IT6_RE = re.compile(r'^It(?:\d|/|$)')


def normalise_rn(rn: str) -> str:
    """Strip noise that would block string equality without losing the
    quality (case-encoded) or inversion/extension content."""
    if not rn:
        return ""
    s = rn
    s = _KEY_PREFIX_RE.sub('', s)
    s = _MOD_PREFIX_RE.sub('', s)
    s = s.replace('%', 'ø')          # DCML half-dim sigil → ours
    s = _PAREN_FIG_RE.sub('', s)     # drop figured-bass parens (we don't emit them)
    return s.strip()


def split_rn(rn: str) -> Optional[tuple[str, str, str]]:
    """Return (accidental, degree-base, suffix) or None if unparseable.

    The degree-base keeps its case (the quality marker).  Both inputs are
    expected to be already normalised via ``normalise_rn``.
    """
    if not rn:
        return None
    # Augmented-sixth Italian token ("It6", "It", "It6/ii") begins with the
    # letter 'I' that the degree regex would otherwise mis-read as a major
    # tonic.  Route it to the unparseable -> root-only fallback, matching how
    # Ger / Fr / N (which the degree regex already rejects) are handled.  We do
    # NOT invent a root mapping; the DCML-side root_pc is owned by dcml_parser.
    # (Stage 2.2-ii F-2; dossier §4.)
    if _IT6_RE.match(rn):
        return None
    m = _DEGREE_RE.match(rn)
    if not m:
        return None
    return m.group('acc'), m.group('deg'), rn[m.end():]


def _same_quality(ours_deg: str, dcml_deg: str) -> bool:
    """Case-sensitive degree comparison (case = quality colour)."""
    return ours_deg == dcml_deg


# Inversion figures that indicate a seventh chord (vs. triad).
_SEVENTH_FIGURES = {"7", "65", "43", "42", "2"}


def extract_quality(rn_norm: str) -> str:
    """Return a coarse chord-quality token for a normalised Roman numeral.

    Tokens: Maj, Min, Dom7, Maj7, Min7, MinMaj7, Dim, Dim7, HalfDim, HalfDim7,
    Aug, Aug7, ? (unparseable).  Tonicisation markers (``/V`` etc.) are
    discarded — only the primary degree's quality is considered.
    """
    parts = split_rn(rn_norm)
    if parts is None:
        return "?"
    _, deg, suffix = parts
    if not deg:
        return "?"
    is_upper = deg[0].isupper()
    # Drop secondary-degree marker; quality lives on the primary numeral.
    s = suffix.split('/', 1)[0]

    # Diminished is keyed off BOTH the degree-sign '°' (U+00B0) and the letter
    # 'o' that DCML and our analyzer actually emit (viio6 / iio65).  Before
    # Stage 2.2-ii only '°' was recognized, so 'o'-diminished chords were
    # mis-coarse-classified as Min / Min7 (F-1; dossier §4).  The 'ø' half-dim
    # check runs first below, so a half-dim 'ø' token is not swallowed here.
    has_dim    = ('°' in s) or ('o' in s)
    has_hdim   = 'ø' in s
    has_aug    = '+' in s
    has_majm7  = bool(re.search(r'(M7|maj7|M9|maj9)', s))
    digits     = re.findall(r'\d+', s)
    has_7thfig = any(d in _SEVENTH_FIGURES for d in digits)
    has_seventh = has_majm7 or has_7thfig

    if has_hdim:
        return "HalfDim7" if has_seventh else "HalfDim"
    if has_dim:
        return "Dim7" if has_seventh else "Dim"
    if has_aug:
        return "Aug7" if has_seventh else "Aug"
    if is_upper:
        if has_majm7:
            return "Maj7"
        if has_seventh:
            return "Dom7"
        return "Maj"
    else:
        if has_majm7:
            return "MinMaj7"
        if has_seventh:
            return "Min7"
        return "Min"


# ── Per-pair classification ───────────────────────────────────────────────

# Reported in this fixed order.
RN_CATEGORIES = ("exact", "partial", "key_disagree", "quality_disagree", "root_err")


@dataclass
class RnPair:
    """One matched (ours, DCML) region pair."""
    measure:      int
    beat:         float
    ours_rn_raw:  str
    dcml_rn_raw:  str
    ours_rn:      str          # normalised
    dcml_rn:      str          # normalised
    ours_root_pc: int
    dcml_root_pc: Optional[int]
    category:     str          # one of RN_CATEGORIES


def classify_pair(ours_region, dcml_region) -> Optional[RnPair]:
    """Classify a matched ours/DCML pair.  Returns None if the pair cannot
    be scored — e.g. DCML has no resolvable root_pc or one side has no
    parseable degree."""
    if dcml_region is None:
        return None
    if dcml_region.root_pc is None:
        return None

    ours_raw = ours_region.roman_numeral or ""
    dcml_raw = dcml_region.chord_symbol or ""

    ours_norm = normalise_rn(ours_raw)
    dcml_norm = normalise_rn(dcml_raw)

    ours_parts = split_rn(ours_norm)
    dcml_parts = split_rn(dcml_norm)

    # If either side is unparseable, fall back to root-only classification.
    if ours_parts is None or dcml_parts is None:
        if ours_region.root_pc == dcml_region.root_pc:
            # Root agrees, but we can't compare RN strings — treat as partial
            # (unknown extension/quality difference) so we don't claim exact.
            cat = "partial"
        else:
            cat = "root_err"
        return RnPair(
            measure=ours_region.measure_number,
            beat=ours_region.beat,
            ours_rn_raw=ours_raw,
            dcml_rn_raw=dcml_raw,
            ours_rn=ours_norm,
            dcml_rn=dcml_norm,
            ours_root_pc=ours_region.root_pc,
            dcml_root_pc=dcml_region.root_pc,
            category=cat,
        )

    root_match    = (ours_region.root_pc == dcml_region.root_pc)
    quality_match = _same_quality(ours_parts[1], dcml_parts[1])

    if root_match and quality_match:
        # Same root + same case = same broad quality; check the full string.
        if ours_norm == dcml_norm:
            cat = "exact"
        else:
            cat = "partial"
    elif root_match and not quality_match:
        o_ext_q = extract_quality(ours_norm)
        d_ext_q = extract_quality(dcml_norm)
        cat = "key_disagree" if o_ext_q == d_ext_q else "quality_disagree"
    else:
        cat = "root_err"

    return RnPair(
        measure=ours_region.measure_number,
        beat=ours_region.beat,
        ours_rn_raw=ours_raw,
        dcml_rn_raw=dcml_raw,
        ours_rn=ours_norm,
        dcml_rn=dcml_norm,
        ours_root_pc=ours_region.root_pc,
        dcml_root_pc=dcml_region.root_pc,
        category=cat,
    )


# ── Per-piece aggregation ─────────────────────────────────────────────────

@dataclass
class PieceStats:
    movements:        int = 0
    matched:          int = 0
    exact:            int = 0
    partial:          int = 0
    key_disagree:     int = 0
    quality_disagree: int = 0
    root_err:         int = 0
    patterns:         Counter = None    # type: ignore[assignment]
    # quality_disagree-only pattern counters (populated unconditionally; only
    # consumed when --quality-breakdown is requested).
    qe_quality_pairs: Counter = None    # type: ignore[assignment]
    qe_rn_pairs:      Counter = None    # type: ignore[assignment]
    # For cross-checking against compare_analyses' root_agree on the same
    # input — we accept both 'aligned-but-no-rn' regions (counted toward
    # root_agree only) and aligned RN-scoreable ones.
    root_aligned:     int = 0           # aligned with DCML root_pc resolved
    root_agree:       int = 0

    def __post_init__(self):
        if self.patterns is None:
            self.patterns = Counter()
        if self.qe_quality_pairs is None:
            self.qe_quality_pairs = Counter()
        if self.qe_rn_pairs is None:
            self.qe_rn_pairs = Counter()

    def add(self, other: "PieceStats") -> None:
        self.movements        += other.movements
        self.matched          += other.matched
        self.exact            += other.exact
        self.partial          += other.partial
        self.key_disagree     += other.key_disagree
        self.quality_disagree += other.quality_disagree
        self.root_err         += other.root_err
        self.root_aligned += other.root_aligned
        self.root_agree   += other.root_agree
        self.patterns.update(other.patterns)
        self.qe_quality_pairs.update(other.qe_quality_pairs)
        self.qe_rn_pairs.update(other.qe_rn_pairs)


def score_piece(ours_path: Path, tsv_path: Path) -> Optional[PieceStats]:
    """Score one ours.json vs one DCML harmonies.tsv pair."""
    try:
        _, ours_regions = cmp.load_analysis(ours_path)
    except Exception:
        return None
    try:
        dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
    except Exception:
        return None
    if not ours_regions or not dcml_regions:
        return None

    matches = cmp.align_dcml_regions(ours_regions, dcml_regions,
                                     mode=cmp.DEFAULT_DCML_MATCH_MODE)

    stats = PieceStats(movements=1)
    for ours_r, dr in zip(ours_regions, matches):
        if dr is None:
            continue
        # root-agree denominator (parallel to compare_analyses.dcml_direct)
        if dr.root_pc is not None:
            stats.root_aligned += 1
            if dr.root_pc == ours_r.root_pc:
                stats.root_agree += 1
        pair = classify_pair(ours_r, dr)
        if pair is None:
            continue
        stats.matched += 1
        if pair.category == "exact":
            stats.exact += 1
        elif pair.category == "partial":
            stats.partial += 1
        elif pair.category == "key_disagree":
            stats.key_disagree += 1
        elif pair.category == "quality_disagree":
            stats.quality_disagree += 1
            o_q = extract_quality(pair.ours_rn)
            d_q = extract_quality(pair.dcml_rn)
            stats.qe_quality_pairs[(o_q, d_q)] += 1
            stats.qe_rn_pairs[
                (pair.ours_rn or "<empty>", pair.dcml_rn or "<empty>")
            ] += 1
        elif pair.category == "root_err":
            stats.root_err += 1
        if pair.category != "exact":
            key = (pair.ours_rn or "<empty>", pair.dcml_rn or "<empty>")
            stats.patterns[key] += 1
    return stats


# ── Per-corpus aggregation ────────────────────────────────────────────────

def _find_tsv(tsv_dir: Path, stem: str) -> Optional[Path]:
    for cand in (f"{stem}.harmonies.tsv", f"{stem}.tsv"):
        p = tsv_dir / cand
        if p.exists():
            return p
    return None


def score_corpus(ours_dir: Path, tsv_dir: Path) -> Optional[PieceStats]:
    if not ours_dir.is_dir() or not tsv_dir.is_dir():
        return None
    ours_files = sorted(ours_dir.glob("*.ours.json"))
    if not ours_files:
        return None
    agg = PieceStats()
    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        tsv  = _find_tsv(tsv_dir, stem)
        if tsv is None:
            continue
        s = score_piece(p, tsv)
        if s is not None:
            agg.add(s)
    return agg if agg.movements > 0 else None


def discover_corpora(root: Path) -> "OrderedDict[str, Path]":
    """For a live_<timestamp> directory, find the per-corpus ours subdirectory."""
    out: "OrderedDict[str, Path]" = OrderedDict()
    for label, cfg in CROSS_CORPORA.items():
        ours_dir = None
        for cand in sorted(root.glob(cfg["ours_glob"])):
            if cand.is_dir():
                ours_dir = cand
                break
        if ours_dir is not None:
            out[label] = ours_dir
    return out


# ── Reporting ─────────────────────────────────────────────────────────────

def _pct(num: int, denom: int) -> float:
    return 100.0 * num / denom if denom else 0.0


def format_report(label: str, stats: PieceStats, top_n: int = 10) -> str:
    """Render the per-corpus report block."""
    m = stats.matched
    lines: list[str] = []
    lines.append(f"=== {label} ===")
    lines.append(f"  movements:       {stats.movements}")
    lines.append(f"  matched regions: {m}")
    rn_agree = stats.exact + stats.partial
    lines.append(f"  rn_agree:        {_pct(rn_agree, m):5.1f}%  ({rn_agree}/{m})")
    lines.append(f"  root_agree:      {_pct(stats.root_agree, stats.root_aligned):5.1f}%"
                 f"  ({stats.root_agree}/{stats.root_aligned}  — compare_analyses parity)")
    lines.append(f"    exact_match:   {_pct(stats.exact, m):5.1f}%  ({stats.exact}/{m})")
    lines.append(f"    partial_match: {_pct(stats.partial, m):5.1f}%  ({stats.partial}/{m})"
                 f"   (root + quality agree, inversion/extension differs)")
    lines.append(f"  key_disagree:    {_pct(stats.key_disagree, m):5.1f}%  ({stats.key_disagree}/{m})"
                 f"   (root agrees, quality agrees, scale degree wrong — key detection error)")
    lines.append(f"  quality_disagree:{_pct(stats.quality_disagree, m):5.1f}%  ({stats.quality_disagree}/{m})"
                 f"   (root agrees, quality differs — true chord-quality error)")
    lines.append(f"  root_err:        {_pct(stats.root_err, m):5.1f}%  ({stats.root_err}/{m})"
                 f"   (root disagrees — same set as BIR=false fraction)")

    if stats.patterns:
        lines.append("")
        lines.append(f"  Top disagreement patterns (up to {top_n}):")
        lines.append(f"    {'ours':<14} {'-> DCML':<18} count")
        for (o, d), n in stats.patterns.most_common(top_n):
            lines.append(f"    {o:<14} {('-> ' + d):<18} {n}")
    return "\n".join(lines)


def _format_quality_breakdown(
    agg: PieceStats,
    per_corpus: "OrderedDict[str, PieceStats]",
    top_rn: int = 20,
) -> list[str]:
    """Render the three quality_disagree breakdown tables for --quality-breakdown."""
    lines: list[str] = []
    total_qe = agg.quality_disagree
    lines.append("=== QUALITY DISAGREE BREAKDOWN (root correct, quality differs) ===")
    lines.append(f"  total quality_disagree: {total_qe}  ({_pct(total_qe, agg.matched):.1f}% of matched)")
    lines.append("")
    lines.append("Quality disagree breakdown (ours_quality → dcml_quality):")
    lines.append(f"  {'ours_quality':<12}  {'dcml_quality':<14}  {'count':>7}  {'% of qd':>8}")
    for (o, d), n in agg.qe_quality_pairs.most_common():
        lines.append(f"  {o:<12}  -> {d:<11}  {n:>7}  {_pct(n, total_qe):>7.1f}%")

    lines.append("")
    lines.append(f"Top quality-disagree Roman numeral pairs (ours → DCML, top {top_rn}):")
    lines.append(f"  {'ours_rn':<14}  {'dcml_rn':<16}  {'count':>7}")
    for (o, d), n in agg.qe_rn_pairs.most_common(top_rn):
        lines.append(f"  {o:<14}  -> {d:<13}  {n:>7}")

    lines.append("")
    lines.append("Quality disagrees by corpus:")
    lines.append(f"  {'corpus':<14}  {'quality_dis':>11}  {'matched':>8}  {'% matched':>10}  {'% all qd':>9}")
    for label, st in per_corpus.items():
        pct_matched = _pct(st.quality_disagree, st.matched)
        pct_all     = _pct(st.quality_disagree, total_qe)
        lines.append(f"  {label:<14}  {st.quality_disagree:>11}  {st.matched:>8}  {pct_matched:>9.1f}%  {pct_all:>8.1f}%")
    return lines


# ── CLI ───────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Roman-numeral comparison of ours vs DCML.")
    ap.add_argument("ours",      nargs="?", help="Single ours.json (with --tsv)")
    ap.add_argument("tsv",       nargs="?", help="Matching DCML harmonies.tsv")
    ap.add_argument("--corpus",
                    help="Score one corpus: directory of *.ours.json files")
    ap.add_argument("--tsv-dir",
                    help="Directory of *.harmonies.tsv files (used with --corpus)")
    ap.add_argument("--cross-corpus",
                    help="Score all configured corpora rooted at this live_<ts> dir")
    ap.add_argument("--top-patterns", type=int, default=10,
                    help="Number of disagreement patterns to show per block")
    ap.add_argument("--quality-breakdown", action="store_true",
                    help="After the summary, print breakdown tables of the "
                         "quality_disagree bucket: ours_quality→dcml_quality pairs, "
                         "top ours_rn→dcml_rn pairs, and per-corpus shares.")
    ap.add_argument("--output",
                    help="Also write the full report text to this file")
    args = ap.parse_args()

    out_lines: list[str] = []

    if args.cross_corpus:
        root = Path(args.cross_corpus).resolve()
        if not root.is_dir():
            print(f"ERROR: {root} is not a directory", file=sys.stderr)
            return 2
        corpora = discover_corpora(root)
        out_lines.append(f"cross-corpus root: {root}")
        out_lines.append(f"corpora found:     {', '.join(corpora.keys()) or '(none)'}")
        out_lines.append("")
        agg = PieceStats()
        per_corpus: "OrderedDict[str, PieceStats]" = OrderedDict()
        for label, ours_dir in corpora.items():
            cfg = CROSS_CORPORA[label]
            tsv_dir = REPO_ROOT / cfg["tsv_dir"]
            stats = score_corpus(ours_dir, tsv_dir)
            if stats is None:
                out_lines.append(f"=== {label} ===")
                out_lines.append(f"  (no usable .ours/DCML pairs in {ours_dir})")
                out_lines.append("")
                continue
            out_lines.append(format_report(label, stats, args.top_patterns))
            out_lines.append("")
            agg.add(stats)
            per_corpus[label] = stats
        if agg.movements > 0:
            out_lines.append(format_report("CROSS-CORPUS AGGREGATE", agg,
                                            args.top_patterns))
        if args.quality_breakdown and agg.matched > 0:
            out_lines.append("")
            out_lines.extend(_format_quality_breakdown(agg, per_corpus))

    elif args.corpus:
        if not args.tsv_dir:
            print("ERROR: --corpus requires --tsv-dir", file=sys.stderr)
            return 2
        stats = score_corpus(Path(args.corpus), Path(args.tsv_dir))
        if stats is None:
            print("No usable pairs.", file=sys.stderr)
            return 1
        out_lines.append(format_report(Path(args.corpus).name, stats,
                                        args.top_patterns))

    elif args.ours and args.tsv:
        stats = score_piece(Path(args.ours), Path(args.tsv))
        if stats is None:
            print("Could not score the pair.", file=sys.stderr)
            return 1
        out_lines.append(format_report(Path(args.ours).name, stats,
                                        args.top_patterns))

    else:
        ap.print_help()
        return 2

    text = "\n".join(out_lines)
    print(text)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
