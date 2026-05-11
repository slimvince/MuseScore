#!/usr/bin/env python3
"""Iteration 24: enumerate all Cat 1 Minor-winner cases and classify by reference."""
import json, re, statistics, sys
from pathlib import Path

CORPUS = Path(__file__).resolve().parent / "corpus"
sys.path.insert(0, str(Path(__file__).resolve().parent))

_NOTE_PC = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}

def parse_root_pc(sym: str) -> int:
    if not sym: return -1
    base = sym.rsplit('/', 1)[0]
    m = re.match(r'^([A-G])([#b]*)', base)
    if not m: return -1
    pc = _NOTE_PC[m.group(1)]
    for ch in m.group(2):
        pc += 1 if ch == '#' else -1
    return pc % 12

PC_NAMES = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]
def pn(pc): return PC_NAMES[pc % 12] if pc is not None and pc >= 0 else "?"

def find_region(regions, meas, beat):
    best, bd = None, float('inf')
    for tol in (0.26, 1.5):
        for r in regions:
            if r.get("measureNumber") == meas:
                d = abs(float(r.get("beat", 0)) - beat)
                if d < bd and d <= tol:
                    bd, best = d, r
        if best is not None:
            break
    return best

def interval_label(s):
    i = s % 12
    return {4:"I4", 3:"I3", 7:"I7", 0:"UNISON"}.get(i, f"OTHER({i})")

CASES = [
    ("bwv153.9",  5,  3.0, "Em"),
    ("bwv154.3",  1,  2.0, "F#m"),
    ("bwv184.5",  10, 3.0, "Em"),
    ("bwv187.7",  14, 2.0, "Gm6"),
    ("bwv227.11", 10, 3.0, "Em6"),
    ("bwv245.14", 2,  2.0, "F#m"),
    ("bwv245.22", 1,  2.0, "C#m"),
    ("bwv278",    8,  2.0, "Em6"),
    ("bwv282",    12, 3.0, "Bm"),
    ("bwv301",    2,  3.0, "Dm6"),
    ("bwv302",    1,  4.0, "Em"),
    ("bwv322",    11, 4.0, "Em"),
    ("bwv327",    6,  3.0, "F#m"),
    ("bwv353",    8,  3.0, "Dm"),
    ("bwv359",    1,  2.0, "F#m"),
    ("bwv37.6",   13, 4.0, "F#m"),
    ("bwv378",    13, 4.0, "Em"),
    ("bwv383",    6,  3.0, "Em"),
    ("bwv397",    1,  4.0, "Dm"),
    ("bwv40.6",   14, 2.0, "Gm"),
    ("bwv408",    4,  1.0, "Dm"),
    ("bwv409",    4,  2.0, "F#m"),
    ("bwv423",    9,  2.0, "Gm"),
    ("bwv423",    9,  3.0, "Dm"),
    ("bwv85.6",   5,  1.0, "Fm"),
]

rows = []
for stem, meas, beat, our_sym in CASES:
    with open(CORPUS / f"{stem}.ours.json") as f:
        ours_data = json.load(f)
    with open(CORPUS / f"{stem}.music21.json") as f:
        m21_data = json.load(f)

    our_r = find_region(ours_data.get("regions", []), meas, beat)
    m21_r = find_region(m21_data.get("regions", []), meas, beat)
    assert our_r is not None, f"ours not found: {stem} m{meas} b{beat}"

    our_root  = our_r.get("rootPitchClass", -1)
    our_bass  = our_r.get("bassPitchClass", our_root)
    our_score = float(our_r.get("chordScore", 0))
    our_chord = our_r.get("chordSymbol", "?")
    alts      = our_r.get("alternatives", [])

    alt1_sym = alt1_score = None
    for alt in alts:
        s = alt.get("chordSymbol", "")
        if s and s != our_chord:
            alt1_sym   = s
            alt1_score = float(alt.get("score", 0))
            break

    raw_margin = (our_score - alt1_score) if alt1_score is not None else None

    ref_root  = m21_r.get("rootPitchClass", -1) if m21_r else -1
    ref_chord = m21_r.get("chordSymbol", "?")   if m21_r else "?"

    if ref_root >= 0 and our_bass is not None:
        interval = (our_bass - ref_root) % 12
        itype    = interval_label(interval)
    else:
        interval, itype = -1, "?"

    ref_in_alts = ref_alt_idx = ref_alt_sym = ref_alt_score = None
    ref_in_alts = False
    if ref_root >= 0:
        for idx, alt in enumerate(alts):
            if parse_root_pc(alt.get("chordSymbol","")) == ref_root:
                ref_in_alts  = True
                ref_alt_idx  = idx
                ref_alt_sym  = alt.get("chordSymbol","")
                ref_alt_score = float(alt.get("score", 0))
                break

    rows.append(dict(
        stem=stem, meas=meas, beat=beat,
        our_chord=our_chord, our_root=our_root, our_bass=our_bass,
        our_score=our_score,
        ref_chord=ref_chord, ref_root=ref_root,
        alt1_sym=alt1_sym, alt1_score=alt1_score,
        raw_margin=raw_margin,
        interval=interval, itype=itype,
        ref_in_alts=ref_in_alts, ref_alt_idx=ref_alt_idx,
        ref_alt_sym=ref_alt_sym, ref_alt_score=ref_alt_score,
    ))

