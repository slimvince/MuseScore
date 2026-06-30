"""Chordonomicon CSV parser (chromatic pop). chords column has inline <structure> tags
+ plain-letter chords (s=sharp, min/maj/7). No key -> tonic = most-common root (neutral)."""
import os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths, canon_quality_harte
import pandas as pd
_TAG = re.compile(r"<[^>]*>")
_R = re.compile(r"^([A-G])(s|#|b)?(.*)$")
def _ch(tok):
    m = _R.match(tok.strip())
    if not m: return None
    name = m.group(1) + ("#" if m.group(2) == "s" else (m.group(2) or ""))
    rf = name_to_fifths(name)
    return None if rf is None else (rf, canon_quality_harte(m.group(3) or "maj"))
def load_chordonomicon(csv, source="chordonomicon", tradition="pop", limit=2000):
    df = pd.read_csv(csv, usecols=["chords"], nrows=limit)
    pieces = []
    for i, s in enumerate(df["chords"].astype(str)):
        raw = [c for c in (_ch(t) for t in _TAG.sub(" ", s).split()) if c]
        if len(raw) < 4: continue
        tonic = collections.Counter(r for r, _ in raw).most_common(1)[0][0]
        pieces.append(Piece(source=source, pid=str(i),
                            chords=[ChordEvent(root_fifths=r - tonic, quality=q) for r, q in raw],
                            mode=None, meta={"tradition": tradition}))
    return pieces
