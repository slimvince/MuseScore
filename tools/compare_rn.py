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

# Default When-in-Rome (Bach chorale rntxt) annotation root, resolved via
# dcml_parser.find_wir_file.  Used by the --wir-bach mode (BUILD 1).  Same path
# characterise_bir_false.py uses for its WiR reference.
WIR_BASE_DEFAULT = REPO_ROOT / "tools" / "dcml" / "when_in_rome"


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


# ── Key-context tonic parsing (BUILD 3, --key-breakdown) ──────────────────
# Ported verbatim from the ratified key_confound.py driver (dossier §1.5).  These
# resolve a (tonic_pc, is_major) pair for our key string and for a DCML key
# string so key_disagree can be split into the S1 (tonicization label-gap,
# =global ≠local) and S2 (genuine key error, ≠global) sub-tags.  No metric bucket
# is redefined — this is a sub-classification *within* the existing key_disagree
# bucket (cc_stage1d "orchestration is not a metric definition" basis).

# OI-126: single-sourced from dcml_parser._NOTE_TO_PC (were verbatim copies — one concern, three
# sites). _KB_NOTE_OURS is the uppercase note→pc map itself; _KB_NOTE_DCML is its lowercase-keyed
# view. Read-only lookup maps; values byte-identical to the former hand-written copies.
_KB_NOTE_OURS = dcml._NOTE_TO_PC
_KB_NOTE_DCML = {k.lower(): v for k, v in dcml._NOTE_TO_PC.items()}

_KB_DCML_KEY_RE = re.compile(r'^([a-gA-G])([#b]*)$')
# The mode suffix may contain uppercase letters (e.g. 'Dor', 'PhrygDom'), so the
# mode group is [A-Za-z]+ (was [a-z]+, which rejected those and mis-counted them as
# key-parse failures — carry-fix 2 Task 2, measurement fairness).
_KB_OURS_KEY_RE = re.compile(r'^([A-G])([#b]?)([A-Za-z]+)$')

# ── Grader-side mode-qualified local-key normalization (carry-fix 2 Task 2) ──
# The chain's local-key path emits mode-qualified names (Xharm/Xmel harmonic/melodic
# minor, XDor Dorian, XPhrygDom Phrygian-dominant) whose TONIC is correct but whose
# STRING the maj/min-only DCML key parser rejected → they were counted keyparse_fail,
# conflating key-inference quality with mode-label string parseability. This grader-only
# normalization maps a mode suffix to a major/minor identity so the key comparison scores
# key IDENTITY, not parseability. PRODUCTION EMITS THESE UNCHANGED.
#
# Mapping (mode-prefix, lower-cased → is_major), applied to every mode EXCEPT the five
# dominant-family modes handled by _parent_collection_reduction below:
#   • major-third modes maj / ion(ian) / lyd(ian) / mix(olydian)     → MAJOR
#   • every other (minor-third) mode → MINOR, i.e.:
#       - Xharm / Xmel  → X minor      (harmonic / melodic minor variants of the tonic)
#       - XDor           → X minor      — the PARENT-SIGNATURE CLASSIFICATION (declared choice):
#            Dorian is a minor-third mode; its natural-scale parent at the SAME tonic is the
#            minor key, and the key comparison uses only (tonic_pc, is_major). Classifying
#            D-Dorian as (D, minor) PRESERVES the correct tonic (the property the E0′ spot-
#            check verified) and keeps the whole minor-mode family on one side. The rejected
#            alternative — the RELATIVE-major signature (D-Dorian → F major) — was declined
#            because it MOVES the tonic and would break the tonic-correct property.
_KB_MAJOR_MODE_PREFIXES = ('maj', 'ion', 'lyd', 'mix')


def _mode_is_major(mode: str) -> bool:
    """Classify a local-key mode suffix as major (True) or minor (False), case-
    insensitively, per the carry-fix-2 Task-2 mapping documented above."""
    return mode.lower()[:3] in _KB_MAJOR_MODE_PREFIXES


