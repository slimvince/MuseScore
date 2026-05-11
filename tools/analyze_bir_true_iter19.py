#!/usr/bin/env python3
"""
analyze_bir_true_iter19.py — Diagnostic categorization of the 98 remaining
BIR=true mismatches (Iteration 19).

Pure diagnostic: zero logic changes. Writes no corpus files.

Usage:
    cd C:\s\MS && python tools/analyze_bir_true_iter19.py
"""
from __future__ import annotations

import re
import sys
import statistics
from pathlib import Path
from collections import Counter
from typing import Optional

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


# ── §3b: chord-symbol parser ──────────────────────────────────────────────────

_NOTE_PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def parse_chord_symbol(sym: str) -> tuple[int, int]:
    """
    Returns (rootPc, bassPc) for a chord symbol string.
    Strips a trailing /Bass inversion suffix if present.
    Returns (-1, -1) on parse failure.
    """
    if not sym:
        return (-1, -1)
    # Split on the last '/' — that gives root part and optional bass note
    parts = sym.rsplit('/', 1)
    root_part = parts[0]
    bass_part = parts[1] if len(parts) == 2 else None

    def _parse_note(s: str) -> int:
        if not s:
            return -1
        m = re.match(r'^([A-G])([#b]*)', s)
        if not m:
            return -1
        pc = _NOTE_PC[m.group(1)]
        for ch in m.group(2):
            if ch == '#':
                pc += 1
            elif ch == 'b':
                pc -= 1
        return pc % 12

    root_pc = _parse_note(root_part)
    if root_pc == -1:
        return (-1, -1)

    if bass_part is not None:
        bass_pc = _parse_note(bass_part)
        if bass_pc == -1:
            return (-1, -1)
    else:
        bass_pc = root_pc

    return (root_pc, bass_pc)


def _smoke_test():
    cases = [
        ("Gm",       (7,  7)),
        ("Am/C",     (9,  0)),
        ("F#m7/A",   (6,  9)),
        ("Bbadd9",   (10, 10)),
        ("Dm7/Bb",   (2,  10)),
    ]
    print("Smoke test — parse_chord_symbol:")
    for sym, expected in cases:
        result = parse_chord_symbol(sym)
        status = "OK" if result == expected else f"FAIL (expected {expected})"
        print(f"  parse_chord_symbol({sym!r:15s}) → {str(result):10s}  {status}")
    print()


# ── §3a helper: reuse _infer_quality from analyze_inversion_errors ─────────────

def _infer_quality(sym: str) -> str:
    """Infer a quality category name from a chord symbol string."""
    s = sym.split('/')[0]
    m = re.match(r'^[A-G][#b]?', s)
    if not m:
        return ""
    body = s[m.end():]
    if 'dim7' in body or '°7' in body:
        return "Diminished7"
    if body.startswith('ø') or 'm7b5' in body.lower():
        return "HalfDiminished"
    if 'maj7' in body.lower() or body.startswith('M7'):
        return "Major7"
    if body.startswith('m7') or body.startswith('min7'):
        return "Minor7"
    if body.startswith('7'):
        return "Dominant7"
    if 'dim' in body.lower() or '°' in body:
        return "Diminished"
    if body.startswith('m') or body.startswith('min'):
        return "Minor"
    # Handle add/sus/aug after root without minor prefix → Major family
    return "Major"


# ── §3c key-info parser ────────────────────────────────────────────────────────

def parse_key(key_str: str) -> tuple[int, str]:
    """
    Parse a key string like 'Gmin', 'CMaj', 'F#Dor'.
    Returns (keyTonicPc, mode) where mode is 'major', 'minor', or 'unknown'.
    """
    if not key_str:
        return (-1, "unknown")
    m = re.match(r'^([A-G][#b]?)(.*)', key_str)
    if not m:
        return (-1, "unknown")
    pc = parse_chord_symbol(m.group(1) + "5")[0]  # reuse parser for note
    suffix = m.group(2).lower()
    if suffix in ('maj', 'major', 'ion', 'lyd', 'mix'):
        mode = "major"
    elif suffix in ('min', 'minor', 'aeo', 'dor', 'phr', 'loc'):
        mode = "minor"
    else:
        mode = "unknown"
    return (pc, mode)


