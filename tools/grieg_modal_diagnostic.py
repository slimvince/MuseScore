#!/usr/bin/env python3
"""
grieg_modal_diagnostic.py — Modal false-positive diagnostic for Grieg lyric pieces.

For every disagreeing aligned region in the Grieg run, records:
  - our detected mode (from key field suffix)
  - DCML global key and local key at the matching annotation
  - whether the globalkey is major/minor/other
  - piece stem

Produces:
  1. Mode-vs-globalkey cross-tabulation for all disagreements
  2. Specific counts: "we say Lydian, DCML says major"
                      "DCML says major, we say Mixolydian or Dorian"
  3. Per-piece clustering: do modal false positives concentrate in specific pieces?

Usage:
    python tools/grieg_modal_diagnostic.py [GRIEG_OURS_DIR]

    GRIEG_OURS_DIR  path to directory of .ours.json files
                    (default: tools/reports/grieg_20260406_154216)
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import dcml_parser as dcml

_REPO_ROOT  = Path(__file__).resolve().parent.parent
_GRIEG_TSV  = _REPO_ROOT / "tools" / "dcml" / "grieg_lyric_pieces" / "harmonies"
_DEFAULT_OURS = _REPO_ROOT / "tools" / "reports" / "grieg_20260406_154216"

# ── Mode extraction ──────────────────────────────────────────────────────────

_SUFFIX_MAP = [
    ('Lyd', 'Lydian'),
    ('Dor', 'Dorian'),
    ('Mix', 'Mixolydian'),
    ('Phr', 'Phrygian'),
    ('Loc', 'Locrian'),
    ('harm', 'HarmonicMinor'),
    ('min', 'Minor'),
    ('Maj', 'Major'),
    ('maj', 'Major'),
]

def _our_mode(key_str: str) -> str:
    for suf, label in _SUFFIX_MAP:
        if suf in key_str:
            return label
    return 'Other'

def _dcml_globalkey_mode(globalkey: str) -> str:
    """Classify a DCML globalkey string as Major or Minor."""
    if not globalkey:
        return 'Unknown'
    # DCML convention: uppercase tonic = major, lowercase = minor
    # e.g. 'Eb' = Eb major, 'b' = b minor
    return 'Minor' if globalkey[0].islower() else 'Major'

# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    ours_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else _DEFAULT_OURS
    if not ours_dir.exists():
        print(f"ERROR: {ours_dir} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Grieg modal disagreement diagnostic")
    print(f"ours dir : {ours_dir}")
    print(f"tsv dir  : {_GRIEG_TSV}")
    print()

    # Accumulate all disagreeing aligned pairs.
    # Each entry: (stem, our_mode, dcml_globalkey_mode, dcml_globalkey, dcml_localkey)
    disagree_rows: list[tuple] = []

    mscx_stems = sorted(p.name.removesuffix('.ours.json') for p in ours_dir.glob("*.ours.json"))

    for stem in mscx_stems:
        ours_path = ours_dir / f"{stem}.ours.json"
        tsv_path  = _GRIEG_TSV / f"{stem}.harmonies.tsv"

        if not tsv_path.exists():
            continue

        try:
            dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
            _, ours_regions = cmp.load_analysis(ours_path)
        except Exception as exc:
            print(f"  {stem}: load error — {exc}", file=sys.stderr)
            continue

        # Build a measure→row lookup for raw TSV fields (globalkey, localkey)
        # so we can retrieve them for the matched annotation.
        raw_rows: list[dict] = []
        with open(tsv_path, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh, delimiter='\t')
            for row in reader:
                raw_rows.append(row)

        # Index raw rows by (mn, mn_onset) for fast lookup
        raw_index: dict[tuple, dict] = {}
        for row in raw_rows:
            try:
                mn = int(row.get('mn', 0))
                onset_str = row.get('mn_onset', '0')
                # onset may be a fraction string like "1/2"
                if '/' in onset_str:
                    num, den = onset_str.split('/')
                    onset = float(num) / float(den)
                else:
                    onset = float(onset_str)
                raw_index[(mn, round(onset, 6))] = row
            except Exception:
                pass

        direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions)

        for result in direct:
            if result.category != 'dcml_disagree':
                continue
            our_region = result.ours
            dcml_region = result.dcml  # the matched DCML annotation

            our_key_str = getattr(our_region, 'key', '') or ''
            our_mode = _our_mode(our_key_str)

            # Retrieve globalkey from raw TSV via measure+beat lookup
            # dcml_region has .measure_number and .beat (beat number, 1-based quarter notes)
            dcml_mn = dcml_region.measure_number if dcml_region else None
            dcml_beat = dcml_region.beat if dcml_region else None

            dcml_globalkey = ''
            dcml_localkey  = ''
            if dcml_mn is not None and dcml_beat is not None:
                # beat is 1-based quarter-beat count; mn_onset in TSV is 0-based quarter beats
                onset = dcml_beat - 1.0
                raw = raw_index.get((dcml_mn, round(onset, 6)))
                if raw is None:
                    # Try nearest onset within 0.5 qb
                    for (mn2, on2), r2 in raw_index.items():
                        if mn2 == dcml_mn and abs(on2 - onset) <= 0.5:
                            raw = r2
                            break
                if raw:
                    dcml_globalkey = raw.get('globalkey', '')
                    dcml_localkey  = raw.get('localkey', '')

            gk_mode = _dcml_globalkey_mode(dcml_globalkey)
            disagree_rows.append((stem, our_mode, gk_mode, dcml_globalkey, dcml_localkey))

    total_disagree = len(disagree_rows)
    print(f"Total disagreeing aligned regions: {total_disagree}\n")

    # ── Table 1: our_mode × dcml_globalkey_mode ──────────────────────────────
    cross: Counter = Counter()
    for _, our_mode, gk_mode, _, _ in disagree_rows:
        cross[(our_mode, gk_mode)] += 1

    our_modes  = sorted({r[0] for r in cross}, key=lambda m: -sum(v for (om, _), v in cross.items() if om == m))
    gk_modes   = ['Major', 'Minor', 'Unknown']

    col_w = 16
    header = f"{'our_mode':<18}" + "".join(f"{g:>{col_w}}" for g in gk_modes) + f"{'TOTAL':>{col_w}}"
    print("Table 1 — Disagreements: our mode vs DCML global key mode")
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for om in our_modes:
        row_total = sum(cross[(om, g)] for g in gk_modes)
        if row_total == 0:
            continue
        row = f"{om:<18}" + "".join(f"{cross[(om, g)]:>{col_w}}" for g in gk_modes) + f"{row_total:>{col_w}}"
        print(row)
    print("-" * len(header))
    col_totals = [sum(cross[(om, g)] for om in our_modes) for g in gk_modes]
    print(f"{'TOTAL':<18}" + "".join(f"{t:>{col_w}}" for t in col_totals) + f"{total_disagree:>{col_w}}")
    print()

    # ── Table 2: specific false-positive counts ───────────────────────────────
    lyd_vs_major  = cross[('Lydian',    'Major')]
    mix_vs_major  = cross[('Mixolydian','Major')]
    dor_vs_major  = cross[('Dorian',    'Major')]
    lyd_vs_minor  = cross[('Lydian',    'Minor')]
    mix_vs_minor  = cross[('Mixolydian','Minor')]
    dor_vs_minor  = cross[('Dorian',    'Minor')]

    print("Table 2 — Key false-positive counts")
    print(f"  We say Lydian,     DCML says Major : {lyd_vs_major:4d}")
    print(f"  We say Lydian,     DCML says Minor : {lyd_vs_minor:4d}")
    print(f"  We say Mixolydian, DCML says Major : {mix_vs_major:4d}")
    print(f"  We say Mixolydian, DCML says Minor : {mix_vs_minor:4d}")
    print(f"  We say Dorian,     DCML says Major : {dor_vs_major:4d}")
    print(f"  We say Dorian,     DCML says Minor : {dor_vs_minor:4d}")
    lyd_fp_rate = lyd_vs_major / cross[('Lydian', 'Major')] if cross[('Lydian', 'Major')] else 0
    print()

    # ── Table 3: per-piece modal false-positive concentration ─────────────────
    # "modal FP" = our mode is Lydian/Mixolydian/Dorian AND dcml_gk is Major or Minor
    # (i.e. we detected a non-Ionian diatonic mode but DCML uses a plain key)
    target_modes = {'Lydian', 'Mixolydian', 'Dorian', 'Phrygian'}
    piece_fp: Counter = Counter()
    piece_total: Counter = Counter()
    for stem, our_mode, gk_mode, _, _ in disagree_rows:
        piece_total[stem] += 1
        if our_mode in target_modes and gk_mode in ('Major', 'Minor'):
            piece_fp[stem] += 1

    print("Table 3 — Per-piece modal false-positive concentration")
    print("  (modal FP = we say Lydian/Mixolydian/Dorian/Phrygian, DCML says plain Major/Minor)")
    header3 = f"  {'piece':<20} {'modal_FP':>10} {'total_dis':>10} {'FP%':>8}"
    print(header3)
    print("  " + "-" * (len(header3) - 2))
    # Sort by modal_FP count desc, then by piece name
    for stem in sorted(piece_total, key=lambda s: (-piece_fp[s], s)):
        fp  = piece_fp[stem]
        tot = piece_total[stem]
        pct = 100 * fp / tot if tot else 0
        if fp > 0:
            print(f"  {stem:<20} {fp:>10} {tot:>10} {pct:>7.0f}%")
    print()

    # ── Summary ───────────────────────────────────────────────────────────────
    total_modal_fp = sum(piece_fp.values())
    print(f"Summary")
    print(f"  Total disagreements          : {total_disagree}")
    fp_pct = f"{100*total_modal_fp/total_disagree:.1f}%" if total_disagree else "n/a"
    print(f"  Modal false positives total  : {total_modal_fp}  ({fp_pct} of disagree)")
    pieces_with_fp = sum(1 for v in piece_fp.values() if v > 0)
    print(f"  Pieces with >=1 modal FP     : {pieces_with_fp}/{len(piece_total)}")
    if piece_fp:
        top_stem, top_count = piece_fp.most_common(1)[0]
        print(f"  Highest concentration        : {top_stem} ({top_count} modal FPs / {piece_total[top_stem]} total)")


if __name__ == "__main__":
    main()