# ── The five dominant-family modes: the PARENT-COLLECTION reduction ───────────
# OI-132, ruled by the user 2026-07-13. These five emitted modes are the ones whose TONIC TRIAD
# is major but whose PARENT COLLECTION is a minor scale — each is a rotation of a harmonic- or
# melodic-minor scale. They grade as the MINOR key of that parent collection, uniformly: an
# emitted "C#PhrygDom" (the Phrygian-dominant scale on C#) grades as F# minor, the key it is the
# dominant of. The prefix rule above cannot express this (it never moves the tonic), so these
# five are reduced here, ahead of it.
#
# Evidence (cc_mode_grading_adjudication_probe_report.md, read-only probe on all three presets):
# on the local-key column the parent-collection reading matches the DCML annotators on 67 % of
# the affected duration (54–100 % per mode); the tonic-triad reading matches 0 %. The affected
# duration is 0.48–0.71 % of the graded total.
#
# The mode-suffix spellings are ASCII-normalized before lookup because the chain emits the
# unicode accidentals ♭/♯ inside a mode name (e.g. "AMix♭6"). Modes NOT listed here keep the
# prefix rule verbatim, so no cell outside these five moves.
#
# suffix (ASCII-normalized) -> (semitones from the emitted tonic to the parent tonic, parent_is_major)
_KB_PARENT_COLLECTION_MODES = {
    "PhrygDom": (-7, False),   # 5th mode of harmonic minor
    "Mixb6":    (-7, False),   # 5th mode of melodic minor (Aeolian dominant)
    "Lydb7":    (-5, False),   # 4th mode of melodic minor (Lydian dominant)
    "Lyd+":     (-3, False),   # 3rd mode of melodic minor (Lydian augmented)
    "alt":      (+1, False),   # 7th mode of melodic minor (altered / super-Locrian)
}

_KB_OURS_TONIC_RE = re.compile(r'^([A-G][#b]?)(.*)$')


def _parent_collection_reduction(k: str) -> Optional[tuple[Optional[int], Optional[bool]]]:
    """(parent_tonic_pc, parent_is_major) if `k` names one of the five dominant-family modes;
    None if it does not (the caller then applies the prefix rule unchanged)."""
    m = _KB_OURS_TONIC_RE.match(k.strip().replace('♯', '#').replace('♭', 'b'))
    if not m:
        return None
    parent = _KB_PARENT_COLLECTION_MODES.get(m.group(2))
    if parent is None:
        return None
    offset, parent_is_major = parent
    return ((dcml._key_to_tonic_pc(m.group(1)) + offset) % 12, parent_is_major)


def _dcml_key_tonic(k: Optional[str]) -> tuple[Optional[int], Optional[bool]]:
    """DCML key string ('c', 'C', 'f#', 'bb', 'Ab') -> (tonic_pc, is_major).
    Uppercase letter = major, lowercase = minor.  (None, None) if unparseable."""
    if not k:
        return (None, None)
    m = _KB_DCML_KEY_RE.match(k.strip())
    if not m:
        return (None, None)
    letter, acc = m.group(1), m.group(2)
    pc = _KB_NOTE_DCML[letter.lower()] + acc.count('#') - acc.count('b')
    return (pc % 12, letter.isupper())


