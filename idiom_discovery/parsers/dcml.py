"""DCML harmonies-TSV parser → Piece.

DCML/ms3 `harmonies/*.tsv` give the chord root as `root` = fifths over the LOCAL
tonic (0 = tonic, +1 = dominant, -1 = subdominant, ...) and quality as `chord_type`.
That is already our key-normalized, spelling-aware encoding — no transposition needed,
and it tracks modulation automatically (root is relative to the *local* key).
"""
from __future__ import annotations
import os
import glob
import pandas as pd

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, canon_quality_dcml  # noqa: E402


def parse_harmonies_tsv(path: str, source: str, composer: str = "") -> Piece:
    df = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=True)
    cols = set(df.columns)
    if not {"chord", "root", "chord_type"} <= cols:
        raise ValueError(f"{path}: missing DCML harmony columns (have {sorted(cols)[:8]}…)")

    chords = []
    for _, row in df.iterrows():
        ch = row.get("chord")
        if ch is None or (isinstance(ch, float)) or str(ch).strip() in ("", "nan"):
            continue  # no harmony on this row (phrase/section marker etc.)
        root = row.get("root")
        try:
            root_f = int(round(float(root)))
        except (TypeError, ValueError):
            continue  # @none / unparseable root — skip
        bass = row.get("bass_note")
        try:
            bass_f = int(round(float(bass)))
        except (TypeError, ValueError):
            bass_f = None
        chords.append(ChordEvent(
            root_fifths=root_f,
            quality=canon_quality_dcml(row.get("chord_type")),
            bass_fifths=bass_f,
            raw=str(ch),
        ))

    # opening mode from globalkey_is_minor if present
    mode = None
    if "globalkey_is_minor" in cols and len(df):
        v = str(df.iloc[0].get("globalkey_is_minor")).strip()
        mode = "minor" if v in ("1", "True", "true") else ("major" if v in ("0", "False", "false") else None)

    pid = os.path.splitext(os.path.basename(path))[0]
    return Piece(source=source, pid=pid, chords=chords, mode=mode,
                 meta={"composer": composer, "path": path})


def load_dcml_repo(repo_dir: str, source: str, composer: str = "") -> list:
    """Load every harmonies/*.tsv in a DCML repo (or composer sub-corpus)."""
    pieces = []
    for tsv in sorted(glob.glob(os.path.join(repo_dir, "harmonies", "*.tsv"))):
        try:
            p = parse_harmonies_tsv(tsv, source=source, composer=composer)
            if p.chords:
                pieces.append(p)
        except Exception as e:  # noqa: BLE001 — report and continue (audit-friendly)
            print(f"  ! skip {os.path.basename(tsv)}: {e}")
    return pieces


if __name__ == "__main__":
    # smoke: parse a DCML repo passed on the CLI and summarise
    import collections
    d = sys.argv[1] if len(sys.argv) > 1 else \
        "/sessions/nice-busy-fermat/mnt/MS/corpora/expl/dcml_mozart"
    ps = load_dcml_repo(d, source=os.path.basename(d))
    print(f"pieces: {len(ps)}")
    if ps:
        tot = sum(len(p.chords) for p in ps)
        print(f"total chord events: {tot}  (avg {tot/len(ps):.0f}/piece)")
        q = collections.Counter(c.quality for p in ps for c in p.chords)
        print("quality dist:", dict(q.most_common()))
        ex = ps[0]
        print(f"example {ex.pid} mode={ex.mode}")
        print("  tokens[:12]:", ex.tokens()[:12])
        print("  transitions[:6]:", ex.transition_tokens()[:6])