# ── dataclass for per-case info ───────────────────────────────────────────────

from dataclasses import dataclass, field


@dataclass
class CaseInfo:
    file:             str
    measure:          int
    beat:             float
    winner_symbol:    str
    winner_root_pc:   int
    winner_bass_pc:   int
    winner_quality:   str
    winner_score:     float
    stored_margin:    float
    alt_symbol:       str
    alt_root_pc:      int
    alt_bass_pc:      int
    alt_quality:      str
    alt_score:        float
    raw_margin:       float
    key_str:          str
    key_tonic_pc:     int
    key_mode:         str
    # derived
    alt_root_is_winner_bass: bool = False
    alt_bass_is_winner_bass: bool = False
    alt_is_clean:            bool = False
    category:                int  = 0  # 1, 2, 3, or 4


# ── case builder (shared by main analysis and genuine-48 section) ─────────────

CLEAN_QUALITIES = {"Major", "Minor"}


def _categorize_cases(cases_raw: list) -> list:
    """Convert raw (stem, region) list to categorized CaseInfo list."""
    cases: list[CaseInfo] = []
    for stem, r in cases_raw:
        winner_root_pc = r.root_pc
        winner_bass_pc = r.bass_pc if r.bass_pc is not None else r.root_pc
        winner_quality = r.quality
        winner_score   = r.chord_score or 0.0
        stored_margin  = r.chord_score_margin or 0.0

        alt_symbol = alt_score = None
        for alt in r.alternatives:
            sym = alt.get("chordSymbol", "")
            if sym and sym != r.chord_symbol:
                alt_symbol = sym
                alt_score  = float(alt.get("score", 0.0))
                break

        key_tonic_pc, key_mode = parse_key(r.key)

        if alt_symbol is None:
            cases.append(CaseInfo(
                file=stem, measure=r.measure_number, beat=r.beat,
                winner_symbol=r.chord_symbol,
                winner_root_pc=winner_root_pc, winner_bass_pc=winner_bass_pc,
                winner_quality=winner_quality, winner_score=winner_score,
                stored_margin=stored_margin,
                alt_symbol="", alt_root_pc=-1, alt_bass_pc=-1,
                alt_quality="", alt_score=0.0, raw_margin=0.0,
                key_str=r.key, key_tonic_pc=key_tonic_pc, key_mode=key_mode,
                category=4,
            ))
            continue

        alt_root_pc, alt_bass_pc = parse_chord_symbol(alt_symbol)
        alt_quality = _infer_quality(alt_symbol)
        raw_margin  = winner_score - alt_score

        alt_root_is_winner_bass = (alt_root_pc >= 0 and alt_root_pc == winner_bass_pc)
        alt_bass_is_winner_bass = (alt_bass_pc >= 0 and alt_bass_pc == winner_bass_pc)
        alt_is_clean = alt_quality in CLEAN_QUALITIES

        if alt_root_is_winner_bass:
            category = 1
        elif alt_bass_is_winner_bass:
            category = 2
        else:
            category = 3

        cases.append(CaseInfo(
            file=stem, measure=r.measure_number, beat=r.beat,
            winner_symbol=r.chord_symbol,
            winner_root_pc=winner_root_pc, winner_bass_pc=winner_bass_pc,
            winner_quality=winner_quality, winner_score=winner_score,
            stored_margin=stored_margin,
            alt_symbol=alt_symbol, alt_root_pc=alt_root_pc, alt_bass_pc=alt_bass_pc,
            alt_quality=alt_quality, alt_score=alt_score, raw_margin=raw_margin,
            key_str=r.key, key_tonic_pc=key_tonic_pc, key_mode=key_mode,
            alt_root_is_winner_bass=alt_root_is_winner_bass,
            alt_bass_is_winner_bass=alt_bass_is_winner_bass,
            alt_is_clean=alt_is_clean,
            category=category,
        ))
    return cases


