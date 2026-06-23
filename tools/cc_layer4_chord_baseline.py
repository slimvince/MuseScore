#!/usr/bin/env python3
"""Layer-4 (Increment A) per-slice CHORD decoder — held-out grading harness.

Grades the isolated Layer-4 per-slice chord decoder (the --decode-chords diagnostic,
collected by decode_chord_corpus.py) against the held-out When-in-Rome ground truth,
per preset, on the deterministic md5(stem)%100<test_pct test split — and reports it
DIRECTIONALLY against the per-region baseline (the live analyzer's *.ours.json), both
graded the SAME way (one grading path, extended not forked). Two metrics:

  (1) CHORD-ROOT  — does the chord's root pitch class match the GT chord's root?
      Reuses cmp.load_analysis + cmp.align_dcml_regions (the chord-root graders'
      substrate); GT root + chord-tones come from music21's RomanNumeral parse of the
      SAME WiR annotation the project's metric uses (root() and pitchClasses), the
      coherent single source for both metrics. Per-region (baseline) vs per-slice
      (decoder), so the DURATION-WEIGHTED match is the comparable line.

  (2) NCT MEMBERSHIP (NEW; spec §10) — per sounding note, did the analyzer correctly
      call it a chord-tone vs a non-chord-tone, vs the GT chord-tone set? This metric
      did NOT exist before. INCREMENT A reports the TRIVIAL baseline: the decoder calls
      NO note an NCT (membership is stubbed for Increment B), so every sounding note is
      implicitly a chord tone — NCT recall is 0 and CT precision (fraction of sounding
      notes that ARE GT chord-tones) is exactly the over-read headroom the Increment-B
      membership decision will recover.

Diagnostic-only / read-only: it reads JSON the --decode-chords path emitted (which
returns before any analysis), never touches production. Mirrors
cc_layer3_keymode_baseline.py.

Usage:
    # 1) collect the decoder JSON (both presets):
    python tools/decode_chord_corpus.py --preset Baroque --out tools/corpus_decode_chord
    python tools/decode_chord_corpus.py --preset Jazz    --out tools/corpus_decode_chord
    # 2) grade (decoder vs per-region baseline, held-out):
    python tools/cc_layer4_chord_baseline.py --decode-dir tools/corpus_decode_chord \
        --corpus-root tools/corpus --presets baroque jazz
"""
import argparse
import hashlib
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp     # load_analysis, align_dcml_regions, DEFAULT_DCML_MATCH_MODE
import compare_rn as C             # WIR_BASE_DEFAULT
import dcml_parser as dcml         # find_wir_file, parse_rntxt_file

TEST_PCT_DEFAULT = 20


def split_of(stem: str, test_pct: int) -> str:
    """Deterministic, reproducible train/test partition by stem (the project rule)."""
    h = int(hashlib.md5(stem.encode('utf-8')).hexdigest(), 16)
    return 'test' if (h % 100) < test_pct else 'train'


# ── GT chord (root + chord-tone set) per event, from music21's RomanNumeral parse ──
_M21_CT_CACHE: dict = {}


def m21_chordtone_index(wir_path: str):
    """('ok', {(measureNumber, round(beat,3)): (root_pc, frozenset(chord_tone_pcs))})
    or ('fail', msg). The RomanNumeral is a music21 Chord subclass, so .root() gives the
    GT root pc and .pitchClasses the GT chord-tone set — the coherent single GT source for
    both the root metric and the membership metric. Cached per path (both presets reuse
    the same WiR files)."""
    if wir_path in _M21_CT_CACHE:
        return _M21_CT_CACHE[wir_path]
    try:
        from music21 import converter, roman
        score = converter.parse(wir_path, format='romanText')
        idx: dict = {}
        for rn in score.recurse().getElementsByClass(roman.RomanNumeral):
            try:
                root_pc = int(rn.root().pitchClass)
                cts = frozenset(int(p) for p in rn.pitchClasses)
                idx[(rn.measureNumber, round(float(rn.beat), 3))] = (root_pc, cts)
            except Exception:
                continue
        res = ('ok', idx)
    except Exception as exc:
        res = ('fail', f"{type(exc).__name__}: {exc}")
    _M21_CT_CACHE[wir_path] = res
    return res