def _our_key_tonic(k: Optional[str]) -> tuple[Optional[int], Optional[bool]]:
    """Our key string ('Cmin', 'Cmaj', 'C#min', 'Bbmaj', 'Gdor', 'DDor', 'EPhrygDom')
    -> (tonic_pc, is_major).  THE ONE key-string reduction for grading — every graded
    surface reads it (a8 / the robust unit, c1_reliability and the calibration fit through
    it, the key-disagreement classifier, oracle_root_metric).

    Two rules, in order:
      1. the five dominant-family modes reduce to their PARENT COLLECTION's minor key
         (_parent_collection_reduction — OI-132, user-ruled 2026-07-13);
      2. every other mode suffix keeps its tonic and is normalized to a major/minor identity
         by _mode_is_major (carry-fix 2 Task 2), so a mode-qualified name with a correct tonic
         is not counted a parse failure.

    (None, None) only if the string is genuinely unparseable (empty / not <letter><acc?><mode>)."""
    if not k:
        return (None, None)
    parent = _parent_collection_reduction(k)
    if parent is not None:
        return parent
    m = _KB_OURS_KEY_RE.match(k.strip())
    if not m:
        return (None, None)
    letter, acc, mode = m.group(1), m.group(2), m.group(3)
    pc = _KB_NOTE_OURS[letter] + (1 if acc == '#' else -1 if acc == 'b' else 0)
    return (pc % 12, _mode_is_major(mode))


def key_disagree_subtag(ours_region, dcml_region) -> str:
    """Sub-classify a key_disagree pair (BUILD 3).  Returns:
      'eq_global' — our tonic+mode == DCML *global* key (S1: tonicization
                    label-gap; the degree differs only because DCML reads a
                    local tonic).  Unblocked by Stage 6.
      'ne_global' — our tonic+mode != DCML global key (S2: genuine key error).
                    Unblocked by Stage 4.
      'keyfail'   — our key string did not parse (the 2.4% caveat).  Counts as
                    ne_global for the S1/S2 split (the dossier "lumps into the
                    tonic✗ column"), but is reported separately so it is not
                    silently hidden in S2."""
    otc, omaj = _our_key_tonic(getattr(ours_region, 'key', None))
    if otc is None:
        return 'keyfail'
    gtc, gmaj = _dcml_key_tonic(getattr(dcml_region, 'global_key', None))
    if gtc is not None and (otc, omaj) == (gtc, gmaj):
        return 'eq_global'
    return 'ne_global'


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
        if cmp.roots_agree(ours_region.root_pc, dcml_region.root_pc):   # OI-52
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

    root_match    = cmp.roots_agree(ours_region.root_pc, dcml_region.root_pc)   # OI-52
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
    # ── Key-context sub-tag of the key_disagree bucket (BUILD 3). Populated
    # unconditionally; only consumed when --key-breakdown is requested. The
    # split is *within* key_disagree (kd_eq_global + kd_ne_global == key_disagree);
    # kd_keyfail is a sub-count of kd_ne_global, reported separately as the caveat.
    kd_eq_global:     int = 0           # S1: our key == DCML global (≠local)
    kd_ne_global:     int = 0           # S2: our key  != DCML global
    kd_keyfail:       int = 0           # subset of S2: our key did not parse
    # Corpus-wide our-key parse-failure count over ALL matched pairs (the
    # dossier's 2.4% = 239/10108 caveat); independent of the bucket.
    keyparse_fail:    int = 0

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
        self.kd_eq_global  += other.kd_eq_global
        self.kd_ne_global  += other.kd_ne_global
        self.kd_keyfail    += other.kd_keyfail
        self.keyparse_fail += other.keyparse_fail
        self.patterns.update(other.patterns)
        self.qe_quality_pairs.update(other.qe_quality_pairs)
        self.qe_rn_pairs.update(other.qe_rn_pairs)


