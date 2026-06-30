"""Jazz Harmony Treebank parser → Piece.

treebank.json: each tune has `key` (uppercase=major / lowercase=minor letter, opt. `-`/`#`),
`chords` (list of chord-symbol strings in the documented JHT shorthand), `composers`, `year`,
`meter`.  Chord shorthand: root [A-G][#b]?  then a basic form (m, +, %, o, sus; major = none)
then optional 6 / 7 / ^7.
"""
from __future__ import annotations
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths  # noqa: E402

_ROOT_RE = re.compile(r"^([A-G][#b\-]?)(.*)$")

# JHT form+extension -> canonical quality
_JHT_Q = {
    "": "maj", "6": "maj", "7": "dom7", "^7": "maj7",
    "m": "min", "m6": "min", "m7": "min7", "m^7": "minmaj7",
    "+": "aug", "+7": "aug7", "+^7": "aug7",
    "%": "halfdim7", "%7": "halfdim7",
    "o": "dim", "o7": "dim7",
    "sus": "sus", "sus7": "sus",
}


def _parse_key(k):
    if not k:
        return None, None
    mode = "minor" if k[0].islower() else "major"
    name = k[0].upper() + k[1:].replace("-", "b")
    return name_to_fifths(name), mode


def _parse_chord(sym, tonic_f):
    m = _ROOT_RE.match(sym.strip())
    if not m:
        return None
    root_name, rest = m.group(1).replace("-", "b"), m.group(2)
    rf = name_to_fifths(root_name)
    if rf is None or tonic_f is None:
        return None
    qual = _JHT_Q.get(rest, None)
    if qual is None:
        # tolerate stray extensions: fold to the parent family
        if rest.startswith("m"):
            qual = "min7" if "7" in rest else "min"
        elif rest.startswith("^") or "^7" in rest:
            qual = "maj7"
        elif "7" in rest:
            qual = "dom7"
        else:
            qual = "maj"
    return ChordEvent(root_fifths=rf - tonic_f, quality=qual, raw=sym)


def load_jht(path: str, source: str = "jht") -> list:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    tunes = data.values() if isinstance(data, dict) else data
    pieces = []
    for i, t in enumerate(tunes):
        tonic_f, mode = _parse_key(t.get("key", ""))
        chords = []
        for sym in t.get("chords", []):
            ce = _parse_chord(sym, tonic_f)
            if ce:
                chords.append(ce)
        if chords:
            pieces.append(Piece(source=source, pid=str(t.get("title", i)),
                                chords=chords, mode=mode,
                                meta={"composer": str(t.get("composers", "")),
                                      "year": t.get("year"), "tradition": "jazz"}))
    return pieces


if __name__ == "__main__":
    import collections
    p = sys.argv[1] if len(sys.argv) > 1 else \
        "/sessions/nice-busy-fermat/mnt/MS/corpora/expl/jazz_harmony_treebank/treebank.json"
    ps = load_jht(p)
    print(f"tunes: {len(ps)}")
    tot = sum(len(x.chords) for x in ps)
    print(f"chord events: {tot} (avg {tot/max(len(ps),1):.0f})")
    print("quality dist:", dict(collections.Counter(c.quality for x in ps for c in x.chords).most_common()))
    ex = ps[0]
    print(f"example {ex.pid!r} mode={ex.mode} tokens[:10]:", ex.tokens()[:10])