def _gt_at(dr, m21_idx):
    """The GT (root_pc, chord_tone_set) for the event a DcmlRegion sits on, or None."""
    if m21_idx is None:
        return None
    key = (int(getattr(dr, 'measure_number', -1)), round(float(getattr(dr, 'beat', -1.0)), 3))
    return m21_idx.get(key)


# ══════════════════════════════════════════════════════════════════════════
# (1) Chord-root tally
# ══════════════════════════════════════════════════════════════════════════
class RootTally:
    def __init__(self):
        self.pieces = 0
        self.aligned = 0          # our region aligned to a DCML region
        self.gt_present = 0       # ... and a music21 GT chord exists at that event
        self.scorable = 0         # ... and both roots are known
        self.our_rootfail = 0
        self.gt_rootfail = 0
        self.root_match = 0
        self.dur_scorable = 0
        self.dur_root_match = 0
        self.miss = Counter()     # (our_root, gt_root) -> count

    def add(self, o):
        for k, v in self.__dict__.items():
            if isinstance(v, Counter):
                v.update(o.__dict__[k])
            else:
                self.__dict__[k] += o.__dict__[k]


def score_root(regions, wir_regions, m21_idx) -> RootTally:
    t = RootTally()
    t.pieces = 1
    matches = cmp.align_dcml_regions(regions, wir_regions, mode=cmp.DEFAULT_DCML_MATCH_MODE)
    for r, dr in zip(regions, matches):
        if dr is None:
            continue
        t.aligned += 1
        gt = _gt_at(dr, m21_idx)
        if gt is None:
            continue
        t.gt_present += 1
        gt_root, _ = gt
        dur = max(0, int(getattr(r, 'end_tick', 0)) - int(getattr(r, 'start_tick', 0)))
        our_root = getattr(r, 'root_pc', -1)
        if our_root is None or our_root < 0:
            t.our_rootfail += 1
            continue
        if gt_root is None:
            t.gt_rootfail += 1
            continue
        t.scorable += 1
        t.dur_scorable += dur
        if our_root == gt_root:
            t.root_match += 1
            t.dur_root_match += dur
        else:
            t.miss[(our_root, gt_root)] += 1
    return t


# ══════════════════════════════════════════════════════════════════════════
# (2) NCT-membership tally (per sounding note)
# ══════════════════════════════════════════════════════════════════════════
class MembTally:
    def __init__(self):
        self.slices = 0       # slices with sounding notes AND a GT chord
        self.notes = 0        # sounding notes scored
        self.gt_ct = 0        # notes whose GT label is chord-tone
        self.gt_nct = 0       # notes whose GT label is non-chord-tone (the real NCTs)
        # CT (chord-tone) as the positive class
        self.ct_tp = 0
        self.ct_fp = 0
        self.ct_fn = 0
        # NCT (non-chord-tone) as the positive class
        self.nct_tp = 0
        self.nct_fp = 0
        self.nct_fn = 0

    def add(self, o):
        for k in self.__dict__:
            self.__dict__[k] += o.__dict__[k]