# ── main ──────────────────────────────────────────────────────────────────────


def main():
    _smoke_test()

    # ── Step 3a: load corpus and classify ─────────────────────────────────
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    if not ours_files:
        print("ERROR: No .ours.json files found.", file=sys.stderr)
        sys.exit(1)

    all_bir_2way    = []
    genuine_bir_3way = []
    wir_coverage = 0

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        music21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not music21_path.exists():
            continue
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions  = cmp.load_analysis(music21_path)
        except Exception:
            continue
        if not ours_regions:
            continue

        aligned = cmp.align_regions(ours_regions, m21_regions)

        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regions = []
        if wir_path:
            try:
                wir_regions = dcml.parse_rntxt_file(wir_path)
                wir_coverage += 1
            except Exception:
                pass
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None] * len(ours_regions)

        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue
            if not our_r.bass_is_root:
                continue

            all_bir_2way.append((stem, our_r))

            if wir_regions and i < len(wir_aligned):
                wir_r = wir_aligned[i]
                wir_pc = wir_r.root_pc if wir_r is not None else None
                cat = cmp.three_way_classify(our_r.root_pc,
                                             their_r.root_pc if their_r else None,
                                             wir_pc)
                if cat == "music21_dcml_agree":
                    genuine_bir_3way.append((stem, our_r))

    # Choose set per spec: three-way if ≥50, else two-way
    if len(genuine_bir_3way) >= 50:
        cases_raw = genuine_bir_3way
        set_label = "three-way"
    else:
        cases_raw = all_bir_2way
        set_label = "two-way"

    n = len(cases_raw)
    print(f"Using {set_label} set, n={n}")
    print()

    # ── Step 3c+3d: extract per-case info and categorize ──────────────────
    cases = _categorize_cases(cases_raw)

    # ── Step 3e: printed report ────────────────────────────────────────────

    def pct(k, total=n):
        return f"{100*k/max(1,total):.0f}%"

    def margin_stats(margins):
        if not margins:
            return "n/a"
        return (f"min={min(margins):.2f}  "
                f"median={statistics.median(margins):.2f}  "
                f"max={max(margins):.2f}")

    cat1 = [c for c in cases if c.category == 1]
    cat2 = [c for c in cases if c.category == 2]
    cat3 = [c for c in cases if c.category == 3]
    cat4 = [c for c in cases if c.category == 4]

    print("BIR=true mismatch analysis — Iteration 19")
    print(f"Using {set_label} set, n={n}")
    print("=========================================")
    print()

    # ── Category 1 ────────────────────────────────────────────────────────
    n1 = len(cat1)
    print(f"CATEGORY 1 — Canonical inversion (alt rootPc == winner bassPc)")
    print(f"  Count:  {n1}  ({pct(n1)})")
    if n1:
        wq = Counter(c.winner_quality for c in cat1)
        aq = Counter(c.alt_quality    for c in cat1)
        clean1 = [c for c in cat1 if c.alt_is_clean]
        m1 = [c.raw_margin for c in cat1]
        lt050 = sum(1 for m in m1 if m < 0.50)
        lt100 = sum(1 for m in m1 if m < 1.00)
        print(f"  Winner qualities:  " +
              "  ".join(f"{q}={v}" for q, v in sorted(wq.items())))
        print(f"  Alt qualities:     " +
              "  ".join(f"{q}={v}" for q, v in sorted(aq.items())))
        print(f"  Alt is clean (Major/Minor):  {len(clean1)}  ({pct(len(clean1), n1)})")
        print(f"  raw_margin stats:  {margin_stats(m1)}")
        print(f"  raw_margin < 0.50: {lt050}  ({pct(lt050, n1)})")
        print(f"  raw_margin < 1.00: {lt100}  ({pct(lt100, n1)})")
        print(f"  Examples (up to 5):")
        for c in cat1[:5]:
            print(f"    {c.file:<12s}  m{c.measure}  beat{c.beat}  "
                  f"{c.winner_symbol} → {c.alt_symbol}  "
                  f"margin={c.raw_margin:+.2f}  key={c.key_str}")
    print()

    # ── Category 2 ────────────────────────────────────────────────────────
    n2 = len(cat2)
    print(f"CATEGORY 2 — Same bass, alt root unrelated to winner bass")
    print(f"  Count:  {n2}  ({pct(n2)})")
    if n2:
        pair_counts: Counter = Counter(
            f"({c.winner_quality}→{c.alt_quality})" for c in cat2)
        m2 = [c.raw_margin for c in cat2]
        print(f"  Winner/alt quality pairs:  " +
              "  ".join(f"{p}={v}" for p, v in pair_counts.most_common()))
        print(f"  raw_margin stats:  {margin_stats(m2)}")
        print(f"  Examples (up to 3):")
        for c in cat2[:3]:
            print(f"    {c.file:<12s}  m{c.measure}  beat{c.beat}  "
                  f"{c.winner_symbol} → {c.alt_symbol}  "
                  f"margin={c.raw_margin:+.2f}  key={c.key_str}")
    print()

    # ── Category 3 ────────────────────────────────────────────────────────
    n3 = len(cat3)
    print(f"CATEGORY 3 — Unrelated alternative (no same-bass relationship)")
    print(f"  Count:  {n3}  ({pct(n3)})")
    if n3:
        m3 = [c.raw_margin for c in cat3]
        print(f"  raw_margin stats:  {margin_stats(m3)}")
        print(f"  Examples (up to 3):")
        for c in cat3[:3]:
            print(f"    {c.file:<12s}  m{c.measure}  beat{c.beat}  "
                  f"{c.winner_symbol} → {c.alt_symbol}  "
                  f"margin={c.raw_margin:+.2f}  key={c.key_str}")
    print()

    # ── Category 4 ────────────────────────────────────────────────────────
    n4 = len(cat4)
    print(f"CATEGORY 4 — No real alternative in candidates")
    print(f"  Count:  {n4}  ({pct(n4)})")
    print()

    # ── Summary ───────────────────────────────────────────────────────────
    actionable   = n1 + n2
    clean1_count = sum(1 for c in cat1 if c.alt_is_clean)
    c1_clean_lt050 = sum(1 for c in cat1 if c.alt_is_clean and c.raw_margin < 0.50)
    c1_clean_lt100 = sum(1 for c in cat1 if c.alt_is_clean and c.raw_margin < 1.00)

    print("=========================================")
    print("SUMMARY")
    print(f"  Actionable (Cat 1 + 2):         {actionable}  ({pct(actionable)})")
    print(f"  Cat 1 only (cleanest target):   {n1}  ({pct(n1)})")
    print(f"  Cat 1 with clean alt:           {clean1_count}  ({pct(clean1_count)})")
    print(f"  Cat 1, clean alt, margin<0.50:  {c1_clean_lt050}  ({pct(c1_clean_lt050)})")
    print(f"  Cat 1, clean alt, margin<1.00:  {c1_clean_lt100}  ({pct(c1_clean_lt100)})")

    # ── List 1: Cat 2 Minor→HalfDim cases ────────────────────────────────
    print()
    cat2_mhd = [c for c in cat2
                if c.winner_quality == "Minor" and c.alt_quality == "HalfDiminished"]
    print(f"CAT2-MHD CASE LIST ({len(cat2_mhd)} cases):")
    for c in cat2_mhd:
        print(f"  [CAT2-MHD] file={c.file}  m={c.measure}  beat={c.beat}"
              f"  winner={c.winner_symbol}  alt={c.alt_symbol}"
              f"  margin={c.raw_margin:+.2f}  key={c.key_str}")

    # ── List 2: Cat 1 clean-alt cases ─────────────────────────────────────
    print()
    cat1_cln = [c for c in cat1 if c.alt_quality in CLEAN_QUALITIES]
    print(f"CAT1-CLN CASE LIST ({len(cat1_cln)} cases):")
    for c in cat1_cln:
        print(f"  [CAT1-CLN] file={c.file}  m={c.measure}  beat={c.beat}"
              f"  winner={c.winner_symbol}  alt={c.alt_symbol}"
              f"  margin={c.raw_margin:+.2f}  key={c.key_str}")

    # ── List 3: ALL Cat 1 cases ────────────────────────────────────────────
    print()
    print(f"CAT1-ALL CASE LIST ({len(cat1)} cases):")
    for c in cat1:
        print(f"  [CAT1] file={c.file}  m={c.measure}  beat={c.beat}"
              f"  winner={c.winner_symbol}  alt={c.alt_symbol}"
              f"  margin={c.raw_margin:+.2f}  key={c.key_str}")

    # ── List 4: ALL Cat 2 cases ────────────────────────────────────────────
    print()
    print(f"CAT2-ALL CASE LIST ({len(cat2)} cases):")
    for c in cat2:
        print(f"  [CAT2] file={c.file}  m={c.measure}  beat={c.beat}"
              f"  winner={c.winner_symbol}  alt={c.alt_symbol}"
              f"  margin={c.raw_margin:+.2f}  key={c.key_str}")

    # ── GENUINE THREE-WAY SECTION (always runs, regardless of mode) ───────────
    print()
    print("=" * 70)
    ng = len(genuine_bir_3way)
    print(f"GENUINE THREE-WAY CASES (n={ng}):")
    print("=" * 70)
    gcases = _categorize_cases(genuine_bir_3way)
    gng = len(gcases)

    def gpct(k: int) -> str:
        return f"{100*k/max(1,gng):.0f}%"

    def _qpairs(lst: list) -> Counter:
        return Counter(f"({c.winner_quality}→{c.alt_quality})" for c in lst)

    gc1 = [c for c in gcases if c.category == 1]
    gc2 = [c for c in gcases if c.category == 2]
    gc3 = [c for c in gcases if c.category == 3]
    gc4 = [c for c in gcases if c.category == 4]

    print(f"  Cat 1: {len(gc1)}  ({gpct(len(gc1))})")
    if gc1:
        wq1g = Counter(c.winner_quality for c in gc1)
        aq1g = Counter(c.alt_quality    for c in gc1)
        print(f"    winner_qualities: " + "  ".join(f"{q}={v}" for q,v in sorted(wq1g.items())))
        print(f"    alt_qualities:    " + "  ".join(f"{q}={v}" for q,v in sorted(aq1g.items())))
        for p, v in _qpairs(gc1).most_common(8):
            print(f"      {p}={v}")
    print(f"  Cat 2: {len(gc2)}  ({gpct(len(gc2))})")
    if gc2:
        print(f"    quality_pairs: " + "  ".join(f"{p}={v}" for p,v in _qpairs(gc2).most_common()))
    print(f"  Cat 3: {len(gc3)}  ({gpct(len(gc3))})")
    print(f"  Cat 4: {len(gc4)}  ({gpct(len(gc4))})")
    print()
    for c in gcases:
        tag = f"GENUINE-CAT{c.category}"
        print(f"  [{tag}] file={c.file}  m={c.measure}  beat={c.beat}"
              f"  winner={c.winner_symbol}  alt={c.alt_symbol}"
              f"  margin={c.raw_margin:+.2f}  key={c.key_str}"
              f"  winner_q={c.winner_quality}  alt_q={c.alt_quality}")


if __name__ == "__main__":
    main()