# Print table
print(f"{'FILE':<13} {'M':>3} {'B':>3}  {'OUR-WIN':<8} {'SC':>6}  "
      f"{'REF-ROOT':>8}  {'ALT1'::<17} {'A1-SC':>6}  "
      f"{'MARG':>7}  {'INT':>3} {'TYPE':<8} REF-IN-ALTS")
print("-" * 125)
for r in rows:
    ria = "no"
    if r["ref_in_alts"]:
        ria = f"yes -> alt[{r['ref_alt_idx']}] {r['ref_alt_sym']} ({r['ref_alt_score']:.4f})"
    marg = f"{r['raw_margin']:+.4f}" if r["raw_margin"] is not None else "      ?"
    a1sc = f"{r['alt1_score']:.4f}" if r["alt1_score"] is not None else "     ?"
    print(f"{r['stem']:<13} {r['meas']:>3} {r['beat']:>3.0f}  "
          f"{r['our_chord']:<8} {r['our_score']:>6.4f}  "
          f"{pn(r['ref_root']):>8}  "
          f"{str(r['alt1_sym']):<17} {a1sc:>6}  "
          f"{marg:>8}  {r['interval']:>3} {r['itype']:<8} {ria}")

n = len(rows)
print()
print(f"Total Minor-winner Cat 1 cases: {n}")
for code in ["I4","I3","I7","UNISON"]:
    sub  = [r for r in rows if r["itype"] == code]
    ryes = [r for r in sub if r["ref_in_alts"]]
    ri0  = [r for r in ryes if r["ref_alt_idx"] == 0]
    ri1  = [r for r in ryes if r["ref_alt_idx"] == 1]
    if sub:
        print(f"  {code} ({len(sub)}, {100*len(sub)//n}%):  ref in alts {len(ryes)}/{len(sub)}  "
              f"(alt[0]={len(ri0)}, alt[1]={len(ri1)})")
oth = [r for r in rows if r["itype"].startswith("OTHER")]
if oth:
    print(f"  OTHER ({len(oth)}): " +
          ", ".join(f"{r['stem']} m{r['meas']} interval={r['interval']}" for r in oth))

all_yes = [r for r in rows if r["ref_in_alts"]]
ai0 = [r for r in all_yes if r["ref_alt_idx"] == 0]
ai1 = [r for r in all_yes if r["ref_alt_idx"] == 1]
print()
print(f"Ref in our candidates (any alt): {len(all_yes)}/{n}  ({100*len(all_yes)//n}%)")
print(f"  of which ref is alt[0]:        {len(ai0)}")
print(f"  of which ref is alt[1]:        {len(ai1)}")

margins = [r["raw_margin"] for r in rows if r["raw_margin"] is not None]
print()
print(f"Raw margin stats:  min={min(margins):.4f}  "
      f"median={statistics.median(margins):.4f}  max={max(margins):.4f}")
lt030 = sum(1 for m in margins if m < 0.30)
lt050 = sum(1 for m in margins if m < 0.50)
print(f"  margin < 0.30:  {lt030}/{n}  ({100*lt030//n}%)")
print(f"  margin < 0.50:  {lt050}/{n}  ({100*lt050//n}%)")