def score_regions(ours_regions: list, dcml_regions: list) -> PieceStats:
    """Score one already-loaded (ours_regions, dcml_regions) pair into a
    PieceStats.  Shared body for both the TSV path (score_piece) and the WiR
    path (score_corpus_wir) — the *only* difference between corpora is how the
    DCML/WiR reference is loaded; the metric is byte-identical (reuse, not a new
    definition)."""
    matches = cmp.align_dcml_regions(ours_regions, dcml_regions,
                                     mode=cmp.DEFAULT_DCML_MATCH_MODE)

    stats = PieceStats(movements=1)
    for ours_r, dr in zip(ours_regions, matches):
        if dr is None:
            continue
        # root-agree denominator (parallel to compare_analyses.dcml_direct). The
        # `is not None` guard is the SCOREABILITY decision (a GT root that did not
        # resolve is out of the denominator); the equality itself is OI-52's one helper.
        if dr.root_pc is not None:
            stats.root_aligned += 1
            if cmp.roots_agree(ours_r.root_pc, dr.root_pc):
                stats.root_agree += 1
        pair = classify_pair(ours_r, dr)
        if pair is None:
            continue
        stats.matched += 1
        # Corpus-wide our-key parse-failure caveat (independent of bucket).
        if _our_key_tonic(getattr(ours_r, 'key', None))[0] is None:
            stats.keyparse_fail += 1
        if pair.category == "exact":
            stats.exact += 1
        elif pair.category == "partial":
            stats.partial += 1
        elif pair.category == "key_disagree":
            stats.key_disagree += 1
            tag = key_disagree_subtag(ours_r, dr)
            if tag == "eq_global":
                stats.kd_eq_global += 1
            elif tag == "keyfail":
                stats.kd_ne_global += 1
                stats.kd_keyfail += 1
            else:
                stats.kd_ne_global += 1
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


def score_piece(ours_path: Path, tsv_path: Path) -> Optional[PieceStats]:
    """Score one ours.json vs one DCML harmonies.tsv pair."""
    # OI-123: a corrupt ours.json/tsv drops the WHOLE piece from the aggregate with no counter.
    # Narrow the catch to the load-failure types and SURFACE the drop (name the piece) so a
    # systematic corruption cannot silently shrink the corpus.
    try:
        _, ours_regions = cmp.load_analysis(ours_path)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"[compare_rn] score_piece: DROPPED {ours_path.name} — ours load failed "
              f"({type(exc).__name__}: {exc})", file=sys.stderr)
        return None
    try:
        dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"[compare_rn] score_piece: DROPPED {ours_path.name} — tsv parse failed "
              f"({type(exc).__name__}: {exc})", file=sys.stderr)
        return None
    if not ours_regions or not dcml_regions:
        return None
    return score_regions(ours_regions, dcml_regions)


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


# ── Granularity-robust duration-weighted unit (BUILD 2) ────────────────────
# design §2: a scoring unit that is segmentation-invariant.  The grid is the
# union of region boundaries from both sides; over each half-open cell
# [t_i, t_{i+1}) BOTH sides are piecewise-constant by construction, so
# point-sampling at t_i and weighting by (t_{i+1} - t_i) is exact.  The reported
# number is the fraction of *musical time* in each bucket, which does not change
# when either side's segmentation is refined (a split cell carries the same two
# labels).  This is added ALONGSIDE the region-count metric — it does not
# redefine the existing buckets.

@dataclass
class GridStats:
    pieces:       int = 0
    scored_dur:   int = 0           # Σ duration of cells that yielded a scoreable pair
    unscored_dur: int = 0           # Σ duration of cells with no scoreable pair (gap/unaligned)
    bucket_dur:   Counter = None    # type: ignore[assignment]  bucket -> Σ duration

    def __post_init__(self):
        if self.bucket_dur is None:
            self.bucket_dur = Counter()

    def add(self, other: "GridStats") -> None:
        self.pieces       += other.pieces
        self.scored_dur   += other.scored_dur
        self.unscored_dur += other.unscored_dur
        self.bucket_dur.update(other.bucket_dur)


def _active_index_at(spans: list, tick: int) -> Optional[int]:
    """Index of the half-open span [s, e) containing `tick`, or None.  Spans are
    non-overlapping by construction (region streams / DCML row spans); the first
    containing span is returned."""
    for i, (s, e) in enumerate(spans):
        if e > s and s <= tick < e:
            return i
    return None


