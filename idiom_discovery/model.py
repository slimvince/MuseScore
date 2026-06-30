"""Common data model + low-prejudice encoding for the harmonic-idiom-discovery pipeline.

See cowork_idiom_discovery_design.md (the spec). Core principle: a chord is encoded as a
KEY-NORMALIZED, line-of-fifths root + a canonical quality — no function/genre labels. The
clustering input is built from these tokens (extract.py); naming is post-hoc (discover.py).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Line of fifths.  We keep roots as a signed integer = position on the line of
# fifths RELATIVE TO THE (local) tonic.  0 = tonic, +1 = dominant (a fifth up),
# -1 = subdominant, +2 = supertonic, ...  This is spelling-aware (tpc) and, being
# tonic-relative, already key-normalized.  DCML's `root` column is exactly this.
# ---------------------------------------------------------------------------

# note name (no octave) -> position on the line of fifths, C = 0
_BASE = {"F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5}


def name_to_fifths(name: str) -> Optional[int]:
    """'C'->0, 'G'->1, 'F#'->6, 'Bb'->-2, 'Db'->-5.  None if unparseable.

    Used by the symbol-based parsers (McGill, iRb, ChoCo, Nottingham).  DCML does
    not need it (its `root` is already a tonic-relative fifth)."""
    if not name:
        return None
    letter = name[0].upper()
    if letter not in _BASE:
        return None
    f = _BASE[letter]
    for ch in name[1:]:
        if ch in ("#", "♯"):
            f += 7
        elif ch in ("b", "♭"):
            f -= 7
        else:
            break
    return f


def fifths_to_pc(fifths: int) -> int:
    """Line-of-fifths position -> pitch class (mod 12).  Tonic-relative fifths ->
    tonic-relative pitch class (semitones above tonic)."""
    return (fifths * 7) % 12


# ---------------------------------------------------------------------------
# Canonical chord-quality vocabulary.  Coarse on purpose for v1 (cross-source
# comparability): triad family + the common seventh families + aug6 + sus.
# Extensions (9/11/13) fold onto their parent seventh.  Refinable later.
# ---------------------------------------------------------------------------
CANON_QUALITIES = {
    "maj", "min", "dim", "aug", "dom7", "min7", "maj7",
    "halfdim7", "dim7", "minmaj7", "aug7", "sus", "aug6", "other",
}

# DCML ms3 `chord_type` -> canonical
_DCML_Q = {
    "M": "maj", "m": "min", "o": "dim", "+": "aug",
    "Mm7": "dom7", "mm7": "min7", "MM7": "maj7", "mM7": "minmaj7",
    "o7": "dim7", "%7": "halfdim7", "+7": "aug7", "+M7": "aug7",
    "Ger": "aug6", "It": "aug6", "Fr": "aug6",
}

# Harte / jazz shorthand -> canonical (used by symbol parsers, after stripping
# extension digits).  Keys are lowercased shorthand stems.
_HARTE_Q = {
    "maj": "maj", "": "maj", "major": "maj",
    "min": "min", "m": "min", "minor": "min", "-": "min",
    "dim": "dim", "o": "dim", "aug": "aug", "+": "aug",
    "7": "dom7", "dom7": "dom7",
    "min7": "min7", "m7": "min7", "-7": "min7",
    "maj7": "maj7", "ma7": "maj7", "^7": "maj7",
    "hdim7": "halfdim7", "min7b5": "halfdim7", "m7b5": "halfdim7", "%7": "halfdim7", "%": "halfdim7",
    "dim7": "dim7", "o7": "dim7",
    "minmaj7": "minmaj7", "mmaj7": "minmaj7", "m^7": "minmaj7",
    "sus2": "sus", "sus4": "sus", "sus": "sus",
    "maj6": "maj", "6": "maj", "min6": "min", "m6": "min",
}


def canon_quality_dcml(chord_type: str) -> str:
    return _DCML_Q.get(str(chord_type).strip(), "other")


def canon_quality_harte(shorthand: str) -> str:
    s = str(shorthand).strip().lower()
    if s in _HARTE_Q:
        return _HARTE_Q[s]
    # fold extensions: a trailing 9/11/13 reduces to the parent 7th family
    for ext in ("13", "11", "9"):
        if s.endswith(ext):
            base = s[: -len(ext)]
            if base in ("", "maj", "dom"):
                return "dom7"
            if base in ("min", "m", "-"):
                return "min7"
            if base in ("maj", "ma", "^"):
                return "maj7"
    if s.startswith(("maj", "ma", "^")):
        return "maj7" if "7" in s else "maj"
    if s.startswith(("min", "m", "-")):
        return "min7" if "7" in s else "min"
    if "7" in s:
        return "dom7"
    return "other"


# ---------------------------------------------------------------------------
@dataclass
class ChordEvent:
    root_fifths: Optional[int]   # tonic-relative position on the line of fifths
    quality: str                 # one of CANON_QUALITIES
    bass_fifths: Optional[int] = None
    dur: Optional[float] = None
    raw: str = ""

    def token(self) -> str:
        """The low-prejudice chord token used as an LDA 'word'."""
        r = "x" if self.root_fifths is None else str(self.root_fifths)
        return f"{r}:{self.quality}"


@dataclass
class Piece:
    source: str                  # corpus/source id (the §5 source-leakage label)
    pid: str                     # piece id within the source
    chords: list = field(default_factory=list)   # List[ChordEvent], in order
    mode: Optional[str] = None   # 'major' | 'minor' | None
    meta: dict = field(default_factory=dict)      # composer, year, genre, etc. (lens only)

    def tokens(self, dedup_repeats: bool = True) -> list:
        """Chord-token sequence; consecutive identical tokens collapsed by default
        (change-point view — removes the harmonic-rhythm confound)."""
        toks = [c.token() for c in self.chords]
        if not dedup_repeats:
            return toks
        out = []
        for t in toks:
            if not out or out[-1] != t:
                out.append(t)
        return out

    def transition_tokens(self, dedup_repeats: bool = True) -> list:
        """Adjacent-pair tokens 'a>b' — the progression view (where idiom lives)."""
        seq = self.tokens(dedup_repeats=dedup_repeats)
        return [f"{seq[i]}>{seq[i+1]}" for i in range(len(seq) - 1)]
