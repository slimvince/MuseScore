"""McGill Billboard salami_chords parser → Piece (pop/rock).

Each `salami_chords.txt` has a `# tonic: X` header (and may re-declare mid-body at key
changes), then timestamped lines; chords live inside `| ... |` bars in Harte syntax
(ROOT:quality, optional /bass).  Non-chord tokens (., *, &pause, N, x2, ->, structure
letters, section words) are skipped.  We read only the bar region of each line, so a
leading structure letter like 'A' is never mistaken for an A chord.
"""
from __future__ import annotations
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths, canon_quality_harte  # noqa: E402

_TONIC_RE = re.compile(r"#\s*tonic:\s*([A-G][#b]?)", re.I)
_CHORD_RE = re.compile(r"^([A-G][#b]*)(?::([^/]+))?(?:/.+)?$")


def _chord(tok, tonic_f):
    m = _CHORD_RE.match(tok)
    if not m or tonic_f is None:
        return None
    rf = name_to_fifths(m.group(1))
    if rf is None:
        return None
    qual = canon_quality_harte(m.group(2) if m.group(2) else "maj")
    return ChordEvent(root_fifths=rf - tonic_f, quality=qual, raw=tok)


def parse_salami(path: str, source: str = "mcgill", pid: str = "") -> Piece:
    tonic_f = None
    title = artist = ""
    chords = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            mt = _TONIC_RE.search(line)
            if mt:
                tonic_f = name_to_fifths(mt.group(1))
            if line.startswith("# title:"):
                title = line.split(":", 1)[1].strip()
            elif line.startswith("# artist:"):
                artist = line.split(":", 1)[1].strip()
            if line.startswith("#") or "|" not in line:
                continue
            bars = line[line.index("|"):]            # only the bar region
            for tok in re.split(r"[|\s,]+", bars):
                if not tok or tok in (".", "*", "N", "&pause", "->") or tok.startswith("x"):
                    continue
                ce = _chord(tok, tonic_f)
                if ce:
                    chords.append(ce)
    return Piece(source=source, pid=pid or os.path.basename(os.path.dirname(path)),
                 chords=chords, mode=None,
                 meta={"title": title, "artist": artist, "tradition": "pop"})


def load_mcgill(root: str, source: str = "mcgill") -> list:
    pieces = []
    for path in sorted(glob.glob(os.path.join(root, "*", "salami_chords.txt"))):
        p = parse_salami(path, source=source)
        if p.chords:
            pieces.append(p)
    return pieces


if __name__ == "__main__":
    import collections
    root = sys.argv[1] if len(sys.argv) > 1 else \
        "/sessions/nice-busy-fermat/mnt/MS/corpora/ship/McGill-Billboard"
    ps = load_mcgill(root)
    print(f"songs: {len(ps)}")
    tot = sum(len(x.chords) for x in ps)
    print(f"chord events: {tot} (avg {tot/max(len(ps),1):.0f})")
    print("quality dist:", dict(collections.Counter(c.quality for x in ps for c in x.chords).most_common()))
    ex = next(x for x in ps if len(x.chords) > 6)
    print(f"example {ex.pid} {ex.meta['title']!r} tokens[:10]:", ex.tokens()[:10])