def grid_score_regions(ours_regions: list, dcml_regions: list) -> GridStats:
    """Duration-weighted, segmentation-invariant scoring of one already-loaded
    (ours_regions, dcml_regions) pair (design §2).  Reuses
    ``compare_analyses._dcml_time_spans`` for the DCML-side tick spans (the same
    span arithmetic ``align_dcml_regions`` uses) and the reused ``classify_pair``
    for the per-cell verdict."""
    gs = GridStats()
    if not ours_regions or not dcml_regions:
        return gs
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    dcml_spans = cmp._dcml_time_spans(ours_regions, dcml_regions)

    bounds: set[int] = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s)
            bounds.add(e)
    for (s, e) in dcml_spans:
        if s >= 0 and e > s:
            bounds.add(s)
            bounds.add(e)
    if len(bounds) < 2:
        return gs

    gs.pieces = 1
    grid = sorted(bounds)
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        w = t1 - t0
        if w <= 0:                       # coincident boundaries -> zero-width cell
            continue
        oi = _active_index_at(ours_spans, t0)
        di = _active_index_at(dcml_spans, t0)
        if oi is None or di is None:
            gs.unscored_dur += w
            continue
        pair = classify_pair(ours_regions[oi], dcml_regions[di])
        if pair is None:
            gs.unscored_dur += w
            continue
        gs.bucket_dur[pair.category] += w
        gs.scored_dur += w
    return gs


def grid_score_piece_tsv(ours_path: Path, tsv_path: Path) -> Optional[GridStats]:
    """Grid-score one ours.json vs one DCML harmonies.tsv pair."""
    # OI-123: narrow + surface the whole-piece drop (see score_piece).
    try:
        _, ours_regions = cmp.load_analysis(ours_path)
        dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"[compare_rn] grid_score_piece_tsv: DROPPED {ours_path.name} "
              f"({type(exc).__name__}: {exc})", file=sys.stderr)
        return None
    if not ours_regions or not dcml_regions:
        return None
    return grid_score_regions(ours_regions, dcml_regions)


def grid_score_corpus_tsv(ours_dir: Path, tsv_dir: Path) -> Optional[GridStats]:
    if not ours_dir.is_dir() or not tsv_dir.is_dir():
        return None
    agg = GridStats()
    for p in sorted(ours_dir.glob("*.ours.json")):
        stem = p.name.replace(".ours.json", "")
        tsv = _find_tsv(tsv_dir, stem)
        if tsv is None:
            continue
        g = grid_score_piece_tsv(p, tsv)
        if g is not None:
            agg.add(g)
    return agg if agg.pieces > 0 else None


# ── Bach When-in-Rome corpus mode (BUILD 1) ────────────────────────────────
# Promote the headroom dossier's Bach-WiR wiring to a committed mode, parallel to
# --corpus / --cross-corpus.  ORCHESTRATION ONLY over already-pinned functions:
# dcml_parser.find_wir_file (resolve the analysis.txt for a stem), parse_rntxt_file
# (parse to DcmlRegions), align_dcml_regions (align), classify_pair (classify).
# Zero change to any metric definition.  Bach chorales have no harmonies.tsv —
# their human annotation is When-in-Rome rntxt — so --cross-corpus structurally
# excludes them; this mode closes that 326-chorale coverage hole.

@dataclass
class WirCoverage:
    total:   int = 0   # all *.ours.json in the dir
    covered: int = 0   # those with a resolvable WiR analysis.txt that parsed


def score_corpus_wir(ours_dir: Path, wir_base: Path,
                     ) -> Optional[tuple[PieceStats, GridStats, WirCoverage]]:
    """Score a directory of *.ours.json against When-in-Rome Bach rntxt.

    Returns (region_count_stats, grid_stats, coverage) or None if the dir has no
    usable ours files.  The coverage denominator (covered/total) is reported
    explicitly — only ~326/353 gate chorales have a WiR annotation at all; the
    27 without can never be scored against human ground truth and must never be
    silently folded into a /353 division (design §1.2 coverage fact)."""
    if not ours_dir.is_dir():
        return None
    ours_files = sorted(ours_dir.glob("*.ours.json"))
    if not ours_files:
        return None
    cov = WirCoverage(total=len(ours_files))
    agg = PieceStats()
    grid_agg = GridStats()
    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            _, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue
        cov.covered += 1
        agg.add(score_regions(ours_regions, wir_regions))
        grid_agg.add(grid_score_regions(ours_regions, wir_regions))
    if agg.movements == 0:
        return None
    return agg, grid_agg, cov


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


