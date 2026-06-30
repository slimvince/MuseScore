"""Impro-Visor .ls leadsheet parser (jazz, incl. modal). S-expr header + bar lines
('Dm7 | / | Dm7 |'). No reliable tonic ((key N) is a signature) -> tonic estimated as
the most-common chord root (neutral; works for functional I-emphasis and modal vamps)."""
import os, sys, glob, re, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths, canon_quality_harte
_R = re.compile(r"^([A-G][#b]?)(.*)$")
def _ch(tok):
    tok = tok.strip().split("/")[0]
    if not tok or tok in ("/", "NC", "N.C.", "N"): return None
    m = _R.match(tok)
    if not m: return None
    rf = name_to_fifths(m.group(1))
    return None if rf is None else (rf, canon_quality_harte(m.group(2) or "maj"))
def load_improvisor(folder, source="improvisor", tradition="jazz", limit=None):
    files = sorted(glob.glob(os.path.join(folder, "**", "*.ls"), recursive=True))
    if limit: files = files[:limit]
    pieces = []
    for f in files:
        raw = []
        for line in open(f, encoding="utf-8", errors="replace"):
            line = line.strip()
            if not line or line.startswith("(") or "|" not in line: continue
            for tok in re.split(r"[|\s]+", line):
                c = _ch(tok)
                if c: raw.append(c)
        if len(raw) < 4: continue
        tonic = collections.Counter(r for r, _ in raw).most_common(1)[0][0]
        pieces.append(Piece(source=source, pid=os.path.basename(f),
                            chords=[ChordEvent(root_fifths=r - tonic, quality=q) for r, q in raw],
                            mode=None, meta={"tradition": tradition}))
    return pieces
