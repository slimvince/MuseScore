#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_content_dp_split.py — OI-206 / cc_instruction_analysis_cost_profile.md Task 1: the MANDATORY
content-scoring-vs-dynamic-program split WITHIN the decode (phase 3).

★ WHY THIS EXISTS. The dispatch requires phase 3 (decodePiece) to be split into:
  (a) SEGMENT CONTENT SCORING — the per-segment, per-(key, class) scoring that depends ONLY on the
      segment's own contents and position (probe_decoder.score_segment_content), and
  (b) THE DYNAMIC PROGRAM — the transition + path machinery that COUPLES segments across the piece
      (the semi-Markov Viterbi recursion, candidate generation, the top-K key prune, the transition
      factors entry/key_trans/chord_trans, and the backtrack).
This split decides whether INCREMENTAL PATCHING (extent: whole-piece; frequency: once-then-patch) is
viable. Content scores are position-local and PROVEN reusable across overlapping windows (the OI-206
window study memoized them by (stem, span, key, class, pcset), memo-ON == memo-OFF byte-identical). If
content dominates, incremental patching is promising; if the coupled DP dominates, it is not, and the
extent axis is where the cost must be paid.

★ HOW (#19). The C++ decodePiece is a single src/ call this READ-ONLY instrument may not carve. So the
split is measured on the BYTE-IDENTICAL Python reference decoder (probe_decoder.decode_piece), whose
whole-piece decode is established equal to the committed decode_parity_ref.json (a mismatch is a #13
STOP). We wrap probe_decoder.score_segment_content with a cumulative-time accumulator (decode_piece's
`content()` closure resolves the module global at call time — the same interception the window study
uses), so content time is the sum of the real score_segment_content calls, and DP time = total − content.
This is the CHORALE-envelope shape (the reference decoder runs only on the 326 note_events pieces). The
C++ decode is timed AS A WHOLE per score by pipeline_snapshot_tests LargeScoreDecodeProfile; how the
content/DP FRACTION transfers beyond the chorale envelope is stated as an open question, never asserted.

★ ESTABLISHMENT. Before the split is trusted: for each measured piece the whole-piece decode's committed
segments (i, j, tonic, is_major, class_key) + total_score must reproduce decode_parity_ref.json (the
wrapper only times; the returned value is the real decode). A mismatch STOPs the piece and the run
reports it.

Artifact (#17f): tools/joint_estimator/content_dp_split.json + a printed summary. Read-only (imports the
pinned decoder + parity ref; touches no production code, no golden, no corpus, no tools/robust_stop/).

Usage:
    python tools/joint_estimator/gen_content_dp_split.py                 # every-3rd sample, write
    python tools/joint_estimator/gen_content_dp_split.py --stride 1      # full corpus (slow)
    python tools/joint_estimator/gen_content_dp_split.py --stems bwv269  # subset dry-run (no write)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import probe_decoder as pd   # noqa: E402  the pinned production decoder — IMPORT-ONLY

SEG_CAP = 4
LEFTOVER = "freq"


# ── the content-time accumulator: wrap score_segment_content, sum its self-time ──
class ContentTimer:
    def __init__(self):
        self._orig = pd.score_segment_content
        self.total = 0.0
        self.calls = 0

    def install(self):
        orig = self._orig

        def wrapper(*a, **k):
            t0 = time.perf_counter()
            r = orig(*a, **k)
            self.total += time.perf_counter() - t0
            self.calls += 1
            return r
        pd.score_segment_content = wrapper

    def reset(self):
        self.total = 0.0
        self.calls = 0

    def uninstall(self):
        pd.score_segment_content = self._orig


def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
                                       cwd=str(_HERE)).decode().strip()
    except Exception:
        return "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stride", type=int, default=3, help="sample every Nth name-sorted stem (default 3)")
    ap.add_argument("--stems", nargs="*", default=None, help="explicit stems (dry-run, no write)")
    ap.add_argument("--out", default=str(_HERE / "content_dp_split.json"))
    args = ap.parse_args()

    parity = json.loads((_HERE / "decode_parity_ref.json").read_text(encoding="utf-8"))
    sel_weights = parity["selected_weights"]
    parity_sel = parity["selected"]

    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=sel_weights)
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()

    all_stems = sorted(pieces.keys())
    if args.stems:
        stems = [s for s in args.stems if s in pieces]
    else:
        stems = all_stems[::args.stride]
    write = args.stems is None

    timer = ContentTimer()
    timer.install()

    rows = []
    stops = []
    for stem in stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        timer.reset()
        t0 = time.perf_counter()
        res = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP,
                              sig_fifths=sig, declared_mode=dm)
        total = time.perf_counter() - t0
        content = timer.total
        dp = total - content

        # establishment: the committed segments + total_score must match decode_parity_ref
        est_ok = True
        est_detail = ""
        if stem in parity_sel:
            # res.segments are dicts (i, j, tonic_pc, is_major, class_key, ...); parity segments are
            # lists [i, j, tonic, is_major, class_key, seg_len].
            got = [(s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"]) for s in res.segments]
            exp = [(seg[0], seg[1], seg[2], seg[3], seg[4]) for seg in parity_sel[stem]["segments"]]
            score_ok = abs(res.total_score - parity_sel[stem]["total_score"]) < 1e-9
            est_ok = (got == exp) and score_ok
            if not est_ok:
                est_detail = f"seg_match={got == exp} score_ok={score_ok}"
                stops.append({"stem": stem, "detail": est_detail})

        rows.append({
            "stem": stem,
            "n_events": len(piece.events),
            "n_segments": len(res.segments),
            "content_calls": timer.calls,
            "total_s": total,
            "content_s": content,
            "dp_s": dp,
            "content_frac": (content / total) if total > 0 else None,
            "establishment_ok": est_ok,
            "establishment_detail": est_detail,
        })
        print(f"{stem:14s} ev={len(piece.events):4d} total={total:7.3f}s "
              f"content={content:7.3f}s ({100*content/total:4.1f}%) dp={dp:7.3f}s "
              f"calls={timer.calls} est={'ok' if est_ok else 'STOP'}", flush=True)

    timer.uninstall()

    if stops:
        print(f"\nSTOP (#13): {len(stops)} piece(s) did not reproduce decode_parity_ref — the split is "
              f"NOT on the production decode for them: {stops[:3]}", file=sys.stderr)

    # aggregates
    ok_rows = [r for r in rows if r["establishment_ok"] and r["total_s"] > 0]
    tot_total = sum(r["total_s"] for r in ok_rows)
    tot_content = sum(r["content_s"] for r in ok_rows)
    agg = {
        "n_pieces": len(ok_rows),
        "sum_total_s": tot_total,
        "sum_content_s": tot_content,
        "sum_dp_s": tot_total - tot_content,
        "content_frac_pooled": (tot_content / tot_total) if tot_total > 0 else None,
        "content_frac_mean_of_pieces": (sum(r["content_frac"] for r in ok_rows) / len(ok_rows))
        if ok_rows else None,
        "content_frac_min": min((r["content_frac"] for r in ok_rows), default=None),
        "content_frac_max": max((r["content_frac"] for r in ok_rows), default=None),
    }

    out = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_content_dp_split.py",
            "instrument_commit": git_hash(),
            "open_item": "OI-206 / cc_instruction_analysis_cost_profile.md Task 1 (content vs DP split)",
            "decoder": "tools/joint_estimator/probe_decoder.py decode_piece (pinned; import-only, byte-identical to C++ decodePiece)",
            "seg_cap": SEG_CAP,
            "leftover": LEFTOVER,
            "split_definition": {
                "content_s": "cumulative wall time inside probe_decoder.score_segment_content (the per-segment, per-(key,class) position-local scoring)",
                "dp_s": "decode_piece total minus content_s (the semi-Markov Viterbi recursion + candidate generation + top-K key prune + transition factors + backtrack — the segment-coupling machinery)",
            },
            "caveat": "PYTHON reference decoder timing on the CHORALE envelope (the reference decoder runs only on the 326 note_events pieces). It gives the content/DP FRACTION, established byte-identical to the C++ decode; the C++ absolute decode time is tools/notation_seams/large_score_decode_profile.json. Whether the fraction transfers beyond the chorale envelope is an OPEN question, not asserted.",
            "coverage": f"every-{args.stride}rd name-sorted stem = {len(stems)} of {len(all_stems)} pieces" if write else f"explicit stems: {stems}",
            "establishment": "each piece's whole-piece decode reproduces decode_parity_ref.json committed segments + total_score (a mismatch is a #13 STOP and excluded from the aggregate)",
        },
        "aggregate": agg,
        "stops": stops,
        "pieces": rows,
    }

    if write:
        Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                  encoding="utf-8")
        print(f"\nwrote {args.out}")
    print(f"\nAGGREGATE (n={agg['n_pieces']}): content pooled = "
          f"{100*(agg['content_frac_pooled'] or 0):.1f}%  DP = "
          f"{100*(1-(agg['content_frac_pooled'] or 0)):.1f}%  "
          f"(per-piece content frac range {100*(agg['content_frac_min'] or 0):.1f}"
          f"-{100*(agg['content_frac_max'] or 0):.1f}%)")


if __name__ == "__main__":
    main()