def score_membership(regions, raw_regions, wir_regions, m21_idx) -> MembTally:
    t = MembTally()
    matches = cmp.align_dcml_regions(regions, wir_regions, mode=cmp.DEFAULT_DCML_MATCH_MODE)
    for r, raw, dr in zip(regions, raw_regions, matches):
        if dr is None:
            continue
        gt = _gt_at(dr, m21_idx)
        if gt is None:
            continue
        _, gt_ct = gt
        sounding = raw.get('soundingPitchClasses')
        if not sounding:
            continue
        nc = raw.get('noteClassifications') or {}
        called_nct = set(nc.get('nonChordTones') or [])   # Increment A: empty
        t.slices += 1
        for pc in sounding:
            t.notes += 1
            is_gt_ct = (pc in gt_ct)
            called_ct = (pc not in called_nct)            # not called NCT ⇒ implicitly CT
            if is_gt_ct:
                t.gt_ct += 1
            else:
                t.gt_nct += 1
            # CT positive class
            if called_ct and is_gt_ct:
                t.ct_tp += 1
            elif called_ct and not is_gt_ct:
                t.ct_fp += 1
            elif (not called_ct) and is_gt_ct:
                t.ct_fn += 1
            # NCT positive class
            if (not called_ct) and (not is_gt_ct):
                t.nct_tp += 1
            elif (not called_ct) and is_gt_ct:
                t.nct_fp += 1
            elif called_ct and (not is_gt_ct):
                t.nct_fn += 1
    return t


# ══════════════════════════════════════════════════════════════════════════
# Corpus scoring
# ══════════════════════════════════════════════════════════════════════════
def score_corpus(src_dir: Path, wir_base: Path, test_pct: int, suffix: str,
                 want_membership: bool):
    """src_dir holds <stem><suffix> files. Returns
    (root_splits, memb_splits, meta) where each *_splits is split -> Tally."""
    root_splits = {'train': RootTally(), 'test': RootTally(), 'all': RootTally()}
    memb_splits = {'train': MembTally(), 'test': MembTally(), 'all': MembTally()}
    total = covered = m21_ok = 0
    for p in sorted(src_dir.glob("*" + suffix)):
        total += 1
        stem = p.name[:-len(suffix)]
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            data, regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not regions or not wir_regions:
            continue
        status, m21_idx = m21_chordtone_index(wir_path)
        if status != 'ok':
            m21_idx = None
        else:
            m21_ok += 1
        if m21_idx is None:
            continue                       # no GT chords → cannot grade root or membership
        covered += 1
        sp = split_of(stem, test_pct)

        rt = score_root(regions, wir_regions, m21_idx)
        root_splits[sp].add(rt)
        root_splits['all'].add(rt)

        if want_membership:
            raw = data.get("regions", [])
            mt = score_membership(regions, raw, wir_regions, m21_idx)
            memb_splits[sp].add(mt)
            memb_splits['all'].add(mt)

    meta = {'total': total, 'covered': covered, 'm21_ok': m21_ok}
    return root_splits, memb_splits, meta


def _pct(n, d):
    return (100.0 * n / d) if d else 0.0


def _prec(tp, fp):
    d = tp + fp
    return (100.0 * tp / d) if d else None


def _rec(tp, fn):
    d = tp + fn
    return (100.0 * tp / d) if d else None


def _fmtpct(x):
    return f"{x:5.1f}%" if x is not None else "  N/A"


# ══════════════════════════════════════════════════════════════════════════
# Reports
# ══════════════════════════════════════════════════════════════════════════
def root_directional(preset, base_splits, dec_splits, base_meta, dec_meta, test_pct):
    bt, dt = base_splits['test'], dec_splits['test']
    L = []
    L.append("=" * 84)
    L.append(f"CHORD-ROOT (held-out, TEST split, out-of-sample) — {preset}")
    L.append("=" * 84)
    L.append(f"  WiR-covered stems: baseline {base_meta['covered']}/{base_meta['total']}, "
             f"decoder {dec_meta['covered']}/{dec_meta['total']}   "
             f"(held-out split: md5(stem)%100 < {test_pct} = test)")
    L.append("")
    L.append(f"  root-pc match (region-count):")
    L.append(f"     per-region baseline : {_pct(bt.root_match, bt.scorable):5.1f}%  "
             f"({bt.root_match}/{bt.scorable})")
    L.append(f"     per-slice  decoder  : {_pct(dt.root_match, dt.scorable):5.1f}%  "
             f"({dt.root_match}/{dt.scorable})")
    L.append(f"  root-pc match (DURATION-weighted — the comparable line across granularity):")
    L.append(f"     per-region baseline : {_pct(bt.dur_root_match, bt.dur_scorable):5.1f}%")
    L.append(f"     per-slice  decoder  : {_pct(dt.dur_root_match, dt.dur_scorable):5.1f}%")
    L.append(f"  Δ dur-weighted (decoder − baseline): "
             f"{_pct(dt.dur_root_match, dt.dur_scorable) - _pct(bt.dur_root_match, bt.dur_scorable):+.1f} pts "
             f"(Increment B: does per-slice + membership now MEET/BEAT the per-region baseline?)")
    L.append(f"  decoder top root misses (our->gt): "
             + ", ".join(f"{o}->{d}:{n}" for (o, d), n in dt.miss.most_common(6)))
    return "\n".join(L)


