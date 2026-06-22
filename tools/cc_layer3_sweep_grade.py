#!/usr/bin/env python3
"""BOUNDED L3 SWEEP — region-level tradeoff grader (READ-ONLY).

Grades a decoder corpus against the held-out WiR ground truth at REGION granularity,
split by GT stable (loc==global) vs modulation (loc!=global), and (optionally) diffs a
swept corpus against a baseline corpus to quantify the B-vs-C tradeoff:

  B recovered      = GT-modulation regions wrong@baseline -> correct@swept
  C newly-wrong    = GT-stable     regions correct@baseline -> wrong@swept   (the cost of lowering)
  (also the reverse flows, for completeness)

Slicing is independent of KeyModeSequencePreferences, so a swept regen has IDENTICAL
slices/start_ticks; regions are keyed by (stem, start_tick). Reuses the committed harness
internals verbatim (our_key_tonic_fixed / _dcml_key_tonic / align_dcml_regions / split_of).

Usage:
  python tools/cc_layer3_sweep_grade.py --decode-dir <dir> [--baseline-dir <dir>] \
         [--preset baroque jazz] [--json out.json]
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import cc_layer3_keymode_baseline as H  # noqa
import compare_rn as C  # noqa
import compare_analyses as cmp  # noqa
import dcml_parser as dcml  # noqa


def grade_dir(decode_dir: Path, wir_base, preset: str, test_pct: int):
    """Return {(stem,start_tick): {'correct':bool,'modulation':bool,'carried':bool}}
    over scorable TEST-split regions, plus aggregate counts."""
    d = Path(decode_dir) / preset
    out = {}
    agg = Counter()
    if not d.is_dir():
        return out, agg
    for p in sorted(d.glob("*.decode.json")):
        stem = p.name[:-len(".decode.json")]
        if H.split_of(stem, test_pct) != 'test':
            continue
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            data, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue
        matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        for ours_r, dr in zip(ours_regions, matches):
            if dr is None:
                continue
            otc, omaj = H.our_key_tonic_fixed(getattr(ours_r, 'key', None))
            ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
            gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))
            if otc is None or ltc is None:
                continue
            our = (otc, omaj)
            loc = (ltc, lmaj)
            modulation = (gtc is not None and loc != (gtc, gmaj))
            correct = (our == loc)
            carried = False
            if not correct:
                for a in (getattr(ours_r, 'alternatives', []) or []):
                    if isinstance(a, dict):
                        at, am = H.our_key_tonic_fixed(a.get('key'))
                        if (at, am) == loc:
                            carried = True
                            break
            st = int(getattr(ours_r, 'start_tick', 0))
            out[(stem, st)] = {'correct': correct, 'modulation': modulation, 'carried': carried}
            agg['regions'] += 1
            agg['correct'] += int(correct)
            agg['stable'] += int(not modulation)
            agg['modulation'] += int(modulation)
            agg['stable_correct'] += int((not modulation) and correct)
            agg['modulation_correct'] += int(modulation and correct)
    return out, agg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decode-dir", required=True)
    ap.add_argument("--baseline-dir", default=None)
    ap.add_argument("--wir-base", default=str(H.C.WIR_BASE_DEFAULT))
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz"])
    ap.add_argument("--test-pct", type=int, default=H.TEST_PCT_DEFAULT)
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    result = {}
    for preset in args.presets:
        cur, agg = grade_dir(Path(args.decode_dir), args.wir_base, preset, args.test_pct)
        row = {'regions': agg['regions'], 'correct': agg['correct'],
               'acc': round(100.0 * agg['correct'] / max(1, agg['regions']), 2),
               'stable': agg['stable'], 'stable_correct': agg['stable_correct'],
               'stable_acc': round(100.0 * agg['stable_correct'] / max(1, agg['stable']), 2),
               'modulation': agg['modulation'], 'modulation_correct': agg['modulation_correct'],
               'mod_acc': round(100.0 * agg['modulation_correct'] / max(1, agg['modulation']), 2)}
        print(f"== {preset} ==  regions={row['regions']} acc={row['acc']}%  "
              f"stable {row['stable_correct']}/{row['stable']} ({row['stable_acc']}%)  "
              f"mod {row['modulation_correct']}/{row['modulation']} ({row['mod_acc']}%)")
        if args.baseline_dir:
            base, _ = grade_dir(Path(args.baseline_dir), args.wir_base, preset, args.test_pct)
            flows = Counter()
            for k, cv in cur.items():
                bv = base.get(k)
                if bv is None:
                    continue
                if bv['correct'] == cv['correct']:
                    continue
                # changed
                bucket = ('mod' if cv['modulation'] else 'stab')
                if cv['correct']:   # wrong -> correct (recovered)
                    flows[f'{bucket}_recovered'] += 1
                else:               # correct -> wrong (damaged)
                    flows[f'{bucket}_damaged'] += 1
            B_recovered = flows['mod_recovered']
            C_damaged = flows['stab_damaged']
            stab_rec = flows['stab_recovered']
            mod_dam = flows['mod_damaged']
            net = (B_recovered + stab_rec) - (C_damaged + mod_dam)
            print(f"    vs baseline:  B(mod) recovered={B_recovered}  C(stable) damaged={C_damaged}"
                  f"  | stable recovered={stab_rec}  mod damaged={mod_dam}  NET={net:+d}")
            row['tradeoff'] = {'B_mod_recovered': B_recovered, 'C_stable_damaged': C_damaged,
                               'stable_recovered': stab_rec, 'mod_damaged': mod_dam, 'net': net}
        result[preset] = row

    if args.json:
        Path(args.json).write_text(json.dumps(result, indent=2))
        print(f"[wrote] {args.json}")


if __name__ == "__main__":
    main()