def format_grid_report(label: str, gs: GridStats) -> str:
    """Render the granularity-robust duration-weighted block (BUILD 2)."""
    tot = gs.scored_dur
    lines: list[str] = []
    lines.append(f"=== {label} — granularity-robust (duration-weighted, "
                 f"union-of-boundaries grid) ===")
    lines.append(f"  pieces:            {gs.pieces}")
    lines.append(f"  scored duration:   {tot} ticks")
    lines.append(f"  unscored duration: {gs.unscored_dur} ticks"
                 f"   (cells with no scoreable pair)")
    rn_agree = gs.bucket_dur['exact'] + gs.bucket_dur['partial']
    lines.append(f"  rn_agree:          {_pct(rn_agree, tot):5.1f}%"
                 f"  ({rn_agree}/{tot} ticks)")
    for k in RN_CATEGORIES:
        lines.append(f"    {k:<16}: {_pct(gs.bucket_dur[k], tot):5.1f}%"
                     f"  ({gs.bucket_dur[k]}/{tot})")
    return "\n".join(lines)


def format_key_breakdown(label: str, stats: PieceStats) -> str:
    """Render the key-context sub-tag of key_disagree (BUILD 3, L1 instrument).

    Splits key_disagree into S1 (=global ≠local, tonicization label-gap — the
    Stage-6 axis) and S2 (≠global, genuine key error — the Stage-4 axis).  The
    our-key parse-failure caveat is reported, never hidden in a bucket."""
    kd = stats.key_disagree
    s1 = stats.kd_eq_global
    s2 = stats.kd_ne_global
    kf = stats.kd_keyfail
    lines: list[str] = []
    lines.append(f"=== {label} — KEY-CONTEXT BREAKDOWN of key_disagree "
                 f"(Stage-4 L1 instrument) ===")
    lines.append(f"  key_disagree total: {kd}")
    lines.append(f"  S1  =global ≠local  (tonicization label-gap — Stage 6): "
                 f"{s1:>6}  ({_pct(s1, kd):5.1f}% of key_disagree)")
    lines.append(f"  S2  ≠global         (genuine key error      — Stage 4): "
                 f"{s2:>6}  ({_pct(s2, kd):5.1f}% of key_disagree)")
    lines.append(f"  [caveat] our-key parse failures: "
                 f"{stats.keyparse_fail}/{stats.matched} "
                 f"({_pct(stats.keyparse_fail, stats.matched):.1f}% of matched); "
                 f"the {kf} within key_disagree fall into S2 (the dossier's "
                 f"\"tonic✗ column\").")
    return "\n".join(lines)


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
    ap.add_argument("--wir-bach", metavar="DIR",
                    help="Score a directory of *.ours.json against When-in-Rome "
                         "Bach rntxt (the 326-chorale gate set that --cross-corpus "
                         "excludes because chorales have no harmonies.tsv).  "
                         "Reports the covered/total coverage denominator explicitly.")
    ap.add_argument("--wir-base", metavar="DIR", default=str(WIR_BASE_DEFAULT),
                    help=f"When-in-Rome annotation root (default: {WIR_BASE_DEFAULT}).")
    ap.add_argument("--top-patterns", type=int, default=10,
                    help="Number of disagreement patterns to show per block")
    ap.add_argument("--quality-breakdown", action="store_true",
                    help="After the summary, print breakdown tables of the "
                         "quality_disagree bucket: ours_quality→dcml_quality pairs, "
                         "top ours_rn→dcml_rn pairs, and per-corpus shares.")
    ap.add_argument("--granularity-robust", action="store_true",
                    help="After the region-count summary, print the duration-weighted "
                         "union-of-boundaries unit (segmentation-invariant; design §2).  "
                         "Added alongside — the region-count buckets are unchanged.")
    ap.add_argument("--key-breakdown", action="store_true",
                    help="After the summary, split key_disagree into S1 (=global "
                         "≠local, tonicization label-gap — Stage 6) and S2 (≠global, "
                         "genuine key error — Stage 4); reports the our-key parse-fail caveat.")
    ap.add_argument("--output",
                    help="Also write the full report text to this file")
    args = ap.parse_args()

    out_lines: list[str] = []

    if args.wir_bach:
        ours_dir = Path(args.wir_bach)
        result = score_corpus_wir(ours_dir, Path(args.wir_base))
        if result is None:
            print(f"No usable *.ours.json with WiR coverage in {ours_dir}",
                  file=sys.stderr)
            return 1
        stats, grid, cov = result
        label = f"WiR-Bach {ours_dir.name}"
        out_lines.append(f"=== {label} : When-in-Rome (DCML-only, region-centric) ===")
        out_lines.append(f"  WiR coverage: {cov.covered}/{cov.total} ours files "
                         f"({_pct(cov.covered, cov.total):.1f}%)  "
                         f"— {cov.total - cov.covered} have no WiR annotation")
        out_lines.append("")
        out_lines.append(format_report(label, stats, args.top_patterns))
        if args.granularity_robust:
            out_lines.append("")
            out_lines.append(format_grid_report(label, grid))
        if args.key_breakdown:
            out_lines.append("")
            out_lines.append(format_key_breakdown(label, stats))

    elif args.cross_corpus:
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
        if args.key_breakdown and agg.matched > 0:
            out_lines.append("")
            out_lines.append(format_key_breakdown("CROSS-CORPUS AGGREGATE", agg))
        if args.granularity_robust:
            grid_agg = GridStats()
            for label, ours_dir in corpora.items():
                tsv_dir = REPO_ROOT / CROSS_CORPORA[label]["tsv_dir"]
                g = grid_score_corpus_tsv(ours_dir, tsv_dir)
                if g is not None:
                    grid_agg.add(g)
            if grid_agg.pieces > 0:
                out_lines.append("")
                out_lines.append(format_grid_report("CROSS-CORPUS AGGREGATE", grid_agg))

    elif args.corpus:
        if not args.tsv_dir:
            print("ERROR: --corpus requires --tsv-dir", file=sys.stderr)
            return 2
        stats = score_corpus(Path(args.corpus), Path(args.tsv_dir))
        if stats is None:
            print("No usable pairs.", file=sys.stderr)
            return 1
        label = Path(args.corpus).name
        out_lines.append(format_report(label, stats, args.top_patterns))
        if args.granularity_robust:
            grid = grid_score_corpus_tsv(Path(args.corpus), Path(args.tsv_dir))
            if grid is not None:
                out_lines.append("")
                out_lines.append(format_grid_report(label, grid))
        if args.key_breakdown:
            out_lines.append("")
            out_lines.append(format_key_breakdown(label, stats))

    elif args.ours and args.tsv:
        stats = score_piece(Path(args.ours), Path(args.tsv))
        if stats is None:
            print("Could not score the pair.", file=sys.stderr)
            return 1
        label = Path(args.ours).name
        out_lines.append(format_report(label, stats, args.top_patterns))
        if args.granularity_robust:
            grid = grid_score_piece_tsv(Path(args.ours), Path(args.tsv))
            if grid is not None:
                out_lines.append("")
                out_lines.append(format_grid_report(label, grid))
        if args.key_breakdown:
            out_lines.append("")
            out_lines.append(format_key_breakdown(label, stats))

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