def membership_report(preset, memb_splits, test_pct):
    t = memb_splits['test']
    L = []
    L.append("=" * 84)
    L.append(f"NCT MEMBERSHIP (held-out, TEST split) — {preset}   [Increment B: per-note CT/NCT]")
    L.append("=" * 84)
    L.append(f"  scored: {t.notes} sounding (slice,pc) over {t.slices} slices "
             f"(GT chord-tones {t.gt_ct}, GT non-chord-tones {t.gt_nct})")
    L.append(f"     NCT  precision : {_fmtpct(_prec(t.nct_tp, t.nct_fp))}  "
             f"(tp {t.nct_tp}, fp {t.nct_fp})   ◀ of the notes we CALL non-chord, how many are")
    L.append(f"     NCT  recall    : {_fmtpct(_rec(t.nct_tp, t.nct_fn))}  "
             f"(tp {t.nct_tp}, fn {t.nct_fn})   ◀ of the true non-chord tones, how many we catch")
    L.append(f"     CT   precision : {_fmtpct(_prec(t.ct_tp, t.ct_fp))}  "
             f"(tp {t.ct_tp}, fp {t.ct_fp})   ◀ 1 − (residual over-read)")
    L.append(f"     CT   recall    : {_fmtpct(_rec(t.ct_tp, t.ct_fn))}  "
             f"(tp {t.ct_tp}, fn {t.ct_fn})   ◀ true chord tones we did NOT wrongly drop")
    L.append(f"  over-read rate (sounding notes that are GT non-chord-tones): "
             f"{_pct(t.gt_nct, t.notes):.1f}%  ({t.gt_nct}/{t.notes})")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decode-dir", required=True,
                    help="root of the decoder JSON (decode_chord_corpus.py --out); "
                         "<decode-dir>/<preset>/<stem>.decode.json")
    ap.add_argument("--corpus-root", default=str(Path(__file__).resolve().parent / "corpus"),
                    help="root of the per-region baseline (<corpus-root>/<preset>/<stem>.ours.json)")
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz"])
    ap.add_argument("--wir-base", default=C.WIR_BASE_DEFAULT)
    ap.add_argument("--test-pct", type=int, default=TEST_PCT_DEFAULT)
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    decode_root = Path(args.decode_dir)
    corpus_root = Path(args.corpus_root)
    wir = Path(args.wir_base)

    for preset in args.presets:
        dec_dir = decode_root / preset
        base_dir = corpus_root / preset
        if not dec_dir.is_dir():
            print(f"[skip] decoder dir {dec_dir} not found")
            continue
        dec_root, dec_memb, dec_meta = score_corpus(
            dec_dir, wir, args.test_pct, ".decode.json", want_membership=True)
        if base_dir.is_dir():
            base_root, _, base_meta = score_corpus(
                base_dir, wir, args.test_pct, ".ours.json", want_membership=False)
        else:
            print(f"[note] baseline dir {base_dir} not found — root directional skipped")
            base_root, base_meta = {'test': RootTally(), 'train': RootTally(), 'all': RootTally()}, \
                {'total': 0, 'covered': 0, 'm21_ok': 0}

        print(root_directional(preset, base_root, dec_root, base_meta, dec_meta, args.test_pct))
        print()
        print(membership_report(preset, dec_memb, args.test_pct))
        print()


if __name__ == "__main__":
    main()
